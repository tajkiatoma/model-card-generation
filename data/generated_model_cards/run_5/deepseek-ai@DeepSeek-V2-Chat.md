## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by DeepSeek-AI (Paper: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model, p. 1). The legal entities associated with DeepSeek are Beijing DeepSeek Artificial Intelligence Fundamental Technology Research Co., Ltd., and Hangzhou DeepSeek Artificial Intelligence Fundamental Technology Research Co., Ltd. (LICENSE, Section 1).

### Model date:
The associated academic paper was submitted on June 19, 2024 (Paper: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model, p. 1). The license agreement is dated October 23, 2023 (LICENSE, Version 1.0).

### Model version:
The model is named DeepSeek-V2. It is a Mixture-of-Experts (MoE) model that is a successor to the dense model DeepSeek 67B. Compared to its predecessor, DeepSeek-V2 has more total parameters (236B vs 67B) but fewer activated parameters per token (21B vs 67B), leading to more economical training and efficient inference (Paper: Abstract, p. 1).

A smaller version, **DeepSeek-V2-Lite**, is also available. It has 15.7B total parameters, with 2.4B activated for each token, and is also equipped with the MLA and DeepSeekMoE architecture (Paper: Appendix B, p. 29).

### Model type:
DeepSeek-V2 is a Mixture-of-Experts (MoE) large language model for causal language modeling (Paper: Abstract, p. 1; config.json).

**Architecture:**
The model is based on the Transformer architecture, with innovations in the attention and Feed-Forward Network (FFN) layers (Paper: Section 2, p. 6).
*   **Attention:** It uses a custom **Multi-head Latent Attention (MLA)** mechanism, which employs low-rank key-value joint compression to reduce the size of the KV cache, boosting inference efficiency (Paper: Section 2.1, p. 6).
*   **Feed-Forward Networks:** It uses the **DeepSeekMoE** architecture, which segments experts into finer granularity and isolates shared experts to improve specialization and mitigate knowledge redundancy (Paper: Section 2.2.1, p. 9).
*   **Layers and Dimensions:** The model has 60 hidden layers (`num_hidden_layers`) and a hidden size of 5120 (`hidden_size`) (config.json). It features 128 attention heads (`num_attention_heads`) (Paper: Section 3.1.2, p. 12).
*   **Mixture-of-Experts Details:** Each MoE layer consists of 2 shared experts (`n_shared_experts`) and 160 routed experts (`n_routed_experts`), with 6 experts activated per token (`num_experts_per_tok`) (Paper: Section 3.1.2, p. 12; config.json).

**Size and Context Length:**
*   **Total Parameters:** 236B (Paper: Abstract, p. 1).
*   **Activated Parameters:** 21B per token (Paper: Abstract, p. 1).
*   **Model Size on Disk:** 439.103 GB (model.safetensors.index.json).
*   **Context Length:** Supports a context length of up to 128K tokens (Paper: Abstract, p. 1). The `max_position_embeddings` is set to 163840 in the configuration (config.json).

### Training details:
The model was pretrained on 8.1T tokens from a high-quality, multi-source corpus (Paper: Abstract, p. 1).

*   **Optimizer:** AdamW optimizer with β₁ = 0.9, β₂ = 0.95, and weight_decay = 0.1 (Paper: Section 3.1.2, p. 12).
*   **Learning Rate Schedule:** A warmup-and-step-decay strategy was used. The learning rate linearly increases from 0 to a maximum of 2.4 × 10⁻⁴ over the first 2K steps. It is then decayed by a factor of 0.316 at approximately 60% and 90% of the training steps (Paper: Section 3.1.2, p. 12).
*   **Batch Size:** A scheduling strategy was used, gradually increasing the batch size from 2304 to 9216 sequences (Paper: Section 3.1.2, p. 12).
*   **Sequence Length:** The model was trained with a maximum sequence length of 4K, which was later extended to 128K using YaRN (Paper: Section 3.1.2, p. 12; Section 3.1.4, p. 13).
*   **MoE Training:** To ensure load balancing between experts, the training process incorporated three types of auxiliary losses: expert-level, device-level, and communication balance losses. A token-dropping strategy was also employed to mitigate computation wastage from unbalanced loads (Paper: Sections 2.2.3 & 2.2.4, pp. 10-11). The device-limited routing mechanism ensures that for each token, target experts are distributed on at most 3 devices (M=3) (Paper: Section 3.1.2, p. 12).

