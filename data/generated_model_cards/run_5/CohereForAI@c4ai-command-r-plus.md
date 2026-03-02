## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Cohere, as indicated by the model architecture `CohereForCausalLM` (Source: `config.json`), the model type `cohere` (Source: `config.json`), and the tokenizer class `CohereTokenizer` (Source: `tokenizer_config.json`).

### Model date:
Insufficient information

### Model version:
The model files were generated using version `4.40.0.dev0` of the `transformers` library (Source: `config.json`, `generation_config.json`). No specific version for the model itself is provided.

### Model type:
The model is a `CohereForCausalLM`, which is a Causal Language Model based on a Transformer architecture (Source: `config.json`).

**Architecture Details:**
*   **Model Type:** `cohere` (Source: `config.json`)
*   **Number of Hidden Layers:** 64 (Source: `config.json`)
*   **Hidden Size:** 12288 (Source: `config.json`)
*   **Intermediate Size (Feed-Forward Network):** 33792 (Source: `config.json`)
*   **Number of Attention Heads:** 96 (Source: `config.json`)
*   **Number of Key-Value Heads:** 8 (Source: `config.json`)
*   **Hidden Activation Function:** `silu` (Swish-gated Linear Unit) (Source: `config.json`)
*   **Layer Normalization Epsilon:** 1e-05 (Source: `config.json`)
*   **Vocabulary Size:** 256,000 (Source: `config.json`)
*   **Positional Embeddings:** The model uses Rotary Position Embeddings (RoPE) with a `rope_theta` value of 75,000,000.0 (Source: `config.json`).
*   **Normalization:** The model uses QK Normalization (`use_qk_norm`: true) (Source: `config.json`).

**Model Size and Context Length:**
*   **Total Size:** The model's total size is 207,621,349,376 bytes (approximately 207.6 GB) (Source: `model.safetensors.index.json`).
*   **Maximum Position Embeddings:** 8192 tokens (Source: `config.json`).
*   **Model Max Length:** 131,072 tokens (Source: `config.json`).

### Training details:
The following hyperparameters from the training process are available:
*   **Initializer Range:** 0.02 (Source: `config.json`)
*   **Attention Dropout:** 0.0 (Source: `config.json`)
*   **Logit Scale:** 0.8333333333333334 (Source: `config.json`)
*   **Data Type:** `float16` (Source: `config.json`)

No other details about the training algorithm, optimization techniques, or fairness constraints are provided.

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
Based on the provided chat templates, the model is intended for conversational applications, including general chat, tool use, and Retrieval-Augmented Generation (RAG) (Source: `tokenizer_config.json`).

*   **Conversational AI:** The default chat template structures a conversation with alternating user and chatbot turns, indicating its use as a conversational agent (Source: `tokenizer_config.json`).
*   **Tool Use:** The `tool_use` chat template is designed to integrate external tools. It includes a system preamble that instructs the model on how to use and consume the output of these tools to assist the user. The template provides a structured format for defining tools and their parameters (Source: `tokenizer_config.json`).
*   **Retrieval-Augmented Generation (RAG):** The `rag` chat template is designed for tasks where the model must ground its answers in provided documents. The template includes a format for inputting documents and instructions for the model to identify relevant documents, cite sources, and generate a grounded answer based on the retrieved information (Source: `tokenizer_config.json`).

The model uses special tokens to manage the conversation flow, such as `<|START_OF_TURN_TOKEN|>`, `<|END_OF_TURN_TOKEN|>`, `<|USER_TOKEN|>`, and `<|CHATBOT_TOKEN|>` (Source: `tokenizer_config.json`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
The model's safety preamble in the chat templates states, "Don't answer questions that are harmful or immoral" (Source: `tokenizer_config.json`). This suggests that generating harmful or immoral content is an out-of-scope use.

---

## How to Use
This section outlines how to use the model.

The model is designed to be used with specific chat templates to structure the input for different tasks. The tokenizer configuration includes several special tokens to manage conversations (Source: `tokenizer_config.json`, `special_tokens_map.json`).

**Special Tokens:**
*   **`<BOS_TOKEN>` (ID: 5):** Beginning of sequence token (Source: `config.json`, `special_tokens_map.json`).
*   **`<|END_OF_TURN_TOKEN|>` (ID: 255001):** End of sequence/turn token (Source: `config.json`, `special_tokens_map.json`).
*   **`<PAD>` (ID: 0):** Padding token (Source: `config.json`, `special_tokens_map.json`).
*   **`<|START_OF_TURN_TOKEN|>` (ID: 255000):** Marks the beginning of a turn in a conversation.
*   **`<|USER_TOKEN|>` (ID: 255006):** Denotes a user's turn.
*   **`<|CHATBOT_TOKEN|>` (ID: 255007):** Denotes the model's (chatbot's) turn.
*   **`<|SYSTEM_TOKEN|>` (ID: 255008):** Denotes a system message or instruction.

(Source for all special tokens above: `tokenizer_config.json`, `added_tokens_decoder`).

**Example Usage (based on `default` chat template):**
To have a conversation with the model, the input should be formatted using the special tokens.

**Input Structure:**
```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Hello, how are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
```

The model would then generate its response following the `<|CHATBOT_TOKEN|>`.

**Tool Use and RAG:**
For tool use and RAG, the input must be formatted according to the more complex `tool_use` and `rag` chat templates provided in the `tokenizer_config.json` file. These templates include detailed preambles and structured sections for defining tools or providing documents.

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
*   **Disk Space:** The model's total size is approximately 207.6 GB (Source: `model.safetensors.index.json`).
*   **Memory (RAM/VRAM):** To load the model with its specified `float16` precision, at least 208 GB of RAM or VRAM would be required (Source: `config.json`, `model.safetensors.index.json`).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided repository contains a "Safety Preamble" within its chat templates. This preamble states: "The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral" (Source: `tokenizer_config.json`). This indicates an effort to mitigate the risk of the model generating harmful content.

No other information regarding the use of sensitive data, risk assessments, or other mitigation strategies is available.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---