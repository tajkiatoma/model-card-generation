## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The Cerebras-GPT models were developed by a team at Cerebras Systems (Source: arXiv:2304.03208v1, p. 1). The authors of the paper are Nolan Dey, Gurpreet Gosal, Zhiming (Charles) Chen, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin Tom, and Joel Hestness (Source: arXiv:2304.03208v1, p. 1).

### Model date:
The model was released in March 2023 (Source: arXiv:2304.03208v1, p. 18, Table 7). The accompanying paper was submitted to arXiv on April 6, 2023 (Source: arXiv:2304.03208v1, p. 1).

### Model version:
This model card describes the 13 billion parameter version of the Cerebras-GPT family (Source: config.json, _name_or_path). The Cerebras-GPT family includes models scaled from 111 million to 13 billion parameters (Source: arXiv:2304.03208v1, p. 1, Abstract). The models are released under the Apache 2.0 license (Source: arXiv:2304.03208v1, p. 13). A separate set of models was also trained using Maximal Update Parameterization (µP) to improve training stability and hyperparameter transfer (Source: arXiv:2304.03208v1, p. 4, Section 2.4). This model is the base variant which uses standard parameterization (SP) (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Model type:
Cerebras-GPT is an autoregressive, decoder-only transformer language model with a GPT-3-like architecture (Source: arXiv:2304.03208v1, p. 3, Section 2.1). It uses dense attention in all decoder blocks (Source: arXiv:2304.03208v1, p. 3, Section 2.1).

The specific details for the 13B model are as follows:
*   **Parameters:** 13 billion (Source: arXiv:2304.03208v1, p. 1, Abstract).
*   **Architecture:** GPT-2 style model (Source: config.json, model_type).
*   **Layers:** 40 (Source: config.json, n_layer).
*   **Attention Heads:** 40 (Source: config.json, n_head).
*   **Hidden Size (d_model):** 5120 (Source: config.json, n_embd).
*   **Filter Size (d_ffn):** 20480 (Source: config.json, n_inner).
*   **Activation Function:** GELU (Source: config.json, activation_function).
*   **Context Length:** 2048 tokens (Source: config.json, n_positions).
*   **Vocabulary Size:** 50,257 (Source: config.json, vocab_size).

### Training details:
The model was pre-trained following DeepMind's Chinchilla scaling rules for compute-efficiency, using approximately 20 tokens per parameter (Source: arXiv:2304.03208v1, p. 4, Section 2.3).

**Algorithm and Parameters:**
*   **Optimizer:** AdamW (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Betas:** (0.9, 0.95) (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Epsilon:** 1e-9 (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Weight Decay:** 0.1 (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Learning Rate:** Maximum of 1.2E-04 with a cosine decay schedule (Source: arXiv:2304.03208v1, p. 3, Table 1). The learning rate was warmed up linearly over 375M tokens and then decayed to 10% of the maximum (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Batch Size:** Started with 1.47M tokens (720 sequences of length 2048) and was later increased to 2.21M tokens (1080 sequences) (Source: arXiv:2304.03208v1, p. 3, Table 1 & Section 2.3).
*   **Total Tokens Trained:** 257.1 billion (Source: arXiv:2304.03208v1, p. 3, Table 1).
*   **Precision:** bfloat16 (Source: arXiv:2304.03208v1, p. 4, Section 2.3).
*   **Dropout:** Not used during pre-training (Source: arXiv:2304.03208v1, p. 3, Section 2.3).
*   **Gradient Clipping:** Gradient norm was clipped at 1.0 (Source: arXiv:2304.03208v1, p. 3, Section 2.3).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Dey, N., et al. (2023). *Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster*. arXiv:2304.03208v1.

The pre-trained models are available on HuggingFace, and the source code is in the Cerebras Modelzoo:
*   **Models:** https://huggingface.co/cerebras (Source: arXiv:2304.03208v1, p. 1, Abstract).
*   **Code:** https://github.com/Cerebras/modelzoo (Source: arXiv:2304.03208v1, p. 13).

### Citation details:
Insufficient information.

### License:
The model is released under the Apache 2.0 license, which permits both commercial and non-commercial use (Source: arXiv:2304.03208v1, p. 13, Cerebras-GPT Open-Source References & p. 18, Table 7).

### Contact:
For feedback on the model, contact Nolan Dey and Joel Hestness at {nolan, joel}@cerebras.net (Source: arXiv:2304.03208v1, p. 1 & p. 18, Table 7).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use is to further research into large language models. It can be used as a foundation model for NLP applications, ethics, and alignment research (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Primary intended users:
The primary intended users are researchers working to improve LLMs and practitioners looking for reference implementations, training setups, hyperparameters, or pre-trained models (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Out-of-scope uses:
The model should not be used in production downstream applications without further safety-related testing and mitigations. The model has not been tested for factual accuracy, toxicity, or other socially undesirable text generation (Source: arXiv:2304.03208v1, p. 13, Section 7 & p. 18, Table 7).

---

## How to Use
This section outlines how to use the model. 

Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model was trained on The Pile dataset, which is known to contain content that is toxic, gender-biased, pejorative, and racially sensitive. The model's performance and outputs may be influenced by these biases (Source: arXiv:2304.03208v1, p. 18, Table 7 & p. 19, Appendix A.1). The factors evaluated for bias include Race/Color, Socioeconomic status, Gender, Age, Religion, Disability, Sexual orientation, Nationality, and Physical appearance (Source: arXiv:2304.03208v1, p. 28, Table 11).

### Evaluation factors:
The model was evaluated for bias across nine factors using the CrowS-Pairs dataset: Race/Color, Socioeconomic status, Gender, Age, Religion, Disability, Sexual orientation, Nationality, and Physical appearance (Source: arXiv:2304.03208v1, p. 18, Table 7 & p. 28, Table 11).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using two main types of metrics:
1.  **Upstream (Pre-training):** Text prediction cross-entropy loss on the Pile test set (Source: arXiv:2304.03208v1, p. 5, Section 3.1).
2.  **Downstream:** Text generation accuracy on a suite of seven common sense reasoning tasks, including HellaSwag, PIQA, WinoGrande, Lambada, ARC, and OpenBookQA (Source: arXiv:2304.03208v1, p. 6, Section 3.2 & p. 18, Table 7).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Due to compute budget restrictions, variability analysis was limited. It was performed only for smaller variants of the Cerebras-GPT models, using multiple runs with different random initializations and data loader seeds to assess variance in task performance (Source: arXiv:2304.03208v1, p. 18, Table 7). The run-to-run standard deviation in loss when using different initialization and data random seeds is noted to be around 0.35% (Source: arXiv:2304.03208v1, p. 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on the following datasets:
*   **Upstream Evaluation:** The Pile validation and test set splits were used (Source: arXiv:2304.03208v1, p. 18, Table 7).
*   **Downstream Evaluation:** A suite of standardized tests was used via the EleutherAI evaluation harness (Source: arXiv:2304.03208v1, p. 6, Section 3.2). This includes:
    *   HellaSwag
    *   PIQA
    *   WinoGrande
    *   Lambada
    *   ARC (easy and challenge versions)
    *   OpenBookQA
*   **Bias Evaluation:** The CrowS-Pairs dataset was used to measure social biases (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Motivation:
The evaluation tasks were selected to closely match related works in the field and to cover a broad cross-section of task types (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Preprocessing:
For fair comparison against other models, the evaluation was run on all checkpoints directly. For models that use different vocabularies, the cross-entropy was corrected to be comparable to the GPT-2 vocabulary based on the number of tokens in each dataset (Source: arXiv:2304.03208v1, p. 3, Section 2.2).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on the Pile dataset, an 800GB open-source dataset of diverse text (Source: arXiv:2304.03208v1, p. 1, Introduction & p. 3, Section 2.2). The Pile is composed of 22 different data sources, including Common Crawl, PubMed Central, Books3, OpenWebText2, Github, and arXiv (Source: arXiv:2304.03208v1, p. 3, Section 2.2). The tokenized version of the training set contains approximately 371 billion tokens (Source: arXiv:2304.03208v1, p. 19, Appendix A.1).

### Motivation:
The Pile was chosen because it is a large, diverse, open-source dataset, which supports the project's goal of creating an open and reproducible scaling study (Source: arXiv:2304.03208v1, p. 1, Introduction & p. 13).

### Preprocessing:
The training data underwent the following preprocessing steps:
1.  The raw text was cleaned using the `ftfy` library to normalize text and clean corrupted Unicode (Source: arXiv:2304.03208v1, p. 19, Appendix A.1).
2.  The data was filtered using scripts provided by EleutherAI (Source: arXiv:2304.03208v1, p. 18, Table 7).
3.  The cleaned text was tokenized using byte-pair encoding (BPE) with the GPT-2 vocabulary of size 50,257 (Source: arXiv:2304.03208v1, p. 3, Section 2.2).
4.  As a final step, the entire training dataset was shuffled across all documents to improve model generalization (Source: arXiv:2304.03208v1, p. 19, Appendix A.1).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was analyzed across several individual factors.
*   **Downstream Task Performance (Zero-shot):** For the 13B model, the accuracy on individual tasks was: HellaSwag (0.513), PIQA (0.766), WinoGrande (0.646), Lambada (0.696), ARC-e (0.714), ARC-c (0.367), and OpenBookQA (0.286) (Source: arXiv:2304.03208v1, p. 7, Table 2).
*   **Bias Analysis:** The 13B model's bias scores on the CrowS-Pairs dataset for individual categories were: Race/Color (55.1), Socioeconomic (72.1), Gender (67.5), Age (73.6), Religion (81.1), Disability (73.8), Sexual orientation (78.5), Nationality (59.7), and Physical appearance (75.0) (Source: arXiv:2304.03208v1, p. 28, Table 11). Higher values correspond to higher bias.

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights on disk is approximately 51.4 GB (Source: pytorch_model.bin.index.json, metadata.total_size). Loading the model in its training `float32` data type would require at least this much RAM (Source: config.json, torch_dtype).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on the Andromeda AI Supercomputer, which is a Cerebras Wafer-Scale Cluster with 16 Cerebras CS-2 systems (Source: arXiv:2304.03208v1, p. 18, Table 7). The 13B parameter model specifically was trained on 12 CS-2 systems (Source: arXiv:2304.03208v1, p. 12, Table 6). The software stack used was PyTorch and Cerebras Software Platform (CSoft) release 1.8 (Source: arXiv:2304.03208v1, p. 18, Table 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Sensitive Data:** The model was trained on The Pile dataset, which is known to contain toxic, gender-biased, pejorative, and racially sensitive content. The paper advises referring to the original Pile dataset references for a thorough analysis (Source: arXiv:2304.03208v1, p. 18, Table 7 & p. 19, Appendix A.1).
*   **Risks and Harms:** The outputs from this model may not align with human values. There is a risk of amplifying social stereotypes, memorizing training data, or revealing private or secure information. The paper explicitly warns that the risks should be thoroughly investigated before deploying the model in a production environment where it can directly impact human life (Source: arXiv:2304.03208v1, p. 18, Table 7).
*   **Mitigation Strategies:** The only mitigations employed were those included in the standard Pile dataset pre-processing, such as text normalization with the `ftfy` library (Source: arXiv:2304.03208v1, p. 18, Table 7 & p. 19, Appendix A.1). No further mitigation strategies were applied during development.
*   **Fraught Use Cases:** Any production downstream application is considered out-of-scope without further safety-related testing, mitigations, and output curation (Source: arXiv:2304.03208v1, p. 13, Section 7 & p. 18, Table 7).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Architectural Limitations:** The model uses a well-established but not state-of-the-art architecture. It does not incorporate recent advances like rotary positional embeddings (RoPE), ALiBi, or SwiGLU activation functions (Source: arXiv:2304.03208v1, p. 13, Section 7).
*   **Training Procedure:** The model was not trained with instruction fine-tuning or denoising pre-training objectives, which could improve performance (Source: arXiv:2304.03208v1, p. 13, Section 7).
*   **Dataset Gaps:** The training data was not deduplicated, which has been shown to improve downstream task accuracy in other models like Pythia (Source: arXiv:2304.03208v1, p. 13, Section 7).
*   **Evaluation Gaps:** The model has not been extensively tested for factual accuracy, profanity, toxicity, or other socially undesirable text generation (Source: arXiv:2304.03208v1, p. 13, Section 7). Variability analysis was only performed on smaller model variants due to compute constraints (Source: arXiv:2304.03208v1, p. 18, Table 7).

### Recommendations:
*   Users should perform thorough safety testing, apply mitigations, and curate outputs before deploying this model in any production application, especially those that can impact human life (Source: arXiv:2304.03208v1, p. 13, Section 7 & p. 18, Table 7).
*   Researchers and practitioners should consider the trade-offs between compute-optimal pre-training and inference costs for their specific use case. Training with more tokens may be beneficial if the model is expected to be used for a very large number of inferences (Source: arXiv:2304.03208v1, p. 9, Section 4).
*   Further bias evaluation and mitigation are recommended before deployment in any user-facing settings (Source: arXiv:2304.03208v1, p. 28, Section C.4).

---