## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (LICENSE.txt, CODE_OF_CONDUCT.md.txt). The modeling code also acknowledges the HuggingFace Inc. team as contributors (modeling_phi3.py).

### Model date:
The copyright year on the modeling code is 2024 (modeling_phi3.py). No other specific dates regarding development milestones or release are provided.

### Model version:
The modeling script specifies `_version = "0.0.5"` (modeling_phi3.py). The model checkpoint is identified as `microsoft/Phi-3-mini-128k-instruct`, which distinguishes it from other versions like the `4k` context length model (sample_finetune.py).

### Model type:
**Model Architecture:**
The model is a Transformer-based language model of the `Phi3ForCausalLM` class (modeling_phi3.py). It is a decoder-only architecture consisting of multiple `Phi3DecoderLayer` blocks. Each decoder layer includes:
*   A self-attention mechanism (`Phi3Attention`) which supports standard eager attention, Flash Attention 2 (`Phi3FlashAttention2`), and SDPA (`Phi3SdpaAttention`) implementations (modeling_phi3.py).
*   A Multi-Layer Perceptron (`Phi3MLP`) with a gated activation function (modeling_phi3.py).
*   Layer normalization using `Phi3RMSNorm` (modeling_phi3.py).
*   Rotary Position Embeddings (`Phi3RotaryEmbedding`) for incorporating positional information. It also supports `Phi3LongRoPEScaledRotaryEmbedding` for handling longer sequences based on the `rope_scaling` configuration (modeling_phi3.py).
*   The model incorporates material from third parties, specifically `flash-attention` from Dao-AILab (NOTICE.md.txt).

**Model Category:**
The model is a Causal Language Model (Causal LM) designed for text generation and instruction-following tasks (modeling_phi3.py, sample_finetune.py).

**Model Size and Context Length:**
*   **Total Size:** The model has a total size of 7,642,159,104 bytes (approximately 7.64 GB) (model.safetensors.index.json.txt).
*   **Supported Context Length:** The model supports a maximum context length of 131,072 tokens (tokenizer_config.json.txt). The sample fine-tuning script uses a shorter sequence length of 2048 (sample_finetune.py).

**Tokenizer:**
*   The model uses a `LlamaTokenizer` (tokenizer_config.json.txt).
*   It employs a Byte-Pair Encoding (BPE) model (tokenizer.json.txt).
*   The vocabulary size is 32,064 (modeling_phi3.py, configuration_phi3.py from `modeling_phi3.py`).

### Training details:
The provided repository includes a sample fine-tuning script (`sample_finetune.py`) rather than details of the original pre-training. This script demonstrates how the model can be fine-tuned using Parameter-Efficient Fine-Tuning (PEFT) with LoRA (Low-Rank Adaptation).

**Fine-tuning Algorithm:**
*   Supervised Fine-Tuning (SFT) using the `SFTTrainer` from the TRL library (sample_finetune.py).

**Key Parameters and Hyperparameters for Fine-tuning:**
The sample script defines the following configuration:
*   **Training Arguments (`training_config`):**
    *   `bf16`: True (uses bfloat16 precision)
    *   `learning_rate`: 5.0e-06
    *   `lr_scheduler_type`: "cosine"
    *   `num_train_epochs`: 1
    *   `per_device_train_batch_size`: 4
    *   `gradient_accumulation_steps`: 1
    *   `gradient_checkpointing`: True
    *   `warmup_ratio`: 0.2
    *   `logging_steps`: 20
    *   `save_steps`: 100
    *   `output_dir`: "./checkpoint_dir"
    (sample_finetune.py)
*   **PEFT Configuration (`peft_config`):**
    *   `r`: 16 (LoRA rank)
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `bias`: "none"
    *   `task_type`: "CAUSAL_LM"
    *   `target_modules`: "all-linear"
    (sample_finetune.py)

**Optimization:**
*   The script uses `attn_implementation="flash_attention_2"` for memory efficiency and performance (sample_finetune.py).
*   It is designed to be run with DeepSpeed ZeRO Stage 3 to reduce memory usage (sample_finetune.py).

