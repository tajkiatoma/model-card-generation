## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Nolan Dey, Gurpreet Gosal, Zhiming (Charles) Chen, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin Tom, and Joel Hestness from Cerebras Systems (Paper, p. 1).

### Model date:
The model was developed in March 2023 (Paper, p. 18, Table 7). The associated academic paper was submitted to arXiv on April 6, 2023 (Paper, p. 1).

### Model version:
This model is the 13 billion parameter version from the Cerebras-GPT family, which includes models scaled from 111M to 13B parameters (Paper, p. 1). It is the base variant that uses standard parameterization (SP) for initialization, as opposed to other variants trained with Maximal Update Parameterization (µP) (Paper, p. 18, Table 7; p. 19). The tokenizer version is 0.2 (merges.txt, line 1), and the model was developed using transformers version 4.27.2 (config.json).

### Model type:
Cerebras-GPT-13B is an autoregressive, decoder-only transformer language model with 13 billion parameters, similar in architecture to GPT-2 and GPT-3 (Paper, p. 3, Section 2.1; p. 18, Table 7). It uses dense attention in all decoder blocks (Paper, p. 3, Section 2.1).

**Architecture Details:**
*   **Number of Layers:** 40 (config.json)
*   **Hidden Size (`n_embd`):** 5120 (config.json)
*   **Number of Attention Heads (`n_head`):** 40 (config.json)
*   **Feed-Forward Network Size (`n_inner`):** 20480 (config.json)
*   **Activation Function:** GELU (`gelu`) (config.json)
*   **Layer Normalization Epsilon:** 1e-05 (config.json)
*   **Vocabulary Size:** 50257 (config.json)
*   **Context Length (`n_positions`):** 2048 tokens (config.json; Paper, p. 18, Table 7)
*   **Total Size on Disk:** Approximately 51.4 GB (pytorch_model.bin.index.json)

### Training details:
The model was pre-trained following DeepMind's Chinchilla scaling rules for compute-efficiency, using roughly 20 tokens per parameter (Paper, p. 1, 4).

*   **Optimizer:** AdamW with beta1 = 0.9, beta2 = 0.95, and epsilon = 1e-9 (Paper, p. 3, Section 2.3).
*   **Learning Rate:** The maximum learning rate was 1.2E-04 with a cosine decay schedule. The learning rate was warmed up linearly over 375 million tokens and then decayed to 10% of its maximum value (Paper, p. 3, Table 1, Section 2.3).
*   **Batch Size:** The model was trained with a batch size of 720 sequences (1.47M tokens) for the first 84 billion tokens, which was then increased to 1080 sequences (2.21M tokens) for the remainder of the training (Paper, p. 3, Table 1, Section 2.3).
*   **Other Hyperparameters:**
    *   Weight Decay: 0.1 (Paper, p. 3, Section 2.3).
    *   Gradient Norm Clipping: 1.0 (Paper, p. 3, Section 2.3).
    *   Dropout: Not used during pre-training (Paper, p. 3, Section 2.3).
    *   Precision: Trained using bfloat16 (Paper, p. 4).
*   **Initialization:** The model uses standard parameterization (SP). Embedding and hidden layer weights were initialized from a truncated normal distribution with a standard deviation of 0.02. The last layer in each residual network was initialized with a standard deviation of 0.02/sqrt(2 * n_layers) (Paper, p. 4, Section 2.4).

### Paper or other resource for more information:
The primary resource is the academic paper: "Cerebras-GPT: Open Compute-Optimal Language Models" by Nolan Dey, et al. (Paper, p. 1).

The pre-trained models are available on HuggingFace at `https://huggingface.co/cerebras`, and the source code is available in the Cerebras Modelzoo at `https://github.com/Cerebras/modelzoo` (Paper, p. 1, 13, 19).

### Citation details:
Insufficient information.

### License:
The model is released under the Apache 2.0 license, which permits commercial and non-commercial use (Paper, p. 18, Table 7; p. 19).

