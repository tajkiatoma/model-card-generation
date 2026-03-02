## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (LICENSE; configuration_phi3.py; CODE_OF_CONDUCT.md).

### Model date:
The copyright year for the model's configuration files is 2024 (configuration_phi3.py). No other specific dates regarding the model's development timeline are provided.

### Model version:
This model is `Phi-3-mini-128k-instruct` (config.json). It is part of the Phi-3 family of models, which also includes `Phi-3-mini-4k-instruct`. The primary difference is the context length, with this version supporting up to 128,000 tokens (`max_position_embeddings: 131072`) compared to the 4,000 tokens of the other version (configuration_phi3.py; config.json). The underlying modeling script has a version number of `0.0.5` (modeling_phi3.py).

### Model type:
The model is a `phi3` type, specifically a `Phi3ForCausalLM` (config.json). This is a Transformer-based, decoder-only language model designed for causal language modeling (modeling_phi3.py).

**Architecture Details:**
*   **Hidden Size:** 3072 (config.json)
*   **Intermediate Size (MLP):** 8192 (config.json)
*   **Number of Hidden Layers:** 32 (config.json)
*   **Number of Attention Heads:** 32 (config.json)
*   **Number of Key-Value Heads:** 32 (implying Multi-Head Attention) (config.json)
*   **Activation Function:** SiLU ("silu") (config.json)
*   **Normalization:** RMSNorm (`Phi3RMSNorm`) (modeling_phi3.py)
*   **Positional Embeddings:** Rotary Position Embeddings (`Phi3RotaryEmbedding`) with a "longrope" scaling strategy to extend the context length from a trained length of 4096 tokens to 131,072 tokens (config.json; modeling_phi3.py).
*   **Attention Implementations:** The model supports multiple attention mechanisms, including a standard eager implementation (`Phi3Attention`), Flash Attention 2 (`Phi3FlashAttention2`), and SDPA (`Phi3SdpaAttention`) (modeling_phi3.py).

**Model Size:**
*   **Total Size on Disk:** 7,642,159,104 bytes (approx. 7.64 GB) (model.safetensors.index.json)
*   **Vocabulary Size:** 32,064 (config.json)
*   **Data Type:** bfloat16 (config.json)

**Context Length:**
*   **Maximum Position Embeddings:** 131,072 (128k) (config.json)
*   **Original Maximum Position Embeddings (during training):** 4096 (config.json)

### Training details:
Information regarding the original pre-training of the model is not available in the repository. However, a sample fine-tuning script is provided (`sample_finetune.py`), which demonstrates how the model can be further trained.

The sample fine-tuning process uses the following configuration:
*   **Algorithm:** Supervised Fine-Tuning (SFT) using the `SFTTrainer` from the TRL library (sample_finetune.py).
*   **Optimization:** Low-Rank Adaptation (LoRA) is used for parameter-efficient fine-tuning (PEFT) (sample_finetune.py).
    *   `r`: 16
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `target_modules`: "all-linear"
*   **Key Hyperparameters** (from `TrainingArguments`):
    *   `learning_rate`: 5.0e-06 (sample_finetune.py)
    *   `lr_scheduler_type`: "cosine" (sample_finetune.py)
    *   `warmup_ratio`: 0.2 (sample_finetune.py)
    *   `num_train_epochs`: 1 (sample_finetune.py)
    *   `per_device_train_batch_size`: 4 (sample_finetune.py)
    *   `gradient_accumulation_steps`: 1 (sample_finetune.py)
    *   `mixed_precision`: `bf16` (sample_finetune.py)
*   **Techniques:** Gradient checkpointing is enabled to save memory (sample_finetune.py). The script is also configured to use DeepSpeed with ZeRO stage 3 for distributed training (sample_finetune.py).

### Paper or other resource for more information:
Insufficient information.

### Citation details:
Insufficient information.

### License:
The model and its associated software are provided under the MIT License (LICENSE). Some code files provided by Hugging Face within the repository are licensed under the Apache License, Version 2.0 (e.g., configuration_phi3.py, modeling_phi3.py). The software also incorporates third-party material, such as `flash-attention`, which is licensed under the BSD 3-Clause License (ThirdPartyNotices.txt).

### Contact:
*   For questions or concerns regarding the Microsoft Open Source Code of Conduct, contact `opencode@microsoft.com` (CODE_OF_CONDUCT.md).
*   To report security vulnerabilities, contact the Microsoft Security Response Center (MSRC) at `https://msrc.microsoft.com/create-report` or email `secure@microsoft.com` (SECURITY.md).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is an instruction-tuned causal language model intended for use as a conversational AI or chatbot. Its name, `Phi-3-mini-128k-instruct`, and the presence of a detailed chat template indicate its primary purpose is to follow user instructions and engage in multi-turn conversations (config.json; tokenizer_config.json).

The model can be used for various text generation tasks. It also serves as a base model that can be fine-tuned for more specific downstream tasks, such as sequence classification and token classification, as demonstrated by the `Phi3ForSequenceClassification` and `Phi3ForTokenClassification` classes in the modeling code (modeling_phi3.py).

