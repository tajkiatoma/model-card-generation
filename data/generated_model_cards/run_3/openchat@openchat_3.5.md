## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University, the Institute for AI Industry Research (AIR), and the Shanghai Artificial Intelligence Laboratory (Source: `arXiv_2309.11235v2.pdf`, page 1). The authors are Guan Wang, Sijie Cheng, Xianyuan Zhan, Xiangang Li, Sen Song, and Yang Liu (Source: `arXiv_2309.11235v2.pdf`, page 1).

### Model date:
The accompanying research paper was published as a conference paper at ICLR 2024. The version of the paper provided is dated March 16, 2024 (Source: `arXiv_2309.11235v2.pdf`, page 1).

### Model version:
The model version is `openchat_v3.2_mistral` (Source: `trainer_state.json`). It is an iteration of the OpenChat framework, which proposes a novel fine-tuning method called Conditioned-RLFT (C-RLFT) to leverage mixed-quality training data (Source: `arXiv_2309.11235v2.pdf`, page 1). The accompanying paper primarily discusses experiments on a 13B parameter model (`openchat-13b`), while the provided repository files correspond to this Mistral-7B based version (Source: `config.json`, `arXiv_2309.11235v2.pdf`, page 6).

### Model type:
The model is a `MistralForCausalLM`, a type of decoder-only Transformer architecture designed for causal language modeling (text generation) (Source: `config.json`). It has been fine-tuned for instruction-following and conversational abilities (Source: `tokenizer_config.json`, `arXiv_2309.11235v2.pdf`, page 1).

**Architecture Details:**
*   **Base Model:** `imone/Mistral_7B_with_EOT_token` (Source: `config.json`).
*   **Layers:** 32 hidden layers (Source: `config.json`).
*   **Attention Heads:** 32 attention heads for queries, and 8 heads for keys/values (Grouped-Query Attention) (Source: `config.json`).
*   **Hidden Size:** 4096 (Source: `config.json`).
*   **Intermediate Size:** 14336 (Source: `config.json`).
*   **Activation Function:** SiLU ("silu") (Source: `config.json`).
*   **Context Length:** The model supports a maximum position embedding of 8192 tokens, with a sliding window attention of 4096 tokens (Source: `config.json`).
*   **Vocabulary Size:** 32,002 (Source: `config.json`).
*   **Model Size:** The total size of the model weights is 14,483,496,960 bytes (~14.5 GB), which corresponds to a 7B parameter model stored in `bfloat16` format (Source: `pytorch_model.bin.index.json`, `config.json`).

### Training details:
The model was fine-tuned using the **Conditioned-Reinforcement Learning Fine-Tuning (C-RLFT)** method. C-RLFT is a framework designed to leverage mixed-quality data by treating data from different sources (e.g., GPT-4, GPT-3.5) as distinct classes with coarse-grained reward labels. The model learns a class-conditioned policy, which can be optimized via a simple, RL-free, reward-weighted regression objective (Source: `arXiv_2309.11235v2.pdf`, pages 1, 4-5).

**Hyperparameters:**
*   **Optimizer:** AdamW with `beta1=0.9`, `beta2=0.95`, and `eps=1e-05` (Source: `trainer_state.json`).
*   **Learning Rate:** 1.2507232220003032e-05, with a warmup ratio of 0.05 and decay to 10% of the max value (`lr_min_ratio: 0.1`) (Source: `trainer_state.json`).
*   **Epochs:** 5 (Source: `trainer_state.json`).
*   **Batch Size:** 10 per GPU (Source: `trainer_state.json`).
*   **Weight Decay:** 0.1 (Source: `trainer_state.json`).
*   **Framework:** Training was performed using DeepSpeed (Source: `trainer_state.json`).

### Paper or other resource for more information:
The model and its training methodology are described in the paper:
*   **Title:** OPENCHAT: ADVANCING OPEN-SOURCE LANGUAGE MODELS WITH MIXED-QUALITY DATA
*   **Summary:** The paper introduces the OpenChat framework and the C-RLFT method for fine-tuning language models on data of varying quality. It presents extensive experiments on benchmarks, demonstrating that this approach achieves state-of-the-art performance among open-source models of similar size.
*   **Links:**
    *   Paper: `arXiv:2309.11235v2`
    *   Code and Models: The paper provides links to a GitHub repository (`https://github.com/imoneoi/openchat`) and a Hugging Face organization (`https://huggingface.co/openchat`) (Source: `arXiv_2309.11235v2.pdf`, page 1).

