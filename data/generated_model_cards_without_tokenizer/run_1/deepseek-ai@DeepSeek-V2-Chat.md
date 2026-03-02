## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by DeepSeek-AI (2405.04434.pdf, p. 1). The organization's contact email is research@deepseek.com (2405.04434.pdf, p. 1).

### Model date:
The paper describing the model was submitted to arXiv on May 7, 2024, with the latest revision on June 19, 2024 (2405.04434.pdf, p. 1).

### Model version:
This model is DeepSeek-V2. It is a Mixture-of-Experts (MoE) model that follows the previous release, DeepSeek 67B, which was a dense model. Compared to DeepSeek 67B, DeepSeek-V2 achieves stronger performance while saving 42.5% of training costs, reducing the Key-Value (KV) cache by 93.3%, and boosting the maximum generation throughput by 5.76 times (2405.04434.pdf, p. 1, 4).

### Model type:
DeepSeek-V2 is a strong, economical, and efficient Mixture-of-Experts (MoE) language model (2405.04434.pdf, p. 1). It is a Transformer-based decoder model intended for causal language modeling (modeling_deepseek.py; config.json.txt).

**Architecture Details:**
*   **Total Parameters:** 236B (2405.04434.pdf, p. 1).
*   **Activated Parameters:** 21B per token (2405.04434.pdf, p. 1).
*   **Model Size:** Approximately 439.1 GB (model.safetensors.index.summary.json.txt).
*   **Context Length:** Supports a context length of 128K tokens (2405.04434.pdf, p. 1). The `max_position_embeddings` is set to 163840 (config.json.txt).
*   **Layers:** 60 hidden layers (`num_hidden_layers`) (config.json.txt; 2405.04434.pdf, p. 12).
*   **Hidden Size:** 5120 (`hidden_size`) (config.json.txt).
*   **Vocabulary Size:** 102400 (`vocab_size`) (config.json.txt).
*   **Attention Mechanism:** The model uses an innovative architecture called Multi-head Latent Attention (MLA), which compresses the Key-Value (KV) cache into a latent vector to guarantee efficient inference (2405.04434.pdf, p. 1, 6).
    *   **Attention Heads:** 128 (`num_attention_heads`) (config.json.txt).
    *   **Key-Value Heads:** 128 (`num_key_value_heads`) (config.json.txt).
    *   **RoPE:** The model uses Rotary Position Embedding (RoPE) with a theta value of 10000 (config.json.txt). It employs YaRN scaling to extend the context window (config.json.txt; 2405.04434.pdf, p. 13).
*   **Feed-Forward Networks:** The model employs DeepSeekMoE, a high-performance MoE architecture. FFNs, except for the first layer, are substituted with MoE layers (2405.04434.pdf, p. 6, 9, 12).
    *   **Shared Experts:** 2 (`n_shared_experts`) (config.json.txt).
    *   **Routed Experts:** 160 (`n_routed_experts`) (config.json.txt).
    *   **Experts Activated per Token:** 6 (`num_experts_per_tok`) (config.json.txt).
    *   **Expert Routing:** Uses a "group_limited_greedy" top-k method with 8 groups (`n_group`) and selects from 3 groups (`topk_group`) per token (config.json.txt).
*   **Normalization:** DeepseekV2RMSNorm (modeling_deepseek.py).
*   **Activation Function:** SiLU ("silu") (config.json.txt).

### Training details:
The model was pretrained on a high-quality, multi-source corpus and then underwent Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) (2405.04434.pdf, p. 1).

**Pre-training:**
*   **Algorithm:** The model was trained using the AdamW optimizer with β1 = 0.9, β2 = 0.95, and weight_decay = 0.1 (2405.04434.pdf, p. 12).
*   **Data:** Trained on 8.1T tokens from a bilingual (English and Chinese) corpus (2405.04434.pdf, p. 1, 12).
*   **Hyperparameters:**
    *   The learning rate used a warmup-and-step-decay strategy, with a maximum learning rate of 2.4 × 10⁻⁴ (2405.04434.pdf, p. 12).
    *   Gradient clipping norm was set to 1.0 (2405.04434.pdf, p. 12).
    *   Batch size was gradually increased from 2304 to 9216 sequences (2405.04434.pdf, p. 12).
    *   Maximum sequence length during pre-training was 4K, later extended to 128K using YaRN (2405.04434.pdf, p. 12, 13).
