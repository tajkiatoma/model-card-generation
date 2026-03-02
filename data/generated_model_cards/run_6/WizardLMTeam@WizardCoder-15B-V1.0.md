## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. The developers are affiliated with Microsoft and Hong Kong Baptist University (2306.08568.pdf, p. 1).

### Model date:
The academic paper describing the model was published as a conference paper at ICLR 2024. The version of the paper provided is dated May 27, 2025 (v2) (2306.08568.pdf, p. 1).

### Model version:
The repository describes two versions of the WizardCoder model:
*   **WizardCoder-15B**: Based on the StarCoder 15B model (2306.08568.pdf, p. 5, Section 3.2).
*   **WizardCoder-34B**: Based on the CodeLlama-34B-Python model (2306.08568.pdf, p. 5, Section 3.2).

These models are created by fine-tuning their respective base models using a novel instruction-following training set generated through the "Code Evol-Instruct" method (2306.08568.pdf, p. 5, Section 3.2). The paper demonstrates that these models significantly outperform other open-source Code LLMs and surpass some closed-source models like Claude and Bard on certain benchmarks (2306.08568.pdf, p. 1, Abstract).

### Model type:
WizardCoder is a large language model (LLM) specifically fine-tuned for code generation tasks. It is a decoder-only, auto-regressive transformer-based model (2306.08568.pdf, p. 1; config.json.txt).

**Architecture Details:**
The model architecture is `GPTBigCodeForCausalLM` (config.json.txt, key: "architectures"). Key architectural parameters include:
*   **Model Type:** `gpt_bigcode` (config.json.txt, key: "model_type").
*   **Activation Function:** `gelu` (config.json.txt, key: "activation_function").
*   **Layers:** 40 (`n_layer`) (config.json.txt, key: "n_layer").
*   **Attention Heads:** 48 (`n_head`) (config.json.txt, key: "n_head").
*   **Embedding Size:** 6144 (`n_embd`) (config.json.txt, key: "n_embd").
*   **Attention Mechanism:** Multi-Query attention (`multi_query: true`) (config.json.txt, key: "multi_query").
*   **Vocabulary Size:** 49,153 (config.json.txt, key: "vocab_size").
*   **Context Length:** 8192 tokens (`n_positions`) (config.json.txt, key: "n_positions").

The tokenizer is a Byte-Pair Encoding (BPE) model (tokenizer_summary.json.txt, key: "model.type").

### Training details:
The model was trained using an instruction fine-tuning technique called **Code Evol-Instruct**. This process starts with an initial dataset (Code Alpaca) and iteratively evolves the instructions to increase their complexity and diversity (2306.08568.pdf, p. 5, Section 3.2).

**Code Evol-Instruct Method:**
The core of the training is the data evolution process, which uses `gpt-3.5-turbo` to rewrite and complicate existing code instructions based on five heuristic methods (2306.08568.pdf, p. 4, Section 3.1; p. 6, Section 4.2):
1.  Add new constraints and requirements.
2.  Replace a common requirement with a less common one.
3.  Increase the number of reasoning steps required.
4.  Provide a piece of erroneous code as a reference to misdirect the model.
5.  Propose higher time or space complexity requirements (2306.08568.pdf, p. 5, Code Evolution Heuristic Methods).

**Fine-tuning Process:**
*   **Base Models:** StarCoder 15B and CodeLlama-34B-Python (2306.08568.pdf, p. 5, Section 3.2).
*   **Dataset:** An evolved dataset of approximately 78,000 samples created from the Code Alpaca dataset (2306.08568.pdf, p. 6, Section 4.2).
*   **Hyperparameters:**
    *   Batch Size: 512
    *   Sequence Length: 2048
    *   Fine-tuning Steps: 200
    *   Warmup Steps: 30
    *   Learning Rate: 2e-5 with a Cosine scheduler
    *   Precision: fp16 mixed precision
    (2306.08568.pdf, p. 6, Section 4.2).

The prompt format for fine-tuning follows a specific instruction-response structure (2306.08568.pdf, p. 5, Prompt for Fine-Tuning Format).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   **Title:** WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT
*   **Authors:** Ziyang Luo, Can Xu, Pu Zhao, et al.
*   **Publication:** Published as a conference paper at ICLR 2024.
*   **Summary:** The paper introduces the Code Evol-Instruct method for enhancing Code LLMs by increasing the complexity of instruction data. It details the development and evaluation of the WizardCoder models, showing their superior performance on various code generation benchmarks (2306.08568.pdf).

### Citation details:
Insufficient information. The paper does not provide a BibTeX entry. A citation can be constructed based on the paper's details:
Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang. "WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT." Published as a conference paper at ICLR 2024. arXiv preprint arXiv:2306.08568 (2023) (2306.08568.pdf, p. 1).

