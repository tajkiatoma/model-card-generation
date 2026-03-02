## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was trained by Cohere (from tokenizer_config.json.txt). The tokenizer class is specified as "CohereTokenizer" (from tokenizer_config.json.txt), and a default system prompt identifies the model as "Command-R, a brilliant, sophisticated, AI-assistant trained to assist human users by providing thorough responses. You are trained by Cohere" (from tokenizer_config.json.txt).

### Model date:
Insufficient information

### Model version:
Insufficient information

### Model type:
The model is a large-scale, Transformer-based text generation model (from model.safetensors.index.json.txt).

*   **Architecture**: The model architecture consists of 64 transformer layers (layers 0 through 63), as indicated by the weight map. Each layer contains standard components like self-attention (`self_attn`), a multi-layer perceptron (`mlp`), and layer normalization (`input_layernorm`) (from model.safetensors.index.json.txt).
*   **Category**: It is a conversational AI model designed for chat, tool use, and Retrieval-Augmented Generation (RAG) (from tokenizer_config.json.txt).
*   **Size**: The total size of the model's weights on disk is 207,621,349,376 bytes (approximately 207.6 GB) (from model.safetensors.index.json.txt).
*   **Context Length**: The `model_max_length` is set to 1000000000000000019884624838656 in the configuration file (from tokenizer_config.json.txt).

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
The model is designed as a conversational AI assistant with multiple advanced capabilities, as defined by its chat templates (from tokenizer_config.json.txt).

*   **Conversational Chat**: The model can be used as a general-purpose chatbot to provide thorough responses to user queries. The default system prompt describes it as an "AI-assistant trained to assist human users" (from tokenizer_config.json.txt).
*   **Tool Use**: The model is designed to be augmented with a range of tools. It can understand tool definitions, decide which tools to call based on user input, and format the necessary function calls in JSON. The system prompt for this mode states, "You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user" (from tokenizer_config.json.txt).
*   **Retrieval-Augmented Generation (RAG)**: The model can process a set of retrieved documents to answer user questions. It is instructed to identify relevant documents, cite facts from them, and generate a "Grounded answer" that indicates which facts come from which documents using special markup (e.g., `<co: 0>my fact</co: 0>`) (from tokenizer_config.json.txt).

The input-output structure is based on a sequence of turns, marked by special tokens like `<|START_OF_TURN_TOKEN|>`, `<|USER_TOKEN|>`, and `<|CHATBOT_TOKEN|>` (from tokenizer_config.json.txt).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
The model is explicitly instructed not to answer questions that are "harmful or immoral." This is specified in a "Safety Preamble" within its `tool_use` and `rag` chat templates (from tokenizer_config.json.txt).

---

## How to Use
This section outlines how to use the model.

The model uses a specific set of special tokens and chat templates to structure conversations (from tokenizer_config.json.txt, special_tokens_map.json.txt).

**Special Tokens:**
*   `bos_token`: `<BOS_TOKEN>` (from special_tokens_map.json.txt)
*   `eos_token`: `<|END_OF_TURN_TOKEN|>` (from special_tokens_map.json.txt)
*   `pad_token`: `<PAD>` (from special_tokens_map.json.txt)
*   Turn separators: `<|START_OF_TURN_TOKEN|>`, `<|END_OF_TURN_TOKEN|>` (from tokenizer_config.json.txt)
*   Role tokens: `<|USER_TOKEN|>`, `<|CHATBOT_TOKEN|>`, `<|SYSTEM_TOKEN|>` (from tokenizer_config.json.txt)

**Chat Templates:**
The model has three distinct chat templates for different use cases (from tokenizer_config.json.txt).

1.  **Default Chat (`default`)**: For standard conversational interactions.
    *   **Structure**: The conversation starts with the `bos_token`, followed by an optional system message. Each turn is enclosed in `<|START_OF_TURN_TOKEN|>` and `<|END_OF_TURN_TOKEN|>`, with the role specified by `<|USER_TOKEN|>` or `<|CHATBOT_TOKEN|>`.
    *   **Example Input Structure**:
        ```
        <BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>Hello, who are you?<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
        ```

2.  **Tool Use (`tool_use`)**: For integrating external tools.
    *   **Structure**: This template includes a detailed system preamble that defines the task, style guide, safety rules, and available tools in a specific format. The model is expected to generate a JSON object containing a list of tool calls.
    *   **Example Input Structure**: A conversation history is provided, followed by a system prompt instructing the model to write "Action:" followed by a JSON list of tool calls.
        ```
        <BOS_TOKEN>...[Preamble with tool definitions]...<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|USER_TOKEN|>What's the weather in Toronto?<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Write 'Action:' followed by a json-formatted list of actions...<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
        ```
    *   **Example Model Output (before execution)**:
        ```json
        Action:
        ```json
        [
            {
                "tool_name": "weather_api",
                "parameters": {
                    "city": "Toronto"
                }
            }
        ]
        ```

3.  **Retrieval-Augmented Generation (`rag`)**: For answering questions based on provided documents.
    *   **Structure**: The template includes a system preamble, the conversation history, and a list of retrieved documents formatted within `<results>` tags. The model is then given a multi-part instruction to identify relevant documents, identify documents to be cited, and write both a clean answer and a "Grounded answer" with inline citations.
    *   **Example Input Structure**:
        ```
        <BOS_TOKEN>...[Preamble]...<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|USER_TOKEN|>What is the capital of Canada?<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|><results>
        Document: 0
        title: Canada
        text: The capital of Canada is Ottawa.
        </results><|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Carefully perform the following instructions...<|END_OF_TURN_TOKEN|>
        <|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
        ```
    *   **Example Model Output**:
        ```
        Relevant Documents: 0
        Cited Documents: 0
        Answer: The capital of Canada is Ottawa.
        Grounded answer: The capital of Canada is <co: 0>Ottawa</co: 0>.
        ```

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
The model requires a minimum of **207.6 GB** of disk space to store the model weights (from model.safetensors.index.json.txt). Loading the model into memory would require at least this amount of RAM or VRAM, depending on the precision used (e.g., approximately 208 GB for float16 precision).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model's configuration includes a "Safety Preamble" that provides ethical guardrails. It states: "The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral" (from tokenizer_config.json.txt). This indicates an effort to mitigate the risk of the model generating harmful content. No further information is available regarding the use of sensitive data, risk mitigation strategies, or potential biases.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The provided repository files lack information regarding the model's training data, evaluation procedures, and performance metrics. This absence makes it difficult to assess the model's potential biases, limitations, and overall reliability across different domains and demographic groups.

### Recommendations:
Users should adhere to the safety guidelines embedded in the model's configuration, specifically the instruction to "not answer questions that are harmful or immoral" (from tokenizer_config.json.txt). Given the lack of evaluation data, users should be cautious when deploying the model in sensitive or high-stakes applications and should conduct their own testing to ensure it meets their specific needs and safety requirements.