## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu from BAAI (Beijing Academy of Artificial Intelligence) and the University of Science and Technology of China (Paper, Title and Affiliations).

### Model date:
The paper describing the model was last revised on June 28, 2024 (Paper, Page 1).

### Model version:
The model is named M3-Embedding. The repository does not specify a version number. The model offers several functional variations: Dense, Sparse, Multi-vector, Dense+Sparse, and All (a combination of all three) (Paper, Table 1).

### Model type:
M3-Embedding is a text embedding model based on the XLM-ROBERTa architecture (config.json). It is designed for multi-lingual, multi-functional, and multi-granularity text retrieval (Paper, Abstract).

**Key characteristics:**
*   **Architecture:** XLM-ROBERTa (config.json).
*   **Functionalities:** It supports dense retrieval, sparse (lexical) retrieval, and multi-vector retrieval (Paper, Section 3.2).
*   **Size & Parameters:**
    *   Hidden Size: 1024 (config.json)
    *   Number of Attention Heads: 16 (config.json)
    *   Number of Hidden Layers: 24 (config.json)
    *   Vocabulary Size: 250,002 (config.json)
*   **Context Length:** The model supports input sequences up to 8,192 tokens (Paper, Abstract; sentence_bert_config.json).

### Training details:
The model was trained using a multi-stage process involving a novel self-knowledge distillation framework (Paper, Section 3.3, Figure 2).

**Stage 1: RetroMAE Pre-training**
*   The base model is a further pre-trained XLM-ROBERTa model.
*   The model's maximum position embeddings were extended to 8192.
*   It was updated using the RetroMAE method on a dataset of 184 million text samples covering 105 languages, sourced from Pile, Wudao, and mC4 (Paper, Appendix B.1).

**Stage 2: Unsupervised Pre-training**
*   The model was pre-trained on 1.2 billion text pairs from multilingual corpora (Wikipedia, S2ORC, xP3, mC4, CC-News, MTP) and parallel sentence datasets (NLLB, CCMatrix), covering 194 languages and 2655 cross-lingual correspondences (Paper, Section 3.1, Table 8).
*   This stage trained only the dense retrieval functionality using basic contrastive learning (Paper, Section 3.3).

**Stage 3: Fine-tuning with Self-Knowledge Distillation**
*   The model was fine-tuned to establish all three retrieval functionalities (dense, sparse, multi-vector) (Paper, Section 3.3).
*   This stage used a combination of labeled and synthetic data. Labeled data included English datasets (MS MARCO, HotpotQA, NQ, etc.), Chinese datasets (DuReader, T2-Ranking, etc.), and multilingual datasets (MIRACL, Mr.TyDi) (Paper, Section 3.1, Table 8).
*   Synthetic data (MultiLongDoc) was generated using GPT-3.5 for long document retrieval tasks (Paper, Section 3.1, Appendix A.2).
*   A self-knowledge distillation approach was used, where the integrated relevance scores from the different retrieval methods served as a teacher signal to enhance the learning process (Paper, Section 3.3).
*   The training employed an efficient batching strategy, grouping data by sequence length and using a split-batch method with gradient checkpointing to enable large batch sizes and high throughput, especially for long sequences (Paper, Section 3.4, Figure 3, Table 9).

### Paper or other resource for more information:
*   **Paper:** Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*. arXiv preprint arXiv:2402.03216.
*   **Code and Data:** The model, code, and data are publicly available at: https://github.com/FlagOpen/FlagEmbedding (Paper, Footnote 1).

### Citation details:
Insufficient information.

### License:
Insufficient information.

