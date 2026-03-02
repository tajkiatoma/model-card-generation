## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by SambaNova Systems, Inc. (LICENSE).

### Model date:
The license for the model is dated May 18th, 2023 (LICENSE).

### Model version:
The model license is version 1.0 (LICENSE). The model was developed using version 4.25.0 of the Transformers library (config.json).

Comparative performance evaluations show that BLOOMChat has a significantly higher average win rate (65.92%) over 6 languages compared to models like BLOOMZ (1.46%), OpenAssistant-30B (23.16%), and LLaMA-Adapter-V2-65B (7.55%) (Image1.png). However, it has a lower win rate (44.97%) compared to GPT-4 (55.03%) (Image2.png). In translation tasks, BLOOMChat also outperforms several other models but scores lower than GPT-4 (Image3.png).

### Model type:
The model is a **BloomForCausalLM**, a type of Transformer-based language model for causal language modeling (text generation) (config.json).

**Architecture Details (config.json):**
*   **Model Type:** bloom
*   **Number of Layers (n_layer):** 70
*   **Number of Attention Heads (n_head):** 112
*   **Hidden Size (hidden_size):** 14336
*   **Vocabulary Size (vocab_size):** 250880
*   **Layer Norm Epsilon:** 1e-05
*   **Initializer Range:** 0.02
*   **Attention Dropout:** 0.0
*   **Hidden Dropout:** 0.0

**Model Size:**
The model has 176 billion parameters, as indicated by its name "BLOOMChat-176B".

### Training details:
The following hyperparameters were used during the model's development (config.json):
*   **Attention Dropout:** 0.0
*   **Hidden Dropout:** 0.0
*   **Initializer Range:** 0.02
*   **Layer Norm Epsilon:** 1e-05
*   **Pretraining Tensor Parallelism (pretraining_tp):** 4
*   **Masked Softmax Fusion:** Enabled
*   **Attention Softmax in fp32:** Disabled

Other details about the training process, such as the specific algorithms, datasets, or fairness constraints, are not available.

### Paper or other resource for more information:
Insufficient information.

### Citation details:
Insufficient information.

### License:
The model is licensed under the BLOOMChat-176B LICENSE v1.0 (LICENSE).

Key terms of the license include (LICENSE):
*   **Grant of License:** The license grants a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright and patent license to use, reproduce, distribute, and create derivative works.
*   **Redistribution:** Users may redistribute the work or its derivatives provided they include a copy of the license, state any changes made, retain all original notices, and include the use-based restrictions in any legal agreement governing the distribution.
*   **Use-Based Restrictions:** The model cannot be used for specific purposes outlined in Attachment A of the license. These include violating laws, harming minors, generating verifiable false information to harm others, disseminating personally identifiable information to harm individuals, defaming or harassing others, and providing medical advice, among others.
*   **Disclaimer:** The model is provided "AS IS" without any warranties. The licensor is not liable for any damages arising from the use of the model.

The full license text is available in the repository (LICENSE).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a causal language model intended for chat and text generation tasks (config.json, model name). Its performance has been evaluated on multilingual tasks, including translation, suggesting it is capable of functioning across multiple languages (Image1.png, Image3.png). The model takes text as input and generates text as output (config.json).

### Primary intended users:
Insufficient information.

### Out-of-scope uses:
The license explicitly lists several use cases that are out-of-scope and restricted. Users agree not to use the model or its derivatives for the following purposes (LICENSE, Attachment A):
*   In any way that violates any applicable law or regulation.
*   For exploiting or harming minors.
*   To generate or disseminate verifiably false information with the purpose of harming others.
*   To generate or disseminate personally identifiable information that can be used to harm an individual.
*   To generate content without expressly disclaiming that it is machine-generated.
*   To defame, disparage, or otherwise harass others.
*   To impersonate others.
*   For fully automated decision-making that adversely impacts an individual’s legal rights.
*   For any use that discriminates against or harms individuals or groups based on social behavior or personal characteristics.
*   To exploit vulnerabilities of a specific group of people to distort their behavior in a way that causes harm.
*   To discriminate against individuals or groups based on legally protected characteristics.
*   To provide medical advice and medical results interpretation.
*   For the administration of justice, law enforcement, immigration, or asylum processes.

