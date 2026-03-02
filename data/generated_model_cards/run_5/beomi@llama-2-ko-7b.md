## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by L. Junbum (Beomi) (Source: `LICENSE.md`). The model is based on the Llama 2 materials originally created by Meta Platforms, Inc. (Source: `LICENSE.md`).

### Model date:
The copyright for this model version is dated 2023 (Source: `LICENSE.md`). The underlying Llama 2 model, on which this is based, was released on July 18, 2023 (Source: `LICENSE.md`).

### Model version:
The model is named Llama-2-Ko 7b (Source: `LICENSE.md`). It was developed using version `4.28.0.dev0` of the transformers library (Source: `config.json`, `generation_config.json`).

### Model type:
The model is a Llama-based Causal Language Model (`LlamaForCausalLM`) designed for text generation (Source: `config.json`).

**Architecture Details:**
*   **Model Architecture:** `llama` (Source: `config.json`).
*   **Hidden Size:** 4096 (Source: `config.json`).
*   **Intermediate Size:** 11008 (Source: `config.json`).
*   **Number of Hidden Layers:** 32 (Source: `config.json`).
*   **Number of Attention Heads:** 32 (Source: `config.json`).
*   **Number of Key-Value Heads:** 32 (Source: `config.json`).
*   **Hidden Activation Function:** `silu` (Source: `config.json`).
*   **RMS Norm Epsilon:** 1e-05 (Source: `config.json`).
*   **Initializer Range:** 0.02 (Source: `config.json`).
*   **Vocabulary Size:** 46336 (Source: `config.json`).
*   **Data Type:** `bfloat16` (Source: `config.json`).

**Size and Context Length:**
*   **Total Size on Disk:** 13,711,720,448 bytes (approximately 13.71 GB) (Source: `pytorch_model.bin.index.json`, `model.safetensors.index.json`).
*   **Maximum Context Length:** 4096 tokens (Source: `config.json`, `generation_config.json`).
*   **Maximum Position Embeddings:** 2048 (Source: `config.json`).

### Training details:
The following parameters from the model's configuration provide some insight into its training:
*   **Pretraining Tensor Parallelism (tp):** 1 (Source: `config.json`).
*   **Tie Word Embeddings:** `false` (Source: `config.json`).
*   **Use Cache:** `true` (Source: `config.json`).

Further details about the training algorithm, optimization techniques, or fairness constraints are not available in the repository.

### Paper or other resource for more information:
The documentation for the original Llama 2 model, upon which this model is based, can be found at `ai.meta.com/resources/models-and-libraries/llama-downloads/` (Source: `LICENSE.md`).

### Citation details:
Insufficient information.

### License:
This model is provided under a dual license structure (Source: `LICENSE.md`).

1.  **Llama-2-Ko 7b MIT License**:
    *   Copyright (c) 2023 L. Junbum (Beomi).
    *   Permission is granted to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software.
    *   The software is provided "AS IS", without any warranty.

2.  **LLAMA 2 COMMUNITY LICENSE AGREEMENT**:
    *   This license governs the use of the underlying Llama 2 materials from Meta.
    *   It grants a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, and create derivative works of the Llama Materials.
    *   **Redistribution Requirement**: A copy of the agreement must be provided to any third party receiving the Llama Materials. An attribution notice must be retained in a "Notice" text file.
    *   **Usage Restrictions**: Use must comply with applicable laws and the Acceptable Use Policy (available at `https://ai.meta.com/llama/use-policy`). The Llama Materials cannot be used to improve any other large language model (excluding Llama 2 or its derivatives).
    *   **Commercial Terms**: If the products or services using the model have more than 700 million monthly active users, a separate license must be requested from Meta.

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a causal language model (`LlamaForCausalLM`), indicating its primary use is for autoregressive text generation (Source: `config.json`). The "Ko" in its name, "Llama-2-Ko 7b", suggests it is intended for use with the Korean language.

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
*   The model and its outputs must not be used to improve any other large language model, with the exception of Llama 2 or its derivative works (Source: `LICENSE.md`).
*   All uses must adhere to the Acceptable Use Policy for Llama Materials, which can be found at `https://ai.meta.com/llama/use-policy` (Source: `LICENSE.md`).

---

## How to Use
This section outlines how to use the model.

Insufficient information.

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
The `tokenizer.json` file details the text preprocessing and tokenization pipeline:
*   **Normalization**: A sequence of normalization steps is applied:
    1.  `NFKC`: Unicode normalization.
    2.  `Prepend`: A space is prepended to the input string.
    3.  `Replace`: A pattern to replace spaces with a specific character (` `).
*   **Tokenization Model**: The model uses Byte-Pair Encoding (`BPE`) with a vocabulary size of 46336 (Source: `tokenizer.json`).
*   **Post-processing**: A `TemplateProcessing` step adds special tokens like `<s>` (start of sequence) to single and paired sequences (Source: `tokenizer.json`).
*   **Decoding**: The decoding process involves a sequence of steps:
    1.  `Replace`: Replaces the ` ` character with a standard space.
    2.  `ByteFallback`: Handles unknown tokens by falling back to byte-level representation.
    3.  `Fuse`: Merges tokens.
    4.  `Strip`: Strips leading spaces.

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
*   **Disk Space:** The model requires approximately 13.71 GB of disk space to store its weights (Source: `pytorch_model.bin.index.json`, `model.safetensors.index.json`).
*   **Memory (RAM/VRAM):** The model weights are stored in `bfloat16` format, which will influence the memory required for loading (Source: `config.json`). Specific RAM/VRAM requirements are not provided.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The use of this model is subject to the Llama 2 Acceptable Use Policy, which is incorporated by reference into the license agreement. This policy is available at `https://ai.meta.com/llama/use-policy` (Source: `LICENSE.md`). The license also includes a disclaimer of warranty and limitation of liability, stating that users are solely responsible for determining the appropriateness of using the model and assume any associated risks (Source: `LICENSE.md`). No other specific ethical considerations, such as the use of sensitive data or risk mitigation strategies, are detailed in the provided files.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model is provided on an "AS IS" basis, without warranties of any kind, including non-infringement, merchantability, or fitness for a particular purpose (Source: `LICENSE.md`).
*   Users are solely responsible for determining the appropriateness of using or redistributing the model and assume any risks associated with its use and outputs (Source: `LICENSE.md`).

### Recommendations:
Insufficient information.

---