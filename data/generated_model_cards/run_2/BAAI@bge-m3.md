## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The M3-Embedding model was developed by a team of researchers from the Beijing Academy of Artificial Intelligence (BAAI) and the University of Science and Technology of China (USTC). The developers are Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu (Paper, p. 1).

### Model date:
The academic paper introducing the model was submitted to arXiv with its latest version (v4) dated June 28, 2024 (Paper, p. 1).

### Model version:
The model card is based on version 4 of the research paper (arXiv:2402.03216v4) (Paper, p. 1). This model is distinguished from previous embedding models by its versatility across three dimensions:
*   **Multi-Linguality:** It supports over 100 languages, whereas most existing models are tailored for English (Paper, p. 1).
*   **Multi-Functionality:** It unifies three common retrieval functionalities (dense, sparse, and multi-vector) into a single model, which are typically handled by separate models (Paper, p. 1, 3).
*   **Multi-Granularity:** It can process inputs up to 8,192 tokens, a significant increase over many models that only support short inputs (Paper, p. 1).

### Model type:
M3-Embedding is a versatile text embedding model designed for information retrieval tasks (Paper, p. 1).

*   **Architecture:** The model's architecture is based on an XLM-ROBERTa text encoder, which was further adapted using the RetroMAE (masked auto-encoder) method (Paper, p. 5, 9). The core architecture is a Transformer model with the following specifications:
    *   Model Type: `xlm-roberta` (config.json)
    *   Hidden Layers: 24 (config.json)
    *   Hidden Size: 1024 (config.json)
    *   Attention Heads: 16 (config.json)
*   **Size:** The model has a vocabulary size of 250,002 (config.json).
*   **Context Length:** The model supports a maximum sequence length of 8,192 tokens (Paper, p. 1; config.json).
*   **Functionality:** It generates embeddings that can be used for dense retrieval, sparse (lexical) retrieval, and multi-vector retrieval (Paper, p. 1).

### Training details:
The model was trained using a multi-stage workflow designed to optimize its versatility and performance (Paper, p. 5).

*   **Stage 1: Pre-training:** The foundational text encoder, an XLM-ROBERTa model adapted with the RetroMAE method, was first pre-trained on a massive unsupervised dataset of 1.2 billion multilingual text pairs. In this stage, only the dense retrieval functionality was trained using a basic contrastive learning objective (Paper, p. 5, 14).
*   **Stage 2: Fine-tuning with Self-Knowledge Distillation:** The pre-trained model was then fine-tuned to establish all three retrieval functionalities (dense, sparse, multi-vector). This stage employed a novel **self-knowledge distillation** framework.
    *   **Teacher Signal:** Instead of using an external model, the integrated relevance score from the model's own three retrieval functions (`S_inter = w1 * S_dense + w2 * S_lex + w3 * S_mul`) was used as a "teacher" signal. This allows the multiple retrieval functionalities to be jointly learned and mutually reinforced (Paper, p. 4, 5).
    *   **Loss Function:** The final loss function (`L_final`) is a linear combination of a standard multi-objective InfoNCE loss (`L`) and a modified distillation loss (`L'`) that uses the teacher signal's soft labels. This unified training process helps overcome conflicting objectives between different retrieval methods (Paper, p. 4, 5).
    *   **Parameters:** During training, the weights for combining scores were set to `w1=1`, `w2=0.3`, and `w3=1`. The loss weights were `λ1=1`, `λ2=0.1`, and `λ3=1` to reduce the impact of the randomly initialized sparse retrieval head at the beginning (Paper, p. 5). Hard negative samples were also introduced for each query following the ANCE method (Paper, p. 5).
