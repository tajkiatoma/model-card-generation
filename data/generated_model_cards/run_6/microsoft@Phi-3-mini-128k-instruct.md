## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (LICENSE.txt; configuration_phi3.py; modeling_phi3.py). The project has adopted the Microsoft Open Source Code of Conduct (CODE_OF_CONDUCT.md.txt).

### Model date:
Insufficient information

### Model version:
The model's internal version is "0.0.5" (modeling_phi3.py). It was developed for `transformers` version "4.40.2" (config.json.txt).

### Model type:
The model is a `phi3` type, specifically `Phi3ForCausalLM`, which is a Transformer-based model for causal language modeling (config.json.txt; modeling_phi3.py).

**Architecture Details:**
*   **Model Type:** `phi3` (config.json.txt)
*   **Architecture:** Transformer decoder consisting of 32 hidden layers (`num_hidden_layers`) (config.json.txt; configuration_phi3.py).
*   **Hidden Size:** 3072 (`hidden_size`) (config.json.txt; configuration_phi3.py).
*   **Intermediate Size (MLP):** 8192 (`intermediate_size`) (config.json.txt; configuration_phi3.py).
*   **Attention Heads:** 32 (`num_attention_heads`) (config.json.txt; configuration_phi3.py).
*   **Key-Value Heads:** 32 (`num_key_value_heads`), indicating it uses Multi-Head Attention (MHA) rather than Grouped-Query Attention (GQA) or Multi-Query Attention (MQA) (config.json.txt; configuration_phi3.py).
*   **Activation Function:** SiLU (`hidden_act: "silu"`) (config.json.txt; configuration_phi3.py).
*   **Normalization:** RMSNorm (`Phi3RMSNorm`) with an epsilon of 1e-05 (modeling_phi3.py; config.json.txt).
*   **Positional Embeddings:** Rotary Position Embeddings (RoPE) with a `rope_theta` of 10000.0 (modeling_phi3.py; config.json.txt). It uses a "longrope" scaling strategy to extend the context length (config.json.txt; configuration_phi3.py).
*   **Attention Implementation:** The model supports multiple attention implementations, including `eager` (standard PyTorch), `flash_attention_2`, and `sdpa` (scaled dot-product attention) (modeling_phi3.py). A sample fine-tuning script recommends using `attn_implementation="flash_attention_2"` (sample_finetune.py).

**Size and Context Length:**
*   **Total Size:** Approximately 7.64 GB (`total_size`: 7642159104) (model.safetensors.index.json.txt).
*   **Vocabulary Size:** 32,064 (`vocab_size`) (config.json.txt; configuration_phi3.py).
*   **Maximum Context Length:** The model supports a maximum sequence length of 131,072 tokens (`max_position_embeddings`) (config.json.txt). It was originally trained with a context length of 4096 (`original_max_position_embeddings`) and uses RoPE scaling to handle longer sequences (config.json.txt; configuration_phi3.py).

**Special Tokens:**
The model uses several special tokens, including `<|endoftext|>`, `<|assistant|>`, `<|system|>`, and `<|user|>` (added_tokens.json.txt; tokenizer.json.txt). The End-Of-Sequence (EOS) token ID is 32000 (config.json.txt).

### Training details:
The provided information does not cover the original pre-training process. However, a sample fine-tuning script (`sample_finetune.py`) provides details for fine-tuning the model using the SFTTrainer from the TRL library.

**Fine-tuning Algorithm:**
*   Supervised Fine-Tuning (SFT) (sample_finetune.py).
*   Quantization-aware training can be used via `BitsAndBytesConfig` (sample_finetune.py).
*   Low-Rank Adaptation (LoRA) is used for parameter-efficient fine-tuning (sample_finetune.py).

