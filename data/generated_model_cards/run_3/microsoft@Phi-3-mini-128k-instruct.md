## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (LICENSE, configuration_phi3.py).

### Model date:
The model's development files are copyrighted in 2024, indicating its development and release occurred around this time (configuration_phi3.py, modeling_phi3.py). No other specific dates for development milestones or release are provided.

### Model version:
The model is named `Phi-3-mini-128k-instruct` (config.json). The `Phi3PreTrainedModel` class in the modeling code has a `_version` attribute set to "0.0.5" (modeling_phi3.py). This model is part of the Phi-3 family, which also includes other variants like `microsoft/Phi-3-mini-4k-instruct` (configuration_phi3.py). The key difference in this version is its support for a 128,000-token context length (`max_position_embeddings: 131072` in config.json).

### Model type:
The model is a Transformer-based causal language model, specifically of type `phi3` with a `Phi3ForCausalLM` architecture (config.json). It is designed as a decoder-only model for text generation (modeling_phi3.py).

**Architecture Details:**
*   **Hidden Size:** 3072 (config.json)
*   **Intermediate Size (MLP):** 8192 (config.json)
*   **Number of Hidden Layers:** 32 (config.json)
*   **Attention Heads:** 32 attention heads and 32 key-value heads (Multi-Head Attention) (config.json)
*   **Activation Function:** SiLU ("silu") (config.json)
*   **Normalization:** RMSNorm with an epsilon of 1e-05 (config.json, modeling_phi3.py)
*   **Positional Embeddings:** Rotary Position Embeddings (RoPE) with a `rope_theta` of 10000.0. It uses a "longrope" scaling strategy to extend the context length from its original 4096 tokens to 131,072 (config.json, configuration_phi3.py).
*   **Vocabulary Size:** 32,064 (config.json)

**Model Size:**
*   **Total Size on Disk:** Approximately 7.64 GB (model.safetensors.index.json)
*   **Data Type:** The model is intended to be used with `bfloat16` precision (config.json).

The model supports multiple attention implementations, including a standard eager implementation, Flash Attention 2, and SDPA (modeling_phi3.py).

### Training details:
Insufficient information is available regarding the original pre-training or instruction-tuning process.

However, a sample fine-tuning script is provided, which demonstrates how the model can be further trained using the `SFTTrainer` from the TRL library (sample_finetune.py). The key parameters from this sample script are:
*   **Dataset:** `HuggingFaceH4/ultrachat_200k` (sample_finetune.py)
*   **Learning Rate:** 5.0e-06 (sample_finetune.py)
*   **LR Scheduler:** Cosine (sample_finetune.py)
*   **Precision:** `bfloat16` (sample_finetune.py)
*   **Optimization:** The script uses DeepSpeed ZeRO Stage 3 and gradient checkpointing to manage memory usage (sample_finetune.py).
*   **PEFT:** The script uses LoRA with the following configuration:
    *   `r`: 16
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `target_modules`: "all-linear" (sample_finetune.py)

### Paper or other resource for more information:
No official paper for the Phi-3 model is cited in the repository. However, the modeling files reference the following resources for specific components:
*   A paper on Grouped Query Attention: `https://arxiv.org/pdf/2305.13245.pdf` (though this model uses Multi-Head Attention) (configuration_phi3.py).
*   A paper on attention mask strategy: `https://arxiv.org/abs/1910.13461` (modeling_phi3.py).
*   A list of all Phi-3 models on the Hugging Face Hub: `https://huggingface.co/models?filter=Phi-3` (modeling_phi3.py).

### Citation details:
Insufficient information.

### License:
The model repository is licensed under the MIT License (LICENSE). The source code files within the repository also contain headers indicating they are licensed under the Apache License, Version 2.0 (e.g., configuration_phi3.py, modeling_phi3.py). The software incorporates material from `flash-attention`, which is licensed under the BSD 3-Clause License (THIRD-PARTY-NOTICES.txt).

### Contact:
For questions or concerns regarding the Microsoft Open Source Code of Conduct, contact `opencode@microsoft.com` (CODE_OF_CONDUCT.md). For security vulnerabilities, contact the Microsoft Security Response Center (MSRC) at `secure@microsoft.com` (SECURITY.md).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is an instruction-tuned causal language model intended for conversational and instruction-following tasks (config.json, tokenizer_config.json). It is designed to be used as a chatbot, responding to user prompts in a structured dialogue format. The model's input-output structure is defined by a chat template that includes roles for `system`, `user`, and `assistant` (tokenizer_config.json).

Beyond chat, the model's architecture can be adapted for other NLP tasks. The provided code includes classes for `Phi3ForSequenceClassification` and `Phi3ForTokenClassification`, making it suitable for tasks like text classification and named entity recognition (modeling_phi3.py).

