## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Meta (citation: `LICENSE`, `USE_POLICY.md`). Depending on the user's location, "Meta" refers to Meta Platforms Ireland Limited or Meta Platforms, Inc. (citation: `LICENSE`).

### Model date:
The Llama 2 model was released on July 18, 2023 (citation: `LICENSE`).

### Model version:
The model is identified as Llama 2 (citation: `LICENSE`). The associated transformers library version is "4.31.0.dev0" (citation: `config.json`, `generation_config.json`).

### Model type:
The model is a Llama-type large language model for causal language modeling (citation: `config.json`). It is based on a decoder-only Transformer architecture (citation: `config.json`).

Key architectural details include:
*   **Architecture:** LlamaForCausalLM (citation: `config.json`).
*   **Hidden Size:** 4096 (citation: `config.json`).
*   **Intermediate Size:** 11008 (citation: `config.json`).
*   **Number of Hidden Layers:** 32 (citation: `config.json`).
*   **Number of Attention Heads:** 32 (citation: `config.json`).
*   **Number of Key-Value Heads:** 32 (citation: `config.json`).
*   **Activation Function:** SiLU ("silu") (citation: `config.json`).
*   **Normalization:** RMS Normalization with an epsilon of 1e-05 (citation: `config.json`).
*   **Vocabulary Size:** 32000 (citation: `config.json`).
*   **Context Length (Max Position Embeddings):** 4096 tokens (citation: `config.json`).
*   **Data Type:** float16 (citation: `config.json`).
*   **Model Size:** The total size of the model weights is 13,476,835,328 bytes (approx. 13.5 GB) in SafeTensors format (citation: `model.safetensors.index.json`) and 26,953,670,656 bytes (approx. 27.0 GB) in PyTorch format (citation: `pytorch_model.index.json`).

### Training details:
The provided information on the training process is limited to the following hyperparameters and configuration settings:
*   **Initializer Range:** 0.02 (citation: `config.json`).
*   **Pretraining Tensor Parallelism (TP):** 1 (citation: `config.json`).
*   **Tied Word Embeddings:** `false` (citation: `config.json`).

The repository includes materials such as "trained model weights, inference-enabling code, training-enabling code, [and] fine-tuning enabling code" (citation: `LICENSE`). No further details on training algorithms, fairness constraints, or optimization techniques are available.

### Paper or other resource for more information:
Specifications, manuals, and documentation accompanying Llama 2 are available at `ai.meta.com/resources/models-and-libraries/llama-downloads/` (citation: `LICENSE`).

For reporting issues, the following resources are provided:
*   **Model Issues:** `github.com/facebookresearch/llama` (citation: `USE_POLICY.md`).
*   **Risky Content:** `developers.facebook.com/llama_output_feedback` (citation: `USE_POLICY.md`).
*   **Bugs and Security Concerns:** `facebook.com/whitehat/info` (citation: `USE_POLICY.md`).

### Citation details:
Insufficient information.

### License:
The model is licensed under the LLAMA 2 COMMUNITY LICENSE AGREEMENT (citation: `LICENSE`). Key terms of the license include:
*   A non-exclusive, worldwide, non-transferable, and royalty-free limited license is granted to use, reproduce, distribute, copy, create derivative works of, and modify the Llama Materials (citation: `LICENSE`).
*   If you distribute the Llama Materials, you must provide a copy of the license agreement to the recipient and include the attribution notice: "Llama 2 is licensed under the LLAMA 2 Community License, Copyright (c) Meta Platforms, Inc. All Rights Reserved." (citation: `LICENSE`).
*   Use of the model must comply with applicable laws and the Acceptable Use Policy (citation: `LICENSE`).
*   The model or its outputs cannot be used to improve any other large language model, excluding Llama 2 or its derivatives (citation: `LICENSE`).
*   **Additional Commercial Terms:** If the monthly active users of a licensee's products or services exceed 700 million, a separate license must be requested from Meta (citation: `LICENSE`).

### Contact:
For reporting violations of the Acceptable Use Policy or unlicensed uses of Llama, contact `LlamaUseReport@meta.com` (citation: `USE_POLICY.md`). Other contact channels for specific issues are listed in the "Paper or other resource for more information" section.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a foundational large language model designed for causal language modeling, which involves generating text that continues from a given prompt (citation: `LICENSE`, `config.json`). It is intended for general-purpose applications, as evidenced by the broad scope of the license and acceptable use policy.

### Primary intended users:
The intended users include individuals, researchers, developers, and commercial entities, as indicated by the terms of the license agreement (citation: `LICENSE`). The "Additional Commercial Terms" section specifically addresses large-scale commercial users with over 700 million monthly active users (citation: `LICENSE`).