### License:
Insufficient information.

### Contact:
Contact can be made through the author emails provided in the paper:
*   `{cszyluo, majing}@comp.hkbu.edu.hk`
*   `{caxu, puzhao, qins, xigeng, wenxh, chongyang.tao, qlin, djiang}@microsoft.com`
(2306.08568.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of WizardCoder is for code-related tasks, with a specific focus on code generation. The model is designed to take a programming problem described in natural language (an instruction) and generate a corresponding code solution (2306.08568.pdf, p. 1, Abstract; p. 5, Prompt for Fine-Tuning Format).

**Capabilities:**
*   **Code Generation:** Generating code in various programming languages, including Python, Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (2306.08568.pdf, p. 8, Table 2).
*   **Data Science Tasks:** Solving data science problems that involve libraries like Pandas, NumPy, SciPy, Scikit-learn, Matplotlib, and TensorFlow (2306.08568.pdf, p. 8, Table 3).

**Input-Output Structure:**
The model expects an instruction that describes a task. The output is a response that appropriately completes the request, typically in the form of a code snippet.
*   **Input Format:** `### Instruction: {instruction}`
*   **Output Format:** `### Response: {code_solution}`
(2306.08568.pdf, p. 5, Prompt for Fine-Tuning Format).

### Primary intended users:
Insufficient information. (The paper is academic, implying researchers and developers in the field of AI and software engineering are the target audience).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model. 

The model is used by providing it with a formatted prompt containing a natural language instruction for a coding task. The model then generates the code as a response.

**Example Prompt Structure for Code Generation:**
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Create a Python script for this problem:
{Question}

### Response:
```
(2306.08568.pdf, p. 16, Appendix A).

**Example Evolved Instruction (Input):**
"Write a MongoDB query to select all documents in a collection where the field 'category' is 'clothes' and the 'brand' field is not equal to 'Nike', and the 'price' field is greater than or equal to 100 and less than or equal to 500, and the 'color' field is either 'red' or 'blue'. Additionally, sort the documents in descending order by the 'date_added' field and limit the result to the first 10 documents." (2306.08568.pdf, p. 17, Appendix D).

The model would then generate the corresponding MongoDB query as the output.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Instruction Complexity:** The complexity of the input instruction is a pivotal factor. The Code Evol-Instruct method is designed to systematically increase instruction complexity by adding constraints, requiring more reasoning steps, or introducing higher time/space complexity requirements. This was found to be key in achieving high performance (2306.08568.pdf, p. 1, Abstract; p. 5, Code Evolution Heuristic Methods).
*   **Programming Language:** The model's performance varies across different programming languages (2306.08568.pdf, p. 8, Table 2).
*   **Task Domain:** Performance also varies by the specific domain within programming, such as data science libraries (e.g., Pandas, TensorFlow) (2306.08568.pdf, p. 8, Table 3).

### Evaluation factors:
The model's performance was evaluated and reported based on the following factors:
*   **Programming Language:** Results are disaggregated for Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (2306.08568.pdf, p. 8, Table 2).
*   **Data Science Library:** For Python, results are further broken down by performance on tasks involving Matplotlib, Pandas, NumPy, SciPy, Scikit-learn, and TensorFlow (2306.08568.pdf, p. 8, Table 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's performance is **pass@1**. This metric measures the percentage of problems for which a correct solution is generated in a single attempt (2306.08568.pdf, p. 7, Table 1).

### Decision thresholds:
Insufficient information.

### Variation approaches:
The `pass@1` score is estimated by generating `n` samples for each problem and checking if any are correct. For the HumanEval and MBPP benchmarks, the model generated `n=200` samples per problem with a temperature of 0.2 and top_p of 0.95 (2306.08568.pdf, p. 7, Table 1 caption). For other evaluations, such as on the EvalPlus leaderboard, greedy decoding (a single attempt) was used (2306.08568.pdf, p. 7, Figure 2 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five code generation benchmarks (2306.08568.pdf, p. 5, Section 4):
*   **HumanEval:** A Python benchmark with 164 programming problems and an average of 9.6 test cases each (2306.08568.pdf, p. 6, Section 4.3).
*   **HumanEval+:** An extension of HumanEval with significantly more test cases, averaging 774.8 per problem (2306.08568.pdf, p. 6, Section 4.3).
*   **MBPP (Mostly Basic Python Programming):** A benchmark of 500 Python problems, each with three automated test cases (2306.08568.pdf, p. 6, Section 4.3).
*   **DS-1000:** A benchmark of 1,000 data science problems spanning 7 Python libraries (Pandas, NumPy, etc.) (2306.08568.pdf, p. 8, Section 4.5).
*   **MultiPL-E:** A multilingual benchmark assessing performance across 8 distinct programming languages: Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (2306.08568.pdf, p. 8, Section 4.4).

### Motivation:
These datasets were chosen because they are "key benchmarks in the Code LLM field" for evaluating code generation capabilities (2306.08568.pdf, p. 6, Section 4.3).

### Preprocessing:
To prevent data leakage from the test sets into the training data, a filtering step was implemented. All test samples were used as queries to retrieve the top 5 most similar samples from the training data using the `gte-large` embedding model. GPT-4 was then used to make a binary decision ("yes" or "no") on whether there was a match. If a match was found, the corresponding sample was excluded from the training data (2306.08568.pdf, p. 17, Appendix C).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training process began with the **Code Alpaca** dataset, which contains around 20,000 instruction-following samples (2306.08568.pdf, p. 5, Section 3.2). This initial dataset was then iteratively evolved using the **Code Evol-Instruct** method, resulting in a final training dataset of approximately 78,000 samples (2306.08568.pdf, p. 6, Section 4.2).

### Motivation:
The motivation for using the Code Evol-Instruct method was to "automatically increase the complexity of code instruction data" to better leverage the internal coding capabilities of the base Code LLMs (2306.08568.pdf, p. 2). The goal was to create a more complex and diverse dataset specifically tailored to the coding domain (2306.08568.pdf, p. 4, Section 3.1).

### Preprocessing:
The primary preprocessing step was the **Code Evol-Instruct** data evolution process. This involved using `gpt-3.5-turbo` to rewrite instructions from the Code Alpaca dataset to make them more challenging. The evolution was guided by specific prompts and five heuristic methods (2306.08568.pdf, p. 4, Section 3.1):
1.  **Adding Constraints:** Adding new requirements to the problem.
2.  **Deepening:** Replacing a common requirement with a more specific one.
3.  **Concretizing:** Adding more reasoning steps if the problem is too simple.
4.  **Increasing Reasoning Steps (Misdirection):** Providing erroneous code as a reference.
5.  **Complicating Input:** Proposing higher time or space complexity requirements.

Additionally, a data filtering step was performed to prevent leakage from evaluation benchmarks into the training set (2306.08568.pdf, p. 17, Appendix C).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was analyzed across several individual factors:

**By Programming Language (pass@1 on MultiPL-E):**
*   **Java:** 44.9%
*   **JavaScript:** 55.3%
*   **C++:** 47.2%
*   **PHP:** 47.2%
*   **R:** 39.8%
*   **Julia:** 41.5%
*   **Swift:** 44.3%
*   **Rust:** 46.2%
(2306.08568.pdf, p. 8, Table 2, WizardCoder-34B).

**By Data Science Library (pass@1 on DS-1000, Insertion):**
*   **Matplotlib:** 55.2%
*   **Numpy:** 35.1%
*   **Pandas:** 20.4%
*   **Pytorch:** 30.4%
*   **Scipy:** 28.9%
*   **Scikit-learn:** 32.3%
*   **Tensorflow:** 37.8%
(2306.08568.pdf, p. 8, Table 3, WizardCoder 15B).

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

Insufficient information. The paper does not contain a dedicated section on ethical considerations. The training data is based on the Code Alpaca dataset, which is derived from publicly available code, and was evolved using OpenAI's GPT-3.5 model (2306.08568.pdf, p. 5, Section 3.2; p. 6, Section 4.2). No specific risks or mitigation strategies are discussed.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Gap with SOTA:** While WizardCoder outperforms other open-source models and some closed-source models, its performance "still falls significantly behind the SOTA LLM, GPT4" (2306.08568.pdf, p. 9, Section 6).
*   **Benchmark Limitations:** The WizardCoder-34B model could not be properly evaluated on the DS-1000 benchmark because the benchmark and its evaluation codes were not designed for instruction fine-tuned models, and the base CodeLlama-34B model does not support the required code insertion format. Therefore, only results for the 15B model are reported for this benchmark (2306.08568.pdf, p. 8, footnote 6).
*   **Data Leakage Prevention:** While a data filtering process was implemented to prevent data leakage from test sets, the complexity of this task means there is no absolute guarantee that all leakage was prevented (2306.08568.pdf, p. 17, Appendix C).

### Recommendations:
*   The paper suggests that future work will focus on further augmenting the performance of the model, indicating that there is room for improvement (2306.08568.pdf, p. 9, Section 6).
*   Users should be aware of the performance differences between the 15B and 34B versions and choose the model that best fits their needs and computational resources.