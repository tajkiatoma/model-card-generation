## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model's license is provided by SambaNova Systems, Inc. (LICENSE.txt).

### Model date:
The license for the model is dated May 18th, 2023 (LICENSE.txt).

### Model version:
The model version is BLOOMChat-176B v1.0 (LICENSE.txt).

Evaluation results show that BLOOMChat outperforms several other models in human evaluations and translation tasks.
*   In a human evaluation measuring average win rate over 6 languages, BLOOMChat (65.92%) significantly outperformed BLOOMZ (1.46%), OpenAssistant-30B (23.16%), and LLaMA-Adapter-V2-65B (7.55%) (images/Human_evaluation.png).
*   In a translation task comparison using average Bleu score, BLOOMChat (approx. 20) scored higher than BLOOM, BLOOMZ, OpenAssistant-30B, and Vicuna-13B (all approx. 10-11) (images/Multilingual_capabilities_comparison.png).
*   When compared to GPT-4, BLOOMChat had a lower average win rate in human evaluation (44.97% vs. GPT-4's 55.03%) (images/Human_evaluation_gpt4.png) and a lower average Bleu score in translation (approx. 20 vs. GPT-4's approx. 31) (images/Multilingual_capabilities_comparison.png).

### Model type:
The model is a large language model based on the `bigscience/bloom` architecture (tokenizer_config.json.txt).
*   **Architecture:** It is a Transformer-based model, as indicated by the layer names in the model index file (e.g., `transformer.h.0.self_attention`) (pytorch_model.bin.index.json.txt). The model consists of 70 transformer layers (`transformer.h.0` through `transformer.h.69`) (pytorch_model.bin.index.json.txt).
*   **Model Size:** The model name "BLOOMChat-176B" suggests it has 176 billion parameters (LICENSE.txt).
*   **Tokenizer:** It uses the `BloomTokenizer` class (tokenizer_config.json.txt). Special tokens include `<s>` for BOS, `</s>` for EOS, `<pad>` for padding, and `<unk>` for unknown tokens (tokenizer_config.json.txt, special_tokens_map.json.txt).
*   **Context Length:** The `model_max_length` is set to 1000000000000000019884624838656 in the configuration file (tokenizer_config.json.txt).

### Training details:
Insufficient information

### Paper or other resource for more information:
Insufficient information

### Citation details:
Insufficient information

### License:
The model is licensed under the "BLOOMChat-176B LICENSE v1.0" by SambaNova Systems, Inc. (LICENSE.txt).

Key terms of the license include:
*   **Grant of License:** The license grants a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright and patent license to use, reproduce, prepare Derivative Works of, and distribute the Work (LICENSE.txt, Sections 2 & 3).
*   **Redistribution:** Users may redistribute the Work or its derivatives provided they include a copy of the license, retain all original notices, and include the use-based restrictions in any legal agreement governing the distribution (LICENSE.txt, Section 4).
*   **Use-based Restrictions:** The license includes a detailed list of prohibited uses in "ATTACHMENT A". These restrictions forbid using the model for activities such as:
    *   Violating any applicable laws or regulations.
    *   Harming or exploiting minors.
    *   Generating or disseminating verifiably false information to harm others.
    *   Generating or disseminating personally identifiable information to harm an individual.
    *   Defaming, disparaging, or harassing others.
    *   Impersonating others.
    *   Providing medical advice or interpreting medical results.
    *   Discriminating against individuals or groups based on legally protected characteristics.
    *   Use in the administration of justice, law enforcement, immigration, or asylum processes (LICENSE.txt, Section 5 & ATTACHMENT A).
