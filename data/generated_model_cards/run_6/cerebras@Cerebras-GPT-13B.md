## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The Cerebras-GPT models were developed by Cerebras Systems (2304.03208.pdf, p. 1). The authors of the paper are Nolan Dey, Gurpreet Gosal, Zhiming (Charles) Chen, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin Tom, and Joel Hestness (2304.03208.pdf, p. 1).

### Model date:
The model card included in the appendix of the research paper lists the model date as March 2023 (2304.03208.pdf, p. 18). The associated paper was submitted to arXiv on April 6, 2023 (2304.03208.pdf, p. 1).

### Model version:
This model card describes the 13 billion parameter version of Cerebras-GPT. It is part of a family of seven open compute-optimal language models released by Cerebras, with sizes ranging from 111 million to 13 billion parameters (2304.03208.pdf, p. 1, 19). These models were trained following DeepMind's Chinchilla scaling rules for compute efficiency, which distinguishes them from other open-source models like GPT-J, GPT-NeoX, OPT, and Pythia that were not specifically aimed at being compute-efficient (2304.03208.pdf, p. 1, 2).

### Model type:
Cerebras-GPT is an autoregressive, decoder-only transformer language model with an architecture similar to GPT-2 and GPT-3 (2304.03208.pdf, p. 3, 18). Unlike GPT-3, it uses dense attention in all decoder blocks (2304.03208.pdf, p. 3).

The specific architectural details for the 13B model are as follows:
*   **Parameters:** 13 billion (2304.03208.pdf, p. 1)
*   **Model Type:** `gpt2` (config.json.txt)
*   **Number of Layers (`n_layer`):** 40 (config.json.txt; 2304.03208.pdf, p. 3)
*   **Hidden Size (`n_embd`):** 5120 (config.json.txt; 2304.03208.pdf, p. 3)
*   **Number of Attention Heads (`n_head`):** 40 (config.json.txt)
*   **Head Size (`d_head`):** 128 (calculated from `n_embd`/`n_head`) (2304.03208.pdf, p. 3)
*   **Feed-Forward Network Size (`n_inner`):** 20480 (config.json.txt; 2304.03208.pdf, p. 3)
*   **Activation Function:** GELU (`gelu`) (config.json.txt)
*   **Context Length (`n_positions`):** 2048 tokens (config.json.txt; 2304.03208.pdf, p. 3)
*   **Vocabulary Size (`vocab_size`):** 50257 (config.json.txt)
*   **Total Size on Disk:** 51.4 GB (pytorch_model.bin.index.json.txt)

### Training details:
The model was trained using the AdamW optimizer with beta values of (0.9, 0.95), an epsilon of 1e-9, and a weight decay of 0.1. Gradient norm clipping was set to 1.0 (2304.03208.pdf, p. 3). The training used a linear learning rate decay schedule with a maximum learning rate of 1.2E-04, warming up over the first 375 million tokens and decaying to 10% of the maximum rate (2304.03208.pdf, p. 3). The model was trained with bfloat16 precision for stability (2304.03208.pdf, p. 4).

The batch size was initially 720 sequences of 2048 tokens (1.47M tokens) for the first 84 billion tokens, and was then increased to 1080 sequences (2.21M tokens) for the remainder of the training to manage gradient noise (2304.03208.pdf, p. 3). The model was trained on a total of 257.1 billion tokens (2304.03208.pdf, p. 3).

The model uses standard parameterization (SP) for weight initialization. Embedding and hidden layer weights were initialized with a truncated normal distribution (σ = 0.02), and the last layer in each residual network was initialized with σ = 0.02/sqrt(2 * n_layers) (2304.03208.pdf, p. 4).

### Paper or other resource for more information:
The primary resource is the academic paper: "Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster" by Nolan Dey et al. (2304.03208.pdf). The paper details the model family, training process, scaling laws, and comparative performance analyses.

The pre-trained models are available on Hugging Face at: https://huggingface.co/cerebras (2304.03208.pdf, p. 1, 19).

### Citation details:
Insufficient information. The provided paper does not include a BibTeX entry for itself.

### License:
The model is released under the Apache 2.0 license, which permits commercial and non-commercial use (2304.03208.pdf, p. 18, 19).

### Contact:
For feedback on the model, the suggested contacts are Nolan Dey and Joel Hestness at {nolan, joel}@cerebras.net (2304.03208.pdf, p. 1, 18).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use is to further research into large language models. It can be used as a foundation model for various NLP tasks, applications, ethics research, and alignment research (2304.03208.pdf, p. 18).

### Primary intended users:
The primary intended users are researchers working to improve LLMs and practitioners seeking reference implementations, training setups, hyperparameters, or pre-trained models (2304.03208.pdf, p. 18).

### Out-of-scope uses:
The model family should not be used in production downstream applications without further safety-related testing and mitigations. The outputs may not align with human values, and the risks must be thoroughly investigated before deployment in any application that can directly impact human life (2304.03208.pdf, p. 18).

---

## How to Use
This section outlines how to use the model.

The paper states that the pre-trained models are available on Hugging Face, implying they can be used with the standard Hugging Face Transformers library (2304.03208.pdf, p. 1, 19). No specific code snippets are provided in the repository, but a typical usage pattern would be as follows:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("cerebras/Cerebras-GPT-13B")
model = AutoModelForCausalLM.from_pretrained("cerebras/Cerebras-GPT-13B")

# Example input
prompt = "The capital of France is"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
**Sample Input:**
`"The capital of France is"`

**Sample Output:**
(No example outputs are provided in the repository.)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The training data, The Pile, is known to contain content that is toxic, gender-biased, pejorative, and racially sensitive. These biases present in the data can manifest in the model's outputs (2304.03208.pdf, p. 18, 19).

