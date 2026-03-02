## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Nolan Dey, Gurpreet Gosal, Zhiming (Charles) Chen, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin Tom, and Joel Hestness from Cerebras Systems (Cerebras-GPT: Open Compute-Optimal Language Models, page 1).

### Model date:
The model was released in March 2023 (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7: Cerebras-GPT 13B Parameter Model Card, page 18). The accompanying paper was submitted in April 2023 (Cerebras-GPT: Open Compute-Optimal Language Models, page 1).

### Model version:
This model card describes the 13 billion parameter version of the Cerebras-GPT family. The models were released with two parameterization schemes: Standard Parameterization (SP) and Maximal Update Parameterization (µP). The µP variant is designed to improve training stability and hyperparameter transferability across model scales (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.4, page 4). The models are compatible with transformers version 4.27.2 (config.json).

### Model type:
Cerebras-GPT is an autoregressive, decoder-only transformer language model with an architecture similar to GPT-2 and GPT-3 (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.1, page 3; Table 7, page 18). It uses dense attention in all decoder blocks (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.1, page 3).

**Architecture Details for the 13B Model:**
*   **Parameters:** 13 billion (Cerebras-GPT: Open Compute-Optimal Language Models, Abstract, page 1)
*   **Activation Function:** GELU (config.json)
*   **Number of Layers (`n_layer`):** 40 (config.json; Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18)
*   **Hidden Size (`n_embd`):** 5120 (config.json; Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18)
*   **Number of Attention Heads (`n_head`):** 40 (config.json)
*   **Head Size:** 128 (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18)
*   **Filter Size (`n_inner`):** 20480 (config.json; Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18)
*   **Context Length (`n_positions`):** 2048 tokens (config.json; Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18)
*   **Vocabulary Size (`vocab_size`):** 50257 (config.json)
*   **Total Size on Disk:** Approximately 51.4 GB (pytorch_model.bin.index.json)

### Training details:
The model was trained using the AdamW optimizer with beta1=0.9, beta2=0.95, and an epsilon of 1e-9. A weight decay of 0.1 and gradient norm clipping of 1.0 were applied. No dropout was used during pre-training (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.3, page 3).

The training process included a linear learning rate warmup over 375 million tokens, followed by a cosine decay to 10% of the maximum learning rate of 1.2E-04. The batch size was initially 1.47 million tokens (720 sequences of length 2048) and was increased to 2.21 million tokens (1080 sequences) after 84 billion tokens to manage gradient noise (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.3 and Table 1, page 3). The model was trained using bfloat16 precision for stability (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.3, page 4).

The model was trained following the DeepMind Chinchilla scaling methodology, using approximately 20 tokens per parameter for compute-optimal training (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.3, page 4).

### Paper or other resource for more information:
**Paper:** Dey, N., Gosal, G., Chen, Z. C., Khachane, H., Marshall, W., Pathria, R., Tom, M., & Hestness, J. (2023). *Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster*. arXiv:2304.03208. Available at: https://arxiv.org/abs/2304.03208v1 (Cerebras-GPT: Open Compute-Optimal Language Models... .pdf)

**Model Repository:** The pre-trained models are available on HuggingFace at https://huggingface.co/cerebras (Cerebras-GPT: Open Compute-Optimal Language Models, page 1).

**Source Code:** The source code is available in the Cerebras Modelzoo at https://github.com/Cerebras/modelzoo (Cerebras-GPT: Open Compute-Optimal Language Models, page 13).

### Citation details:
Insufficient information. The paper does not provide a BibTeX entry.

### License:
The model is released under the Apache 2.0 license, which permits commercial and non-commercial use (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18; page 19).

