## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by DeepSeek-AI (2405.04434.pdf, p. 1).

### Model date:
The associated academic paper was first submitted in May 2024 and a revised version was released on June 19, 2024 (2405.04434.pdf, p. 1).

### Model version:
This is DeepSeek-V2. It is a successor to DeepSeek 67B, offering stronger performance, 42.5% lower training costs, a 93.3% smaller KV cache, and 5.76 times the maximum generation throughput (2405.04434.pdf, p. 1).

### Model type:
DeepSeek-V2 is a large language model based on a Mixture-of-Experts (MoE) Transformer architecture (2405.04434.pdf, p. 1, 4).

*   **Architecture Details:** The model features innovative architectural components:
    *   **Multi-head Latent Attention (MLA):** An attention mechanism that uses low-rank key-value joint compression to significantly reduce the size of the KV cache during inference, boosting efficiency (2405.04434.pdf, p. 4, 6).
    *   **DeepSeekMoE:** A high-performance MoE architecture that segments experts into finer granularity and isolates shared experts to mitigate knowledge redundancy, enabling the training of strong models at a lower cost (2405.04434.pdf, p. 4, 9).
    *   The model uses DeepseekV2RMSNorm for layer normalization and Rotary Position Embedding (RoPE) (modeling_deepseek.py; 2405.04434.pdf, p. 8).
*   **Model Size:** It has a total of 236 billion parameters, of which 21 billion are activated for each token (2405.04434.pdf, p. 1). The model's total size on disk is approximately 439.1 GB (model.safetensors.index.summary.json.txt).
*   **Context Length:** The model supports a context length of 128,000 tokens (2405.04434.pdf, p. 1). The tokenizer configuration specifies a `model_max_length` of 16384, which was extended to 128K using YaRN (tokenizer_config.json.txt; 2405.04434.pdf, p. 13).
*   **Tokenizer:** The model uses a Byte-level Byte-Pair Encoding (BBPE) tokenizer with a vocabulary size of 100,000 (2405.04434.pdf, p. 12; tokenizer_summary.json.txt).

### Training details:
The model underwent a multi-stage training process: pre-training, supervised fine-tuning (SFT), and reinforcement learning (RL) (2405.04434.pdf, p. 1).

*   **Pre-training:**
    *   **Algorithm:** The model was pre-trained on a corpus of 8.1 trillion tokens (2405.04434.pdf, p. 1).
    *   **Optimizer:** AdamW optimizer was used with β1 = 0.9, β2 = 0.95, and a weight decay of 0.1 (2405.04434.pdf, p. 12).
    *   **Learning Rate:** A warmup-and-step-decay schedule was used, with the learning rate linearly increasing from 0 to a maximum of 2.4 × 10⁻⁴ during the first 2,000 steps, followed by two decays (2405.04434.pdf, p. 12).
    *   **Batch Size:** A scheduling strategy was employed where the batch size gradually increased from 2,304 to 9,216 sequences (2405.04434.pdf, p. 12).
*   **Alignment:**
    *   **Supervised Fine-Tuning (SFT):** The model was fine-tuned on 1.5 million instruction-following instances (1.2M for helpfulness, 0.3M for safety) for 2 epochs (2405.04434.pdf, p. 16).
    *   **Reinforcement Learning (RL):** Group Relative Policy Optimization (GRPO) was used to further align the model with human preferences, using a two-stage strategy focusing first on reasoning (code and math) and then on general human preference (2405.04434.pdf, p. 17).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model's architecture, training, and evaluation:
*   **Paper:** DeepSeek-AI. (2024). *DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model*. arXiv:2405.04434v5 [cs.CL]. This paper provides a comprehensive overview of the model's architecture (MLA and DeepSeekMoE), training process, dataset construction, and extensive evaluation results (2405.04434.pdf).
*   **Repository:** The model checkpoints are available at `https://github.com/deepseek-ai/DeepSeek-V2` (2405.04434.pdf, p. 1).

### Citation details:
Insufficient information.

### License:
The model is governed by the DEEPSEEK LICENSE AGREEMENT, Version 1.0 (LICENSE.txt).

*   **Permissions:** The license grants a worldwide, non-exclusive, royalty-free copyright and patent license to use, reproduce, prepare derivative works, and distribute the model and complementary materials (LICENSE.txt, Section II).
*   **Conditions:** When distributing the model or its derivatives, you must include a copy of the license and retain all original copyright and patent notices. You must also include the use-based restrictions as an enforceable provision in any legal agreement governing the use of the model (LICENSE.txt, Section III, Para 4).
*   **Restrictions:** The license includes a set of use-based restrictions in "Attachment A". You may not use the model or its derivatives for purposes that include:
    *   Violating any applicable laws or regulations.
    *   Any military use.
    *   Exploiting or harming minors.
    *   Generating or disseminating verifiably false information to harm others.
    *   Defaming, disparaging, or harassing others.
    *   Discriminating against or harming individuals or groups based on legally protected characteristics or social behavior (LICENSE.txt, Attachment A).

