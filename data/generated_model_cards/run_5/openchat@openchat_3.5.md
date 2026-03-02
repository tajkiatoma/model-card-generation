## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Guan Wang, Sijie Cheng, Xianyuan Zhan, Xiangang Li, Sen Song, and Yang Liu (OpenChat_Paper.pdf, p. 1). The developers are affiliated with the Department of Computer Science and Technology at Tsinghua University, the Laboratory of Brain and Intelligence at Tsinghua University, the Institute for AI Industry Research (AIR) at Tsinghua University, and the Shanghai Artificial Intelligence Laboratory (OpenChat_Paper.pdf, p. 1).

The project's code, data, and models are publicly available on GitHub at https://github.com/imoneoi/openchat and on Hugging Face at https://huggingface.co/openchat (OpenChat_Paper.pdf, p. 1).

### Model date:
The associated academic paper is dated March 16, 2024, and was published as a conference paper at ICLR 2024 (OpenChat_Paper.pdf, p. 1).

### Model version:
This model is `openchat-13b`, specifically version `openchat_v3.2_mistral` (training_args.bin; OpenChat_Paper.pdf, p. 1). It is part of the OpenChat framework, which is designed to fine-tune open-source language models using mixed-quality data (OpenChat_Paper.pdf, p. 1).

This model is fine-tuned from the `llama-2-13b` base model (OpenChat_Paper.pdf, p. 2, 6). It differs from other models fine-tuned with Supervised Fine-Tuning (SFT) or Reinforcement Learning from Human Feedback (RLHF) by using a novel method called Conditioned-RLFT (C-RLFT). This method leverages mixed-quality data without requiring preference labels, treating data sources as coarse-grained reward signals (OpenChat_Paper.pdf, p. 1).

### Model type:
The model is a `MistralForCausalLM`, a type of Transformer-based language model for causal language modeling (config.json). It is part of the OpenChat framework, which advances open-source language models (OpenChat_Paper.pdf, p. 1).

**Architecture Details:**
*   **Model Type:** `mistral` (config.json)
*   **Hidden Size:** 4096 (config.json)
*   **Number of Hidden Layers:** 32 (config.json)
*   **Number of Attention Heads:** 32 (config.json)
*   **Number of Key-Value Heads:** 8 (config.json)
*   **Intermediate Size:** 14336 (config.json)
*   **Hidden Activation Function:** `silu` (config.json)
*   **Sliding Window Attention:** 4096 tokens (config.json)
*   **Vocabulary Size:** 32002 (config.json)
*   **Maximum Context Length:** 8192 tokens (config.json)
*   **Model Size:** The model is a 13-billion parameter model (OpenChat_Paper.pdf, p. 1). The total size of its weights is approximately 14.48 GB (pytorch_model.bin.index.json).
*   **Data Type:** `bfloat16` (config.json)

### Training details:
The model was fine-tuned using a novel framework called **Conditioned-RLFT (C-RLFT)**, which is a single-stage, RL-free supervised learning method (OpenChat_Paper.pdf, p. 1). This approach regards different data sources (e.g., GPT-4 and GPT-3.5 conversations) as coarse-grained reward labels and learns a class-conditioned policy to leverage this quality information (OpenChat_Paper.pdf, p. 1, 4). The optimal policy is learned through a simple reward-weighted regression objective (OpenChat_Paper.pdf, p. 5).

**Key Parameters and Hyperparameters:**
*   **Base Model:** `imone/Mistral_7B_with_EOT_token` (config.json)
*   **Optimizer:** AdamW (OpenChat_Paper.pdf, p. 6)
*   **Learning Rate:** 1.2507e-05 (training_args.bin)
*   **Epochs:** 5 (training_args.bin)
*   **Batch Size per GPU:** 10 (training_args.bin)
*   **Sequence Length:** 4096 (OpenChat_Paper.pdf, p. 6)
*   **Weight Decay:** 0.1 (training_args.bin)
*   **Adam Beta1:** 0.9 (training_args.bin)
*   **Adam Beta2:** 0.95 (training_args.bin)
*   **Adam Epsilon:** 1e-05 (training_args.bin)
*   **Learning Rate Schedule:** Cosine schedule with a warmup ratio of 0.05 and a minimum learning rate ratio of 0.1 (training_args.bin; OpenChat_Paper.pdf, p. 6).
*   **Training Framework:** DeepSpeed was used for training (training_args.bin).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Title:** "OPENCHAT: ADVANCING OPEN-SOURCE LANGUAGE MODELS WITH MIXED-QUALITY DATA"
*   **Authors:** Guan Wang, Sijie Cheng, Xianyuan Zhan, Xiangang Li, Sen Song, Yang Liu
*   **Summary:** The paper introduces the OpenChat framework and the C-RLFT method for fine-tuning language models on mixed-quality data without preference labels. It presents extensive experiments showing the model's superior performance on various benchmarks (OpenChat_Paper.pdf).

