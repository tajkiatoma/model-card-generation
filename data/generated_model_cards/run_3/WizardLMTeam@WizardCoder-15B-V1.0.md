## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Microsoft and Hong Kong Baptist University (Source: paper.pdf, page 1). The authors are:
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

Contact emails provided are {cszyluo, majing}@comp.hkbu.edu.hk and {caxu,puzhao,qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com (Source: paper.pdf, page 1).

### Model date:
The associated paper was published as a conference paper at ICLR 2024. The second version of the paper was submitted to arXiv on May 27, 2025 (Source: paper.pdf, page 1).

### Model version:
The model is named WizardCoder. The repository contains information for different versions, including WizardCoder 15B and WizardCoder 34B (Source: paper.pdf, page 7). These models are instruction fine-tuned versions of open-source Code LLMs (StarCoder and CodeLlama) (Source: paper.pdf, page 2). They were developed to enhance performance on code-related tasks and have been shown to outperform other open-source models like CodeLlama-Instruct, OctoCoder, and InstructCodeT5+ on various benchmarks (Source: paper.pdf, pages 1, 7).

### Model type:
WizardCoder is a Code Large Language Model (Code LLM) based on the GPT-BigCode architecture (Source: config.json; paper.pdf, page 1). It is a decoder-only transformer model designed for code generation tasks (Source: paper.pdf, page 1).

Key architectural details include:
*   **Architecture:** GPTBigCodeForCausalLM (Source: config.json).
*   **Vocabulary Size:** 49,153 (Source: config.json).
*   **Context Length (n_positions):** 8192 tokens (Source: config.json).
*   **Number of Layers (n_layer):** 40 (Source: config.json).
*   **Number of Attention Heads (n_head):** 48 (Source: config.json).
*   **Embedding Size (n_embd):** 6144 (Source: config.json).
*   **Activation Function:** GELU (Source: config.json).
*   **Attention Mechanism:** Multi-Query Attention (Source: config.json).

### Training details:
The model was trained using a novel instruction fine-tuning approach called **Code Evol-Instruct**, which is specifically adapted for the coding domain (Source: paper.pdf, page 1).

**Training Process:**
1.  **Initial Dataset:** The process started with the Code Alpaca dataset, which contains around 20,000 instruction-following samples (Source: paper.pdf, page 5).
2.  **Instruction Evolution:** The Code Evol-Instruct method was used to iteratively evolve and complexify the initial instruction dataset. This was done using OpenAI's `gpt-3.5-turbo` to generate more complex instructions based on simpler ones (Source: paper.pdf, page 6). The evolution process incorporated several heuristics, such as adding new constraints, replacing common requirements with more specific ones, adding reasoning steps, providing erroneous code for misdirection, and proposing higher time/space complexity requirements (Source: paper.pdf, pages 4, 5).
3.  **Fine-tuning:** The base models (StarCoder 15B and CodeLlama-34B-Python) were fine-tuned on the newly generated dataset of approximately 78,000 samples (Source: paper.pdf, pages 5, 6).

**Hyperparameters for Fine-tuning:**
*   **Batch Size:** 512 (Source: paper.pdf, page 6).
*   **Sequence Length:** 2048 (Source: paper.pdf, page 6).
*   **Learning Rate:** 2e-5 (Source: paper.pdf, page 6).
*   **Learning Rate Scheduler:** Cosine (Source: paper.pdf, page 6).
*   **Warmup Steps:** 30 (Source: paper.pdf, page 6).
*   **Fine-tuning Steps:** 200 (Source: paper.pdf, page 6).
*   **Precision:** fp16 mixed precision (Source: paper.pdf, page 6).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   **Title:** WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT (Source: paper.pdf, page 1).
*   **Summary:** The paper introduces the Code Evol-Instruct method for enhancing Code LLMs. It details the creation of the WizardCoder models and presents comprehensive experiments showing their superior performance on five code generation benchmarks compared to other open-source and some closed-source models (Source: paper.pdf, page 1).
*   **Link:** The paper is available on arXiv at `arXiv:2306.08568v2` (Source: paper.pdf, page 1).

### Citation details:
Insufficient information.

### License:
Insufficient information.

### Contact:
For questions or feedback, the developers can be contacted via the following emails provided in the research paper (Source: paper.pdf, page 1):
*   {cszyluo, majing}@comp.hkbu.edu.hk
*   {caxu,puzhao,qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for code-related tasks, including code understanding and generation (Source: paper.pdf, page 1). It is designed to be a powerful open-source Code LLM that can follow complex instructions to produce correct and efficient code across multiple programming languages (Source: paper.pdf, pages 1, 7).

The model takes a natural language instruction describing a coding task as input and outputs a code snippet that completes the request (Source: paper.pdf, page 5).

### Primary intended users:
The paper does not explicitly define the primary users, but based on the model's capabilities for code generation and its evaluation on academic benchmarks, the intended users are likely AI researchers, software developers, and data scientists who work with code generation and program synthesis.

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model. 

The model is fine-tuned on instructions following a specific format. To use the model for inference, prompts should be structured similarly (Source: paper.pdf, page 5).

**Prompt Format:**
```
Below is an instruction that describes a task, paired with an input that provides further
context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```
Here, `{instruction}` should be replaced with the natural language description of the coding task (Source: paper.pdf, page 5).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary factor influencing the model's performance is the complexity of the instructions it is trained on. The Code Evol-Instruct method was specifically designed to increase instruction complexity to improve coding performance (Source: paper.pdf, pages 1, 9). Other relevant factors include the programming language and the specific domain of the coding task (e.g., data science libraries) (Source: paper.pdf, page 8).

### Evaluation factors:
The model's performance was evaluated across several factors:
*   **Programming Language:** Performance was measured on Python, Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: paper.pdf, page 8, Table 2).
*   **Data Science Libraries:** For Python, performance was disaggregated by data science libraries, including Matplotlib, Numpy, Pandas, Pytorch, Scipy, Sklearn, and Tensorflow (Source: paper.pdf, page 8, Table 3).
*   **Instruction Complexity:** The model's performance gain is attributed to the increased complexity of the training instructions (Source: paper.pdf, page 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's performance is **pass@1** (Source: paper.pdf, page 7). This metric measures the percentage of problems for which the model generates a correct solution in a single attempt. The correctness is determined by running the generated code against a set of predefined test cases (Source: paper.pdf, page 6).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To estimate the `pass@1` score, the model generates a number of samples for each problem with specific decoding strategies:
*   For HumanEval and MBPP benchmarks, `n=200` samples were generated per problem with `temperature=0.2` and `top_p=0.95` (Source: paper.pdf, page 7).
*   For the DS-1000 benchmark, `n=40` samples were generated per problem with `temperature=0.2` and `top_p=0.5` (Source: paper.pdf, page 8).
*   For single-attempt greedy decoding evaluations (on HumanEval and HumanEval+), the model generates one solution per problem (Source: paper.pdf, page 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five prominent code generation benchmarks (Source: paper.pdf, page 1):
1.  **HumanEval:** Consists of 164 Python programming problems with an average of 9.6 test cases each (Source: paper.pdf, page 6).
2.  **HumanEval+:** An extension of HumanEval with significantly more test cases, averaging 774.8 per problem, to better test for correctness (Source: paper.pdf, page 6).
3.  **MBPP (Mostly Basic Python Programming):** Contains 500 test programming problems, each with three automated test cases (Source: paper.pdf, page 6).
4.  **DS-1000:** A benchmark comprising 1,000 distinct data science problems spanning 7 libraries (e.g., NumPy, Pandas, Matplotlib) (Source: paper.pdf, page 8).
5.  **MultiPL-E:** A benchmark for assessing performance across 8 distinct programming languages, including Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: paper.pdf, page 7).

### Motivation:
These datasets were chosen because they are key, popular, and widely recognized benchmarks in the Code LLM field for evaluating code understanding and generation capabilities (Source: paper.pdf, pages 1, 6). HumanEval+ was specifically used to test for more robust correctness due to its expanded set of test cases (Source: paper.pdf, page 6).

### Preprocessing:
The evaluation prompts were structured according to specific formats for each benchmark to ensure proper evaluation (Source: paper.pdf, page 16).
*   **HumanEval/HumanEval+:** A zero-shot prompt format was used (Source: paper.pdf, page 16).
*   **MBPP:** A three-shot prompt format including three test examples was used (Source: paper.pdf, page 16).
*   **DS-1000 (Completion):** A zero-shot prompt asking the model to complete the Python code was used (Source: paper.pdf, page 16).
*   **DS-1000 (Insertion) & MultiPL-E:** The prompt formats were aligned with the `bigcode-evaluation-harness` to accommodate the specialized symbols and evaluation codes of the benchmarks (Source: paper.pdf, page 16).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was generated using the **Code Evol-Instruct** method. The process started with the **Code Alpaca** dataset, which contains approximately 20,000 instruction-following samples (Source: paper.pdf, page 5). This initial dataset was then iteratively evolved to create a more complex and diverse training set of approximately 78,000 samples (Source: paper.pdf, page 6). The Code Alpaca dataset is publicly available at `https://github.com/sahil280114/codealpaca` (Source: paper.pdf, page 5).

### Motivation:
The motivation for creating a new training dataset was to enhance the capabilities of existing Code LLMs. The developers aimed to automatically increase the complexity of code instruction data to better leverage the internal coding abilities of the base models (Source: paper.pdf, page 2). The Evol-Instruct method was chosen and adapted for the code domain to generate a more challenging and diverse set of instructions than what was available in existing datasets (Source: paper.pdf, page 4).

### Preprocessing:
The training data underwent a multi-stage evolution and filtering process:
1.  **Instruction Evolution:** Instructions from the Code Alpaca dataset were evolved using `gpt-3.5-turbo` based on five heuristic methods: adding constraints, making requirements more specific, increasing reasoning steps, providing erroneous code as a distractor, and adding time/space complexity requirements (Source: paper.pdf, pages 4, 5).
2.  **Data Merging:** After each round of evolution, the newly generated data was merged with the data from all previous rounds and the original dataset (Source: paper.pdf, page 5).
3.  **Data Leakage Filtering:** To prevent data leakage from the test sets, an additional filtering step was implemented. Test samples were used as queries to retrieve the top 5 most similar samples from the training data using the `gte-large` embedding model. GPT-4 was then used to make a binary decision ("yes" or "no") on whether a retrieved sample was a match to the test sample. Matched samples were excluded from the training data (Source: paper.pdf, page 17).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was evaluated across various factors, with results presented in the paper.

**Performance on Python Benchmarks (pass@1):**
*   **WizardCoder-15B:** 57.3% on HumanEval, 51.8% on MBPP (Source: paper.pdf, page 7, Table 1).
*   **WizardCoder-34B:** 73.2% on HumanEval, 61.2% on MBPP (Source: paper.pdf, page 7, Table 1).
*   **WizardCoder-34B on HumanEval+:** 64.6% (Source: paper.pdf, page 6, Figure 2).

**Performance on Multi-Language Benchmark (MultiPL-E, pass@1):**
*   **WizardCoder-34B:**
    *   Java: 44.9%
    *   JavaScript: 55.3%
    *   C++: 47.2%
    *   PHP: 47.2%
    *   R: 39.8%
    *   Julia: 41.5%
    *   Swift: 44.3%
    *   Rust: 46.2%
    (Source: paper.pdf, page 8, Table 2)

**Performance on Data Science Benchmark (DS-1000, Insertion, pass@1):**
*   **WizardCoder-15B (Overall):** 32.8%
    *   Matplotlib: 55.2%
    *   Numpy: 35.1%
    *   Pandas: 20.4%
    *   Pytorch: 30.4%
    *   Scipy: 28.9%
    *   Sklearn: 32.3%
    *   Tensorflow: 37.8%
    (Source: paper.pdf, page 8, Table 3)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

Insufficient information.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   While WizardCoder models demonstrate state-of-the-art performance among open-source Code LLMs and even surpass some closed-source models, their performance still "falls significantly behind the SOTA LLM, GPT4" (Source: paper.pdf, page 9).
*   The model's performance on the DS-1000 benchmark was only reported for the 15B version, as the developers "encounter significant challenges in aligning our 34B model with this framework" (Source: paper.pdf, page 8).

### Recommendations:
*   The authors state that "future work will further augment the performance of our model," suggesting that there is room for improvement and further research (Source: paper.pdf, page 9).
*   The success of the Code Evol-Instruct method highlights the "pivotal role of instruction complexity in enhancing performance," recommending that users and developers focus on the quality and complexity of instruction data for fine-tuning (Source: paper.pdf, page 9).

---