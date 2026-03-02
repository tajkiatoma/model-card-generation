## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Microsoft and Hong Kong Baptist University (WizardCoder_paper.md, page 1). The authors are:
*   Ziyang Luo (Hong Kong Baptist University)
*   Can Xu (Microsoft)
*   Pu Zhao (Microsoft)
*   Qingfeng Sun (Microsoft)
*   Xiubo Geng (Microsoft)
*   Wenxiang Hu (Microsoft)
*   Chongyang Tao (Microsoft)
*   Jing Ma (Hong Kong Baptist University)
*   Qingwei Lin (Microsoft)
*   Daxin Jiang (Microsoft)

(WizardCoder_paper.md, page 1).

### Model date:
The academic paper describing the model was published as a conference paper at ICLR 2024. The arXiv version (v2) is dated May 27, 2025, though this appears to be a typo in the source document, likely meaning 2023 or 2024 (WizardCoder_paper.md, page 1).

### Model version:
The model is named WizardCoder. This model card describes a version based on the StarCoder 15B model (`config.json`, key: `"_name_or_path": "bigcode/starcoder"`). The paper also describes another version based on CodeLlama-34B (WizardCoder_paper.md, page 5). WizardCoder models are created by fine-tuning foundation models (like StarCoder) using the "Code Evol-Instruct" method, which enhances the complexity of code instructions to improve performance on code-related tasks (WizardCoder_paper.md, pages 1, 2).

### Model type:
The model is a `GPTBigCodeForCausalLM`, a type of large language model for code generation, based on the GPT architecture (`config.json`, keys: `architectures`, `model_type`). It is an instruction-tuned model designed for code-related tasks (WizardCoder_paper.md, page 1).

**Architecture Details:**
*   **Model Type:** gpt_bigcode (`config.json`, key: `model_type`)
*   **Activation Function:** gelu (`config.json`, key: `activation_function`)
*   **Layers:** 40 (`config.json`, key: `n_layer`)
*   **Attention Heads:** 48 (`config.json`, key: `n_head`)
*   **Embedding Size:** 6144 (`config.json`, key: `n_embd`)
*   **Vocabulary Size:** 49153 (`config.json`, key: `vocab_size`)
*   **Context Length:** 8192 tokens (`config.json`, key: `n_positions`)
*   **Attention Mechanism:** Multi-Query Attention (`config.json`, key: `multi_query`)

**Tokenizer:**
*   **Type:** Byte-Pair Encoding (BPE) (`tokenizer.json`, key: `model.type`)
*   **Pre-tokenization:** Digits are split into individual digits, followed by ByteLevel pre-tokenization (`tokenizer.json`, key: `pre_tokenizer`)
*   **Special Tokens:** The tokenizer includes additional special tokens for handling code structures, such as `<fim_prefix>`, `<fim_middle>`, `<fim_suffix>` for fill-in-the-middle tasks, and tokens for representing file structure, GitHub metadata, and Jupyter notebooks like `<filename>`, `<gh_stars>`, `<jupyter_code>`, etc. (`special_tokens_map.json`; `tokenizer.json`, key: `special_tokens`).

### Training details:
The model was created by fine-tuning a pre-trained StarCoder 15B model (WizardCoder_paper.md, page 5). The fine-tuning process used a novel instruction-following dataset for code, generated through a method called **Code Evol-Instruct** (WizardCoder_paper.md, page 1).

**Code Evol-Instruct:**
This is an automated method to enhance the complexity and diversity of code instructions. It starts with an initial dataset (Code Alpaca) and iteratively evolves the instructions using GPT-3.5-turbo based on specific heuristics (WizardCoder_paper.md, pages 4, 5). The evolution methods include:
1.  Adding new constraints and requirements.
2.  Replacing a common requirement with a less common one.
3.  Adding more reasoning steps.
4.  Providing a piece of erroneous code to increase misdirection.
5.  Proposing higher time or space complexity requirements (WizardCoder_paper.md, page 5).

**Fine-tuning Hyperparameters:**
*   **Batch Size:** 512 (WizardCoder_paper.md, page 6)
*   **Sequence Length:** 2048 (WizardCoder_paper.md, page 6)
*   **Learning Rate:** 2e-5 with a Cosine scheduler (WizardCoder_paper.md, page 6)
*   **Warmup Steps:** 30 (WizardCoder_paper.md, page 6)
*   **Total Steps:** 200 (WizardCoder_paper.md, page 6)
*   **Precision:** fp16 mixed precision (WizardCoder_paper.md, page 6)
*   **Dropout:** Attention dropout (`attn_pdrop`) is 0.1, embedding dropout (`embd_pdrop`) is 0.1, and residual dropout (`resid_pdrop`) is 0.1 (`config.json`).

