## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Meta (LICENSE.txt). Depending on the user's location, "Meta" refers to Meta Platforms Ireland Limited (for users in the EEA or Switzerland) or Meta Platforms, Inc. (for users outside the EEA or Switzerland) (LICENSE.txt).

### Model date:
The Llama 2 model version was released on July 18, 2023 (LICENSE.txt).

### Model version:
The model is Llama 2 (LICENSE.txt). It was developed using `transformers` version "4.31.0.dev0" (config.json.txt).

### Model type:
The model is a LlamaForCausalLM, which is a type of large language model for causal language modeling (text generation) (config.json.txt). It is part of the Llama 2 family of foundational large language models (LICENSE.txt).

**Architecture Details:**
*   **Model Type:** `llama` (config.json.txt)
*   **Architecture:** `LlamaForCausalLM` (config.json.txt)
*   **Activation Function:** `silu` (config.json.txt)
*   **Hidden Size:** 4096 (config.json.txt)
*   **Intermediate Size:** 11008 (config.json.txt)
*   **Number of Hidden Layers:** 32 (config.json.txt)
*   **Number of Attention Heads:** 32 (config.json.txt)
*   **Number of Key-Value Heads:** 32 (config.json.txt)
*   **Vocabulary Size:** 32000 (config.json.txt)
*   **Context Length (Max Position Embeddings):** 4096 tokens (config.json.txt)
*   **RMS Norm Epsilon:** 1e-05 (config.json.txt)
*   **Initializer Range:** 0.02 (config.json.txt)
*   **Data Type:** `float16` (config.json.txt)

**Model Size:**
The total size of the model weights is approximately 13.48 GB in SafeTensors format (model.safetensors.index.json.txt) and 26.95 GB in PyTorch bin format (pytorch_model.bin.index.json.txt).

**Tokenizer:**
*   **Tokenizer Class:** `LlamaTokenizer` (tokenizer_config.json.txt)
*   **Type:** Byte-Pair Encoding (BPE) (tokenizer.json.txt)
*   **Special Tokens:**
    *   `bos_token` (Beginning of sequence): `<s>` (ID: 1) (special_tokens_map.json.txt, config.json.txt)
    *   `eos_token` (End of sequence): `</s>` (ID: 2) (special_tokens_map.json.txt, config.json.txt)
    *   `unk_token` (Unknown): `<unk>` (ID: 0) (special_tokens_map.json.txt, tokenizer.json.txt)
    *   `pad_token`: The pad token ID is 0 (config.json.txt), but a separate added token file specifies `<pad>` as 32000 (added_tokens.json.txt, generation_config.json.txt).

### Training details:
The model was trained using a `float16` data type (config.json.txt). The pretraining tensor parallelism (`pretraining_tp`) was set to 1 (config.json.txt).

Default generation parameters include:
*   `do_sample`: true (generation_config.json.txt)
*   `temperature`: 0.9 (generation_config.json.txt)
*   `top_p`: 0.6 (generation_config.json.txt)

Insufficient information is available regarding the training algorithms, other hyperparameters (e.g., learning rate, batch size), or any fairness constraints applied during training.

### Paper or other resource for more information:
*   **Documentation:** Specifications, manuals, and documentation are available at `ai.meta.com/resources/models-and-libraries/llama-downloads/` (LICENSE.txt).
*   **GitHub Repository:** A GitHub repository for reporting model issues is located at `github.com/facebookresearch/llama` (USE_POLICY.md.txt).
*   **Acceptable Use Policy:** The full policy is available at `https://ai.meta.com/llama/use-policy` (LICENSE.txt, USE_POLICY.md.txt).

### Citation details:
Insufficient information.

### License:
The model is licensed under the LLAMA 2 COMMUNITY LICENSE AGREEMENT (LICENSE.txt).

Key terms of the license include:
*   **Grant of Rights:** Users are granted a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, copy, create derivative works of, and modify the Llama Materials (LICENSE.txt, Section 1.a).
*   **Redistribution:** If distributing the Llama Materials or derivatives, a copy of the license agreement must be provided to the third party. An attribution notice must also be retained in a "Notice" text file: "Llama 2 is licensed under the LLAMA 2 Community License, Copyright (c) Meta Platforms, Inc. All Rights Reserved." (LICENSE.txt, Section 1.b).
*   **Restrictions:**
    *   Use of the model must comply with applicable laws and the Acceptable Use Policy (USE_POLICY.md.txt).
    *   The Llama Materials or their outputs cannot be used to improve any other large language model (excluding Llama 2 or its derivatives) (LICENSE.txt, Section 1.b.v).
*   **Commercial Terms:** If the monthly active users of a licensee's products or services exceed 700 million, a separate license must be requested from Meta (LICENSE.txt, Section 2).
*   **Disclaimer:** The model is provided "AS IS" without warranties of any kind (LICENSE.txt, Section 3).

