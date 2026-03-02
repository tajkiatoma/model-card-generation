## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (Source: `LICENSE`, `configuration_phi3.py`).

### Model date:
The model development code is copyrighted in 2024 (Source: `configuration_phi3.py`, `modeling_phi3.py`). The model was developed using `transformers` version 4.40.2 or later (Source: `config.json`, `generation_config.json`).

### Model version:
The model name is Phi-3-mini-128k-instruct (Source: `config.json`). This version is part of the Phi-3 model family, which also includes Phi-3-mini-4k-instruct. The primary difference is the context length, with this model supporting up to 128,000 tokens (Source: `configuration_phi3.py`, `config.json`). The internal version number for the model's implementation in the `transformers` library is "0.0.5" (Source: `modeling_phi3.py`).

### Model type:
Phi-3-mini-128k-instruct is a Transformer-based language model of type `phi3` (Source: `config.json`). It is a decoder-only, causal language model (`Phi3ForCausalLM`) designed for text generation (Source: `config.json`, `modeling_phi3.py`).

**Architecture Details:**
*   **Architecture:** Transformer decoder (Source: `modeling_phi3.py`).
*   **Activation Function:** SiLU (`silu`) (Source: `config.json`).
*   **Hidden Size:** 3072 (Source: `config.json`).
*   **Intermediate MLP Size:** 8192 (Source: `config.json`).
*   **Number of Hidden Layers:** 32 (Source: `config.json`).
*   **Number of Attention Heads:** 32 (Source: `config.json`).
*   **Number of Key-Value Heads:** 32 (implying Multi-Head Attention) (Source: `config.json`).
*   **Normalization:** RMSNorm with an epsilon of 1e-05 (Source: `config.json`, `modeling_phi3.py`).
*   **Positional Embeddings:** Rotary Position Embeddings (RoPE) with a `rope_theta` of 10000.0 and a `longrope` scaling strategy to handle long contexts (Source: `config.json`, `modeling_phi3.py`).

**Model Size:**
*   **Total Size on Disk:** Approximately 7.64 GB (Source: `model.safetensors.index.json`).
*   **Vocabulary Size:** 32,064 (Source: `config.json`).

**Context Length:**
*   **Maximum Context Length:** 131,072 tokens (128k) (Source: `config.json`, `tokenizer_config.json`).
*   **Original Training Context Length:** 4096 tokens (Source: `config.json`).

### Training details:
Information regarding the original pre-training of the model is not available in the repository. However, an example fine-tuning script is provided, which uses the following configuration (Source: `sample_finetune.py`):
*   **Fine-tuning Algorithm:** Supervised Fine-Tuning (SFT) using the `trl` library's `SFTTrainer` (Source: `sample_finetune.py`).
*   **Optimization:** The example uses DeepSpeed with ZeRO Stage 3 for memory optimization (Source: `sample_finetune.py`).
*   **Parameter-Efficient Fine-Tuning (PEFT):** The script uses Low-Rank Adaptation (LoRA) with the following hyperparameters:
    *   `r`: 16
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `target_modules`: "all-linear"
*   **Key Hyperparameters for Fine-tuning:**
    *   **Learning Rate:** 5.0e-06
    *   **LR Scheduler:** Cosine
    *   **Number of Epochs:** 1
    *   **Batch Size:** 4 per device
    *   **Precision:** `bfloat16`
    *   **Gradient Checkpointing:** Enabled
    *   **Warmup Ratio:** 0.2

