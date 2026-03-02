## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by L. Junbum (Beomi) (Source: `LICENSE.md`). The model is based on Llama 2, which was developed by Meta (Source: `LICENSE.md`).

### Model date:
The copyright for this model version is 2023 (Source: `LICENSE.md`). The underlying Llama 2 model was released on July 18, 2023 (Source: `LICENSE.md`).

### Model version:
The model name is Llama-2-Ko 7b. The version of the `transformers` library used is "4.28.0.dev0" (Source: `config.json`, `generation_config.json`).

### Model type:
The model is a LlamaForCausalLM, which is a type of causal language model based on the Llama architecture (Source: `config.json`).

**Architecture Details:**
*   **Model Type:** llama (Source: `config.json`)
*   **Hidden Size:** 4096 (Source: `config.json`)
*   **Intermediate Size:** 11008 (Source: `config.json`)
*   **Number of Hidden Layers:** 32 (Source: `config.json`)
*   **Number of Attention Heads:** 32 (Source: `config.json`)
*   **Number of Key-Value Heads:** 32 (Source: `config.json`)
*   **Vocabulary Size:** 46336 (Source: `config.json`)
*   **Hidden Activation Function:** silu (Source: `config.json`)
*   **RMS Norm Epsilon:** 1e-05 (Source: `config.json`)
*   **Initializer Range:** 0.02 (Source: `config.json`)

**Size and Context Length:**
*   **Model Size on Disk:** 13,711,720,448 bytes (approx. 13.7 GB) (Source: `model.safetensors.index.json`, `pytorch_model.bin.index.json`).
*   **Maximum Position Embeddings:** 2048 tokens (Source: `config.json`).
*   **Maximum Generation Length:** 4096 tokens (Source: `generation_config.json`).

### Training details:
The model was trained or stored using the `bfloat16` data type (Source: `config.json`). No other details about the training process, algorithms, or hyperparameters are provided.

### Paper or other resource for more information:
Documentation for the base Llama 2 model is available at `ai.meta.com/resources/models-and-libraries/llama-downloads/` (Source: `LICENSE.md`).

### Citation details:
Insufficient information.

### License:
This model is provided under a dual license structure (Source: `LICENSE.md`).

1.  **Llama-2-Ko 7b MIT License**:
    *   Copyright (c) 2023 L. Junbum (Beomi).
    *   Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
    *   The software is provided "AS IS" without any warranty.
    *   The copyright notice and this permission notice must be included in all copies or substantial portions of the Software.

2.  **LLAMA 2 COMMUNITY LICENSE AGREEMENT**:
    *   This license governs the use of the underlying Llama 2 materials from Meta.
    *   It grants a non-exclusive, worldwide, non-transferable, and royalty-free license to use, reproduce, distribute, and create derivative works of the Llama Materials.
    *   **Restrictions**:
        *   When redistributing, a copy of this agreement must be provided to third parties.
        *   An attribution notice must be retained: "Llama 2 is licensed under the LLAMA 2 Community License, Copyright (c) Meta Platforms, Inc. All Rights Reserved."
        *   Use must comply with applicable laws and the Acceptable Use Policy (available at `https://ai.meta.com/llama/use-policy`).
        *   The model or its outputs cannot be used to improve any other large language model (excluding Llama 2 or its derivatives).
    *   **Commercial Terms**: If the products or services using the model have more than 700 million monthly active users, a separate license must be requested from Meta.

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a causal language model (`LlamaForCausalLM`) (Source: `config.json`). The "Ko" in its name suggests it is intended for generating text in the Korean language.

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
*   The model must not be used to improve any other large language model, except for Llama 2 or its derivatives (Source: `LICENSE.md`).
*   Use of the model must adhere to the Llama 2 Acceptable Use Policy, which prohibits usage in violation of any applicable laws or regulations, among other things (Source: `LICENSE.md`).

---

## How to Use
This section outlines how to use the model.

The model can be loaded using the `transformers` library for causal language modeling tasks. It uses a `LlamaTokenizer` (Source: `tokenizer_config.json`). The tokenizer is a Byte-Pair Encoding (BPE) model (Source: `tokenizer.json`).

Key special tokens include:
*   **BOS (Beginning of Sequence) token:** `<s>` (ID: 1) (Source: `special_tokens_map.json`, `config.json`)
*   **EOS (End of Sequence) token:** `</s>` (ID: 2) (Source: `special_tokens_map.json`, `config.json`)
*   **UNK (Unknown) token:** `<unk>` (ID: 0) (Source: `special_tokens_map.json`)
*   **PAD (Padding) token:** ID 0 (Source: `config.json`, `generation_config.json`)

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
The tokenizer configuration specifies the following preprocessing steps for input text (Source: `tokenizer.json`):
*   **Normalization:** A sequence of NFKC normalization, prepending a space (` `), and replacing the standard space character with ` `.
*   **Post-processing:** A template is used to add the beginning-of-sequence token `<s>` to single sequences.
*   **Decoding:** When converting tokens back to text, the decoder replaces ` ` with a space, uses a ByteFallback mechanism, fuses tokens, and strips leading spaces.

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
*   **Disk Space:** The model weights require approximately 13.7 GB of disk space (Source: `model.safetensors.index.json`, `pytorch_model.bin.index.json`).
*   **RAM/VRAM:** Since the model's data type is `bfloat16` (Source: `config.json`), it would require at least 14 GB of RAM or VRAM to load the model into memory.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The use of the model is governed by the LLAMA 2 COMMUNITY LICENSE AGREEMENT, which requires adherence to an Acceptable Use Policy available at `https://ai.meta.com/llama/use-policy` (Source: `LICENSE.md`). This policy outlines prohibited uses of the model to mitigate ethical risks. The license also states that the model must not be used in a way that violates applicable laws and regulations (Source: `LICENSE.md`).

No specific information is provided regarding the use of sensitive data, risk mitigation strategies employed during development, or an analysis of potential harms and biases for this specific model.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The repository does not contain any evaluation data or performance metrics. Therefore, the model's capabilities, accuracy, potential biases, and limitations are unknown.
*   There is no information about the datasets used to train this model, which makes it difficult to assess its suitability for specific domains or its potential to generate biased or inappropriate content.

### Recommendations:
*   Users should thoroughly test the model for their specific use case before deploying it in a production environment, paying close attention to performance, fairness, and safety.
*   Users must adhere to the terms of the MIT License and the LLAMA 2 Community License, including the Acceptable Use Policy (Source: `LICENSE.md`).