Additional resources include:
*   **GitHub Repository:** https://github.com/imoneoi/openchat (OpenChat_Paper.pdf, p. 1)
*   **Hugging Face Repository:** https://huggingface.co/openchat (OpenChat_Paper.pdf, p. 1)

### Citation details:
Insufficient information.

### License:
Insufficient information.

### Contact:
For questions, issues, or feedback, you can contact the developers via email: `imonenext@gmail.com` or `csj23@mails.tsinghua.edu.cn` (OpenChat_Paper.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a general-purpose, instruction-following chatbot designed for conversational AI applications (OpenChat_Paper.pdf, p. 1, 6). Its primary purpose is to provide high-quality, helpful, and harmless responses to user instructions and questions across a variety of domains, including writing, roleplay, extraction, reasoning, mathematics, and coding (OpenChat_Paper.pdf, p. 1, 5).

The model is intended to be used in a chat format. The input is a sequence of messages with roles (e.g., 'User', 'Assistant'), and the model generates a response as the 'Assistant'. The specific format is defined by its chat template (tokenizer_config.json; OpenChat_Paper.pdf, p. 4).

### Primary intended users:
The primary intended users are AI researchers and developers interested in advancing and building upon open-source large language models (OpenChat_Paper.pdf, p. 10). The release of the model aims to democratize AI research and stimulate innovation within the community (OpenChat_Paper.pdf, p. 10).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model is intended to be used as a conversational agent. To achieve the best results during inference, prompts should be formatted according to the GPT-4 template used during training (OpenChat_Paper.pdf, p. 4). The model uses `<|end_of_turn|>` as its end-of-sequence token (tokenizer_config.json).

Below is a Python code snippet demonstrating how to use the model with the `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_name = "openchat/openchat-3.5-1210" # Example model name, replace with the correct one
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Format the prompt using the chat template
messages = [
    {"role": "user", "content": "Craft an intriguing opening paragraph for a fictional short story. The story should involve a character who wakes up one morning to find that they can time travel."}
]
# The tokenizer's apply_chat_template will format this correctly based on the template:
# "{{ bos_token }}{% for message in messages %}{{ 'GPT4 Correct ' + message['role'].title() + ': ' + message['content'] + '<|end_of_turn|>'}}{% endfor %}{% if add_generation_prompt %}{{ 'GPT4 Correct Assistant:' }}{% endif %}"
# (tokenizer_config.json)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Generate a response
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200, use_cache=True, do_sample=True, temperature=0.5, top_p=1.0)
response = tokenizer.decode(outputs[0, inputs.input_ids.shape[1]:], skip_special_tokens=True)

print(response)
```

**Sample Output:**
For the input prompt above, the model might generate a response like this:
> "As the first rays of sunlight peeked through the window, Sarah closed her eyes, relishing the warmth that caressed her face. She never could resist the allure of a beautiful morning, but this particular day was about to become anything but ordinary. With a start, she sat up in bed, her heart pounding, as she realized she was somewhere else, somewhere she had never been before. Confused and exhilarated, Sarah discovered that she had the extraordinary ability to time travel, her very first morning blessed - or perhaps cursed - with the power to traverse the fabric of time." (OpenChat_Paper.pdf, p. 18)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The most relevant factor identified during the model's development is the **quality of the training data**. The C-RLFT framework is explicitly designed to handle "mixed-quality data" by distinguishing between different data sources, such as high-quality "expert" data (from GPT-4) and lower-quality "sub-optimal" data (from GPT-3.5) (OpenChat_Paper.pdf, p. 1, 4). The model's performance is sensitive to the proportion and quality of this expert data (OpenChat_Paper.pdf, p. 9).

### Evaluation factors:
The model's evaluation was disaggregated based on the training data composition. The ablation studies analyzed performance under different data conditions:
*   Training with the full mixed-quality dataset (OpenChat_Paper.pdf, p. 8, Table 2).
*   Training using only the high-quality GPT-4 data subset (OpenChat_Paper.pdf, p. 8, Table 2).
*   Training using only the sub-optimal GPT-3.5 data subset (OpenChat_Paper.pdf, p. 8, Table 2).
*   Varying the sub-sample ratio of each data class from 60% to 100% to measure robustness (OpenChat_Paper.pdf, p. 9, Figure 6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using three primary metrics based on the benchmark being used:
1.  **Win Rate (%):** Used for pairwise comparisons where an LLM evaluator (e.g., GPT-4) compares the model's output against a baseline's output. The model receives 1 point for a win, 0.5 for a tie, and 0 for a loss. This was used for AlpacaEval and Vicuna-bench (OpenChat_Paper.pdf, p. 6).
2.  **Score:** Used for single-answer grading on a scale of 1 to 10, where an LLM evaluator judges the quality of the generated answer. This was used for MT-bench (OpenChat_Paper.pdf, p. 6).
3.  **Accuracy (%):** Used for multiple-choice exam questions in the AGIEval benchmark (OpenChat_Paper.pdf, p. 6).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Performance was measured using automatic evaluators. To ensure consistency and mitigate self-enhancement bias, multiple evaluators were used, including `gpt-4`, `gpt-3.5`, `claude-2`, and `alpaca_eval_gpt`. The correlation between these evaluators was analyzed to verify the consistency of the results (OpenChat_Paper.pdf, p. 6, 9).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on four standard benchmarks:
1.  **AlpacaEval:** A test set of 805 user instructions collected from diverse sources, with reference responses from `text-davinci-003` (OpenChat_Paper.pdf, p. 5, 15).
2.  **MT-bench:** A benchmark of 80 high-quality, multi-turn questions across eight topics: writing, roleplay, extraction, reasoning, mathematics, coding, and two knowledge categories (STEM and humanities/social science) (OpenChat_Paper.pdf, p. 5, 15).
3.  **Vicuna-bench:** A benchmark evaluating proficiency across eight question categories: generic, knowledge, roleplay, commonsense, Fermi problems, counterfactual scenarios, coding, mathematics, and writing (OpenChat_Paper.pdf, p. 5, 15).
4.  **AGIEval:** A collection of human-centric standardized exams, including English multiple-choice tasks from general college admission tests (SAT, AQUA-RAT), law school admission tests (LSAT), and civil service exams (LogiQA) (OpenChat_Paper.pdf, p. 5, 15).

### Motivation:
These datasets were chosen because they are "widely recognized benchmarks" for assessing instruction-following ability. AGIEval was specifically included to "verify the model generalization performance" on human-centric, standardized exams (OpenChat_Paper.pdf, p. 6).

### Preprocessing:
For the AGIEval benchmark, the official zero-shot prompt and answer matching methods were used. For conversational benchmarks (MT-bench, Vicuna-bench), the zero-shot prompt was formatted as the user's question within the model's conversation template (OpenChat_Paper.pdf, p. 6).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was fine-tuned on the **ShareGPT dataset**, which consists of approximately 70,000 user-shared conversations collected from `https://sharegpt.com/` (OpenChat_Paper.pdf, p. 2, 6). This dataset is of mixed quality and was divided into two subsets based on the source:
*   **Expert Data (`Dexp`):** Approximately 6,000 conversations generated by GPT-4 (OpenChat_Paper.pdf, p. 5).
*   **Sub-optimal Data (`Dsub`):** The remaining ~64,000 conversations generated by GPT-3.5 (OpenChat_Paper.pdf, p. 5).

### Motivation:
The ShareGPT dataset was chosen because it is a popular, widely-used SFT dataset that naturally contains mixed-quality data. This aligns with the project's goal of developing a framework to effectively fine-tune models on such data without requiring expensive human preference labels (OpenChat_Paper.pdf, p. 1, 3).

### Preprocessing:
The training data was preprocessed to create a "class-conditioned dataset" (OpenChat_Paper.pdf, p. 4). This involved:
1.  **Labeling:** Each conversation was labeled with its source class (`GPT-4` or `GPT-3.5`).
2.  **Templating:** The conversations were formatted using distinct templates for each class to condition the model. For example:
    *   **GPT-4 Template:** `GPT4 User: Question<|end_of_turn|>GPT4 Assistant:`
    *   **GPT-3.5 Template:** `GPT3 User: Question<|end_of_turn|>GPT3 Assistant:`
3.  **Special Tokens:** A new special token, `<|end_of_turn|>`, was added to differentiate between user and assistant utterances (OpenChat_Paper.pdf, p. 4; tokenizer.json).
4.  **Tokenization:** The data was tokenized and truncated to a maximum sequence length of 4096 tokens (OpenChat_Paper.pdf, p. 6).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides ablation studies that analyze the model's performance when trained on individual data sources (OpenChat_Paper.pdf, p. 8, Table 2).

**Performance on AlpacaEval (Win Rate % vs. `text-davinci-003`):**
*   Trained on only GPT-4 data (~6k samples): **85.8%**
*   Trained on only GPT-3.5 data (~64k samples): **76.5%**

**Performance on MT-bench (Score):**
*   Trained on only GPT-4 data (~6k samples): **33.4**
*   Trained on only GPT-3.5 data (~64k samples): **16.9**

**Performance on Vicuna-bench (Win Rate % vs. `gpt-3.5-turbo`):**
*   Trained on only GPT-4 data (~6k samples): **84.4%**
*   Trained on only GPT-3.5 data (~64k samples): **35.0%**

Figure 6 in the paper also analyzes the impact of sub-sampling each data source individually, showing that performance is more sensitive to the amount of high-quality GPT-4 data than the much larger GPT-3.5 dataset (OpenChat_Paper.pdf, p. 9).

### Intersectional results:
The main results of the `openchat-13b` model are based on training with the intersection of both GPT-4 and GPT-3.5 data using the C-RLFT method (OpenChat_Paper.pdf, p. 6, Table 1).

**Overall Performance (Average Win Rate %):**
*   **openchat-13b (full model):** 77.3%
*   **Ablation (w/o reward weighting):** 74.0%
*   **Ablation (w/o class-conditioning):** 60.5%

These results demonstrate that the combination of both data sources, leveraged through the class-conditioned policy and reward weighting, is crucial for achieving the model's top performance.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights are stored in `bfloat16` format (config.json). The total size of the model is approximately 14.48 GB (pytorch_model.bin.index.json). Therefore, loading the model requires at least 14.5 GB of RAM or VRAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training process utilized DeepSpeed, which suggests a multi-GPU setup (training_args.bin). The effective batch size was 200,000 tokens, with a per-GPU batch size of 10 and a sequence length of 4096, indicating a substantial hardware requirement (training_args.bin; OpenChat_Paper.pdf, p. 6). However, specific hardware details (e.g., number and type of GPUs) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers provide an Ethics Statement in their paper (OpenChat_Paper.pdf, p. 10), which includes the following points:

*   **Democratizing AI:** The study aims to advance open-source language models, which broadens accessibility to AI research and stimulates innovation from a diverse community of researchers.
*   **Safety and Fairness:** By refining the model's ability to follow instructions, the work can lead to more satisfying and safer responses, including the reduction of human bias and the promotion of fairness.
*   **Data Privacy:** The dataset used (ShareGPT) consists of publicly available, user-shared instances. This approach was chosen to minimize potential data leakage and privacy concerns. No sensitive or private data was used in the development of this model.
*   **Risks:** While not explicitly enumerated, the goal of improving instruction-following is framed as a step toward safer and more reliable models. The paper does not note any known risks associated with the model's use.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge several limitations and areas for future improvement (OpenChat_Paper.pdf, p. 10):
*   **Oversimplified Data Quality Assumption:** The assumption that data quality can be determined solely by its source (GPT-4 vs. GPT-3.5) is simplistic. The assigned coarse-grained rewards could be more finely tuned to reflect the actual quality of each data point.
*   **Focus on Instruction-Following:** The model was primarily developed and evaluated for its instruction-following capabilities. Its performance on complex reasoning tasks may be limited, and this is noted as a promising avenue for future work.
*   **Prompt Sensitivity:** The model's performance can decline if the prompt format used during inference does not match the one used during training (e.g., using the GPT-3.5 prompt instead of the GPT-4 prompt) (OpenChat_Paper.pdf, p. 8, Figure 5).

### Recommendations:
*   **Inference Prompting:** For optimal performance, users should format their prompts using the GPT-4 conversation template: `GPT4 User: Question<|end_of_turn|>GPT4 Assistant:` (OpenChat_Paper.pdf, p. 4).
*   **Multi-Turn Conversations:** To maintain consistency in multi-turn dialogues, it is recommended to repeat the condition prompt (e.g., `GPT4 User:`) at every turn, as models may "forget" the initial prompt in long contexts (OpenChat_Paper.pdf, p. 4, 14).