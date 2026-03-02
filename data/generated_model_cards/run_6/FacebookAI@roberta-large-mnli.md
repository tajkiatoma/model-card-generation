## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Facebook AI and the Paul G. Allen School of Computer Science & Engineering at the University of Washington (1907.11692.pdf, Page 1). The authors are:
*   Yinhan Liu (Facebook AI)
*   Myle Ott (Facebook AI)
*   Naman Goyal (Facebook AI)
*   Jingfei Du (Facebook AI)
*   Mandar Joshi (University of Washington)
*   Danqi Chen (Facebook AI)
*   Omer Levy (Facebook AI)
*   Mike Lewis (Facebook AI)
*   Luke Zettlemoyer (University of Washington, Facebook AI)
*   Veselin Stoyanov (Facebook AI)

### Model date:
The associated academic paper was submitted to arXiv on July 26, 2019 (1907.11692.pdf, Page 1).

### Model version:
This model is RoBERTa (Robustly Optimized BERT Pretraining Approach). It is presented as an improved recipe for training BERT models, resulting from a replication study of BERT pre-training that measures the impact of key hyperparameters and training data size (1907.11692.pdf, Page 1, Abstract). The key modifications from the original BERT include:
1.  Training the model for a longer duration, with larger batches, and on more data (1907.11692.pdf, Page 1, Abstract).
2.  Removing the Next Sentence Prediction (NSP) objective (1907.11692.pdf, Page 1, Abstract).
3.  Training on longer sequences (1907.11692.pdf, Page 1, Abstract).
4.  Dynamically changing the masking pattern applied to the training data (1907.11692.pdf, Page 1, Abstract).

### Model type:
RoBERTa is a Transformer-based language model pretrained for natural language understanding tasks. This specific version is `RobertaForSequenceClassification` (config.json.txt).

**Architecture Details:**
*   **Model Type:** `roberta` (config.json.txt).
*   **Architecture:** It follows the BERT-large architecture with 24 hidden layers (`num_hidden_layers`), a hidden size of 1024 (`hidden_size`), 16 attention heads (`num_attention_heads`), and a feed-forward network inner hidden size of 4096 (`intermediate_size`) (1907.11692.pdf, Page 6, Section 5; config.json.txt). This results in 355 million parameters (1907.11692.pdf, Page 6, Section 5).
*   **Activation Function:** GELU (`hidden_act`) (1907.11692.pdf, Page 2, Section 2.4; config.json.txt).
*   **Dropout:** Attention probability dropout is 0.1 (`attention_probs_dropout_prob`) and hidden layer dropout is 0.1 (`hidden_dropout_prob`) (config.json.txt).

**Tokenizer and Vocabulary:**
*   **Tokenizer Type:** Byte-Pair Encoding (BPE) at the byte level (1907.11692.pdf, Page 6, Section 4.4; tokenizer_summary.json.txt).
*   **Vocabulary Size:** 50,265 (`vocab_size`) (config.json.txt; tokenizer_summary.json.txt).
*   **Context Length:** The model supports a maximum sequence length of 514 tokens (`max_position_embeddings`) (config.json.txt). The tokenizer configuration specifies a `model_max_length` of 512 (tokenizer_config.json.txt).

### Training details:
RoBERTa is pretrained using a masked language model objective, similar to BERT, but with several key changes to the training procedure (1907.11692.pdf, Page 6, Section 5).

**Training Procedure Modifications:**
*   **Dynamic Masking:** Instead of a static mask performed once during data preprocessing, the masking pattern is generated every time a sequence is fed to the model (1907.11692.pdf, Page 4, Section 4.1).
*   **Input Format and Objective:** The model is trained with full sentences packed into sequences of up to 512 tokens, and the Next Sentence Prediction (NSP) loss is removed (1907.11692.pdf, Page 5, Section 4.2).
*   **Large Batches:** The model was trained with large mini-batches of 8,000 sequences (1907.11692.pdf, Page 6, Section 4.3).

