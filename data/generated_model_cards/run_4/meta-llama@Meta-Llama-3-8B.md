## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Meta (META LLAMA 3 COMMUNITY LICENSE AGREEMENT). Depending on the user's location, "Meta" refers to Meta Platforms Ireland Limited (for users in the EEA or Switzerland) or Meta Platforms, Inc. (for users outside the EEA or Switzerland) (META LLAMA 3 COMMUNITY LICENSE AGREEMENT).

### Model date:
The release date for this version of Meta Llama 3 is April 18, 2024 (META LLAMA 3 COMMUNITY LICENSE AGREEMENT).

### Model version:
The model is identified as Meta Llama 3 (META LLAMA 3 COMMUNITY LICENSE AGREEMENT). It was developed using transformers version "4.40.0.dev0" (config.json, generation_config.json).

### Model type:
Meta Llama 3 is a foundational large language model (META LLAMA 3 COMMUNITY LICENSE AGREEMENT).

**Architecture:**
The model is a LlamaForCausalLM, which is a decoder-only transformer-based architecture designed for causal language modeling (config.json).

**Key Architectural Details:**
*   **Model Type:** `llama` (config.json)
*   **Hidden Size:** 4096 (config.json, params.json)
*   **Number of Hidden Layers:** 32 (config.json, params.json)
*   **Number of Attention Heads:** 32 (config.json, params.json)
*   **Number of Key-Value Heads:** 8 (config.json, params.json)
*   **Intermediate Size (FFN):** 14336 (config.json)
*   **Activation Function:** SiLU (`silu`) (config.json)
*   **Vocabulary Size:** 128256 (config.json, params.json)
*   **Maximum Position Embeddings (Context Length):** 8192 tokens (config.json)
*   **Normalization:** RMS Normalization with an epsilon of 1e-05 (config.json, params.json)
*   **Rope Theta:** 500000.0 (config.json, params.json)
*   **Data Type:** `bfloat16` (config.json)

**Model Size:**
*   **Total Size on Disk:** 16,060,522,496 bytes (approx. 16.06 GB) (index.json)

### Training details:
The following hyperparameters were used during the model's development:
*   **Initializer Range:** 0.02 (config.json)
*   **RMS Norm Epsilon:** 1e-05 (config.json, params.json)
*   **Rope Theta:** 500000.0 (config.json, params.json)
*   **Pretraining Tensor Parallelism (tp):** 1 (config.json)
*   **Attention Dropout:** 0.0 (config.json)
*   **Tie Word Embeddings:** `false` (config.json)

Further details on the training algorithm, methodologies, or fairness constraints are not available in the provided information.

### Paper or other resource for more information:
The following resources provide more information about the model and its usage:
*   **Getting Started Documentation:** https://llama.meta.com/get-started/ (META LLAMA 3 COMMUNITY LICENSE AGREEMENT)
*   **Model Downloads:** https://llama.meta.com/llama-downloads (META LLAMA 3 COMMUNITY LICENSE AGREEMENT)
*   **GitHub Repository (for reporting issues):** https://github.com/meta-llama/llama3 (USE_POLICY.md)
*   **Acceptable Use Policy:** https://llama.meta.com/llama3/use-policy (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, USE_POLICY.md)

### Citation details:
Insufficient information

### License:
The model is licensed under the "META LLAMA 3 COMMUNITY LICENSE AGREEMENT" (META LLAMA 3 COMMUNITY LICENSE AGREEMENT).

**Key terms of the license include:**
*   **Grant of Rights:** Users are granted a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, copy, create derivative works of, and modify the Llama Materials (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.a).
*   **Redistribution Requirements:**
    *   If you distribute the Llama Materials or a derivative, you must provide a copy of the license agreement (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.i.A).
    *   You must prominently display "Built with Meta Llama 3" on a related website, UI, or documentation (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.i.B).
    *   If you create an AI model using Llama Materials, you must include "Llama 3" at the beginning of the model's name (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.i).
    *   You must retain the attribution notice: "Meta Llama 3 is licensed under the Meta Llama 3 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved." in a "Notice" text file (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.iii).
*   **Usage Restrictions:**
    *   Use must comply with applicable laws and the Acceptable Use Policy (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.iv).
    *   You may not use the Llama Materials or their outputs to improve any other large language model (excluding Meta Llama 3 or its derivatives) (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.v).
*   **Commercial Terms:** If the monthly active users of a licensee's products or services exceed 700 million, a separate license must be requested from Meta (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 2).
*   **Disclaimer:** The materials are provided "AS IS" without warranties of any kind (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 3).

### Contact:
For issues, violations, or security concerns, use the following channels:
*   **Reporting issues with the model:** https://github.com/meta-llama/llama3 (USE_POLICY.md)
*   **Reporting risky content generated by the model:** developers.facebook.com/llama_output_feedback (USE_POLICY.md)
*   **Reporting bugs and security concerns:** facebook.com/whitehat/info (USE_POLICY.md)
*   **Reporting violations of the Acceptable Use Policy or unlicensed uses:** LlamaUseReport@meta.com (USE_POLICY.md)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a foundational large language model (META LLAMA 3 COMMUNITY LICENSE AGREEMENT) with a causal language modeling architecture (`LlamaForCausalLM`), making it suitable for text generation tasks (config.json).

