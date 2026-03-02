## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Microsoft (LICENSE.txt). The model development code also credits the HuggingFace Inc. team (modeling_phi3.py).

### Model date:
The copyright notice in the model's implementation code is dated 2024 (modeling_phi3.py). The model configuration specifies that it was built with `transformers_version` "4.40.2" (config.json.txt).

### Model version:
The model name is `Phi-3-mini-128k-instruct` (_name_or_path in config.json.txt). The internal version number for the `Phi3PreTrainedModel` class is "0.0.5" (modeling_phi3.py). The repository lists other related models, such as `microsoft/Phi-3-mini-4k-instruct`, suggesting that this version is distinguished by its 128k token context length (modeling_phi3.py, configuration_phi3.py).

### Model type:
The model is a `Phi3ForCausalLM`, a Transformer-based model for causal language modeling (config.json.txt).

**Architecture Details:**
*   **Model Type:** `phi3` (config.json.txt).
*   **Layers:** The model consists of 32 hidden layers (`num_hidden_layers` in config.json.txt). Each layer is a `Phi3DecoderLayer` containing self-attention and MLP blocks (modeling_phi3.py).
*   **Attention Mechanism:** It uses 32 attention heads (`num_attention_heads`) and 32 key-value heads (`num_key_value_heads`), indicating Multi-Head Attention (config.json.txt). The implementation supports multiple attention mechanisms, including standard eager attention (`Phi3Attention`), `flash_attention_2` (`Phi3FlashAttention2`), and Scaled Dot-Product Attention (`Phi3SdpaAttention`) (modeling_phi3.py).
*   **Normalization:** The model uses RMS Normalization (`Phi3RMSNorm`) before the attention and MLP blocks and after the final layer (modeling_phi3.py, config.json.txt). The epsilon for RMSNorm is `1e-05` (config.json.txt).
*   **Positional Embeddings:** It employs Rotary Position Embeddings (RoPE). For long contexts, it uses `Phi3LongRoPEScaledRotaryEmbedding` with a `longrope` scaling type (modeling_phi3.py, config.json.txt). The RoPE base theta is 10000.0 (config.json.txt).
*   **Activation Function:** The hidden activation function is `silu` (config.json.txt).
*   **Hidden Size:** The hidden representation dimension is 3072 (`hidden_size` in config.json.txt).
*   **Intermediate Size:** The MLP intermediate dimension is 8192 (`intermediate_size` in config.json.txt).

**Model Size:**
*   **Total Size:** The model's total size is 7,642,159,104 bytes (approximately 7.64 GB) (model.safetensors.index.json.txt).
*   **Vocabulary Size:** 32,064 tokens (config.json.txt).

**Context Length:**
*   The model supports a maximum context length of 131,072 tokens (`max_position_embeddings` in config.json.txt). Its original training was with a context length of 4,096 tokens (`original_max_position_embeddings` in config.json.txt).

### Training details:
Information regarding the model's original pre-training is not available in the repository. However, a sample script for fine-tuning is provided (`sample_finetune.py`), which uses the following configuration:

*   **Algorithm:** Supervised Fine-Tuning (SFT) using the `SFTTrainer` from the TRL library (sample_finetune.py).
*   **Optimization:** The fine-tuning process utilizes Low-Rank Adaptation (LoRA) via the `peft` library. The LoRA configuration includes:
    *   `r`: 16
    *   `lora_alpha`: 32
    *   `lora_dropout`: 0.05
    *   `target_modules`: "all-linear"
    (sample_finetune.py).
*   **Training Arguments:**
    *   `learning_rate`: 5.0e-06
    *   `lr_scheduler_type`: "cosine"
    *   `num_train_epochs`: 1
    *   `per_device_train_batch_size`: 4
    *   `gradient_accumulation_steps`: 1
    *   `warmup_ratio`: 0.2
    *   `bf16`: True
    (sample_finetune.py).
*   **Techniques:** The script uses gradient checkpointing and is configured to work with DeepSpeed ZeRO Stage 3 to reduce memory usage (sample_finetune.py).

### Paper or other resource for more information:
The model's implementation code references a paper on Grouped Query Attention: https://arxiv.org/pdf/2305.13245.pdf (modeling_phi3.py).

The model can be found on the Hugging Face Hub at the following locations:
*   https://huggingface.co/microsoft/Phi-3-mini-4k-instruct (configuration_phi3.py)
*   https://huggingface.co/microsoft/Phi-3-mini-128k-instruct (configuration_phi3.py)

The model code incorporates material from `flash-attention`, available at https://github.com/Dao-AILab/flash-attention (NOTICE.md.txt).

### Citation details:
Insufficient information

### License:
The model and its associated software are released under the MIT License (LICENSE.txt).

The software also incorporates material from third parties, including `flash-attention`, which is available under the BSD 3-Clause License (NOTICE.md.txt).

### Contact:
For questions or concerns regarding the project's code of conduct, contact opencode@microsoft.com (CODE_OF_CONDUCT.md.txt).

For security vulnerabilities, please report them to the Microsoft Security Response Center (MSRC) at https://msrc.microsoft.com/create-report or via email to secure@microsoft.com (SECURITY.md.txt).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is an instruction-tuned causal language model (`Phi-3-mini-128k-instruct`) designed for text generation based on a given prompt (config.json.txt, modeling_phi3.py). Its architecture, `Phi3ForCausalLM`, is suited for auto-regressive decoding tasks (modeling_phi3.py). The provided fine-tuning script uses a chat dataset (`HuggingFaceH4/ultrachat_200k`) and applies a chat template, indicating that the model is intended for conversational or chat-based applications (sample_finetune.py).