---

## How to Use
This section outlines how to use the model. 

Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Language is a key factor influencing the model's performance. The model's capabilities were evaluated across six languages and on specific translation tasks involving French, Hindi, and Chinese (Image1.png, Image3.png).

### Evaluation factors:
The model was evaluated based on its performance across different languages (Image1.png, Image2.png, Image3.png).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was measured using the following metrics:
*   **Average Win Rate:** Used to compare the model's output against other models (BLOOMZ, OpenAssistant-30B, LLaMA-Adapter-V2-65B, and GPT-4) in a general sense over 6 languages (Image1.png, Image2.png).
*   **Average BLEU score:** Used to evaluate the quality of machine translation for French, Hindi, and Chinese (Image3.png).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model's translation performance was evaluated on the following datasets (Image3.png):
*   **WMT14:** For French (fr) and Hindi (hi) translation tasks.
*   **WMT18:** For Chinese (zh) translation tasks.

Information about the datasets used for the "Average Win Rate" evaluation is not available (Image1.png, Image2.png).

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
The model's performance was compared against several other language models:

**Average Win Rate Over 6 Languages (Image1.png, Image2.png):**
*   **BLOOMChat:** 65.92%
*   **BLOOMZ:** 1.46%
*   **OpenAssistant-30B:** 23.16%
*   **LLaMA-Adapter-V2-65B:** 7.55%

*   **BLOOMChat:** 44.97%
*   **GPT-4:** 55.03%

**Translation Task Comparison (Average BLEU score over fr, hi, and zh) (Image3.png):**
*   **BLOOMChat:** ~20.5
*   **GPT-4:** ~31.0
*   **BLOOM:** ~10.5
*   **BLOOMZ:** ~10.8
*   **OpenAssistant-30B:** ~11.0
*   **Vicuna-13B:** ~11.2

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

The developers have implemented risk mitigation strategies through the model's license, which explicitly prohibits usage for unethical or harmful purposes (LICENSE, Attachment A). These restrictions address risks such as:
*   **Generation of Harmful Content:** Prohibits generating verifiably false information to harm others, defaming or harassing individuals, and exploiting or harming minors.
*   **Misinformation and Deception:** Requires users to clearly state that content is machine-generated and prohibits impersonation.
*   **Discrimination and Bias:** Forbids use that discriminates against individuals or groups based on legally protected characteristics, social behavior, or personal characteristics.
*   **Unsafe Automated Decision-Making:** Restricts use for fully automated decision-making that impacts legal rights or for sensitive applications like law enforcement, immigration, and medical advice.

There is no information provided about the use of sensitive data during the model's training or evaluation.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Limitations:** While BLOOMChat outperforms several open-source models, quantitative analyses show it still underperforms compared to state-of-the-art models like GPT-4 in both general win rate and specific translation tasks (Image2.png, Image3.png).
*   **Limited Evaluation Scope:** The provided evaluations are based on an unspecified set of 6 languages for win rate and on WMT14/WMT18 datasets for specific translation tasks. The model's performance on other languages, domains, or tasks is not documented.
*   **Accountability for Output:** The licensor claims no rights in the output generated by the user, and the user is accountable for the output and its subsequent uses (LICENSE, Section 6).

### Recommendations:
*   **Disclose AI-Generated Content:** When generating or disseminating content, users must "expressly and intelligibly disclaim that the text is machine generated" (LICENSE, Attachment A).
*   **Adhere to Use Restrictions:** Users must strictly adhere to the use-based restrictions outlined in the license to prevent misuse and potential harm (LICENSE, Attachment A).