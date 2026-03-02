## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by DeepSeek-AI (2405.04434.pdf, p. 1). DeepSeek is defined as Beijing DeepSeek Artificial Intelligence Fundamental Technology Research Co., Ltd., Hangzhou DeepSeek Artificial Intelligence Fundamental Technology Research Co., Ltd. and/or any of their affiliates (LICENSE.txt, Section 1).

### Model date:
The associated academic paper was last updated on June 19, 2024 (2405.04434.pdf, p. 1). The license agreement is dated October 23, 2023 (LICENSE.txt).

### Model version:
This model is DeepSeek-V2 (2405.04434.pdf, p. 1). It is an innovative Mixture-of-Experts (MoE) model that differs from the previous dense model, DeepSeek 67B. Compared to DeepSeek 67B, DeepSeek-V2 saves 42.5% of training costs, reduces the Key-Value (KV) cache by 93.3%, and boosts the maximum generation throughput by 5.76 times, while achieving stronger performance (2405.04434.pdf, p. 1, 4). A smaller version, DeepSeek-V2-Lite, has also been released (2405.04434.pdf, p. 5).

### Model type:
DeepSeek-V2 is a Mixture-of-Experts (MoE) Transformer-based language model designed for causal language modeling (2405.04434.pdf, p. 1; config.json.txt).

*   **Architecture:** The model uses an innovative architecture featuring Multi-head Latent Attention (MLA) and DeepSeekMoE (2405.04434.pdf, p. 1).
    *   **Multi-head Latent Attention (MLA):** An attention mechanism with low-rank key-value joint compression to significantly reduce the KV cache size during inference, boosting efficiency (2405.04434.pdf, p. 4, 6).
    *   **DeepSeekMoE:** A high-performance MoE architecture that enables training strong models at an economical cost. It uses fine-grained expert segmentation and shared expert isolation (2405.04434.pdf, p. 4, 9). All Feed-Forward Networks (FFNs) except for the first layer are replaced with MoE layers (2405.04434.pdf, p. 12).
*   **Size and Parameters:**
    *   **Total Parameters:** 236B (2405.04434.pdf, p. 1).
    *   **Activated Parameters:** 21B are activated for each token (2405.04434.pdf, p. 1).
    *   **Total Size:** 439.103 GB (model.safetensors.index.summary.json.txt).
*   **Key Specifications:**
    *   **Layers:** 60 Transformer layers (config.json.txt; 2405.04434.pdf, p. 12).
    *   **Hidden Size:** 5120 (config.json.txt).
    *   **Attention Heads:** 128 (config.json.txt).
    *   **Vocabulary Size:** 102,400, using a Byte-level Byte-Pair Encoding (BBPE) tokenizer (config.json.txt; 2405.04434.pdf, p. 12).
    *   **Context Length:** Supports a context length of 128K tokens, extended from an initial 4K using the YaRN method (2405.04434.pdf, p. 1, 13). The configuration file specifies a `max_position_embeddings` of 163,840 (config.json.txt).
*   **MoE Details:**
    *   Each MoE layer consists of 2 shared experts and 160 routed experts (config.json.txt; 2405.04434.pdf, p. 12).
    *   6 experts are activated per token (config.json.txt; 2405.04434.pdf, p. 12).
    *   The intermediate hidden dimension of each expert is 1536 (config.json.txt; 2405.04434.pdf, p. 12).

### Training details:
The model was pretrained and then aligned using Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) (2405.04434.pdf, p. 1).