### Contact:
*   stxiao@baai.ac.cn
*   {namespace.pt, luokun695, zhengliu1026}@gmail.com
*   chenjianlv@mail.ustc.edu.cn
*   liandefu@ustc.edu.cn
(Paper, Page 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is a versatile text embedding model designed for information retrieval (IR) systems. Its primary uses include:
*   **Multi-Lingual Retrieval:** It supports semantic retrieval in over 100 languages, enabling both retrieval within a single language and cross-lingual retrieval between different languages (Paper, Abstract).
*   **Multi-Functionality Retrieval:** It unifies three common retrieval functionalities (Paper, Section 3.2):
    *   **Dense Retrieval:** Represents queries and passages as single vectors, with relevance measured by inner product.
    *   **Sparse (Lexical) Retrieval:** Estimates the importance of each term to facilitate lexical matching.
    *   **Multi-Vector Retrieval:** Uses all token embeddings for fine-grained relevance calculation via late-interaction.
*   **Multi-Granularity Retrieval:** It can process inputs of varying lengths, from short sentences to long documents of up to 8,192 tokens (Paper, Abstract).

The model is intended to be a foundational component for building advanced IR systems that can operate across diverse languages, document types, and retrieval paradigms (Paper, Section 1).

### Primary intended users:
The primary users are researchers and developers in the field of Natural Language Processing (NLP) and Information Retrieval (IR) who require a powerful and versatile text embedding model for tasks such as semantic search, question answering, and document retrieval across multiple languages (Paper, Section 1).

### Out-of-scope uses:
The paper does not explicitly list out-of-scope uses. However, based on the provided information, the following should be considered out-of-scope or require caution:
*   **Generative Tasks:** M3-Embedding is an encoder-only model designed for producing text embeddings for retrieval tasks, not for generating text.
*   **Documents Exceeding 8,192 Tokens:** The model's maximum context length is 8,192 tokens. Its performance on documents exceeding this limit has not been investigated (Paper, Section 5).
*   **Guaranteed Performance on All Languages:** While the model supports over 100 languages, performance may vary across them due to the uneven distribution of training data. The model's effectiveness on low-resource languages not extensively covered in the benchmarks should be validated before deployment (Paper, Section 5).

---

## How to Use
The provided information is from a research paper and does not include specific code snippets for implementation. However, it describes the conceptual usage for its different retrieval functionalities (Paper, Section 3.2, Section 4.1).

*   **Dense Retrieval:** The input text is encoded, and the normalized hidden state of the `[CLS]` token is used as the final embedding. Retrieval is performed by calculating the inner product between query and document embeddings.
*   **Sparse Retrieval:** The model outputs term weights for each token in the input text. These weights can be used in a lexical retrieval system like Lucene to calculate a relevance score based on co-occurring terms between a query and a document.
*   **Multi-Vector Retrieval:** The model generates embeddings for all tokens in the input text. A late-interaction mechanism, similar to ColBERT, is then used to compute a fine-grained relevance score between the query's and the document's token embeddings.
*   **Hybrid Retrieval:** The relevance scores from the dense, sparse, and multi-vector methods can be combined in a weighted sum to re-rank candidate documents for improved performance. The paper suggests different weighting schemes depending on the task (Paper, Section 4.1, 4.3). For example, for the MIRACL dataset, the weights `w1=1` (dense), `w2=0.3` (sparse), and `w3=1` (multi-vec) are used for the "All" method (Paper, Section 4.1).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is designed to be multilingual, and its performance is evaluated across a wide range of languages. Performance can vary depending on the language due to the distribution of training data (Paper, Section 5, Tables 1, 2, 3).
*   **Input Length/Granularity:** The model is designed to handle inputs from short sentences to long documents up to 8,192 tokens. Performance varies with sequence length (Paper, Abstract, Figure 5).
*   **Retrieval Method:** The choice of retrieval method (Dense, Sparse, Multi-vector, or a hybrid combination) significantly impacts performance, with different methods being more suitable for certain tasks (e.g., sparse retrieval for long documents) (Paper, Tables 1, 3, 4).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Language:** Performance was disaggregated by language in the MIRACL (18 languages) and MKQA (25 languages) benchmarks (Paper, Tables 1, 2, 12, 13).
*   **Input Length:** Performance on long-document retrieval was specifically evaluated on the MLDR and NarrativeQA datasets, with an analysis of how performance changes with sequence length (Paper, Section 4.3, Figure 5).
*   **Retrieval Functionality:** The performance of each retrieval method (Dense, Sparse, Multi-vector) and their combinations was reported separately (Paper, Tables 1, 3, 4, 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metrics used for evaluation are:
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** Used for the MIRACL, MLDR, and NarrativeQA benchmarks (Paper, Tables 1, 3, 4, 5).
*   **Recall@100:** Used as the primary metric for the MKQA cross-lingual benchmark (Paper, Section 4.2, Table 2).
*   **Recall@20:** Used as an auxiliary metric for the MKQA benchmark (Paper, Appendix C.1, Table 13).
*   **MRR (Mean Reciprocal Rank):** Shown in a comparison graph with other models across several languages (unnamed figure, likely from the MTEB benchmark).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several public benchmarks (Paper, Section 4):
*   **MIRACL (Multilingual Information Retrieval Across a Continuum of Languages):** An ad-hoc retrieval dataset covering 18 diverse languages (Paper, Section 4.1).
*   **MKQA (Multilingual Knowledge Questions & Answers):** A cross-lingual open-domain question answering benchmark with queries in 25 non-English languages against the English Wikipedia corpus (Paper, Section 4.2).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark created by the authors for long-document retrieval, curated from multilingual articles from Wikipedia, Wudao, and mC4. It includes data for 13 languages (Paper, Section 4.3, Table 7).
*   **NarrativeQA:** An English-only benchmark for long-document retrieval (Paper, Section 4.3, Table 4).

### Motivation:
The datasets were chosen to demonstrate the model's versatility across its three key characteristics:
*   **Multi-linguality:** MIRACL and MLDR test retrieval within the same language for multiple languages.
*   **Cross-linguality:** MKQA tests the ability to retrieve English documents using queries from other languages.
*   **Multi-granularity:** MLDR and NarrativeQA test the model's capability on long documents (up to 8192 tokens).

### Preprocessing:
The evaluation follows standard procedures for the respective benchmarks. For retrieval tasks, the Pyserini toolkit was used. Dense retrieval uses a Faiss index, and sparse retrieval uses a Lucene index. Hybrid methods involve re-ranking candidates retrieved by the individual methods (Paper, Section 4.1).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is a large-scale, diverse, multilingual collection from three sources (Paper, Section 3.1, Table 8):
1.  **Unsupervised Data:** 1.2 billion text pairs extracted from corpora including Wikipedia, S2ORC, xP3, mC4, CC-News, and MTP. This also includes parallel sentences from NLLB and CCMatrix to learn cross-lingual alignments. This data covers 194 languages (Paper, Section 3.1). The language distribution is shown in Figure 4, with English comprising 43.9% of the data.
2.  **Labeled Fine-tuning Data:** A collection of smaller, high-quality datasets for supervised fine-tuning.
    *   **English:** 1.1M pairs from MS MARCO, HotpotQA, NQ, NLI, etc.
    *   **Chinese:** 386.6K pairs from DuReader, T2-Ranking, NLI-zh, etc.
    *   **Multilingual:** 88.9K pairs from MIRACL and Mr.TyDi.
3.  **Synthetic Data (MultiLongDoc):** 41.4K question-article pairs generated using GPT-3.5 from long articles in Wikipedia, Wudao, and mC4 to improve long-document retrieval capabilities (Paper, Section 3.1, Table 7).

### Motivation:
The data was curated to be large-scale and diverse to enable the model to learn general semantic representations across many languages and domains. The combination of unsupervised, supervised, and synthetic data, applied in different training stages, provides a solid foundation for the model's versatility (Paper, Section 3.1).

### Preprocessing:
*   Raw data was filtered to remove "potential bad contents and low-relevance samples" (Paper, Section 3.1).
*   For long texts in the unsupervised data, a random shuffling of text segments was applied with a 0.2% probability to prevent the model from overfitting to information in the initial sentences (Paper, Appendix A.1).
*   For synthetic data generation, a specific prompt was used with GPT-3.5 to generate a question based on a given text passage (Paper, Appendix A.2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is reported for each of its retrieval functionalities (Dense, Sparse, Multi-vec) and for individual languages across multiple benchmarks.

*   **MIRACL (nDCG@10):** The Dense method achieves an average score of 69.2, outperforming baselines like mE5-large (66.6) and E5mistral-7b (63.4). The Sparse method achieves 53.9, and Multi-vec achieves 70.5. Performance varies by language, e.g., for English (en), Dense scores 56.9, while for Yoruba (yo), it scores 81.8 (Paper, Table 1).
*   **MKQA (Recall@100):** The Dense method achieves an average score of 75.1, outperforming all baselines. The Sparse method scores 45.3, and Multi-vec scores 75.3. Performance varies by language, e.g., for Arabic (ar), Dense scores 71.1, while for Khmer (km), it scores 68.6 (Paper, Table 2).
*   **MLDR (nDCG@10):** For long-document retrieval, the Sparse method (62.2) outperforms the Dense method (52.5). The Multi-vec method is also strong (57.6) (Paper, Table 3).
*   **NarrativeQA (nDCG@10):** On this English long-document task, the Sparse method (57.5) again outperforms the Dense method (48.7) (Paper, Table 4).

### Intersectional results:
The paper analyzes the performance of combining different retrieval methods.

*   **Dense+Sparse:** On MIRACL, this combination achieves an average nDCG@10 of 70.4. On MLDR, it achieves 64.8 (Paper, Tables 1 & 3).
*   **All (Dense+Sparse+Multi-vec):** This combination yields the best overall performance on all benchmarks:
    *   MIRACL (nDCG@10): 71.5 (Paper, Table 1)
    *   MKQA (Recall@100): 75.5 (Paper, Table 2)
    *   MLDR (nDCG@10): 65.0 (Paper, Table 3)
    *   NarrativeQA (nDCG@10): 61.7 (Paper, Table 4)

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on high-end GPUs (Paper, Appendix B.1):
*   **RetroMAE Pre-training:** 32 A100 (40GB) GPUs.
*   **Unsupervised Pre-training:** 96 A800 (80GB) GPUs.
*   **Fine-tuning:** 24 A800 (80GB) GPUs.

The paper highlights an "Efficient Batching" strategy that uses gradient checkpointing and splits large batches into smaller sub-batches. This allows for a significant increase in effective batch size, especially for long sequences. For an input length of 8192, this method increased the batch size per device from 6 to 130 (Paper, Section 3.4, Table 10).

---

## Ethical Considerations
The model is intended to be publicly available, and as such, it is subject to the inherent impacts of open-source models. The training data is multilingual and sourced from the web, which may contain biases. Due to the uneven distribution of training data across different languages, the model's performance may vary, which could potentially be seen as discriminatory or unfair. The authors state that their work is conformant to the ACL Ethics Policy (Paper, Section "Ethics Consideration").

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors note the following limitations (Paper, Section 5):
*   **Generalizability:** While the model shows strong performance on established benchmarks, its generalizability to other diverse datasets and real-world scenarios requires further investigation.
*   **Extremely Long Documents:** The model is designed for inputs up to 8,192 tokens. Its performance and efficiency on documents exceeding this length have not been evaluated and could pose challenges.
*   **Performance Variation Across Languages:** The paper claims support for over 100 languages, but performance is not evaluated on all of them. There are likely performance variations across different language families and resource levels that have not been thoroughly analyzed.

### Recommendations:
Based on the paper's findings, the following recommendations can be made:
*   For optimal performance, a hybrid retrieval approach combining dense, sparse, and multi-vector scores is recommended, as it consistently achieved the best results across all benchmarks (Paper, Tables 1-5).
*   For long-document retrieval specifically, sparse retrieval or a hybrid method heavily weighting the sparse score may be more effective than dense retrieval alone (Paper, Section 4.3).
*   The paper suggests that exploring better tokenizers for sparse representation is a promising area for future research to further improve performance (Paper, Appendix C.2).