### Out-of-scope uses:
The model is not designed for any purpose that violates the Llama 2 Acceptable Use Policy. All users must agree not to use the model for these prohibited applications. A summary of out-of-scope uses includes:

1.  **Illegal Activities or Rights Violations:** Engaging in or promoting illegal acts, child exploitation, human trafficking, harassment, discrimination, unauthorized practice of a profession (e.g., legal or medical advice), violating privacy, infringing on third-party rights, or creating malware (citation: `USE_POLICY.md`).
2.  **Activities with High Risk of Harm:** Use related to military and warfare, illegal weapons development, illegal drugs, operation of critical infrastructure, or content that promotes self-harm (citation: `USE_POLICY.md`).
3.  **Deceptive or Misleading Content:** Generating content for fraud, disinformation, defamation, spam, impersonation, or representing AI-generated outputs as human-generated (citation: `USE_POLICY.md`).
4.  **Failure to Disclose Dangers:** Failing to inform end users about any known dangers of an AI system built using the model (citation: `USE_POLICY.md`).

---

## How to Use
This section outlines how to use the model.

The model is a `LlamaForCausalLM` and can be used with the `LlamaTokenizer` class, which is standard in the Hugging Face Transformers library (citation: `config.json`, `tokenizer_config.json`).

The model expects tokenized text as input and generates a sequence of tokens as output.
*   **Input:** A sequence of text.
*   **Output:** A continuation of the input text.

**Tokenizer Details:**
*   A beginning-of-sequence token (`<s>`) is automatically added to the input (citation: `tokenizer_config.json`, `special_tokens_map.json`).
*   Special tokens include:
    *   `bos_token`: `<s>` (citation: `special_tokens_map.json`)
    *   `eos_token`: `</s>` (citation: `special_tokens_map.json`)
    *   `unk_token`: `<unk>` (citation: `special_tokens_map.json`)

**Generation Settings:**
The default generation configuration is set to use sampling with the following parameters:
*   `do_sample`: `true` (citation: `generation_config.json`)
*   `temperature`: 0.9 (citation: `generation_config.json`)
*   `top_p`: 0.6 (citation: `generation_config.json`)

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
Insufficient information.

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
The model weights require approximately 13.5 GB of storage for the SafeTensors version and 27.0 GB for the PyTorch version (citation: `model.safetensors.index.json`, `pytorch_model.index.json`). The model uses the `float16` data type, suggesting that a GPU with sufficient VRAM is recommended for efficient loading and inference (citation: `config.json`). Specific RAM or VRAM requirements are not provided.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development and release of Llama 2 were accompanied by a detailed Acceptable Use Policy that outlines ethical guidelines and restrictions (citation: `USE_POLICY.md`).

*   **Sensitive Data:** The policy prohibits users from collecting, processing, or generating "health, demographic, or other sensitive personal or private information about individuals without rights and consents required by applicable laws" (citation: `USE_POLICY.md`).
*   **Risks and Mitigation:** Potential risks are identified and addressed through the list of "Prohibited Uses" in the `USE_POLICY.md`. These risks include the generation of harmful, illegal, or deceptive content. The primary mitigation strategy is the enforcement of this policy, which all licensees must agree to (citation: `LICENSE`). Meta has also established reporting channels for users to flag policy violations, risky content, and security concerns, creating a mechanism for post-deployment risk management (citation: `USE_POLICY.md`).
*   **Use Case Prohibitions:** The policy explicitly forbids using the model for high-stakes applications where its failure could lead to death or bodily harm, such as military use, illegal weapons development, and the operation of critical infrastructure (citation: `USE_POLICY.md`). It also prohibits uses that could lead to social harm, such as generating disinformation, harassment, or discriminatory content (citation: `USE_POLICY.md`).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The provided repository contains no information on the model's performance on standard benchmarks or its evaluation against different demographic or linguistic groups. This lack of quantitative data represents a significant gap in understanding the model's capabilities and limitations.
*   The license includes a "Disclaimer of Warranty," stating that the model is provided "AS IS" without warranties of any kind. Users are "solely responsible for determining the appropriateness of using or redistributing the Llama Materials and assume any risks associated with" its use (citation: `LICENSE`).

### Recommendations:
*   Users must read and adhere to the Llama 2 Acceptable Use Policy at all times (citation: `LICENSE`, `USE_POLICY.md`).
*   Users should report any violations of the policy, software bugs, or the generation of risky content through the channels provided by Meta (citation: `USE_POLICY.md`).
*   Developers building applications with Llama 2 are prohibited from failing "to appropriately disclose to end users any known dangers of your AI system" (citation: `USE_POLICY.md`).
*   When redistributing the model or its derivatives, users must provide a copy of the LLAMA 2 COMMUNITY LICENSE AGREEMENT to the recipient (citation: `LICENSE`).