*   **Pre-training Algorithm:** The model was trained using the AdamW optimizer (2405.04434.pdf, p. 12).
*   **Pre-training Hyperparameters:**
    *   **Optimizer:** AdamW with β1 = 0.9, β2 = 0.95, and weight_decay = 0.1 (2405.04434.pdf, p. 12).
    *   **Learning Rate:** A warmup-and-step-decay schedule was used, with a maximum learning rate of 2.4 × 10⁻⁴ (2405.04434.pdf, p. 12).
    *   **Batch Size:** A scheduling strategy was used, gradually increasing the batch size from 2304 to 9216 sequences (2405.04434.pdf, p. 12).
    *   **Sequence Length:** The maximum sequence length during pre-training was 4K (2405.04434.pdf, p. 12).
    *   **Gradient Clipping:** The gradient clipping norm was set to 1.0 (2405.04434.pdf, p. 12).
*   **MoE Training Methodologies:**
    *   **Load Balancing:** Three auxiliary losses were used to control expert-level, device-level, and communication load balance (2405.04434.pdf, p. 10). The loss coefficients were α1=0.003, α2=0.05, and α3=0.02 (2405.04434.pdf, p. 12).
    *   **Routing:** A device-limited routing mechanism was used, where each token is sent to at most 3 devices (2405.04434.pdf, p. 12).
    *   **Token Dropping:** A device-level token-dropping strategy was employed during training to mitigate computation wastage from unbalanced loads (2405.04434.pdf, p. 11).
*   **Alignment:**
    *   **Supervised Fine-Tuning (SFT):** The model was fine-tuned for 2 epochs on a dataset of 1.5M instances (1.2M for helpfulness, 0.3M for safety) (2405.04434.pdf, p. 16).
    *   **Reinforcement Learning (RL):** The Group Relative Policy Optimization (GRPO) algorithm was used to align the model with human preferences (2405.04434.pdf, p. 17).

### Paper or other resource for more information:
*   **Academic Paper:** The model is described in detail in the paper "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model" (2405.04434.pdf).
*   **Repository:** The model checkpoints are available at the official GitHub repository: https://github.com/deepseek-ai/DeepSeek-V2 (2405.04434.pdf, p. 1).

### Citation details:
```bibtex
@misc{deepseek_v2,
      title={DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, 
      author={DeepSeek-AI},
      year={2024},
      eprint={2405.04434},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(2405.04434.pdf)

### License:
The model is governed by the DEEPSEEK LICENSE AGREEMENT (Version 1.0, 23 October 2023) (LICENSE.txt).

*   **Permissions:** The license grants a perpetual, worldwide, non-exclusive, royalty-free, irrevocable copyright and patent license to reproduce, prepare, display, perform, sublicense, and distribute the model and its derivatives (LICENSE.txt, Section II).
*   **Conditions:** When distributing the model or its derivatives, you must include the use-based restrictions as an enforceable provision, provide a copy of the license, and retain all copyright and patent notices (LICENSE.txt, Section III, Para 4).
*   **Restrictions:** The license includes a set of use-based restrictions detailed in Attachment A. These prohibit using the model for purposes such as military use, generating verifiably false information to harm others, and discriminating against individuals or groups (LICENSE.txt, Attachment A).

### Contact:
For questions, issues, or feedback, contact the developers at `research@deepseek.com` (2405.04434.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
DeepSeek-V2 is a large language model intended for general-purpose text generation and understanding in both English and Chinese (2405.04434.pdf, p. 4, 13). Its capabilities have been evaluated on a wide range of tasks, including:
*   Language understanding and reasoning (2405.04434.pdf, p. 14).
*   Multi-subject question answering (2405.04434.pdf, p. 14).
*   Mathematical reasoning (2405.04434.pdf, p. 14).
*   Code generation and understanding (2405.04434.pdf, p. 14).
*   Conversational AI and chatbot applications (for the chat-tuned versions) (2405.04434.pdf, p. 16).

The model is also intended to facilitate further research and development in efficient and powerful language models, particularly those using Mixture-of-Experts (MoE) and novel attention mechanisms (2405.04434.pdf, p. 5).

The input-output structure for the chat model is defined by a template that formats conversations with "User:" and "Assistant:" roles (tokenizer_config.json.txt).

### Primary intended users:
The primary intended users are researchers, developers, and the open-source community who are interested in building with, and advancing the state of, large language models (2405.04434.pdf, p. 5; LICENSE.txt, Section I).

### Out-of-scope uses:
The model is not designed for and is explicitly restricted from being used for the following applications, as outlined in the license agreement:
*   Any use that violates applicable national or international laws or regulations (LICENSE.txt, Attachment A).
*   Military use in any way (LICENSE.txt, Attachment A).
*   Exploiting, harming, or attempting to exploit or harm minors (LICENSE.txt, Attachment A).
*   Generating or disseminating verifiably false information and/or content with the purpose of harming others (LICENSE.txt, Attachment A).
*   Generating or disseminating personal identifiable information without due authorization (LICENSE.txt, Attachment A).
*   Defaming, disparaging, or otherwise harassing others (LICENSE.txt, Attachment A).
*   Fully automated decision-making that adversely impacts an individual’s legal rights (LICENSE.txt, Attachment A).
*   Discriminating against or harming individuals or groups based on social behavior or personal characteristics (LICENSE.txt, Attachment A).

---

## How to Use
This section outlines how to use the model.

The following code snippet demonstrates how to load the DeepSeek-V2 model and tokenizer to generate text (modeling_deepseek.py, `DeepseekV2ForCausalLM` docstring).

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Specify the model repository ID
model_id = "deepseek-ai/DeepSeek-V2-Chat"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="auto")

# Create a conversation
messages = [
    {"role": "user", "content": "Hello, who are you?"}
]
# Apply the chat template
input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

# Generate a response
# The generation config is loaded from the repository
outputs = model.generate(**inputs, max_new_tokens=100)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)
```

