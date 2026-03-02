## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The M3-Embedding model was developed by researchers from the Beijing Academy of Artificial Intelligence (BAAI) and the University of Science and Technology of China (USTC). The authors are Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu (M3-Embedding Paper, Page 1).

### Model date:
The academic paper describing the model is version v4, dated June 28, 2024 (M3-Embedding Paper, Page 1).

### Model version:
The model is presented as M3-Embedding. The paper also evaluates several variations and ablation models to demonstrate the impact of different components (M3-Embedding Paper, Pages 8, 9):
*   **M3-Embedding (Full Model):** The complete model with all functionalities (Dense, Sparse, Multi-vec) and training stages.
*   **M3-w.o.long:** A version of the model fine-tuned without long document data to test the impact of this training stage.
*   **M3-w.o.skd:** A version trained without self-knowledge distillation, where each retrieval method is trained independently.

### Model type:
M3-Embedding is a text embedding model designed for multi-lingual, multi-functional, and multi-granularity semantic retrieval (M3-Embedding Paper, Page 1).

*   **Architecture:** The model is based on the XLM-RoBERTa architecture (config.json). It is a Transformer-based model with the following specifications:
    *   24 hidden layers (`num_hidden_layers`) (config.json).
    *   1024 hidden size (`hidden_size`) (config.json).
    *   4096 intermediate size (`intermediate_size`) (config.json).
    *   16 attention heads (`num_attention_heads`) (config.json).
    *   250,002 vocabulary size (`vocab_size`) (config.json).
*   **Size:** The model is an XLM-RoBERTa-large variant (M3-Embedding Paper, Page 14).
*   **Context Length:** The model supports a maximum sequence length of 8,192 tokens (sentence_bert_config.json; M3-Embedding Paper, Page 1).
*   **Functionality:** It is structured as a Sentence Transformers model that processes input through a Transformer, a Pooling layer (to create a fixed-size embedding), and a Normalize layer (modules.json).

### Training details:
The model was trained using a multi-stage workflow (M3-Embedding Paper, Page 5):
1.  **Pre-training on Unsupervised Data:** The XLM-RoBERTa encoder is first pre-trained using the RetroMAE method and then further trained on a massive unsupervised multilingual dataset of 1.2 billion text pairs. In this stage, only dense retrieval is trained using a basic contrastive learning objective (InfoNCE loss) (M3-Embedding Paper, Pages 5, 9, 14).
2.  **Fine-tuning with Self-Knowledge Distillation:** The model is then fine-tuned on a combination of labeled and synthetic data to establish its three retrieval functionalities (dense, sparse, multi-vector). A novel self-knowledge distillation framework is used, where the integrated relevance scores from all three retrieval methods act as a "teacher" signal to enhance the training of each individual method. This helps unify the optimization process and overcome conflicting training objectives (M3-Embedding Paper, Pages 2, 4).

Key parameters and techniques include:
*   **Loss Function:** The training minimizes the InfoNCE loss for positive and negative sample discrimination. The final loss is a combination of the standard InfoNCE loss and a modified loss function derived from the self-knowledge distillation process (M3-Embedding Paper, Pages 4, 5).
*   **Efficient Batching:** To handle diverse and long sequences efficiently, the training data is grouped by sequence length. For long sequences, mini-batches are split into smaller sub-batches, and gradient checkpointing is used to reduce memory usage. This allows for significantly larger effective batch sizes (M3-Embedding Paper, Page 5). For example, for text with a length of 8192, the batch size can be increased by more than 20 times (M3-Embedding Paper, Page 5, Appendix B.3).

### Paper or other resource for more information:
*   **Academic Paper:** Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*. arXiv:2402.03216v4. This paper provides a comprehensive overview of the model's architecture, training process, and evaluation.
*   **Repository:** The model, code, and data are publicly available at: https://github.com/FlagOpen/FlagEmbedding (M3-Embedding Paper, Page 1).

### Citation details:
Insufficient information. A BibTeX entry can be constructed from the paper details:
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

### License:
Insufficient information. The paper states the model is "publicly available" but does not specify a license (M3-Embedding Paper, Page 2).

