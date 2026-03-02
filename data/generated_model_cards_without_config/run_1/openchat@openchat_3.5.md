## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model and its underlying framework, OpenChat, were developed by researchers from several institutions:
*   Guan Wang (Tsinghua University, Laboratory of Brain and Intelligence)
*   Sijie Cheng (Tsinghua University, Institute for AI Industry Research (AIR), 01.AI)
*   Xianyuan Zhan (Institute for AI Industry Research (AIR), Shanghai Artificial Intelligence Laboratory)
*   Xiangang Li (01.AI)
*   Sen Song (Laboratory of Brain and Intelligence, Tsinghua University)
*   Yang Liu (Tsinghua University, Institute for AI Industry Research (AIR), Shanghai Artificial Intelligence Laboratory)

(Source: 2309.11235.pdf, page 1).

### Model date:
The associated academic paper was published as a conference paper at ICLR 2024. The second version of the paper is dated March 16, 2024 (Source: 2309.11235.pdf, page 1).

### Model version:
The model described and evaluated in the primary research paper is `openchat-13b` (Source: 2309.11235.pdf, page 1). The training configuration files in the repository refer to a variant named `openchat_v3.2_mistral`, which is based on Mistral-7B (Source: openchat.json.txt).

The OpenChat framework differs from standard Supervised Fine-Tuning (SFT) and Reinforcement Learning Fine-Tuning (RLFT) by proposing a method called Conditioned-RLFT (C-RLFT). Unlike SFT which treats all data equally, and RLFT which requires costly preference data, C-RLFT leverages mixed-quality data by treating data sources as coarse-grained reward labels and learning a class-conditioned policy. This allows for lightweight, RL-free supervised learning that can distinguish between expert and sub-optimal data (Source: 2309.11235.pdf, page 1).

### Model type:
The model is a Transformer-based Large Language Model (LLM) fine-tuned for instruction-following and chat capabilities (Source: 2309.11235.pdf, pages 1, 3).

*   **Architecture:** The primary model evaluated in the paper, `openchat-13b`, is based on the `llama-2-13b` base model (Source: 2309.11235.pdf, page 6, Table 1). The repository also contains configuration for a variant based on `Mistral_7B` (Source: openchat.json.txt).
*   **Size:** The main evaluated model has 13 billion parameters (Source: 2309.11235.pdf, page 1). The total size of the model weights in the repository is approximately 14.5 GB, which is consistent with a 7B parameter model (Source: pytorch_model.bin.index.json.txt).
*   **Context Length:** The model was fine-tuned with a sequence length of 4,096 tokens (Source: 2309.11235.pdf, page 6).

### Training details:
The model was fine-tuned using a novel method called **Conditioned-Reinforcement Learning Fine-Tuning (C-RLFT)**. This is a single-stage, RL-free supervised learning approach designed to leverage mixed-quality data (Source: 2309.11235.pdf, page 1).

*   **Algorithm:** C-RLFT regards different data sources (e.g., GPT-4 vs. GPT-3.5) as coarse-grained reward labels. It learns a class-conditioned policy that is regularized with respect to a class-conditioned reference policy. The optimal policy is solved via a simple reward-weighted regression objective (Source: 2309.11235.pdf, page 4-5).
*   **Hyperparameters:** The `openchat-13b` model was fine-tuned for 5 epochs using the AdamW optimizer with the following parameters:
    *   Learning Rate: 6.7 x 10⁻⁵ (with a cosine schedule, decaying to 10% of the max value)
    *   β1: 0.9
    *   β2: 0.95
    *   ε: 10⁻⁵
    *   Weight Decay: 0.1
    *   Effective Batch Size: 200k tokens
    *   Sequence Length: 4,096 tokens
    (Source: 2309.11235.pdf, page 6).
*   A training configuration file in the repository specifies slightly different parameters for the `openchat_v3.2_mistral` model, including a learning rate of 1.25 x 10⁻⁵ (Source: openchat.json.txt).

### Paper or other resource for more information:
The model and C-RLFT framework are described in the academic paper "OPENCHAT: ADVANCING OPEN-SOURCE LANGUAGE MODELS WITH MIXED-QUALITY DATA" (Source: 2309.11235.pdf).

