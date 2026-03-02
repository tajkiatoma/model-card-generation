## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Guan Wang, Sijie Cheng, Xianyuan Zhan, Xiangang Li, Sen Song, and Yang Liu from the Department of Computer Science and Technology at Tsinghua University, the Laboratory of Brain and Intelligence at Tsinghua University, the Institute for AI Industry Research (AIR) at Tsinghua University, and the Shanghai Artificial Intelligence Laboratory (2309.11235.pdf, p. 1).

### Model date:
The associated academic paper was last revised on March 16, 2024 (2309.11235.pdf, p. 1).

### Model version:
The model is identified as `openchat_v3.2_mistral` (openchat.json.txt). It is an application of the OpenChat framework, which uses a method called Conditioned-Reinforcement Learning Fine-Tuning (C-RLFT) to learn from mixed-quality data (2309.11235.pdf, p. 1). This approach differs from standard Supervised Fine-Tuning (SFT) by treating data from different sources as having different quality levels and learning a class-conditioned policy, and it differs from standard Reinforcement Learning Fine-Tuning (RLFT) by not requiring costly human preference labeling (2309.11235.pdf, p. 2).

### Model type:
The model is a `MistralForCausalLM`, a type of decoder-only Transformer architecture designed for causal language modeling (text generation) (config.json.txt). It is based on the Mistral 7B architecture (config.json.txt, openchat.json.txt).

Key architectural details include:
*   **Model Type:** `mistral` (config.json.txt)
*   **Parameters:** 7 billion (derived from base model name `Mistral_7B_with_EOT_token` in config.json.txt)
*   **Layers:** 32 hidden layers (config.json.txt)
*   **Hidden Size:** 4096 (config.json.txt)
*   **Intermediate Size:** 14336 (config.json.txt)
*   **Attention Heads:** 32 (config.json.txt)
*   **Key-Value Heads:** 8 (Grouped-Query Attention) (config.json.txt)
*   **Activation Function:** `silu` (config.json.txt)
*   **Vocabulary Size:** 32002 (config.json.txt)
*   **Max Position Embeddings (Context Length):** 8192 tokens (config.json.txt)
*   **Sliding Window Attention:** 4096 tokens (config.json.txt)
*   **Total Size on Disk:** Approximately 14.5 GB (pytorch_model.bin.index.json.txt)

### Training details:
The model was fine-tuned from the `imone/Mistral_7B_with_EOT_token` base model using the Conditioned-Reinforcement Learning Fine-Tuning (C-RLFT) framework (config.json.txt, 2309.11235.pdf, p. 1). C-RLFT is a method designed to leverage mixed-quality data by treating different data sources as having coarse-grained reward labels. It learns a class-conditioned policy that can distinguish between expert and sub-optimal data, which is optimized via a simple, RL-free, reward-weighted regression objective (2309.11235.pdf, p. 4).

The training was configured for 5 epochs with the following hyperparameters (openchat.json.txt):
*   **Learning Rate:** 1.2507232220003032e-05
*   **LR Minimum Ratio:** 0.1
*   **LR Warmup Ratio:** 0.05
*   **Weight Decay:** 0.1
*   **Adam Beta1:** 0.9
*   **Adam Beta2:** 0.95
*   **Adam Epsilon:** 1e-05
*   **Batch Size Per GPU:** 10
*   **Distributed Training:** DeepSpeed was used (openchat.json.txt).

### Paper or other resource for more information:
The model and its training framework, OpenChat, are described in the paper "OPENCHAT: ADVANCING OPEN-SOURCE LANGUAGE MODELS WITH MIXED-QUALITY DATA". The paper details the C-RLFT methodology, experiments, and results. The code, data, and models are publicly available on GitHub and Hugging Face (2309.11235.pdf, p. 1).

*   **Paper:** Wang, G., Cheng, S., Zhan, X., Li, X., Song, S., & Liu, Y. (2024). *OPENCHAT: ADVANCING OPEN-SOURCE LANGUAGE MODELS WITH MIXED-QUALITY DATA*. Published as a conference paper at ICLR 2024. arXiv:2309.11235v2.

### Citation details:
Insufficient information.

### License:
The repository states that the code, data, and models are "publicly available" (2309.11235.pdf, p. 1). However, the specific license (e.g., Apache 2.0, MIT) is not detailed in the provided files.