*   **Efficient Batching Strategy:** To handle diverse and massive multilingual data efficiently, an optimized batching strategy was used:
    1.  Training data was grouped by sequence length to reduce padding and improve GPU utilization.
    2.  For long sequences (e.g., 8192 tokens), mini-batches were split into smaller sub-batches, which were processed iteratively using gradient checkpointing to save memory. This increased the effective batch size by over 20 times for the longest sequences (Paper, p. 5, 16).
    3.  Embeddings from different GPUs were broadcasted across all devices in the distributed environment, significantly expanding the pool of in-batch negative samples to improve the discriminativeness of the learned embeddings (Paper, p. 5).

### Paper or other resource for more information:
*   **Academic Paper:** For a detailed explanation of the model's architecture, training process, and evaluation, refer to the original paper:
    *   Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*. arXiv preprint arXiv:2402.03216v4. (Paper, p. 1)
*   **Repository:** The model, source code, and data are publicly available at the FlagEmbedding GitHub repository:
    *   https://github.com/FlagOpen/FlagEmbedding (Paper, p. 1)

### Citation details:
To cite this model in your work, please use the following BibTeX entry:
```bibtex
@misc{chen2024m3embedding,
      title={M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation}, 
      author={Jianlv Chen and Shitao Xiao and Peitian Zhang and Kun Luo and Defu Lian and Zheng Liu},
      year={2024},
      eprint={2402.03216v4},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(Paper, p. 1)

### License:
The model, code, and data are publicly available (Paper, p. 1). The specific license details can be found in the model's repository.

### Contact:
For questions, feedback, or to report issues, you can contact the developers via the email addresses provided in the academic paper:
*   stxiao@baai.ac.cn
*   {namespace.pt, luokun695, zhengliu1026}@gmail.com
*   chenjianlv@mail.ustc.edu.cn
*   liandefu@ustc.edu.cn
(Paper, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is a general-purpose text embedding model designed for a wide range of semantic retrieval tasks. Its capabilities are built on three core pillars (Paper, p. 1):

1.  **Multi-Lingual Retrieval:** The model supports semantic retrieval in over 100 languages. It can be used for:
    *   **Monolingual Retrieval:** Finding relevant documents in the same language as the query.
    *   **Cross-Lingual Retrieval:** Using a query in one language to retrieve documents in another (e.g., a German query to find English documents).
2.  **Multi-Functional Retrieval:** The model unifies three distinct retrieval methods in a single framework:
    *   **Dense Retrieval:** Encodes text into a single dense vector. Relevance is determined by the similarity (e.g., inner product) between query and document embeddings. This is the most common form of semantic search (Paper, p. 4).
    *   **Sparse (Lexical) Retrieval:** Estimates the importance (weight) of each term (token) in the text. Relevance is calculated based on the joint importance of overlapping terms between the query and document, similar to traditional methods like BM25 but with learned weights (Paper, p. 4).
    *   **Multi-Vector Retrieval:** Represents text as a set of embeddings (one for each token). It computes a fine-grained relevance score using late-interaction between all query and document embeddings, capturing more nuanced relationships (Paper, p. 4).
    *   **Hybrid Retrieval:** The scores from the above methods can be combined in a weighted sum to re-rank candidates, often leading to superior performance (Paper, p. 4).
3.  **Multi-Granularity Retrieval:** The model is capable of processing text inputs of varying lengths, from short sentences and passages up to long documents of 8,192 tokens (Paper, p. 1).

**Input-Output Structure:**
*   **Input:** A string of text (query or document).
*   **Output:** A set of embeddings (hidden states) for each token in the input text.
    *   For **dense retrieval**, the embedding of the `[CLS]` token is typically used as the representation for the entire text (Paper, p. 4).
    *   For **sparse retrieval**, the embeddings are used to compute a scalar weight for each term (Paper, p. 4).
    *   For **multi-vector retrieval**, the full sequence of token embeddings is used (Paper, p. 4).

### Primary intended users:
The primary intended users are researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who need a powerful and versatile tool for building semantic search and retrieval systems across multiple languages and for various document lengths (Paper, p. 2).

### Out-of-scope uses:
The model is specialized for text retrieval and embedding tasks. It is not designed for:
*   **Generative tasks:** It cannot generate text like a large language model (LLM).
*   **Discriminative tasks outside of retrieval:** It is not fine-tuned for tasks like sequence classification, named entity recognition, or other common NLP tasks, though its embeddings could potentially be used as features for them.
*   **Processing documents longer than 8,192 tokens:** The model's performance on inputs exceeding its specified context length has not been investigated and may be suboptimal. Processing extremely long documents could also pose computational challenges (Paper, p. 9).
*   **Guaranteed performance on all languages:** While it supports over 100 languages, performance may vary, especially for low-resource languages, due to the uneven distribution of training data (Paper, p. 9).

---

## How to Use
This section outlines how to use the model.

The model can be used for three different retrieval functionalities, either individually or combined in a hybrid process. The input is a text query `q` and a passage `p`.

**1. Dense Retrieval**
The model transforms the input text into hidden states. The normalized hidden state of the special `[CLS]` token is used as the final embedding. The relevance score is the inner product of the query and passage embeddings.
*   `eq = norm(Hq[0])`
*   `ep = norm(Hp[0])`
*   `S_dense = <ep, eq>`
(Paper, p. 4)

**2. Lexical (Sparse) Retrieval**
The model estimates the importance of each term (token). A learnable matrix `W_lex` maps the hidden state of each token to a float number, and a ReLU activation is applied. The relevance score is the sum of the products of weights for co-existing terms.
*   `w_qt = Relu(W_lex * Hq[i])` for term `t` at position `i` in the query.
*   `S_lex = Σ (w_qt * w_pt)` for all terms `t` in both `q` and `p`.
(Paper, p. 4)

**3. Multi-Vector Retrieval**
This method uses the entire sequence of output embeddings. A learnable projection matrix `W_mul` is applied. A late-interaction mechanism computes the fine-grained relevance score by taking the sum of maximum similarity scores for each query token embedding against all passage token embeddings.
*   `Eq = norm(W_mul * Hq)`
*   `Ep = norm(W_mul * Hp)`
*   `S_mul = (1/N) * Σ_i max_j (Eq[i] * Ep[j])`, where N is the query length.
(Paper, p. 4)

**4. Hybrid Retrieval**
For the best performance, the scores from the individual methods can be combined to re-rank a set of candidate documents.
*   `S_rank = w1 * S_dense + w2 * S_lex + w3 * S_mul`
The weights `w1`, `w2`, and `w3` depend on the downstream task. For example, in the MIRACL evaluation, the weights for combining dense and sparse were `w1=1, w2=0.3, w3=0` (Paper, p. 6). For the MLDR long-document task, weights were `w1=0.15, w2=0.5, w3=0.35` (Paper, p. 8).

**5. MCLS (Multiple CLS) Method for Long Documents**
For users without the resources to fine-tune on long documents, a simple inference-time strategy called MCLS is proposed. This method inserts a `[CLS]` token at fixed intervals (e.g., every 256 tokens) into the long document. The final embedding for the document is the average of the last hidden states of all these `[CLS]` tokens. This significantly improves long-document retrieval performance without any additional training (Paper, p. 6, 8, 14).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is designed to be multilingual, but its performance can vary across different languages. This is influenced by the amount and quality of training data available for each language (Paper, p. 9).
*   **Input Granularity (Text Length):** The model's performance is affected by the length of the input text. It is designed to handle a wide range from short sentences to long documents up to 8,192 tokens, and its effectiveness can differ across this spectrum (Paper, p. 1, 8).
*   **Retrieval Functionality:** The choice of retrieval method (dense, sparse, multi-vector, or a hybrid combination) significantly impacts performance, with different methods being more effective for certain tasks or data types (Paper, p. 6, 8).

### Evaluation factors:
The model's evaluation was disaggregated based on the relevant factors identified above:
*   **Language:** Performance was reported individually for each of the 18 languages in the MIRACL benchmark, 25 languages in the MKQA benchmark, and 14 languages in the MLDR benchmark (Paper, p. 6, 7, 8).
*   **Input Granularity:** The model was explicitly evaluated on long-document retrieval benchmarks (MLDR and NarrativeQA) which use inputs up to 8,192 tokens, and its performance was compared against baselines with shorter context lengths (Paper, p. 8). Figure 5 in the paper shows performance on NarrativeQA as a function of sequence length (Paper, p. 16).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to assess the model's retrieval effectiveness on standard benchmarks:
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** This was the primary metric for evaluating ranking quality in multilingual ad-hoc retrieval (MIRACL) and long-document retrieval (MLDR, NarrativeQA) tasks (Paper, p. 6, 8).
*   **Recall@100 (Recall at 100):** This was the primary metric for the cross-lingual retrieval task (MKQA), measuring the percentage of queries for which a correct answer is found within the top 100 retrieved documents (Paper, p. 7).
*   **Recall@20 and Recall@100:** These were also reported as auxiliary metrics for the MKQA and MIRACL benchmarks, respectively (Paper, p. 7, 17).

### Decision thresholds:
During evaluation, specific thresholds were used to manage the retrieval and re-ranking process:
*   For dense and sparse retrieval methods, the **top-1000** candidates were initially retrieved (Paper, p. 6).
*   For the computationally intensive multi-vector method, it was used to re-rank the **top-200** candidates retrieved by the dense method (Paper, p. 6).
*   For hybrid retrieval (Dense+Sparse), the union of the top-1000 candidates from each method was re-ranked using a weighted score combination (Paper, p. 6).

### Variation approaches:
Performance was measured on the official development or test sets of established public benchmarks. The evaluation setup followed standard practices for each benchmark to ensure reproducibility and fair comparison with prior work (Paper, p. 6, 7).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a diverse set of public benchmarks to test its capabilities in multilingual, cross-lingual, and long-document retrieval.
*   **MIRACL (Multilingual Information Retrieval Across a Continuum of Languages):** A benchmark for ad-hoc retrieval consisting of tasks in 18 diverse languages (Paper, p. 6).
*   **MKQA (Multilingual Knowledge Questions & Answers):** A cross-lingual question-answering benchmark. The evaluation task involves using queries in 25 non-English languages to retrieve relevant passages from the English Wikipedia corpus processed by the BEIR benchmark (Paper, p. 7).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark created by the authors for long-document retrieval, curated from multilingual articles from Wikipedia, Wudao, and mC4. It covers 14 languages and includes 41,434 training queries and a corpus of 493,709 documents (Paper, p. 8, 15).
*   **NarrativeQA:** An English-only benchmark for question answering over long documents (full books and movie scripts), used to evaluate long-context retrieval capabilities (Paper, p. 8).

### Motivation:
These datasets were chosen because they are standard and challenging benchmarks that directly align with the model's core intended uses.
*   MIRACL and MKQA were used to rigorously test the **multi-linguality** and **cross-linguality** claims (Paper, p. 6, 7).
*   MLDR and NarrativeQA were used to evaluate the **multi-granularity** claim, specifically the model's proficiency in handling long documents, which is a known challenge for many embedding models (Paper, p. 8).

### Preprocessing:
The preprocessing of evaluation data followed the standard procedures for each benchmark to ensure fair comparisons.
*   For MIRACL, the official benchmark setup was used with Pyserini to build search indices (Paper, p. 6).
*   For MKQA, the well-processed English Wikipedia corpus from the BEIR benchmark was used as the retrieval target (Paper, p. 7).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
A large-scale and diverse multilingual dataset was curated from three main sources, totaling over 1.2 billion text pairs for the unsupervised stage (Paper, p. 3, 15).

1.  **Unsupervised Data (1.2 Billion pairs):** This data was used for the initial pre-training stage and was collected from various corpora by extracting semantically related text pairs (e.g., title-body, instruction-output).
    *   **Sources:** Wikipedia, S2ORC, xP3, mC4, CC-News, and MTP (Paper, p. 3).
    *   **Languages:** This collection covers 194 languages (Paper, p. 3). The language distribution is illustrated in Figure 4, with English (43.9%), Chinese (20.5%), and Spanish (6.1%) being the most prominent (Paper, p. 16).
    *   **Cross-Lingual Data:** To learn a unified embedding space, parallel sentences from two translation datasets, NLLB (2655 cross-lingual correspondences) and CCMatrix, were included (Paper, p. 3).

2.  **Fine-tuning Data (Labeled Corpora):** Smaller, high-quality labeled datasets were used for the fine-tuning stage.
    *   **English (1.1M pairs):** Datasets include MS MARCO, HotpotQA, TriviaQA, NQ, SQuAD, PubMedQA, COLI-EE, and NLI data from SimCSE (Paper, p. 3, 15).
    *   **Chinese (386.6K pairs):** Datasets include DuReader, mMARCO-ZH, T2-Ranking, LawGPT, CMedQAv2, NLI-zh, and LeCaRDv2 (Paper, p. 3, 15).
    *   **Other Languages (88.9K pairs):** Data from the MIRACL and Mr. TyDi benchmarks were used (Paper, p. 3, 15).

3.  **Synthetic Data (41.4K pairs):** To address the scarcity of long-document retrieval data, a new dataset called **MultiLongDoc** was generated.
    *   **Method:** Lengthy articles were sampled from Wikipedia, Wudao, and mC4. Paragraphs were randomly selected from these articles, and GPT-3.5 was used to generate a specific and valuable question based on the paragraph content (Paper, p. 3, 14).
    *   **Structure:** The resulting dataset consists of generated question and source article pairs across 14 languages (Paper, p. 15).

### Motivation:
The choice of datasets was motivated by the goal of creating a single, versatile embedding model.
*   The massive unsupervised multilingual data provides a strong foundation for learning general semantic representations across many languages (Paper, p. 3).
*   The high-quality labeled fine-tuning data helps specialize the model for specific retrieval tasks and functionalities (Paper, p. 3).
*   The synthetic long-document data was crucial for teaching the model to handle long-context inputs, a key feature of M3-Embedding (Paper, p. 3).

### Preprocessing:
*   The raw unsupervised data was filtered to remove "potential bad contents and low-relevance samples" (Paper, p. 3).
*   For long texts in the training data (e.g., from CC-News), a random shuffling strategy was applied. The text was divided into three segments, their order was shuffled, and they were recombined. This was done with a probability of 0.2% to prevent the model from over-relying on information in the initial sentences of long documents (Paper, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was disaggregated by language across multiple benchmarks. The tables below show the nDCG@10 score for the `Dense` retrieval method on the MIRACL dev set and the MLDR test set.

**MIRACL (nDCG@10)** (Paper, p. 6, Table 1)
| Language | ar | bn | en | es | fa | fi | fr | hi | id | ja | ko | ru | sw | te | th | zh | de | yo |
| :--- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| M3-Dense | 78.4 | 80.0 | 56.9 | 56.1 | 60.9 | 78.6 | 58.3 | 59.5 | 56.1 | 72.8 | 69.9 | 70.1 | 78.7 | 86.2 | 82.6 | 62.7 | 56.7 | 81.8 |

**MLDR (nDCG@10)** (Paper, p. 8, Table 3)
| Language | ar | de | en | es | fr | hi | it | ja | ko | pt | ru | th | zh |
| :--- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| M3-Dense | 47.6 | 46.1 | 48.9 | 74.8 | 73.8 | 40.7 | 62.7 | 50.9 | 42.9 | 74.4 | 59.5 | 33.6 | 26.0 |

**MKQA (Recall@100)** (Paper, p. 7, Table 2)
| Language | ar | da | de | es | fi | fr | he | hu | it | ja | km | ko | ms | nl | no | pl | pt | ru | sv | th | tr | vi | zh_cn | zh_hk | zh_tw |
| :--- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| M3-Dense | 71.1 | 77.2 | 76.2 | 76.4 | 75.1 | 76.2 | 72.4 | 74.7 | 76.0 | 75.0 | 68.6 | 71.6 | 77.2 | 77.4 | 77.1 | 76.3 | 76.3 | 76.2 | 76.9 | 76.4 | 75.6 | 76.6 | 74.6 | 73.8 | 73.5 |

### Intersectional results:
The paper does not provide explicit intersectional results across multiple demographic or environmental factors. However, the evaluation on the MLDR benchmark can be seen as an intersectional analysis of **language** and **document length (granularity)**, as it measures performance on long documents across 14 different languages (Paper, p. 8).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training process for M3-Embedding required significant computational resources, detailed as follows:
*   **Initial Pre-training (RetroMAE adaptation):** This stage was conducted on 32 A100 (40GB) GPUs for 20,000 steps (Paper, p. 14).
*   **Unsupervised Data Pre-training:** The main pre-training phase on 1.2 billion text pairs was conducted on 96 A800 (80GB) GPUs for 25,000 steps (Paper, p. 14).
*   **Fine-tuning:** The final fine-tuning stage with self-knowledge distillation was carried out on 24 A800 (80GB) GPUs (Paper, p. 14).

The paper also highlights memory-saving techniques that were critical for training with long sequences, such as **gradient checkpointing** and a **split-batch method**. These techniques enabled a more than 20-fold increase in effective batch size when processing texts with a length of 8192 tokens, compared to traditional methods (Paper, p. 5, 16).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers acknowledge several ethical considerations related to the development and release of M3-Embedding (Paper, p. 9).
*   **Open-Source Impact:** As the model is publicly available, it is subject to the inherent impacts and potential misuse cases common to open-source models.
*   **Performance Disparities:** The model is trained on multilingual data that includes a wide variety of languages. However, the distribution of this training data is uneven across languages. This may cause the model's performance to vary, with potentially lower effectiveness for low-resource languages. The developers note that this performance gap "could potentially be seen as discriminatory or unfair."
*   **Data Content:** The model was trained on large-scale corpora scraped from the web (e.g., mC4, CC-News). While the data was filtered, it may still contain sensitive, personal, or biased information present in the original sources.
*   **Compliance:** The developers state that their work is conformant to the ACL Ethics Policy.

No specific risks in model usage or mitigation strategies beyond data filtering are detailed. The potential for the model to produce biased embeddings based on the training data is a risk inherent in its design.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors identify several limitations and areas for future work (Paper, p. 9):
*   **Generalizability:** While the model achieves state-of-the-art performance on popular benchmarks like MIRACL and MKQA, its generalizability to other diverse, real-world datasets and scenarios requires further investigation. Different datasets may present unique challenges that could affect performance.
*   **Long-Document Processing:** The model is designed to handle inputs up to 8,192 tokens. However, processing extremely long documents beyond this limit could pose challenges in terms of computational resources and efficiency. The model's performance on such documents needs to be further evaluated.
*   **Language Performance Variation:** The model claims support for over 100 languages, but the paper does not provide a thorough analysis of performance variations across this broad range of languages. Further evaluation is needed to understand the model's robustness and effectiveness across different language families and linguistic characteristics.

### Recommendations:
*   **Hybrid Retrieval:** For achieving the best possible retrieval performance, it is recommended to use a hybrid approach that combines the scores from the dense, sparse, and/or multi-vector functionalities to re-rank candidate documents (Paper, p. 6, 7).
*   **MCLS for Resource-Constrained Users:** For applications involving long documents where fine-tuning is not feasible due to data or GPU resource constraints, the authors recommend using the simple **MCLS (Multiple CLS)** inference strategy. This method can significantly improve long-document retrieval performance without any additional training (Paper, p. 8).