The model expects input formatted in a specific chat structure, with roles for `system`, `user`, and `assistant`, each delimited by special tokens like `<|system|>`, `<|user|>`, and `<|end|>` (tokenizer_config.json).

### Primary intended users:
The primary intended users are AI researchers and developers who can build upon, fine-tune, and integrate the model into their applications. The inclusion of a sample fine-tuning script and its compatibility with popular libraries like Hugging Face Transformers, PEFT, and TRL supports this (sample_finetune.py).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model can be loaded using the `transformers` library. For optimal performance, it is recommended to use `flash_attention_2` if available (sample_finetune.py).

**Basic Generation Example:**
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# It is recommended to use the Flash Attention 2 implementation for better performance.
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
    attn_implementation="flash_attention_2"
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

prompt = "This is an example script."
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate text
generation_args = {
    "max_new_tokens": 50,
    "temperature": 0.7,
    "do_sample": True,
}
output_ids = model.generate(**inputs, **generation_args)
response = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
print(response)
```

**Chat Template Usage:**
The model is designed to be used with a specific chat template. Here is how to format a conversation:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
    attn_implementation="flash_attention_2"
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

# Apply the chat template
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to("cuda")

# Generate a response
output_ids = model.generate(inputs, max_new_tokens=32, eos_token_id=tokenizer.eos_token_id)
response = tokenizer.decode(output_ids[0][inputs.shape[1]:], skip_special_tokens=True)
print(response)
```
**Sample Output:**
A sample output from a similar model version is provided in the documentation (modeling_phi3.py):
```
'This is an example script .\n Certainly! Below is a sample script that demonstrates a simple task, such as calculating the sum'
```

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
Insufficient information.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
No information is provided about the datasets used for the original evaluation of the model. The included sample fine-tuning script uses the `test_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for its evaluation step (sample_finetune.py).

### Motivation:
Insufficient information.

### Preprocessing:
In the sample fine-tuning script, the evaluation data undergoes the following preprocessing:
1.  The `messages` column, containing conversational turns, is formatted into a single string using `tokenizer.apply_chat_template` (sample_finetune.py).
2.  The tokenizer's padding side is set to `left` for evaluation to support batched generation (sample_finetune.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
No information is provided about the datasets used for the original pre-training or instruction tuning of the model. The included sample script uses the `train_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for fine-tuning (sample_finetune.py).

### Motivation:
Insufficient information.

### Preprocessing:
In the sample fine-tuning script, the training data undergoes the following preprocessing:
1.  The `messages` column is formatted into a single string using `tokenizer.apply_chat_template` (sample_finetune.py).
2.  The `SFTTrainer` is configured with `packing=True`, which concatenates multiple short examples into a single sequence to maximize computational efficiency during training (sample_finetune.py).
3.  The tokenizer's `model_max_length` is set to 2048, and `padding_side` is set to `right` for the training phase (sample_finetune.py).

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
*   **Disk Space:** Approximately 7.64 GB (model.safetensors.index.json).
*   **VRAM/RAM:** The model is designed to be loaded in `bfloat16` format, requiring at least 7.64 GB of memory to load the weights (config.json).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The provided sample fine-tuning script suggests the following requirements:
*   **GPU:** V100 or a later generation GPU (sample_finetune.py).
*   **Frameworks:** The script utilizes `accelerate` with DeepSpeed ZeRO stage 3 offloading to reduce memory usage (sample_finetune.py).
*   **Precision:** The training is performed using `bfloat16` mixed precision (sample_finetune.py).
*   **Attention:** The script is configured to use `flash_attention_2` for improved performance and memory efficiency (sample_finetune.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The repository includes a `CODE_OF_CONDUCT.md` which adopts the Microsoft Open Source Code of Conduct, governing the behavior of contributors to the project (CODE_OF_CONDUCT.md). However, there is no specific information provided regarding ethical considerations in the model's development, such as the use of sensitive data, risk assessments, or mitigation strategies for potential harms.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model comes with no warranties. The license states that "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED..." (LICENSE).
*   Performance may vary depending on the attention implementation used. The modeling code warns, "You are not running the flash-attention implementation, expect numerical differences" if a fallback is used (modeling_phi3.py).
*   When using `flash_attention_2` with caching for batched generation, `padding_side` must be set to `'left'`. Using `'right'` padding may lead to unexpected behavior (modeling_phi3.py).
*   The SDPA attention implementation (`Phi3SdpaAttention`) does not support returning attention weights (`output_attentions=True`) and will fall back to the standard implementation if this option is enabled (modeling_phi3.py).

### Recommendations:
*   For better performance and memory efficiency, it is recommended to use the `flash_attention_2` implementation when possible (sample_finetune.py; modeling_phi3.py).
*   When performing batched generation, set the tokenizer's padding side to `left` (e.g., `tokenizer.padding_side = 'left'`) to avoid issues with the Flash Attention implementation (modeling_phi3.py).
*   For fine-tuning on consumer-grade or memory-constrained hardware, consider using techniques like DeepSpeed ZeRO3 and LoRA, as demonstrated in the sample script (sample_finetune.py).