**Optimization:**
*   **Optimizer:** Adam optimizer (1907.11692.pdf, Page 2, Section 2.4).
*   **Hyperparameters:**
    *   Adam β1: 0.9 (1907.11692.pdf, Page 13, Table 9).
    *   Adam β2: 0.98 (1907.11692.pdf, Page 13, Table 9).
    *   Adam ε: 1e-6 (1907.11692.pdf, Page 13, Table 9).
    *   Learning Rate: Peak learning rate of 4e-4 with a linear warmup and linear decay (1907.11692.pdf, Page 13, Table 9).
    *   Weight Decay: 0.01 (1907.11692.pdf, Page 13, Table 9).
    *   Dropout: 0.1 (1907.11692.pdf, Page 13, Table 9).
*   **Training Steps:** The model was trained for up to 500,000 steps (1907.11692.pdf, Page 7, Table 4).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   **Title:** RoBERTa: A Robustly Optimized BERT Pretraining Approach (1907.11692.pdf, Page 1).
*   **Summary:** The paper presents a replication study of BERT pretraining, identifying several key design choices and training strategies that improve performance. It introduces RoBERTa, which achieves state-of-the-art results on several NLU benchmarks by training BERT longer, with larger batches, on more data, and with a modified pretraining objective (1907.11692.pdf, Page 1, Abstract).
*   **Code Repository:** The paper states that models and code are available at `https://github.com/pytorch/fairseq` (1907.11692.pdf, Page 1, Footnote 1).

### Citation details:
The following BibTeX entry can be used to cite the paper:
```bibtex
@article{liu2019roberta,
  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
  journal={arXiv preprint arXiv:1907.11692},
  year={2019}
}
```
(Derived from 1907.11692.pdf)

### License:
The paper points to a GitHub repository for the code, but the license itself is not specified in the provided files (1907.11692.pdf, Page 1, Footnote 1).

