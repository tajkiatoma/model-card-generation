## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model is based on `microsoft/deberta-v3-large` (Source: `ranker_config.json.txt`). No specific version for this fine-tuned model is provided.

### Model type:
This is a ranking model of type `pairranker` (Source: `ranker_config.json.txt`). It is built upon the DeBERTa architecture, specifically using the `microsoft/deberta-v3-large` base model (Source: `ranker_config.json.txt`).

**Architecture Details:**
*   **Base Model:** DeBERTa V3 Large (Source: `ranker_config.json.txt`).
*   **Tokenizer:** The model uses a `DebertaV2Tokenizer` (Source: `tokenizer_config.json.txt`). The tokenizer model is of type `Unigram` with a vocabulary size of 128,000 tokens (Source: `tokenizer_summary.json.txt`).
*   **Special Tokens:** The tokenizer includes standard special tokens such as `[CLS]`, `[SEP]`, `[PAD]`, `[MASK]`, and `[UNK]` (Source: `special_tokens_map.json.txt`, `tokenizer_summary.json.txt`). Additionally, it has added tokens for ranking tasks: `<|source|>`, `<|candidate1|>`, `<|candidate2|>`, and `<|candidate|>` (Source: `added_tokens.json.txt`, `tokenizer_config.json.txt`).

**Size and Context Length:**
*   **Source Max Length:** The maximum length for the source input is 1224 tokens (Source: `ranker_config.json.txt`).
*   **Candidate Max Length:** The maximum length for the candidate input is 412 tokens (Source: `ranker_config.json.txt`).
*   **Model Max Length:** The tokenizer is configured with a theoretical maximum length of 1000000000000000019884624838656 (Source: `tokenizer_config.json.txt`).

### Training details:
The model was trained as a `pairranker` using the following configurations:
*   **Loss Function:** The loss type used was `instructgpt` (Source: `ranker_config.json.txt`).
*   **Reduction Type:** The reduction type is `linear` (Source: `ranker_config.json.txt`).
*   **Dropout:** A dropout rate of 0.05 was applied during training (Source: `ranker_config.json.txt`).
*   **Precision:** The model was trained with 16-bit floating-point precision (`fp16: true`) (Source: `ranker_config.json.txt`).
*   **Data Sampling:** The training data was structured with 5 positive (`num_pos: 5`) and 5 negative (`num_neg: 5`) candidates for each source. The sub-sampling mode was `all_pair` with a ratio of 0.4 (Source: `ranker_config.json.txt`).
*   **Inference Mode:** The model is configured for `bubble` inference mode (Source: `ranker_config.json.txt`).

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
Based on its configuration as a `pairranker` and the presence of special tokens like `<|source|>` and `<|candidate|>` (Source: `ranker_config.json.txt`, `added_tokens.json.txt`), the model is intended for ranking tasks. Its primary use is to rank a set of "candidate" texts based on their relevance or quality with respect to a "source" text.

The input-output structure involves providing a source text and one or more candidate texts, likely formatted with the special tokens. The model then outputs scores that can be used to rank the candidates.

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model. 

While no code snippets are provided, the model's usage can be inferred from its configuration files. The model expects input formatted with a source text and candidate texts, separated by special tokens.

**Input Structure:**
The input should be structured using the special tokens defined in the tokenizer. For a ranking task, the input would likely be a sequence containing the source text, prefixed by `<|source|>`, and a candidate text, prefixed by `<|candidate|>` or similar tokens (Source: `added_tokens.json.txt`).

**Settings:**
*   The source text will be truncated to a maximum of 1224 tokens (Source: `ranker_config.json.txt`).
*   The candidate text will be truncated to a maximum of 412 tokens (Source: `ranker_config.json.txt`).
*   The tokenizer's post-processor will add `[CLS]` at the beginning and `[SEP]` at the end of sequences (Source: `tokenizer_summary.json.txt`).

**Example Input Format (Inferred):**
`[CLS] <|source|> [source text] [SEP] <|candidate|> [candidate text] [SEP]`

**Example Output:**
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
Insufficient information

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
Insufficient information

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The specific datasets used for training are not mentioned. However, the configuration implies a dataset structure where each instance consists of a source text, 5 positive candidates, and 5 negative candidates (Source: `ranker_config.json.txt`, `num_pos: 5`, `num_neg: 5`). During training, pairs were created from these candidates using an `all_pair` sub-sampling mode with a ratio of 0.4 (Source: `ranker_config.json.txt`).

### Motivation:
Insufficient information

### Preprocessing:
The text data was preprocessed using the model's tokenizer, which includes the following steps (Source: `tokenizer_summary.json.txt`):
1.  **Normalization:** A sequence of normalizers is applied:
    *   `Strip`: Strips leading and trailing whitespace from the text.
    *   `Precompiled`: Uses a precompiled character map for normalization.
    *   `Replace`: Replaces occurrences of two or more spaces with a single space.
2.  **Pre-tokenization:** A `Metaspace` pre-tokenizer is used, which replaces whitespace with a special metaspace character (` `) and adds a prefix space.
3.  **Post-processing:** A `TemplateProcessing` step adds special tokens to the input.
    *   For single sequences: `[CLS] A [SEP]`
    *   For paired sequences: `[CLS] A [SEP] B [SEP]`
4.  **Decoding:** A `Metaspace` decoder is used to reconstruct the text from tokens, replacing the metaspace character with a space.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Insufficient information

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
The model was trained using 16-bit floating-point precision (`fp16: true`) (Source: `ranker_config.json.txt`), which suggests that training required a GPU with support for half-precision arithmetic (e.g., GPUs with Tensor Cores). Specific hardware details are not provided.

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