### Primary intended users:
The primary intended users are developers and researchers in the field of artificial intelligence and natural language processing. The provided sample fine-tuning script and adaptable model classes suggest it is aimed at users who wish to build upon, fine-tune, or integrate a powerful language model into their applications (sample_finetune.py, modeling_phi3.py).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model can be loaded using the `transformers` library. Below is an example of how to use it for text generation in a chat format.

**Code Snippet:**
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# It is recommended to use the Flash Attention 2 implementation for better performance
# model = AutoModelForCausalLM.from_pretrained(
#     "microsoft/Phi-3-mini-128k-instruct", 
#     device_map="cuda", 
#     torch_dtype="auto", 
#     trust_remote_code=True, 
#     attn_implementation="flash_attention_2"
# )

# The following code is for a machine without flash attention
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True
)

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")

messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "What is the capital of France?"},
]

# Apply the chat template
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate a response
generation_args = {
    "max_new_tokens": 500,
    "temperature": 0.7,
    "do_sample": True,
}

output_ids = model.generate(**inputs, **generation_args)
response = tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

print(response)
```
(Derived from modeling_phi3.py, sample_finetune.py, and tokenizer_config.json)

**Sample Output:**
```
The capital of France is Paris.
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
Insufficient information is available regarding the metrics used to evaluate the base model. The provided fine-tuning script (`sample_finetune.py`) includes an evaluation step, which for causal language models typically involves metrics like perplexity or cross-entropy loss, but the specific metrics are not detailed in the script (sample_finetune.py).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
No information is provided about the datasets used for the original evaluation of the `Phi-3-mini-128k-instruct` model. The sample fine-tuning script uses the `test_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for its evaluation step (sample_finetune.py).

### Motivation:
Insufficient information.

### Preprocessing:
For the evaluation data in the sample fine-tuning script, preprocessing consists of applying the model's chat template to the `messages` column. This formats the conversational turns into a single string that the model can process (sample_finetune.py). The template is defined as: `{% for message in messages %}{% if message['role'] == 'system' %}{{'<|system|>\n' + message['content'] + '<|end|>\n'}}{% elif message['role'] == 'user' %}{{'<|user|>\n' + message['content'] + '<|end|>\n'}}{% elif message['role'] == 'assistant' %}{{'<|assistant|>\n' + message['content'] + '<|end|>\n'}}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ '<|assistant|>\n' }}{% else %}{{ eos_token }}{% endif %}` (tokenizer_config.json).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Insufficient information is available about the datasets used for the original training of the model. The provided sample script demonstrates how to fine-tune the model on the `train_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset (sample_finetune.py).

### Motivation:
Insufficient information.

### Preprocessing:
Insufficient information is available about the preprocessing of the original training data. For the sample fine-tuning script, the preprocessing involves applying the model's chat template to format the conversational data (sample_finetune.py).

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
*   **Disk Space:** ~7.64 GB (model.safetensors.index.json).
*   **VRAM/RAM:** To load the model in its recommended `bfloat16` format, approximately 8 GB of VRAM is required, plus overhead for inference (config.json).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The provided sample fine-tuning script suggests the following requirements:
*   **GPU:** V100 or later generation GPUs are recommended (sample_finetune.py).
*   **Precision:** The script uses `bfloat16` for training (sample_finetune.py).
*   **Memory Optimization:** The script utilizes DeepSpeed ZeRO Stage 3 and gradient checkpointing to manage memory, making it feasible to fine-tune on multi-GPU setups (e.g., 4 GPUs) (sample_finetune.py).
*   **Attention Implementation:** Using `attn_implementation="flash_attention_2"` is recommended for better performance and potentially lower memory usage (sample_finetune.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The repository includes a general [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) that outlines standards for community interaction but does not provide specific ethical considerations for the model itself (CODE_OF_CONDUCT.md). No information is provided regarding the use of sensitive data, risk assessments, or mitigation strategies related to the model's potential harms or biases.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Differences:** The model's output may have numerical differences if not using the `flash-attention` implementation (modeling_phi3.py).
*   **Padding Side:** For batched generation using Flash Attention, users must set the tokenizer's padding side to `left` (`tokenizer.padding_side = 'left'`) to avoid unexpected behavior (modeling_phi3.py, sample_finetune.py). For training, `right` padding is used (sample_finetune.py).
*   **Gradient Checkpointing:** Using `use_cache=True` during training is incompatible with gradient checkpointing and will be automatically disabled (modeling_phi3.py).

### Recommendations:
*   **Performance:** For optimal performance, it is recommended to install and use the Flash Attention 2 implementation by setting `attn_implementation="flash_attention_2"` when loading the model (sample_finetune.py).
*   **Security:** Users should report any discovered security vulnerabilities to the Microsoft Security Response Center (MSRC) as detailed in the `SECURITY.md` file. Public disclosure of vulnerabilities is discouraged (SECURITY.md).