### Citation details:
Insufficient information.

### License:
Insufficient information.

### Contact:
For questions or feedback, the authors of the paper can be contacted at `imonenext@gmail.com` or `csj23@mails.tsinghua.edu.cn` (Source: `arXiv_2309.11235v2.pdf`, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for use as a general-purpose, instruction-following conversational agent (Source: `tokenizer_config.json`, `arXiv_2309.11235v2.pdf`, page 1). It is designed to provide high-quality responses by leveraging its training on mixed-quality data sources. The model's input-output structure is a multi-turn chat format, where a user provides a series of messages and the model generates a response (Source: `tokenizer_config.json`). During inference, it is recommended to use the template associated with the higher-quality training data (i.e., the "GPT-4" template) to generate better responses (Source: `arXiv_2309.11235v2.pdf`, page 5).

### Primary intended users:
The primary intended users are researchers and developers in the field of artificial intelligence. The project aims to democratize AI research by providing an accessible, transparent, and high-performing open-source model that stimulates innovation and collaboration (Source: `arXiv_2309.11235v2.pdf`, page 10).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model should be used in a conversational format. The provided `tokenizer_config.json` specifies a chat template for formatting conversations. Users should structure their input as a list of messages, each with a `role` and `content`. The special token `<|end_of_turn|>` is used to signal the end of a turn.

Below is a Python code snippet demonstrating how to use the model with the `transformers` library:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the model and tokenizer
model_name = "openchat/openchat_v3.2" # Use the correct model name on Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16, # As specified in config.json
    device_map="auto"
)

# Format the conversation using the chat template
messages = [
    {"role": "user", "content": "Hello! Can you write a short poem about the ocean?"}
]
# The tokenizer will apply the template: "GPT4 Correct User: Hello! Can you write a short poem about the ocean?<|end_of_turn|>GPT4 Correct Assistant:"
inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to(model.device)

# Generate a response
outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, temperature=0.5)
response = tokenizer.decode(outputs[0], skip_special_tokens=False)

