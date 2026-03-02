## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
Insufficient information

### Model type:
The model is a text generation model with a hybrid architecture that incorporates Mamba blocks, standard self-attention blocks, and Mixture-of-Experts (MoE) feed-forward layers (from `model.safetensors.index.json.txt`). The architecture appears to have 32 layers (`model.layers.0` to `model.layers.31`), with different block types at different layers. For example:
*   Layers 0, 10, 14, 16, 18, 22, 24, 26, and 30 contain Mamba blocks (`mamba.A_log`, `mamba.conv1d.weight`, etc.) (from `model.safetensors.index.json.txt`).
*   Layers 4, 12, 20, and 28 contain standard self-attention blocks (`self_attn.q_proj.weight`, `self_attn.k_proj.weight`, etc.) (from `model.safetensors.index.json.txt`).
*   Layers 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, and 31 contain Mixture-of-Experts feed-forward blocks, each with 16 experts (`feed_forward.experts.0` to `feed_forward.experts.15`) and a router (`feed_forward.router.weight`) (from `model.safetensors.index.json.txt`).

**Model Size:** The total size of the model's weights is 103,140,646,656 bytes (approximately 103.14 GB) (from `model.safetensors.index.json.txt`).

**Context Length:** The model's maximum length is configured to 1000000000000000019884624838656 tokens (from `tokenizer_config.json.txt`).

**Tokenizer:**
*   The model uses a Byte-Pair Encoding (BPE) tokenizer with a vocabulary size of 65,536 (from `tokenizer_summary.json.txt`).
*   The tokenizer class is specified as `LlamaTokenizer` (from `tokenizer_config.json.txt`).
*   Special tokens include `<|pad|>` (ID 0), `<|startoftext|>` (ID 1), `<|endoftext|>` (ID 2), and `<|unk|>` (ID 3) (from `tokenizer_summary.json.txt`).
*   Additional special tokens are defined for chat and tool use, such as `<|eom|>`, `<|bom|>`, `<|system|>`, `<|user|>`, `<|assistant|>`, and `<|tool|>` (from `special_tokens_map.json.txt` and `tokenizer_config.json.txt`).

### Training details:
Insufficient information

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
Based on the provided chat template, the model is intended for conversational AI and chat-based applications. It is designed to handle complex interactions that involve system instructions, user queries, and assistant responses (from `tokenizer_config.json.txt`).

The model has built-in capabilities for:
*   **Tool Use:** The chat template includes logic for processing tool definitions and generating tool calls, indicated by special tokens like `<tool_definitions>`, `</tool_definitions>`, `<tool_calls>`, and `</tool_calls>` (from `tokenizer_config.json.txt`).
*   **Retrieval-Augmented Generation (RAG):** The model can process and reference external documents provided in the prompt. The chat template defines a structure for including documents using `<documents>` and `</documents>` tags and for generating citations with `<citations>` and `</citations>` tags (from `tokenizer_config.json.txt`).
*   **Configurable Output Modes:** The template supports "knobs" to control response styles, such as a "fast" citation mode and a "json_object" response format, managed via `<active_output_modes>` and `</active_output_modes>` tags (from `tokenizer_config.json.txt`).

The input-output structure is a formatted string representing a conversation, where each message is enclosed by `<|bom|>` (beginning of message) and `<|eom|>` (end of message) tokens, and prefixed with a role token (e.g., `<|system|>`, `<|user|>`, `<|assistant|>`) (from `tokenizer_config.json.txt`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses a specific chat template to format conversational input. Each turn in the conversation should be structured according to the Jinja2 template provided in `tokenizer_config.json.txt`.

**Key Special Tokens:**
*   `<|startoftext|>`: Prepended to the entire prompt (from `tokenizer_config.json.txt`).
*   `<|bom|>`: Beginning of a message turn (from `tokenizer_config.json.txt`).
*   `<|eom|>`: End of a message turn (from `tokenizer_config.json.txt`).
*   `<|system|>`, `<|user|>`, `<|assistant|>`: Role specifiers for each message (from `tokenizer_config.json.txt`).
*   `<|tool|>`: Role specifier for tool-related messages (from `tokenizer_config.json.txt`).

**Basic Chat Structure:**
A conversation is a sequence of messages. The template starts with `<|startoftext|>`, followed by the formatted messages. Each message begins with `<|bom|>`, a role token (e.g., `<|user|>`), the content, and ends with `<|eom|>`.

*Example of a simple user-assistant conversation:*
```
<|startoftext|><|bom|><|user|> Hello, how are you?<|eom|><|bom|><|assistant|> I am a large language model. I am doing well.<|eom|>
```

**Advanced Usage (Tool Use and RAG):**
The chat template includes macros for handling more complex scenarios like providing system messages, tool definitions, and documents.

1.  **System Message and Tools:** A system message and tool definitions can be provided at the beginning of the conversation.
    ```
    <|startoftext|><|bom|><|system|> You are a helpful assistant.
    
    <tool_definitions>
    # Tools
    
    ## Functions
    
    {
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          }
        },
        "required": ["location"]
      }
    }
    </tool_definitions><|eom|>
    ```

2.  **Including Documents (RAG):** Documents can be provided within a system message before the final user turn.
    ```
    <|bom|><|system|> <documents>
    # Documents
    
    You can use the following documents for reference:
    
    ## Document ID: 0
    Title: Photosynthesis
    Text: Photosynthesis is a process used by plants, algae, and certain bacteria to convert light energy into chemical energy.
    </documents><|eom|>
    ```

3.  **Generating Tool Calls:** When the model needs to use a tool, it is expected to generate a response in the following format:
    ```
    <|bom|><|assistant|> <tool_calls>
    [
      {"name": "get_weather", "arguments": {"location": "Boston, MA"}}
    ]
    </tool_calls><|eom|>
    ```

The full logic for constructing these prompts is detailed in the `chat_template` within `tokenizer_config.json.txt`.

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
The total size of the model weights is 103,140,646,656 bytes (approximately 103.14 GB) (from `model.safetensors.index.json.txt`). Loading the model into memory would require at least this amount of disk space and a comparable amount of RAM or VRAM, depending on the data type used for the weights (e.g., float32, float16).

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