## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The tokenizer used for this model is version 0.2 and was trained by `huggingface/tokenizers` (Source: merges.txt). There is no information available regarding the version of the model itself.

### Model type:
The model is based on the `roberta-base` architecture (Source: tokenizer_config.json.txt).

**Architecture Details:**
*   **Tokenizer Type:** The model uses a Byte-Pair Encoding (BPE) tokenizer (Source: tokenizer_summary.json.txt).
*   **Vocabulary Size:** The tokenizer has a vocabulary of 50,265 tokens (Source: tokenizer_summary.json.txt, vocab.json.txt).
*   **Pre-tokenizer:** The text is pre-processed using a ByteLevel pre-tokenizer, which splits text into tokens at the byte level (Source: tokenizer_summary.json.txt).
*   **Post-processor:** The tokenizer output is formatted using RobertaProcessing, which adds special tokens like `<s>` and `</s>` (Source: tokenizer_summary.json.txt).
*   **Special Tokens:** The model uses the following special tokens:
    *   `<s>` as the beginning-of-sequence (bos) and classification (cls) token (Source: tokenizer_config.json.txt, special_tokens_map.json.txt).
    *   `</s>` as the end-of-sequence (eos) and separator (sep) token (Source: tokenizer_config.json.txt, special_tokens_map.json.txt).
    *   `<pad>` as the padding token (Source: tokenizer_config.json.txt, special_tokens_map.json.txt).
    *   `<unk>` as the unknown token (Source: tokenizer_config.json.txt, special_tokens_map.json.txt).
    *   `<mask>` as the mask token (Source: tokenizer_config.json.txt, special_tokens_map.json.txt).
*   **Model Max Length:** The model supports a maximum context length of 512 tokens (Source: tokenizer_config.json.txt).

### Training details:
The model was trained for 3.0 epochs out of a planned 10 epochs, completing 16,281 steps out of a planned 54,270 (Source: trainer_state.json.txt).

*   **Learning Rate:** The training process used a variable learning rate, starting at approximately `1.98e-05` and decreasing over the course of training. At step 16,000, the learning rate was `1.41e-05` (Source: trainer_state.json.txt).
*   **Loss:** The training loss decreased from an initial value of `0.1826` at step 500 to `0.0714` at step 16,000 (Source: trainer_state.json.txt).
*   **Best Checkpoint:** The best performing model checkpoint was saved at step 16,281, which achieved the best evaluation metric (F1 score of 0.586) (Source: trainer_state.json.txt).

### Paper or other resource for more information:
Insufficient information

### Citation details:
Insufficient information

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Insufficient information

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model. 

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information

### Evaluation factors:
Insufficient information

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was evaluated using the following metrics (Source: trainer_state.json.txt):
*   **Accuracy:** Measures the proportion of correct predictions.
*   **F1 Score:** The harmonic mean of precision and recall. This was the primary metric for determining the best model checkpoint.
*   **Loss:** The evaluation loss on the validation dataset.
*   **ROC AUC:** The Area Under the Receiver Operating Characteristic Curve, which measures the model's ability to distinguish between classes.

The final evaluation at epoch 3.0 yielded the following performance measures:
*   **eval_accuracy:** 0.47475
*   **eval_f1:** 0.58626
*   **eval_loss:** 0.08390
*   **eval_roc_auc:** 0.75068

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Insufficient information

### Motivation:
Insufficient information

### Preprocessing:
The data was pre-processed using a ByteLevel pre-tokenizer. This method splits text based on byte-level representations and handles all UTF-8 characters. The tokenizer configuration specifies that prefix spaces are not added, and offsets are trimmed (Source: tokenizer_summary.json.txt). After tokenization, the input is formatted using RobertaProcessing, which adds a start-of-sequence token (`<s>`) at the beginning and an end-of-sequence token (`</s>`) at the end (Source: tokenizer_summary.json.txt).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Insufficient information

### Motivation:
Insufficient information

### Preprocessing:
The data was pre-processed using a ByteLevel pre-tokenizer. This method splits text based on byte-level representations and handles all UTF-8 characters. The tokenizer configuration specifies that prefix spaces are not added, and offsets are trimmed (Source: tokenizer_summary.json.txt). After tokenization, the input is formatted using RobertaProcessing, which adds a start-of-sequence token (`<s>`) at the beginning and an end-of-sequence token (`</s>`) at the end (Source: tokenizer_summary.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The following are the overall performance results on the evaluation dataset at the end of each epoch during training (Source: trainer_state.json.txt).

**End of Epoch 1.0 (Step 5427):**
*   **eval_loss:** 0.0882
*   **eval_accuracy:** 0.4021
*   **eval_f1:** 0.5346
*   **eval_roc_auc:** 0.7099

**End of Epoch 2.0 (Step 10854):**
*   **eval_loss:** 0.0843
*   **eval_accuracy:** 0.4401
*   **eval_f1:** 0.5612
*   **eval_roc_auc:** 0.7305

**End of Epoch 3.0 (Step 16281):**
*   **eval_loss:** 0.0839
*   **eval_accuracy:** 0.4748
*   **eval_f1:** 0.5863
*   **eval_roc_auc:** 0.7507

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The total number of floating-point operations (FLOPs) for the training performed was 8,568,237,917,583,360.0 (Source: trainer_state.json.txt). Specific hardware details such as GPU type or memory requirements are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---