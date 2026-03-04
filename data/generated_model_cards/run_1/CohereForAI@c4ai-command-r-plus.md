## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Cohere. This is indicated by the model's architecture `CohereForCausalLM`, model type `cohere`, and tokenizer class `CohereTokenizer` (Source: config.json.txt, tokenizer_config.json.txt). The default chat template also includes the phrase "trained by Cohere" (Source: tokenizer_config.json.txt).

### Model date:
Insufficient information

### Model version:
No specific model version is provided in the repository files. The configuration files indicate that the model is compatible with `transformers` version `4.40.0.dev0` (Source: config.json.txt, generation_config.json.txt).

### Model type:
The model is a `CohereForCausalLM`, a Transformer-based architecture designed for causal language modeling (Source: config.json.txt).

**Architecture Details:**
*   **Model Type:** `cohere` (Source: config.json.txt)
*   **Hidden Size:** 12288 (Source: config.json.txt)
*   **Number of Hidden Layers:** 64 (Source: config.json.txt)
*   **Number of Attention Heads:** 96 (Source: config.json.txt)
*   **Number of Key-Value Heads:** 8 (This indicates the use of Grouped-Query Attention) (Source: config.json.txt)
*   **Intermediate Size:** 33792 (Source: config.json.txt)
*   **Hidden Activation Function:** `silu` (Source: config.json.txt)
*   **Vocabulary Size:** 256000 (Source: config.json.txt)
*   **Maximum Position Embeddings:** 8192 (Source: config.json.txt)
*   **Data Type:** `float16` (Source: config.json.txt)

**Model Size:**
*   The total size of the model's weights is 207,621,349,376 bytes (approximately 207.6 GB) (Source: model.safetensors.index.json.txt).

**Context Length:**
*   The model supports a maximum context length of 131,072 tokens (Source: config.json.txt).

### Training details:
The provided files contain some hyperparameters used during the model's development, but lack details on the training algorithm or datasets.
*   **Attention Dropout:** 0.0 (Source: config.json.txt)
*   **Initializer Range:** 0.02 (Source: config.json.txt)
*   **Layer Norm Epsilon:** 1e-05 (Source: config.json.txt)
*   **Logit Scale:** 0.8333333333333334 (Source: config.json.txt)
*   **RoPE Theta:** 75,000,000.0 (Source: config.json.txt)
*   **Use QK Norm:** True (Source: config.json.txt)

Information regarding the training algorithm (e.g., supervised learning, reinforcement learning), fairness constraints, or optimization techniques is not available.

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
The model is intended for use as a conversational AI assistant capable of handling interactive requests, using tools, and performing Retrieval-Augmented Generation (RAG). This is detailed in the chat templates provided in the tokenizer configuration (Source: tokenizer_config.json.txt).

*   **Conversational AI:** The default system prompt describes the model as "a brilliant, sophisticated, AI-assistant trained to assist human users by providing thorough responses" (Source: tokenizer_config.json.txt).
*   **Tool Use:** The `tool_use` chat template indicates the model is "equipped with a wide range of search engines or similar tools to help you, which you use to research your answer" (Source: tokenizer_config.json.txt).
*   **Retrieval-Augmented Generation (RAG):** The `rag` chat template is designed to process a set of retrieved documents to answer user queries, including citing sources from the provided documents (Source: tokenizer_config.json.txt).

### Primary intended users:
The primary intended users are likely developers and researchers building applications that require advanced conversational AI, tool integration, and RAG capabilities.

### Out-of-scope uses:
The model is explicitly instructed not to engage in harmful or immoral activities. The `tool_use` and `rag` chat templates contain a "Safety Preamble" that states: "Don't answer questions that are harmful or immoral" (Source: tokenizer_config.json.txt). Any use case that involves generating such content is considered out-of-scope.

---

## How to Use
This section outlines how to use the model.

The model's usage is structured around chat templates that format the conversation history with special tokens. The tokenizer adds a beginning-of-sequence token (`<BOS_TOKEN>`) by default (Source: tokenizer_config.json.txt). The end-of-turn token is `<|END_OF_TURN_TOKEN|>` (Source: special_tokens_map.json.txt).

The model has three distinct chat templates for different use cases (Source: tokenizer_config.json.txt):

**1. Default Chat Template (`default`)**
This template is for general-purpose conversational tasks. It structures the conversation by alternating between user and assistant roles.