**Fine-tuning Hyperparameters (from `sample_finetune.py`):**
*   **Precision:** `bf16: True` (sample_finetune.py).
*   **Learning Rate:** 5.0e-06 (sample_finetune.py).
*   **LR Scheduler:** `cosine` (`lr_scheduler_type`) (sample_finetune.py).
*   **Warmup Ratio:** 0.2 (sample_finetune.py).
*   **Optimizer:** The script uses DeepSpeed ZeRO3, which can offload the optimizer (sample_finetune.py).
*   **Batch Size:** 4 per device (`per_device_train_batch_size`) (sample_finetune.py).
*   **Gradient Accumulation:** 1 (`gradient_accumulation_steps`) (sample_finetune.py).
*   **Gradient Checkpointing:** `True` (sample_finetune.py).
*   **LoRA Configuration (`peft_config`):**
    *   `r`: 16
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `target_modules`: "all-linear"
    (sample_finetune.py)

### Paper or other resource for more information:
The model configuration files list Hugging Face repositories as the primary resource for more information (configuration_phi3.py; modeling_phi3.py):
*   [https://huggingface.co/microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) (configuration_phi3.py)
*   [https://huggingface.co/microsoft/Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) (configuration_phi3.py)

The configuration file also references a paper on Grouped Query Attention for more details on that specific technique: [https://arxiv.org/pdf/2305.13245.pdf](https://arxiv.org/pdf/2305.13245.pdf) (configuration_phi3.py).

### Citation details:
Insufficient information

### License:
The model is licensed under the MIT License (LICENSE.txt). The license grants permission to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, provided that the copyright notice and permission notice are included in all copies (LICENSE.txt). The software is provided "AS IS", without warranty of any kind (LICENSE.txt).

The software also incorporates material from third parties, such as `flash-attention`, which is licensed under the BSD 3-Clause License (NOTICE.md.txt).

### Contact:
For questions or concerns regarding the Microsoft Open Source Code of Conduct, the contact is [opencode@microsoft.com](mailto:opencode@microsoft.com) (CODE_OF_CONDUCT.md.txt).

For reporting security vulnerabilities, contact the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) or by email at [secure@microsoft.com](mailto:secure@microsoft.com) (SECURITY.md.txt).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a causal language model (`Phi3ForCausalLM`) that has been instruction-tuned (`Phi-3-mini-128k-instruct`), making it suitable for chat and instruction-following tasks (modeling_phi3.py; config.json.txt). Its primary use is to generate text-based responses to user prompts in a conversational format (tokenizer_config.json.txt).

The model's input-output structure is text-in, text-out. It processes a sequence of text formatted with special tokens for system, user, and assistant roles, and generates a text response for the assistant (tokenizer_config.json.txt).

### Primary intended users:
The provided fine-tuning script and model implementation suggest that the primary intended users are developers and researchers in the field of machine learning and natural language processing (sample_finetune.py; modeling_phi3.py).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model. 

The model can be loaded using the `transformers` library. The following Python code snippet, derived from the model's docstrings, demonstrates how to use the model for text generation (modeling_phi3.py).

**Input/Output Structure:**
The model expects input formatted as a chat conversation. The `tokenizer.apply_chat_template` method should be used to format the input correctly with special tokens like `<|system|>`, `<|user|>`, and `<|assistant|>` (tokenizer_config.json.txt; sample_finetune.py).

**Code Snippet:**
```python
from transformers import AutoTokenizer, Phi3ForCausalLM

# Load the model and tokenizer
model = Phi3ForCausalLM.from_pretrained("microsoft/phi-3-mini-128k-instruct")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-128k-instruct")

# Create a prompt
prompt = "This is an example script ."
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
generate_ids = model.generate(inputs.input_ids, max_length=30)
output = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

print(output)
```
(modeling_phi3.py)

**Sample Output (from docstring):**
```
'This is an example script .\n Certainly! Below is a sample script that demonstrates a simple task, such as calculating the sum'
```
(modeling_phi3.py)

**Chat Template Usage:**
For conversational use, the tokenizer's chat template should be applied as shown in the sample fine-tuning script (sample_finetune.py; tokenizer_config.json.txt):
```python
messages = [
    {"role": "user", "content": "Can you provide a short story about a robot learning to paint?"},
]

# The tokenizer applies the chat template to format the input
# e.g., "<|user|>\nCan you provide a short story about a robot learning to paint?<|end|>\n<|assistant|>\n"
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
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
The sample fine-tuning script uses the test split of the `HuggingFaceH4/ultrachat_200k` dataset for evaluation (`raw_dataset["test_sft"]`) (sample_finetune.py).

### Motivation:
Insufficient information

### Preprocessing:
The evaluation data is preprocessed by applying a chat template to format the conversational turns. This is done using the `tokenizer.apply_chat_template` method, which converts the `messages` column into a single formatted string in the `text` column (sample_finetune.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Information on the original pre-training data is not provided. The sample script for fine-tuning uses the training split of the `HuggingFaceH4/ultrachat_200k` dataset (`raw_dataset["train_sft"]`) (sample_finetune.py).

### Motivation:
Insufficient information

### Preprocessing:
The fine-tuning data is preprocessed by applying the model's chat template using `tokenizer.apply_chat_template`. This formats the conversational data into a single string (sample_finetune.py). The `SFTTrainer` is also configured with `packing=True`, which concatenates multiple short examples into a single sequence to improve training efficiency (sample_finetune.py).

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
*   **Disk Space:** The model weights have a total size of approximately 7.64 GB (model.safetensors.index.json.txt).
*   **Precision:** The model is designed to be loaded in `bfloat16` precision (`torch_dtype`) (config.json.txt; sample_finetune.py). Loading in this precision requires a GPU that supports it (e.g., Ampere series or newer).
*   **VRAM:** Loading the model in `bfloat16` would require at least 7.64 GB of VRAM, plus overhead for the model architecture and activations.

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The provided sample fine-tuning script (`sample_finetune.py`) suggests the following requirements:
*   **GPU:** The script notes it can be run on "V100 or later generation GPUs" (sample_finetune.py).
*   **Precision:** Fine-tuning is performed in `bfloat16` (`bf16: True`) (sample_finetune.py).
*   **Distributed Training:** The script is designed to be launched with `accelerate` and supports DeepSpeed ZeRO Stage 3 with optimizer and parameter offloading to reduce memory usage (sample_finetune.py).
*   **Attention:** The script recommends using `attn_implementation="flash_attention_2"` for better performance, which requires the `flash-attn` package to be installed (sample_finetune.py; modeling_phi3.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The repository includes a Code of Conduct which states that the project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) (CODE_OF_CONDUCT.md.txt).

The repository also provides a security policy for reporting vulnerabilities. It explicitly states not to report security issues through public GitHub issues and instead directs users to the Microsoft Security Response Center (MSRC) (SECURITY.md.txt).

There is no specific information provided regarding the use of sensitive data, risk mitigation strategies during development, or known ethical risks associated with the model's application.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Differences:** The model's implementation file warns that users not running the `flash-attention` implementation should "expect numerical differences" compared to the standard eager attention mechanism (modeling_phi3.py).
*   **Padding for Batched Generation:** When using `flash_attention_2` with caching for batched generation, using `padding_side='right'` may lead to unexpected behavior. The model implementation raises a `ValueError` in this case (modeling_phi3.py).

### Recommendations:
*   **Performance:** For better performance, it is recommended to install the `flash-attention` package (modeling_phi3.py). The sample fine-tuning script also recommends loading the model with `attn_implementation="flash_attention_2"` (sample_finetune.py).
*   **Tokenization for Generation:** For batched generation, it is recommended to set the tokenizer's padding side to left: `tokenizer.padding_side = 'left'` (sample_finetune.py).
*   **Attention Implementation Fallback:** The SDPA (scaled dot-product attention) implementation does not support `output_attentions=True`. If this is required, the model will fall back to the manual "eager" implementation and issue a warning (modeling_phi3.py).