**Sample Output:**
```
User: Hello, who are you?

Assistant: I am DeepSeek-V2, a large language model developed by DeepSeek AI. I am designed to be a helpful and harmless AI assistant. How can I help you today?
```

The chat template formats the conversation history. For example, a user message is prepended with `User: ` and an assistant message is prepended with `Assistant: ` and appended with the end-of-sentence token (tokenizer_config.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model was pretrained on a bilingual corpus of English and Chinese text. Its performance may be limited in other languages (2405.04434.pdf, p. 13, 21).
*   **Cultural Context:** The developers made efforts to filter contentious content and mitigate data bias from specific regional cultures during pre-training. This may affect the model's performance on test sets closely associated with specific cultural values (e.g., American values in the MMLU Humanity-Moral subset) (2405.04434.pdf, p. 11, 32).

### Evaluation factors:
The model's performance was evaluated and disaggregated by:
*   **Language:** The model was evaluated on a wide range of standard benchmarks in both English and Chinese (2405.04434.pdf, p. 15, Table 2).
*   **Task Domain:** Performance was reported separately for different domains, including English, Chinese, Math, and Code (2405.04434.pdf, p. 15, Table 2).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of metrics depending on the evaluation benchmark (2405.04434.pdf, p. 15, Table 2):
*   **Accuracy (Acc.)**: Used for multiple-choice and classification tasks like MMLU, ARC, and C-Eval.
*   **Exact Match (EM)**: Used for question-answering and reasoning tasks like TriviaQA, GSM8K, and MATH.
*   **F1 Score**: Used for reading comprehension tasks like DROP.
*   **Bits-Per-Byte (BPB)**: Used for language modeling evaluation on the Pile-test dataset.
*   **Pass@1**: Used for code generation tasks like HumanEval and MBPP.
*   **Open-ended Generation Scores**: For conversational benchmarks, metrics include MT-Bench score, length-controlled win rate on AlpacaEval 2.0, and overall score on AlignBench (2405.04434.pdf, p. 18-19).

### Decision thresholds:
Insufficient information

### Variation approaches:
Two main evaluation approaches were used (2405.04434.pdf, p. 14):
*   **Perplexity-based evaluation**: Used for datasets like HellaSwag, PIQA, WinoGrande, RACE, MMLU, and C-Eval.
*   **Generation-based evaluation**: Used for datasets like TriviaQA, NaturalQuestions, DROP, MATH, GSM8K, and HumanEval.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks in English and Chinese (2405.04434.pdf, p. 14):
*   **Multi-subject Multiple-choice:** MMLU, C-Eval, CMMLU.
*   **Language Understanding and Reasoning:** HellaSwag, PIQA, ARC, BigBench Hard (BBH).
*   **Closed-book Question Answering:** TriviaQA, NaturalQuestions.
*   **Reading Comprehension:** RACE, DROP, C3, CMRC.
*   **Reference Disambiguation:** WinoGrande, CLUEWSC.
*   **Language Modeling:** Pile.
*   **Chinese Understanding and Culture:** CHID, CCPM.
*   **Math:** GSM8K, MATH, CMath.
*   **Code:** HumanEval, MBPP, CRUXEval.
*   **Standardized Exams:** AGIEval (includes both English and Chinese subsets).
*   **Open-ended Conversation:** MT-Bench, AlpacaEval 2.0, AlignBench.

### Motivation:
The datasets were chosen to provide a comprehensive evaluation of the model's capabilities across a wide range of tasks and domains. Since the model was pretrained on a bilingual corpus, benchmarks in both English and Chinese were selected to assess its proficiency in both languages (2405.04434.pdf, p. 13).

### Preprocessing:
The evaluation formats for each benchmark are provided in the paper's appendix (2405.04434.pdf, p. 33). Depending on the dataset, either perplexity-based or generation-based evaluation was performed (2405.04434.pdf, p. 14). For some few-shot evaluations on chat models, the format constraints were not strictly adhered to, which may lead to underestimation of performance (2405.04434.pdf, p. 19, Table 3 caption).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
*   **Pre-training:** The model was pretrained on a high-quality, multi-source corpus of 8.1 trillion tokens. This corpus is an extension of the one used for DeepSeek 67B, with more data, especially Chinese data. Chinese tokens are approximately 12% more numerous than English tokens in the corpus (2405.04434.pdf, p. 1, 4, 12).
*   **Supervised Fine-Tuning (SFT):** For alignment, a dataset of 1.5 million instruction-following instances was curated, comprising 1.2 million instances for helpfulness and 0.3 million for safety (2405.04434.pdf, p. 16).
*   **Reinforcement Learning (RL):** Preference data was collected for RL training. Code preference data was based on compiler feedback, and mathematical preference data was based on ground-truth labels (2405.04434.pdf, p. 17).

### Motivation:
The pre-training corpus was constructed to extend the amount of data and elevate the data quality compared to previous models. More Chinese data was incorporated to "better leverage the corpus available on the Chinese internet" (2405.04434.pdf, p. 11). The alignment data was curated to improve helpfulness, safety, writing proficiency, and to mitigate hallucinatory responses (2405.04434.pdf, p. 16).

### Preprocessing:
*   **Filtering:** An improved quality-based filtering algorithm was used to remove non-beneficial data while retaining valuable data. Contentious content influenced by regional cultures was also filtered out to mitigate data bias (2405.04434.pdf, p. 11).
*   **Tokenization:** The data was tokenized using the same Byte-level Byte-Pair Encoding (BBPE) tokenizer as DeepSeek 67B, which has a vocabulary size of 100,000 (2405.04434.pdf, p. 12; tokenizer_summary.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is presented separately for different task domains and languages in the associated paper.
*   **Table 2 (p. 15)** shows performance across benchmarks categorized as English, Code, Math, and Chinese (2405.04434.pdf, p. 15).
*   **Table 3 (p. 19)** shows the performance of the chat-tuned versions on English and Chinese benchmarks (2405.04434.pdf, p. 19).
*   **Table 5 (p. 20)** presents results on the Chinese AlignBench, broken down by capability, including Fundamental Tasks, Chinese Understanding, Open-ended Questions, Writing, Role-playing, and Professional Ability (2405.04434.pdf, p. 20).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model has a total size of approximately 439.1 GB, which is the minimum disk space required to store the weights (model.safetensors.index.summary.json.txt). Loading the model requires significant RAM or VRAM, likely exceeding this amount depending on the data type (e.g., bfloat16).

### Deploying Requirements:
For efficient deployment, the paper suggests converting the model's parameters to FP8 precision and using KV cache quantization to compress each element to 6 bits on average. On a single node with 8 NVIDIA H800 GPUs, the deployed model can achieve a generation throughput exceeding 50,000 tokens per second (2405.04434.pdf, p. 16).

### Training or Fine-tuning Requirements:
*   **Hardware:** The model was trained on a cluster of NVIDIA H800 GPUs (2405.04434.pdf, p. 13).
*   **Parallelism:** The training framework used a 16-way zero-bubble pipeline parallelism, an 8-way expert parallelism, and ZeRO-1 data parallelism. Due to its architecture, the model can be trained without tensor parallelism, reducing communication overhead (2405.04434.pdf, p. 12).
*   **Training Cost:** Training the model on one trillion tokens requires 172.8K GPU hours on the H800 cluster (2405.04434.pdf, p. 16).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Bias Mitigation:** During pre-training data preparation, developers identified and filtered "contentious content, such as values influenced by regional cultures, to avoid our model exhibiting unnecessary subjective biases" (2405.04434.pdf, p. 32). This effort was made to mitigate data bias introduced from specific regional cultures (2405.04434.pdf, p. 11).
*   **Safety Alignment:** The Supervised Fine-Tuning (SFT) dataset included 0.3 million instances specifically for safety (2405.04434.pdf, p. 16). The alignment team's goal is to develop a model that is "not only helpful but also honest and safe for worldwide users" (2405.04434.pdf, p. 21).
*   **Risk Mitigation through Licensing:** The model's license explicitly prohibits use cases that are considered harmful. This includes military use, generating false information to harm others, exploiting minors, harassment, and discrimination. Downstream users are required to enforce these same restrictions in any legal agreements governing the use of the model or its derivatives (LICENSE.txt, Section III & Attachment A).
*   **Potential Risks and Harms:** The paper acknowledges limitations common to LLMs, including the potential to generate non-factual or unverified information and to produce hallucinations. Since the training data is primarily English and Chinese, the model may have limited proficiency and could perform poorly in other languages, which is a potential risk in multilingual applications (2405.04434.pdf, p. 21).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Knowledge Cutoff:** The model lacks ongoing knowledge updates after pre-training, so its information may not be current (2405.04434.pdf, p. 21).
*   **Hallucination and Factual Accuracy:** Like other LLMs, the model may generate non-factual information, unverified advice, or produce hallucinations (2405.04434.pdf, p. 21).
*   **Language Proficiency:** The model's proficiency is highest in English and Chinese. Performance in other languages may be limited (2405.04434.pdf, p. 21).
*   **Alignment Tax:** The process of aligning the model with human preferences through Reinforcement Learning can negatively impact performance on some standard benchmarks (a phenomenon known as "alignment tax") (2405.04434.pdf, p. 20).
*   **Value-Sensitivity:** The model's performance on value-sensitive topics may differ from other models due to the debiasing efforts in pre-training. For example, it may perform differently on subsets like the MMLU Humanity-Moral subset, which is associated with American values (2405.04434.pdf, p. 32).

### Recommendations:
*   Users should be cautious when using the model in scenarios beyond Chinese and English (2405.04434.pdf, p. 21).
*   Outputs from the model, especially those containing factual claims or advice, should be critically evaluated and verified by users.
*   Users and developers building on DeepSeek-V2 must adhere to the use-based restrictions outlined in the license to prevent misuse (LICENSE.txt, Attachment A).

---