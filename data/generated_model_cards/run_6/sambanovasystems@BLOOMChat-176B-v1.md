## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by SambaNova Systems, Inc. (Source: LICENSE.txt).

### Model date:
The license for the model is dated May 18th, 2023 (Source: LICENSE.txt).

### Model version:
The model is named BLOOMChat-176B and the license version is v1.0 (Source: LICENSE.txt). The model was developed using transformers version 4.25.0 (Source: config.json.txt).

### Model type:
The model is a BloomForCausalLM, which is a type of Causal Language Model based on the Bloom architecture (Source: config.json.txt).

**Architecture Details:**
*   **Model Type:** bloom (Source: config.json.txt)
*   **Number of Layers:** 70 (Source: config.json.txt)
*   **Number of Attention Heads:** 112 (Source: config.json.txt)
*   **Hidden Size:** 14336 (Source: config.json.txt)
*   **Vocabulary Size:** 250880 (Source: config.json.txt)
*   **Maximum Length:** 1000000000000000019884624838656 (Source: tokenizer_config.json.txt)

### Training details:
The following hyperparameters and settings were used during the model's development:
*   **Attention Dropout:** 0.0 (Source: config.json.txt)
*   **Hidden Dropout:** 0.0 (Source: config.json.txt)
*   **Initializer Range:** 0.02 (Source: config.json.txt)
*   **Layer Norm Epsilon:** 1e-05 (Source: config.json.txt)
*   **Pretraining Tensor Parallelism (TP):** 4 (Source: config.json.txt)
*   **Masked Softmax Fusion:** Enabled (Source: config.json.txt)
*   **Attention Softmax in fp32:** Disabled (Source: config.json.txt)

### Paper or other resource for more information:
Insufficient information.

### Citation details:
Insufficient information.

### License:
The model is licensed under the "BLOOMChat-176B LICENSE v1.0" (Source: LICENSE.txt).

Key terms of the license include:
*   **Permissions:** You are granted a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and its derivatives (Source: LICENSE.txt, Section 2).
*   **Redistribution:** When redistributing, you must include the use-based restrictions from the license, provide a copy of the license, note any changes made to files, and retain all original copyright, patent, trademark, and attribution notices (Source: LICENSE.txt, Section 4).
*   **Accountability:** You are accountable for the output you generate and its subsequent uses. No use of the output can contravene any provision of the license (Source: LICENSE.txt, Section 6).
*   **Disclaimer:** The model is provided "AS IS" without warranties of any kind (Source: LICENSE.txt, Section 9).
*   **Use Restrictions:** The license includes a detailed list of use-based restrictions in Attachment A, which prohibits using the model for unlawful purposes, harming minors, generating verifiable false information to harm others, and other specific uses (Source: LICENSE.txt, Section 5 & Attachment A).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model's name, "BLOOMChat," suggests it is intended for conversational AI and chat applications (Source: LICENSE.txt). Its evaluation on translation tasks indicates it has multilingual capabilities (Source: images/Multilingual_capabilities_comparison.png). The license states that use may include "creating any content with, finetuning, updating, running, training, evaluating and/or reparametrizing the Work" (Source: LICENSE.txt, Section 5).

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
The license explicitly lists a number of "USE RESTRICTIONS." You agree not to use the model or its derivatives for the following purposes (Source: LICENSE.txt, Attachment A):
*   In any way that violates any applicable law or regulation.
*   For exploiting or harming minors.
*   To generate or disseminate verifiably false information with the purpose of harming others.
*   To generate or disseminate personally identifiable information that can be used to harm an individual.
*   To generate content without expressly disclaiming that it is machine-generated.
*   To defame, disparage, or otherwise harass others.
*   To impersonate or attempt to impersonate others.
*   For fully automated decision-making that adversely impacts an individual’s legal rights.
*   For any use that discriminates against or harms individuals or groups based on social behavior or personal characteristics.
*   To exploit vulnerabilities of a specific group of persons to distort their behavior in a harmful way.
*   For any use that discriminates against individuals or groups based on legally protected characteristics.
*   To provide medical advice and medical results interpretation.
*   For administration of justice, law enforcement, immigration, or asylum processes.

---

## How to Use
This section outlines how to use the model.

While no specific code snippets are provided, the configuration files indicate the following tokenizer settings (Source: tokenizer_config.json.txt, special_tokens_map.json.txt):
*   **Tokenizer Class:** `BloomTokenizer`
*   **Padding Side:** `left`
*   **Special Tokens:**
    *   `bos_token`: `<s>`
    *   `eos_token`: `</s>`
    *   `pad_token`: `<pad>`
    *   `unk_token`: `<unk>`

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Language is a relevant factor, as the model's performance was evaluated across multiple languages (Source: images/Human_evaluation.png, images/Multilingual_capabilities_comparison.png).