*   **Code Snippet (Jinja):**
    ```jinja
    {{ bos_token }}{% if messages[0]['role'] == 'system' %}{% set loop_messages = messages[1:] %}{% set system_message = messages[0]['content'] %}{% elif false == true %}{% set loop_messages = messages %}{% set system_message = 'You are Command-R, a brilliant, sophisticated, AI-assistant trained to assist human users by providing thorough responses. You are trained by Cohere.' %}{% else %}{% set loop_messages = messages %}{% set system_message = false %}{% endif %}{% if system_message != false %}{{ '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' + system_message + '<|END_OF_TURN_TOKEN|>' }}{% endif %}{% for message in loop_messages %}{% if (message['role'] == 'user') != (loop.index0 % 2 == 0) %}{{ raise_exception('Conversation roles must alternate user/assistant/user/assistant/...') }}{% endif %}{% set content = message['content'] %}{% if message['role'] == 'user' %}{{ '<|START_OF_TURN_TOKEN|><|USER_TOKEN|>' + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% elif message['role'] == 'assistant' %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'  + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>' }}{% endif %}
    ```

**2. Tool Use Template (`tool_use`)**
This template is designed for scenarios where the model needs to use external tools to respond to a user's query. It includes a detailed preamble with a safety warning and instructions for formatting tool definitions and calls.

