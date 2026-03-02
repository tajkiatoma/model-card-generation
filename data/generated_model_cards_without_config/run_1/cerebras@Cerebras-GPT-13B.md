## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Nolan Dey, Gurpreet Gosal, Zhiming (Charles) Chen, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin Tom, and Joel Hestness from Cerebras Systems (Source: 2304.03208.pdf, p. 1).

### Model date:
The model was released in March 2023 (Source: 2304.03208.pdf, p. 18, Table 7). The accompanying paper was submitted on April 6, 2023 (Source: 2304.03208.pdf, p. 1).

### Model version:
This is a family of models named Cerebras-GPT, with sizes including 111M, 256M, 590M, 1.3B, 2.7B, 6.7B, and 13B parameters. These models were trained following compute-optimal principles. A separate set of models was also trained using Maximal Update Parameterization (µP) to improve training stability and hyperparameter predictability (Source: 2304.03208.pdf, p. 1, Abstract). The models are released under the Apache 2.0 license, which permits commercial and non-commercial use (Source: 2304.03208.pdf, p. 19).

### Model type:
Cerebras-GPT is a family of autoregressive, decoder-only Transformer language models with a GPT-3-like architecture (Source: 2304.03208.pdf, p. 3, Section 2.1). Unlike GPT-3, Cerebras-GPT uses dense attention in all decoder blocks (Source: 2304.03208.pdf, p. 3, Section 2.1). The models are trained with a maximum sequence length of 2048 tokens (Source: 2304.03208.pdf, p. 3, Table 1).

The model family includes the following sizes (Source: 2304.03208.pdf, p. 3, Table 1):
*   **111M parameters:** 10 layers, hidden size 768
*   **256M parameters:** 14 layers, hidden size 1088
*   **590M parameters:** 18 layers, hidden size 1536
*   **1.3B parameters:** 24 layers, hidden size 2048
*   **2.7B parameters:** 32 layers, hidden size 2560
*   **6.7B parameters:** 32 layers, hidden size 4096
*   **13B parameters:** 40 layers, hidden size 5120

The models use a byte-pair encoding tokenizer with the GPT-2 vocabulary of size 50257 (Source: 2304.03208.pdf, p. 3, Section 2.2; vocab.json.txt). The total size of the 13B parameter model's weights is approximately 51.4 GB (Source: pytorch_model.bin.index.json.txt).

### Training details:
The models were trained on the Cerebras Wafer-Scale Cluster in a compute-efficient manner, following the DeepMind Chinchilla scaling methodology, which suggests training with roughly 20 tokens per parameter (Source: 2304.03208.pdf, p. 4).

Key training parameters include (Source: 2304.03208.pdf, p. 3, Section 2.3):
*   **Optimizer:** AdamW with (beta1, beta2) = (0.9, 0.95).
*   **Precision:** bfloat16 mixed precision for stability (Source: 2304.03208.pdf, p. 4).
*   **Learning Rate:** Varies by model size (e.g., 6.0E-04 for 111M, 1.2E-04 for 13B). A linear learning rate decay was used for most models, warming up over 375M tokens and decaying to 10% of the maximum rate (Source: 2304.03208.pdf, p. 3, Section 2.3, Table 1).
*   **Hyperparameters:** Weight decay of 0.1, gradient norm clipping of 1.0, and no dropout (Source: 2304.03208.pdf, p. 3, Section 2.3).
*   **Batch Size:** Scaled with model size, from 246K tokens for the 111M model up to 2.21M tokens for the 13B model (Source: 2304.03208.pdf, p. 3, Table 1).

A variant of the models was trained using Maximal Update Parameterization (µP) to improve training stability and hyperparameter transfer across scales (Source: 2304.03208.pdf, p. 4, Section 2.4).

### Paper or other resource for more information:
The primary resource is the academic paper "Cerebras-GPT: Open Compute-Optimal Language Models" (Source: 2304.03208.pdf).

