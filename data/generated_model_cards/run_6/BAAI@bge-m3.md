## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu from BAAI (Beijing Academy of Artificial Intelligence) and the University of Science and Technology of China (2402.03216.pdf, p. 1).

### Model date:
The academic paper describing the model is version v4, dated June 28, 2024 (2402.03216.pdf, p. 1). The development involved a multi-stage training process, but specific dates for each stage are not provided (2402.03216.pdf, p. 5).

### Model version:
The model is named M3-Embedding (2402.03216.pdf, p. 1). The associated paper is version v4 (2402.03216.pdf, p. 1). The model was built using sentence-transformers version 2.2.2, transformers version 4.33.0, and PyTorch version 2.1.2+cu121 (config_sentence_transformers.json). M3-Embedding is distinguished by its versatility in three key areas:
*   **Multi-Linguality:** It supports semantic retrieval for over 100 languages (2402.03216.pdf, p. 1).
*   **Multi-Functionality:** It can perform dense, sparse, and multi-vector retrieval (2402.03216.pdf, p. 1).
*   **Multi-Granularity:** It can process inputs of varying lengths, from short sentences to long documents up to 8,192 tokens (2402.03216.pdf, p. 1).

### Model type:
M3-Embedding is a text embedding model based on the XLM-RoBERTa architecture (config.json; 2402.03216.pdf, p. 5). Its structure consists of a Transformer model followed by Pooling and Normalize layers (modules.json).

**Architecture Details (config.json):**
*   **Model Type:** `xlm-roberta`
*   **Architecture:** `XLMRobertaModel`
*   **Hidden Size:** 1024
*   **Number of Hidden Layers:** 24
*   **Number of Attention Heads:** 16
*   **Intermediate Size:** 4096
*   **Vocabulary Size:** 250002
*   **Maximum Context Length:** 8192 tokens (max_position_embeddings is 8194)

The pooling layer uses the `[CLS]` token's hidden state for the final embedding (1_Pooling/config.json).

### Training details:
The model was trained using a multi-stage workflow (2402.03216.pdf, p. 4, Figure 2).

**Stage 1: Pre-training**
The foundational model, an XLM-ROBERTa large model, was first adapted using the RetroMAE method (2402.03216.pdf, p. 5, 14). It was then pre-trained on 1.2 billion pairs of multilingual unsupervised data using a basic contrastive learning objective for dense retrieval (2402.03216.pdf, p. 5, 15). Key hyperparameters for this stage included a learning rate of 5e-5, a warmup ratio of 0.1, and a weight decay of 0.01, running for 25,000 steps (2402.03216.pdf, p. 14).

**Stage 2: Fine-tuning with Self-Knowledge Distillation**
In the second stage, the model was fine-tuned on a combination of labeled and synthetic data to establish its three retrieval functionalities (dense, sparse, multi-vector) (2402.03216.pdf, p. 5). A novel **self-knowledge distillation** framework was proposed to unify the training process. In this framework, the relevance scores from the different retrieval methods are integrated to form a "teacher" signal, which enhances the learning process for each individual method (2402.03216.pdf, p. 4). The final loss function is a combination of the InfoNCE loss for each retrieval method and a distillation loss derived from the integrated teacher score (2402.03216.pdf, p. 4-5). Hard negative samples were introduced for each query following the ANCE method (2402.03216.pdf, p. 5).

**Efficient Batching Strategy**
To handle diverse and long-sequence data efficiently, an optimized batching strategy was used. Training data was grouped by sequence length to reduce padding. For long sequences, mini-batches were further divided into sub-batches, and gradient checkpointing was used to save memory, allowing for a significant increase in effective batch size (2402.03216.pdf, p. 5).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Paper:** Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*. arXiv preprint arXiv:2402.03216 (2402.03216.pdf).
*   **Repository:** The model, code, and data are publicly available at: https://github.com/FlagOpen/FlagEmbedding (2402.03216.pdf, p. 1).

### Citation details:
Insufficient information. A BibTeX entry is not provided, but one can be created from the paper details.

### License:
Insufficient information.