### Contact:
For feedback on the model, contact Nolan Dey and Joel Hestness at `{nolan, joel}@cerebras.net` (Paper, p. 1, 18).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use is to further research into large language models. It can be used as a foundation model for Natural Language Processing (NLP) applications, ethics research, and alignment research (Paper, p. 18, Table 7).

### Primary intended users:
The model is intended for researchers working to improve Large Language Models (LLMs) and for practitioners seeking reference implementations, training setups, hyperparameters, or pre-trained models (Paper, p. 18, Table 7).

### Out-of-scope uses:
The model has not been tested for factual accuracy, profanity, or toxicity. Further safety-related testing, mitigations, and output curation should be applied before using the Cerebras-GPT model family in production downstream applications (Paper, p. 13, Section 7; p. 18, Table 7).

---

## How to Use
This section outlines how to use the model. 

The model is available on HuggingFace (`https://huggingface.co/cerebras`) and can be used with the transformers library (Paper, p. 1, 19). The provided repository data does not include specific code snippets for model usage.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model was trained on The Pile dataset, which is known to contain content that is toxic, gender-biased, pejorative, and racially sensitive (Paper, p. 18, Table 7). An analysis of the model's biases was conducted across nine categories: Race/Color, Socioeconomic status, Gender, Age, Religion, Disability, Sexual orientation, Nationality, and Physical appearance (Paper, p. 28, Table 11).