Additional resources mentioned in the paper include:
*   **Hugging Face Repository:** `https://huggingface.co/cerebras` for pre-trained models (Source: 2304.03208.pdf, p. 1, Abstract).
*   **Cerebras Modelzoo:** `https://github.com/Cerebras/modelzoo` for source code (Source: 2304.03208.pdf, p. 2).

### Citation details:
Insufficient information. A BibTeX citation is not provided in the repository.

### License:
The models are released under the Apache 2.0 license, which permits both commercial and non-commercial use (Source: 2304.03208.pdf, p. 19).

### Contact:
For feedback on the model, contact Nolan Dey and Joel Hestness at `{nolan, joel}@cerebras.net` (Source: 2304.03208.pdf, p. 18, Table 7).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use is to further research into large language models. The models can serve as a foundation for NLP applications, ethics studies, and alignment research (Source: 2304.03208.pdf, p. 18, Table 7).

### Primary intended users:
The primary users are researchers working to improve LLMs and practitioners seeking reference implementations, training setups, hyperparameters, or pre-trained models (Source: 2304.03208.pdf, p. 18, Table 7).

### Out-of-scope uses:
The models were only trained and evaluated as described in the paper due to budget constraints. Further safety-related testing and mitigations should be applied before using the Cerebras-GPT model family in production downstream applications (Source: 2304.03208.pdf, p. 18, Table 7). The models have not been tested for factual accuracy, profanity, or toxicity (Source: 2304.03208.pdf, p. 13, Section 7).

---

## How to Use
This section outlines how to use the model. 

The pre-trained models are available for download from Hugging Face at `https://huggingface.co/cerebras`, and the source code is available in the Cerebras Modelzoo at `https://github.com/Cerebras/modelzoo` (Source: 2304.03208.pdf, p. 19). The repository does not contain specific code snippets for usage.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The training data, The Pile, is known to contain content that is toxic, gender-biased, pejorative, and racially sensitive. These biases can be propagated by the model (Source: 2304.03208.pdf, p. 18, Table 7; p. 19, Appendix A.1).

### Evaluation factors:
The model was evaluated for various bias factors using the CrowS-Pairs dataset. The categories analyzed include Race/Color, Socioeconomic status, Gender, Age, Religion, Disability, Sexual orientation, Nationality, and Physical appearance (Source: 2304.03208.pdf, p. 28, Table 11).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Pre-training:** Model performance is measured using text prediction cross-entropy (in nats/token) on the Pile test set (Source: 2304.03208.pdf, p. 3, Section 2.2; p. 5, footnote 3).
*   **Downstream Tasks:** Performance is measured by text generation accuracy on a suite of seven common sense reasoning tasks: HellaSwag, PIQA, WinoGrande, Lambada, ARC (easy and challenge), and OpenBookQA (Source: 2304.03208.pdf, p. 6, Section 3.2).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Due to compute budget restrictions, variability analysis was only performed for small variants of the Cerebras-GPT models. This involved multiple runs from different random initializations and data loader seeds to assess variance in task performance (Source: 2304.03208.pdf, p. 18, Table 7).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Upstream (Pre-training) Evaluation:** The Pile validation and test set splits were used (Source: 2304.03208.pdf, p. 18, Table 7).
*   **Downstream Evaluation:** Standardized tests were used, including:
    *   **Cloze and completion tasks:** LAMBADA, HellaSwag.
    *   **Common Sense Reasoning tasks:** PIQA, ARC, OpenBookQA.
    *   **Winograd schema type tasks:** WinoGrande.
    These evaluations were performed using the EleutherAI eval-harness (Source: 2304.03208.pdf, p. 18, Table 7).
*   **Bias Evaluation:** The CrowS-Pairs dataset was used (Source: 2304.03208.pdf, p. 18, Table 7).

### Motivation:
The evaluation tasks were chosen to closely match related works in the field and to cover a broad cross-section of task types (Source: 2304.03208.pdf, p. 18, Table 7).

