## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Cohere. This is indicated by the model's architecture, `CohereForCausalLM` (Source: `config.json`), its tokenizer class, `CohereTokenizer` (Source: `tokenizer_config.json`), and system prompts within the chat templates which state, "You are a powerful conversational AI trained by Cohere" (Source: `tokenizer_config.json`).

### Model date:
Insufficient information

### Model version:
The model was developed using `transformers` version `4.40.0.dev0` (Source: `config.json`, `generation_config.json`). No specific version for the model itself is provided.

### Model type:
The model is a Causal Language Model of type "cohere" with the `CohereForCausalLM` architecture (Source: `config.json`). It is a Transformer-based model designed for text generation.

**Architecture Details:**
*   **Layers:** 64 hidden layers (`num_hidden_layers`) (Source: `config.json`).
*   **Attention Heads:** 96 attention heads (`num_attention_heads`) and 8 key-value heads (`num_key_value_heads`) (Source: `config.json`).
*   **Hidden Size:** 12,288 (`hidden_size`) (Source: `config.json`).
*   **Intermediate Size:** 33,792 (`intermediate_size`) for the feed-forward network (Source: `config.json`).
*   **Activation Function:** SiLU (`silu`) (Source: `config.json`).
*   **Normalization:** Uses Layer Normalization with an epsilon of 1e-05 (`layer_norm_eps`) and applies normalization to query and key projections (`use_qk_norm: true`) (Source: `config.json`).
*   **Positional Embeddings:** Uses Rotary Position Embedding (RoPE) with a theta value of 75,000,000.0 (`rope_theta`) (Source: `config.json`).

**Model Size and Context Length:**
*   **Size:** The total size of the model's weights is approximately 207.6 GB (207,621,349,376 bytes) (Source: `model.safetensors.index.json`).
*   **Context Length:** The model supports a maximum position embeddings of 8,192 tokens (`max_position_embeddings`) and a model max length of 131,072 tokens (`model_max_length`) (Source: `config.json`).
*   **Vocabulary Size:** 256,000 tokens (`vocab_size`) (Source: `config.json`).

**Tokenizer:**
*   The model uses the `CohereTokenizer` class (Source: `tokenizer_config.json`).
*   Special tokens include `<BOS_TOKEN>` (ID: 5), `<|END_OF_TURN_TOKEN|>` (ID: 255001), and `<PAD>` (ID: 0) (Source: `config.json`, `special_tokens_map.json`). A full list of added special tokens for chat and tool use is available in the tokenizer configuration (Source: `tokenizer_config.json`).

### Training details:
The following training-related hyperparameters are specified in the model's configuration:
*   **Attention Dropout:** 0.0 (`attention_dropout`) (Source: `config.json`).
*   **Initializer Range:** 0.02 (`initializer_range`) (Source: `config.json`).
*   **Logit Scale:** 0.8333333333333334 (`logit_scale`) (Source: `config.json`).
*   **Data Type:** The model was trained using `float16` precision (`torch_dtype`) (Source: `config.json`).

No further information is available regarding the training algorithm, optimization techniques, or fairness constraints.

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
Based on the provided chat templates, the model is designed for the following primary uses (Source: `tokenizer_config.json`):

1.  **Conversational AI / Chatbot:** The model can function as a sophisticated AI assistant for engaging in dialogue with users. The default chat template includes a system prompt: "You are Command-R, a brilliant, sophisticated, AI-assistant trained to assist human users by providing thorough responses" (Source: `tokenizer_config.json`).

2.  **Tool Use:** The model is specifically designed to be augmented with external tools. It can interpret a user's request, determine which tools to call, format the necessary parameters, and generate a response based on the tool outputs. The `tool_use` chat template provides a detailed framework for defining tools and their parameters for the model (Source: `tokenizer_config.json`).

3.  **Retrieval-Augmented Generation (RAG):** The model can be used in RAG pipelines where it is provided with a set of retrieved documents to answer user queries. It is capable of identifying relevant documents, citing sources, and generating a "grounded answer" that links facts back to the provided documents using special markup like `<co: doc>` (Source: `tokenizer_config.json`).

The model's input-output structure for chat is a list of messages, each with a specified `role` (e.g., 'user', 'assistant', 'system', 'tool') and `content` (Source: `tokenizer_config.json`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
The model is instructed not to engage in harmful or immoral behavior. The `tool_use` and `rag` chat templates contain a "Safety Preamble" that explicitly states: "Don't answer questions that are harmful or immoral" (Source: `tokenizer_config.json`). This is a stated out-of-scope use case.

---

## How to Use
This section outlines how to use the model.

The model's usage is primarily guided by chat templates that format the input for different tasks. The input should be a list of message dictionaries, each containing `role` and `content` keys. The model supports three distinct chat templates (Source: `tokenizer_config.json`).