### Paper or other resource for more information:
The repository provides links to related resources:
*   A list of pretrained Phi-3 models on the Hugging Face Hub is mentioned in the modeling script (modeling_phi3.py).
*   The software incorporates material from the `flash-attention` repository on GitHub: https://github.com/Dao-AILab/flash-attention (NOTICE.md.txt).

### Citation details:
Insufficient information.

### License:
The model and its associated code are released under multiple licenses:
*   The main software is under the **MIT License**. The license requires that the copyright notice and permission notice be included in all copies or substantial portions of the Software (LICENSE.txt).
*   The Python modeling code (`modeling_phi3.py`) is licensed under the **Apache License, Version 2.0** (modeling_phi3.py).
*   A third-party component, `flash-attention`, is included under the **BSD 3-Clause License** (NOTICE.md.txt).

### Contact:
*   For questions or concerns regarding the Microsoft Open Source Code of Conduct, contact [opencode@microsoft.com](mailto:opencode@microsoft.com) (CODE_OF_CONDUCT.md.txt).
*   For reporting security vulnerabilities, contact the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) or email [secure@microsoft.com](mailto:secure@microsoft.com) (SECURITY.md.txt).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a Causal Language Model intended for text generation and conversational AI applications. Its designation as an "instruct" model and the inclusion of a `chat_template` indicate it is fine-tuned to follow user instructions and participate in dialogue (sample_finetune.py, tokenizer_config.json.txt).

The model's input-output structure is text-based. For chat applications, the input should be formatted as a list of messages, each with a "role" (`system`, `user`, or `assistant`) and "content". The model then generates the assistant's response (tokenizer_config.json.txt, sample_finetune.py).

### Primary intended users:
The provided fine-tuning script and detailed modeling code suggest that the primary intended users are developers and researchers in the field of machine learning and natural language processing (sample_finetune.py, modeling_phi3.py).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model can be loaded and used with the Hugging Face `transformers` library. The sample fine-tuning script provides an example of how to load the model and tokenizer (sample_finetune.py).

**Loading the Model and Tokenizer:**
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint_path = "microsoft/Phi-3-mini-128k-instruct"
model_kwargs = dict(
    use_cache=False,
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
    torch_dtype=torch.bfloat16,
    device_map=None
)
model = AutoModelForCausalLM.from_pretrained(checkpoint_path, **model_kwargs)
tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
```
(Source: sample_finetune.py)

**Chat Usage:**
The model uses a specific chat template for formatting conversational input. The roles for messages are `<|system|>`, `<|user|>`, and `<|assistant|>` (tokenizer_config.json.txt, added_tokens.json.txt).

Here is an example of how to format input for a chat interaction:
```python
messages = [
    {"role": "user", "content": "Can you provide a recipe for a classic chocolate chip cookie?"},
]

# The tokenizer applies the chat template
inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

# Generate a response
# generate_ids = model.generate(inputs, max_length=512)
# response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```
(Source: tokenizer_config.json.txt, sample_finetune.py)

The chat template is defined as:
`{% for message in messages %}{% if message['role'] == 'system' %}{{'<|system|>\n' + message['content'] + '<|end|>\n'}}{% elif message['role'] == 'user' %}{{'<|user|>\n' + message['content'] + '<|end|>\n'}}{% elif message['role'] == 'assistant' %}{{'<|assistant|>\n' + message['content'] + '<|end|>\n'}}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '<|assistant|>\n' }}{% else %}{{ eos_token }}{% endif %}`
(Source: tokenizer_config.json.txt)

