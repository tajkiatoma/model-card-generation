## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from BAAI (Beijing Academy of Artificial Intelligence) and the University of Science and Technology of China (2402.03216.pdf, p. 1). The authors are Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu (2402.03216.pdf, p. 1).

### Model date:
The academic paper describing the model is version 4, dated June 28, 2024 (2402.03216.pdf, p. 1).

### Model version:
The model is named M3-Embedding (2402.03216.pdf, p. 1). The paper does not specify a numerical version but describes different functional components and combinations that can be used:
*   **Dense:** For dense vector retrieval (2402.03216.pdf, p. 4).
*   **Sparse:** For lexical/sparse retrieval (2402.03216.pdf, p. 4).
*   **Multi-vec:** For multi-vector retrieval using fine-grained interactions (2402.03216.pdf, p. 4).
*   **Dense+Sparse:** A hybrid method combining dense and sparse retrieval (2402.03216.pdf, p. 6).
*   **All:** A hybrid method combining all three retrieval functionalities (2402.03216.pdf, p. 6).

### Model type:
M3-Embedding is a text embedding model designed for versatility in multi-linguality, multi-functionality, and multi-granularity (2402.03216.pdf, p. 1).

*   **Architecture:** The model is based on a Transformer architecture, specifically a pre-trained XLM-ROBERTa model adapted with the RetroMAE method (2402.03216.pdf, p. 5, 14). The overall structure follows a `Transformer` -> `Pooling` -> `Normalize` sequence (modules.json.txt).
*   **Category:** It falls under the category of information retrieval and semantic representation. It unifies three common retrieval functionalities: dense retrieval, sparse (lexical) retrieval, and multi-vector retrieval (2402.03216.pdf, p. 1).
*   **Size and Context Length:** The model supports a maximum context length of 8,192 tokens (2402.03216.pdf, p. 1; tokenizer_config.json.txt).

### Training details:
The model was trained using a multi-stage workflow (2402.03216.pdf, p. 5, Figure 2).

*   **Stage 1: Pre-training:** The text encoder, an XLM-ROBERTa model adapted by the RetroMAE method, is first pre-trained on massive unsupervised data (184 million text samples covering 105 languages) (2402.03216.pdf, p. 5, 14). This stage uses a basic form of contrastive learning for dense retrieval (2402.03216.pdf, p. 5).
*   **Stage 2: Fine-tuning with Self-Knowledge Distillation:** The model is then fine-tuned on a combination of labeled and synthetic data to establish all three retrieval functionalities (dense, sparse, multi-vector) (2402.03216.pdf, p. 5). A novel self-knowledge distillation framework is used, where relevance scores from the different retrieval methods are integrated to create a "teacher" signal, enhancing the learning process (2402.03216.pdf, p. 1, 4). The training objective is to minimize the InfoNCE loss (2402.03216.pdf, p. 4).
*   **Hyperparameters:** During pre-training, the learning rate was 7e-5 with a batch size of 32 and 16 gradient accumulation steps (2402.03216.pdf, p. 14). During the main training phase on unsupervised data, the learning rate was 5e-5 with a weight decay of 0.01 and a warmup ratio of 0.1 (2402.03216.pdf, p. 14).
*   **Optimization:** An efficient batching strategy was employed, grouping data by sequence length and using gradient checkpointing to enable large batch sizes and high training throughput, especially for long sequences (2402.03216.pdf, p. 5).

### Paper or other resource for more information:
*   **Academic Paper:** Chen, J., Xiao, S., Zhang, P., Luo, K., Lian, D., & Liu, Z. (2024). *M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation*. arXiv preprint arXiv:2402.03216. (2402.03216.pdf).
*   **Repository:** The model, code, and data are publicly available at https://github.com/FlagOpen/FlagEmbedding (2402.03216.pdf, p. 1, footnote 1).

### Citation details:
Insufficient information. The provided repository does not contain a pre-formatted BibTeX citation.

### License:
The paper states that "The model, code, and data is publicly available" (2402.03216.pdf, p. 1, footnote 1). However, the specific license (e.g., Apache 2.0, MIT) is not mentioned in the provided documents.