### Contact:
For issues, questions, or feedback, the following channels are provided:
*   **Reporting model issues:** [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama) (USE_POLICY.md.txt)
*   **Reporting risky content:** [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback) (USE_POLICY.md.txt)
*   **Reporting bugs and security concerns:** [facebook.com/whitehat/info](http://facebook.com/whitehat/info) (USE_POLICY.md.txt)
*   **Reporting policy violations or unlicensed use:** [LlamaUseReport@meta.com](mailto:LlamaUseReport@meta.com) (USE_POLICY.md.txt)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a foundational large language model designed for causal language modeling, meaning it is a general-purpose text generation model (LICENSE.txt, config.json.txt). Its intended use is not explicitly defined by specific tasks but rather by the broad capabilities of language models, with restrictions on misuse outlined in the Acceptable Use Policy (USE_POLICY.md.txt).

### Primary intended users:
The license agreement addresses a general "Licensee" or "you," which includes individuals, their employers, or other entities (LICENSE.txt). The inclusion of commercial terms suggests that intended users include developers, researchers, and businesses (LICENSE.txt, Section 2).

### Out-of-scope uses:
The Acceptable Use Policy explicitly prohibits using Llama 2 for a range of activities. Any use that violates laws or others' rights is out-of-scope. Prohibited uses include, but are not limited to:

*   **Illegal Activities:** Engaging in, promoting, or inciting violence, terrorism, child exploitation, human trafficking, sexual solicitation, or any other criminal activity (USE_POLICY.md.txt, Section 1.a).
*   **Harmful Content:** Facilitating harassment, abuse, bullying, or discrimination (USE_POLICY.md.txt, Section 1.b, 1.c).
*   **High-Risk Activities:** Use related to military, warfare, espionage, illegal weapons, illegal drugs, operation of critical infrastructure, or activities that present a risk of death or bodily harm (USE_POLICY.md.txt, Section 2).
*   **Deception and Misinformation:** Generating content for fraud, disinformation, defamation, spam, or impersonating an individual without consent. Users must not represent outputs from Llama 2 as being human-generated (USE_POLICY.md.txt, Section 3).
*   **Unlicensed Professional Advice:** Engaging in the unauthorized practice of professions such as finance, law, or medicine (USE_POLICY.md.txt, Section 1.d).
*   **Privacy Violations:** Processing or inferring sensitive personal information about individuals without the required legal rights and consents (USE_POLICY.md.txt, Section 1.e).

---

## How to Use
This section outlines how to use the model.

Insufficient information. No code snippets or specific usage instructions are provided in the repository.

However, based on the configuration files, the model can be used with a `LlamaTokenizer` (tokenizer_config.json.txt). The model expects input tokenized into a sequence of up to 4096 tokens (config.json.txt).

The default generation settings are configured for sampling-based text generation with a temperature of 0.9 and top-p of 0.6 (generation_config.json.txt).

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
Insufficient information. The repository contains the model's trained weights but does not specify the datasets used for training (LICENSE.txt).

### Motivation:
Insufficient information.

### Preprocessing:
While preprocessing steps for the original training data are not available, the tokenizer configuration describes the text normalization process applied to the model's input. This includes:
*   Prepending a space to the input string (tokenizer.json.txt).
*   Replacing the character ` ` with ` ` (tokenizer.json.txt).

The decoder configuration specifies post-processing steps for the generated output, including replacing ` ` with a space and stripping leading spaces (tokenizer.json.txt).

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
The model weights are provided in `float16` precision (config.json.txt). The total size of the model is approximately 13.5 GB (SafeTensors format) or 27 GB (PyTorch bin format) (model.safetensors.index.json.txt, pytorch_model.bin.index.json.txt). Loading the model would require RAM/VRAM sufficient to hold these weights.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development and use of Llama 2 are governed by an Acceptable Use Policy (USE_POLICY.md.txt), which outlines key ethical considerations and risks.

*   **Sensitive Data:** The policy prohibits the use of the model to "collect, process, disclose, generate, or infer health, demographic, or other sensitive personal or private information about individuals without rights and consents required by applicable laws" (USE_POLICY.md.txt, Section 1.e). This indicates that the use of sensitive data was a consideration.

*   **Risks and Mitigation:** The policy identifies numerous potential risks associated with the model's application and prohibits its use in these contexts. These risks include:
    *   **Illegal and Harmful Activities:** Inciting violence, terrorism, child exploitation, human trafficking, harassment, and discrimination (USE_POLICY.md.txt, Section 1).
    *   **Deception:** Generating disinformation, spam, defamatory content, or impersonating individuals (USE_POLICY.md.txt, Section 3).
    *   **Physical Harm:** Use in high-risk domains such as military applications, weapon development, and operation of critical infrastructure is forbidden (USE_POLICY.md.txt, Section 2).
    *   **Unqualified Advice:** The policy prohibits the unauthorized practice of regulated professions like medicine or law (USE_POLICY.md.txt, Section 1.d).

*   **Mitigation Strategies:** The primary mitigation strategy provided is the Acceptable Use Policy itself, which contractually forbids misuse. Meta also provides channels for reporting policy violations, risky content, and security concerns to help mitigate harm (USE_POLICY.md.txt). The policy also mandates that users must "appropriately disclose to end users any known dangers of your AI system" (USE_POLICY.md.txt, Section 4).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The provided repository does not contain information on the datasets used for training or evaluation.
*   No performance metrics (e.g., accuracy, bias, toxicity) are included, making it difficult to assess the model's effectiveness and potential biases.
*   The model should not be used to generate outputs that are represented as being human-generated (USE_POLICY.md.txt, Section 3.e).

### Recommendations:
*   Users must adhere to the LLAMA 2 COMMUNITY LICENSE AGREEMENT (LICENSE.txt) and the Acceptable Use Policy (USE_POLICY.md.txt).
*   Do not use the model for any of the prohibited uses listed in the "Out-of-scope uses" and "Ethical Considerations" sections.
*   Report any violations of the policy, software bugs, or risky content generated by the model through the contact channels provided in the "Contact" section (USE_POLICY.md.txt).
*   Users should disclose to their end users any known dangers associated with their implementation of the model (USE_POLICY.md.txt, Section 4).