The model's generation behavior can be configured with the following parameters:
*   `do_sample`: `true` (enables sampling-based generation)
*   `temperature`: 0.6
*   `max_length`: 4096
*   `top_p`: 0.9
(generation_config.json)

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Users are prohibited from using Meta Llama 3 for activities outlined in the Acceptable Use Policy. These include, but are not limited to:

*   **Violating Laws or Rights:** Engaging in or promoting illegal activities such as violence, terrorism, child exploitation, human trafficking, sexual solicitation, harassment, or discrimination (USE_POLICY.md, Section 1).
*   **High-Risk Activities:** Planning or developing activities that risk death or bodily harm, including military/warfare applications, illegal weapons development, illegal drugs, operation of critical infrastructure, or encouraging self-harm (USE_POLICY.md, Section 2).
*   **Deception and Misinformation:** Intentionally deceiving or misleading others, such as generating content for fraud, disinformation, defamation, spam, or unauthorized impersonation. Users must not represent model outputs as human-generated (USE_POLICY.md, Section 3).
*   **Unauthorized Professional Practice:** Engaging in the unlicensed practice of professions like finance, law, or medicine (USE_POLICY.md, Section 1.d).
*   **Privacy Violations:** Processing sensitive personal or private information without the necessary legal rights and consents (USE_POLICY.md, Section 1.e).
*   **Improving Other LLMs:** Using the model or its outputs to improve any other large language model (excluding Llama 3 or its derivatives) (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.v).

---

## How to Use
This section outlines how to use the model. 

Insufficient information is available to provide comprehensive code snippets. However, the model uses special tokens to structure inputs and outputs:
*   **Beginning of Sequence Token:** `<|begin_of_text|>` (ID: 128000) (special_tokens_map.json, tokenizer.json)
*   **End of Sequence Token:** `<|end_of_text|>` (ID: 128001) (special_tokens_map.json, tokenizer.json)
*   Other special tokens for formatting include `<|start_header_id|>`, `<|end_header_id|>`, and `<|eot_id|>` (tokenizer.json).

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
Insufficient information

### Motivation:
Insufficient information

### Preprocessing:
The training data was pre-processed for tokenization using a sequence of two pre-tokenizers (tokenizer.json):
1.  **Split:** The text is split based on a regular expression `(?i:'s|'t|'re|'ve|'m|'ll|'d)|[^\\r\\n\\p{L}\\p{N}]?\\p{L}+|\\p{N}{1,3}| ?[^\\s\\p{L}\\p{N}]+[\\r\\n]*|\\s*[\\r\\n]+|\\s+(?!\\S)|\\s+`. This pattern isolates contractions, words, numbers up to 3 digits, and whitespace in a specific manner (tokenizer.json).
2.  **ByteLevel:** This pre-tokenizer processes the text at the byte level, which helps handle any character, including those outside the standard vocabulary (tokenizer.json).

The model uses a Byte-Pair Encoding (BPE) model for tokenization (tokenizer.json).

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
*   **Disk Space:** The model requires approximately 16.06 GB of disk space (index.json).
*   **Memory (RAM/VRAM):** The model weights are stored in `bfloat16` format, which requires 2 bytes per parameter. Loading the model would require at least 16.06 GB of memory, plus overhead for the framework and execution (config.json, index.json).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The use of Meta Llama 3 is governed by an Acceptable Use Policy that outlines key ethical boundaries and risks (USE_POLICY.md).

*   **Risks and Mitigation:** The policy explicitly prohibits using the model for illegal, harmful, or deceptive purposes. This serves as the primary risk mitigation strategy by setting clear guidelines for users. Prohibited uses include:
    *   **Harmful Content:** Generating content related to terrorism, child exploitation, human trafficking, harassment, or discrimination (USE_POLICY.md, Section 1).
    *   **Physical Harm:** Using the model for military applications, illegal weapon development, or activities that could lead to death or bodily harm (USE_POLICY.md, Section 2).
    *   **Deception:** Creating disinformation, fraudulent content, spam, or impersonating individuals. The policy mandates that model outputs should not be represented as human-generated (USE_POLICY.md, Section 3).
    *   **Sensitive Data:** The policy prohibits the processing of sensitive personal or health information without the required legal consents, addressing privacy risks (USE_POLICY.md, Section 1.e).
*   **Reporting Mechanisms:** To address ongoing risks, Meta has established channels for reporting model issues, risky content, security vulnerabilities, and policy violations (USE_POLICY.md).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **"AS IS" Basis:** The model and its outputs are provided on an "AS IS" basis, without any warranties of title, non-infringement, merchantability, or fitness for a particular purpose (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 3).
*   **User Responsibility:** Users are solely responsible for determining the appropriateness of using or redistributing the model and assume all risks associated with its use and outputs (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 3).
*   **Unknown Dangers:** The Acceptable Use Policy requires users to "appropriately disclose to end users any known dangers of your AI system," implying that not all potential risks may be known or mitigated by default (USE_POLICY.md, Section 4).

### Recommendations:
*   **Adherence to Policy:** Users must adhere to the Acceptable Use Policy to ensure safe and responsible use (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.iv).
*   **Attribution:** When distributing the model, derivatives, or services using the model, users should prominently display "Built with Meta Llama 3" and include "Llama 3" in the name of any derivative AI models (META LLAMA 3 COMMUNITY LICENSE AGREEMENT, Section 1.b.i).
*   **Report Issues:** Users are encouraged to report any violations of the policy, software bugs, or other problems that could lead to a policy violation through the provided channels (USE_POLICY.md).