print(response)
```
**Sample Output Structure:**
The model's output will continue the formatted prompt, generating text for the assistant's turn and concluding with the end-of-turn token.

`<s> GPT4 Correct User: Hello! Can you write a short poem about the ocean?<|end_of_turn|> GPT4 Correct Assistant: A canvas vast, of deepest blue,
Where sunlit diamonds dance in view.
With every wave, a whispered lore,
Upon the sands of a timeless shore.<|end_of_turn|>`

(Source: `tokenizer_config.json`, `config.json`, `arXiv_2309.11235v2.pdf`, page 5)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data Quality:** The core of the model's training methodology revolves around distinguishing between different qualities of data. The model's performance is influenced by the mix of "expert" (e.g., from GPT-4) and "sub-optimal" (e.g., from GPT-3.5) data it was trained on (Source: `arXiv_2309.11235v2.pdf`, page 4).
*   **Data Size:** The performance is robust to variations in data size, but the amount of high-quality expert data is shown to be particularly important, even when it constitutes a small fraction of the total dataset (Source: `arXiv_2309.11235v2.pdf`, page 9).
*   **Inference Prompting:** The model's output quality is sensitive to the prompt template used during inference. Using the prompt template associated with the high-quality data source (`GPT-4`) leads to significantly better performance than using the template for the lower-quality source (`GPT-3.5`) (Source: `arXiv_2309.11235v2.pdf`, page 8).

### Evaluation factors:
The model was evaluated on a range of standardized benchmarks that test different capabilities:
*   **Instruction Following and Conversational Ability:** Assessed using AlpacaEval, MT-bench, and Vicuna-bench (Source: `arXiv_2309.11235v2.pdf`, page 5).
*   **Domain-Specific Knowledge and Reasoning:** Evaluated across topics like writing, reasoning, mathematics, coding, STEM, and humanities (Source: `arXiv_2309.11235v2.pdf`, page 15).
*   **Generalization:** Tested using the AGIEval benchmark, which includes tasks from standardized exams like the SAT and LSAT (Source: `arXiv_2309.11235v2.pdf`, page 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to evaluate the model's performance on various benchmarks:
*   **Win Rate (%):** Used for pairwise comparisons against baseline models (e.g., `text-davinci-003`, `gpt-3.5-turbo`). The tested model receives 1 point for a win, 0.5 for a tie, and 0 for a loss (Source: `arXiv_2309.11235v2.pdf`, pages 5-6).
*   **Score:** For single-answer grading in MT-bench, an LLM evaluator assigns a score from 1 to 10 to the model's generated answer (Source: `arXiv_2309.11235v2.pdf`, page 6).
*   **Accuracy:** Used for multiple-choice questions in the AGIEval benchmark (Source: `arXiv_2309.11235v2.pdf`, page 6).

### Decision thresholds:
Insufficient information.

### Variation approaches:
The paper does not report using statistical methods like cross-validation or bootstrapping for the main results. However, it analyzes the consistency of the automatic evaluators (GPT-4, GPT-3.5, Claude-2) by computing the Pearson correlation (r) between their evaluation scores on the AlpacaEval benchmark (Source: `arXiv_2309.11235v2.pdf`, page 16, Appendix E).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on four standard, publicly available benchmarks:
*   **AlpacaEval:** A benchmark for instruction-following that includes a test set of 805 user instructions (Source: `arXiv_2309.11235v2.pdf`, page 15).
*   **MT-bench:** A multi-turn benchmark with 80 high-quality questions covering eight topics: writing, roleplay, extraction, reasoning, mathematics, coding, STEM knowledge, and humanities/social science knowledge (Source: `arXiv_2309.11235v2.pdf`, page 15).
*   **Vicuna-bench:** A benchmark evaluating proficiency across eight categories: generic, knowledge, roleplay, commonsense, Fermi problems, counterfactual scenarios, coding, mathematics, and writing (Source: `arXiv_2309.11235v2.pdf`, page 15).
*   **AGIEval:** A collection of human-centric standardized tests, including English multiple-choice tasks from college admission tests (SAT, AQUA-RAT), law school admission tests (LSAT), and civil service exams (LogiQA) (Source: `arXiv_2309.11235v2.pdf`, page 15).

### Motivation:
These datasets were chosen because they are widely recognized benchmarks for assessing the instruction-following ability, conversational skills, and generalization performance of large language models in a standardized manner (Source: `arXiv_2309.11235v2.pdf`, page 5).

### Preprocessing:
For the AGIEval benchmark, the official zero-shot prompt and answer matching methodology was used. For conversational models, the prompts were formatted using their respective conversation templates (Source: `arXiv_2309.11235v2.pdf`, page 16, Appendix F). No other specific preprocessing steps for the evaluation data were described.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was fine-tuned on the **ShareGPT dataset** (Source: `arXiv_2309.11235v2.pdf`, page 5).
*   **Size:** The dataset contains approximately 70,000 user-shared conversations (Source: `arXiv_2309.11235v2.pdf`, page 5).
*   **Structure and Diversity:** The dataset is of mixed quality, comprising two distinct sources:
    *   Approximately 6,000 "expert" conversations generated by GPT-4.
    *   The remaining ~64,000 "sub-optimal" conversations generated by GPT-3.5.
    (Source: `arXiv_2309.11235v2.pdf`, page 5).
*   The tokenized version of the data used for this specific training run is referenced as `dataset_openchat3.5/tokenized/openchat_mistral_1017` (Source: `trainer_state.json`).

### Motivation:
The ShareGPT dataset was chosen because its mixed-quality composition (GPT-4 and GPT-3.5 conversations) makes it ideal for developing and testing the C-RLFT framework, which is designed to effectively learn from such data without requiring costly human preference labels (Source: `arXiv_2309.11235v2.pdf`, page 3).

### Preprocessing:
The key preprocessing step is the application of the C-RLFT method's class-conditioning:
*   Data from different sources (GPT-4 and GPT-3.5) were assigned distinct class labels (Source: `arXiv_2309.11235v2.pdf`, page 4).
*   Each training example was formatted using a conversation template specific to its source class to create a class-conditioned policy.
    *   **GPT-4 Template:** `GPT4 User: Question<|end_of_turn|>GPT4 Assistant:`
    *   **GPT-3.5 Template:** `GPT3 User: Question<|end_of_turn|>GPT3 Assistant:`
    (Source: `arXiv_2309.11235v2.pdf`, page 4).
*   A new special token, `<|end_of_turn|>`, was added to the vocabulary to separate utterances from different speakers (Source: `arXiv_2309.11235v2.pdf`, page 4; `special_tokens_map.json`).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the `openchat-13b` model (a Llama-2-13B variant trained with the same method) is reported across several benchmarks:
*   **Average Win Rate:** 77.3% across AlpacaEval, MT-bench, and Vicuna-bench (Source: `arXiv_2309.11235v2.pdf`, page 6, Table 1).
    *   AlpacaEval: 89.5%
    *   MT-bench: 57.5%
    *   Vicuna-bench: 85.0%
*   **AGIEval Average Accuracy:** 36.4% across all English tasks (Source: `arXiv_2309.11235v2.pdf`, page 16, Table 5).
    *   AQUA-RAT: 19.3%
    *   LogiQA: 34.9%
    *   LSAT-AR: 19.1%
    *   LSAT-LR: 37.5%
    *   LSAT-RC: 45.0%
    *   SAT-English: 66.0%
    *   SAT-Math: 30.9%

### Intersectional results:
The paper provides an ablation study analyzing the impact of the two key components of the C-RLFT method: coarse-grained rewards and the class-conditioned policy. The results are for the `openchat-13b` model.

| Model Configuration | AlpacaEval Win Rate | MT-bench Win Rate | Vicuna-bench Win Rate | Average Win Rate |
| :--- | :--- | :--- | :--- | :--- |
| **openchat-13b (full model)** | 89.5 | 57.5 | 85.0 | **77.3** |
| w/o reward | 89.1 | 52.8 | 80.0 | 74.0 |
| w/o condition | 79.1 | 38.1 | 64.4 | 60.5 |

(Source: `arXiv_2309.11235v2.pdf`, page 8, Table 2)

This analysis shows that both the reward mechanism and the class-conditioning are critical for the model's final performance, with the class-conditioned policy having a particularly significant impact.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model is stored in `bfloat16` precision (Source: `config.json`). The total size of the weights is approximately 14.5 GB (Source: `pytorch_model.bin.index.json`). Therefore, loading the model requires at least 15 GB of RAM or VRAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained using the DeepSpeed library, which is designed for large-scale model training (Source: `trainer_state.json`). The save path in the training state (`/ML-A100/home/...`) strongly suggests that the model was trained on NVIDIA A100 GPUs (Source: `trainer_state.json`).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The authors provide an "Ethics Statement" in the research paper (Source: `arXiv_2309.11235v2.pdf`, page 10).
*   **Data Privacy:** The training dataset consists of publicly available, user-shared conversations. The authors state that this approach helps minimize potential data leakage and privacy concerns.
*   **Bias and Fairness:** The paper suggests that refining the instruction-following capabilities of models can lead to safer responses, including "the reduction of human bias and the promotion of fairness."
*   **Openness and Accessibility:** The study aims to advance open-source language models to democratize AI research. The authors believe that open, transparent platforms stimulate innovation, broaden accessibility, and foster a dynamic research community that can lead to more comprehensive discussions and faster progress.

No specific risks, potential harms, or affected groups are explicitly detailed. The focus is on the positive societal benefits of developing more capable and accessible open-source models.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors acknowledge several limitations and areas for future work:
*   **Oversimplified Data Quality Assumption:** The method assumes data quality is uniform within a source (e.g., all GPT-4 data is "expert"). This may be an oversimplification, as the actual quality of individual data points can vary (Source: `arXiv_2309.11235v2.pdf`, page 10).
*   **Coarse-Grained Rewards:** The rewards assigned to data sources are coarse-grained. The authors suggest that performance could be improved if rewards were more finely tuned to reflect the quality of each specific data point (Source: `arXiv_2309.11235v2.pdf`, page 10).
*   **Focus on Instruction Following:** The model was primarily developed to enhance instruction-following capabilities. Its reasoning abilities were not the main focus, and improving this aspect is noted as a promising area for future research (Source: `arXiv_2309.11235v2.pdf`, page 10).

### Recommendations:
*   **Use the High-Quality Prompt Template:** For best results during inference, users should format their prompts using the template associated with the high-quality data source (the "GPT-4" template), as this was shown to produce significantly better responses (Source: `arXiv_2309.11235v2.pdf`, pages 5, 8).
*   **Be Aware of Limitations:** Users should be aware of the model's caveats, particularly that its primary strength is instruction-following rather than complex reasoning, and that its knowledge is based on the quality and content of its training data.