### Contact:
For questions or feedback, contact can be made via the email provided in the research paper: `csj23@mails.tsinghua.edu.cn` (2309.11235.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended as a general-purpose, instruction-following chatbot (2309.11235.pdf, p. 1, 6). Its primary use is to generate helpful and relevant responses to user prompts in a conversational format. It has been evaluated on its capabilities in writing, roleplay, extraction, reasoning, mathematics, and coding (2309.11235.pdf, p. 15).

The model expects input formatted in a specific chat structure. During inference, the recommended format is the one used for the high-quality (GPT-4) training data to generate high-quality responses (2309.11235.pdf, p. 5). The input-output structure is a sequence of turns, each marked with a role (`User` or `Assistant`) and separated by a special token `<|end_of_turn|>` (2309.11235.pdf, p. 4; tokenizer_config.json.txt).

### Primary intended users:
The primary users are researchers and developers in the field of artificial intelligence and natural language processing who are interested in advancing and utilizing open-source language models (2309.11235.pdf, p. 1, 10).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model should be used as a conversational AI. Prompts should be formatted according to the model's chat template. To elicit the highest quality responses, the template used for expert data (GPT-4) during training is recommended for inference (2309.11235.pdf, p. 5).

The specific chat template is defined as follows (tokenizer_config.json.txt):
`{{ bos_token }}{% for message in messages %}{{ 'GPT4 Correct ' + message['role'].title() + ': ' + message['content'] + '<|end_of_turn|>'}}{% endfor %}{% if add_generation_prompt %}{{ 'GPT4 Correct Assistant:' }}{% endif %}`

This template translates to the following format for a conversation:
`<s>GPT4 Correct User: {user_prompt_1}<|end_of_turn|>GPT4 Correct Assistant: {model_response_1}<|end_of_turn|>GPT4 Correct User: {user_prompt_2}<|end_of_turn|>GPT4 Correct Assistant:`

A special token, `<|end_of_turn|>` (ID 32000), is used to separate turns in the conversation (added_tokens.json.txt, 2309.11235.pdf, p. 4).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The most relevant factor for this model is the quality of the training data. The OpenChat framework is explicitly designed to differentiate between data sources of varying quality, such as "expert" data (e.g., from GPT-4) and "sub-optimal" data (e.g., from GPT-3.5) (2309.11235.pdf, p. 1, 4). The model's performance is influenced by the mix and quality of these data sources.

### Evaluation factors:
The model's evaluation includes analyses based on data quality. Ablation studies were conducted by training the model with and without the coarse-grained rewards that signify data quality, as well as training on only expert data versus only sub-optimal data (2309.11235.pdf, p. 8, Table 2). The effect of varying the proportion of each data class was also analyzed (2309.11235.pdf, p. 9, Figure 6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using three main metrics across different benchmarks (2309.11235.pdf, p. 6):
1.  **Win rate (%)**: Used for pairwise comparisons in benchmarks like AlpacaEval and Vicuna-bench. The model receives 1 point for a win, 0.5 for a tie, and 0 for a loss against a baseline model.
2.  **Score**: A single-answer grading score from 1 to 10, used in MT-bench, where an LLM evaluator judges the quality of the generated answer.
3.  **Accuracy**: Used for multiple-choice exam questions in the AGIEval benchmark.

### Decision thresholds:
Insufficient information.

### Variation approaches:
To evaluate performance, the study relies on automatic evaluators, primarily `gpt-4` and `text-davinci-003` (`alpaca_eval_gpt`), as specified by the official benchmark implementations (2309.11235.pdf, p. 5). To ensure the reliability of these automatic evaluators, consistency checks were performed by comparing results from `gpt-4`, `gpt-3.5`, and `claude-2`, which showed a strong Pearson correlation (r = 0.91 between Claude-2 and GPT-3.5) (2309.11235.pdf, p. 16).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on four standard benchmarks (2309.11235.pdf, p. 5, 15):
1.  **AlpacaEval**: A benchmark for instruction-following, consisting of 805 user instructions from diverse sources.
2.  **MT-bench**: A multi-turn benchmark with 80 high-quality questions across eight topics (writing, roleplay, reasoning, math, etc.).
3.  **Vicuna-bench**: A benchmark evaluating proficiency across eight question categories, including commonsense, coding, and math.
4.  **AGIEval**: A collection of human-centric standardized exams, including English multiple-choice tasks from SAT, AQUA-RAT, LSAT, and civil service exams (LogiQA).

### Motivation:
These datasets were chosen to provide a comprehensive assessment of the model's capabilities. AlpacaEval, MT-bench, and Vicuna-bench were used to evaluate instruction-following and conversational abilities, while AGIEval was used to validate the model's generalization performance on complex problem-solving tasks (2309.11235.pdf, p. 1, 5).

### Preprocessing:
For the AGIEval benchmark, the official zero-shot prompt and answer matching methods were used. For conversational benchmarks, the evaluation prompts were formatted as user questions within the model's conversation template (2309.11235.pdf, p. 16).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was fine-tuned on the **ShareGPT dataset**. This dataset contains approximately 70,000 user-shared conversations. It is a mixed-quality dataset composed of two main sources (2309.11235.pdf, p. 5):
*   **Expert Data (`D_exp`)**: Around 6,000 conversations generated by GPT-4.
*   **Sub-optimal Data (`D_sub`)**: The remaining ~64,000 conversations generated by GPT-3.5.

### Motivation:
The primary motivation for using the mixed-quality ShareGPT dataset was to develop and validate the OpenChat framework, which is designed to fine-tune language models effectively without requiring costly, manually created preference labels. The framework leverages the inherent quality difference between data sources (GPT-4 vs. GPT-3.5) as a coarse-grained reward signal (2309.11235.pdf, p. 3).

### Preprocessing:
The data was preprocessed to create a class-conditioned dataset. Each conversation was conditioned on its source using a distinct template. This allows the model to learn to differentiate between the data qualities during training (2309.11235.pdf, p. 4).
*   **GPT-4 Template**: `GPT4 User: Question<|end_of_turn|>GPT4 Assistant:`
*   **GPT-3.5 Template**: `GPT3 User: Question<|end_of_turn|>GPT3 Assistant:`

A special token, `<|end_of_turn|>`, was added to the vocabulary to differentiate between speaker turns (2309.11235.pdf, p. 4; added_tokens.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Ablation studies were performed to analyze the impact of individual components. The results are presented as average win rates across AlpacaEval, MT-bench, and Vicuna-bench (2309.11235.pdf, p. 8, Table 2):
*   **Full `openchat-13b` model**: 77.3% average win rate.
*   **Without rewards** (treating all data equally): 74.0% average win rate.
*   **Without class-conditioning**: 60.5% average win rate.
*   **SFT on only GPT-4 data** (~6k samples): 64.5% average win rate.
*   **SFT on only GPT-3.5 data** (~64k samples): 42.8% average win rate.

These results show that both the class-conditioned policy and the coarse-grained rewards are crucial for the model's performance (2309.11235.pdf, p. 8).

### Intersectional results:
The main performance of the `openchat-13b` model, trained on the intersection of GPT-4 and GPT-3.5 data using the C-RLFT method, is as follows (2309.11235.pdf, p. 6, Table 1):
*   **AlpacaEval (win rate %)**: 89.5
*   **MT-bench (score)**: 57.5 (Note: The paper reports this as a win rate, which is likely a typo. The value corresponds to the MT-bench score from Figure 2a, page 7)
*   **Vicuna-bench (win rate %)**: 85.0
*   **Average Win Rate**: 77.3%

The model achieves the highest average performance among all evaluated 13B open-source models (2309.11235.pdf, p. 6).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model's total size is approximately 14.5 GB (pytorch_model.bin.index.json.txt). It was trained with `bfloat16` precision, so loading the model for inference would require a GPU or RAM with at least 15 GB of available memory (config.json.txt).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training configuration specifies the use of DeepSpeed, indicating that fine-tuning was performed in a distributed, multi-GPU environment (openchat.json.txt). Specific hardware details (e.g., number or type of GPUs) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development of this model was guided by the following ethical considerations, as outlined in the associated paper (2309.11235.pdf, p. 10):
*   **Democratizing AI Research**: By advancing open-source models, the study aims to broaden accessibility to AI research, fostering a more inclusive and transparent community.
*   **Fairness and Bias Reduction**: The fine-tuning method is intended to lead to more satisfying and safer responses, which includes efforts to reduce human bias and promote fairness.
*   **Data Privacy**: The training dataset (ShareGPT) consists of publicly available, user-shared instances. This approach was chosen to minimize potential data leakage and privacy concerns associated with collecting private user data.

No sensitive or private data was explicitly collected for this study. The risks are those generally associated with large language models, such as generating biased, unfair, or harmful content, which the C-RLFT method aims to mitigate by learning to prefer higher-quality, expert-demonstrated conversations (2309.11235.pdf, p. 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors acknowledge the following limitations (2309.11235.pdf, p. 10):
*   The assumption that data quality can be perfectly separated based on its source (e.g., GPT-4 vs. GPT-3.5) is an oversimplification.
*   The coarse-grained rewards assigned to each data source could be more finely tuned to reflect the actual quality of each individual data point, rather than a single value for the entire class.

### Recommendations:
*   For inference, users should use the prompt template corresponding to the expert data source (`GPT4 User: ... GPT4 Assistant:`) to generate the highest quality responses, as the model has learned to associate this condition with better outputs (2309.11235.pdf, p. 5).
*   The paper suggests that future work could explore applying the OpenChat framework to improve the reasoning abilities of LLMs, as the current study focused primarily on instruction-following capabilities (2309.11235.pdf, p. 10).