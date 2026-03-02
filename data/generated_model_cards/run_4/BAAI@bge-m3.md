## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu from BAAI (Beijing Academy of Artificial Intelligence) and the University of Science and Technology of China (Paper, Title and Authors).

### Model date:
The paper describing the model was last revised on June 28, 2024 (Paper, Date).

### Model version:
The model is named M3-Embedding. No specific version number is provided in the repository data (Paper). The underlying architecture uses `transformers` version 4.33.0 (`modules.json`).

### Model type:
M3-Embedding is a text embedding model distinguished by its versatility in Multi-Linguality, Multi-Functionality, and Multi-Granularity (Paper, Abstract).

*   **Architecture:** The model is based on the XLM-ROBERTa architecture (Paper, Section 3.4; `config.json`). It has 24 hidden layers, a hidden size of 1024, 16 attention heads, and an intermediate size of 4096 (`config.json`). The total vocabulary size is 250,002 (`config.json`).
*   **Functionality:** It is a unified model that supports three common retrieval functionalities (Paper, Abstract):
    *   **Dense Retrieval:** Uses the normalized hidden state of the `[CLS]` token as the text representation (Paper, Section 3.2).
    *   **Sparse Retrieval:** Estimates the importance of each term (token) by mapping its hidden state to a float number, which is then used as the term weight (Paper, Section 3.2).
    *   **Multi-Vector Retrieval:** Uses the entire sequence of output embeddings with a learnable projection matrix to compute fine-grained relevance scores via late-interaction (Paper, Section 3.2).
*   **Size and Context Length:** The model supports a maximum sequence length of up to 8,192 tokens (Paper, Abstract; `config.json`). The word embedding dimension is 1024 (`1_Pooling/config.json`).

### Training details:
The model was trained using a multi-stage process involving a novel self-knowledge distillation framework (Paper, Section 3.3, Figure 2).

*   **Stage 1: Pre-training:** The XLM-ROBERTa model was first adapted using the RetroMAE method (Xiao et al., 2022) on a dataset of 184 million text samples from Pile, Wudao, and mC4, covering 105 languages. This stage used a max sequence length of 8192, a learning rate of 7 x 10⁻⁵, and a batch size of 32 with 16 gradient accumulation steps. This was conducted on 32 A100 (40GB) GPUs for 20,000 steps (Paper, Appendix B.1).
*   **Stage 2: Fine-tuning with Self-Knowledge Distillation:**
    *   **Data:** This stage used a combination of massive unsupervised data (1.2 billion text pairs from sources like Wikipedia, mC4, CC-News, NLLB, etc.), labeled fine-tuning data (from datasets like MS MARCO, MIRACL, Mr. TyDi), and synthetic long-document data generated using GPT-3.5 (Paper, Section 3.1, Table 8).
    *   **Methodology:** The model was trained to optimize for dense, sparse, and multi-vector retrieval simultaneously. A self-knowledge distillation approach was used, where the relevance scores from the different retrieval functions are integrated to form a "teacher signal" that enhances the learning process for each individual function. The final loss is a combination of the standard InfoNCE loss and the distillation loss (Paper, Section 3.3).
    *   **Batching:** An efficient batching strategy was employed where training data is grouped by sequence length to reduce padding. For long sequences, mini-batches are divided into smaller sub-batches and processed iteratively using gradient checkpointing to increase the effective batch size significantly (Paper, Section 3.4, Figure 3). For example, for sequences of length 8192, the batch size can be increased by more than 20 times (Paper, Appendix C.1, Table 10).
    *   **Hardware:** The fine-tuning stage was conducted on 96 A800 (80GB) GPUs for the unsupervised pre-training part and 24 A800 (80GB) GPUs for the final fine-tuning with self-knowledge distillation (Paper, Appendix B.1).

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
### Primary intended uses:
M3-Embedding is designed for versatile semantic retrieval across more than 100 languages (Paper, Abstract). Its primary uses include:
*   **Multi-Lingual Retrieval:** Retrieving documents in the same language as the query for over 100 languages (Paper, Section 1).
*   **Cross-Lingual Retrieval:** Retrieving documents in a different language (e.g., English) from a query in another language (Paper, Section 1, Section 4.2).
*   **Multi-Granularity Retrieval:** Processing inputs of varying lengths, from short sentences to long documents of up to 8,192 tokens (Paper, Abstract).
*   **Multi-Functionality Retrieval:** The model can be used for dense, sparse, and multi-vector retrieval. These methods can be used individually or combined in a hybrid approach for re-ranking to achieve better performance (Paper, Section 3.2).