### Evaluation factors:
The model was evaluated based on its performance in different languages. The human evaluation was conducted over 6 languages, and the translation evaluation was performed on French (fr), Hindi (hi), and Chinese (zh) (Source: images/Human_evaluation.png, images/Multilingual_capabilities_comparison.png).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was measured using the following metrics:
*   **Average Win Rate:** Used in human evaluations to compare BLOOMChat against other models like BLOOMZ, OpenAssistant, LLaMA-Adapter, and GPT-4 (Source: images/Human_evaluation.png, images/Human_evaluation_gpt4.png).
*   **Average Bleu score:** Used to evaluate performance on translation tasks (Source: images/Multilingual_capabilities_comparison.png).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on the following datasets for translation tasks (Source: images/Multilingual_capabilities_comparison.png):
*   **wmt14:** For French (fr) and Hindi (hi).
*   **wmt18:** For Chinese (zh).

The specific datasets used for the human evaluation (win rate) are not mentioned (Source: images/Human_evaluation.png, images/Human_evaluation_gpt4.png).

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
The model's performance was compared against several other models:

**Human Evaluation (Average Win Rate over 6 Languages):**
*   **BLOOMChat:** 65.92%
*   BLOOMZ: 1.46%
*   OpenAssistant-30B: 23.16%
*   LLaMA-Adapter-V2-65B: 7.55%
(Source: images/Human_evaluation.png)

**Human Evaluation vs. GPT-4 (Average Win Rate over 6 Languages):**
*   **BLOOMChat:** 44.97%
*   GPT-4: 55.03%
(Source: images/Human_evaluation_gpt4.png)

**Translation Task Comparison (Average Bleu score):**
*   **BLOOMChat:** ~20.5
*   GPT-4: ~31.0
*   BLOOM: ~10.5
*   BLOOMZ: ~10.8
*   OpenAssistant-30B: ~11.0
*   Vicuna-13B: ~11.2
(Source: images/Multilingual_capabilities_comparison.png)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The configuration file indicates that the model was developed with a tensor parallelism degree of 4, suggesting a multi-GPU/TPU environment was required for the original training (Source: config.json.txt). However, specific requirements for users to fine-tune the model are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model's license outlines significant ethical considerations and risk mitigation strategies through its "USE RESTRICTIONS" (Source: LICENSE.txt, Attachment A).

**Risks and Mitigation:**
*   **Generation of Harmful Content:** The model could be used to defame, harass, or harm individuals. The license prohibits such use (Source: LICENSE.txt, Attachment A, sections f, i, k).
*   **Disinformation:** The model could generate verifiably false information. The license forbids using the model for this purpose if the intent is to harm others (Source: LICENSE.txt, Attachment A, section c).
*   **Impersonation:** The model could be used to impersonate others. This is explicitly forbidden by the license (Source: LICENSE.txt, Attachment A, section g).
*   **Privacy Violations:** The model could generate or disseminate personally identifiable information. The license prohibits this if it can be used to harm an individual (Source: LICENSE.txt, Attachment A, section d).
*   **Unsafe Medical Advice:** The model is not intended to provide medical advice or interpret medical results, and the license restricts this use case (Source: LICENSE.txt, Attachment A, section l).
*   **Automated Decision-Making:** Using the model for fully automated decision-making that impacts legal rights or creates binding obligations is prohibited (Source: LICENSE.txt, Attachment A, section h).
*   **Misuse in Justice and Law Enforcement:** The license prohibits using the model for the administration of justice, law enforcement, immigration, or asylum processes (Source: LICENSE.txt, Attachment A, section m).

A key mitigation strategy required by the license is transparency: users must "expressly and intelligibly" disclaim that content is machine-generated (Source: LICENSE.txt, Attachment A, section e).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model's performance, while strong against some open models, is lower than GPT-4 in both human evaluation and translation tasks (Source: images/Human_evaluation_gpt4.png, images/Multilingual_capabilities_comparison.png).
*   The human evaluation was conducted over 6 languages, but these languages are not specified, limiting the understanding of the model's specific linguistic strengths and weaknesses (Source: images/Human_evaluation.png).
*   The datasets used for the human "win rate" evaluation are not disclosed (Source: images/Human_evaluation.png).

### Recommendations:
*   Users must adhere to all "USE RESTRICTIONS" outlined in the license to prevent misuse and potential harm (Source: LICENSE.txt, Attachment A).
*   When generating or disseminating content with the model, users must clearly state that the text is machine-generated, as required by the license (Source: LICENSE.txt, Attachment A, section e).
*   Given the restrictions, the model should not be used for applications in sensitive domains such as medicine, law, or for making critical automated decisions about individuals (Source: LICENSE.txt, Attachment A).

---