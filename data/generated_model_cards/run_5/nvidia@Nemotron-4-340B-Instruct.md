## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model was developed using NeMo version 1.22.0 (Source: `model_config.yaml`, `nemo_version`). No specific version for the model itself is provided.

### Model type:
The model is a Megatron-based Generative Pre-trained Transformer (GPT) (Source: `model_config.yaml`, `target`). It is designed for chat and conversational tasks (Source: `model_config.yaml`, `data.chat`).

**Architecture Details:**
*   **Layers:** 96 (Source: `model_config.yaml`, `num_layers`)
*   **Hidden Size:** 18,432 (Source: `model_config.yaml`, `hidden_size`)
*   **FFN Hidden Size:** 73,728 (Source: `model_config.yaml`, `ffn_hidden_size`)
*   **Attention Heads:** 96 (Source: `model_config.yaml`, `num_attention_heads`)
*   **Query Groups:** 8, indicating it uses Grouped-Query Attention (GQA) (Source: `model_config.yaml`, `num_query_groups`)
*   **Context Length:** 4096 tokens (Source: `model_config.yaml`, `max_position_embeddings`, `encoder_seq_length`)
*   **Activation Function:** Squared ReLU (Source: `model_config.yaml`, `activation`)
*   **Normalization:** LayerNorm1p (Source: `model_config.yaml`, `normalization`)
*   **Position Embeddings:** Rotary Position Embeddings (RoPE) (Source: `model_config.yaml`, `position_embedding_type`)
*   **Tokenizer:** SentencePiece (Source: `model_config.yaml`, `tokenizer.library`)

### Training details:
The model was fine-tuned from a pre-existing base model located at `/models/340B_base` (Source: `model_config.yaml`, `restore_from_path`). The fine-tuning process involved Direct Preference Optimization (DPO) using a reward-reversed preference loss (Source: `model_config.yaml`, `dpo.preference_loss: reward_rev_dpo`).

**Key Training Parameters:**
*   **Optimizer:** Distributed Fused Adam (Source: `model_config.yaml`, `optim.name`)
    *   **Learning Rate:** 3.001e-07 (Source: `model_config.yaml`, `optim.lr`)
    *   **Betas:** (0.9, 0.98) (Source: `model_config.yaml`, `optim.betas`)
    *   **Weight Decay:** 0.1 (Source: `model_config.yaml`, `optim.weight_decay`)
*   **Scheduler:** Cosine Annealing with 10 warmup steps (Source: `model_config.yaml`, `optim.sched`)
*   **Precision:** `bf16-mixed` (Source: `model_config.yaml`, `precision`)
*   **Global Batch Size:** 256 (Source: `model_config.yaml`, `global_batch_size`)
*   **Micro Batch Size:** 1 (Source: `model_config.yaml`, `micro_batch_size`)
*   **Parallelism:**
    *   Tensor Model Parallel Size: 8 (Source: `model_config.yaml`, `tensor_model_parallel_size`)
    *   Pipeline Model Parallel Size: 4 (Source: `model_config.yaml`, `pipeline_model_parallel_size`)
*   **Dropout:** All dropout rates (hidden, attention, FFN) were set to 0.0 (Source: `model_config.yaml`, `hidden_dropout`, `attention_dropout`, `ffn_dropout`)
*   **Seed:** 1234 (Source: `model_config.yaml`, `seed`)

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
The model is intended for use as a conversational agent or chatbot (Source: `model_config.yaml`, `data.chat: true`). It is designed to process and generate text in a multi-turn dialogue format, following a specific structure of "System", "User", and "Assistant" roles (Source: `model_config.yaml`, `data.train_ds.prompt_template`).

The model's input is a formatted string representing the conversation history, and its output is the text for the Assistant's next turn (Source: `model_config.yaml`, `data.train_ds.label_key: output`).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model expects input in a specific chat format, using special tokens to delineate different parts of the conversation.

**Special Tokens:**
*   **System Turn Start:** `<extra_id_0>` (Source: `model_config.yaml`, `data.chat_prompt_tokens.system_turn_start`)
*   **User/Assistant Turn Start:** `<extra_id_1>` (Source: `model_config.yaml`, `data.chat_prompt_tokens.turn_start`)
*   **Start of Assistant's Label (for training):** `<extra_id_2>` (Source: `model_config.yaml`, `data.chat_prompt_tokens.label_start`)

**Prompt Template for Inference:**
To generate a response, the input prompt must follow this structure. The model will generate the text that comes after the final `<extra_id_1>Assistant` turn.

```
<extra_id_0>System
{system message}

<extra_id_1>User
{turn 1 user message}

<extra_id_1>Assistant
{turn 1 assistant message}

<extra_id_1>User
{turn 2 user message}

<extra_id_1>Assistant
```
(Source: `model_config.yaml`, `data.train_ds.prompt_template`)

**Example:**
```
<extra_id_0>System
You are a helpful assistant.

<extra_id_1>User
Hello, what is the capital of France?

<extra_id_1>Assistant
The capital of France is Paris.

<extra_id_1>User
What is it famous for?

<extra_id_1>Assistant
```

The model would then generate a response, such as: "Paris is famous for many landmarks, including the Eiffel Tower, the Louvre Museum, and the Notre-Dame Cathedral."

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
The model's performance during validation was measured using the `loss` metric (Source: `model_config.yaml`, `data.validation_ds.metric.name`).

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a validation dataset located at `/dataset/val.jsonl` (Source: `model_config.yaml`, `data.validation_ds.file_path`). The data is in JSONL format and was loaded as a Hugging Face dataset (Source: `model_config.yaml`, `data.data_impl`, `data.validation_ds.hf_dataset`). No further details on the size, source, or diversity of the data are available.

### Motivation:
Insufficient information

### Preprocessing:
The evaluation data was preprocessed using the following steps:
*   The data was formatted according to the chat `prompt_template` (Source: `model_config.yaml`, `data.validation_ds.prompt_template`).
*   Sequences were truncated from the right to a maximum length of 4096 tokens (Source: `model_config.yaml`, `data.validation_ds.max_seq_length`, `data.validation_ds.truncation_method`).
*   A SentencePiece tokenizer was used for tokenization (Source: `model_config.yaml`, `tokenizer.library`).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a dataset located at `/dataset/train.jsonl` (Source: `model_config.yaml`, `data.train_ds.file_path`). The data is in JSONL format and was loaded as a Hugging Face dataset (Source: `model_config.yaml`, `data.data_impl`, `data.train_ds.hf_dataset`). The dataset was shuffled during training (Source: `model_config.yaml`, `data.train_ds.shuffle: true`). No further details on the size, source, or diversity of the data are available.

### Motivation:
Insufficient information

### Preprocessing:
The training data was preprocessed using the following steps:
*   The data was formatted according to the chat `prompt_template` (Source: `model_config.yaml`, `data.train_ds.prompt_template`).
*   Sequences were truncated from the right to a maximum length of 4096 tokens (Source: `model_config.yaml`, `data.train_ds.max_seq_length`, `data.train_ds.truncation_method`).
*   A SentencePiece tokenizer was used for tokenization (Source: `model_config.yaml`, `tokenizer.library`).

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
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The provided configuration implies a significant hardware setup for training. The parallelism settings suggest a multi-node, multi-GPU environment, likely consisting of at least 32 GPUs (8 for tensor parallelism multiplied by 4 for pipeline parallelism) (Source: `model_config.yaml`, `tensor_model_parallel_size`, `pipeline_model_parallel_size`). The use of `bf16-mixed` precision indicates that the GPUs must support the bfloat16 data type (Source: `model_config.yaml`, `precision`).

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