The model takes text (query or document) as input and outputs embeddings. For dense and multi-vector retrieval, these are dense vectors. For sparse retrieval, it outputs term weights (Paper, Section 3.2).

### Primary intended users:
The model is intended for researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who require a versatile text embedding model for various retrieval tasks, especially in multilingual and long-document contexts (Paper, Section 1).

### Out-of-scope uses:
*   The model is not designed for processing documents that significantly exceed the 8,192 token limit (Paper, Limitations).
*   Due to the uneven distribution of training data, the model's performance may vary across different languages. It may exhibit lower performance on low-resource languages compared to high-resource ones like English (Paper, Ethical Considerations).
*   The model is designed for retrieval tasks. Its performance on other NLP tasks like classification, summarization, or generation has not been evaluated.

---

## How to Use
The provided repository data does not include specific code snippets for using the model. However, the paper describes the different retrieval methods that can be implemented using the model's outputs (Paper, Section 3.2):

*   **Dense Retrieval:** The input text is encoded, and the normalized hidden state of the `[CLS]` token is used as the final embedding. Retrieval is performed by computing the inner product between query and document embeddings.
*   **Sparse Retrieval:** The model outputs a weight for each token in the input text. The relevance score is calculated based on the joint importance of co-occurring terms between the query and the document.
*   **Multi-Vector Retrieval:** This method uses all token embeddings from the encoder's output. A learnable projection matrix is applied, followed by a late-interaction mechanism (max-similarity) to compute a fine-grained relevance score. This is computationally more expensive and is suggested for re-ranking a smaller set of candidates (Paper, Section 4.1).
*   **Hybrid Retrieval:** The scores from dense, sparse, and multi-vector retrieval can be combined using a weighted sum to re-rank candidate documents for improved performance. The paper provides example weights for different scenarios (Paper, Section 3.2, Section 4.1, Section 4.3).
*   **MCLS (Multiple CLS) Method:** For users who cannot fine-tune on long documents, the paper proposes a simple inference-time strategy. Multiple `[CLS]` tokens are inserted into the long document (e.g., one for every 256 tokens), and the final document embedding is the average of the output embeddings of all `[CLS]` tokens. This method was shown to significantly improve long-document retrieval performance without any additional training (Paper, Appendix B.2).

---

## Factors
### Relevant factors:
*   **Language:** The model is designed to be multilingual, and its performance is evaluated across a wide range of languages. Performance can vary depending on the language due to the distribution of training data (Paper, Section 4, Ethical Considerations).
*   **Input Length/Granularity:** The model is designed to handle inputs of varying lengths, from short sentences to long documents up to 8,192 tokens. Performance is shown to improve with longer context on relevant tasks (Paper, Abstract, Figure 5).
*   **Retrieval Functionality:** The choice of retrieval method (dense, sparse, multi-vector, or a hybrid combination) significantly impacts performance. The optimal combination and weighting can depend on the specific downstream task (Paper, Section 4).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Language:** Performance was disaggregated by language in the MIRACL (18 languages) and MKQA (25 languages) benchmarks (Paper, Table 1, Table 2, Table 12, Table 13).
*   **Input Length:** Performance on long-document retrieval was evaluated on the MLDR and NarrativeQA datasets, with a specific analysis showing performance scaling with sequence length (Paper, Section 4.3, Figure 5).
*   **Retrieval Method:** Performance was reported for each retrieval method (Dense, Sparse, Multi-vec) and their combinations (Dense+Sparse, All) (Paper, Table 1, Table 3, Table 4).