### Paper or other resource for more information:
*   **Academic Paper:** A detailed description of the model's architecture, training, and evaluation can be found in the accompanying paper: *DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model*.
*   **GitHub Repository:** The model checkpoints are available at: `https://github.com/deepseek-ai/DeepSeek-V2` (Paper: Abstract, p. 1).

### Citation details:
Insufficient information. A BibTeX entry is not provided in the repository.

### License:
The model is governed by the DEEPSEEK LICENSE AGREEMENT, Version 1.0 (LICENSE).
*   **Permissions:** The license grants a perpetual, worldwide, non-exclusive, royalty-free, irrevocable copyright and patent license to reproduce, prepare, display, perform, sublicense, and distribute the model and its derivatives (LICENSE, Section II).
*   **Conditions:** When distributing the model or its derivatives, you must include the use-based restrictions (Attachment A) as an enforceable provision, provide a copy of the license, and retain all original copyright and patent notices (LICENSE, Section III, Para 4).
*   **Use-Based Restrictions:** The model cannot be used for specific purposes, including military use, harming minors, generating or disseminating verifiably false information to harm others, and uses that discriminate against or harm individuals or groups (LICENSE, Attachment A).
*   **Disclaimer:** The model is provided "AS IS" without warranties of any kind. The developers are not liable for any damages arising from the use of the model (LICENSE, Sections 10 & 11).

### Contact:
For questions or feedback, contact the developers at `research@deepseek.com` (Paper: p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
DeepSeek-V2 is a large language model designed for a wide range of natural language processing tasks in both English and Chinese (Paper: Section 3.2.1, p. 13). Its primary use is as a foundation model for text generation and understanding.

**Capabilities:**
Based on the evaluation benchmarks, the model is intended for tasks such as:
*   Multi-subject question answering (e.g., MMLU, C-Eval) (Paper: Section 3.2.1, p. 14).
*   Language understanding and reasoning (e.g., HellaSwag, ARC, BBH) (Paper: Section 3.2.1, p. 14).
*   Reading comprehension (e.g., RACE, DROP, CMRC) (Paper: Section 3.2.1, p. 14).
*   Mathematical reasoning (e.g., GSM8K, MATH) (Paper: Section 3.2.1, p. 14).
*   Code generation and understanding (e.g., HumanEval, MBPP) (Paper: Section 3.2.1, p. 14).

The chat-finetuned versions are specifically intended for conversational AI and instruction-following tasks (Paper: Section 4, p. 16). The model takes text as input and generates text as output.

### Primary intended users:
The model is released to the open-source community to "facilitate further research and development" (Paper: p. 5). Therefore, the primary intended users are AI researchers, developers, and practitioners who build applications on top of large language models.

### Out-of-scope uses:
The model is designed exclusively for the text modality and does not support other modalities like images or audio (Paper: Section 5, p. 21).

Additionally, the license explicitly prohibits the following uses (LICENSE, Attachment A):
*   Any use that violates applicable laws or regulations.
*   Any military use.
*   Exploiting or harming minors.
*   Generating or disseminating verifiably false information with the purpose of harming others.
*   Generating or disseminating personal identifiable information without authorization.
*   Defaming, disparaging, or harassing others.
*   Fully automated decision-making that adversely impacts an individual’s legal rights.
*   Discriminating against or harming individuals or groups based on social behavior or personal characteristics.
*   Exploiting vulnerabilities of a specific group of people to cause physical or psychological harm.

---

## How to Use
This section outlines how to use the model.

The model can be loaded and used with the Hugging Face `transformers` library. Below is an example of how to use the chat model for a conversational task.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Specify the model path
model_path = "deepseek-ai/DeepSeek-V2-Chat"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
# For demonstration, loading with lower precision and on CPU.
# For better performance, use a GPU with appropriate memory.
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map='auto' # or 'cuda' if you have a GPU
)

# Create a conversation history
messages = [
    {"role": "user", "content": "Hello, what can you do?"}
]

# Apply the chat template and tokenize the input
input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")

# Generate a response
outputs = model.generate(input_tensor.to(model.device), max_new_tokens=100)

# Decode and print the response
response = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)
print(response)
```

**Sample Output:**
```
I am DeepSeek-V2, a large language model developed by DeepSeek AI. I can help you with a wide range of tasks, including:

1.  **Answering questions:** I can provide information on various topics, from science and history to current events.
2.  **Writing and content creation:** I can help you draft emails, write articles, create stories, and more.
3.  **Coding assistance:** I can help you write, debug, and explain code in various programming languages.
4.  **Translation:** I can translate text between different languages.
5.  **Summarization:** I can summarize long documents or articles for you.
6.  **Brainstorming:** I can help you generate ideas for projects, stories, or any other creative endeavor.