The model takes `input_ids` (tokenized text) as input and generates a sequence of `generate_ids` as output (modeling_phi3.py).

### Primary intended users:
The provided resources, such as the sample fine-tuning script, suggest that the primary intended users are developers and researchers who want to build applications using or further fine-tune large language models (sample_finetune.py).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

### Inference
The following code snippet from the model's documentation demonstrates how to use the model for text generation (modeling_phi3.py):
```python
from transformers import AutoTokenizer, Phi3ForCausalLM

model = Phi3ForCausalLM.from_pretrained("microsoft/phi-3-mini-128k-instruct")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-128k-instruct")

prompt = "This is an example script ."
inputs = tokenizer(prompt, return_tensors="pt")

# Generate
generate_ids = model.generate(inputs.input_ids, max_length=30)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
```
**Sample Output:**
```
'This is an example script .\n Certainly! Below is a sample script that demonstrates a simple task, such as calculating the sum'
```
(modeling_phi3.py)

### Fine-tuning
A sample script, `sample_finetune.py`, is provided to demonstrate how to fine-tune the model.

**1. Installation:**
Users need to install the following dependencies:
```bash
conda install -c conda-forge accelerate
pip3 install -i https://pypi.org/simple/ bitsandbytes
pip3 install peft transformers trl datasets
pip3 install deepspeed
```
(sample_finetune.py)

**2. Configuration:**
Set up `accelerate` and DeepSpeed configuration based on the machine used by running `accelerate config` (sample_finetune.py).

**3. Running the script:**
The fine-tuning script can be launched using `accelerate launch sample_finetune.py` (sample_finetune.py).

The script loads the `microsoft/Phi-3-mini-128k-instruct` model and tokenizer, processes the `HuggingFaceH4/ultrachat_200k` dataset by applying a chat template, and then starts training using the `SFTTrainer` (sample_finetune.py).

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
The provided fine-tuning script includes an evaluation step (`trainer.evaluate()`) but does not specify which metrics are used to assess performance (sample_finetune.py).

### Decision thresholds:
Insufficient information

### Variation approaches:
The sample fine-tuning script evaluates the model on a predefined test split (`test_sft`) of the `HuggingFaceH4/ultrachat_200k` dataset (sample_finetune.py).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The sample fine-tuning script uses the `test_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset for evaluation (sample_finetune.py).

### Motivation:
Insufficient information

### Preprocessing:
The evaluation data is preprocessed using a function that applies the tokenizer's chat template to the `messages` column of the dataset. For evaluation, the tokenizer's `padding_side` is set to `'left'` (sample_finetune.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
No information is provided about the original pre-training dataset. The sample script for **fine-tuning** uses the `train_sft` split of the `HuggingFaceH4/ultrachat_200k` dataset (sample_finetune.py).

### Motivation:
Insufficient information

### Preprocessing:
For fine-tuning, the training data is preprocessed by applying the tokenizer's chat template to the `messages` column. The tokenizer is configured with `model_max_length = 2048`, the `pad_token` is set to the `unk_token`, and `padding_side` is set to `'right'` (sample_finetune.py).

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
The provided sample fine-tuning script (`sample_finetune.py`) offers the following guidance:
*   **GPU:** The script can be run on "V100 or later generation GPUs" (sample_finetune.py).
*   **Data Type:** The model is loaded with `torch_dtype=torch.bfloat16` (sample_finetune.py).
*   **Memory Reduction:** The script utilizes "DeepSpeed ZeRO3 offload to reduce the memory usage." To further reduce memory consumption, it is suggested to:
    *   reduce batch size
    *   decrease lora dimension
    *   restrict lora target modules
    (sample_finetune.py).
*   **Distributed Training:** The sample `accelerate` configuration uses DeepSpeed with `num_processes: 4` (sample_finetune.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The project has adopted the Microsoft Open Source Code of Conduct, which outlines standards for maintaining a positive and respectful community environment (CODE_OF_CONDUCT.md.txt).

The repository includes a security policy that details how to report security vulnerabilities to the Microsoft Security Response Center (MSRC). This provides a clear channel for mitigating security risks (SECURITY.md.txt).

No information is provided regarding the use of sensitive data during training, potential biases, or specific risks associated with the model's application.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Differences:** Users are warned that not running the `flash_attention_2` implementation will lead to numerical differences compared to the optimized version (modeling_phi3.py).
*   **Flash Attention Version:** The model's sliding window attention feature requires a version of the `flash-attention` library that supports the `window_size` parameter. Older versions may not be compatible (modeling_phi3.py).
*   **Padding Side:** When using `flash_attention_2` for batched generation, using `padding_side='right'` may lead to unexpected behavior. It is recommended to set `tokenizer.padding_side = 'left'` before tokenizing input (modeling_phi3.py).

### Recommendations:
*   **Performance:** For better performance, it is recommended to install the `flash-attention` package (modeling_phi3.py).
*   **Fine-tuning Dependencies:** For fine-tuning, users should install `accelerate`, `bitsandbytes`, `peft`, `transformers`, `trl`, and `deepspeed` (sample_finetune.py).
*   **Batched Generation:** When performing batched generation, set the tokenizer's padding side to 'left' to avoid issues with the Flash Attention implementation (modeling_phi3.py).