### Paper or other resource for more information:
The repository does not link to a specific paper for the Phi-3 model itself. However, the model's configuration file references a paper for Grouped Query Attention (GQA), a technique used in some model configurations:
*   **GQA Paper:** [https://arxiv.org/pdf/2305.13245.pdf](https://arxiv.org/pdf/2305.13245.pdf) (Source: `configuration_phi3.py`).

The model is available on the Hugging Face Hub at these locations:
*   [https://huggingface.co/microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) (Source: `configuration_phi3.py`)
*   [https://huggingface.co/microsoft/Phi-3-mini-128k-instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) (Source: `configuration_phi3.py`)

### Citation details:
Insufficient information

### License:
The model repository contains a `LICENSE` file with the **MIT License** (Source: `LICENSE`).

The Python source code files (`configuration_phi3.py`, `modeling_phi3.py`) are part of the `transformers` library and include a header stating they are licensed under the **Apache License, Version 2.0** (Source: `configuration_phi3.py`, `modeling_phi3.py`).

The model also incorporates material from third parties, such as `flash-attention`, which is licensed under the **BSD 3-Clause License** (Source: `ThirdPartyNotices.txt`).

### Contact:
*   For questions or concerns regarding the Microsoft Open Source Code of Conduct, contact [opencode@microsoft.com](mailto:opencode@microsoft.com) (Source: `CODE_OF_CONDUCT.md`).
*   To report security vulnerabilities, contact the Microsoft Security Response Center (MSRC) at [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) or email [secure@microsoft.com](mailto:secure@microsoft.com) (Source: `SECURITY.md`).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is an instruction-tuned, causal language model intended for conversational AI and text generation tasks (Source: `config.json`, `tokenizer_config.json`). Its primary function is to generate text based on a given input prompt, following instructions provided in a chat-like format.

The model's input-output structure is text-to-text. It processes a string of text, which can be formatted with special tokens to delineate roles like "system", "user", and "assistant", and generates a text continuation (Source: `tokenizer_config.json`).

Example applications include:
*   Chatbots and conversational agents.
*   Instruction-following tasks.
*   Text summarization and generation.
*   Question answering.

### Primary intended users:
The primary intended users are software developers and researchers who want to build applications using or experiment with large language models (Source: `sample_finetune.py`, `modeling_phi3.py`).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model. 

The model can be loaded using the `AutoModelForCausalLM` and `AutoTokenizer` classes from the `transformers` library. For optimal performance, it is recommended to use `flash_attention_2` if the hardware supports it (Source: `sample_finetune.py`, `modeling_phi3.py`).

The model expects input formatted with a specific chat template to distinguish between system, user, and assistant roles (Source: `tokenizer_config.json`).

**Example Code Snippet for Inference:**
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Set torch device
torch.set_default_device("cuda")

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(
    "microsoft/Phi-3-mini-128k-instruct"
)

# Define the chat messages
messages = [
    {"role": "user", "content": "Can you provide a brief overview of the Phi-3 model family?"},
]

# Apply chat template and tokenize
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

# Generate a response
generate_ids = model.generate(
    inputs, 
    max_new_tokens=512,
    eos_token_id=tokenizer.eos_token_id
)
response_text = tokenizer.batch_decode(
    generate_ids[:, inputs.shape[1]:], 
    skip_special_tokens=True, 
    clean_up_tokenization_spaces=False
)[0]

print(response_text)
```
(Source: `modeling_phi3.py`, `tokenizer_config.json`)

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
When fine-tuning or evaluating with labels, the model's implementation calculates Cross-Entropy Loss to measure performance (Source: `modeling_phi3.py`). The provided fine-tuning script logs evaluation metrics but does not specify which ones are used beyond the loss (Source: `sample_finetune.py`).

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The provided example script for fine-tuning uses the test split of the `HuggingFaceH4/ultrachat_200k` dataset for evaluation (Source: `sample_finetune.py`). This is a publicly available dataset.

### Motivation:
Insufficient information

### Preprocessing:
The evaluation data is preprocessed by applying the model's chat template to format the conversational turns. The `apply_chat_template` function is used for this purpose. For evaluation, the tokenizer is configured with `padding_side='left'` (Source: `sample_finetune.py`).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Information about the original pre-training data for Phi-3-mini-128k-instruct is not available in the repository.

An example fine-tuning script uses the `train_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset (Source: `sample_finetune.py`). This is a publicly available, large-scale conversational dataset.

### Motivation:
Insufficient information

### Preprocessing:
The fine-tuning script preprocesses the data by applying the model's specific chat template to format the conversational messages into a single string. The `SFTTrainer` is then used with `packing=True` to combine multiple short examples into a single sequence to improve training efficiency. The tokenizer is configured with `padding_side='right'` for training, and sequences are truncated or padded to a `max_seq_length` of 2048 tokens (Source: `sample_finetune.py`).

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
*   **Model Size:** The model weights are approximately 7.64 GB (Source: `model.safetensors.index.json`).
*   **Precision:** The model is designed to be loaded in `bfloat16` precision (Source: `config.json`).
*   **Hardware:** A GPU is required. The fine-tuning script suggests that V100 or later generation GPUs are suitable (Source: `sample_finetune.py`).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The provided fine-tuning script (`sample_finetune.py`) outlines a configuration for memory-efficient training:
*   **Hardware:** V100 or later generation GPUs (Source: `sample_finetune.py`).
*   **Frameworks:** The script uses `accelerate` with a DeepSpeed ZeRO Stage 3 configuration to reduce memory usage (Source: `sample_finetune.py`).
*   **Precision:** `bf16` mixed precision is used (Source: `sample_finetune.py`).
*   **Techniques:** Gradient checkpointing is enabled to further save memory (Source: `sample_finetune.py`).
*   **Attention Mechanism:** The script loads the model with `attn_implementation="flash_attention_2"` for better performance and memory efficiency (Source: `sample_finetune.py`).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The repository includes a standard [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) which outlines standards for behavior in project communities (Source: `CODE_OF_CONDUCT.md`). It also provides a security policy for reporting vulnerabilities (Source: `SECURITY.md`).

However, the provided materials do not contain specific information regarding:
*   The use of sensitive or personal data during the model's training.
*   Known biases or risks associated with the model's application.
*   Strategies used during development to mitigate risks of harm.
*   Groups that may be disproportionately affected by the model's limitations.

### Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Differences:** The model's implementation warns that users not running the `flash-attention` implementation should expect numerical differences compared to the standard version (Source: `modeling_phi3.py`).
*   **Flash Attention Version:** The current `flash-attention` version may not support sliding window attention. Users are advised to upgrade their `flash-attention` library or use `attn_implementation='eager'` in such cases (Source: `modeling_phi3.py`).
*   **Data Type Casting:** The model code warns that if embedding or layer norm layers are upcasted to `float32`, the input hidden states might be silently cast, which can slow down training and inference. It is recommended not to cast LayerNorms to `fp32` (Source: `modeling_phi3.py`).
*   **Attention Output:** The `Phi3SdpaAttention` implementation does not support returning attention weights (`output_attentions=True`) and will fall back to the manual implementation if this is requested (Source: `modeling_phi3.py`).
*   **Batched Generation with Padding:** Using `padding_side='right'` for batched generation with the Flash Attention version of Phi-3 may lead to unexpected behavior (Source: `modeling_phi3.py`).

### Recommendations:
*   **Performance:** For better performance, it is recommended to install the `flash-attention` package (Source: `modeling_phi3.py`).
*   **Padding:** For fine-tuning, it is recommended to use `tokenizer.padding_side = 'right'`. For evaluation and inference, `tokenizer.padding_side = 'left'` should be used (Source: `sample_finetune.py`).
*   **Memory Usage:** To reduce memory consumption during fine-tuning, users can reduce the batch size, decrease the LoRA dimension, or restrict the LoRA target modules (Source: `sample_finetune.py`).
*   **Security:** Users should not report security vulnerabilities through public GitHub issues but instead report them to the Microsoft Security Response Center (Source: `SECURITY.md`).