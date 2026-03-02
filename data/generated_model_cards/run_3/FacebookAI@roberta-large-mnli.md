## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Facebook AI and the Paul G. Allen School of Computer Science & Engineering at the University of Washington (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).

The authors are: Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).

### Model date:
The associated academic paper was submitted to arXiv on July 26, 2019 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1). The development involved collecting news data crawled between September 2016 and February 2019 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).

### Model version:
The model is referred to as RoBERTa (A Robustly Optimized BERT Pretraining Approach). The provided repository indicates version 0.2 (`version` file).

RoBERTa is presented as an improved training recipe for BERT models. It differs from the original BERT by implementing the following changes:
1.  Training the model for a longer duration, with larger batches, over more data.
2.  Removing the Next Sentence Prediction (NSP) training objective.
3.  Training on longer sequences.
4.  Dynamically changing the masking pattern applied to the training data.
(Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1, Abstract).

### Model type:
RoBERTa is a transformer-based language model pretrained for general-purpose language understanding (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1, Section 1). The specific architecture is `RobertaForSequenceClassification` (`config.json`).

This model card describes the RoBERTa-large architecture, which has the following specifications:
*   **Architecture:** Transformer (`config.json`; Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 2, Section 2.2).
*   **Layers (L):** 24 (`config.json`: `num_hidden_layers`).
*   **Hidden Size (H):** 1024 (`config.json`: `hidden_size`).
*   **Attention Heads (A):** 16 (`config.json`: `num_attention_heads`).
*   **Feed-Forward Network (FFN) Inner Hidden Size:** 4096 (`config.json`: `intermediate_size`).
*   **Total Parameters:** 355 million (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 5).
*   **Supported Context Length:** Up to 512 tokens (`special_tokens_map.json`: `model_max_length`; `config.json`: `max_position_embeddings` is 514 to account for special tokens).
*   **Vocabulary Size:** 50,265, using a byte-level Byte-Pair Encoding (BPE) (`config.json`: `vocab_size`; Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 4.4).

### Training details:
RoBERTa was pretrained using a masked language modeling (MLM) objective. Unlike the original BERT, the Next Sentence Prediction (NSP) objective was removed (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section 4.2). The model was trained with dynamic masking, where a new masking pattern is generated each time a sequence is fed to the model (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section 4.1).

The pretraining was performed for 500,000 steps (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 4, page 7). Key hyperparameters for the RoBERTa-large model include:
*   **Optimizer:** Adam (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 2, Section 2.4).
*   **Adam Parameters:** β1 = 0.9, β2 = 0.98, ε = 1e-6 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.1 and Table 9, page 13).
*   **Peak Learning Rate:** 4e-4 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 9, page 13).
*   **Learning Rate Schedule:** Linear warmup for the first 30,000 steps, followed by a linear decay (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 9, page 13).
*   **Batch Size:** 8,000 sequences (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 9, page 13).
*   **Sequence Length:** 512 tokens (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.1).
*   **Dropout:** 0.1 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 9, page 13).
*   **Weight Decay:** 0.01 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 9, page 13).

The final model was trained on 1024 NVIDIA V100 GPUs for approximately one day (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Section 5).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   **Title:** RoBERTa: A Robustly Optimized BERT Pretraining Approach
*   **Authors:** Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov.
*   **Link:** https://arxiv.org/abs/1907.11692v1 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).

The models and code are available at the Fairseq repository: https://github.com/pytorch/fairseq (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1, footnote 1).

### Citation details:
```bibtex
@article{liu2019roberta,
  title={RoBERTa: A Robustly Optimized BERT Pretraining Approach},
  author={Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
  journal={arXiv preprint arXiv:1907.11692},
  year={2019}
}
```
(Derived from Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).

### License:
Insufficient information.

