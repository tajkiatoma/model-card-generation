## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu from BAAI (Beijing Academy of Artificial Intelligence) and the University of Science and Technology of China (M3-Embedding paper, p. 1).

### Model date:
The academic paper describing the model was last revised on June 28, 2024 (M3-Embedding paper, p. 1).

### Model version:
This is the first version of the M3-Embedding model described in the paper (M3-Embedding paper, p. 1). The model was developed using sentence-transformers version 2.2.2, transformers version 4.33.0, and PyTorch version 2.1.2+cu121 (`__version__.json`). The model is presented as a new state-of-the-art embedding model that outperforms previous baselines such as BM25, mDPR, mContriever, mE5, E5mistral-7b, and OpenAI's text-embedding-ada-002 on various retrieval benchmarks (M3-Embedding paper, p. 6, 8; MLDR results table).

### Model type:
M3-Embedding is a text embedding model designed for versatility in multi-linguality, multi-functionality, and multi-granularity (M3-Embedding paper, p. 1).

*   **Architecture:** The model is based on the XLM-RoBERTa architecture (`config.json`). It consists of a Transformer layer, a Pooling layer, and a Normalize layer (`modules.json`).
*   **Specifications:**
    *   **Model Type:** xlm-roberta (`config.json`)
    *   **Hidden Size:** 1024 (`config.json`)
    *   **Number of Hidden Layers:** 24 (`config.json`)
    *   **Number of Attention Heads:** 16 (`config.json`)
    *   **Intermediate Size:** 4096 (`config.json`)
    *   **Vocabulary Size:** 250002 (`config.json`)
    *   **Max Context Length:** 8192 tokens (`config.json`, `sentence_bert_config.json`, M3-Embedding paper, p. 1).

### Training details:
The model was trained using a multi-stage workflow (M3-Embedding paper, p. 5).

*   **Stage 1: Pre-training:** An XLM-ROBERTa model, adapted with the RetroMAE method, was first pre-trained on massive unsupervised data. In this stage, only dense retrieval was trained using a basic form of contrastive learning (M3-Embedding paper, p. 5). This was conducted on 32 A100(40GB) GPUs for 20,000 steps (M3-Embedding paper, p. 14). A second pre-training phase on 1.2 billion multilingual unsupervised text pairs was conducted for 25,000 steps on 96 A800(80GB) GPUs (M3-Embedding paper, p. 3, 14).
*   **Stage 2: Fine-tuning with Self-Knowledge Distillation:** The model was then fine-tuned to establish three retrieval functionalities (dense, sparse, and multi-vector). This stage uses a novel self-knowledge distillation framework where the integrated relevance scores from the different retrieval functions act as a "teacher" signal to enhance the learning process (M3-Embedding paper, p. 1, 4). The training minimizes the InfoNCE loss (M3-Embedding paper, p. 4). This stage used both labeled and synthetic data and was carried out on 24 A800(80GB) GPUs (M3-Embedding paper, p. 5, 14).
*   **Efficient Batching:** The training process was optimized with an efficient batching strategy. Data was grouped by sequence length to reduce padding, and gradient checkpointing was used to increase batch sizes for long sequences, significantly improving training efficiency (M3-Embedding paper, p. 5).

### Paper or other resource for more information:
*   **Academic Paper:** Jianlv Chen, Shitao Xiao, et al. "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation." arXiv:2402.03216v4 [cs.CL], 28 Jun 2024. The paper provides a detailed explanation of the model's architecture, training process, and evaluation (M3-Embedding paper, p. 1-18).
*   **Repository:** The model, code, and data are publicly available at: https://github.com/FlagOpen/FlagEmbedding (M3-Embedding paper, p. 1).