*   **Hardware:** The model was trained on a cluster of NVIDIA H800 GPUs using the HAI-LLM framework, which employed a 16-way zero-bubble pipeline parallelism, an 8-way expert parallelism, and ZeRO-1 data parallelism (2405.04434.pdf, p. 12).

**Alignment:**
*   **Supervised Fine-Tuning (SFT):** The model was fine-tuned on 1.5M instances (1.2M for helpfulness, 0.3M for safety) for 2 epochs with a learning rate of 5 × 10⁻⁶ (2405.04434.pdf, p. 16).
*   **Reinforcement Learning (RL):** The model was aligned with human preference using Group Relative Policy Optimization (GRPO) in a two-stage process focusing first on reasoning (code and math) and then on general human preference (2405.04434.pdf, p. 17).

### Paper or other resource for more information:
The model is described in the academic paper "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model".
*   **arXiv Link:** https://arxiv.org/abs/2405.04434 (2405.04434.pdf)
*   **GitHub Repository:** https://github.com/deepseek-ai/DeepSeek-V2 (2405.04434.pdf, p. 1)

The paper provides a detailed description of the model's architecture (MLA and DeepSeekMoE), pre-training process, alignment techniques, and comprehensive evaluation results.

### Citation details:
```bibtex
@misc{deepseek2024deepseekv2,
      title={DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, 
      author={DeepSeek-AI},
      year={2024},
      eprint={2405.04434},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(Derived from 2405.04434.pdf)

### License:
The model is governed by the DeepSeek License Agreement, Version 1.0 (LICENSE.txt). The license aims to balance open access with responsible use.

*   **Permissions:** You are granted a perpetual, worldwide, non-exclusive, royalty-free, irrevocable copyright and patent license to reproduce, prepare, publicly display, perform, sublicense, and distribute the model, its derivatives, and complementary materials (LICENSE.txt, Section II).
*   **Conditions:** When distributing the model or its derivatives, you must include the use-based restrictions from the license, provide a copy of the license, and retain all original copyright and patent notices (LICENSE.txt, Section III, paragraph 4).
*   **Restrictions:** The license includes a list of "Use-based restrictions" in Attachment A, which must be included as an enforceable provision in any legal agreement governing the use or distribution of the model or its derivatives (LICENSE.txt, Section III, paragraph 4a, 5). These restrictions are detailed in the "Out-of-scope uses" section.

### Contact:
For questions, issues, or feedback, contact DeepSeek-AI at `research@deepseek.com` (2405.04434.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
DeepSeek-V2 is a large, open-source Mixture-of-Experts (MoE) language model designed for general-purpose text generation and understanding. It is characterized by economical training and efficient inference (2405.04434.pdf, p. 1).

*   **Capabilities:** The model demonstrates top-tier performance among open-source models, particularly in English and Chinese language tasks, as well as in domains like mathematics and coding (2405.04434.pdf, p. 4, 14). The chat-tuned versions are designed for instruction-based conversation tasks (2405.04434.pdf, p. 18).
*   **Input-Output Structure:** The model takes a sequence of text tokens as input and generates a sequence of text tokens as output (modeling_deepseek.py).

### Primary intended users:
The primary intended users are researchers and developers in the field of artificial intelligence and natural language processing who wish to build upon or experiment with large-scale language models (LICENSE.txt, Preamble).

### Out-of-scope uses:
The license explicitly prohibits using the model or its derivatives for certain applications. You may not use the model:
*   In any way that violates applicable laws or infringes on third-party rights (LICENSE.txt, Attachment A).
*   For any military use (LICENSE.txt, Attachment A).
*   To exploit or harm minors (LICENSE.txt, Attachment A).
*   To generate or disseminate verifiably false information with the purpose of harming others (LICENSE.txt, Attachment A).
*   To generate or disseminate inappropriate content subject to applicable regulations (LICENSE.txt, Attachment A).
*   To generate or disseminate personally identifiable information without authorization (LICENSE.txt, Attachment A).
*   To defame, disparage, or harass others (LICENSE.txt, Attachment A).
*   For fully automated decision-making that adversely impacts an individual’s legal rights (LICENSE.txt, Attachment A).
*   For uses that discriminate against or harm individuals or groups based on social behavior or personal characteristics (LICENSE.txt, Attachment A).
*   To exploit vulnerabilities of a specific group of people to distort their behavior in a way that causes physical or psychological harm (LICENSE.txt, Attachment A).

---

## How to Use
This section outlines how to use the model.

Insufficient information. The provided repository does not contain a README or example code snippets for using the model. However, as a model with a standard Transformer architecture, it is likely compatible with common libraries like Hugging Face Transformers. The model's configuration files indicate it is a causal language model (`DeepseekV2ForCausalLM`) (config.json.txt).

The generation configuration suggests the following default parameters for text generation:
*   `do_sample`: true
*   `temperature`: 0.3
*   `top_p`: 0.95
*   `bos_token_id`: 100000
*   `eos_token_id`: 100001
(generation_config.json.txt)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Based on the evaluation in the paper, the following are relevant factors for the model's performance:
*   **Language:** The model is pretrained on a bilingual corpus of English and Chinese and is evaluated on benchmarks in both languages (2405.04434.pdf, p. 13, 15). Its proficiency in other languages may be limited (2405.04434.pdf, p. 21).
*   **Domain:** The model's performance is evaluated across various domains, including general language understanding, reasoning, mathematics, and code generation (2405.04434.pdf, p. 14).
*   **Task Type:** Performance varies between tasks like multiple-choice questions, open-ended generation, and code completion (2405.04434.pdf, p. 15).

### Evaluation factors:
The model evaluation explicitly analyzes performance across different languages (English and Chinese) and domains (general knowledge, code, math) (2405.04434.pdf, Table 2, p. 15).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of metrics tailored to different benchmarks (2405.04434.pdf, p. 14-15):
*   **Accuracy (Acc.):** Used for multiple-choice question answering tasks like MMLU, C-Eval, CMMLU, ARC, and AGIEval.
*   **Exact Match (EM):** Used for question answering and standardized exam tasks like TriviaQA, NaturalQuestions, GSM8K, MATH, and BBH.
*   **F1 Score:** Used for reading comprehension tasks like DROP.
*   **Pass@1:** Used for code generation tasks like HumanEval and MBPP to measure the percentage of problems for which at least one correct solution is generated.
*   **Bits-Per-Byte (BPB):** Used for language modeling evaluation on the Pile-test dataset to ensure fair comparison across different tokenizers.
*   **Length-Controlled Win Rate:** Used for open-ended conversation evaluation on AlpacaEval 2.0.
*   **Overall Score:** Used for open-ended conversation benchmarks like MT-Bench and AlignBench.

### Decision thresholds:
Insufficient information.

### Variation approaches:
The evaluation settings specify the number of few-shot examples for each benchmark (e.g., 5-shot for MMLU, 8-shot for GSM8K), but the paper does not detail statistical methods like cross-validation or bootstrapping for calculating uncertainty (2405.04434.pdf, Table 2, p. 15).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of public benchmarks covering multiple languages and domains (2405.04434.pdf, p. 14).

*   **English Benchmarks:**
    *   **Multi-subject:** MMLU
    *   **Language Understanding/Reasoning:** HellaSwag, PIQA, ARC, BigBench Hard (BBH)
    *   **Question Answering:** TriviaQA, NaturalQuestions
    *   **Reading Comprehension:** RACE, DROP
    *   **Reference Disambiguation:** WinoGrande
    *   **Language Modeling:** Pile
*   **Chinese Benchmarks:**
    *   **Multi-subject:** C-Eval, CMMLU
    *   **Reading Comprehension:** C3, CMRC
    *   **Reference Disambiguation:** CLUEWSC
    *   **Understanding/Culture:** CHID, CCPM
*   **Math Benchmarks:** GSM8K, MATH, CMath
*   **Code Benchmarks:** HumanEval, MBPP, CRUXEval
*   **Standardized Exams (Bilingual):** AGIEval
*   **Open-Ended Conversation:** MT-Bench, AlpacaEval 2.0 (English), AlignBench (Chinese)

### Motivation:
These datasets were chosen as they are standard, representative benchmarks for evaluating the capabilities of large language models in areas such as general knowledge, reasoning, reading comprehension, mathematics, and coding in both English and Chinese (2405.04434.pdf, p. 13-14).

### Preprocessing:
The paper specifies that evaluation was either perplexity-based or generation-based depending on the dataset. For language modeling on Pile-test, Bits-Per-Byte (BPB) was used as the metric to ensure a fair comparison among models with different tokenizers. No other specific preprocessing steps for the evaluation data are detailed (2405.04434.pdf, p. 14).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a high-quality, multi-source corpus consisting of 8.1 trillion tokens. The dataset is bilingual, containing both English and Chinese data. The paper notes that the corpus contains approximately 12% more Chinese tokens than English ones (2405.04434.pdf, p. 11-12).

### Motivation:
The training data was constructed to build a strong bilingual language model. Compared to the corpus used for the previous DeepSeek 67B model, this dataset features an extended amount of data, especially Chinese data, and higher data quality. The goal was to better leverage the corpus available on the Chinese internet and improve overall model performance (2405.04434.pdf, p. 11).

### Preprocessing:
The data processing involved several stages to improve quality (2405.04434.pdf, p. 11):
*   **Data Cleaning:** Optimized cleaning processes were used to recover a large amount of mistakenly deleted data from internet sources.
*   **Quality Filtering:** An improved quality-based filtering algorithm was used to remove non-beneficial data while retaining valuable data.
*   **Content Filtering:** Contentious content, such as values influenced by specific regional cultures, was filtered out to mitigate data bias. A detailed discussion of this strategy is in Appendix E of the paper (2405.04434.pdf, p. 11, 32).
*   **Tokenization:** The same tokenizer as DeepSeek 67B was used, which is based on the Byte-level Byte-Pair Encoding (BBPE) algorithm and has a vocabulary size of 100K (2405.04434.pdf, p. 12).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was evaluated across several categories. The results below are for the base pre-trained model (2405.04434.pdf, Table 2, p. 15).

| Category | Benchmark         | Metric | # Shots | DeepSeek-V2 Score |
| :------- | :---------------- | :----- | :------ | :---------------- |
| **English** | Pile-test         | BPB    | -       | 0.606             |
|          | BBH               | EM     | 3-shot  | 78.9              |
|          | MMLU              | Acc.   | 5-shot  | 78.5              |
|          | DROP              | F1     | 3-shot  | 80.1              |
|          | ARC-Easy          | Acc.   | 25-shot | 97.6              |
|          | ARC-Challenge     | Acc.   | 25-shot | 92.4              |
|          | HellaSwag         | Acc.   | 10-shot | 84.2              |
|          | PIQA              | Acc.   | 0-shot  | 83.7              |
|          | WinoGrande        | Acc.   | 5-shot  | 84.9              |
|          | RACE-Middle       | Acc.   | 5-shot  | 73.1              |
|          | RACE-High         | Acc.   | 5-shot  | 52.7              |
|          | TriviaQA          | EM     | 5-shot  | 79.9              |
|          | NaturalQuestions  | EM     | 5-shot  | 38.7              |
|          | AGIEval           | Acc.   | 0-shot  | 51.2              |
| **Code**    | HumanEval         | Pass@1 | 0-shot  | 48.8              |
|          | MBPP              | Pass@1 | 3-shot  | 66.6              |
|          | CRUXEval-I        | Acc.   | 2-shot  | 52.8              |
|          | CRUXEval-O        | Acc.   | 2-shot  | 49.8              |
| **Math**    | GSM8K             | EM     | 8-shot  | 79.2              |
|          | MATH              | EM     | 4-shot  | 43.6              |
|          | CMath             | EM     | 3-shot  | 78.7              |
| **Chinese** | CLUEWSC           | EM     | 5-shot  | 82.2              |
|          | C-Eval            | Acc.   | 5-shot  | 81.7              |
|          | CMMLU             | Acc.   | 5-shot  | 84.0              |
|          | CMRC              | EM     | 1-shot  | 77.5              |
|          | C3                | Acc.   | 0-shot  | 77.4              |
|          | CHID              | Acc.   | 0-shot  | 92.7              |
|          | CCPM              | Acc.   | 0-shot  | 93.1              |

### Intersectional results:
Insufficient information. The paper does not provide intersectional results (e.g., performance on math benchmarks broken down by language).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** The model weights are approximately 439.1 GB (model.safetensors.index.summary.json.txt).
*   **Precision:** The model is stored in `bfloat16` format (config.json.txt). Loading the model would require at least 440 GB of RAM/VRAM.

### Deploying Requirements:
For efficient deployment, the developers converted the model's parameters to FP8 precision and used KV cache quantization to compress each element in the cache to 6 bits on average. Benefiting from the MLA architecture and these optimizations, the deployed model requires significantly less KV cache than dense models of similar size (2405.04434.pdf, p. 16). On a single node with 8 NVIDIA H800 GPUs, the model can achieve a generation throughput exceeding 50K tokens per second (2405.04434.pdf, p. 16).

### Training or Fine-tuning Requirements:
The model was trained on a cluster of NVIDIA H800 GPUs. The training framework utilized a combination of parallelism strategies to manage the model's size and computational cost:
*   16-way zero-bubble pipeline parallelism
*   8-way expert parallelism
*   ZeRO-1 data parallelism
(2405.04434.pdf, p. 12)
Due to the model's sparse activation, it could be trained without tensor parallelism, reducing communication overhead (2405.04434.pdf, p. 12).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Bias Mitigation:** During pre-training data preparation, the developers identified and filtered out contentious content, such as values influenced by specific regional cultures, to avoid the model exhibiting unnecessary subjective biases. This effort in debiasing the pre-training corpus is cited as a reason for the model's performance on certain value-sensitive test sets like the MMLU Humanity-Moral subset (2405.04434.pdf, p. 32).
*   **Potential Risks and Harms:**
    *   The model shares limitations common to other LLMs, including the potential to generate non-factual information, unverified advice, and hallucinations (2405.04434.pdf, p. 21).
    *   The model's knowledge is not updated after pre-training, so it may produce outdated information (2405.04434.pdf, p. 21).
    *   Since the training data is primarily Chinese and English, the model may exhibit limited proficiency and could produce lower-quality or biased outputs for other languages (2405.04434.pdf, p. 21).
*   **Risk Mitigation and Use Restrictions:** The model license includes an extensive list of use-based restrictions to prevent misuse. These restrictions prohibit using the model for illegal activities, military purposes, harming minors, generating disinformation to harm others, and other unethical applications (LICENSE.txt, Attachment A). Users are accountable for the output they generate and must ensure its use does not contravene any provisions of the license (LICENSE.txt, Section III, paragraph 6).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Common LLM Limitations:** The model is susceptible to common LLM issues such as generating factually incorrect information (hallucinations) and possessing outdated knowledge due to the static nature of its training data (2405.04434.pdf, p. 21).
*   **Language Proficiency:** The model's training data is primarily composed of Chinese and English content. Consequently, its performance in other languages may be limited and should be used with caution in non-English and non-Chinese contexts (2405.04434.pdf, p. 21).
*   **Performance Gaps:** The paper acknowledges that due to being trained on fewer English tokens, DeepSeek-V2 has a slight gap in basic English capabilities compared to models like LLaMA3 70B (2405.04434.pdf, p. 15).
*   **Alignment Tax:** The process of aligning the model with human preferences via Reinforcement Learning can negatively impact performance on some standard benchmarks (a phenomenon known as "alignment tax"). While efforts were made to find a tolerable trade-off, users may observe performance variations between the base and chat-tuned models on certain tasks (2405.04434.pdf, p. 20).

### Recommendations:
*   Users should be critical of the model's outputs and verify any factual claims, especially in high-stakes domains.
*   The model should be used with caution for applications involving languages other than English and Chinese (2405.04434.pdf, p. 21).
*   Users must adhere to the use-based restrictions outlined in the license to ensure responsible application of the model (LICENSE.txt, Attachment A).
*   Users are solely responsible for the output they generate and its subsequent uses (LICENSE.txt, Section III, paragraph 6).