### Preprocessing:
For fair comparisons with other publicly available models, the researchers ran evaluations on all checkpoints themselves. For models using different vocabularies, the cross-entropy was corrected to be equivalent to the GPT-2 vocabulary based on the number of tokens in each dataset (Source: 2304.03208.pdf, p. 3, Section 2.2).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The models were trained on the Pile dataset, an 800GB open-source dataset composed of 22 diverse text sources, including Common Crawl, PubMed Central, Books3, OpenWebText2, Github, and arXiv (Source: 2304.03208.pdf, p. 3, Section 2.2). The tokenized version of the training set contains approximately 371 billion tokens (Source: 2304.03208.pdf, p. 19, Appendix A.1).

### Motivation:
The Pile was chosen as it is a large, diverse, open-source dataset suitable for the goal of creating open and reproducible compute-optimal language models (Source: 2304.03208.pdf, p. 1, Introduction; p. 3, Section 2.2).

### Preprocessing:
The raw text from the Pile was cleaned using the `ftfy` library to normalize text and clean corrupted Unicode. It was then filtered using scripts provided by EleutherAI. The data was tokenized using byte-pair encoding (BPE) with the GPT-2 vocabulary of size 50257. As a final step, the entire training dataset was shuffled across all documents to improve model generalization (Source: 2304.03208.pdf, p. 3, Section 2.2; p. 18, Table 7; p. 19, Appendix A.1). Deduplication was not performed (Source: 2304.03208.pdf, p. 3, Section 2.2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides an analysis of bias on the CrowS-Pairs dataset, disaggregated by nine categories. For the 13B model, the bias scores were (Source: 2304.03208.pdf, p. 28, Table 11):
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

(Higher values correspond to higher bias.)

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
The models were trained on the Andromeda AI Supercomputer, which is a Cerebras Wafer-Scale Cluster composed of 16 Cerebras CS-2 systems. Each CS-2 system contains a Wafer-Scale Engine (WSE-2) processor with 40 GB of high-bandwidth SRAM. The total cluster has a peak throughput of 120 PFLOP/s (Source: 2304.03208.pdf, p. 10, Section 5.1). The training software used was PyTorch and Cerebras Software Platform (CSoft) release 1.8 (Source: 2304.03208.pdf, p. 18, Table 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Data:** The model was trained on The Pile dataset, which has been analyzed from various ethical standpoints and is known to contain toxic, gender-biased, pejorative, and racially sensitive content (Source: 2304.03208.pdf, p. 18, Table 7; p. 19, Appendix A.1).
*   **Human Life:** The model's outputs may not align with human values. The paper states that the risk needs to be thoroughly investigated before deploying the model in a production environment where it can directly impact human life (Source: 2304.03208.pdf, p. 18, Table 7).
*   **Risks and Harms:** There is a risk of distributional bias from the training data manifesting in the model's outputs. Other known risks associated with large language models include amplifying social stereotypes, memorizing training data, or revealing private or secure information (Source: 2304.03208.pdf, p. 18, Table 7).
*   **Mitigations:** The only mitigations employed during pre-training were those included in the standard Pile dataset preprocessing, which involved cleaning the raw text with the `ftfy` library (Source: 2304.03208.pdf, p. 18, Table 7; p. 19, Appendix A.1).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper explicitly states the following limitations (Source: 2304.03208.pdf, p. 13, Section 7):
*   The models use well-established architectures and do not explore recent architectural features like RoPE, ALiBi, or SwiGLU.
*   The models were not subjected to instruction fine-tuning.
*   The models have not been extensively tested for factual accuracy, profanity, toxicity, or other socially undesirable text generation.
*   Due to compute and financial budgets, training and evaluation were limited to the approaches described in the paper (Source: 2304.03208.pdf, p. 18, Table 7).

### Recommendations:
*   Users should apply further safety-related testing, mitigations, and output curation before using the Cerebras-GPT model family in production or downstream applications (Source: 2304.03208.pdf, p. 13, Section 7; p. 18, Table 7).
*   The paper recommends that the research community consider the aggregate compute budget (both pre-training and expected inference costs) when deciding on the balance of model size and pre-training dataset size for future models (Source: 2304.03208.pdf, p. 2).