### Contact:
Contact can be made with the authors via the emails provided in the paper (M3-Embedding Paper, Page 1):
*   `stxiao@baai.ac.cn`
*   `{namespace.pt, luokun695, zhengliu1026}@gmail.com`
*   `chenjianlv@mail.ustc.edu.cn`
*   `liandefu@ustc.edu.cn`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is a general-purpose text embedding model designed for versatile information retrieval tasks (M3-Embedding Paper, Page 1). Its primary capabilities are:
*   **Multi-Linguality:** Provides semantic retrieval support for over 100 languages, enabling both multilingual retrieval (query and document in the same language) and cross-lingual retrieval (query and document in different languages) (M3-Embedding Paper, Pages 1-2).
*   **Multi-Functionality:** Unifies three common retrieval functionalities into a single model:
    *   **Dense Retrieval:** Computes relevance based on the inner product of dense vector representations of a query and a document (using the `[CLS]` token embedding) (M3-Embedding Paper, Page 4).
    *   **Sparse Retrieval (Lexical):** Estimates the importance of each term (token) and computes a relevance score based on the co-occurring terms between a query and a document (M3-Embedding Paper, Page 4).
    *   **Multi-Vector Retrieval:** Uses the entire sequence of output embeddings (not just `[CLS]`) to compute a fine-grained relevance score via late-interaction, following the ColBERT methodology (M3-Embedding Paper, Page 4).
*   **Multi-Granularity:** Capable of processing inputs of varying lengths, from short sentences and passages to long documents up to 8,192 tokens (M3-Embedding Paper, Page 1).

The model can be used in hybrid retrieval systems where scores from dense, sparse, and multi-vector methods are combined to improve ranking performance (M3-Embedding Paper, Page 4).

### Primary intended users:
The primary intended users are researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who require a single, versatile model for various text retrieval tasks across multiple languages and document lengths.

### Out-of-scope uses:
The model is designed for generating text embeddings for retrieval tasks and should not be used for text generation. Other out-of-scope uses include:
*   **Exceeding Context Length:** The model's performance on documents significantly exceeding the 8,192 token limit has not been investigated and may be suboptimal (M3-Embedding Paper, Page 9).
*   **Making Critical Decisions:** The model should not be used to make automated, high-stakes decisions without human oversight, as its performance can vary across languages and domains.
*   **Harmful Use Cases:** The model should not be used for any purpose that is illegal, harmful, or promotes discrimination.

---

## How to Use
This section outlines how to use the model.

The model can be used to generate embeddings for various retrieval strategies. The official code is available at the project's GitHub repository (M3-Embedding Paper, Page 1). While specific code snippets are not provided in the paper, the usage is described based on its functionalities (M3-Embedding Paper, Page 4):

*   **Input-Output Structure:** The model takes text (queries or documents) as input and outputs embeddings. The specific embedding used depends on the retrieval method.
*   **Dense Retrieval:** Use the normalized hidden state of the `[CLS]` token as the dense vector representation for the entire text. The relevance score is the inner product of the query and document vectors.
*   **Sparse Retrieval:** The model outputs a weight for each token in the text. These weights are used to calculate a lexical matching score based on terms that co-occur in the query and the document.
*   **Multi-Vector Retrieval:** The entire sequence of output embeddings for each token is used. A fine-grained relevance score is computed using a late-interaction mechanism between the query's and the document's embeddings.
*   **Hybrid Retrieval:** The final ranking can be determined by a weighted sum of the scores from the dense, sparse, and multi-vector methods. The weights can be tuned for the specific downstream task (M3-Embedding Paper, Page 4).
*   **Long Document Inference (MCLS Method):** For users who cannot fine-tune the model on long documents, the paper proposes the MCLS (Multi-CLS) method for inference. This involves inserting a `[CLS]` token every 256 tokens into the long document. The final embedding for the document is the average of the last hidden states of all these `[CLS]` tokens (M3-Embedding Paper, Page 14).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The key factors that influence the model's performance are (M3-Embedding Paper, Pages 1, 9):
*   **Language:** The model is multilingual, but performance can vary across different languages. This is partly due to the uneven distribution of languages in the training data.
*   **Input Granularity (Sequence Length):** The model is designed to handle inputs of varying lengths, from short sentences to long documents. Its performance relative to other models changes with sequence length.
*   **Dataset Characteristics:** The model's generalizability to different datasets and real-world scenarios may vary, as different data sources have unique characteristics and challenges.