### Contact:
Contact can be made with the authors via the following emails provided in the paper (2402.03216.pdf, p. 1):
*   `stxiao@baai.ac.cn`
*   `{namespace.pt, luokun695, zhengliu1026}@gmail.com`
*   `chenjianlv@mail.ustc.edu.cn`
*   `liandefu@ustc.edu.cn`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is a general-purpose text embedding model designed for versatile semantic retrieval tasks (2402.03216.pdf, p. 1). Its primary capabilities are:
*   **Multi-Lingual Retrieval:** Retrieving documents in the same language as the query, with support for over 100 languages (2402.03216.pdf, p. 1).
*   **Cross-Lingual Retrieval:** Retrieving documents in a different language from the query (e.g., a non-English query to retrieve English documents) (2402.03216.pdf, p. 2).
*   **Long-Document Retrieval:** Processing and retrieving long-form documents with up to 8,192 tokens (2402.03216.pdf, p. 1).
*   **Hybrid Retrieval:** The model supports three distinct retrieval functionalities that can be used individually or combined for improved performance (2402.03216.pdf, p. 4):
    *   **Dense Retrieval:** Based on the embedding similarity of the `[CLS]` token.
    *   **Sparse (Lexical) Retrieval:** Based on learned term weights for each token.
    *   **Multi-Vector Retrieval:** Based on fine-grained interactions between all token embeddings of the query and document.

The model takes text (a query or a document) as input and outputs a dense vector representation (embedding) (2402.03216.pdf, p. 4).

### Primary intended users:
The primary intended users are researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who require a versatile and high-performing text embedding model for multilingual and long-document applications (2402.03216.pdf, p. 1-2).

### Out-of-scope uses:
The model is designed for text embedding and retrieval tasks. It is not intended for:
*   **Text Generation:** The model does not generate text.
*   **Conversational AI or Chatbots:** It is not a conversational agent.
*   **Use in languages with low representation:** The model's performance may be degraded for languages that were not well-represented in the training data, which could lead to unfair or discriminatory outcomes (2402.03216.pdf, p. 9).
*   **Tasks requiring reasoning beyond semantic similarity:** The model's core function is to measure semantic relevance between texts.

---

## How to Use
This section outlines how to use the model.

Insufficient information. The provided repository does not include code snippets or a `README.md` file with usage instructions.

However, the research paper describes the conceptual workflow for using the model's different retrieval functionalities (2402.03216.pdf, p. 6):
1.  **Generate Embeddings/Weights:** Use the M3-Embedding model to encode all documents in the corpus and the input query.
2.  **Index the Corpus:**
    *   For **Dense** retrieval, build a dense index (e.g., using Faiss) from the generated `[CLS]` embeddings.
    *   For **Sparse** retrieval, build a sparse index (e.g., using Lucene) from the generated term weights.
3.  **Retrieve Candidates:** Search the index with the query's embedding/weights to retrieve an initial set of top-k candidates (e.g., top-1000).
4.  **Re-rank (Optional):** For higher accuracy, the initial candidates can be re-ranked using more computationally intensive methods like **Multi-vector** retrieval or a **hybrid score** combining dense, sparse, and multi-vector relevance scores (2402.03216.pdf, p. 4, 6).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The key factors that influence the model's performance are (2402.03216.pdf, p. 1, 9):
*   **Language:** As a multilingual model, performance can vary significantly across different languages. This is attributed to the uneven distribution of languages in the training data.
*   **Input Granularity / Document Length:** The model is designed to handle inputs from short sentences to long documents. Its performance is dependent on the length of the text being processed.
*   **Domain:** The model's generalizability to different domains and real-world scenarios beyond the evaluation benchmarks needs further investigation.

