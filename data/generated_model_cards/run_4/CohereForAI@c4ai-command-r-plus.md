## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model was developed using `transformers` version `4.40.0.dev0` (Source: `config.json`, `generation_config.json`).

### Model type:
This is a `cohere` type model, specifically a `CohereForCausalLM` (Causal Language Model) architecture (Source: `config.json`).

**Architecture Details:**
*   **Layers:** 64 hidden layers (Source: `config.json`).
*   **Attention Heads:** 96 attention heads and 8 key-value heads (Source: `config.json`).
*   **Hidden Size:** 12,288 (Source: `config.json`).
*   **Intermediate Size:** 33,792 (Source: `config.json`).
*   **Activation Function:** SiLU (`silu`) (Source: `config.json`).
*   **Vocabulary Size:** 256,000 (Source: `config.json`).
*   **Tokenizer:** `CohereTokenizer` (Source: `tokenizer_config.json`).

**Size and Context Length:**
*   **Total Size:** The model's total size is 207,621,349,376 bytes (approximately 207.6 GB) (Source: `model.safetensors.index.json`).
*   **Context Length:** The model supports a maximum position embeddings of 8,192 tokens and a model max length of 131,072 tokens (Source: `config.json`).

### Training details:
The model was trained with the following parameters and configurations:
*   **Data Type:** `float16` (Source: `config.json`).
*   **Initializer Range:** 0.02 (Source: `config.json`).
*   **Layer Norm Epsilon:** 1e-05 (Source: `config.json`).
*   **Logit Scale:** 0.8333333333333334 (Source: `config.json`).
*   **Attention Dropout:** 0.0 (Source: `config.json`).
*   **RoPE Theta:** 75,000,000.0 (Source: `config.json`).
*   **Normalization:** Query and Key normalization (`use_qk_norm`) is enabled (Source: `config.json`).

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
Based on the provided chat templates, the model is designed for several primary uses (Source: `tokenizer_config.json`):

1.  **Conversational Chat:** The `default` chat template shows the model is intended for conversational interactions, alternating between a user and an assistant. It can handle system prompts to guide its behavior (Source: `tokenizer_config.json`).
2.  **Tool Use:** The `tool_use` chat template indicates the model is capable of using external tools. It is designed to be provided with a list of available tools and their specifications, and it can generate structured JSON output to call these tools with the necessary parameters (Source: `tokenizer_config.json`).
3.  **Retrieval-Augmented Generation (RAG):** The `rag` chat template is designed for scenarios where the model is provided with a set of retrieved documents. The model is instructed to identify relevant documents, cite facts from them, and generate a "Grounded answer" that explicitly links statements to the source documents using special tags (e.g., `<co: 0>my fact</co: 0>`) (Source: `tokenizer_config.json`).

The model's input-output structure is managed through specific chat templates that format the conversation history, system messages, tool definitions, and retrieved documents using special tokens (Source: `tokenizer_config.json`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses a structured format for conversations, which is defined by chat templates. These templates rely on special tokens to delineate different parts of the conversation (Source: `tokenizer_config.json`, `special_tokens_map.json`).

**Special Tokens:**
*   `<BOS_TOKEN>`: Beginning of sequence token (Source: `special_tokens_map.json`).
*   `<|END_OF_TURN_TOKEN|>`: End of a turn for a user, assistant, or system (Source: `special_tokens_map.json`).
*   `<|START_OF_TURN_TOKEN|>`: Start of a turn (Source: `tokenizer_config.json`).
*   `<|SYSTEM_TOKEN|>`: Indicates a system message (Source: `tokenizer_config.json`).
*   `<|USER_TOKEN|>`: Indicates a user message (Source: `tokenizer_config.json`).
*   `<|CHATBOT_TOKEN|>`: Indicates a message from the model/assistant (Source: `tokenizer_config.json`).
*   `<PAD>`: Padding token (Source: `special_tokens_map.json`).

**Example Usage (based on `default` chat template):**
A typical conversation is structured by alternating between user and assistant turns, each enclosed in start and end-of-turn tokens.

A conversation might be formatted like this:
```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Hello, how are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>I am doing well, thank you! How can I help you today?<|END_OF_TURN_TOKEN|>
```
(Source: `tokenizer_config.json`).

**Tool Use Usage (based on `tool_use` chat template):**
For tool use, the prompt must include a system preamble that defines the available tools in a specific format. The model is then expected to generate an action in a JSON format to call the appropriate tool.

Example of a system prompt section for tool definition:
```python
## Available Tools
Here is a list of tools that you have available to you:

```python
def search_tool(query: str) -> List[Dict]:
    """
    Searches for information on a given topic.

    Args:
        query (str): The search query.
    """
    pass
```
```
The model would then respond with an action like:
```json
Action:
```json
[
    {
        "tool_name": "search_tool",
        "parameters": {
            "query": "information about large language models"
        }
    }
]
```
```
(Source: `tokenizer_config.json`).

**RAG Usage (based on `rag` chat template):**
For RAG, the prompt includes retrieved documents formatted with metadata. The model is then instructed to generate a response that cites these documents.

Example of document formatting in the prompt:
```
<results>
Document: 0
title: Large Language Models
content: LLMs are a type of AI...
</results>
```
The model is then expected to produce a grounded answer:
```
Grounded answer: <co: 0>LLMs are a type of AI</co: 0>.
```
(Source: `tokenizer_config.json`).

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
*   **Disk Space:** The model weights have a total size of approximately 207.6 GB (Source: `model.safetensors.index.json`).
*   **Memory (RAM/VRAM):** The model was trained using `float16` precision (Source: `config.json`). Loading the model would require at least 207.6 GB of memory, plus additional overhead for computation.

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The model's `torch_dtype` is `float16`, which suggests it was trained or is intended for use on hardware that supports half-precision floating-point format, such as modern GPUs (Source: `config.json`).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model's `tool_use` and `rag` chat templates include a "Safety Preamble" which contains the instruction: "Don't answer questions that are harmful or immoral." This preamble is designed to override other instructions in the prompt, indicating a built-in risk mitigation strategy to prevent the generation of unsafe content (Source: `tokenizer_config.json`).

No other information regarding ethical considerations, data privacy, or potential biases is available.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---