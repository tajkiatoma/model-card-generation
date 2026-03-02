## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model configuration specifies it was developed with `transformers` version 4.40.2 (Source: `config.json`). The generation configuration specifies `transformers` version 4.44.2 (Source: `generation_config.json`).

### Model type:
The model is a `jamba` type model, with a `JambaForCausalLM` architecture, designed for causal language modeling (text generation) (Source: `config.json`).

**Architecture Details:**
This model features a hybrid architecture that combines elements of traditional Transformers and Mamba (State Space Model). It alternates between attention layers and Mamba layers.

*   **Model Size:** The total size of the model's weights is approximately 96.06 GB (103,140,646,656 bytes) (Source: `model.safetensors.index.json`).
*   **Context Length:** The model supports a maximum context length of 262,144 tokens (Source: `config.json`, `max_position_embeddings`).
*   **Layers:** It has 32 hidden layers (Source: `config.json`, `num_hidden_layers`).
*   **Hidden Size:** The hidden size is 4096 (Source: `config.json`, `hidden_size`).
*   **Intermediate Size:** The intermediate size for feed-forward networks is 14336 (Source: `config.json`, `intermediate_size`).
*   **Vocabulary Size:** The vocabulary size is 65,536 (Source: `config.json`, `vocab_size`).
*   **Attention Mechanism:**
    *   It uses 32 attention heads (Source: `config.json`, `num_attention_heads`).
    *   It uses 8 key-value heads, indicating Grouped-Query Attention (Source: `config.json`, `num_key_value_heads`).
    *   Attention layers are placed periodically, starting at layer 4 with a period of 8 (Source: `config.json`, `attn_layer_offset`, `attn_layer_period`).
*   **Mixture of Experts (MoE):**
    *   The model employs a Mixture of Experts (MoE) mechanism with 16 experts in total (Source: `config.json`, `num_experts`).
    *   For each token, 2 experts are selected (Source: `config.json`, `num_experts_per_tok`).
    *   Expert layers are placed periodically, starting at layer 1 with a period of 2 (Source: `config.json`, `expert_layer_offset`, `expert_layer_period`).
*   **Mamba Components:**
    *   The model is configured to use Mamba kernels (Source: `config.json`, `use_mamba_kernels`).
    *   Mamba-specific parameters include `mamba_d_conv: 4`, `mamba_d_state: 16`, `mamba_dt_rank: 256`, and `mamba_expand: 2` (Source: `config.json`).

### Training details:
The following hyperparameters and settings from the model's configuration provide some insight into its training:
*   **Activation Function:** The hidden activation function is `silu` (Source: `config.json`, `hidden_act`).
*   **Normalization:** RMS Normalization is used with an epsilon of 1e-06 (Source: `config.json`, `rms_norm_eps`).
*   **Initializer Range:** The initializer range for weights is 0.02 (Source: `config.json`, `initializer_range`).
*   **Loss Coefficient:** The auxiliary loss coefficient for the MoE router is 0.001 (Source: `config.json`, `router_aux_loss_coef`).
*   **Precision:** The model is trained and stored in `bfloat16` precision (Source: `config.json`, `torch_dtype`).

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
The model is a causal language model, intended for generating human-like text (Source: `config.json`, `architectures`). Based on its chat template and special tokens, it is specifically designed for conversational and instruction-following tasks.

The input-output structure is chat-based, using special tokens to delineate roles and content (Source: `tokenizer_config.json`, `chat_template`). The model supports:
*   **Conversational Chat:** With roles for `<|system|>`, `<|user|>`, and `<|assistant|>` (Source: `special_tokens_map.json`).
*   **Tool Use:** The model can process tool definitions (`<tool_definitions>`) and generate tool calls (`<tool_calls>`) (Source: `special_tokens_map.json`, `chat_template`).
*   **Retrieval Augmented Generation (RAG):** The model can process external documents provided in the context using `<documents>` tags and is expected to ground its responses in these documents, providing `<citations>` (Source: `special_tokens_map.json`, `chat_template`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model is intended to be used in a conversational format. The structure of the conversation is defined by a chat template (Source: `tokenizer_config.json`, `chat_template`).

**Special Tokens:**
The model uses several special tokens to structure the input:
*   `<|startoftext|>`: Beginning of sequence token (Source: `special_tokens_map.json`).
*   `<|endoftext|>`: End of sequence token (Source: `special_tokens_map.json`).
*   `<|pad|>`: Padding token (Source: `special_tokens_map.json`).
*   `<|unk|>`: Unknown token (Source: `special_tokens_map.json`).
*   `<|bom|>`: Beginning of message token (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<|eom|>`: End of message token (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<|system|>`, `<|user|>`, `<|assistant|>`: Role tokens for chat participants (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<|tool|>`: Token to indicate tool-related content (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<documents>`, `</documents>`: Tokens to wrap provided documents for RAG (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<tool_definitions>`, `</tool_definitions>`: Tokens to wrap tool definitions (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<tool_calls>`, `</tool_calls>`: Tokens to wrap model-generated tool calls (Source: `tokenizer_config.json`, `additional_special_tokens`).
*   `<citations>`, `</citations>`: Tokens to wrap citations of provided documents (Source: `tokenizer_config.json`, `additional_special_tokens`).

**Example Input Structure (Conceptual):**
A typical conversation would be formatted as follows, according to the logic in the `chat_template` (Source: `tokenizer_config.json`):

```
<|startoftext|><|bom|><|system|> You are a helpful assistant.<|eom|><|bom|><|user|> What is the capital of France?<|eom|><|bom|><|assistant|>
```

For more complex interactions involving tools or documents, the template provides logic for inserting sections like `<tool_definitions>` or `<documents>` within the system message context.

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
The training data was processed using a Byte-Pair Encoding (BPE) tokenizer (Source: `tokenizer.json`, `model.type`).

*   **Vocabulary Size:** The tokenizer has a vocabulary of 65,536 tokens (Source: `tokenizer.json`, `model.vocab_size`).
*   **Normalization:** The text is normalized by replacing occurrences of " " with " " (a distinct character) (Source: `tokenizer.json`, `normalizer`).
*   **Decoding:** The decoder sequence includes replacing " " back to a standard space, using a byte-level fallback for unknown tokens, and fusing tokens (Source: `tokenizer.json`, `decoder`).
*   **Post-processing:** The tokenizer adds a beginning-of-sequence token (`<|startoftext|>`) to single sequences (Source: `tokenizer.json`, `post_processor`).

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
*   **Storage:** The model weights require approximately 96.06 GB of disk space (Source: `model.safetensors.index.json`).
*   **Memory (RAM/VRAM):** To load the model in its native `bfloat16` precision, at least 96.06 GB of VRAM or RAM is required, though additional memory will be needed for inference overhead (Source: `config.json`, `torch_dtype`; `model.safetensors.index.json`, `total_size`).

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