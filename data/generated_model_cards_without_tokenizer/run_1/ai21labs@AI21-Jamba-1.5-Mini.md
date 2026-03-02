## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model was developed using `transformers` version 4.40.2 (config.json.txt) and the generation configuration is compatible with `transformers` version 4.44.2 (generation_config.json.txt).

### Model type:
The model is a `JambaForCausalLM`, a causal language model based on the Jamba architecture (config.json.txt). It combines Mamba and Transformer layers, including Mixture-of-Experts (MoE) layers.

**Architecture Details (config.json.txt):**
*   **Model Type:** `jamba`
*   **Layers:** 32 hidden layers (`num_hidden_layers`).
*   **Hidden Size:** 4096 (`hidden_size`).
*   **Intermediate Size (Feed-Forward):** 14336 (`intermediate_size`).
*   **Activation Function:** SiLU (`hidden_act`).
*   **Vocabulary Size:** 65536 (`vocab_size`).
*   **Maximum Context Length:** 262,144 tokens (`max_position_embeddings`).
*   **Normalization:** RMS Normalization with an epsilon of 1e-06 (`rms_norm_eps`).
*   **Word Embeddings:** Word embeddings are not tied (`tie_word_embeddings`).

**Attention Mechanism Details (config.json.txt):**
*   **Attention Layers:** Attention layers appear with a period of 8, starting from layer 4 (`attn_layer_period`, `attn_layer_offset`).
*   **Attention Heads:** 32 (`num_attention_heads`).
*   **Key-Value Heads:** 8 (`num_key_value_heads`).
*   **Attention Dropout:** 0.0 (`attention_dropout`).
*   **Sliding Window:** Not specified (`sliding_window`: null).

**Mixture-of-Experts (MoE) Details (config.json.txt):**
*   **Expert Layers:** MoE layers appear every 2 layers, starting from layer 1 (`expert_layer_period`, `expert_layer_offset`).
*   **Number of Experts:** 16 (`num_experts`).
*   **Experts per Token:** 2 experts are used per token (`num_experts_per_tok`).

**Mamba Layer Details (config.json.txt):**
*   **Convolutional Kernel Size:** 4 (`mamba_d_conv`).
*   **State Dimension:** 16 (`mamba_d_state`).
*   **Expansion Factor:** 2 (`mamba_expand`).
*   **Delta t (dt) Rank:** 256 (`mamba_dt_rank`).
*   **Biases:** Convolutional layers have biases (`mamba_conv_bias`), but projection layers do not (`mamba_proj_bias`).
*   **Kernels:** The model is configured to use Mamba kernels (`use_mamba_kernels`).

**Model Size:**
*   The total size of the model's weights is 103,140,646,656 bytes (approximately 103.14 GB) (model.safetensors.index.json.txt).

### Training details:
The following parameters and configurations were used during the model's development (config.json.txt):
*   **Data Type:** The model was trained using `bfloat16` precision (`torch_dtype`).
*   **Initializer Range:** The model's weights were initialized with a range of 0.02 (`initializer_range`).
*   **Router Auxiliary Loss Coefficient:** A coefficient of 0.001 was used for the router's auxiliary loss (`router_aux_loss_coef`).
*   **Cache:** The model is configured to use a cache for faster generation (`use_cache`).

### Paper or other resource for more information:
Insufficient information

### Citation details:
Insufficient information

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Based on its architecture, `JambaForCausalLM`, the model is intended for causal language modeling (config.json.txt). This typically involves tasks like text generation, completion, and other applications that require predicting the next token in a sequence.

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses the following special token IDs for generation (config.json.txt, generation_config.json.txt):
*   **Beginning of Sequence (BOS) Token ID:** 1
*   **End of Sequence (EOS) Token IDs:** 2, 518
*   **Padding (PAD) Token ID:** 0
*   **Suppressed Tokens:** Token ID 2 is suppressed during generation (generation_config.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information

### Evaluation factors:
Insufficient information

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
Insufficient information

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Insufficient information

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
Insufficient information

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** The model requires approximately 103.14 GB of disk space to store its weights (model.safetensors.index.json.txt).
*   **Memory (RAM/VRAM):** To load the model in `bfloat16` precision, at least 103.14 GB of memory is required, plus additional overhead for the framework and activations (config.json.txt, model.safetensors.index.json.txt).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---