### Evaluation factors:
The model evaluations reported in the paper are disaggregated by the following factors:
*   **Language:** All multilingual and cross-lingual benchmark results are reported on a per-language basis (2402.03216.pdf, Tables 1, 2, 3).
*   **Document Length:** The model is explicitly evaluated on long-document retrieval benchmarks (MLDR and NarrativeQA) to assess its performance on longer sequences (2402.03216.pdf, p. 7-8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics are used to evaluate the model's retrieval performance on different benchmarks (2402.03216.pdf, p. 6-8):
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** The primary metric for multilingual retrieval on the MIRACL and MLDR benchmarks, and for long-document retrieval on NarrativeQA.
*   **Recall@100 (Recall at 100):** The primary metric for cross-lingual retrieval on the MKQA benchmark.
*   **Recall@20 (Recall at 20):** An auxiliary metric reported for the MKQA benchmark.

### Decision thresholds:
The evaluation pipeline described in the paper uses the following thresholds (2402.03216.pdf, p. 6):
*   **Top-1000:** For initial candidate retrieval using the Dense and Sparse methods.
*   **Top-200:** For re-ranking using the Multi-vector method.

### Variation approaches:
Insufficient information. The paper does not describe the use of statistical methods like cross-validation or bootstrapping to estimate uncertainty in performance metrics.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several public benchmarks to test its different capabilities (2402.03216.pdf, p. 6-8):
*   **MIRACL (Multilingual Information Retrieval Across a Continuum of Languages):** Used for evaluating multilingual retrieval. It consists of ad-hoc retrieval tasks in 18 languages (2402.03216.pdf, p. 6).
*   **MKQA (Multilingual Knowledge Questions & Answers):** Used for evaluating cross-lingual retrieval. It includes queries in 25 non-English languages for retrieving passages from the English Wikipedia corpus (2402.03216.pdf, p. 7).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark for multilingual long-document retrieval curated from Wikipedia, Wudao, and mC4. It covers 13 languages and contains over 41,000 training queries and a corpus of nearly 500,000 documents (2402.03216.pdf, p. 8, 15, Table 7).
*   **NarrativeQA:** An English-only benchmark used for evaluating long-document retrieval (2402.03216.pdf, p. 8).

### Motivation:
These datasets were chosen because they are popular and standard benchmarks for evaluating the model's core intended uses: multilingual retrieval (MIRACL), cross-lingual retrieval (MKQA), and long-document retrieval (MLDR, NarrativeQA) (2402.03216.pdf, p. 2, 9).

### Preprocessing:
For the MKQA evaluation, the well-processed English Wikipedia corpus from the BEIR benchmark was used (2402.03216.pdf, p. 7). Other specific preprocessing steps for the evaluation data are not detailed, aside from the indexing procedures performed with tools like Pyserini, Faiss, and Lucene (2402.03216.pdf, p. 6).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
A large-scale, diverse multilingual dataset was curated from three sources, totaling over 1.2 billion text pairs (2402.03216.pdf, p. 3, 15, Table 8).

1.  **Unsupervised Data (1.2 Billion pairs):**
    *   **Source:** Rich-semantic structures (e.g., title-body, instruction-output) were extracted from multilingual corpora including Wikipedia, S2ORC, xP3, mC4, and CC-News. Parallel sentences from NLLB and CCMatrix were also included to learn cross-lingual semantics (2402.03216.pdf, p. 3).
    *   **Diversity:** This data covers 194 languages and 2655 cross-lingual correspondences (2402.03216.pdf, p. 3).

2.  **Fine-tuning Data (Labeled Corpora):**
    *   **English (1.1M):** A collection of 8 datasets including MS MARCO, HotpotQA, TriviaQA, NQ, and NLI data from SimCSE (2402.03216.pdf, p. 3, 15).
    *   **Chinese (386.6K):** A collection of 7 datasets including DuReader, mMARCO-ZH, T2-Ranking, and LawGPT (2402.03216.pdf, p. 3, 15).
    *   **Other Languages (130.3K):** Training data from the MIRACL and Mr. TyDi benchmarks (2402.03216.pdf, p. 3, 15).

3.  **Synthetic Data (41.4K):**
    *   **Source:** To address the scarcity of long-document retrieval data, question-article pairs were generated using GPT-3.5. Lengthy articles were sampled from Wikipedia, Wudao, and mC4, and questions were generated based on random paragraphs from them (2402.03216.pdf, p. 3). This dataset is named MultiLongDoc (2402.03216.pdf, p. 15).

### Motivation:
The data was collected to create a comprehensive training resource that could support the model's three-fold versatility (Multi-Linguality, Multi-Functionality, Multi-Granularity). The three data sources are complementary and were applied at different stages of the training process to build a solid foundation for the text embeddings (2402.03216.pdf, p. 3).

### Preprocessing:
*   The raw unsupervised data was filtered to remove "potential bad contents and low-relevance samples" (2402.03216.pdf, p. 3).
*   To prevent the model from relying only on the beginning of long documents, a random shuffling strategy was applied. Long texts were divided into three segments, their order was shuffled, and they were recombined. This was applied to passages with a probability of 0.2% during training (2402.03216.pdf, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides detailed performance results for the model's different retrieval methods (Dense, Sparse, Multi-vec, and combined) disaggregated by language across multiple benchmarks.

*   **MIRACL (Multilingual Retrieval, nDCG@10):** Performance is reported for 18 languages, including Arabic (ar), Bengali (bn), English (en), Spanish (es), French (fr), Japanese (ja), and Yoruba (yo). The full "All" model achieves an average score of 71.5 (2402.03216.pdf, p. 6, Table 1).
*   **MKQA (Cross-Lingual Retrieval, Recall@100):** Performance is reported for 25 languages querying an English corpus, including German (de), Finnish (fi), Hebrew (he), Khmer (km), and Vietnamese (vi). The "All" model achieves an average score of 75.5 (2402.03216.pdf, p. 7, Table 2).
*   **MLDR (Multilingual Long-Doc Retrieval, nDCG@10):** Performance is reported for 13 languages, including Chinese (zh), German (de), Hindi (hi), Italian (it), and Russian (ru). The "All" model achieves an average score of 65.0 (2402.03216.pdf, p. 8, Table 3).
*   **NarrativeQA (English Long-Doc Retrieval, nDCG@10):** The "All" model achieves a score of 61.7 (2402.03216.pdf, p. 8, Table 4).

### Intersectional results:
Insufficient information. The paper does not present performance results across combinations of factors (e.g., performance on long documents for a specific language other than English).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training process was computationally intensive and required high-end GPUs (2402.03216.pdf, p. 14):
*   **Initial Model Adaptation (RetroMAE):** Conducted on 32 A100 (40GB) GPUs for 20,000 steps.
*   **Unsupervised Pre-training:** Conducted on 96 A800 (80GB) GPUs for 25,000 steps.
*   **Fine-tuning Stage:** Conducted on 24 A800 (80GB) GPUs.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper includes an "Ethics Consideration" section with the following points (2402.03216.pdf, p. 9):
*   **Public Availability:** The model is publicly available, and as such, is influenced by the inherent impacts of open-source models.
*   **Performance Disparity Risk:** The primary ethical risk identified is related to fairness. The training data has an uneven distribution across different languages. Consequently, the model's performance may vary across languages, which "could potentially be seen as discriminatory or unfair."
*   **Data Usage:** The paper states that multilingual data including "all kinds of languages" was used in training. There is no mention of using personally identifiable or sensitive data.
*   **Compliance:** The authors state that their work is conformant to the ACL Ethics Policy.
*   **Risk Mitigation:** No specific risk mitigation strategies are described beyond acknowledging the potential for performance disparities.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper's "Limitations" section highlights several areas for future work and user caution (2402.03216.pdf, p. 9):
*   **Generalizability:** The model's performance on datasets and real-world scenarios that differ from the evaluation benchmarks has not been fully investigated.
*   **Extremely Long Documents:** While the model supports up to 8,192 tokens, its performance and efficiency on documents exceeding this limit, or on very long documents in general, may pose challenges and require further study.
*   **Language Performance Variation:** The paper claims support for over 100 languages, but the performance variations across this broad range of languages are not thoroughly analyzed. The robustness and effectiveness of the model may differ significantly between high-resource and low-resource languages.

### Recommendations:
Based on the paper's findings, users should consider the following:
*   **Hybrid Retrieval for Best Performance:** For the highest retrieval quality, users should combine the dense, sparse, and multi-vector retrieval methods, as this "All" configuration consistently achieved the best results (2402.03216.pdf, p. 7).
*   **Awareness of Language Bias:** Users should be aware that performance may be lower for languages that are less represented in the training data.
*   **Resource-Constrained Long-Doc Retrieval:** For users without the data or GPU resources to fine-tune on long documents, the paper proposes a simple inference-time strategy called MCLS (Multiple CLS), which was shown to significantly improve performance without any additional training (2402.03216.pdf, p. 8).