### Paper or other resource for more information:
The primary resource is the academic paper: "WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT" by Ziyang Luo, Can Xu, et al., published as a conference paper at ICLR 2024 (WizardCoder_paper.md, page 1). The paper details the Code Evol-Instruct method, the training process, and comprehensive experimental results.

### Citation details:
The paper has been accepted to ICLR 2024. The authors recommend citing the ICLR version (WizardCoder_paper.md, page 1). A BibTeX entry can be constructed from the paper's title and author list.

### License:
Insufficient information

### Contact:
Contact information for the authors is provided in the academic paper:
*   `{cszyluo, majing}@comp.hkbu.edu.hk`
*   `{caxu,puzhao}@microsoft.com`
*   `{qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com`

(WizardCoder_paper.md, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for code generation and code-related tasks. It is designed to follow complex instructions to generate code in various programming languages (WizardCoder_paper.md, pages 1, 7). The model can be used for tasks such as:
*   Generating Python scripts based on problem descriptions (WizardCoder_paper.md, page 16).
*   Solving programming problems that require specific constraints, requirements, or reasoning steps (WizardCoder_paper.md, page 5).
*   Code generation for data science tasks involving libraries like pandas, numpy, and matplotlib (WizardCoder_paper.md, page 8).
*   Code generation in multiple languages including Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (WizardCoder_paper.md, page 7).

The model takes an instruction describing a task as input and outputs the corresponding code to complete the request (WizardCoder_paper.md, page 5).

### Primary intended users:
The paper does not explicitly state the primary intended users, but based on the model's capabilities, the target audience includes software developers, data scientists, and researchers in the field of AI and code generation.

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model is designed to follow instructions for code generation. The prompt format for fine-tuning and inference follows a specific structure, as shown below (WizardCoder_paper.md, page 5):

**Prompt Format:**
```
Below is an instruction that describes a task, paired with an input that provides further
context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```
Where `{instruction}` is the user's request for code generation.

**Example 1: Zero-Shot Prompt for HumanEval** (WizardCoder_paper.md, page 16)
*   **Input:**
    ```
    Below is an instruction that describes a task, paired with an input that provides further
    context. Write a response that appropriately completes the request.

    ### Instruction:
    Create a Python script for this problem:
    {Question}

    ### Response:
    ```
*   **Output:** A Python script that solves the `{Question}`.

**Example 2: Three-Shot Prompt for MBPP** (WizardCoder_paper.md, page 16)
*   **Input:**
    ```
    Below is an instruction that describes a task, paired with an input that provides further
    context. Write a response that appropriately completes the request.

    ### Instruction:
    Create a Python script for this problem:
    {Question}
    {Test Example 1}
    {Test Example 2}
    {Test Example 3}

    ### Response:
    ```
*   **Output:** A Python script that solves the `{Question}` and passes the test examples.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Instruction Complexity:** The paper identifies instruction complexity as a pivotal factor in achieving exceptional coding performance. The Code Evol-Instruct method was specifically designed to increase the complexity of training instructions (WizardCoder_paper.md, pages 1, 9).
*   **Programming Language:** The model's performance varies across different programming languages, as shown in the MultiPL-E benchmark results (WizardCoder_paper.md, page 8, Table 2).
*   **Task Domain:** Performance also varies by the specific domain of the coding task, such as data science workflows involving different libraries (e.g., pandas, numpy, scikit-learn) (WizardCoder_paper.md, page 8, Table 3).

### Evaluation factors:
The model's performance was evaluated and reported based on the following factors:
*   **Programming Language:** The evaluation on the MultiPL-E benchmark was disaggregated by 8 languages: Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (WizardCoder_paper.md, page 8, Table 2).
*   **Data Science Library:** The evaluation on the DS-1000 benchmark was disaggregated by 7 Python libraries: Matplotlib, Numpy, Pandas, PyTorch, Scipy, Scikit-learn, and Tensorflow (WizardCoder_paper.md, page 8, Table 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's performance is **pass@1**. This metric measures the percentage of problems for which a correct solution is generated in a single attempt (WizardCoder_paper.md, pages 2, 7).

### Decision thresholds:
Insufficient information

### Variation approaches:
Two approaches were used to estimate the pass@1 score:
1.  **Greedy Decoding:** For benchmarks like HumanEval and HumanEval+, a single answer is generated using greedy decoding, and the pass rate is reported (WizardCoder_paper.md, page 6).
2.  **Sampling:** For benchmarks like the original HumanEval and MBPP, `n=200` samples are generated for each problem to estimate the pass@1 score, following the methodology of previous works. The hyperparameters for this sampling are `temperature=0.2` and `top_p=0.95` (WizardCoder_paper.md, page 7). For the DS-1000 benchmark, `n=40` samples were used (WizardCoder_paper.md, page 8).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five prominent code generation benchmarks (WizardCoder_paper.md, page 1):
*   **HumanEval:** Comprises 164 Python programming problems with an average of 9.6 test cases each (WizardCoder_paper.md, page 6).
*   **HumanEval+:** An extension of HumanEval that significantly increases the number of test cases to an average of 774.8 per problem for more rigorous evaluation (WizardCoder_paper.md, page 6).
*   **MBPP (Mostly Basic Python Programming):** Contains 500 test programming problems, each with three automated test cases (WizardCoder_paper.md, page 6).
*   **DS-1000:** A benchmark with 1,000 distinct data science problems spanning 7 libraries (e.g., NumPy, Pandas, Matplotlib). It supports both completion and insertion evaluation modes (WizardCoder_paper.md, pages 7, 8).
*   **MultiPL-E:** A benchmark for assessing performance across 8 distinct programming languages: Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (WizardCoder_paper.md, page 7).

### Motivation:
These datasets were chosen because they are "prominent code generation benchmarks" and "key benchmarks in the Code LLM field," allowing for comprehensive comparison against other state-of-the-art closed-source and open-source models (WizardCoder_paper.md, pages 1, 6). HumanEval+ is used for its rigorousness, while DS-1000 and MultiPL-E are used to assess performance in data science and multilingual contexts, respectively (WizardCoder_paper.md, pages 6, 7).

### Preprocessing:
The evaluation prompts were formatted specifically for each benchmark to ensure fair comparison and adherence to the benchmark's requirements (WizardCoder_paper.md, page 16).
*   For HumanEval, HumanEval+, and DS-100 (Completion), a zero-shot prompt format was used.
*   For MBPP, a three-shot prompt format including test examples was used.
*   For DS-1000 (Insertion) and MultiPL-E, the prompt format was aligned with the one used by the StarCoder model and its evaluation harness to ensure compatibility (WizardCoder_paper.md, page 16).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training process started with the **Code Alpaca** dataset, which contains around 20,000 instruction-following samples (WizardCoder_paper.md, page 5). This initial dataset was then iteratively evolved using the **Code Evol-Instruct** method, resulting in a final training dataset of approximately 78,000 samples (WizardCoder_paper.md, page 6).

### Motivation:
The motivation for creating a new training dataset was to automatically increase the complexity and diversity of code instructions. The goal was to better leverage the internal coding capabilities of the base Code LLMs (StarCoder), as preliminary studies indicated that instruction complexity is key to achieving exceptional coding performance (WizardCoder_paper.md, pages 1, 2).

### Preprocessing:
The training data was generated through an iterative evolution process called **Code Evol-Instruct**. This involved using OpenAI's `gpt-3.5-turbo` model to rewrite and complicate instructions from the Code Alpaca dataset based on a set of code-specific heuristics (WizardCoder_paper.md, pages 4, 5).

Additionally, a data filtering step was implemented to prevent data leakage from the test sets. This involved using the `gte-large` embedding model to retrieve the top 5 most similar training samples for each test sample, and then using GPT-4 to perform a binary classification ("yes" or "no") to determine if there was a match. Samples that matched were excluded from the training data (WizardCoder_paper.md, page 17).

The tokenizer uses Byte-Pair Encoding (BPE) with ByteLevel pre-tokenization (`tokenizer.json`, keys: `model`, `pre_tokenizer`).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by individual factors.

**Performance by Programming Language (pass@1 % on MultiPL-E):** (WizardCoder_paper.md, page 8, Table 2)
*   Java: 35.8
*   JavaScript: 41.9
*   C++: 39.0
*   PHP: 39.3
*   R: 33.5
*   Julia: 34.0
*   Swift: 33.7
*   Rust: 27.1

**Performance by Data Science Library (pass@1 % on DS-1000, Insertion):** (WizardCoder_paper.md, page 8, Table 3)
*   Matplotlib: 55.2
*   Numpy: 35.1
*   Pandas: 20.4
*   PyTorch: 30.4
*   Scipy: 28.9
*   Scikit-learn: 32.3
*   Tensorflow: 37.8

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
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model's performance, while state-of-the-art among open-source models at the time of publication, still "falls significantly behind the SOTA LLM, GPT4" (WizardCoder_paper.md, page 9).
*   The evaluation on the DS-1000 benchmark for the 34B model version faced challenges in aligning with the framework, so only the 15B model results were included for that specific benchmark (WizardCoder_paper.md, page 8, footnote 6).

### Recommendations:
*   The authors state that "future work will further augment the performance of our model," suggesting that there is room for improvement (WizardCoder_paper.md, page 9).
*   The paper's analysis underscores the "pivotal role of instruction complexity in enhancing performance," recommending that future work in this area should focus on this aspect (WizardCoder_paper.md, page 9).