The paper also provides links to the project's code, data, and models:
*   **GitHub:** https://github.com/imoneoi/openchat
*   **Hugging Face:** https://huggingface.co/openchat
(Source: 2309.11235.pdf, page 1).

### Citation details:
```bibtex
@article{wang2023openchat,
  title={OpenChat: Advancing Open-source Language Models with Mixed-Quality Data},
  author={Wang, Guan and Cheng, Sijie and Zhan, Xianyuan and Li, Xiangang and Song, Sen and Liu, Yang},
  journal={arXiv preprint arXiv:2309.11235},
  year={2023},
  note={Published as a conference paper at ICLR 2024}
}
```
(Source: 2309.11235.pdf)

### License:
Insufficient information

### Contact:
For questions or feedback, the developers can be contacted via email: `imonenext@gmail.com`, `csj23@mails.tsinghua.edu.cn` (Source: 2309.11235.pdf, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of the OpenChat model is as an open-source, instruction-following language model for chat and conversational AI applications (Source: 2309.11235.pdf, page 1, 6). It is designed to align with human goals and provide more satisfying and safer responses by effectively learning from data of mixed quality (Source: 2309.11235.pdf, page 10).

The model's input-output structure is conversational. The input is a user prompt, and the model generates a relevant and helpful response. The conversation history is maintained as context for multi-turn dialogues (Source: 2309.11235.pdf, page 4). The specific format is defined by a chat template (Source: tokenizer_config.json.txt).

### Primary intended users:
The primary users are AI researchers and developers. The project aims to democratize AI research by providing an accessible, transparent, and high-performing open-source model, fostering innovation and collaboration within the community (Source: 2309.11235.pdf, page 10).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses a specific conversation template to differentiate between data sources during training and for generation during inference. A special token, `<|end_of_turn|>`, is used to signify the end of an utterance (Source: 2309.11235.pdf, page 4; added_tokens.json.txt).

**Chat Template:**
The general template for conversations is as follows:
```
{{ bos_token }}{% for message in messages %}{{ 'GPT4 Correct ' + message['role'].title() + ': ' + message['content'] + '<|end_of_turn|>'}}{% endfor %}{% if add_generation_prompt %}{{ 'GPT4 Correct Assistant:' }}{% endif %}
```
(Source: tokenizer_config.json.txt)

**Inference Usage:**
For generating high-quality responses during inference, the template conditioned on the "expert" data source (GPT-4) should be used (Source: 2309.11235.pdf, page 5).

*   **Inference Template:** `GPT4 User: {Question}<|end_of_turn|>GPT4 Assistant:` (Source: 2309.11235.pdf, page 5).

**Example Input/Output Structure:**
*   **Input:** A list of messages, where each message is a dictionary with 'role' ('user' or 'assistant') and 'content'.
*   **Formatted Input String:** `<s>GPT4 Correct User: Hello, how are you?<|end_of_turn|>GPT4 Correct Assistant: I'm doing great. How can I help you today?<|end_of_turn|>GPT4 Correct User: What is C-RLFT?<|end_of_turn|>GPT4 Correct Assistant:`
*   **Output:** The model generates the text that follows the final `Assistant:` prompt.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The most relevant factor for the OpenChat framework is **data quality**. The model is explicitly designed to handle mixed-quality data by distinguishing between different data sources, which are treated as coarse-grained reward labels. The primary distinction made during training is between high-quality "expert" data (from GPT-4) and lower-quality "sub-optimal" data (from GPT-3.5) (Source: 2309.11235.pdf, page 3). The size of the data from each quality tier is also a relevant factor (Source: 2309.11235.pdf, page 9).

### Evaluation factors:
The evaluation factors analyzed in the paper are directly related to the relevant factors:
*   **Coarse-grained rewards:** An ablation study was performed by removing the reward weighting, treating all data equally, which led to a performance decline (Source: 2309.11235.pdf, Table 2, page 8).
*   **Class-conditioned policy:** An ablation study was performed by removing the class-conditioning prompts, which also significantly reduced performance (Source: 2309.11235.pdf, Table 2, page 8).
*   **Data source filtering:** The model was evaluated when trained only on GPT-4 data versus only on GPT-3.5 data to understand the impact of each quality tier (Source: 2309.11235.pdf, Table 2, page 8).
*   **Data size:** The impact of data size was evaluated by sub-sampling the GPT-4 and GPT-3.5 datasets at different ratios (60% to 100%) (Source: 2309.11235.pdf, Section 5.4, page 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using three main metrics across several standard benchmarks (Source: 2309.11235.pdf, pages 5-6):
*   **Win Rate (%):** Used for pairwise comparisons in benchmarks like AlpacaEval and Vicuna-bench. An LLM evaluator compares the model's response to a reference model's response. The tested model gets 1 point for a win, 0.5 for a tie, and 0 for a loss.
*   **Score:** Used for single-answer grading in MT-bench. An LLM evaluator judges the generated answer with a score from 1 to 10.
*   **Accuracy:** Used for multiple-choice exam questions in the AGIEval benchmark.

### Decision thresholds:
Insufficient information

### Variation approaches:
Performance was evaluated using automated evaluators based on powerful LLMs. To ensure reliability and mitigate self-enhancement bias, the authors verified consistency across different evaluators (Source: 2309.11235.pdf, page 5, Appendix E, page 16).
*   **AlpacaEval:** Uses `alpaca_eval_gpt` (based on `text-davinci-003`). Consistency was checked using GPT-3.5 and Claude-2 as evaluators, which showed a strong Pearson correlation (r=0.91) (Source: 2309.11235.pdf, page 5, 16).
*   **MT-bench and Vicuna-bench:** Use GPT-4 as the evaluator.
*   **AGIEval:** Uses official answer matching for accuracy calculation.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on four standard benchmarks (Source: 2309.11235.pdf, page 5, Appendix C, page 15):
*   **AlpacaEval:** A benchmark for instruction-following that includes a test set of 805 user instructions from diverse sources.
*   **MT-bench:** A multi-turn benchmark with 80 high-quality questions across eight topics (writing, roleplay, reasoning, math, etc.) to test conversational and instruction-following abilities.
*   **Vicuna-bench:** A benchmark evaluating proficiency across eight question categories, including generic questions, knowledge, coding, and math.
*   **AGIEval:** A collection of human-centric standardized exams in English, including tasks from SAT, AQUA-RAT, LSAT, and civil service exams (LogiQA), to gauge problem-solving abilities.

### Motivation:
These datasets were chosen because they are widely recognized benchmarks for assessing key LLM capabilities such as instruction-following, multi-turn conversation, and generalization to complex, human-centric tasks (Source: 2309.11235.pdf, page 5).

### Preprocessing:
For conversational benchmarks (MT-bench, Vicuna-bench), the official zero-shot prompt for each question was set as the user's question within the model's corresponding conversation template (Source: 2309.11235.pdf, page 16).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on the **ShareGPT dataset**, which is a publicly available collection of user-shared conversations with ChatGPT (Source: 2309.11235.pdf, page 2, 5).
*   **Size and Structure:** The dataset consists of approximately 70,000 conversations.
*   **Diversity and Features:** The data is of mixed quality and is divided into two main sources for training:
    1.  **Expert Data (`D_exp`):** ~6,000 conversations generated by GPT-4.
    2.  **Sub-optimal Data (`D_sub`):** The remaining ~64,000 conversations generated by GPT-3.5.
(Source: 2309.11235.pdf, page 5).

### Motivation:
The ShareGPT dataset was chosen because it is a widely-used SFT dataset that naturally contains mixed-quality data. This aligns with the core goal of the OpenChat framework, which is to develop a method that can effectively learn from such datasets without requiring expensive human preference labels (Source: 2309.11235.pdf, page 2, 5).

### Preprocessing:
The training data was preprocessed to enable the C-RLFT method (Source: 2309.11235.pdf, page 4):
*   **Class-Conditioning:** Each conversation was conditioned on its source using distinct conversation templates. For example:
    *   **GPT-4 Template:** `GPT4 User: {Question}<|end_of_turn|>GPT4 Assistant:`
    *   **GPT-3.5 Template:** `GPT3 User: {Question}<|end_of_turn|>GPT3 Assistant:`
*   **Special Tokens:** A new special token, `<|end_of_turn|>`, was added to the tokenizer to differentiate between user and assistant utterances. This token functions similarly to an EOS token for stopping generation (Source: 2309.11235.pdf, page 4; added_tokens.json.txt).
*   **Reward Weighting:** During training, examples from the expert (GPT-4) data were given a higher weight (unit weight of 1) than examples from the sub-optimal (GPT-3.5) data (weight of 0.1) (Source: 2309.11235.pdf, page 6).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents ablation studies that analyze the performance based on unitary factors (Source: 2309.11235.pdf, Table 2, page 8):
*   **Training on "only GPT-4" data (~6k samples):** Achieved an average score of 64.5 across benchmarks.
*   **Training on "only GPT-3.5" data (~64k samples):** Achieved an average score of 42.8.
*   **Training on all ~70k samples with standard SFT:** Achieved an average score of 52.7.

The paper also analyzes the effect of data size by subsampling each data source. For example, reducing the GPT-4 data to 60% of its original size while keeping GPT-3.5 data at 100% resulted in a noticeable drop in average win rate, highlighting the importance of expert data (Source: 2309.11235.pdf, Figure 6, page 9).

### Intersectional results:
The main results of the `openchat-13b` model are based on the intersection of mixed-quality data and the C-RLFT training method. Ablation studies show the performance with and without key components (Source: 2309.11235.pdf, Table 2, page 8):
*   **Full Model (C-RLFT with reward and condition):** 77.3 average score.
*   **Without reward weighting (SFT with condition):** 74.0 average score.
*   **Without class-conditioning (SFT with reward):** 60.5 average score.

These results demonstrate that the combination of class-conditioning and reward-weighting is crucial for the model's final performance.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper notes that the C-RLFT method is computationally efficient compared to PPO-based RLHF methods because it does not require loading the original base model during fine-tuning to compute a KL penalty. This saves a "considerable amount of computation resources" (Source: 2309.11235.pdf, page 5). However, specific hardware details (e.g., GPU type, number of GPUs, VRAM) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper includes an "Ethics Statement" that addresses several considerations (Source: 2309.11235.pdf, page 10):
*   **Data Privacy:** The training dataset (ShareGPT) consists of publicly available, user-shared instances. This approach is noted to help minimize potential data leakage and privacy concerns.
*   **Democratization of AI:** The project aims to advance open-source language models to broaden accessibility, stimulate innovation, and cultivate a dynamic and inclusive research community.
*   **Fairness and Bias:** The paper suggests that refining the model's ability to follow instructions can lead to safer responses, including the reduction of human bias and the promotion of fairness.
*   **Risks:** While not explicitly detailed, the general risks associated with language models (e.g., generating harmful or biased content) are implicitly acknowledged through the goal of producing "safer responses."

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors acknowledge several limitations and areas for future work (Source: 2309.11235.pdf, page 10):
*   **Oversimplified Data Quality Assumption:** The assumption that data quality can be perfectly divided based on the source model (GPT-4 vs. GPT-3.5) is "overly simplistic." The assigned coarse-grained rewards could be more finely tuned to reflect the actual quality of each data point.
*   **Focus on Instruction-Following:** The model primarily focuses on enhancing instruction-following capabilities. Its reasoning abilities were not a primary target for improvement, offering a "promising avenue for future work."
*   **Multi-turn Consistency:** The paper notes that LLMs can tend to "forget" prompts at the beginning of long conversations, which can affect multi-turn consistency (Source: 2309.11235.pdf, page 14).

### Recommendations:
*   **Inference Prompting:** To generate the highest quality responses, users should use the specific conversation template associated with the expert data source (i.e., the GPT-4 prompt) during inference (Source: 2309.11235.pdf, page 5, 8).
*   **Multi-turn Conversations:** To improve the effect of the class-conditioned policy, the condition prompt (e.g., `GPT4 User:`) should be repeated at every turn of the conversation (Source: 2309.11235.pdf, page 14).