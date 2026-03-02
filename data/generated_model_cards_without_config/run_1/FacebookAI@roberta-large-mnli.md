## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from the Paul G. Allen School of Computer Science & Engineering at the University of Washington and Facebook AI (Source: 1907.11692.pdf, p. 1). The authors are Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov (Source: 1907.11692.pdf, p. 1).

### Model date:
The associated academic paper was submitted to arXiv on July 26, 2019 (Source: 1907.11692.pdf, p. 1).

### Model version:
The model is named RoBERTa (Robustly Optimized BERT Approach). It is presented as an improved recipe for pretraining BERT models (Source: 1907.11692.pdf, p. 1). RoBERTa differs from the original BERT (Devlin et al., 2019) through several modifications:
1.  Training the model for a longer duration, with larger batches, over more data (Source: 1907.11692.pdf, p. 1).
2.  Removing the Next Sentence Prediction (NSP) objective from the pretraining process (Source: 1907.11692.pdf, p. 1, 4).
3.  Training on longer sequences (Source: 1907.11692.pdf, p. 1, 3).
4.  Dynamically changing the masking pattern applied to the training data (Source: 1907.11692.pdf, p. 1, 4).

The paper evaluates two main configurations: `RoBERTa_BASE` and `RoBERTa_LARGE` (Source: 1907.11692.pdf, p. 12).

### Model type:
RoBERTa is a Transformer-based language model, following the architecture of BERT (Source: 1907.11692.pdf, p. 2). Key details include:
*   **Architecture**: It uses a multi-layer bidirectional Transformer architecture (Source: 1907.11692.pdf, p. 2).
    *   `RoBERTa_BASE`: L=12 layers, H=768 hidden dimension, A=12 self-attention heads, 110M parameters (Source: 1907.11692.pdf, p. 4, 13).
    *   `RoBERTa_LARGE`: L=24 layers, H=1024 hidden dimension, A=16 self-attention heads, 355M parameters (Source: 1907.11692.pdf, p. 6, 13).
*   **Tokenizer**: It uses a byte-level Byte-Pair Encoding (BPE) with a vocabulary size of 50,265 (Source: 1907.11692.pdf, p. 6; tokenizer_summary.json.txt, model.vocab_size). The tokenizer does not require any preprocessing or heuristic tokenization of the input (Source: 1907.11692.pdf, p. 6).
*   **Context Length**: The model supports a maximum sequence length of 512 tokens (Source: 1907.11692.pdf, p. 3; tokenizer_config.json.txt, model_max_length).

### Training details:
RoBERTa's training is an optimized version of BERT's pretraining.
*   **Training Objective**: The model is trained using a masked language model (MLM) objective. It does not use the Next Sentence Prediction (NSP) loss used in the original BERT (Source: 1907.11692.pdf, p. 4).
*   **Masking Strategy**: RoBERTa uses *dynamic masking*, where the masking pattern is generated every time a sequence is fed to the model, unlike BERT's *static masking* which was done once during data preprocessing (Source: 1907.11692.pdf, p. 4).
*   **Input Format**: The model is trained on full sentences sampled contiguously from one or more documents, with a total length of at most 512 tokens (Source: 1907.11692.pdf, p. 5).
*   **Optimization**:
    *   **Optimizer**: Adam optimizer with parameters β1 = 0.9, β2 = 0.98, ε = 1e-6, and L2 weight decay of 0.01 (Source: 1907.11692.pdf, p. 2, 13). The β2 parameter was changed to 0.98 to improve stability with large batches (Source: 1907.11692.pdf, p. 3).
    *   **Batch Size**: Trained with large mini-batches of 8,000 sequences (Source: 1907.11692.pdf, p. 6, 13).
    *   **Learning Rate**: A peak learning rate of 4e-4 for `RoBERTa_LARGE` and 6e-4 for `RoBERTa_BASE`, with a linear warmup followed by a linear decay (Source: 1907.11692.pdf, p. 13).
    *   **Training Steps**: The final `RoBERTa_LARGE` model was trained for 500,000 steps (Source: 1907.11692.pdf, p. 7, 13).
