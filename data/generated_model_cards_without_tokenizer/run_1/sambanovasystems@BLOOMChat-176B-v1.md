## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by SambaNova Systems, Inc. (Source: `BLOOMChat-176B LICENSE v1.0`).

### Model date:
The license associated with the model is dated May 18th, 2023 (Source: `BLOOMChat-176B LICENSE v1.0`). No other dates regarding the model's development timeline are provided.

### Model version:
The model is named BLOOMChat-176B. The configuration specifies it was built using `transformers` version 4.25.0 (Source: `config.json.txt`). Human evaluation results show that BLOOMChat has a significantly higher average win rate (65.92%) over 6 languages compared to models like BLOOMZ (1.46%), OpenAssistant-30B (23.16%), and LLaMA-Adapter-V2-65B (7.55%) (Source: `images/Human_evaluation.png`). In translation tasks, it achieves a higher average BLEU score than BLOOM, BLOOMZ, OpenAssistant-30B, and Vicuna-13B (Source: `images/Multilingual_capabilities_comparison.png`).

### Model type:
The model is a `BloomForCausalLM`, which is a type of Transformer-based language model for causal language modeling (Source: `config.json.txt`). It is based on the `bloom` model type (Source: `config.json.txt`).

Key architectural details include:
*   **Parameters:** 176 billion (implied by the model name "BLOOMChat-176B").
*   **Layers (`n_layer`):** 70 (Source: `config.json.txt`).
*   **Attention Heads (`n_head`):** 112 (Source: `config.json.txt`).
*   **Hidden Size (`hidden_size`):** 14336 (Source: `config.json.txt`).
*   **Vocabulary Size (`vocab_size`):** 250880 (Source: `config.json.txt`).
*   **Layer Norm Epsilon:** 1e-05 (Source: `config.json.txt`).
*   **Initializer Range:** 0.02 (Source: `config.json.txt`).

The model weights are sharded into 20 files (Source: `pytorch_model.bin.index.json.txt`).

### Training details:
The model is a Causal Language Model, as indicated by its architecture `BloomForCausalLM` (Source: `config.json.txt`). The following hyperparameters were used during its configuration:
*   `attention_dropout`: 0.0 (Source: `config.json.txt`).
*   `hidden_dropout`: 0.0 (Source: `config.json.txt`).
*   `apply_residual_connection_post_layernorm`: false (Source: `config.json.txt`).
*   `attention_softmax_in_fp32`: false (Source: `config.json.txt`).
*   `masked_softmax_fusion`: true (Source: `config.json.txt`).

No other details about the training algorithm, data, or process are available.

### Paper or other resource for more information:
Insufficient information.

### Citation details:
Insufficient information.

### License:
The model is licensed under the "BLOOMChat-176B LICENSE v1.0" (Source: `BLOOMChat-176B LICENSE v1.0`).

Key terms of the license include:
*   **Grant of License:** The license grants a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright and patent license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work (Source: `BLOOMChat-176B LICENSE v1.0`, Sections 2 & 3).
*   **Redistribution:** Users may reproduce and distribute copies of the Work or its derivatives, provided they include the use-based restrictions, a copy of the license, and retain all original copyright, patent, trademark, and attribution notices (Source: `BLOOMChat-176B LICENSE v1.0`, Section 4).
*   **Use-Based Restrictions:** The license includes a list of prohibited uses, detailed in Attachment A. These restrictions must be included in any legal agreement governing the use or distribution of the model (Source: `BLOOMChat-176B LICENSE v1.0`, Sections 4a & 5).
*   **Disclaimer:** The model is provided "AS IS" without warranties of any kind. The Licensor and Contributors are not liable for any damages arising from the use of the model (Source: `BLOOMChat-176B LICENSE v1.0`, Sections 9 & 10).
*   **Output:** The user is accountable for the output they generate and its subsequent uses. No use of the output can contravene any provision of the license (Source: `BLOOMChat-176B LICENSE v1.0`, Section 6).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for use as a multilingual conversational agent or chatbot, as suggested by its name "BLOOMChat" and its evaluation across multiple languages (Source: `images/Human_evaluation.png`). It also has strong multilingual capabilities, particularly for translation tasks (Source: `images/Multilingual_capabilities_comparison.png`).

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
The license explicitly lists several out-of-scope and restricted uses in "ATTACHMENT A". Users agree not to use the model or its derivatives for the following purposes (Source: `BLOOMChat-176B LICENSE v1.0`, Attachment A):
*   In any way that violates any applicable law or regulation.
*   For exploiting or harming minors.
*   To generate or disseminate verifiably false information with the purpose of harming others.
*   To generate or disseminate personally identifiable information to harm an individual.
*   To generate or disseminate content without an express disclaimer that the text is machine-generated.
*   To defame, disparage, or harass others.
*   To impersonate others.
*   For fully automated decision-making that adversely impacts an individual’s legal rights.
*   For uses that discriminate against or harm individuals or groups based on social behavior or personal characteristics.
*   To exploit vulnerabilities of a specific group of persons to distort their behavior in a harmful way.
*   To discriminate against individuals or groups based on legally protected characteristics.
*   To provide medical advice and medical results interpretation.
*   For administration of justice, law enforcement, immigration, or asylum processes.

