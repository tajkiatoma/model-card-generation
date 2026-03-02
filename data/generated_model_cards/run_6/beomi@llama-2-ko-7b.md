## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by L. Junbum (Beomi) (LICENSE.txt). The model is based on Llama 2, which is a proprietary model of Meta Platforms, Inc. (LICENSE.txt).

### Model date:
The copyright for the model is dated 2023 (LICENSE.txt). The underlying Llama 2 model, on which this model is based, has a version release date of July 18, 2023 (LICENSE.txt).

### Model version:
The model name is Llama-2-Ko 7b (LICENSE.txt). The model was developed using transformers version 4.28.0.dev0 (config.json.txt, generation_config.json.txt).

### Model type:
The model is a LlamaForCausalLM, which is a type of large language model for causal language modeling (text generation) (config.json.txt).

**Architecture Details:**
*   **Model Type:** llama (config.json.txt)
*   **Hidden Size:** 4096 (config.json.txt)
*   **Intermediate Size:** 11008 (config.json.txt)
*   **Number of Hidden Layers:** 32 (config.json.txt)
*   **Number of Attention Heads:** 32 (config.json.txt)
*   **Number of Key-Value Heads:** 32 (config.json.txt)
*   **Hidden Activation Function:** silu (config.json.txt)
*   **RMS Norm Epsilon:** 1e-05 (config.json.txt)
*   **Initializer Range:** 0.02 (config.json.txt)
*   **Vocabulary Size:** 46336 (config.json.txt, tokenizer_summary.json.txt)
*   **Data Type:** bfloat16 (config.json.txt)

**Size and Context Length:**
*   **Total Size:** 13,711,720,448 bytes (~13.71 GB) (model.safetensors.index.json.txt, pytorch_model.bin.index.json.txt)
*   **Maximum Position Embeddings:** 2048 (config.json.txt)
*   **Maximum Length:** 4096 (config.json.txt, generation_config.json.txt)

### Training details:
The provided files contain limited information about the training process. The model uses a `bfloat16` torch data type (config.json.txt). Other details such as the training algorithm, optimization techniques, or fairness constraints are not specified.

### Paper or other resource for more information:
The license agreement for the base Llama 2 model mentions that documentation is available from Meta at `ai.meta.com/resources/models-and-libraries/llama-downloads/` (LICENSE.txt). The license also refers to an Acceptable Use Policy available at `https://ai.meta.com/llama/use-policy` (LICENSE.txt).

### Citation details:
Insufficient information.

### License:
The model is provided under a dual license structure (LICENSE.txt).

1.  **Llama-2-Ko 7b MIT License**:
    *   Copyright (c) 2023 L. Junbum (Beomi).
    *   Permission is granted free of charge to any person to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
    *   The copyright notice and this permission notice must be included in all copies or substantial portions of the Software.
    *   The software is provided "AS IS", without any warranty.

2.  **LLAMA 2 COMMUNITY LICENSE AGREEMENT**:
    *   Users are granted a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, copy, create derivative works of, and modify the Llama Materials (LICENSE.txt).
    *   **Redistribution**: If distributing the Llama Materials, a copy of this agreement must be provided to the third party, and an attribution notice must be retained (LICENSE.txt).
    *   **Usage Restrictions**:
        *   Use must comply with applicable laws and the Acceptable Use Policy (LICENSE.txt).
        *   The model or its outputs cannot be used to improve any other large language model, excluding Llama 2 or its derivatives (LICENSE.txt).
    *   **Commercial Terms**: If the monthly active users of products or services using the model exceed 700 million, a separate license must be requested from Meta (LICENSE.txt).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model architecture, `LlamaForCausalLM`, indicates it is designed for causal language modeling, which involves predicting the next token in a sequence (config.json.txt). This makes it suitable for text generation tasks. The model name, "Llama-2-Ko," suggests it is specialized for the Korean language (LICENSE.txt). The model takes text as input and generates text as output.

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
Based on the license, the model has the following out-of-scope uses:
*   The model or its outputs cannot be used to improve any other large language model (excluding Llama 2 or its derivatives) (LICENSE.txt).
*   Any use that violates applicable laws, regulations, or the Llama 2 Acceptable Use Policy is prohibited (LICENSE.txt).

---

## How to Use
This section outlines how to use the model.

The model can be used with the `LlamaTokenizer` class (tokenizer_config.json.txt). The tokenizer uses a Byte-Pair Encoding (BPE) model (tokenizer_summary.json.txt).

**Special Tokens:**
*   **Beginning of Sequence (BOS):** `<s>` (ID: 1) (config.json.txt, special_tokens_map.json.txt)
*   **End of Sequence (EOS):** `</s>` (ID: 2) (config.json.txt, special_tokens_map.json.txt)
*   **Unknown Token:** `<unk>` (ID: 0) (special_tokens_map.json.txt)
*   **Padding Token:** The pad token ID is 0 (config.json.txt).

No code snippets or example outputs are provided in the repository.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information.

### Evaluation factors:
Insufficient information.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
Insufficient information.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Insufficient information.

### Motivation:
Insufficient information.

### Preprocessing:
Insufficient information.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Insufficient information.

### Motivation:
Insufficient information.

### Preprocessing:
While information on the training dataset itself is unavailable, the `tokenizer_summary.json.txt` file describes the text preprocessing steps applied by the tokenizer:
*   **Normalization:** A sequence of normalizers is applied, including NFKC Unicode normalization, prepending a space to the input string, and replacing the space character with a special ` ` character (U+2581) (tokenizer_summary.json.txt).
*   **Tokenization:** The model uses a Byte-Pair Encoding (BPE) tokenizer with a vocabulary of 46,336 tokens (tokenizer_summary.json.txt).
*   **Post-processing:** A template processor adds the beginning-of-sequence token `<s>` to the start of a single input sequence (tokenizer_summary.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Insufficient information.

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   The total size of the model weights is approximately 13.71 GB (model.safetensors.index.json.txt, pytorch_model.bin.index.json.txt).
*   The model is configured to use the `bfloat16` data type, so loading the model would require at least 14 GB of RAM or VRAM, plus overhead for the framework and execution (config.json.txt).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided repository files do not contain information about the use of sensitive data, risk assessments, or specific mitigation strategies. However, the LLAMA 2 COMMUNITY LICENSE AGREEMENT mandates that any use of the model must adhere to the Acceptable Use Policy, which is available at `https://ai.meta.com/llama/use-policy` (LICENSE.txt). Users are responsible for complying with this policy.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The repository does not include any evaluation data or performance metrics. Therefore, the model's accuracy, fairness, and potential biases are unknown.
*   There is no information about the data used to train the model, which makes it difficult to assess its suitability for specific domains or its potential to generate harmful or biased content.
*   The model's performance on languages other than Korean is not documented.

### Recommendations:
*   Users should conduct a thorough evaluation of the model for their specific use case before deploying it in a production environment, paying close attention to performance, bias, and safety.
*   Users must review and adhere to all terms and restrictions outlined in both the MIT License and the LLAMA 2 COMMUNITY LICENSE AGREEMENT (LICENSE.txt).
*   It is strongly recommended that users review the Llama 2 Acceptable Use Policy at `https://ai.meta.com/llama/use-policy` to understand the ethical guidelines and restrictions on the model's application (LICENSE.txt).
*   Do not use the model or its outputs to improve any other large language model (except for Llama 2 and its derivatives) as this is a violation of the license (LICENSE.txt).