*   **Disclaimer:** The model is provided "AS IS" without warranties of any kind (LICENSE.txt, Section 9).

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for conversational AI (chat) and translation tasks, as demonstrated by the provided evaluation metrics (images/Human_evaluation.png, images/Multilingual_capabilities_comparison.png). The license states that "Use may include creating any content with, finetuning, updating, running, training, evaluating and/or reparametrizing the Work" (LICENSE.txt, Section 5).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
The license explicitly lists several out-of-scope and restricted uses. Users are prohibited from using the model or its derivatives for the following purposes:
*   In any way that violates any applicable national, federal, state, local or international law or regulation (LICENSE.txt, ATTACHMENT A, a).
*   For the purpose of exploiting, harming or attempting to exploit or harm minors in any way (LICENSE.txt, ATTACHMENT A, b).
*   To generate or disseminate verifiably false information with the purpose of harming others (LICENSE.txt, ATTACHMENT A, c).
*   To generate or disseminate personal identifiable information that can be used to harm an individual (LICENSE.txt, ATTACHMENT A, d).
*   To generate or disseminate information or content without expressly and intelligibly disclaiming that the text is machine generated (LICENSE.txt, ATTACHMENT A, e).
*   To defame, disparage or otherwise harass others (LICENSE.txt, ATTACHMENT A, f).
*   To impersonate or attempt to impersonate others (LICENSE.txt, ATTACHMENT A, g).
*   For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation (LICENSE.txt, ATTACHMENT A, h).
*   For any use intended to or which has the effect of discriminating against or harming individuals or groups (LICENSE.txt, ATTACHMENT A, i, k).
*   To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics (LICENSE.txt, ATTACHMENT A, j).
*   To provide medical advice and medical results interpretation (LICENSE.txt, ATTACHMENT A, l).
*   To generate or disseminate information for the purpose to be used for administration of justice, law enforcement, immigration or asylum processes (LICENSE.txt, ATTACHMENT A, m).

---

## How to Use
This section outlines how to use the model.

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance was evaluated across multiple languages, indicating that language is a relevant factor (images/Human_evaluation.png, images/Human_evaluation_gpt4.png, images/Multilingual_capabilities_comparison.png).

### Evaluation factors:
The model was evaluated based on its performance in different languages. The human evaluation win rate was averaged over 6 languages (images/Human_evaluation.png, images/Human_evaluation_gpt4.png), and the translation score was measured on French (fr), Hindi (hi), and Chinese (zh) (images/Multilingual_capabilities_comparison.png).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using the following metrics:
*   **Average Bleu score:** Used to evaluate performance on translation tasks (images/Multilingual_capabilities_comparison.png).
*   **Average Win Rate:** Used in human evaluations to compare the model's output against other models for chat capabilities over 6 languages (images/Human_evaluation.png, images/Human_evaluation_gpt4.png).

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The datasets used for evaluation include:
*   **Translation:** WMT14 for French (fr) and Hindi (hi), and WMT18 for Chinese (zh) (images/Multilingual_capabilities_comparison.png).
*   **Human Evaluation:** The specific datasets used for the human evaluation over 6 languages are not specified (images/Human_evaluation.png, images/Human_evaluation_gpt4.png).

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
Insufficient information

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
**Translation Task Comparison (Average Bleu Score):**
*   **BLOOMChat:** ~20.0
*   GPT-4: ~31.0
*   Vicuna-13B: ~11.0
*   OpenAssistant-30B: ~11.0
*   BLOOMZ: ~10.5
*   BLOOM: ~10.5
(images/Multilingual_capabilities_comparison.png)

**Human Evaluation (Average Win Rate over 6 Languages):**
*   **BLOOMChat:** 65.92%
*   OpenAssistant-30B: 23.16%
*   LLaMA-Adapter-V2-65B: 7.55%
*   BLOOMZ: 1.46%
(images/Human_evaluation.png)

**Human Evaluation vs. GPT-4 (Average Win Rate over 6 Languages):**
*   **BLOOMChat:** 44.97%
*   GPT-4: 55.03%
(images/Human_evaluation_gpt4.png)

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
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The license for BLOOMChat-176B outlines significant ethical considerations and risk mitigation strategies by imposing strict use-based restrictions (LICENSE.txt, ATTACHMENT A).
*   **Sensitive Data:** It is not specified whether sensitive data was used in the training process.
*   **Risk Mitigation:** The license attempts to mitigate risks by prohibiting users from applying the model in harmful ways. Prohibited uses include generating misinformation to harm others, harassment, discrimination, providing medical advice, and applications in law enforcement or justice systems.
*   **Transparency:** The license mandates that any content generated by the model must be clearly disclaimed as machine-generated, which promotes transparency and helps prevent deception (LICENSE.txt, ATTACHMENT A, e).
*   **Accountability:** The license states, "You are accountable for the Output you generate and its subsequent uses" (LICENSE.txt, Section 6).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Based on the license terms, it is a requirement for users to:
*   "expressly and intelligibly" disclaim that any text generated by the model is machine-generated (LICENSE.txt, ATTACHMENT A, e).
*   Adhere strictly to all use-based restrictions outlined in the license to prevent misuse and potential harm (LICENSE.txt, ATTACHMENT A).