---

## How to Use
This section outlines how to use the model. 

Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Language is a key factor influencing the model's performance. The model's capabilities were evaluated across 6 different languages for human preference and on specific languages (French, Hindi, Chinese) for translation tasks (Source: `images/Human_evaluation.png`, `images/Multilingual_capabilities_comparison.png`).

### Evaluation factors:
The model was evaluated based on its performance across multiple languages (Source: `images/Human_evaluation.png`, `images/Multilingual_capabilities_comparison.png`).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using the following metrics:
*   **Average Win Rate:** Used in human evaluations to compare BLOOMChat's responses against other models like GPT-4, BLOOMZ, OpenAssistant-30B, and LLaMA-Adapter-V2-65B (Source: `images/Human_evaluation.png`, `images/Human_evaluation_gpt4.png`).
*   **Average BLEU score:** Used to measure performance on translation tasks (Source: `images/Multilingual_capabilities_comparison.png`).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated for translation tasks using the following datasets (Source: `images/Multilingual_capabilities_comparison.png`):
*   **WMT14:** for French (fr) and Hindi (hi) translation.
*   **WMT18:** for Chinese (zh) translation.

The specific dataset used for the human evaluation of chat capabilities across 6 languages is not specified (Source: `images/Human_evaluation.png`).

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
**Human Evaluation (Average Win Rate over 6 Languages)**
*   **Against other open models:**
    *   **BLOOMChat:** 65.92%
    *   OpenAssistant-30B: 23.16%
    *   LLaMA-Adapter-V2-65B: 7.55%
    *   BLOOMZ: 1.46%
    (Source: `images/Human_evaluation.png`)

*   **Against GPT-4:**
    *   **BLOOMChat:** 44.97%
    *   GPT-4: 55.03%
    (Source: `images/Human_evaluation_gpt4.png`)

**Translation Task Comparison (Average BLEU score over fr, hi, and zh)**
*   BLOOMChat achieved an average BLEU score of approximately 20, outperforming BLOOM, BLOOMZ, OpenAssistant-30B, and Vicuna-13B, but underperforming GPT-4 (Source: `images/Multilingual_capabilities_comparison.png`).

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
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The developers have implemented risk mitigation strategies through the model's license, which contains a comprehensive set of use-based restrictions. These restrictions are designed to prevent the model from being used for harmful or unethical purposes (Source: `BLOOMChat-176B LICENSE v1.0`, Attachment A).

Prohibited uses that address ethical risks include:
*   **Misinformation:** Generating or disseminating verifiably false information to harm others is forbidden.
*   **Harassment and Harm:** The model cannot be used to defame, disparage, harass, or exploit individuals, especially minors.
*   **Discrimination:** Any use intended to discriminate against or harm individuals or groups based on social behavior, personal characteristics, or legally protected categories is prohibited.
*   **Unsafe Advice:** Providing medical advice is an out-of-scope use.
*   **Sensitive Decision-Making:** The model cannot be used for fully automated decision-making that impacts legal rights or for applications in the administration of justice, law enforcement, or immigration.
*   **Transparency:** Users who disseminate content generated by the model must expressly disclaim that it is machine-generated.

The license also places accountability on the user, stating, "You are accountable for the Output you generate and its subsequent uses" (Source: `BLOOMChat-176B LICENSE v1.0`, Section 6).

### Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The datasets used for training and for the human evaluation of chat capabilities are not disclosed.
*   Performance results are aggregated over multiple languages; a breakdown of performance for each of the 6 languages evaluated is not available.
*   Quantitative analyses show that while BLOOMChat is competitive with other open models, it underperforms GPT-4 in both human preference evaluations and translation tasks (Source: `images/Human_evaluation_gpt4.png`, `images/Multilingual_capabilities_comparison.png`).

### Recommendations:
*   Users must strictly adhere to the use-based restrictions outlined in Attachment A of the license to prevent misuse and potential harm (Source: `BLOOMChat-176B LICENSE v1.0`).
*   When disseminating content generated by the model, users must clearly state that the text is machine-generated, as required by the license (Source: `BLOOMChat-176B LICENSE v1.0`, Attachment A, item e).
*   Given that the model can generate incorrect or biased information, users should critically evaluate all outputs before relying on them for any purpose.

---