### Evaluation factors:
The model's performance is evaluated and reported based on the following factors:
*   **Language:** Performance is disaggregated by language in the MIRACL (18 languages), MKQA (25 languages), and MLDR (13 languages) benchmarks (M3-Embedding Paper, Tables 1, 2, 3).
*   **Sequence Length:** Performance on the NarrativeQA benchmark is analyzed with respect to varying maximum sequence lengths (128 to 8192 tokens) to demonstrate its proficiency in handling long inputs (M3-Embedding Paper, Figure 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics are used to evaluate the model's retrieval effectiveness on different benchmarks (M3-Embedding Paper, Pages 6, 7, 8):
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** This is the primary metric for evaluating ranking quality on the MIRACL (multilingual retrieval) and MLDR (long-document retrieval) benchmarks.
*   **Recall@100 (Recall at 100):** This is the primary metric for the MKQA (cross-lingual retrieval) benchmark, measuring the percentage of queries for which a correct answer is found within the top 100 retrieved documents.

### Decision thresholds:
For hybrid retrieval, the model's final ranking score is a weighted combination of scores from different retrieval methods. These weights act as decision thresholds that are set based on the specific benchmark (M3-Embedding Paper, Pages 6, 8):
*   **MIRACL (Dense+Sparse):** `s_rank = 1.0 * s_dense + 0.3 * s_sparse`
*   **MIRACL (All):** `s_rank = 1.0 * s_dense + 0.3 * s_sparse + 1.0 * s_mul` (on top-200 candidates from Dense)
*   **MLDR (Dense+Sparse):** `s_rank = 0.2 * s_dense + 0.8 * s_sparse`
*   **MLDR (All):** `s_rank = 0.15 * s_dense + 0.5 * s_sparse + 0.35 * s_mul`

### Variation approaches:
Insufficient information. The paper reports point estimates of performance metrics on standard test/dev sets but does not describe methods like bootstrapping or cross-validation to estimate uncertainty.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several standard public benchmarks (M3-Embedding Paper, Pages 6-8):
*   **MIRACL (Multilingual Retrieval):** A benchmark for ad-hoc retrieval tasks in 18 diverse languages. Each task consists of queries and passages in the same language (M3-Embedding Paper, Page 6).
*   **MKQA (Cross-Lingual Retrieval):** A benchmark with queries in 25 non-English languages that must be used to retrieve answers from the English Wikipedia corpus (M3-Embedding Paper, Page 7).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark curated from multilingual articles from Wikipedia, Wudao, and mC4. It covers 13 languages and focuses on long-document retrieval (M3-Embedding Paper, Page 8).
*   **NarrativeQA (English Long-Doc Retrieval):** An English-only benchmark for evaluating retrieval performance on longer sequences (M3-Embedding Paper, Page 8).

### Motivation:
These datasets were chosen because they are established and challenging benchmarks that allow for a comprehensive evaluation of the model's core capabilities: multi-linguality (MIRACL), cross-linguality (MKQA), and multi-granularity/long-document handling (MLDR, NarrativeQA) (M3-Embedding Paper, Pages 6-8).

### Preprocessing:
The evaluation process followed standard procedures for these benchmarks (M3-Embedding Paper, Pages 6-7):
*   For MIRACL, embeddings were generated for the corpus. A dense index was built using Faiss for candidate retrieval, and a sparse index was built using Lucene.
*   For MKQA, the well-processed English Wikipedia corpus provided by the BEIR benchmark was used.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
A large-scale, diverse, and multilingual dataset was curated from three sources, totaling over 1.2 billion text pairs (M3-Embedding Paper, Page 3, Table 8):
1.  **Unsupervised Data (1.2B pairs):** This data was created by extracting semantically related text pairs (e.g., title-body, instruction-output) from massive multilingual corpora. Sources include MTP, S2ORC, Wikipedia, xP3, mC4, and CC-News. For cross-lingual learning, parallel sentences were sourced from NLLB and CCMatrix (M3-Embedding Paper, Page 3).
2.  **Fine-tuning Data (Labeled):** High-quality labeled datasets were collected for English, Chinese, and other languages.
    *   **English (1.1M):** MS MARCO, HotpotQA, NQ, TriviaQA, SQuAD, NLI, etc.
    *   **Chinese (386.6K):** DuReader, T2-Ranking, NLI-zh, etc.
    *   **Multilingual (88.9K):** MIRACL, Mr.TyDi.
3.  **Synthetic Data (41.4K):** To address the scarcity of long-document retrieval data, a new dataset called `MultiLongDoc` was created. Long articles were sampled from Wikipedia, Wudao, and mC4, and GPT-3.5 was used to generate corresponding questions (M3-Embedding Paper, Page 3).

### Motivation:
The goal was to create a comprehensive training resource to build a versatile embedding model. The three data sources are complementary: the massive unsupervised data provides broad semantic understanding, the high-quality labeled data fine-tunes the model for specific retrieval tasks, and the synthetic data fills the gap for long-document retrieval (M3-Embedding Paper, Pages 2-3).

### Preprocessing:
The following preprocessing steps were applied to the training data:
*   The raw data was filtered to remove low-relevance samples and potentially harmful content (M3-Embedding Paper, Page 3).
*   For long texts in the unsupervised data (e.g., from CC-News), the document was divided into three segments which were then randomly shuffled. This was done to prevent the model from only learning from the summarizing statements typically found at the beginning of articles (M3-Embedding Paper, Page 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance was analyzed for each language across different benchmarks.
*   **Multilingual Retrieval (MIRACL, nDCG@10):** The full model (`All`) achieves a state-of-the-art average score of 71.5. It shows a consistent advantage in most individual languages, outperforming baselines like mE5-large and E5mistral-7b (M3-Embedding Paper, Table 1). For example, scores range from 59.6 (English) to 83.5 (Yoruba).
*   **Cross-Lingual Retrieval (MKQA, Recall@100):** The full model (`All`) achieves an average score of 75.5, outperforming all baselines. It maintains a relatively stable and high performance across all 25 languages, including low-resource ones where other models struggle (e.g., `ar`, `km`, `he`) (M3-Embedding Paper, Table 2).
*   **Long-Document Retrieval (MLDR, nDCG@10):** The full model (`All`) achieves an average score of 65.0. The sparse functionality is particularly effective on this benchmark, scoring 62.2 on its own. The model outperforms strong baselines like OpenAI's text-embedding-3-large and E5mistral-7b across nearly all 13 languages (M3-Embedding Paper, Table 3).

### Intersectional results:
The paper analyzes performance by the intersection of language (English only) and sequence length on the NarrativeQA dataset (M3-Embedding Paper, Figure 5).
*   **Performance vs. Sequence Length (NarrativeQA, nDCG@10):** M3-Embedding's performance advantage over baselines like jina-embeddings-v2-base-en grows as the sequence length increases.
    *   At 128 tokens: 19.6
    *   At 512 tokens: 22.2
    *   At 4096 tokens: 39.4
    *   At 8192 tokens: 48.7
This demonstrates the model's proficiency in handling long contexts.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on high-performance GPUs (M3-Embedding Paper, Page 14):
*   **Initial Pre-training (RetroMAE):** Conducted on 32 A100 (40GB) GPUs for 20,000 steps.
*   **Unsupervised Data Stage:** Conducted on 96 A800 (80GB) GPUs for 25,000 steps.
*   **Fine-tuning Stage (Self-Knowledge Distillation):** Conducted on 24 A800 (80GB) GPUs.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The authors include an "Ethics Consideration" section in their paper (M3-Embedding Paper, Page 9).
*   **Data and Open Source Impact:** The model will be publicly available and is therefore influenced by the inherent impacts and potential biases of open-source models. The training data is multilingual and includes a wide variety of languages.
*   **Risk of Performance Disparity:** The authors acknowledge that the training data is unevenly distributed across languages. This may cause the model's performance to vary, which "could potentially be seen as discriminatory or unfair."
*   **Mitigation and Compliance:** The authors state that their work is conformant to the ACL Ethics Policy. Further analysis and evaluation on a broader range of languages are noted as necessary to better understand the model's robustness and effectiveness across different language families (M3-Embedding Paper, Page 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors list several limitations in the paper (M3-Embedding Paper, Page 9):
*   **Generalizability:** While the model achieves state-of-the-art performance on popular benchmarks, its generalizability to other diverse datasets and real-world scenarios requires further investigation.
*   **Extremely Long Documents:** The model is designed for inputs up to 8,192 tokens. Processing documents that significantly exceed this limit could pose challenges in terms of computational resources and model efficiency, and performance may degrade.
*   **Language Performance Variation:** The paper claims support for over 100 languages, but the potential variations in performance across this broad range of languages are not thoroughly discussed. Further analysis is needed to understand its robustness across different language families.

### Recommendations:
*   **Hybrid Retrieval Tuning:** For users implementing hybrid retrieval, the weights for combining dense, sparse, and multi-vector scores should be tuned for the specific downstream scenario to achieve optimal performance (M3-Embedding Paper, Page 4).
*   **Long-Document Retrieval without Fine-tuning:** For users with limited computational resources who cannot fine-tune the model on long-document data, the paper recommends using the **MCLS (Multiple CLS)** method at inference time. This simple but effective strategy can significantly improve long-document retrieval performance without any additional training (M3-Embedding Paper, Page 8).