---

## Metrics
### Model performance measures:
The model's performance was measured using standard information retrieval metrics (Paper, Section 4):
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** Used for the MIRACL, MLDR, and NarrativeQA benchmarks.
*   **Recall@100 and Recall@20:** Used for the MKQA cross-lingual benchmark.

### Decision thresholds:
The evaluation metrics are based on retrieving a ranked list of documents. The thresholds are implicit in the metrics used, such as retrieving the top 10 (for nDCG@10) or top 100/20 (for Recall@100/20) documents (Paper, Section 4).

### Variation approaches:
The performance metrics are reported as single scores on the development or test sets of standard benchmarks. The provided information does not mention the use of statistical methods like cross-validation or bootstrapping to estimate uncertainty (Paper, Section 4).

---

## Evaluation Data
### Datasets:
The model was evaluated on several public benchmarks (Paper, Section 4):
*   **MIRACL (Multilingual Information Retrieval Across a Continuum of Languages):** An ad-hoc retrieval dataset covering 18 diverse languages (Paper, Section 4.1).
*   **MKQA (Massive Knowledge QA):** A cross-lingual open-domain question answering benchmark with queries in 25 non-English languages against an English Wikipedia corpus (Paper, Section 4.2).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark curated by the authors for long-document retrieval, using articles from Wikipedia, Wudao, and mC4 (Paper, Section 4.3, Table 7).
*   **NarrativeQA:** An English-language benchmark for long-document retrieval (Paper, Section 4.3).

### Motivation:
These datasets were chosen to demonstrate the model's claimed versatility across multiple languages (MIRACL, MKQA), its ability to handle long documents (MLDR, NarrativeQA), and its effectiveness in both multilingual and cross-lingual settings (Paper, Section 4).

### Preprocessing:
For a fair comparison with the BM25 baseline on the MIRACL dataset, the same XLM-R tokenizer was used for both M3-Embedding and BM25 (Paper, Section 4.1). For the MKQA evaluation, the well-processed corpus from the BEIR benchmark was used (Paper, Section 4.2).

---

## Training Data
### Datasets:
The model was trained on a large-scale, diverse, multilingual dataset curated from three sources (Paper, Section 3.1, Table 8):
*   **Unsupervised Data (1.2 Billion pairs):** Text pairs were extracted from multilingual corpora including MTP, S2ORC, Wikipedia, xP3, mC4, and CC-News. This also included parallel sentences from NLLB and CCMatrix for cross-lingual learning (Paper, Section 3.1, Table 8). The language distribution of this data is shown in Figure 4, with English comprising 43.9% and Chinese 20.5% (Paper, Figure 4).
*   **Labeled Fine-tuning Data:**
    *   **English (1.1M):** MS MARCO, HotpotQA, NQ, SQuAD, NLI, etc.
    *   **Chinese (386.6K):** DuReader, T2-Ranking, NLI-zh, etc.
    *   **Multilingual (88.9K):** MIRACL, Mr.TyDi.
*   **Synthetic Data (41.4K):** A new dataset called MultiLongDoc was generated using GPT-3.5 to create question-passage pairs from long articles in Wikipedia, Wudao, and mC4 to address the shortage of long-document retrieval data (Paper, Section 3.1, Table 7).

### Motivation:
The goal of the data curation was to create a comprehensive dataset to train a versatile embedding model. The unsupervised data provides broad semantic knowledge, the labeled data fine-tunes the model for specific retrieval tasks, and the synthetic data improves long-document capabilities (Paper, Section 3.1).

