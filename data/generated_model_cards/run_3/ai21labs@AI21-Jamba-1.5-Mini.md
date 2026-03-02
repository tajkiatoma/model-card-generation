## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
Insufficient information regarding the model's specific version is available. The model was developed for use with `transformers` library versions `4.40.2` (Source: config.json) and `4.44.2` (Source: generation_config.json).

### Model type:
The model is a `jamba` type, specifically a `JambaForCausalLM` (Causal Language Model) (Source: config.json). It features a hybrid architecture that combines elements of Transformer and Mamba (State Space Model) models, along with a Mixture-of-Experts (MoE) framework.

**Architecture Details:**
The model is structured with 32 hidden layers. These layers are a mix of attention, Mamba, and MoE feed-forward blocks (Source: config.json):
*   **Attention Layers:** Standard attention blocks appear periodically, starting at layer 4 and repeating every 8 layers (`attn_layer_offset: 4`, `attn_layer_period: 8`) (Source: config.json).
*   **Mixture-of-Experts (MoE) Layers:** MoE layers are used for the feed-forward components, starting at layer 1 and repeating every 2 layers (`expert_layer_offset: 1`, `expert_layer_period: 2`). The model contains 16 experts in total, with 2 experts activated per token (`num_experts: 16`, `num_experts_per_tok: 2`) (Source: config.json).
*   **Mamba Layers:** The remaining layers utilize Mamba blocks.

**Key Specifications:**
*   **Model Size:** The total size of the model is approximately 103.14 GB (`total_size: 103140646656`) (Source: model.safetensors.index.json).
*   **Context Length:** The model supports a maximum context length of 262,144 tokens (`max_position_embeddings: 262144`) (Source: config.json).
*   **Hidden Size:** 4096 (`hidden_size: 4096`) (Source: config.json).
*   **Intermediate Size:** 14336 (`intermediate_size: 14336`) (Source: config.json).
*   **Attention Heads:** 32 attention heads and 8 key-value heads (indicating Grouped-Query Attention) (`num_attention_heads: 32`, `num_key_value_heads: 8`) (Source: config.json).
*   **Vocabulary Size:** 65,536 (`vocab_size: 65536`) (Source: config.json).
*   **Precision:** The model uses `bfloat16` precision (`torch_dtype: "bfloat16"`) (Source: config.json).

### Training details:
Insufficient information is available about the training algorithm, optimizer, or learning rate schedule. The following configuration parameters related to training are specified:
*   **Initializer Range:** 0.02 (`initializer_range: 0.02`) (Source: config.json).
*   **RMS Norm Epsilon:** 1e-06 (`rms_norm_eps: 1e-06`) (Source: config.json).
*   **Router Auxiliary Loss Coefficient:** 0.001 (`router_aux_loss_coef: 0.001`), a parameter used in MoE training (Source: config.json).
*   **Hidden Activation Function:** SiLU (`hidden_act: "silu"`) (Source: config.json).

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
The model is designed as a Causal Language Model for conversational AI and instruction-following tasks (Source: config.json, tokenizer_config.json). The detailed chat template and specialized tokens indicate its capabilities for:
*   **Conversational Chat:** Engaging in dialogue with a user, differentiating between system instructions, user prompts, and assistant responses using tokens like `<|system|>`, `<|user|>`, and `<|assistant|>` (Source: special_tokens_map.json, tokenizer_config.json).
*   **Tool Use:** The model is equipped to understand and generate calls to external tools or functions, indicated by tokens such as `<|tool|>`, `<tool_definitions>`, and `<tool_calls>` (Source: special_tokens_map.json, tokenizer_config.json).
*   **Retrieval-Augmented Generation (RAG):** The model can process and cite external documents provided in the prompt, using `<documents>` and `<citations>` tokens (Source: special_tokens_map.json, tokenizer_config.json).

The model's input-output structure is managed by a chat template that formats conversations, tool definitions, and documents into a single prompt for processing (Source: tokenizer_config.json).

### Primary intended users:
Based on its capabilities, the primary intended users are likely developers and researchers building applications such as chatbots, virtual assistants, and systems that require interaction with external APIs or knowledge bases.

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model should be used with its accompanying tokenizer, which formats inputs according to a specific chat template. The template structures the conversation using special tokens to delineate roles and content (Source: tokenizer_config.json, special_tokens_map.json).

**Special Tokens:**
*   `<|startoftext|>`: Beginning of a text sequence (Source: tokenizer_config.json).
*   `<|endoftext|>`: End of a text sequence (Source: tokenizer_config.json).
*   `<|pad|>`: Padding token (Source: special_tokens_map.json).
*   `<|bom|>`: Beginning of a message (Source: tokenizer_config.json).
*   `<|eom|>`: End of a message (Source: tokenizer_config.json).
*   `<|system|>`: Denotes system-level instructions (Source: special_tokens_map.json).
*   `<|user|>`: Denotes a user's message (Source: special_tokens_map.json).
*   `<|assistant|>`: Denotes the model's response (Source: special_tokens_map.json).
*   `<|tool|>`: Denotes a message containing the output of a tool call (Source: special_tokens_map.json).
*   `<tool_definitions>` / `</tool_definitions>`: Encloses definitions of available tools (Source: special_tokens_map.json).
*   `<tool_calls>` / `</tool_calls>`: Encloses tool calls generated by the assistant (Source: special_tokens_map.json).
*   `<documents>` / `</documents>`: Encloses external documents for RAG (Source: special_tokens_map.json).
*   `<citations>` / `</citations>`: Encloses citations for RAG (Source: special_tokens_map.json).

**Example Input Structure (Conceptual):**

A typical conversation prompt should be formatted by the tokenizer's chat template. Conceptually, a multi-turn conversation with tool use would look like this:

```
<|startoftext|><|bom|><|system|> You are a helpful assistant.<|eom|><|bom|><|user|> What's the weather in London?<|eom|><|bom|><|assistant|> <tool_calls>[{"name": "get_weather", "arguments": {"city": "London"}}]</tool_calls><|eom|><|bom|><|tool|> {"temperature": "15°C"}<|eom|><|bom|><|assistant|> The weather in London is 15°C.
```

The `chat_template` provided in `tokenizer_config.json` automates this formatting process when using a compatible library like Hugging Face Transformers. Users should pass a list of message dictionaries, and the template will construct the final prompt string.

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
The model's total size is approximately 103.14 GB (`total_size: 103140646656`) (Source: model.safetensors.index.json). As the model weights are in `bfloat16` format (Source: config.json), loading the model into memory requires at least 104 GB of RAM or VRAM.

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