### Contact:
Contact information for the authors is provided in the paper:
*   `{yinhanliu,myleott,naman,jingfeidu,danqi,omerlevy,mikelewis,lsz,ves}@fb.com`
*   `{mandar90,lsz}@cs.washington.edu`
(1907.11692.pdf, Page 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for Natural Language Understanding (NLU) and can be fine-tuned for various downstream tasks. The primary intended uses demonstrated in the paper are:
*   **Sentence-Pair Classification:** Tasks that require reasoning about the relationship between pairs of sentences, such as Natural Language Inference (e.g., MNLI, RTE) (1907.11692.pdf, Page 3, Section 3.3). This specific model checkpoint is configured for a 3-label classification task: `CONTRADICTION`, `NEUTRAL`, and `ENTAILMENT` (config.json.txt).
*   **Single-Sentence Classification:** Tasks like sentiment analysis (e.g., SST-2) or linguistic acceptability (e.g., CoLA) (1907.11692.pdf, Page 3, Section 3.3).
*   **Extractive Question Answering:** Tasks where the model must extract a span of text from a given context to answer a question (e.g., SQuAD, RACE) (1907.11692.pdf, Page 3, Section 3.3).

The model takes one or two segments of text as input and is pretrained to understand language, making it a general-purpose tool for a wide range of NLP tasks (1907.11692.pdf, Page 2, Section 2.1).

### Primary intended users:
The primary intended users are Natural Language Processing (NLP) researchers and developers who need a powerful pretrained model for fine-tuning on specific downstream tasks (inferred from the paper's content and publication venue).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model expects input sequences formatted with special tokens. For a single sequence, the format is `<s> text </s>`. For a pair of sequences, the format is `<s> text1 </s></s> text2 </s>` (tokenizer_summary.json.txt, post_processor section; 1907.11692.pdf, Page 2, Section 2.1). The total sequence length should not exceed the model's maximum length of 512 tokens (tokenizer_config.json.txt).

This particular checkpoint is a sequence classification model fine-tuned for a task with three labels (config.json.txt):
*   `0`: CONTRADICTION
*   `1`: NEUTRAL
*   `2`: ENTAILMENT

Code snippets and sample input-outputs are not available in the provided repository.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The research paper focuses on factors related to the training procedure and data, rather than demographic or environmental factors. The key factors identified and analyzed for their impact on performance are:
*   **Masking Strategy:** Static vs. Dynamic masking of input tokens (1907.11692.pdf, Page 4, Section 4.1).
*   **Model Input Format and Pretraining Objective:** The use or removal of the Next Sentence Prediction (NSP) loss (1907.11692.pdf, Page 4, Section 4.2).
*   **Batch Size:** Training with different batch sizes (e.g., 256, 2K, 8K) (1907.11692.pdf, Page 5, Section 4.3).
*   **Training Data Size:** The amount of data used for pretraining (16GB vs. 160GB) (1907.11692.pdf, Page 7, Table 4).
*   **Number of Training Steps:** The duration of pretraining (100K, 300K, 500K steps) (1907.11692.pdf, Page 7, Table 4).

### Evaluation factors:
The model's performance is evaluated based on the training procedure factors listed above. The paper presents disaggregated results to show how each of these factors contributes to the final performance (1907.11692.pdf, Section 4 & 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is measured using standard metrics for the GLUE, SQuAD, and RACE benchmarks. These include:
*   **Accuracy:** Used for tasks like MNLI, QNLI, RTE, SST-2, and RACE (1907.11692.pdf, Page 5, Table 2; Page 8, Table 5).
*   **F1 Score:** Used for question answering tasks like SQuAD (1907.11692.pdf, Page 4, Table 1).
*   Other GLUE metrics such as Matthew's Correlation Coefficient (for CoLA) and Pearson/Spearman correlation (for STS) are also used for evaluation on the full benchmark (1907.11692.pdf, Page 8, Table 5).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robust measurements, the development set results are reported as the median over 5 random initializations (seeds) for each task (1907.11692.pdf, Page 5, Table 2 caption). For the final test set submissions to the GLUE leaderboard, ensembles of 5 to 7 models per task were used (1907.11692.pdf, Page 7, Section 5.1).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three standard NLU benchmarks (1907.11692.pdf, Page 3, Section 3.3):
1.  **GLUE (General Language Understanding Evaluation):** A collection of 9 datasets for single-sentence and sentence-pair classification tasks, including MNLI, QNLI, QQP, RTE, SST-2, MRPC, CoLA, STS-B, and WNLI.
2.  **SQuAD (Stanford Question Answering Dataset):** Versions v1.1 and v2.0 were used. This is an extractive question answering task.
3.  **RACE (ReAding Comprehension from Examinations):** A large-scale reading comprehension dataset collected from English examinations for middle and high school students.

### Motivation:
These datasets were chosen because they are widely used benchmarks for evaluating the performance of general-purpose natural language understanding systems (1907.11692.pdf, Page 3, Section 3.3).

### Preprocessing:
For most tasks, the finetuning procedure follows the original BERT paper (1907.11692.pdf, Page 3, Section 3.3). However, some task-specific modifications were made:
*   **QNLI:** A pairwise ranking formulation was adopted for the test submission (1907.11692.pdf, Page 8, Section 5.1).
*   **WNLI:** The data was reformatted to indicate the span of the query pronoun and referent, and a margin ranking loss was used (1907.11692.pdf, Page 8, Section 5.1).
*   **SQuAD v2.0:** An additional binary classifier was trained jointly with the span predictor to determine if a question is answerable (1907.11692.pdf, Page 4).
*   **RACE:** Each of the four candidate answers was concatenated with the corresponding question and passage to form four input sequences, which are then classified (1907.11692.pdf, Page 9, Section 5.3).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on a combination of five English-language corpora, totaling over 160GB of uncompressed text (1907.11692.pdf, Page 3, Section 3.2):
*   **BOOKCORPUS:** The original dataset used to train BERT (16GB).
*   **English WIKIPEDIA:** The original dataset used to train BERT (16GB).
*   **CC-NEWS:** A dataset collected from the English portion of the CommonCrawl News dataset, containing 63 million articles (76GB after filtering).
*   **OPENWEBTEXT:** An open-source recreation of the WebText corpus, with content extracted from URLs shared on Reddit (38GB).
*   **STORIES:** A dataset from Trinh and Le (2018) containing a subset of CommonCrawl data filtered to match a story-like style (31GB).

### Motivation:
The datasets were chosen to explore the impact of training data size and diversity on model performance. The collection of a large new dataset (CC-NEWS) and the use of other publicly available corpora were intended to better control for training set size effects compared to previous work that used private datasets (1907.11692.pdf, Page 1, Abstract; Page 3, Section 3.2).

### Preprocessing:
The text was encoded using a byte-level Byte-Pair Encoding (BPE) vocabulary. A key aspect of the preprocessing is its simplicity: no additional preprocessing or tokenization of the input was performed beyond the BPE encoding (1907.11692.pdf, Page 6, Section 4.4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by different training procedure choices.

**Effect of Model Input Format and NSP Loss (BERT-BASE on BOOKCORPUS + WIKIPEDIA):**
| Format | NSP Loss | SQuAD 2.0 (F1) | MNLI-m (Acc) | SST-2 (Acc) | RACE (Acc) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SEGMENT-PAIR | Yes | 78.7 | 84.0 | 92.9 | 64.2 |
| FULL-SENTENCES | No | 79.1 | 84.7 | 92.5 | 64.8 |
| DOC-SENTENCES | No | 79.7 | 84.7 | 92.7 | 65.6 |
(1907.11692.pdf, Page 5, Table 2)

**Effect of Batch Size (BERT-BASE on BOOKCORPUS + WIKIPEDIA):**
| Batch Size | Steps | Learning Rate | Perplexity | MNLI-m (Acc) | SST-2 (Acc) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 256 | 1M | 1e-4 | 3.99 | 84.7 | 92.7 |
| 2K | 125K | 7e-4 | 3.68 | 85.2 | 92.9 |
| 8K | 31K | 1e-3 | 3.77 | 84.6 | 92.8 |
(1907.11692.pdf, Page 6, Table 3)

### Intersectional results:
Insufficient information. The paper does not provide results for intersections of demographic or environmental factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
*   The initial pretraining experiments were conducted on DGX-1 machines, each with 8 x 32GB Nvidia V100 GPUs (1907.11692.pdf, Page 3, Section 3.1).
*   The final RoBERTa-large model was pretrained on 1024 V100 GPUs for approximately one day (1907.11692.pdf, Page 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information. The provided paper does not contain a discussion of ethical considerations.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Potential for Overfitting:** The paper notes that even the model trained for the longest duration (500K steps) did not appear to overfit the data and would likely benefit from additional training (1907.11692.pdf, Page 7).
*   **Text Encoding:** The comparison between character-level BPE and byte-level BPE was not exhaustive, and the authors note that a more detailed comparison is an area for future work (1907.11692.pdf, Page 6, Section 4.4).
*   **Data Analysis:** The experiments conflate increases in data size and diversity. A more careful analysis of these two dimensions is left to future work (1907.11692.pdf, Page 7, Footnote 9).

### Recommendations:
*   **BERT was Undertrained:** The central finding is that the original BERT model was significantly undertrained. Users and developers should be aware that performance can be substantially improved by training longer, with larger batches, and over more data (1907.11692.pdf, Page 1, Abstract).
*   **Re-evaluate Design Choices:** The paper recommends reconsidering key design choices from the original BERT model. Specifically, removing the Next Sentence Prediction (NSP) objective was found to match or slightly improve performance on downstream tasks (1907.11692.pdf, Page 5, Section 4.2).
*   **Use Dynamic Masking:** For pretraining, dynamic masking is recommended as it is comparable or slightly better than static masking and is more efficient for longer training or larger datasets (1907.11692.pdf, Page 4, Section 4.1).