### 1. Default Chat Template
This template is for general conversational use.

**Jinja Template:**
```jinja
{{ bos_token }}{% if messages[0]['role'] == 'system' %}{% set loop_messages = messages[1:] %}{% set system_message = messages[0]['content'] %}{% elif false == true %}{% set loop_messages = messages %}{% set system_message = 'You are Command-R, a brilliant, sophisticated, AI-assistant trained to assist human users by providing thorough responses. You are trained by Cohere.' %}{% else %}{% set loop_messages = messages %}{% set system_message = false %}{% endif %}{% if system_message != false %}{{ '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' + system_message + '<|END_OF_TURN_TOKEN|>' }}{% endif %}{% for message in loop_messages %}{% if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}{{ raise_exception('Conversation roles must alternate user/assistant/user/assistant/...') }}{% endif %}{% set content = message['content'] %}{% if message['role'] == 'user' %}{{ '<|START_OF_TURN_TOKEN|><|USER_TOKEN|>' + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% elif message['role'] == 'assistant' %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'  + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>' }}{% endif %}
```

### 2. Tool Use Template
This template is for scenarios where the model needs to interact with external tools. It includes a detailed preamble that defines the available tools and instructs the model on how to format its response to call them.

**Jinja Template Snippet (Preamble):**
```jinja
...
{{-'\n\n## Available Tools\nHere is a list of tools that you have available to you:\n\n'}}
{%- set ns = namespace(new_tools=true) %}
{%- for tool in tools %}
    {%- if tool.parameter_definitions is defined %}
        {%- set ns.new_tools = false %}
    {%- endif %}
{%- endfor %}
{%- if ns.new_tools %}
    {{- new_tool_parser(tools) }}
{%- else %}
    {{- old_tool_parser(tools) }}
{%- endif %}
{{- '<|END_OF_TURN_TOKEN|>'}}
...
```
The full template includes macros (`new_tool_parser`, `old_tool_parser`) to parse tool definitions and format them into a Python-like docstring that the model can understand (Source: `tokenizer_config.json`).

### 3. RAG (Retrieval-Augmented Generation) Template
This template is for answering questions based on a set of provided documents. It instructs the model to first identify relevant documents and then generate a grounded answer with citations.

**Jinja Template Snippet (Instructions):**
```jinja
...
{{ '<results>' }}{% for document in documents %}{{ '\nDocument: ' }}{{ loop.index0 }}\n{% for key, value in document.items() %}{{ key }}: {{value}}\n{% endfor %}{% endfor %}{{ '</results>'}}{{ '<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' }}{{ 'Carefully perform the following instructions, in order, starting each with a new line.\n' }}{{ 'Firstly, Decide which of the retrieved documents are relevant to the user\\'s last input by writing \\'Relevant Documents:\\' followed by comma-separated list of document numbers. If none are relevant, you should instead write \\'None\\'.\n' }}{{ 'Secondly, Decide which of the retrieved documents contain facts that should be cited in a good answer to the user\\'s last input by writing \\'Cited Documents:\\' followed a comma-separated list of document numbers. If you dont want to cite any of them, you should instead write \\'None\\'.\n' }}{% if citation_mode=='accurate' %}{{ 'Thirdly, Write \\'Answer:\\' followed by a response to the user\\'s last input in high quality natural english. Use the retrieved documents to help you. Do not insert any citations or grounding markup.\n' }}{% endif %}{{ 'Finally, Write \\'Grounded answer:\\' followed by a response to the user\\'s last input in high quality natural english. Use the symbols <co: doc> and </co: doc> to indicate when a fact comes from a document in the search result, e.g <co: 0>my fact</co: 0> for a fact from document 0.' }}{{ '<|END_OF_TURN_TOKEN|>' }}
...
```
This template structures the context with documents and then provides a multi-step instruction for the model to follow to generate its final, grounded response (Source: `tokenizer_config.json`).

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
*   **Disk Space:** The model weights require approximately 207.6 GB of disk space (Source: `model.safetensors.index.json`).
*   **RAM/VRAM:** To load the model in `float16` precision, at least 208 GB of RAM or VRAM would be required (inferred from model size and `torch_dtype` in `config.json`).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The primary risk mitigation strategy identified in the repository is a "Safety Preamble" included in the system prompts for the `tool_use` and `rag` chat templates. This preamble instructs the model with the following rule: "Don't answer questions that are harmful or immoral" (Source: `tokenizer_config.json`). This serves as a direct instruction to the model to refuse to generate content that falls into these categories.

No information is provided regarding the use of sensitive data during training, other potential risks, or the groups that might be affected by the model's use.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---