**Special Tokens:**
The tokenizer uses several special tokens, including:
*   `<s>`: Beginning of sequence token (bos_token) (tokenizer_config.json.txt).
*   `<|endoftext|>`: End of sequence token (eos_token) (tokenizer_config.json.txt, special_tokens_map.json.txt).
*   `<unk>`: Unknown token (unk_token) (tokenizer_config.json.txt).
*   `<|system|>`, `<|user|>`, `<|assistant|>`: Role tokens for chat (added_tokens.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information.

### Evaluation factors:
Insufficient information.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The provided `modeling_phi3.py` script specifies loss functions used for different tasks, which are used to guide training but are not typically reported as final performance measures:
*   For causal language modeling (`Phi3ForCausalLM`), `CrossEntropyLoss` is used (modeling_phi3.py).
*   For sequence classification (`Phi3ForSequenceClassification`), `MSELoss`, `CrossEntropyLoss`, or `BCEWithLogitsLoss` may be used depending on the problem type (modeling_phi3.py).

The sample fine-tuning script logs metrics from the training and evaluation process but does not specify which metrics are calculated (sample_finetune.py).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The sample fine-tuning script uses the `test_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for evaluation (sample_finetune.py).

### Motivation:
Insufficient information.

### Preprocessing:
The evaluation data is preprocessed using an `apply_chat_template` function. This function takes the `messages` column from the dataset and formats it into a single string field named `text` according to the model's chat template. Columns from the original dataset are removed after this mapping (sample_finetune.py). For the fine-tuning example, the maximum sequence length is set to 2048 tokens (sample_finetune.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The provided `sample_finetune.py` script uses the `train_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for fine-tuning (sample_finetune.py). Details about the original pre-training data are not available in the repository.

### Motivation:
Insufficient information.

### Preprocessing:
The preprocessing for the fine-tuning data is as follows:
*   **Chat Templating:** An `apply_chat_template` function is used to convert the conversational `messages` column into a single `text` field that the model can process (sample_finetune.py).
*   **Tokenization:** The tokenizer prepends a space to the input sequence and replaces any occurrences of a space with a specific space character (` `) (tokenizer.json.txt).
*   **Packing:** The `SFTTrainer` is configured with `packing=True`, which is a technique to combine multiple short examples into a single sequence to improve training efficiency (sample_finetune.py).
*   **Padding:** For the fine-tuning script, the tokenizer's padding side is set to `right` (sample_finetune.py).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Insufficient information.

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The sample script for fine-tuning loads the model using `torch_dtype=torch.bfloat16` and enables `attn_implementation="flash_attention_2"` to improve performance (sample_finetune.py).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The provided `sample_finetune.py` script is designed to run on "V100 or later generation GPUs" (sample_finetune.py). It utilizes several techniques to manage memory consumption during fine-tuning:
*   **DeepSpeed:** The script is intended to be launched via `accelerate` using a DeepSpeed configuration with ZeRO Stage 3 and CPU offloading enabled to reduce GPU memory usage (sample_finetune.py).
*   **Quantization/Precision:** The model is loaded in `bfloat16` (`bf16: True`) (sample_finetune.py).
*   **PEFT:** LoRA (Low-Rank Adaptation) is used to fine-tune only a small subset of the model's parameters (sample_finetune.py).
*   **Gradient Checkpointing:** This is enabled (`gradient_checkpointing: True`) to trade compute for memory (sample_finetune.py).

The script also suggests that memory consumption can be further reduced by decreasing the batch size, lowering the LoRA dimension (`r`), or restricting the LoRA target modules (sample_finetune.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The repository includes a **Code of Conduct** based on the Microsoft Open Source Code of Conduct. It promotes a positive and respectful environment and outlines unacceptable behaviors such as harassment, trolling, and publishing others' private information. It provides a contact email, [opencode@microsoft.com](mailto:opencode@microsoft.com), for reporting issues (CODE_OF_CONDUCT.md.txt).

The repository also contains a **Security Policy** that outlines a process for reporting security vulnerabilities to the Microsoft Security Response Center (MSRC). It explicitly requests that vulnerabilities not be reported through public GitHub issues to ensure they are handled securely (SECURITY.md.txt).

There is no information provided regarding the use of sensitive data in the training process or specific risks associated with the model's application.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Differences:** The modeling code warns that not using the `flash_attention_2` implementation will result in numerical differences compared to the reference implementation (modeling_phi3.py).
*   **Flash Attention Version:** The code notes that older versions of the `flash-attention` library may not support sliding window attention. It is recommended to upgrade the library or use `attn_implementation='eager'` in such cases (modeling_phi3.py).

### Recommendations:
*   **Performance:** For better performance, it is recommended to install the `flash-attention` package (modeling_phi3.py).
*   **Batched Generation:** When performing batched generation with Flash Attention, it is recommended to set the tokenizer's padding side to `left` (`tokenizer.padding_side = 'left'`) to avoid unexpected behavior (sample_finetune.py).