### Contact:
For questions or feedback, contact the developers at `research@deepseek.com` (2405.04434.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
DeepSeek-V2 is a powerful, open-source language model designed for general-purpose text generation. It demonstrates top-tier performance on a wide range of benchmarks in both English and Chinese (2405.04434.pdf, p. 4). Its primary capabilities include:
*   **Bilingual Understanding and Generation:** The model is pretrained on a large bilingual corpus, making it highly proficient in both English and Chinese tasks (2405.04434.pdf, p. 13-14).
*   **Reasoning and Problem Solving:** The model shows strong performance on math and code generation benchmarks (2405.04434.pdf, p. 15).
*   **Conversational AI:** The fine-tuned chat versions (DeepSeek-V2 Chat) are designed for instruction-following and conversational tasks, achieving strong performance on open-ended conversation benchmarks like MT-Bench and AlpacaEval 2.0 (2405.04434.pdf, p. 16, 19).

The model takes text as input and generates text as output. The chat version follows a specific template for multi-turn conversations (tokenizer_config.json.txt).

### Primary intended users:
The primary intended users are AI researchers, developers, and practitioners who can use the open-source model to build applications, conduct research, and further the understanding of large-scale language models (2405.04434.pdf, p. 5).

### Out-of-scope uses:
The model is not intended for any use that violates the use-based restrictions outlined in the license. These include, but are not limited to:
*   Any military applications (LICENSE.txt, Attachment A).
*   Generating or spreading misinformation with the intent to harm (LICENSE.txt, Attachment A).
*   Activities that involve harassment, discrimination, or exploitation of vulnerable groups (LICENSE.txt, Attachment A).
*   Applications requiring factual accuracy without human oversight, as the model may produce non-factual information or hallucinations (2405.04434.pdf, p. 21).
*   High-stakes applications in languages other than English and Chinese, as the model's proficiency in other languages may be limited (2405.04434.pdf, p. 21).

---

## How to Use
This section outlines how to use the model.

The provided repository files do not contain a direct code snippet for running the model. However, the `tokenizer_config.json` file specifies a chat template for conversational use with the fine-tuned versions of the model. This template structures the conversation between a user, an assistant, and an optional system prompt.

**Chat Template:**
```jinja
{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{{ bos_token }}{% for message in messages %}{% if message['role'] == 'user' %}{{ 'User: ' + message['content'] + '\n\n' }}{% elif message['role'] == 'assistant' %}{{ 'Assistant: ' + message['content'] + eos_token }}{% elif message['role'] == 'system' %}{{ message['content'] + '\n\n' }}{% endif %}{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}
```
(tokenizer_config.json.txt)

This template formats a list of messages, each with a `role` ('user', 'assistant', or 'system') and `content`. It adds special tokens (`bos_token`, `eos_token`) and role identifiers ('User:', 'Assistant:') to create a single string for the model input.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is primarily trained on English and Chinese data. Its performance is strongest in these two languages and may be limited in others (2405.04434.pdf, p. 12, 21).
*   **Cultural Context:** The developers made efforts to filter contentious content and reduce bias from specific regional cultures during data preprocessing. This may affect the model's performance on value-sensitive test sets that are closely associated with a particular culture (e.g., American values in the MMLU Humanity-Moral subset) (2405.04434.pdf, p. 11, 32).

### Evaluation factors:
The model's evaluation was disaggregated across several factors:
*   **Language:** Performance is reported separately on a wide range of English and Chinese benchmarks (2405.04434.pdf, p. 15, Table 2).
*   **Task Domain:** Results are grouped by domain, including general language understanding, mathematics, and code generation (2405.04434.pdf, p. 15, Table 2).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard metrics tailored to different tasks:
*   **Accuracy (Acc.):** Used for multiple-choice question answering benchmarks like MMLU, C-Eval, CMMLU, and ARC (2405.04434.pdf, p. 15, Table 2).
*   **Exact Match (EM):** Used for generation tasks where a precise answer is expected, such as TriviaQA, GSM8K, and MATH (2405.04434.pdf, p. 15, Table 2).
*   **F1 Score:** Used for the DROP reading comprehension benchmark, which measures the harmonic mean of precision and recall (2405.04434.pdf, p. 15, Table 2).
*   **Pass@1:** Used to evaluate code generation capabilities on benchmarks like HumanEval and MBPP, measuring the percentage of problems for which at least one generated solution passes the unit tests (2405.04434.pdf, p. 15, Table 2).
*   **Bits-Per-Byte (BPB):** Used for language modeling evaluation on the Pile-test dataset to ensure a fair comparison across models with different tokenizers (2405.04434.pdf, p. 14).
*   **Open-ended Generation Scores:** For chat models, performance was measured using scores from benchmarks like MT-Bench, AlpacaEval 2.0 (length-controlled win rate), and AlignBench, which often use stronger models like GPT-4 as judges (2405.04434.pdf, p. 19-20).

### Decision thresholds:
Insufficient information. This is not typically applicable to generative language models.

### Variation approaches:
The evaluations were conducted using few-shot learning approaches, where the number of examples provided in the prompt was specified for each benchmark. The number of shots varied from 0-shot to 25-shot depending on the specific dataset and task (2405.04434.pdf, p. 15, Table 2).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of public benchmarks covering various capabilities in English and Chinese. These include:
*   **Multi-subject Multiple-Choice:** MMLU, C-Eval, CMMLU (2405.04434.pdf, p. 14).
*   **Language Understanding and Reasoning:** HellaSwag, PIQA, ARC, BigBench Hard (BBH), WinoGrande (2405.04434.pdf, p. 14).
*   **Question Answering:** TriviaQA, NaturalQuestions (2405.04434.pdf, p. 14).
*   **Reading Comprehension:** RACE, DROP, C3, CMRC (2405.04434.pdf, p. 14).
*   **Math:** GSM8K, MATH, CMath (2405.04434.pdf, p. 14).
*   **Code:** HumanEval, MBPP, CRUXEval (2405.04434.pdf, p. 14).
*   **Chinese Language & Culture:** CHID, CCPM, CLUEWSC (2405.04434.pdf, p. 14).
*   **Standardized Exams:** AGIEval (2405.04434.pdf, p. 14).
*   **Open-ended Conversation:** MT-Bench, AlpacaEval 2.0, AlignBench (2405.04434.pdf, p. 16).

### Motivation:
These datasets were chosen to provide a thorough evaluation of the model's capabilities across a wide range of tasks and to allow for direct comparison with other leading open-source models in both English and Chinese (2405.04434.pdf, p. 4, 14).

### Preprocessing:
The evaluation methodology varied by dataset. Some datasets (like MMLU and HellaSwag) used perplexity-based evaluation, while others (like TriviaQA and GSM8K) used generation-based evaluation. For the Pile language modeling benchmark, Bits-Per-Byte (BPB) was used as the metric to ensure a fair comparison among models with different tokenizers (2405.04434.pdf, p. 14).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
*   **Pre-training Data:** The model was pre-trained on a high-quality, multi-source corpus consisting of 8.1 trillion tokens. The dataset is bilingual, with a focus on English and Chinese; Chinese tokens make up approximately 12% more of the corpus than English tokens (2405.04434.pdf, p. 4, 11-12).
*   **Alignment Data:** For supervised fine-tuning (SFT), a dataset of 1.5 million instances was curated, comprising 1.2 million for helpfulness and 300,000 for safety. For reinforcement learning (RL), preference data was collected for code (based on compiler feedback), math (based on ground-truth labels), and general helpfulness/safety (2405.04434.pdf, p. 16-17).

### Motivation:
The pre-training dataset was constructed to build a powerful bilingual foundation model. Compared to the data used for DeepSeek 67B, this corpus was expanded with more data, particularly Chinese data, and the overall quality was improved to enhance model performance (2405.04434.pdf, p. 11). The alignment data was curated to improve helpfulness, safety, and instruction-following capabilities (2405.04434.pdf, p. 16).

### Preprocessing:
The data processing pipeline was an extension of the one used for DeepSeek 67B. Key steps included:
*   Optimizing data cleaning processes to recover valuable data that might have been mistakenly deleted (2405.04434.pdf, p. 11).
*   Improving the quality-based filtering algorithm to better remove non-beneficial data while retaining valuable content (2405.04434.pdf, p. 11).
*   Filtering out contentious content to mitigate data bias introduced from specific regional cultures (2405.04434.pdf, p. 11).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was extensively benchmarked against other leading open-source models. The results are presented in tables disaggregated by individual benchmarks. For example, on the 5-shot MMLU benchmark, DeepSeek-V2 achieved an accuracy of 78.5% (2405.04434.pdf, p. 15, Table 2). On 8-shot GSM8K, it scored 79.2% EM (2405.04434.pdf, p. 15, Table 2).

**Performance on Key Benchmarks (Base Model):**
| Benchmark | Metric | # Shots | DeepSeek-V2 Score |
| :--- | :--- | :--- | :--- |
| MMLU | Acc. | 5-shot | 78.5 |
| BBH | EM | 3-shot | 78.9 |
| GSM8K | EM | 8-shot | 79.2 |
| MATH | EM | 4-shot | 43.6 |
| HumanEval | Pass@1 | 0-shot | 48.8 |
| C-Eval | Acc. | 5-shot | 81.7 |
| CMMLU | Acc. | 5-shot | 84.0 |
(Source: 2405.04434.pdf, p. 15, Table 2)

### Intersectional results:
The evaluation results are presented in groups based on language (English, Chinese) and domain (Code, Math), allowing for an intersectional analysis of the model's capabilities. For instance, the model's performance on Chinese benchmarks like C-Eval (81.7%) and CMMLU (84.0%) is reported alongside its performance on English benchmarks like MMLU (78.5%) (2405.04434.pdf, p. 15, Table 2). The paper also includes a specific analysis of the MMLU Humanity-Moral subset, discussing how the model's performance is influenced by cultural factors and the data debiasing process (2405.04434.pdf, p. 32).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is 439.103 GB, distributed across 55 shards. Loading the model would require at least this amount of RAM or a combination of CPU and GPU memory sufficient to hold the parameters (model.safetensors.index.summary.json.txt).

### Deploying Requirements:
The model is designed for efficient inference.
*   **KV Cache:** The Multi-head Latent Attention (MLA) architecture reduces the KV cache size by 93.3% compared to a dense model of similar capability (DeepSeek 67B) (2405.04434.pdf, p. 1).
*   **Quantization:** For deployment, the model's parameters are converted to FP8 precision, and the KV cache is quantized to an average of 6 bits per element (2405.04434.pdf, p. 16).
*   **Throughput:** On a single node with 8 NVIDIA H800 GPUs, the deployed model can achieve a generation throughput exceeding 50,000 tokens per second (2405.04434.pdf, p. 16).

### Training or Fine-tuning Requirements:
*   **Hardware:** The model was trained on a cluster equipped with NVIDIA H800 GPUs, with 8 GPUs per node connected via NVLink and NVSwitch (2405.04434.pdf, p. 13).
*   **Parallelism:** The training framework utilized a 16-way zero-bubble pipeline parallelism, an 8-way expert parallelism, and ZeRO-1 data parallelism (2405.04434.pdf, p. 12).
*   **Training Cost:** Training the model on one trillion tokens requires 172.8K GPU hours, which is 42.5% less than the cost for the dense DeepSeek 67B model (2405.04434.pdf, p. 16).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Filtering and Debiasing:** During pre-training data preparation, the developers identified and filtered out contentious content, such as values influenced by specific regional cultures, to avoid the model exhibiting unnecessary subjective biases (2405.04434.pdf, p. 11, 32).
*   **Risk Mitigation through Licensing:** The model is released with a license that includes a comprehensive set of use-based restrictions to prevent misuse. Prohibited uses include military applications, generating harmful misinformation, harassment, and discrimination, thereby providing a legal framework to enforce responsible use (LICENSE.txt, Attachment A).
*   **Safety Alignment:** The supervised fine-tuning stage included 300,000 instances specifically curated for safety to align the model's behavior with safety guidelines (2405.04434.pdf, p. 16).
*   **Acknowledged Risks:** The developers acknowledge risks common to all large language models, including the potential to generate non-factual or unverified information (hallucinations). Since the training data is primarily Chinese and English, the model may have limited proficiency and could produce lower-quality or biased outputs in other languages (2405.04434.pdf, p. 21).
*   **Personal Information:** The license notes that the model may contain personal information and that the user is solely responsible for complying with applicable laws and regulations regarding its handling (LICENSE.txt, Section IV, Para 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Static Knowledge:** The model's knowledge is frozen at the end of its training period and is not updated with new information from the real world (2405.04434.pdf, p. 21).
*   **Hallucination Risk:** Like other LLMs, DeepSeek-V2 can generate non-factual information, unverified advice, and produce hallucinations. It should not be relied upon for factually critical applications without human verification (2405.04434.pdf, p. 21).
*   **Language Limitations:** The model's training data is primarily composed of Chinese and English content. Consequently, it may exhibit limited proficiency and reliability in other languages (2405.04434.pdf, p. 21).
*   **Alignment Tax:** The process of aligning the model with human preferences through reinforcement learning can sometimes negatively impact performance on certain standard academic benchmarks (a phenomenon known as "alignment tax") (2405.04434.pdf, p. 20).

### Recommendations:
*   **Use with Caution:** The model should be used with caution in scenarios beyond Chinese and English due to potential performance limitations (2405.04434.pdf, p. 21).
*   **Adhere to License:** All users must comply with the use-based restrictions outlined in the DEEPSEEK LICENSE AGREEMENT to ensure responsible and ethical application of the model (LICENSE.txt).
*   **Human Oversight:** For applications where factual accuracy is important, human oversight and verification of the model's outputs are strongly recommended.