### Preprocessing:
*   Raw data was filtered to remove "potential bad contents and low-relevance samples" (Paper, Section 3.1).
*   For long texts in the unsupervised data, a random shuffling strategy was applied to segments of the text to prevent the model from relying only on initial sentences for context (Paper, Appendix A.1).

---

## Quantitative Analyses
### Unitary results:
The model's performance was extensively evaluated and compared against several baselines, including BM25, mDPR, mContriever, mE5large, E5mistral-7b, and OpenAI's text-embedding-3-large.

*   **MIRACL (Multi-lingual Retrieval, nDCG@10):** M3-Embedding (All) achieves an average score of 71.5, outperforming all baselines. The Dense-only version scores 69.2, which is also superior to previous state-of-the-art models like mE5large (66.6) (Paper, Table 1).
*   **MKQA (Cross-lingual Retrieval, Recall@100):** M3-Embedding (All) achieves an average score of 75.5. The Dense-only version scores 75.1, outperforming all baselines, including E5mistral-7b (70.1) and OpenAI-3 (69.5) (Paper, Table 2).
*   **MLDR (Multilingual Long-Doc Retrieval, nDCG@10):** M3-Embedding (All) achieves an average score of 65.0. The Sparse (62.2) and Dense+Sparse (64.8) versions significantly outperform all other methods, including BM25 (53.6) and E5mistral-7b (42.6) (Paper, Table 3).
*   **NarrativeQA (English Long-Doc Retrieval, nDCG@10):** M3-Embedding (All) achieves a score of 61.7, outperforming all baselines, including text-embedding-3-large (51.6) and E5mistral-7b (49.9) (Paper, Table 4).
*   **Ablation Studies:** Disabling self-knowledge distillation (M3-w.o.skd) significantly degrades performance, especially for the sparse method (from 53.9 to 36.7 on MIRACL) (Paper, Table 5). The multi-stage training process shows clear benefits, with each stage (RetroMAE pre-training, unsupervised pre-training, fine-tuning) contributing to the final performance (Paper, Table 6).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
*   The initial RetroMAE pre-training was conducted on 32 A100 (40GB) GPUs (Paper, Appendix B.1).
*   The unsupervised data training stage was conducted on 96 A800 (80GB) GPUs (Paper, Appendix B.1).
*   The final fine-tuning stage with self-knowledge distillation was conducted on 24 A800 (80GB) GPUs (Paper, Appendix B.1).

---

## Ethical Considerations
The authors state that since the model will be publicly available, it is "influenced by the inherent impacts of open-source model" (Paper, Ethical Considerations). They acknowledge that the training data has an uneven distribution across languages, which may lead to performance variations. This "could potentially be seen as discriminatory or unfair" (Paper, Ethical Considerations). The authors state that their work conforms to the ACL Ethics Policy (Paper, Ethical Considerations).

---

## Caveats and Recommendations
### Caveats:
*   **Generalizability:** While the model shows state-of-the-art performance on several benchmarks, its generalizability to other diverse datasets and real-world scenarios requires further investigation (Paper, Limitations).
*   **Extremely Long Documents:** The model is designed for inputs up to 8192 tokens. Its performance and efficiency on documents exceeding this limit have not been investigated and could pose challenges (Paper, Limitations).
*   **Language Performance Variation:** The model supports over 100 languages, but performance may vary across them due to imbalances in the training data. The paper does not provide a thorough analysis of these variations (Paper, Limitations).

### Recommendations:
*   For optimal performance, a hybrid retrieval approach combining dense, sparse, and multi-vector scores is recommended (Paper, Section 4.1). The paper suggests specific weights for different datasets (e.g., w1=1, w2=0.3, w3=1 for MIRACL; w1=0.15, w2=0.5, w3=0.35 for MLDR) (Paper, Section 4.1, 4.3).
*   For users with limited computational resources or no access to long-document training data, the paper recommends the MCLS inference strategy to improve long-document retrieval performance without retraining the model (Paper, Appendix B.2).