### Contact:
Contact information for the development teams can be found in the paper:
*   **University of Washington:** {mandar90,lsz}@cs.washington.edu (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).
*   **Facebook AI:** {yinhanliu,myleott,naman,jingfeidu, danqi,omerlevy,mikelewis,lsz,ves}@fb.com (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
RoBERTa is a pretrained language model designed for general-purpose Natural Language Understanding (NLU). It is intended to be finetuned on a variety of downstream tasks (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 2, Section 2.1).

The model has been evaluated on and is suitable for tasks such as:
*   **Sentence-pair classification:** Including Natural Language Inference (NLI) tasks like MNLI, QNLI, RTE, and WNLI, where the model predicts the relationship between two sentences (e.g., entailment, contradiction, neutral) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3; `config.json`: `id2label`).
*   **Single-sentence classification:** Including tasks like sentiment analysis (SST-2) and linguistic acceptability (CoLA) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3).
*   **Question Answering:** Such as SQuAD, where the model extracts an answer span from a given context paragraph (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3).
*   **Reading Comprehension:** Such as RACE, where the model selects the correct answer from four options based on a given passage (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section RACE).

The model takes a sequence of up to 512 tokens as input. For sentence-pair tasks, the input is formatted as `[CLS] sentence1 [SEP] sentence2 [EOS]` (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 2, Section 2.1).

### Primary intended users:
The primary intended users are Natural Language Processing (NLP) researchers and developers who require a powerful pretrained model as a base for their specific applications.

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model is intended to be used within the Fairseq framework (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.1). While specific code snippets are not provided in the repository, the paper describes the finetuning procedures for various tasks:

*   **General Finetuning:** The general procedure follows the original BERT paper, where the pretrained model is augmented with a small task-specific network and all parameters are finetuned on the downstream task data (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3).

*   **For Reading Comprehension (RACE):**
    *   **Input:** For each of the four candidate answers, create a single input sequence by concatenating the question, the passage, and the candidate answer.
    *   **Output:** Each of the four sequences is passed through the model. The resulting `[CLS]` token representations are fed into a fully-connected layer to predict the correct answer.
    (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 9, Section 5.3).

*   **For Extractive Question Answering (SQuAD):**
    *   **Input:** A single sequence containing the question and the context paragraph.
    *   **Output:** The model predicts the start and end tokens of the answer span within the paragraph. For SQuAD 2.0, an additional binary classifier is trained jointly to determine if the question is answerable.
    (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section SQuAD).

*   **For Sentence-Pair Classification (e.g., MNLI):**
    *   **Input:** The two sentences are concatenated into a single sequence, separated by a special token.
    *   **Output:** The `[CLS]` token's representation is used to make a classification decision (e.g., Entailment, Neutral, Contradiction).
    (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 2, Section 2.1).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper systematically investigates several factors that significantly impact the performance of BERT-style models. These include:
*   **Masking Strategy:** The choice between applying a mask to the data once statically before training versus generating a new mask dynamically for each training sequence (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section 4.1).
*   **Training Objective:** The impact of including or removing the Next Sentence Prediction (NSP) loss (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section 4.2).
*   **Batch Size:** The effect of training with larger mini-batches (from 256 up to 8K sequences) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 5, Section 4.3).
*   **Data Size and Diversity:** The performance gains from increasing the amount and variety of pretraining data (from 16GB to 160GB) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 5).
*   **Training Duration:** The effect of pretraining for more steps (from 100K to 500K) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 5).
*   **Text Encoding:** The choice of BPE vocabulary, comparing character-level BPE with byte-level BPE (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 4.4).

