## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xiubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma, Qingwei Lin, and Daxin Jiang (wizardcoder.pdf, p. 1). The developers are affiliated with Microsoft and Hong Kong Baptist University (wizardcoder.pdf, p. 1). Contact emails are provided as {cszyluo, majing}@comp.hkbu.edu.hk and {caxu,puzhao,qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com (wizardcoder.pdf, p. 1).

### Model date:
The paper describing the model was published as a conference paper at ICLR 2024 (wizardcoder.pdf, p. 1). The version of the paper provided is v2, dated May 27, 2025 (wizardcoder.pdf, p. 1).

### Model version:
The repository contains information for multiple versions of the WizardCoder model, primarily WizardCoder-15B and WizardCoder-34B (wizardcoder.pdf, p. 7, Table 1). These models are created by fine-tuning the StarCoder and CodeLlama-34B-Python models, respectively, using a novel instruction-tuning approach called Code Evol-Instruct (wizardcoder.pdf, p. 5, Section 3.2). The key difference between the versions is the base model used and the parameter count. The models consistently outperform other open-source Code LLMs on various benchmarks (wizardcoder.pdf, p. 1, Abstract).

### Model type:
The model is a Code Large Language Model (Code LLM) of type GPTBigCodeForCausalLM, designed for code generation and understanding (config.json; wizardcoder.pdf, p. 1, Abstract).

**Architecture Details:**
*   **Model Type:** gpt_bigcode (config.json)
*   **Activation Function:** gelu (config.json)
*   **Layers:** 40 (`n_layer`) (config.json)
*   **Attention Heads:** 48 (`n_head`) (config.json)
*   **Embedding Size:** 6144 (`n_embd`) (config.json)
*   **Vocabulary Size:** 49153 (config.json)
*   **Context Length:** 8192 positions (`n_positions`) (config.json)
*   **Attention Mechanism:** Multi-Query Attention (`multi_query: true`) (config.json)

The model uses a BPE (Byte-Pair Encoding) tokenizer (tokenizer.json).

### Training details:
The WizardCoder models were developed by fine-tuning pre-trained Code LLMs (StarCoder 15B and CodeLlama-34B-Python) using a novel method called **Code Evol-Instruct** (wizardcoder.pdf, p. 1, Abstract; p. 5, Section 3.2).

**Code Evol-Instruct:**
This is an instruction fine-tuning approach adapted for the code domain. It starts with an initial dataset (Code Alpaca) and iteratively evolves the instructions to increase their complexity and diversity (wizardcoder.pdf, p. 4, Section 3.1; p. 5, Section 3.2). The evolution process uses OpenAI's `gpt-3.5-turbo` and incorporates several heuristics tailored for coding tasks, such as (wizardcoder.pdf, p. 4, Section 3.1; p. 6, Section 4.2):
*   Adding new constraints and requirements.
*   Replacing common requirements with more specific ones.
*   Increasing the reasoning steps required.
*   Providing erroneous code as a reference for misdirection.
*   Proposing higher time or space complexity requirements.

The final training dataset consists of approximately 78,000 samples (wizardcoder.pdf, p. 6, Section 4.2).

**Fine-tuning Hyperparameters:**
*   **Batch Size:** 512 (wizardcoder.pdf, p. 6, Section 4.2)
*   **Sequence Length:** 2048 (wizardcoder.pdf, p. 6, Section 4.2)
*   **Learning Rate:** 2e-5 (wizardcoder.pdf, p. 6, Section 4.2)
*   **Learning Rate Scheduler:** Cosine (wizardcoder.pdf, p. 6, Section 4.2)
*   **Warmup Steps:** 30 (wizardcoder.pdf, p. 6, Section 4.2)
*   **Fine-tuning Steps:** 200 (wizardcoder.pdf, p. 6, Section 4.2)
*   **Precision:** fp16 mixed precision (wizardcoder.pdf, p. 6, Section 4.2)

The prompt format for fine-tuning is as follows (wizardcoder.pdf, p. 5, Section 3.2):
```
Below is an instruction that describes a task, paired with an input that provides further
context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```