### Citation details:
```bibtex
@misc{chen2024m3embedding,
      title={M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation}, 
      author={Jianlv Chen and Shitao Xiao and Peitian Zhang and Kun Luo and Defu Lian and Zheng Liu},
      year={2024},
      eprint={2402.03216},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(M3-Embedding paper, p. 1)

### License:
Insufficient information. The paper states the model is "publicly available" but does not specify a license (M3-Embedding paper, p. 1).

### Contact:
For questions or feedback, the authors can be contacted via the following emails:
*   `stxiao@baai.ac.cn`
*   `{namespace.pt, luokun695, zhengliu1026}@gmail.com`
*   `chenjianlv@mail.ustc.edu.cn`
*   `liandefu@ustc.edu.cn`

(M3-Embedding paper, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is a versatile text embedding model designed for high-performance semantic retrieval across multiple languages, functionalities, and text granularities (M3-Embedding paper, p. 1).

*   **Multi-Lingual Retrieval:** Provides uniform support for semantic retrieval in over 100 languages, enabling both retrieval within a single language and cross-lingual retrieval between different languages (M3-Embedding paper, p. 1).
*   **Multi-Functional Retrieval:** The model can simultaneously perform three common retrieval tasks:
    1.  **Dense Retrieval:** The `[CLS]` token embedding is used to represent the entire text for semantic similarity search (M3-Embedding paper, p. 4).
    2.  **Sparse (Lexical) Retrieval:** Token-level embeddings are used to estimate the importance of each term, facilitating lexical matching (M3-Embedding paper, p. 4).
    3.  **Multi-Vector Retrieval:** Utilizes all output token embeddings for fine-grained relevance computation via late-interaction (M3-Embedding paper, p. 4).
*   **Multi-Granularity Retrieval:** The model is capable of processing inputs of varying lengths, from short sentences to long documents of up to 8,192 tokens (M3-Embedding paper, p. 1).

The model takes text as input and outputs embeddings that can be used to compute relevance scores for information retrieval systems (M3-Embedding paper, p. 4).

### Primary intended users:
The primary users are researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who require a powerful and versatile text embedding model for building or improving search and retrieval systems (M3-Embedding paper, p. 1-2).

### Out-of-scope uses:
*   **Documents Exceeding 8192 Tokens:** The model's performance on documents that significantly exceed the 8,192 token limit has not been investigated and may pose challenges in terms of computational resources and efficiency (M3-Embedding paper, p. 9).
*   **Non-Retrieval Tasks:** The model is specifically designed and trained for retrieval tasks. Its applicability to other NLP tasks like text generation, classification, or summarization is not intended or evaluated.
*   **Untested Domains:** The model's generalizability to highly specialized or diverse real-world datasets and scenarios that differ significantly from the training and evaluation data needs further investigation (M3-Embedding paper, p. 9).

---

## How to Use
This section outlines how to use the model.

The model can be used for different retrieval functionalities by utilizing its output embeddings in specific ways (M3-Embedding paper, p. 4).

*   **Dense Retrieval:**
    *   **Input:** A query text and a passage/document text.
    *   **Process:** For each text, obtain the model's output hidden states. The embedding is the normalized hidden state of the special `[CLS]` token (i.e., `eq = norm(Hq[0])`).
    *   **Output:** The relevance score is the inner product of the query embedding and the passage embedding (`S_dense = <ep, eq>`).

*   **Lexical (Sparse) Retrieval:**
    *   **Input:** A query text and a passage/document text.
    *   **Process:** For each term (token) in the input texts, compute a term weight using its corresponding hidden state and a learned matrix (`W_qt = Relu(W_lex * H_q[i])`).
    *   **Output:** The relevance score is the sum of the products of weights for co-occurring terms between the query and the passage.

*   **Multi-Vector Retrieval:**
    *   **Input:** A query text and a passage/document text.
    *   **Process:** Use the entire sequence of output embeddings for both the query (`E_q`) and the passage (`E_p`), transformed by a learnable projection matrix. A late-interaction mechanism computes the fine-grained relevance score by finding the maximum similarity for each query token embedding across all passage token embeddings.
    *   **Output:** An aggregated relevance score (`S_mul`).

*   **Hybrid Retrieval:**
    *   **Process:** For the highest performance, the scores from the individual retrieval methods can be combined in a weighted sum to re-rank candidate documents. The paper suggests different weights for different scenarios. For example, for the MIRACL benchmark, the hybrid `Dense+Sparse` method uses weights `w1=1` (dense) and `w2=0.3` (sparse) (M3-Embedding paper, p. 6). For the MLDR long-document benchmark, the `All` method uses `w1=0.15` (dense), `w2=0.5` (sparse), and `w3=0.35` (multi-vec) (M3-Embedding paper, p. 8).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** As a multilingual model, performance can vary across the 100+ supported languages. This is influenced by the amount and quality of training data available for each language (M3-Embedding paper, p. 9).
*   **Input Text Length (Granularity):** The model is designed to handle inputs of varying lengths, from short sentences to documents up to 8192 tokens. Performance is dependent on the length of the input sequence (M3-Embedding paper, p. 1, 8).
*   **Retrieval Method:** The choice of retrieval method (Dense, Sparse, Multi-Vector, or a Hybrid combination) significantly impacts performance, with different methods being more effective for different tasks or data types (e.g., sparse for long documents) (M3-Embedding paper, p. 8).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Language:** Performance was measured on multilingual benchmarks (MIRACL, MLDR) and cross-lingual benchmarks (MKQA), with results disaggregated by language (M3-Embedding paper, p. 6, 7, 8).
*   **Input Text Length:** The model's capability was specifically evaluated on long-document retrieval benchmarks (MLDR and NarrativeQA) (M3-Embedding paper, p. 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to evaluate the model's retrieval effectiveness:
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** This was the primary metric for evaluating multilingual retrieval on the MIRACL dataset and long-document retrieval on the MLDR and NarrativeQA datasets (M3-Embedding paper, p. 6, 8).
*   **Recall@100:** This was the primary metric for evaluating cross-lingual retrieval on the MKQA benchmark (M3-Embedding paper, p. 7).

### Decision thresholds:
In the evaluation process, decision thresholds are used to create a set of candidates for re-ranking:
*   For dense and sparse methods, top-1000 candidates are retrieved initially (M3-Embedding paper, p. 6).
*   For the multi-vector method, which is more computationally expensive, it is used to re-rank the top-200 candidates retrieved by the dense method (M3-Embedding paper, p. 6).

### Variation approaches:
Performance is reported on the development set of MIRACL and the test sets of MLDR and NarrativeQA, following the standard evaluation protocols of these benchmarks (M3-Embedding paper, p. 6, 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **MIRACL (Multilingual Information Retrieval Across a Continuum of Languages):** A benchmark for ad-hoc retrieval tasks in 18 diverse languages (M3-Embedding paper, p. 6).
*   **MKQA (Multilingual Knowledge Questions & Answers):** A cross-lingual retrieval benchmark with queries in 25 non-English languages used to retrieve answers from the English Wikipedia corpus (M3-Embedding paper, p. 7).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark for long-document retrieval curated from multilingual articles from Wikipedia, Wudao, and mC4 (M3-Embedding paper, p. 8).
*   **NarrativeQA:** An English-only benchmark for long-document retrieval tasks (M3-Embedding paper, p. 8).

### Motivation:
These datasets were chosen because they are standard and challenging benchmarks for evaluating the model's core capabilities: multilingual retrieval (MIRACL), cross-lingual retrieval (MKQA), and long-document retrieval (MLDR, NarrativeQA) (M3-Embedding paper, p. 6-8).

### Preprocessing:
For the MKQA evaluation, the well-processed English Wikipedia corpus provided by the BEIR benchmark was used (M3-Embedding paper, p. 7). For MIRACL, the evaluation followed the official benchmark using the Pyserini toolkit (M3-Embedding paper, p. 6).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale, diverse multilingual dataset curated from three sources (M3-Embedding paper, p. 3; Table 8, p. 15):
*   **Unsupervised Data (1.2 billion text pairs):** This data was created by extracting semantically related text pairs (e.g., title-body, instruction-output) from large multilingual corpora, including Wikipedia, S2ORC, xP3, mC4, CC-News, and MTP. It also includes 391.3M parallel sentences from NLLB and CCMatrix to learn a unified cross-lingual embedding space (M3-Embedding paper, p. 3, 15).
*   **Fine-tuning Data (Labeled Corpora):**
    *   **English (1.1M):** A collection of 8 datasets such as MS MARCO, HotpotQA, NQ, and TriviaQA.
    *   **Chinese (386.6K):** A collection of 7 datasets including DuReader, T2-Ranking, and mMARCO-ZH.
    *   **Multilingual (88.9K + 41.4K):** Data from the MIRACL and Mr.TyDi benchmarks.
    (M3-Embedding paper, p. 3, 15)
*   **Synthetic Data (MultiLongDoc):** To address the scarcity of long-document retrieval data, synthetic question-article pairs were generated using GPT-3.5 on lengthy articles sampled from Wikipedia, Wudao, and mC4 datasets (M3-Embedding paper, p. 3).

### Motivation:
The datasets were chosen to build a comprehensive and versatile training resource. The three sources are complementary: unsupervised data provides broad semantic knowledge, labeled data provides high-quality signals for specific retrieval tasks, and synthetic data fills the gap for long-document retrieval (M3-Embedding paper, p. 2, 3).

### Preprocessing:
*   The raw unsupervised data was filtered to remove "potential bad contents and low-relevance samples" (M3-Embedding paper, p. 3).
*   To prevent the model from only learning from the beginning of long documents (which often contain summaries), a random shuffling strategy was applied to segments of text with a 0.2% probability during training (M3-Embedding paper, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents detailed performance results for individual languages and retrieval methods across several benchmarks.

*   **Multilingual Retrieval (MIRACL, nDCG@10):** The model's `Dense` method achieves an average score of 69.2, outperforming baselines like mE5large (66.6) and E5mistral-7b (63.4). The combined `All` method achieves the highest average score of 71.5. Results are broken down for 18 languages including Arabic (ar), English (en), Spanish (es), Japanese (ja), and Yoruba (yo) (M3-Embedding paper, Table 1, p. 6).
*   **Cross-Lingual Retrieval (MKQA, Recall@100):** The `Dense` method achieves an average score of 75.1, and the `All` method achieves 75.5, outperforming all baselines. Results are provided for 25 languages, showing strong performance even in low-resource languages like Khmer (km) where it scores 68.6 compared to baselines' 28.1-34.3 (M3-Embedding paper, Table 2, p. 7).
*   **Long-Document Retrieval (MLDR, nDCG@10):** The `Sparse` method (62.2) is particularly effective, outperforming the `Dense` method (52.5) and strong baselines like BM25 (53.6). The combined `All` method achieves the best average score of 65.0. Results are broken down for 13 languages (MLDR results table; M3-Embedding paper, Table 3, p. 8).

### Intersectional results:
The paper does not provide explicit intersectional results (e.g., performance for a specific demographic group within a particular language). However, results are presented for different languages on tasks with different input lengths (e.g., MLDR for long documents vs. MIRACL for shorter passages), allowing for some cross-analysis of language and granularity factors (M3-Embedding paper, Tables 1 & 3, p. 6, 8).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The paper specifies the hardware used for the different stages of training:
*   **Initial Pre-training (RetroMAE):** 32 A100 (40GB) GPUs (M3-Embedding paper, p. 14).
*   **Unsupervised Data Pre-training:** 96 A800 (80GB) GPUs (M3-Embedding paper, p. 14).
*   **Fine-tuning Stage:** 24 A800 (80GB) GPUs (M3-Embedding paper, p. 14).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model is publicly available and was trained on multilingual data, which introduces ethical considerations related to open-source models and data distribution (M3-Embedding paper, p. 9).

*   **Sensitive Data:** The model was trained on large web-crawled corpora like mC4 and CC-News, which may contain unfiltered personal or sensitive information (M3-Embedding paper, p. 3).
*   **Risks and Mitigation:** The primary risk identified by the authors is potential performance disparity across languages. Due to the "uneven distribution of training data for different languages, the model's performance may vary across languages, which could potentially be seen as discriminatory or unfair." The comprehensive data curation across over 100 languages is an implicit mitigation strategy to address this imbalance. The authors state that their work conforms to the ACL Ethics Policy (M3-Embedding paper, p. 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors acknowledge several limitations of the model:
*   **Generalizability:** The model's state-of-the-art performance was demonstrated on specific benchmarks. Its generalizability to other diverse datasets and real-world scenarios requires further investigation (M3-Embedding paper, p. 9).
*   **Extremely Long Documents:** While the model handles documents up to 8192 tokens, its performance and efficiency on documents exceeding this limit need to be further evaluated (M3-Embedding paper, p. 9).
*   **Performance Variation Across Languages:** Although the model supports over 100 languages, the performance variations across different language families and linguistic characteristics have not been thoroughly analyzed (M3-Embedding paper, p. 9).

### Recommendations:
*   **Use Hybrid Retrieval for Best Performance:** For optimal results, users should combine the outputs of the dense, sparse, and multi-vector retrieval methods, as this consistently yields the best performance across benchmarks (M3-Embedding paper, p. 6, 7, 8).
*   **Use MCLS for Long Documents without Fine-tuning:** For users with limited computational resources who cannot fine-tune on long-document data, the paper proposes a simple inference-time strategy called MCLS (Multiple CLS). This involves inserting multiple `[CLS]` tokens into a long document and averaging their embeddings, which significantly improves long-document retrieval performance without any training (M3-Embedding paper, p. 8, 14).
*   **Future Research:** The paper suggests that exploring tokenizers that perform better for sparse representation is a worthwhile area for future research, as BM25 remains a very competitive baseline for sparse retrieval on long documents (M3-Embedding paper, p. 16).