### Evaluation factors:
The model's performance was evaluated across the same factors identified as relevant. The paper presents disaggregated results to show the impact of each of these design choices on downstream task performance (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Section 4, pages 4-6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is measured using standard metrics for established NLP benchmarks:
*   **GLUE Benchmark:** Accuracy is reported for MNLI, QNLI, RTE, SST-2, and WNLI. F1 score is used for QQP and MRPC. Matthews Correlation Coefficient is used for CoLA, and Spearman correlation for STS-B. An overall average GLUE score is also reported (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 5, page 8 and Table 8, page 13).
*   **SQuAD Benchmark:** Exact Match (EM) and F1 score are used to measure question-answering performance (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 6, page 9).
*   **RACE Benchmark:** Accuracy is reported for both middle- and high-school level questions (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 7, page 9).
*   **Pretraining Objective:** Perplexity (ppl) is used to evaluate the performance of the masked language modeling objective on held-out training data (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 3, page 6).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robust measurements and account for performance variability:
*   **Development Set Evaluation:** Results on the GLUE and SQuAD development sets are reported as the median over 5 random initializations (seeds) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 2 caption, page 5).
*   **Test Set Evaluation:** For the official GLUE leaderboard submission, an ensemble of 5 to 7 models was used for each task (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Section 5.1).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three standard NLU benchmarks:
1.  **GLUE (General Language Understanding Evaluation):** A collection of nine datasets for single-sentence and sentence-pair classification tasks, including CoLA, SST, MRPC, STS, QQP, MNLI, QNLI, RTE, and WNLI. The evaluation was performed on the private held-out test sets via the official leaderboard (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3).
2.  **SQuAD (Stanford Question Answering Dataset):** Used for extractive question answering. Both version 1.1 and 2.0 were used for evaluation (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.3).
3.  **RACE (ReAding Comprehension from Examinations):** A large-scale multiple-choice reading comprehension dataset collected from English examinations in China for middle and high school students. It contains over 28,000 passages and nearly 100,000 questions (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section RACE).

### Motivation:
These datasets were chosen because they are widely-used benchmarks in the NLP community, allowing for direct comparison with previously published state-of-the-art models like BERT and XLNet (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1, Abstract).

### Preprocessing:
For most tasks, the finetuning procedure follows the original BERT implementation. However, some task-specific modifications were made for the final evaluation:
*   **QNLI:** A pairwise ranking formulation was adopted for test set submissions (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 8, Section Task-specific modifications).
*   **WNLI:** The data was reformatted using the version from SuperGLUE, and a margin ranking loss was used for finetuning (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 8, Section Task-specific modifications).
*   **RACE:** Each question-passage-answer triplet was concatenated into a single sequence for classification (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 9, Section 5.3).
*   **RTE, STS, MRPC:** For test set submissions, models were finetuned starting from the MNLI-finetuned model checkpoint instead of the base pretrained model (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Section 5.1).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on a combination of five English-language text corpora, totaling over 160GB of uncompressed text (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2). The datasets are:
*   **BOOKCORPUS:** A large collection of books (16GB, combined with Wikipedia) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).
*   **English WIKIPEDIA:** (16GB, combined with BookCorpus) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).
*   **CC-NEWS:** A dataset collected from the English portion of the CommonCrawl News dataset, containing 63 million articles from September 2016 to February 2019 (76GB) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).
*   **OPENWEBTEXT:** An open-source recreation of the WebText corpus, with content extracted from URLs shared on Reddit (38GB) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).
*   **STORIES:** A dataset containing a subset of CommonCrawl data, filtered to match a story-like style (31GB) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).

### Motivation:
The choice to use a larger and more diverse collection of datasets was motivated by previous work showing that increasing data size can result in improved end-task performance. This large dataset was also gathered to better control for data size effects when comparing with other models that use large private datasets (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2).