### Paper or other resource for more information:
The primary resource is the academic paper: "WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT" by Ziyang Luo, Can Xu, et al., published at ICLR 2024. The paper details the Code Evol-Instruct methodology, the training process, and comprehensive experimental results on various code generation benchmarks (wizardcoder.pdf).

### Citation details:
Insufficient information. The provided paper does not include a BibTeX entry for citation.

### License:
Insufficient information.

### Contact:
For questions or feedback, the developers can be contacted via the following emails (wizardcoder.pdf, p. 1):
*   {cszyluo, majing}@comp.hkbu.edu.hk
*   {caxu,puzhao,qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for code generation and various code-related tasks (wizardcoder.pdf, p. 1, Abstract). It is designed to follow complex instructions to generate code in multiple programming languages, including Python, Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (wizardcoder.pdf, p. 8, Table 2). It has also been evaluated on data science workflows involving libraries like Matplotlib, Numpy, Pandas, Scipy, Scikit-learn, and Tensorflow (wizardcoder.pdf, p. 8, Table 3).

The model takes a code-related instruction as input and generates a code snippet or program as a response (wizardcoder.pdf, p. 5, Section 3.2).

### Primary intended users:
The primary users are likely researchers and developers in the field of AI and software engineering who are working with or building upon large language models for code.

### Out-of-scope uses:
The model is specifically trained and fine-tuned on code-related instructions. While it is based on a large language model, its performance on general-purpose natural language tasks (non-coding related) is not its primary focus and has not been evaluated in the provided paper.

---

## How to Use
This section outlines how to use the model. 

The model is designed to be used in an instruction-following format. The prompt structure used for fine-tuning and evaluation provides a template for how to interact with the model (wizardcoder.pdf, p. 5, Section 3.2; p. 16, Appendix A).

**Example Prompt Structure (Zero-Shot for HumanEval):**
```
Below is an instruction that describes a task, paired with an input that provides further
context. Write a response that appropriately completes the request.

### Instruction:
Create a Python script for this problem:
{Question}

### Response:
```
(wizardcoder.pdf, p. 16, Appendix A)

**Example Input:**
An instruction describing a programming task, such as "Develop a Python program that creates a random password of length 8 characters" (wizardcoder.pdf, p. 2, Figure 1).

**Example Output:**
A code snippet that fulfills the instruction, such as a Python function to generate the password (wizardcoder.pdf, p. 2, Figure 1).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary relevant factor identified is **instruction complexity**. The core methodology, Code Evol-Instruct, is designed to systematically increase the complexity of training instructions to enhance the model's coding performance (wizardcoder.pdf, p. 1, Abstract; p. 9, Section 5).

### Evaluation factors:
The model's performance is evaluated and reported across different **programming languages** (Python, Java, JavaScript, C++, PHP, R, Julia, Swift, Rust) and different **data science libraries** (Matplotlib, Numpy, Pandas, Scipy, Scikit-learn, Tensorflow) (wizardcoder.pdf, p. 8, Tables 2 & 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess the model's performance is **pass@1**. This metric measures the percentage of problems for which a correct solution is generated in a single attempt (wizardcoder.pdf, p. 7, Table 1). For the HumanEval and MBPP benchmarks, pass@1 is estimated by generating n=200 samples for each problem with a temperature of 0.2 and top_p of 0.95 (wizardcoder.pdf, p. 7, Table 1). For other benchmarks, greedy decoding (a single attempt) is used (wizardcoder.pdf, p. 6, Figure 2).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For the HumanEval and MBPP benchmarks, the pass@1 score is estimated by generating 200 samples per problem to ensure a robust measurement (wizardcoder.pdf, p. 7, Table 1). For the DS-1000 benchmark, the pass@1 score is an average over 40 samples (wizardcoder.pdf, p. 8, Table 3).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five prominent code generation benchmarks (wizardcoder.pdf, p. 1, Abstract):
1.  **HumanEval:** A benchmark featuring 164 Python programming problems with an average of 9.6 test cases each (wizardcoder.pdf, p. 6, Section 4.3).
2.  **HumanEval+:** An extension of HumanEval with significantly more test cases, averaging 774.8 per problem (wizardcoder.pdf, p. 6, Section 4.3).
3.  **MBPP (Mostly Basic Python Programming):** A benchmark of 500 test programming problems with three automated test cases each (wizardcoder.pdf, p. 6, Section 4.3).
4.  **DS-1000:** A benchmark comprising 1,000 distinct data science problems spanning 7 libraries (wizardcoder.pdf, p. 8, Section 4.5).
5.  **MultiPL-E:** A benchmark for assessing performance across 8 distinct programming languages (Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust) (wizardcoder.pdf, p. 8, Section 4.4).

### Motivation:
These datasets were chosen because they are key, widely recognized, and popular benchmarks in the Code LLM field for evaluating code generation and understanding capabilities (wizardcoder.pdf, p. 1, Abstract; p. 3, Section 2; p. 6, Section 4.3).

### Preprocessing:
To prevent data leakage, the developers implemented a filtering step. All test samples from the evaluation datasets were used as queries to retrieve the top 5 most similar samples from the training data using the `gte-large` embeddings model. GPT-4 was then used to perform a binary decision ("yes" or "no") on whether a retrieved sample was a match to the test sample. Any matching samples were excluded from the training data (wizardcoder.pdf, p. 17, Appendix C).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training process started with the **Code Alpaca** dataset, which contains around 20,000 instruction-following samples (wizardcoder.pdf, p. 5, Section 3.2). This initial dataset was then iteratively evolved using the **Code Evol-Instruct** method, resulting in a final training set of approximately 78,000 samples (wizardcoder.pdf, p. 6, Section 4.2). The Code Alpaca dataset is publicly available at https://github.com/sahil280114/codealpaca (wizardcoder.pdf, p. 5, footnote 3).

### Motivation:
The initial Code Alpaca dataset was chosen as a starting point for code instruction data. The motivation for evolving this dataset with Code Evol-Instruct was to automatically increase the complexity and diversity of the instructions, aiming to better leverage the internal coding capabilities of the base Code LLMs (wizardcoder.pdf, p. 2).

### Preprocessing:
The primary preprocessing step was the application of the **Code Evol-Instruct** method. This involved using `gpt-3.5-turbo` to rewrite and complicate the initial instructions from the Code Alpaca dataset based on a set of five code-specific heuristics (wizardcoder.pdf, p. 4, Section 3.1). Additionally, a data filtering step was implemented to prevent data leakage from the test sets into the training data (wizardcoder.pdf, p. 17, Appendix C).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is reported separately for each of the following factors:
*   **Programming Language (on MultiPL-E benchmark):** Pass@1 scores are provided for Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (wizardcoder.pdf, p. 8, Table 2).
*   **Data Science Library (on DS-1000 benchmark):** Pass@1 scores are provided for Matplotlib, Numpy, Pandas, Scipy, Scikit-learn, and Tensorflow (wizardcoder.pdf, p. 8, Table 3).

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
*   The model's performance, while superior to other open-source models, still "falls significantly behind the SOTA LLM, GPT4" (wizardcoder.pdf, p. 9, Section 6).
*   The developers noted challenges in aligning the 34B model with the DS-1000 benchmark framework, as it is not specifically designed for instruction fine-tuned models (wizardcoder.pdf, p. 8, footnote 6).
*   The evolution process for creating the training data does not always lead to higher similarity scores with the test set, indicating that performance gains are from increased instruction complexity rather than data leakage. However, this also means the evolved data may not perfectly cover all types of problems in the evaluation benchmarks (wizardcoder.pdf, p. 9, Figure 4).

### Recommendations:
The paper suggests that future work will focus on further augmenting the performance of the model, implying that there is still room for improvement (wizardcoder.pdf, p. 9, Section 6). Users should be aware that while the model is powerful, it may not match the performance of top-tier closed-source models like GPT-4.