How can I assist you today?
```
The chat template is defined in `tokenizer_config.json` and follows a specific format for user and assistant roles (tokenizer_config.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is pretrained on a bilingual corpus of English and Chinese. Its performance may be limited in other languages (Paper: Section 3.2.1, p. 13; Section 5, p. 21).
*   **Cultural Context:** The pre-training data was filtered to remove "contentious content, such as values influenced by regional cultures" to avoid subjective biases. This may affect the model's performance on tasks that are closely associated with specific cultural values (e.g., American values in the Humanity-Moral subset of MMLU) (Paper: Appendix E, p. 32).

### Evaluation factors:
*   **Language:** The model's performance is evaluated and reported separately on a wide range of benchmarks in both English and Chinese (Paper: Table 2, p. 15).
*   **Cultural Context:** The paper includes a discussion on the model's performance on value-sensitive test sets, indicating this was a factor considered during evaluation (Paper: Appendix E, p. 32).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of metrics depending on the evaluation benchmark (Paper: Table 2, p. 15):
*   **Accuracy (Acc.)**: Used for multiple-choice question answering tasks (e.g., MMLU, ARC, C-Eval).
*   **Exact Match (EM)**: Used for question answering and reasoning tasks where the generated answer must exactly match the ground truth (e.g., TriviaQA, GSM8K, CMRC).
*   **F1 Score**: Used for reading comprehension tasks like DROP, where partial credit is given.
*   **Pass@1**: Used for code generation tasks (e.g., HumanEval, MBPP) to measure the percentage of problems for which the first generated solution passes all unit tests.
*   **Bits-Per-Byte (BPB)**: Used for language modeling tasks (e.g., Pile-test) to measure the model's compression ability, ensuring a fair comparison across different tokenizers.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of public benchmarks in English and Chinese. The specific datasets are listed below (Paper: Section 3.2.1, p. 14):
*   **Multi-subject multiple-choice:** MMLU, C-Eval, CMMLU.
*   **Language understanding and reasoning:** HellaSwag, PIQA, ARC, BigBench Hard (BBH).
*   **Closed-book question answering:** TriviaQA, NaturalQuestions.
*   **Reading comprehension:** RACE, DROP, C3, CMRC.
*   **Reference disambiguation:** WinoGrande, CLUEWSC.
*   **Language modeling:** Pile.
*   **Chinese understanding and culture:** CHID, CCPM.
*   **Math:** GSM8K, MATH, CMath.
*   **Code:** HumanEval, MBPP, CRUXEval.
*   **Standardized exams:** AGIEval (both English and Chinese subsets).
*   **Open-ended conversation:** MT-Bench, AlpacaEval 2.0, AlignBench.

### Motivation:
The datasets were chosen to provide a comprehensive evaluation of the model's capabilities across a wide range of tasks and in both English and Chinese, reflecting its bilingual pre-training corpus (Paper: Section 3.2.1, p. 13).

### Preprocessing:
The paper states that all models were evaluated using an internal evaluation framework to ensure a consistent evaluation setting (Paper: Section 3.2.2, p. 14). Two main evaluation methods were used depending on the dataset (Paper: Section 3.2.1, p. 14):
*   **Perplexity-based evaluation:** For datasets like HellaSwag, PIQA, MMLU, and C-Eval.
*   **Generation-based evaluation:** For datasets like TriviaQA, GSM8K, HumanEval, and MATH.
Specific preprocessing steps for each dataset are not detailed.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on a high-quality, multi-source corpus of **8.1 trillion tokens** (Paper: Abstract, p. 1). This corpus is an extension of the one used for DeepSeek 67B, with an increased amount of data, particularly Chinese data, to better leverage the corpus available on the Chinese internet (Paper: Section 3.1.1, p. 11). The corpus is bilingual, with Chinese tokens being approximately 12% more than English ones (Paper: Section 3.1.1, p. 12).

### Motivation:
The choice of datasets was motivated by the goal of creating a strong bilingual model. The data was expanded and curated to improve data quality and better represent both English and Chinese languages (Paper: Section 3.1.1, p. 11).

### Preprocessing:
The data underwent several processing stages to improve its quality (Paper: Section 3.1.1, p. 11):
*   **Cleaning:** Optimized cleaning processes were used to recover a large amount of mistakenly deleted data from internet sources.
*   **Quality Filtering:** An improved quality-based filtering algorithm was applied to remove non-beneficial data while retaining valuable data.
*   **Debiasing:** Contentious content and material reflecting specific regional cultures were filtered out to mitigate data bias.
*   **Tokenization:** The text was tokenized using the same Byte-level Byte-Pair Encoding (BBPE) tokenizer as DeepSeek 67B, with a vocabulary size of 102,400 (Paper: Section 3.1.1, p. 12; config.json).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results are disaggregated by language (English and Chinese). Table 2 in the academic paper presents a detailed breakdown of the model's performance on various benchmarks for each language, compared against other open-source models (Paper: Table 2, p. 15).

**English Benchmarks (selected results from Table 2):**
*   **MMLU (5-shot Acc.):** 78.5
*   **BBH (3-shot EM):** 78.9
*   **HumanEval (Pass@1):** 48.8
*   **GSM8K (8-shot EM):** 79.2

**Chinese Benchmarks (selected results from Table 2):**
*   **C-Eval (5-shot Acc.):** 81.7
*   **CMMLU (5-shot Acc.):** 84.0
*   **CMRC (1-shot EM):** 77.5
*   **CCPM (0-shot Acc.):** 93.1

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights on disk is **439.103 GB** (model.safetensors.index.json). Loading the model in `bfloat16` precision would require a similar amount of VRAM.

### Deploying Requirements:
For efficient deployment, the paper describes a setup using a single node with **8 NVIDIA H800 GPUs**. The model parameters are converted to **FP8 precision**, and the KV cache is quantized to an average of **6 bits per element**. This setup achieves a generation throughput exceeding 50K tokens per second (Paper: Section 3.2.3, p. 16).

### Training or Fine-tuning Requirements:
The model was trained on a cluster equipped with **NVIDIA H800 GPUs** (Paper: Section 3.1.3, p. 13). The training framework utilized a combination of parallelism strategies to manage the model's size and computational cost (Paper: Section 3.1.3, p. 12):
*   16-way zero-bubble pipeline parallelism
*   8-way expert parallelism
*   ZeRO-1 data parallelism
The paper notes that due to the model's relatively few activated parameters, tensor parallelism was not necessary, which reduced communication overhead (Paper: Section 3.1.3, p. 12).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

**Data and Bias Mitigation:**
*   The developers identified and filtered "contentious content" from the pre-training data, specifically values influenced by regional cultures, to avoid the model exhibiting "unnecessary subjective biases" (Paper: Appendix E, p. 32). This effort was made to mitigate data bias introduced from specific cultures (Paper: Section 3.1.1, p. 11).
*   The model may contain personal information and works with IP rights from its training data. The license states that the user is an independent personal information processor and is solely responsible for ensuring compliance with relevant legal requirements when handling such information (LICENSE, Section 9).

**Risks and Prohibited Uses:**
*   The model shares limitations common to other LLMs, including the potential to generate non-factual or unverified information (hallucinations) (Paper: Section 5, p. 21).
*   The license explicitly prohibits use cases that pose significant ethical risks. These include, but are not limited to: military applications, harming minors, generating disinformation to harm others, harassment, unauthorized use of personal information, and creating systems for discriminatory automated decision-making (LICENSE, Attachment A).

**Alignment Efforts:**
*   The alignment team's stated goal is to develop a model that is "not only helpful but also honest and safe for worldwide users" and to "align the values of our model with human values" (Paper: Section 5, p. 21). This indicates an ongoing effort to address safety and ethical challenges.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Knowledge Cutoff:** The model lacks ongoing knowledge updates after pre-training, so its information may not be current (Paper: Section 5, p. 21).
*   **Hallucinations:** The model may generate non-factual information or produce hallucinations, a common issue in current LLMs (Paper: Section 5, p. 21).
*   **Language Proficiency:** The model's training data primarily consists of Chinese and English content. It may exhibit limited proficiency in other languages and should be used with caution in scenarios beyond Chinese and English (Paper: Section 5, p. 21).
*   **Cultural Bias:** Despite efforts to debias the training data, the model's responses may still be influenced by the cultural contexts present in the remaining data. Its performance on value-sensitive topics may vary (Paper: Appendix E, p. 32).

### Recommendations:
*   Users should be aware of the model's limitations and verify critical information generated by the model, especially in high-stakes domains.
*   It is strongly recommended to adhere to the use-based restrictions outlined in the license to prevent misuse and potential harm (LICENSE, Attachment A).
*   For applications in languages other than English and Chinese, thorough testing is recommended to assess the model's performance and suitability.
*   The developers intend for the model to be used in a way that has a "positive and beneficial impact on society." Users are encouraged to prioritize ethical considerations and responsible development in their applications (Paper: Section 5, p. 21).