*   **Other Details**: Training used a dropout of 0.1 on all layers and attention weights, and the GELU activation function (Source: 1907.11692.pdf, p. 2).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L., & Stoyanov, V. (2019). *RoBERTa: A Robustly Optimized BERT Pretraining Approach*. arXiv:1907.11692. (Source: 1907.11692.pdf).

The models and code are available at:
*   https://github.com/pytorch/fairseq (Source: 1907.11692.pdf, p. 1).

### Citation details:
```bibtex
@misc{liu2019roberta,
    title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
    author={Yinhan Liu and Myle Ott and Naman Goyal and Jingfei Du and Mandar Joshi and Danqi Chen and Omer Levy and Mike Lewis and Luke Zettlemoyer and Veselin Stoyanov},
    year={2019},
    eprint={1907.11692},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
(Source: Derived from 1907.11692.pdf)

### License:
Insufficient information.

### Contact:
Contact information for the authors is available in the paper, including emails at cs.washington.edu and fb.com domains (Source: 1907.11692.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is pretrained for general-purpose Natural Language Understanding (NLU). It is intended to be finetuned for various downstream tasks. The paper demonstrates its effectiveness on:
*   **Sentence-pair classification tasks**: Such as Natural Language Inference (e.g., MNLI, RTE) and Paraphrase Detection (e.g., QQP, MRPC) (Source: 1907.11692.pdf, p. 3, 8).
*   **Single-sentence classification tasks**: Such as sentiment analysis (SST-2) and linguistic acceptability (CoLA) (Source: 1907.11692.pdf, p. 3, 8).
*   **Extractive Question Answering**: As demonstrated on the SQuAD benchmark, where the task is to extract an answer span from a given context paragraph (Source: 1907.11692.pdf, p. 3, 9).
*   **Multiple Choice Question Answering**: As demonstrated on the RACE benchmark, where the task is to select the correct answer from four options based on a given passage (Source: 1907.11692.pdf, p. 4, 9).

### Primary intended users:
The primary intended users are Natural Language Processing (NLP) researchers and developers who require a powerful pretrained language model as a base for their specific downstream tasks (Source: 1907.11692.pdf, p. 1, 10).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model is implemented in the FAIRSEQ PyTorch library (Source: 1907.11692.pdf, p. 2). The code for pretraining and finetuning is available at https://github.com/pytorch/fairseq (Source: 1907.11692.pdf, p. 1).

The model expects input sequences of up to 512 tokens (Source: 1907.11692.pdf, p. 3). The input text is processed using a byte-level BPE tokenizer (Source: 1907.11692.pdf, p. 6). For tasks involving sentence pairs, the input is formatted with special tokens. The post-processor for the tokenizer is `RobertaProcessing`, which adds a start-of-sequence token (`<s>`) at the beginning and an end-of-sequence token (`</s>`) at the end of each sequence (Source: tokenizer_summary.json.txt, post_processor).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper identifies several key factors that significantly influence the model's performance on downstream tasks:
*   **Masking Strategy**: The choice between static masking (masking once during preprocessing) and dynamic masking (masking on-the-fly for each training step) (Source: 1907.11692.pdf, p. 4).
*   **Model Input Format and Pretraining Objective**: The effect of including or removing the Next Sentence Prediction (NSP) loss, and the format of input sequences (e.g., pairs of sentences vs. full sentences packed together) (Source: 1907.11692.pdf, p. 4-5).
*   **Batch Size**: The size of the mini-batches used during pretraining (Source: 1907.11692.pdf, p. 5).
*   **Training Data**: The size and diversity of the text corpora used for pretraining (Source: 1907.11692.pdf, p. 6-7).
*   **Training Duration**: The total number of training steps or passes over the data (Source: 1907.11692.pdf, p. 7).

### Evaluation factors:
The evaluation analyzes performance across the relevant factors listed above. For example:
*   Performance is compared between static and dynamic masking (Source: 1907.11692.pdf, Table 1, p. 4).
*   Performance is compared across different input formats and the presence/absence of the NSP loss (Source: 1907.11692.pdf, Table 2, p. 5).
*   Performance is compared for different batch sizes (Source: 1907.11692.pdf, Table 3, p. 6).
*   Performance is compared for models trained on different data sizes and for different numbers of steps (Source: 1907.11692.pdf, Table 4, p. 7).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using standard metrics for the respective benchmarks:
*   **GLUE**: Accuracy is used for most tasks (MNLI, QNLI, RTE, SST-2, WNLI). Matthews Correlation Coefficient is used for CoLA, and Pearson/Spearman correlation for STS-B. F1 score is also used for QQP and MRPC (Source: 1907.11692.pdf, p. 8, Table 5).
*   **SQuAD**: Exact Match (EM) and F1 score are used (Source: 1907.11692.pdf, p. 9, Table 6).
*   **RACE**: Accuracy is used (Source: 1907.11692.pdf, p. 9, Table 7).
*   **Pretraining**: Perplexity on a held-out training set is used to measure the performance of the masked language modeling objective (Source: 1907.11692.pdf, p. 6, Table 3).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For development set results on GLUE and SQuAD, the paper reports the median of 5 runs with different random initializations (seeds) to ensure robustness of the results (Source: 1907.11692.pdf, p. 4, 8). For GLUE test set submissions, an ensemble of 5 to 7 models per task is used (Source: 1907.11692.pdf, p. 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model is evaluated on three standard NLU benchmarks:
1.  **GLUE (General Language Understanding Evaluation)**: A collection of 9 datasets for single-sentence and sentence-pair classification tasks, including MNLI, QNLI, QQP, RTE, SST-2, MRPC, CoLA, and STS-B (Source: 1907.11692.pdf, p. 3).
2.  **SQuAD (Stanford Question Answering Dataset)**: Versions 1.1 and 2.0 are used for extractive question answering (Source: 1907.11692.pdf, p. 3).
3.  **RACE (ReAding Comprehension from Examinations)**: A large-scale multiple-choice reading comprehension dataset collected from English examinations for middle and high school students (Source: 1907.11692.pdf, p. 4).

### Motivation:
These datasets were chosen because they are widely-used benchmarks for evaluating the performance of general-purpose language understanding models, allowing for direct comparison with previous state-of-the-art models like BERT and XLNet (Source: 1907.11692.pdf, p. 1, 3).

### Preprocessing:
For most tasks, the finetuning procedure follows the original BERT paper (Source: 1907.11692.pdf, p. 3). However, some task-specific modifications were made for GLUE test set submissions:
*   **RTE, STS, MRPC**: Finetuning is started from the MNLI single-task model rather than the baseline pretrained model (Source: 1907.11692.pdf, p. 8).
*   **WNLI**: The data is reformatted to indicate the span of the query pronoun and referent, and a margin ranking loss is used (Source: 1907.11692.pdf, p. 8).
For the RACE task, each candidate answer is concatenated with the corresponding question and passage to form four separate input sequences for classification (Source: 1907.11692.pdf, p. 9).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
RoBERTa was pretrained on a combination of five English-language text corpora, totaling over 160GB of uncompressed text (Source: 1907.11692.pdf, p. 3). The datasets are:
1.  **BOOKCORPUS** plus **English WIKIPEDIA**: The original data used to train BERT (16GB) (Source: 1907.11692.pdf, p. 3).
2.  **CC-NEWS**: A dataset collected by the authors from the CommonCrawl News dataset, containing 63 million English news articles (76GB after filtering) (Source: 1907.11692.pdf, p. 3).
3.  **OPENWEBTEXT**: An open-source recreation of the WebText corpus, consisting of web content from URLs shared on Reddit (38GB) (Source: 1907.11692.pdf, p. 3).
4.  **STORIES**: A dataset from CommonCrawl filtered to match a story-like style (31GB) (Source: 1907.11692.pdf, p. 3).

### Motivation:
The motivation for collecting a larger dataset (160GB vs. the 16GB used for BERT) was to carefully measure the impact of training data size on end-task performance and to better control for this variable when comparing with other models like XLNet, which also used a very large private dataset (Source: 1907.11692.pdf, p. 1, 3, 7).

### Preprocessing:
The text is tokenized using a byte-level Byte-Pair Encoding (BPE) vocabulary. A key aspect of the preprocessing is its simplicity: unlike the original BERT, RoBERTa uses this BPE implementation without any additional preprocessing or heuristic tokenization of the input text (Source: 1907.11692.pdf, p. 6). The tokenizer uses a `ByteLevel` pre-tokenizer, which operates on raw bytes (Source: tokenizer_summary.json.txt, pre_tokenizer).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents several analyses of individual factors:
*   **Masking**: Dynamic masking performs comparably or slightly better than the static masking used in the original BERT. For example, on SQuAD 2.0, dynamic masking achieved an F1 score of 78.7, compared to 78.3 for static masking (Source: 1907.11692.pdf, Table 1, p. 4).
*   **NSP Loss**: Removing the Next Sentence Prediction (NSP) loss and training with packed full sentences (FULL-SENTENCES format) improved performance over the original BERT setup. For example, MNLI-m accuracy improved from 84.0% to 84.7% (Source: 1907.11692.pdf, Table 2, p. 5).
*   **Batch Size**: Training with larger batches improved performance. Increasing the batch size from 256 to 2K improved MNLI-m accuracy from 84.7% to 85.2% (Source: 1907.11692.pdf, Table 3, p. 6).
*   **Data Size & Training Steps**: Performance consistently improves with more data and longer training. Training on 160GB of data instead of 16GB improved MNLI-m accuracy from 89.0% to 89.3%. Increasing training steps from 100K to 500K on the 160GB dataset further improved MNLI-m accuracy to 90.2% (Source: 1907.11692.pdf, Table 4, p. 7).

### Intersectional results:
The final RoBERTa model combines the best-performing choices from the unitary analyses (dynamic masking, no NSP loss, large batches, and a large BPE vocabulary) and is trained on a large dataset (160GB) for an extended number of steps (500K). The cumulative effect of these choices results in state-of-the-art performance, e.g., achieving 90.2% on MNLI-m and 96.4% on SST-2 on the development set (Source: 1907.11692.pdf, p. 6-7, Table 4).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The models were trained with mixed-precision floating-point arithmetic on DGX-1 machines, each with 8 x 32GB Nvidia V100 GPUs (Source: 1907.11692.pdf, p. 3). The final `RoBERTa_LARGE` model was pretrained on 1024 V100 GPUs for approximately one day (Source: 1907.11692.pdf, p. 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information. The paper does not include a section on ethical considerations. The training data includes large, unfiltered web text from sources like CommonCrawl and Reddit, which may contain biases, offensive content, or personal information.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The paper notes that even the longest-trained model (500K steps) did not appear to overfit the data and would likely benefit from additional training (Source: 1907.11692.pdf, p. 7).
*   The experiments on data size conflate the effects of increasing both the size and the diversity of the training data. A more careful analysis of these two dimensions is left for future work (Source: 1907.11692.pdf, p. 7, footnote 9).
*   The performance on the WNLI task was found to be challenging, and the authors resorted to a different formulation and loss function for that specific task (Source: 1907.11692.pdf, p. 8).

### Recommendations:
The paper's main contribution is an improved recipe for pretraining BERT-style models. The key recommendations are:
1.  Use dynamic masking instead of static masking (Source: 1907.11692.pdf, p. 4).
2.  Remove the Next Sentence Prediction (NSP) loss and instead train with sequences of full sentences packed together (Source: 1907.11692.pdf, p. 5).
3.  Train with much larger batch sizes (e.g., 8K sequences) (Source: 1907.11692.pdf, p. 5).
4.  Train for a longer duration and on more diverse and larger datasets (Source: 1907.11692.pdf, p. 7).

---