### Preprocessing:
The text was encoded using a byte-level Byte-Pair Encoding (BPE) with a vocabulary of 50,000 subword units. This was done without any heuristic tokenization or preprocessing of the input text (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 4.4). For training, sequences were created by packing full sentences sampled contiguously from one or more documents to a maximum length of 512 tokens (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 5, Section 4.2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides detailed analyses of performance based on individual training factors:
*   **Masking Strategy:** Dynamic masking performed comparably or slightly better than static masking. For example, on SQuAD 2.0 F1, dynamic masking scored 78.7 vs. 78.3 for static (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 1, page 4).
*   **Training Objective:** Removing the Next Sentence Prediction (NSP) loss and training on full sentences (FULL-SENTENCES) improved performance over the original BERT setup (SEGMENT-PAIR+NSP). On RACE, this improved accuracy from 64.2 to 64.8 (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 2, page 5).
*   **Batch Size:** Increasing the batch size from 256 to 2K improved MNLI-m accuracy from 84.7 to 85.2, though a further increase to 8K did not yield additional gains in this experiment (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 3, page 6).
*   **GLUE Tasks:** The final RoBERTa model achieves state-of-the-art results on 4 of the 9 GLUE tasks on the test set, including MNLI (90.8/90.2), QNLI (98.9), RTE (88.2), and STS-B (92.2) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 5, page 8).
*   **RACE Task:** The model achieves state-of-the-art accuracy on both the Middle (86.5) and High (81.3) school levels (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 7, page 9).

### Intersectional results:
The paper analyzes the combined effect of data size and training duration.
*   Training the RoBERTa-large model on 160GB of data (vs. 16GB) for 100K steps improved MNLI-m accuracy from 89.0 to 89.3.
*   Further increasing the training steps on the 160GB dataset to 300K steps increased MNLI-m accuracy to 90.0.
*   Training for 500K steps further increased MNLI-m accuracy to 90.2.
Similar gains were observed across SQuAD and SST-2 tasks, demonstrating the intersectional benefit of both more data and longer training (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 4, page 7).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
*   **Pretraining:** The model was trained on DGX-1 machines, each equipped with 8 x 32GB NVIDIA V100 GPUs. The final RoBERTa-large model was pretrained on 1024 V100 GPUs for approximately one day (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.1 and page 7, Section 5).
*   **Fine-tuning:** The paper specifies batch sizes used for finetuning, which can indicate memory requirements. For the RoBERTa-large model, batch sizes were in the set {16, 32} for GLUE tasks, 48 for SQuAD, and 16 for RACE (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", Table 10, page 13).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided repository data does not contain a discussion of ethical considerations. The model was trained on large corpora scraped from the internet, including BOOKCORPUS, Wikipedia, CommonCrawl News, and Reddit links (OpenWebText) (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 3, Section 3.2). Such datasets may contain sensitive personal information, reflect societal biases, or include offensive content. The potential risks associated with using models trained on this type of data are not addressed in the paper.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The analysis of training data conflates the effects of increasing data size with increasing data diversity. The paper suggests that a more careful analysis of these two dimensions is an area for future work (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, footnote 9).
*   The model's performance may still be suboptimal, as even the longest-trained version (500K steps) did not appear to overfit the training data, suggesting it could benefit from even more training (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Section 5).
*   The finetuning approach for the WNLI task was noted to be suboptimal, as the formulation used excluded over half of the provided training examples (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 8, Section Task-specific modifications).
*   The comparison with other models like XLNet is based on their reported results; the paper notes that it is possible those other methods could also improve with similar tuning and longer training (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 1, footnote 2).

### Recommendations:
The paper's findings serve as a set of recommendations for training high-performing BERT-style models:
*   **Use Dynamic Masking:** Generate masking patterns on-the-fly during training rather than using a static, pre-computed mask (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 4, Section 4.1).
*   **Train without NSP:** Remove the Next Sentence Prediction loss and train with full sentences packed into long sequences (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 5, Section 4.2).
*   **Train with Large Batches:** Training with very large mini-batches (e.g., 8K sequences) can improve perplexity and end-task performance (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 6, Section 4.3).
*   **Train Longer on More Data:** Significant performance gains can be achieved by pretraining for more steps on larger, more diverse datasets (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Table 4).
*   **Task-Specific Finetuning:** For some tasks (RTE, STS, MRPC), performance can be improved by finetuning from a model already finetuned on a large, related task like MNLI, rather than from the base pretrained model (Paper: "RoBERTa: A Robustly Optimized BERT Pretraining Approach", page 7, Section 5.1).