### Contact:
Contact can be made with the authors via the email addresses provided in the academic paper (2402.03216.pdf, p. 1):
*   stxiao@baai.ac.cn
*   {namespace.pt, luokun695, zhengliu1026}@gmail.com
*   chenjianlv@mail.ustc.edu.cn
*   liandefu@ustc.edu.cn

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
M3-Embedding is designed as a versatile text embedding model for information retrieval tasks across multiple languages, functionalities, and text lengths (2402.03216.pdf, p. 1).

*   **Multi-Lingual and Cross-Lingual Retrieval:** It supports semantic retrieval for over 100 languages, enabling both retrieval within a single language and across different languages (e.g., a non-English query to search an English document corpus) (2402.03216.pdf, p. 1-2).
*   **Multi-Functional Retrieval:** It can be used for:
    *   **Dense Retrieval:** Retrieving documents based on the similarity of a single embedding vector (the `[CLS]` token's representation) (2402.03216.pdf, p. 4).
    *   **Sparse/Lexical Retrieval:** Estimating the importance of each term (token) in a text to facilitate lexical matching (2402.03216.pdf, p. 4).
    *   **Multi-Vector Retrieval:** Computing fine-grained relevance scores based on interactions between all token embeddings of a query and a document (2402.03216.pdf, p. 4).
*   **Multi-Granularity Processing:** It is capable of processing inputs of varying lengths, from short sentences to long documents of up to 8,192 tokens (2402.03216.pdf, p. 1).
*   **Input-Output Structure:** The model takes text as input and outputs embeddings that can be used to compute relevance scores for retrieval tasks (2402.03216.pdf, p. 4).

### Primary intended users:
The primary intended users are researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who need to build or improve semantic search and retrieval systems, especially for multilingual or long-document applications (2402.03216.pdf, p. 1-2).

### Out-of-scope uses:
The provided documents do not explicitly list out-of-scope uses. However, the "Limitations" section suggests areas where the model may not perform optimally (2402.03216.pdf, p. 9):
*   The model's performance on "very long documents or documents exceeding the specified token limit [of 8192 tokens] needs to be further investigated."
*   The model is not a generative model and is not intended for tasks like text generation, summarization, or translation. Its purpose is to generate embeddings for retrieval.

---

## How to Use
This section outlines how to use the model.

The model can be used to generate embeddings for various retrieval strategies. The core idea is to encode a query and a set of documents into embeddings and then compute a relevance score between them (2402.03216.pdf, p. 4).

*   **Dense Retrieval:**
    1.  Input a query and a document into the model.
    2.  Use the normalized hidden state of the `[CLS]` token as the embedding for each.
    3.  The relevance score is the inner product of the query and document embeddings (2402.03216.pdf, p. 4).
*   **Sparse (Lexical) Retrieval:**
    1.  Input a query and a document into the model.
    2.  For each token, compute a term weight using its hidden state.
    3.  The relevance score is calculated based on the joint importance of co-occurring terms between the query and the document (2402.03216.pdf, p. 4).
*   **Multi-Vector Retrieval:**
    1.  Input a query and a document into the model to get their full sequences of token embeddings.
    2.  Use a late-interaction mechanism to compute a fine-grained relevance score by finding the maximum similarity for each query token embedding across all document token embeddings and averaging these maximums (2402.03216.pdf, p. 4).
*   **Hybrid Retrieval:**
    The scores from the individual methods can be combined in a weighted sum to re-rank candidate documents for improved performance. The weights depend on the downstream scenario (2402.03216.pdf, p. 4). For example, on the MLDR benchmark, the weights for the "All" method were `w1=0.15` (dense), `w2=0.5` (sparse), and `w3=0.35` (multi-vec) (2402.03216.pdf, p. 8).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is designed to be multilingual, but performance can vary across languages. This is attributed to the uneven distribution of training data for different languages (2402.03216.pdf, p. 9).
*   **Input Length (Granularity):** The model is designed to handle inputs up to 8,192 tokens. Performance is shown to vary with sequence length, with the model demonstrating a growing advantage over baselines as sequence length increases (2402.03216.pdf, p. 8, Figure 5).
*   **Retrieval Task Type:** The model's performance differs between multi-lingual, cross-lingual, and long-document retrieval tasks. For instance, the sparse retrieval component is less effective in cross-lingual scenarios where there are few overlapping terms between languages (2402.03216.pdf, p. 7).

### Evaluation factors:
The model evaluations are disaggregated by the relevant factors identified above:
*   **Language:** Performance is reported for each individual language in the MIRACL, MKQA, and MLDR benchmarks (2402.03216.pdf, Tables 1, 2, 3).
*   **Task:** Separate evaluations are conducted for multi-lingual retrieval (MIRACL), cross-lingual retrieval (MKQA), and long-document retrieval (MLDR, NarrativeQA) (2402.03216.pdf, p. 6-8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics are used to evaluate the model's retrieval performance:
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10):** This is the primary metric for evaluating multi-lingual retrieval on the MIRACL benchmark and long-document retrieval on MLDR and NarrativeQA (2402.03216.pdf, p. 6, 8).
*   **Recall@100:** This is the primary metric for evaluating cross-lingual retrieval on the MKQA benchmark (2402.03216.pdf, p. 7).
*   **Recall@20:** Used as an auxiliary metric for the MKQA benchmark (2402.03216.pdf, p. 7).

### Decision thresholds:
For hybrid retrieval, the model uses weights to combine the scores from different retrieval methods. These weights act as decision parameters and are set based on the specific task (2402.03216.pdf, p. 4). For example:
*   For **MIRACL (Dense+Sparse)**: `w1=1` (dense), `w2=0.3` (sparse) (2402.03216.pdf, p. 6).
*   For **MLDR (All)**: `w1=0.15` (dense), `w2=0.5` (sparse), `w3=0.35` (multi-vec) (2402.03216.pdf, p. 8).

### Variation approaches:
Insufficient information. The paper reports performance on standard evaluation datasets but does not describe using statistical methods like bootstrapping or cross-validation to estimate uncertainty or variance in the performance metrics.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several public benchmarks (2402.03216.pdf, p. 6-8):
*   **MIRACL:** An ad-hoc retrieval dataset covering 18 diverse languages for multi-lingual retrieval evaluation (2402.03216.pdf, p. 6).
*   **MKQA:** A cross-lingual retrieval benchmark with queries in 25 non-English languages used to retrieve answers from the English Wikipedia corpus (2402.03216.pdf, p. 7).
*   **MLDR (Multilingual Long-Doc Retrieval):** A benchmark created from multilingual articles from Wikipedia, Wudao, and mC4 for evaluating long-document retrieval (2402.03216.pdf, p. 8).
*   **NarrativeQA:** An English-only benchmark for long-document retrieval (2402.03216.pdf, p. 8).

### Motivation:
These datasets were chosen because they are popular and standard benchmarks for testing the model's key capabilities: multi-lingual retrieval (MIRACL), cross-lingual retrieval (MKQA), and long-document retrieval (MLDR, NarrativeQA) (2402.03216.pdf, p. 2, 6-8).

### Preprocessing:
*   For MIRACL evaluation, the Pyserini toolkit was used, following the official benchmark guidelines (2402.03216.pdf, p. 6).
*   For MKQA evaluation, the well-processed English Wikipedia corpus from the BEIR benchmark was used (2402.03216.pdf, p. 7).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
A comprehensive, multi-source dataset was curated for training (2402.03216.pdf, p. 3, Table 8).
*   **Unsupervised Data (1.2 billion text pairs):** This data was extracted from large multilingual corpora, including Wikipedia, S2ORC, xP3, mC4, and CC-News. It also includes parallel sentences from translation datasets like NLLB and CCMatrix to learn cross-lingual semantics. This data covers 194 languages (2402.03216.pdf, p. 3, Table 8).
*   **Fine-tuning Data (Labeled Corpora):**
    *   **English:** 1.1M samples from 8 datasets including MS MARCO, HotpotQA, NQ, and TriviaQA (2402.03216.pdf, p. 3, Table 8).
    *   **Chinese:** 386.6K samples from 7 datasets including DuReader, T2-Ranking, and NLI-zh (2402.03216.pdf, p. 3, Table 8).
    *   **Multilingual:** 88.9K samples from MIRACL and 41.4K from Mr.TyDi (2402.03216.pdf, p. 15, Table 8).
*   **Synthetic Data (MultiLongDoc):** To address the scarcity of long-document retrieval data, questions were generated from lengthy articles in Wikipedia, Wudao, and mC4 using GPT-3.5. This dataset contains 41.4K training samples (2402.03216.pdf, p. 3, 15).

### Motivation:
The datasets were chosen to be large-scale and diverse to provide a solid foundation for training a versatile model capable of handling many languages, retrieval functions, and input granularities (2402.03216.pdf, p. 3). The three data sources (unsupervised, labeled, synthetic) are complementary and used in different training stages (2402.03216.pdf, p. 3).

### Preprocessing:
*   Raw unsupervised data was filtered to "remove potential bad contents and low-relevance samples" (2402.03216.pdf, p. 3).
*   To prevent the model from only learning from the beginning of long documents, a random shuffling strategy was applied. Texts were divided into three segments, their order was shuffled, and then they were recombined. This was applied to passages with a probability of 0.2% during training (2402.03216.pdf, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive results disaggregated by individual factors.
*   **Performance by Language:** Tables 1, 2, 3, 12, 13, 14, and 15 in the paper show performance metrics (nDCG@10, Recall@100, Recall@20) for each language in the MIRACL, MKQA, and MLDR datasets (2402.03216.pdf, p. 6-8, 17-18).
*   **Performance by Model Component:** The tables also break down performance for different model versions (Dense, Sparse, Multi-vec, All), allowing for analysis of each retrieval functionality (2402.03216.pdf, p. 6-8).
*   **Performance by Input Length:** Figure 5 shows the nDCG@10 score on the NarrativeQA dataset for different maximum sequence lengths, comparing M3-Embedding (Dense) with a baseline model (2402.03216.pdf, p. 16).

### Intersectional results:
Insufficient information. The paper does not present results for combinations of factors (e.g., performance for a specific language on long-document tasks). The analyses focus on one primary factor at a time.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training process required significant computational resources (2402.03216.pdf, p. 14):
*   **Initial Pre-training (RetroMAE adaptation):** Conducted on 32 A100 (40GB) GPUs for 20,000 steps.
*   **Second Stage Pre-training (on 1.2B pairs):** Conducted on 96 A800 (80GB) GPUs for 25,000 steps.
*   **Fine-tuning Stage (with self-knowledge distillation):** Conducted on 24 A800 (80GB) GPUs.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper includes a dedicated "Ethics Consideration" section (2402.03216.pdf, p. 9).
*   **Data and Bias:** The model is trained on multilingual data covering many languages. However, the authors acknowledge that "due to the uneven distribution of training data for different languages, the model's performance may vary across languages, which could potentially be seen as discriminatory or unfair."
*   **Open Source Impact:** As the model is publicly available, it is "influenced by the inherent impacts of open-source model[s]."
*   **Mitigation:** The authors state that their work is conformant to the ACL Ethics Policy. No other specific risk mitigation strategies are detailed.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper's "Limitations" section highlights several areas for caution and future work (2402.03216.pdf, p. 9):
*   **Generalizability:** While the model achieves state-of-the-art performance on the tested benchmarks, its generalizability to other diverse datasets and real-world scenarios needs further investigation.
*   **Computational Cost:** Processing extremely long documents (beyond the 8192 token limit or in large volumes) could present challenges in terms of computational resources and efficiency.
*   **Language Coverage:** Although the model claims support for over 100 languages, the performance variations across this broad range of languages have not been thoroughly analyzed, especially for low-resource languages.

### Recommendations:
*   For users with limited computational resources or no access to long-text fine-tuning data, the paper proposes a simple strategy called **MCLS (Multiple CLS)**. This method involves inserting multiple `[CLS]` tokens throughout a long document during inference and averaging their embeddings. This was shown to significantly improve long-document retrieval performance without any additional training (2402.03216.pdf, p. 6, 8).
*   Users should be aware of potential performance disparities across different languages and test the model for their specific use case, especially if it involves low-resource languages (2402.03216.pdf, p. 9).