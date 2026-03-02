## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model was developed using `transformers` version 4.40.2 (Source: `config.json`) and the generation configuration is compatible with `transformers` version 4.44.2 (Source: `generation_config.json`). No specific version number for the model itself is provided.

### Model type:
The model is a `jamba` type model, specifically a `JambaForCausalLM` for causal language modeling (Source: `config.json`). It features a hybrid architecture that combines elements of Transformer, Mamba, and Mixture-of-Experts (MoE).

**Architecture Details:**
The model has 32 hidden layers (`num_hidden_layers`) with a hidden size of 4096 (`hidden_size`) (Source: `config.json`). The architecture alternates between different types of layers:
*   **Attention Layers:** Standard Transformer attention layers are used periodically, starting at layer 4 with a period of 8 (`attn_layer_offset`, `attn_layer_period`). These layers have 32 attention heads (`num_attention_heads`) and 8 key-value heads (`num_key_value_heads`) (Source: `config.json`).
*   **Mamba Layers:** The model incorporates Mamba state space model components, as indicated by parameters like `mamba_d_conv`, `mamba_d_state`, and `mamba_expand` (Source: `config.json`).
*   **Mixture-of-Experts (MoE) Layers:** MoE layers are used for feed-forward computations, starting at layer 1 with a period of 2 (`expert_layer_offset`, `expert_layer_period`). There are 16 experts in total (`num_experts`), and the model routes each token to the top 2 experts (`num_experts_per_tok`) (Source: `config.json`).

**Model Size and Context Length:**
*   **Size:** The total size of the model's weights is 103,140,646,656 bytes (approximately 103.14 GB) (Source: `model.safetensors.index.json`).
*   **Context Length:** The model supports a maximum context length of 262,144 tokens (`max_position_embeddings`) (Source: `config.json`).
*   **Vocabulary Size:** The model's vocabulary contains 65,536 tokens (`vocab_size`) (Source: `config.json`, `tokenizer.json`).

### Training details:
The model was likely trained using the `bfloat16` data type (`torch_dtype`) (Source: `config.json`). Key hyperparameters specified in the configuration include:
*   `hidden_act`: "silu" (Activation function)
*   `initializer_range`: 0.02
*   `rms_norm_eps`: 1e-06 (Epsilon for RMS Normalization)
*   `router_aux_loss_coef`: 0.001 (Auxiliary loss coefficient for the MoE router)
(Source: `config.json`)

Further details about the training algorithm, optimizer, learning rate, or fairness constraints are not available.

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
The model is a causal language model designed for conversational AI and instruction-following tasks. This is evident from the specialized tokens and chat template provided. The model supports multi-turn conversations with distinct roles for "system," "user," and "assistant" (Source: `special_tokens_map.json`, `tokenizer_config.json`).

Its capabilities appear to include:
*   **Conversational Chat:** Engaging in dialogue by processing a sequence of messages from different roles (Source: `tokenizer_config.json`).
*   **Tool Use:** The model is designed to interact with external tools, as indicated by the presence of `<tool_definitions>`, `<tool_calls>`, and `<|tool|>` tokens (Source: `special_tokens_map.json`, `tokenizer.json`).
*   **Retrieval-Augmented Generation (RAG):** The model can process external documents provided in the context, indicated by `<documents>` and `</documents>` tokens, and generate responses with citations, indicated by `<citations>` and `</citations>` tokens (Source: `special_tokens_map.json`, `tokenizer.json`).

The input is expected to be a structured conversation, and the output is a text completion in the "assistant" role.

### Primary intended users:
The primary intended users are likely developers and researchers building applications that require advanced conversational abilities, such as chatbots, virtual assistants, and systems that can leverage external tools and knowledge sources.

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model expects input in a specific conversational format defined by its chat template. Each message in a conversation is enclosed by a Begin-of-Message (`<|bom|>`) token and an End-of-Message (`<|eom|>`) token. The role of the speaker (`system`, `user`, or `assistant`) is indicated by a special token (e.g., `<|user|>`) (Source: `tokenizer_config.json`).

The following is an example of how to structure a conversation according to the model's `chat_template` (Source: `tokenizer_config.json`).

**Chat Structure Example:**

A typical multi-turn conversation would be formatted as a single string like this:
```
<|startoftext|><|bom|><|system|> You are a helpful assistant.<|eom|><|bom|><|user|> What is the capital of France?<|eom|><|bom|><|assistant|> The capital of France is Paris.<|eom|><|bom|><|user|> What is its population?<|eom|><|bom|><|assistant|>
```

**Code Snippet for Formatting Input:**

While a direct code snippet for running the model is not available, here is a conceptual Python example demonstrating how to use the `chat_template` with a tokenizer.

```python
from transformers import AutoTokenizer

# This is a hypothetical example. The actual tokenizer name may differ.
tokenizer = AutoTokenizer.from_pretrained("ai-forever/jamba-v0.1") 

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What is its population?"}
]

# Apply the chat template to format the input
formatted_prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

print(formatted_prompt)
```

**Special Tokens:**
The tokenizer includes several special tokens to handle different functionalities:
*   `<|startoftext|>`: Marks the beginning of a text sequence (Source: `tokenizer_config.json`).
*   `<|endoftext|>`: Marks the end of a text sequence (Source: `tokenizer_config.json`).
*   `<|pad|>`: Padding token (Source: `tokenizer_config.json`).
*   `<|bom|>`: Begin-of-Message token (Source: `tokenizer.json`).
*   `<|eom|>`: End-of-Message token (Source: `tokenizer.json`).
*   `<|system|>`, `<|user|>`, `<|assistant|>`: Role tokens for conversations (Source: `tokenizer.json`).
*   `<|tool|>`, `<tool_definitions>`, `</tool_definitions>`, `<tool_calls>`, `</tool_calls>`: Tokens for tool use functionality (Source: `tokenizer.json`).
*   `<documents>`, `</documents>`, `<citations>`, `</citations>`: Tokens for RAG and citation functionality (Source: `tokenizer.json`).

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
The text data is processed using a Byte-Pair Encoding (BPE) tokenizer (Source: `tokenizer.json`). The preprocessing steps applied by the tokenizer include:
*   **Normalization:** Replaces occurrences of the space character (` `) with a special space character (` `) (Source: `tokenizer.json`).
*   **Tokenization:** Uses a BPE model with a vocabulary of 65,536 tokens (Source: `tokenizer.json`).
*   **Post-processing:** Adds a `<|startoftext|>` token to the beginning of each sequence (Source: `tokenizer.json`).

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
*   **Disk Space:** The model weights require approximately 103.14 GB of disk space (Source: `model.safetensors.index.json`).
*   **VRAM/RAM:** To load the model in `bfloat16` precision, at least 104 GB of VRAM or RAM is required. Additional memory will be needed for inference overhead, activations, and the key-value cache (Source: `config.json`, `model.safetensors.index.json`).

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