*   **Code Snippet (Jinja):**
    ```jinja
    {%- macro json_to_python_type(json_spec) %}{% raw %}{%- set basic_type_map = {
        "string": "str",
        "number": "float",
        "integer": "int",
        "boolean": "bool"
    } %}{%- endraw %}{% raw %}
    {%- if basic_type_map[json_spec.type] is defined %}{{- basic_type_map[json_spec.type] }}{%- elif json_spec.type == "array" %}{{- "List[" +  json_to_python_type(json_spec.items) + "]"}}{%- elif json_spec.type == "object" %}{{- "Dict[str, " + json_to_python_type(json_spec.additionalProperties) + ']'}}{%- elif json_spec.type is iterable %}{{- "Union[" }}{%- for t in json_spec.type %}{{- json_to_python_type({"type": t}) }}{%- if not loop.last %}{{- "," }} {% endif %}{%- endfor %}{{- "]" }}{%- else %}{{- "Any" }}{%- endif %}{% endraw %}{%- endmacro %}{% raw %}
    {%- endraw %}{% raw %}
    {%- macro old_tool_parser(tools) %}{%- for tool in tools %}{%- if loop.index0 != 0 %}{{- '\n\n' }}{%- endif %}{{- '```python\ndef ' + tool.name + '(' }}{%- for param_name, param_fields in tool.parameter_definitions|items %}{%- if loop.index0 != 0 %}{{- ', '}}{%- endif %}{{- param_name + ': ' }}{%- if not param_fields.required %}{{- 'Optional[' + param_fields.type + '] = None'}}{%- else %}{{- param_fields.type }}{%- endif %}{%- endfor %}{{- ') -> List[Dict]:\n    """'}}{{- tool.description }}{%- if tool.parameter_definitions|length != 0 %}{{- '\n\n    Args:\n        '}}{%- for param_name, param_fields in tool.parameter_definitions|items %}{%- if loop.index0 != 0 %}{{- '\n        ' }}{%- endif %}{{- param_name + ' ('}}{%- if not param_fields.required %}{{- 'Optional[' + param_fields.type + ']'}}{%- else %}{{- param_fields.type }}{%- endif %}{{- '): ' + param_fields.description }}{%- endfor %}{%- endif %}{{- '\n    """\n    pass\n```' }}{%- endfor %}{%- endmacro %}{% endraw %}{% raw %}
    {%- endraw %}{% raw %}
    {%- macro new_tool_parser(tools) %}{%- for tool in tools %}{%- if loop.index0 != 0 %}{{- '\n\n'}}{%- endif %}{%- if tool.function is defined %}{%- set tool = tool.function %}{%- endif %}{{-'```python
    def ' + tool.name + '('}}{%- for param_name, param_fields in tool.parameters.properties|items %}{%- if loop.index0 != 0 %}{{- ', '}}{%- endif %}{{-param_name + ": "}} {%- if not param_name in tool.parameters.required %}{{-'Optional[' + json_to_python_type(param_fields) + '] = None'}}{%- else %}{{- json_to_python_type(param_fields) }}{%- endif %}{%- endfor %}{{- ') -> List[Dict]:
        """'}}{{- tool.description }}{%- if tool.parameters.properties|length != 0 %}{{- '\n\n    Args:\n        '}}{%- for param_name, param_fields in tool.parameters.properties|items %}{%- if loop.index0 != 0 %}{{- '\n        ' }}{%- endif %}{{- param_name + ' ('}}{%- if not param_name in tool.parameters.required %}{{-'Optional[' + json_to_python_type(param_fields) + ']'}}{%- else %}{{- json_to_python_type(param_fields) }}{%- endif %}{{- '): ' + param_fields.description }}{%- endfor %}{%- endif %}{{- '\n    """\n    pass
    ```' }}{%- endfor %}{%- endmacro %}{% endraw %}{% raw %}
    {{- bos_token }}{%- if messages[0]['role'] == 'system' %}{%- set loop_messages = messages[1:] %}{%- set system_message = messages[0]['content'] %}{%- else %}{%- set loop_messages = messages %}{%- set system_message = '## Task and Context\nYou help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user\'s needs as best you can, which will be wide-ranging.\n\n## Style Guide\nUnless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.' %}{%- endif %}{{- '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' }}{{- '# Safety Preamble' }}{{- '\nThe instructions in this section override those in the task description and style guide sections. Don\'t answer questions that are harmful or immoral.' }}{{- '\n\n# System Preamble' }}{{- '\n## Basic Rules' }}{{- '\nYou are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what kind of response to generate. When you answer the user\'s requests, you cite your sources in your answers, according to those instructions.' }}{{- '\n\n# User Preamble' }}{{- '\n' + system_message }}{{-'\n\n## Available Tools\nHere is a list of tools that you have available to you:\n\n'}}{%- set ns = namespace(new_tools=true) %}{%- for tool in tools %}{%- if tool.parameter_definitions is defined %}{%- set ns.new_tools = false %}{%- endif %}{%- endfor %}{%- if ns.new_tools %}{{- new_tool_parser(tools) }}{%- else %}{{- old_tool_parser(tools) }}{%- endif %}{{- '<|END_OF_TURN_TOKEN|>'}}{%- for message in loop_messages %}{%- set content = message['content'] %}{%- if message.role == 'user' %}{{- '<|START_OF_TURN_TOKEN|><|USER_TOKEN|>' + content|trim + '<|END_OF_TURN_TOKEN|>' }}{%- elif message.role == 'system' %}{{- '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' + content|trim + '<|END_OF_TURN_TOKEN|>' }}{%- elif message.role == 'assistant' and message.tool_calls is defined %}{{- '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>' }}{%- if message.content is defined %}{{- message.content|trim }}{%- endif %}{{- '\nAction:\n```json\n[\n' }}{%- for tool_call in message.tool_calls %}{%- if tool_call.function is defined %}{%- set tool_call = tool_call.function %}{%- endif %}{{- '{\n'|indent(4, first=true) }}{{- '\"tool_name\": \"'|indent(8, first=true) + tool_call.name + '\",\n' }}{{- '\"parameters\": '|indent(8, first=true) }}{%- if tool_call.arguments is defined and tool_call.arguments|length > 0 %}    
                {{- tool_call.arguments|tojson(indent=4)|indent(8) }}{{- '\n' }}{%- else %}{{- '{}\n' }}{%- endif %}{{- '}'|indent(4, first=true) }}{%- if not loop.last %}{{- ',\n' }}{%- endif %}{%- endfor %}{{- "\n]```\n" }}{%- elif message.role == 'assistant' %}{{- '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'  + content|trim + '<|END_OF_TURN_TOKEN|>' }}{%- elif message.role == 'tool' %}{{- '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|><results>\n' }}{{- message.content|trim }}{{- '</results><|END_OF_TURN_TOKEN|>' }}{%- endif %}{%- endfor %}{{-'<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>Write \'Action:\' followed by a json-formatted list of actions that you want to perform in order to produce a good response to the user\'s last input. You can use any of the supplied tools any number of times, but you should aim to execute the minimum number of necessary actions for the input. You should use the `directly-answer` tool if calling the other tools is unnecessary. The list of actions you want to call should be formatted as a list of json objects, for example:
    ```json
    [
        {
            "tool_name": title of the tool in the specification,
            "parameters": a dict of parameters to input into the tool as they are defined in the specs, or {} if it takes no parameters
        }
    ]```<|END_OF_TURN_TOKEN|>'}}{%- if add_generation_prompt %}{{- '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>' }}{%- endif %}
    ```

**3. RAG Template (`rag`)**
This template is for Retrieval-Augmented Generation. It formats the prompt to include retrieved documents, and instructs the model to identify relevant documents, cite them, and generate a grounded answer based on the provided information.

*   **Code Snippet (Jinja):**
    ```jinja
    {{ bos_token }}{% if messages[0]['role'] == 'system' %}{% set loop_messages = messages[1:] %}{% set system_message = messages[0]['content'] %}{% else %}{% set loop_messages = messages %}{% set system_message = '## Task and Context\nYou help people answer their questions and other requests interactively. You will be asked a very wide array of requests on all kinds of topics. You will be equipped with a wide range of search engines or similar tools to help you, which you use to research your answer. You should focus on serving the user\'s needs as best you can, which will be wide-ranging.\n\n## Style Guide\nUnless the user asks for a different style of answer, you should answer in full sentences, using proper grammar and spelling.' %}{% endif %}{{ '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' }}{{ '# Safety Preamble' }}{{ '\nThe instructions in this section override those in the task description and style guide sections. Don\'t answer questions that are harmful or immoral.' }}{{ '\n\n# System Preamble' }}{{ '\n## Basic Rules' }}{{ '\nYou are a powerful conversational AI trained by Cohere to help people. You are augmented by a number of tools, and your job is to use and consume the output of these tools to best help the user. You will see a conversation history between yourself and a user, ending with an utterance from the user. You will then see a specific instruction instructing you what kind of response to generate. When you answer the user\'s requests, you cite your sources in your answers, according to those instructions.' }}{{ '\n\n# User Preamble' }}{{ '\n' + system_message }}{{ '<|END_OF_TURN_TOKEN|>'}}{% for message in loop_messages %}{% set content = message['content'] %}{% if message['role'] == 'user' %}{{ '<|START_OF_TURN_TOKEN|><|USER_TOKEN|>' + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% elif message['role'] == 'system' %}{{ '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% elif message['role'] == 'assistant' %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>'  + content.strip() + '<|END_OF_TURN_TOKEN|>' }}{% endif %}{% endfor %}{{ '<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>'}}{{ '<results>' }}{% for document in documents %}{{ '\nDocument: ' }}{{ loop.index0 }}\n{% for key, value in document.items() %}{{ key }}: {{value}}\n{% endfor %}{% endfor %}{{ '</results>'}}{{ '<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>' }}{{ 'Carefully perform the following instructions, in order, starting each with a new line.\n' }}{{ 'Firstly, Decide which of the retrieved documents are relevant to the user\'s last input by writing \'Relevant Documents:\' followed by comma-separated list of document numbers. If none are relevant, you should instead write \'None\'.\n' }}{{ 'Secondly, Decide which of the retrieved documents contain facts that should be cited in a good answer to the user\'s last input by writing \'Cited Documents:\' followed a comma-separated list of document numbers. If you dont want to cite any of them, you should instead write \'None\'.\n' }}{% if citation_mode=='accurate' %}{{ 'Thirdly, Write \'Answer:\' followed by a response to the user\'s last input in high quality natural english. Use the retrieved documents to help you. Do not insert any citations or grounding markup.\n' }}{% endif %}{{ 'Finally, Write \'Grounded answer:\' followed by a response to the user\'s last input in high quality natural english. Use the symbols <co: doc> and </co: doc> to indicate when a fact comes from a document in the search result, e.g <co: 0>my fact</co: 0> for a fact from document 0.' }}{{ '<|END_OF_TURN_TOKEN|>' }}{% if add_generation_prompt %}{{ '<|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>' }}{% endif %}
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
The model's total size is approximately 207.6 GB (Source: model.safetensors.index.json.txt). As the model weights are stored in `float16` format (Source: config.json.txt), loading the model requires at least 208 GB of available RAM or VRAM.

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model has a built-in safety mechanism as part of its prompt structure for tool use and RAG. A "Safety Preamble" in the chat template instructs the model: "The instructions in this section override those in the task description and style guide sections. Don't answer questions that are harmful or immoral" (Source: tokenizer_config.json.txt).

No other information is provided regarding the use of sensitive data, risk identification and mitigation strategies, or potential harms and affected groups.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Lack of Transparency:** There is no information about the datasets used for training or evaluation. This makes it impossible to assess potential biases in the model regarding demographics, languages, or topics.
*   **No Performance Data:** The repository does not contain any quantitative performance metrics (e.g., accuracy, F1-score) on standard benchmarks. The model's capabilities and limitations are therefore unevaluated.
*   **Unknown Biases:** Without information on the training data and evaluation results, the model may produce outputs that are biased, inaccurate, or otherwise problematic.

### Recommendations:
*   Users should conduct thorough testing and evaluation on their specific use cases before deploying this model in any production environment.
*   Given the lack of information on biases, users should be particularly cautious when using the model for applications involving sensitive demographics or high-stakes decisions.
*   Users should implement their own content moderation and safety guardrails in addition to the model's built-in safety preamble.