### Evaluation factors:
The model was evaluated for various bias factors using the CrowS-Pairs dataset task (Paper, p. 18, Table 7).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was measured using:
*   **Upstream (Pre-training):** Text prediction cross-entropy loss (in nats/token) on the Pile test set (Paper, p. 5, footnote 3; p. 18, Table 7).
*   **Downstream:** Text generation accuracy on a suite of seven common sense reasoning tasks: HellaSwag, PIQA, WinoGrande, Lambada, ARC (easy and challenge versions), and OpenBookQA (Paper, p. 6, Section 3.2; p. 18, Table 7).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Due to compute budget restrictions, variability analysis was only performed for smaller versions of the Cerebras-GPT models. This involved multiple training runs from different random initializations and data loader seeds to assess variance in task performance (Paper, p. 18, Table 7). The run-to-run standard deviation in loss was found to be around 0.35% (Paper, p. 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Upstream Evaluation:** The Pile validation and test set splits were used for pre-training evaluation (Paper, p. 18, Table 7).
*   **Downstream Evaluation:** A suite of standardized tests was used via the EleutherAI evaluation harness (Paper, p. 6, Section 3.2). These include:
    *   **Cloze and Completion:** LAMBADA, HellaSwag
    *   **Common Sense Reasoning:** PIQA, ARC, OpenBookQA
    *   **Winograd Schema:** WinoGrande (Paper, p. 18, Table 7)
*   **Bias Evaluation:** The CrowS-Pairs dataset was used to measure social biases (Paper, p. 18, Table 7).

### Motivation:
The evaluation tasks were selected to align closely with related works in the field and to cover a broad cross-section of NLP task types (Paper, p. 18, Table 7).

### Preprocessing:
Downstream evaluations were performed using the standard splits and formats provided by the EleutherAI evaluation harness (Paper, p. 6, Section 3.2).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on The Pile, an 800GB open-source dataset composed of 22 diverse text sources, including Common Crawl, PubMed Central, Books3, OpenWebText2, Github, and arXiv (Paper, p. 3, Section 2.2; p. 14, Gao et al., 2020). The tokenized version of the training set contains approximately 371 billion tokens (Paper, p. 19, Appendix A.1).

### Motivation:
The Pile was chosen because it is a large, open-source dataset that has been used to train other publicly available models, allowing for fair and direct comparisons of model performance and training efficiency (Paper, p. 5, Section 3.1).

### Preprocessing:
The raw text from The Pile was cleaned using the `ftfy` library to normalize text and then filtered with scripts provided by EleutherAI. The cleaned data was tokenized using a byte-pair encoding (BPE) tokenizer with the GPT-2 vocabulary of size 50,257. As a final step, the entire training dataset was shuffled across all documents to improve model generalization. The dataset was not deduplicated (Paper, p. 3, Section 2.2; p. 18, Table 7; p. 19, Appendix A.1).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the 13B model is reported across several tasks and dimensions:
*   **Pile Test Loss:** 1.572 (Paper, p. 7, Table 2).
*   **Zero-Shot Downstream Task Accuracy:**
    *   HellaSwag: 0.513
    *   PIQA: 0.766
    *   WinoGrande: 0.646
    *   Lambada: 0.696
    *   ARC-e: 0.714
    *   ARC-c: 0.367
    *   OpenBookQA: 0.286
    *   **Average:** 0.570 (Paper, p. 7, Table 2).
*   **Five-Shot Downstream Task Accuracy:**
    *   HellaSwag: 0.514
    *   PIQA: 0.768
    *   WinoGrande: 0.674
    *   Lambada: 0.655
    *   ARC-e: 0.743
    *   ARC-c: 0.398
    *   OpenBookQA: 0.318
    *   **Average:** 0.581 (Paper, p. 25, Table 9).
*   **Bias Scores (CrowS-Pairs, higher is more biased):**
    *   Race/Color: 55.1
    *   Socioeconomic: 72.1
    *   Gender: 67.5
    *   Age: 73.6
    *   Religion: 81.1
    *   Disability: 73.8
    *   Sexual orientation: 78.5
    *   Nationality: 59.7
    *   Physical appearance: 75.0
    *   **Average:** 65.7 (Paper, p. 28, Table 11).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights on disk is approximately 51.4 GB (pytorch_model.bin.index.json). To load the model in bfloat16 precision, approximately 26 GB of RAM or VRAM would be required (13 billion parameters * 2 bytes/parameter).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on the Andromeda AI Supercomputer, a cluster of 16 Cerebras CS-2 systems. Specifically, the 13B model was trained on 12 CS-2 systems (Paper, p. 12, Table 6; p. 18, Table 7). The training was performed using PyTorch and the Cerebras Software Platform (CSoft) release 1.8 (Paper, p. 18, Table 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Sensitive Data:** The model was trained on The Pile dataset, which is known to contain toxic, gender-biased, pejorative, and racially sensitive content (Paper, p. 18, Table 7).
*   **Risks and Harms:** There is a risk of distributional bias from the training data manifesting in the model's outputs. Other potential harms associated with large language models include amplifying social stereotypes, memorizing and revealing private information from the training data, and generating factually incorrect or harmful content (Paper, p. 18, Table 7).
*   **Risk Mitigation:** During pre-training, the only mitigations employed were those included in the standard pre-processing of The Pile dataset (Paper, p. 18, Table 7). The model's outputs may not align with human values, and the risks should be thoroughly investigated before deploying it in a production environment that could directly impact human life (Paper, p. 18, Table 7).
*   **Known Fraught Use Cases:** The paper recommends that "further safety-related testing, mitigations, and output curation should be applied" before using the model in any production downstream applications (Paper, p. 18, Table 7).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Architecture:** The model uses a well-established architecture but does not incorporate more recent features like RoPE, ALiBi, or SwiGLU, which might offer further improvements (Paper, p. 13, Section 7).
*   **Training Paradigms:** The model was not trained with instruction fine-tuning or denoising pre-training objectives (Paper, p. 13, Section 7).
*   **Dataset:** The training data was not deduplicated, which could be a future area for improvement (Paper, p. 13, Section 7).
*   **Evaluation:** The model has not been extensively tested for factual accuracy, profanity, toxicity, or other socially undesirable text generation. Its performance in real-world application settings is unknown (Paper, p. 13, Section 7).

### Recommendations:
*   Users should conduct further safety-related testing, apply mitigations, and curate outputs before deploying this model in any production setting (Paper, p. 13, Section 7).
*   Further bias evaluation and mitigation are recommended before deployment, especially since compute-optimal training may extract biases more efficiently (Paper, p. 28, Appendix C.4).

---