### Evaluation factors:
The model was evaluated for bias using the CrowS-Pairs dataset. The evaluation measured bias across nine categories: Race/Color, Socioeconomic status, Gender, Age, Religion, Disability, Sexual orientation, Nationality, and Physical appearance (2304.03208.pdf, p. 18, 28).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Upstream (Pre-training):** The model's performance is measured using text prediction cross-entropy loss on the Pile test set, reported in nats/token (2304.03208.pdf, p. 5).
*   **Downstream:** Performance is measured by text generation accuracy on a suite of seven common sense reasoning tasks: HellaSwag, PIQA, WinoGrande, Lambada, ARC (easy and challenge versions), and OpenBookQA (2304.03208.pdf, p. 6, 18).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Due to compute budget restrictions, variability analysis was only performed for smaller variants of the Cerebras-GPT models. This involved multiple training runs from different random initializations and data loader seeds to assess variance in task performance (2304.03208.pdf, p. 18). The paper notes that the run-to-run standard deviation in loss when using different initialization and data random seeds is around 0.35% (2304.03208.pdf, p. 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Upstream Evaluation:** The Pile's validation and test set splits were used for pre-training evaluation (2304.03208.pdf, p. 18).
*   **Downstream Evaluation:** A suite of standardized tests was used via the EleutherAI eval-harness (2304.03208.pdf, p. 6). These include:
    *   **Cloze and completion tasks:** LAMBADA, HellaSwag
    *   **Common Sense Reasoning tasks:** PIQA, ARC, OpenBookQA
    *   **Winograd schema type tasks:** WinoGrande (2304.03208.pdf, p. 18)
*   **Bias Evaluation:** The CrowS-Pairs dataset was used to evaluate social biases (2304.03208.pdf, p. 18).

### Motivation:
The evaluation tasks were chosen to closely match related works in the field of large language models and to cover a broad cross-section of task types (2304.03208.pdf, p. 18).

### Preprocessing:
Downstream evaluations were performed using the EleutherAI eval-harness (2304.03208.pdf, p. 6). For fair comparison with models that use different vocabularies, cross-entropy results were corrected to be equivalent to the GPT-2 vocabulary based on the number of tokens in each dataset (2304.03208.pdf, p. 5).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on the Pile dataset, an 800GB open-source dataset of diverse text. It consists of data from 22 different sources, including Common Crawl, PubMed Central, Books3, OpenWebText2, Github, and arXiv (2304.03208.pdf, p. 3, 13).

### Motivation:
The Pile was chosen as it is a large, open-source dataset that has been used to train other prominent open-source language models, allowing for direct comparisons (2304.03208.pdf, p. 1, 5).

### Preprocessing:
The raw text from the Pile was cleaned using the `ftfy` library to normalize text and clean corrupted Unicode. The data was then tokenized using byte-pair encoding (BPE) with the GPT-2 vocabulary of size 50257. As a final step, the entire training dataset was shuffled across all documents to improve model generalization (2304.03208.pdf, p. 3, 18, 19). The tokenized version of the training set contains approximately 371 billion tokens (2304.03208.pdf, p. 19).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model was evaluated for bias using the CrowS-Pairs dataset. The results for the 13B model across nine categories are presented in Table 11 of the research paper. Higher values indicate higher bias (2304.03208.pdf, p. 28).

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
The total size of the model weights is 51.4 GB (pytorch_model.bin.index.json.txt). To load the model in its native precision (bfloat16 or float16), approximately 26 GB of RAM or VRAM would be required.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was pre-trained on the Andromeda AI Supercomputer, which is a cluster of 16 Cerebras CS-2 systems (2304.03208.pdf, p. 9, 18). The 13B model specifically was trained on 12 CS-2 systems (2304.03208.pdf, p. 12). Each CS-2 system contains a Wafer-Scale Engine (WSE-2) processor with 40 GB of on-wafer SRAM (2304.03208.pdf, p. 10). The training was orchestrated using PyTorch and the Cerebras Software Platform (CSoft) release 1.8 (2304.03208.pdf, p. 18).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The training data, The Pile, has been analyzed from various ethical standpoints and is known to contain sensitive data, including content considered toxic, gender-biased, pejorative, and racially sensitive (2304.03208.pdf, p. 18, 19).

Potential risks and harms associated with the model include the manifestation of distributional biases from the training data, such as amplifying social stereotypes. Other risks common to large language models include memorizing training data and potentially revealing private or secure information (2304.03208.pdf, p. 18).

The outputs from this model may not align with human values, and the paper warns that these risks need to be thoroughly investigated before deploying the model in a production environment where it can directly impact human life (2304.03208.pdf, p. 18).

The only mitigation strategies employed during development were the standard preprocessing steps for the Pile dataset. No further specific mitigations were applied during pre-training (2304.03208.pdf, p. 18).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers note several limitations (2304.03208.pdf, p. 13):
*   The model has not been extensively tested for factual accuracy, profanity, toxicity, or other socially undesirable text generation.
*   The model uses a well-established but not state-of-the-art architecture. It does not incorporate recent advances like RoPE or ALiBi for position embeddings, or SwiGLU for activation functions.
*   The model was not trained with instruction fine-tuning or denoising pre-training objectives.
*   The dataset was not deduplicated, which could be a potential area for improvement, as shown by the performance of Pythia models trained on a deduplicated version of the Pile (2304.03208.pdf, p. 7, 13).

### Recommendations:
*   Users should apply further safety-related testing, mitigations, and output curation before using the Cerebras-GPT model family in production or any downstream application that could impact human life (2304.03208.pdf, p. 13, 18).
*   Further bias evaluation and mitigation are recommended before deploying the models in production settings (2304.03208.pdf, p. 28).