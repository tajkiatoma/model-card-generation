## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The specific version of the model is not specified. The model configuration was created with `transformers` library version 4.40.2 (Source: `config.json.txt`), and the generation configuration was created with version 4.44.2 (Source: `generation_config.json.txt`).

### Model type:
The model is a `jamba` type model with a `JambaForCausalLM` architecture, designed for causal language modeling (i.e., predicting the next token in a sequence) (Source: `config.json.txt`). It features a hybrid architecture that combines elements of both Transformer (attention) and Mamba (State Space Model), along with a Mixture-of-Experts (MoE) approach.

**Architecture Details (Source: `config.json.txt`):**
*   **Hybrid Structure:** The model alternates between attention/MoE blocks and Mamba/MoE blocks. Out of 32 hidden layers, attention layers are used periodically (`attn_layer_period: 8`) with an offset (`attn_layer_offset: 4`), while expert layers are used more frequently (`expert_layer_period: 2`, `expert_layer_offset: 1`).
*   **Hidden Layers:** 32 (`num_hidden_layers`)
*   **Hidden Size:** 4096 (`hidden_size`)
*   **Intermediate Size:** 14336 (`intermediate_size`)
*   **Activation Function:** SiLU (`hidden_act: "silu"`)
*   **Attention Mechanism:**
    *   Attention Heads: 32 (`num_attention_heads`)
    *   Key-Value Heads: 8 (`num_key_value_heads`)
    *   Attention Dropout: 0.0 (`attention_dropout`)
*   **Mixture-of-Experts (MoE):**
    *   Number of Experts: 16 (`num_experts`)
    *   Experts per Token: 2 (`num_experts_per_tok`)
    *   Router Loss Coefficient: 0.001 (`router_aux_loss_coef`)
*   **Mamba Components:**
    *   State Dimension: 16 (`mamba_d_state`)
    *   Convolution Dimension: 4 (`mamba_d_conv`)
    *   Expansion Factor: 2 (`mamba_expand`)
*   **Context Length:** The model supports a maximum context length of 262,144 tokens (`max_position_embeddings`) (Source: `config.json.txt`).
*   **Model Size:** The total size of the model's weights is 103,140,646,656 bytes (approximately 103.14 GB) (Source: `model.safetensors.index.json.txt`).
*   **Tokenizer:** The model uses a Byte-Pair Encoding (BPE) tokenizer (Source: `tokenizer_summary.json.txt`).
    *   **Vocabulary Size:** 65,536 (`vocab_size`) (Source: `config.json.txt`, `tokenizer_summary.json.txt`).

### Training details:
The model was trained using a `bfloat16` data type (`torch_dtype`) (Source: `config.json.txt`). The architecture `JambaForCausalLM` implies a supervised learning approach on a causal language modeling task.

**Key Hyperparameters (Source: `config.json.txt`):**
*   **Initializer Range:** 0.02 (`initializer_range`)
*   **RMS Norm Epsilon:** 1e-06 (`rms_norm_eps`)
*   **Router Auxiliary Loss Coefficient:** 0.001 (`router_aux_loss_coef`)
*   **Use Cache:** Enabled (`use_cache: true`) for faster inference.

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
Based on its architecture and tokenizer configuration, the model is intended for a variety of text generation tasks, with a strong focus on conversational AI and instruction following. The detailed chat template and special tokens indicate its capabilities for:
*   **Conversational Chat:** The model can handle multi-turn conversations with distinct roles for `<|system|>`, `<|user|>`, and `<|assistant|>` (Source: `tokenizer_config.json.txt`).
*   **Tool Use:** The model is designed to integrate with external tools, using special tokens like `<tool_definitions>`, `<tool_calls>`, and `</tool_calls>` to process tool information and generate tool-related responses (Source: `tokenizer_config.json.txt`, `special_tokens_map.json.txt`).
*   **Retrieval-Augmented Generation (RAG):** The model supports the inclusion of external documents for grounded responses, using `<documents>` and `</documents>` tokens to delimit provided context and `<citations>` to reference sources (Source: `tokenizer_config.json.txt`, `special_tokens_map.json.txt`).

The model's input is a formatted string containing the conversation history and any additional context (like tools or documents), and its output is the generated text continuing the conversation, typically from the assistant's perspective.

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model. 

The model's usage is primarily governed by its chat template. A conversation should be formatted using specific roles and control tokens.

**Special Tokens (Source: `special_tokens_map.json.txt`, `tokenizer_config.json.txt`):**
*   `bos_token` (`<|startoftext|>`): Marks the beginning of a text sequence.
*   `eos_token` (`<|endoftext|>`): Marks the end of a text sequence.
*   `<|bom|>`: Marks the beginning of a message.
*   `<|eom|>`: Marks the end of a message.
*   `<|system|>`: Denotes a system-level instruction.
*   `<|user|>`: Denotes a user's message.
*   `<|assistant|>`: Denotes the model's response.

**Chat Template Structure (Source: `tokenizer_config.json.txt`):**
A typical conversation is structured as a sequence of messages, each starting with `<|bom|>` and ending with `<|eom|>`.

A simple user-assistant exchange would be formatted as:
```
<|startoftext|><|bom|><|user|> Hello, how are you?<|eom|><|bom|><|assistant|>
```

A more complex example involving a system prompt:
```
<|startoftext|><|bom|><|system|> You are a helpful assistant.<|eom|><|bom|><|user|> What is the capital of France?<|eom|><|bom|><|assistant|>
```

The template also includes logic for handling tool definitions, tool calls, external documents, and citations, which are inserted into the prompt using their respective special tokens (`<tool_definitions>`, `<documents>`, etc.) (Source: `tokenizer_config.json.txt`).

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
The text data is processed by a BPE tokenizer. The tokenizer's configuration specifies the following preprocessing steps (Source: `tokenizer_summary.json.txt`):
*   **Normalizer:** A sequence normalizer is used, which includes a step to replace the string `" "` with `" "`.
*   **Decoder:** The decoder sequence includes replacing `" "` with `" "`, a byte-level fallback for unknown tokens, and a fuse step.

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
*   **Disk Space:** The model weights require approximately 103.14 GB of disk space (Source: `model.safetensors.index.json.txt`).
*   **VRAM/RAM:** To load the model in its native `bfloat16` precision, at least 104 GB of VRAM or RAM would be required, with additional memory needed for inference overhead (Source: `config.json.txt`, `model.safetensors.index.json.txt`).

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