### Contact:
For feedback on the model, contact Nolan Dey and Joel Hestness at {nolan, joel}@cerebras.net (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use is to further research into large language models. The model can be used as a foundation model for Natural Language Processing (NLP) applications, ethics, and alignment research (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

### Primary intended users:
The primary intended users are researchers working to improve Large Language Models (LLMs) and practitioners looking for reference implementations, training setups, hyperparameters, or pre-trained models (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

### Out-of-scope uses:
The model has not been extensively tested for factual accuracy, toxicity, or other socially undesirable text generation. Further safety-related testing, mitigations, and output curation should be applied before using the Cerebras-GPT model family in production downstream applications (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13; Table 7, page 18).

---

## How to Use
This section outlines how to use the model. 

Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is known to be influenced by societal biases present in the training data. Factors evaluated include biases related to race/color, socioeconomic status, gender, age, religion, disability, sexual orientation, nationality, and physical appearance (Cerebras-GPT: Open Compute-Optimal Language Models, Section C.4 and Table 11, page 28).

### Evaluation factors:
The model was evaluated for bias using the CrowS-Pairs dataset, which measures bias across nine different categories (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18; Section C.4, page 28).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's pre-training performance was measured using cross-entropy loss on the Pile test set. For downstream tasks, performance was measured by text generation accuracy on a suite of seven common sense reasoning tasks, including HellaSwag, PIQA, WinoGrande, Lambada, ARC, and OpenBookQA (Cerebras-GPT: Open Compute-Optimal Language Models, Section 3.1, page 5; Section 3.2, page 6; Table 7, page 18).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Due to compute budget restrictions, variability analysis was limited to smaller versions of the Cerebras-GPT models. This involved multiple training runs with different random initializations and data loader seeds to assess variance in task performance (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
**Upstream (Pre-training) Evaluation:**
*   **Dataset:** The Pile validation and test sets were used (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18). The Pile is an 800GB dataset of diverse text from 22 sources (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.2, page 3).

**Downstream Task Evaluation:**
*   **Datasets:** A suite of standardized tests was used via the EleutherAI evaluation harness (Cerebras-GPT: Open Compute-Optimal Language Models, Section 3.2, page 6).
    *   **Cloze and completion tasks:** LAMBADA, HellaSwag
    *   **Common Sense Reasoning tasks:** PIQA, ARC (easy and challenge versions), OpenBookQA
    *   **Winograd schema type tasks:** WinoGrande
*   **Bias Evaluation:** The CrowS-Pairs dataset was used to measure social biases (Cerebras-GPT: Open Compute-Optimal Language Models, Section C.4, page 28).

### Motivation:
The evaluation tasks were selected to closely align with related works in the field and to cover a broad cross-section of common sense reasoning and language understanding capabilities (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

### Preprocessing:
The raw text of the Pile dataset was cleaned using the `ftfy` library to normalize text and clean corrupted Unicode. The data was then tokenized using byte-pair encoding with the GPT-2 vocabulary (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.2, page 3; Appendix A.1, page 19).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on the Pile dataset, an 800GB open-source collection of text from 22 diverse sources, including Common Crawl, PubMed Central, Books3, OpenWebText2, Github, and arXiv (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.2, page 3). The tokenized version of the training set contains approximately 371 billion tokens (Cerebras-GPT: Open Compute-Optimal Language Models, Appendix A.1, page 19).

### Motivation:
Insufficient information.

### Preprocessing:
The Pile dataset was preprocessed using tools from EleutherAI. The raw text was cleaned using the `ftfy` library to normalize text. The data was then tokenized using a byte-pair encoding (BPE) with the GPT-2 vocabulary of size 50,257. Finally, the entire training dataset was shuffled across all documents to improve model generalization (Cerebras-GPT: Open Compute-Optimal Language Models, Section 2.2, page 3; Appendix A.1, page 19).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
**Downstream Task Performance (Zero-shot):**
The 13B model achieved the following accuracies on various downstream tasks (Cerebras-GPT: Open Compute-Optimal Language Models, Table 2, page 7):
*   **HellaSwag:** 0.513
*   **PIQA:** 0.766
*   **WinoGrande:** 0.646
*   **Lambada:** 0.696
*   **ARC-e:** 0.714
*   **ARC-c:** 0.367
*   **OpenBookQA:** 0.286
*   **Average:** 0.570

**Bias Analysis (CrowS-Pairs):**
The model's bias score (higher is more biased) was evaluated across nine categories (Cerebras-GPT: Open Compute-Optimal Language Models, Table 11, page 28):
*   **Race/Color:** 55.1
*   **Socioeconomic status:** 72.1
*   **Gender:** 67.5
*   **Age:** 73.6
*   **Religion:** 81.1
*   **Disability:** 73.8
*   **Sexual orientation:** 78.5
*   **Nationality:** 59.7
*   **Physical appearance:** 75.0
*   **Average:** 65.7

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights have a total size of approximately 51.4 GB on disk (pytorch_model.bin.index.json). Loading the model in float32 would require at least this much RAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on the Andromeda AI Supercomputer, which is a Cerebras Wafer-Scale Cluster composed of 16 Cerebras CS-2 systems. The software used was PyTorch and the Cerebras Software Platform (CSoft) release 1.8 (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18; Section 5, page 9).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The training data, the Pile dataset, has been analyzed and is known to contain toxic, gender-biased, pejorative, and racially sensitive content. The model may generate outputs that do not align with human values (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

Potential risks include the amplification of social stereotypes, memorization of training data, and the potential to reveal private or secure information. The risk of the model producing harmful or biased content needs to be thoroughly investigated before it is used in any production environment that could directly impact human life (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

Mitigation during pre-training was limited to the standard preprocessing steps applied to the Pile dataset. No further specific mitigations were employed (Cerebras-GPT: Open Compute-Optimal Language Models, Table 7, page 18).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Architectural Limitations:** The model uses a well-established architecture but does not incorporate more recent features like RoPE or ALiBi position embeddings, or SwiGLU activation functions, which might offer performance improvements (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13).
*   **Training Paradigm:** The model was not trained with denoising pre-training objectives or instruction fine-tuning, which are other avenues for improving performance (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13).
*   **Dataset Cleaning:** The model was trained on the standard Pile dataset. Further dataset cleaning and deduplication could improve model performance, as shown by tests on Pythia models (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13).
*   **Evaluation Gaps:** The model has not been extensively tested for factual accuracy, profanity, toxicity, or other socially undesirable text generation (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13).

### Recommendations:
*   Users should conduct thorough safety-related testing, implement mitigations, and apply output curation before deploying this model in any production or user-facing application (Cerebras-GPT: Open Compute-Optimal Language Models, Section 7, page 13).
*   Further bias evaluation is recommended before deployment in production settings (Cerebras-GPT: Open Compute-Optimal Language Models, Section C.4, page 28).

---