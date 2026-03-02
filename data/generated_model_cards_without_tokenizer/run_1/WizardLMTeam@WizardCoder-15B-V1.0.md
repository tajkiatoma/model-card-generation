## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The WizardCoder model was developed by a team of researchers from Microsoft and Hong Kong Baptist University (Source: `2306.08568.pdf`, Page 1). The authors are:
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

### Model date:
The associated paper was published as a conference paper at ICLR 2024 (Source: `2306.08568.pdf`, Page 1). The second version of the preprint on arXiv is dated May 27, 2025 (Source: `2306.08568.pdf`, Page 1).

### Model version:
The paper presents two main versions of the model (Source: `2306.08568.pdf`, Page 5):
*   **WizardCoder-15B:** This version is based on the StarCoder 15B model.
*   **WizardCoder-34B:** This version is based on the CodeLlama-34B-Python model.

Both versions are created by fine-tuning their respective base models using a novel instruction-following training set generated through the `Code Evol-Instruct` method. This method is the primary differentiator, designed to enhance the complexity of training instructions to improve the model's coding capabilities (Source: `2306.08568.pdf`, Page 1).

### Model type:
WizardCoder is a Large Language Model for Code (Code LLM) based on the GPT-BigCode architecture, designed for causal language modeling (i.e., text generation) (Source: `config.json.txt`, `2306.08568.pdf`, Page 1).

Key architectural details include (Source: `config.json.txt`):
*   **Architecture:** GPTBigCodeForCausalLM
*   **Activation Function:** gelu
*   **Attention Mechanism:** Multi-Query Attention (`"multi_query": true`)
*   **Layers:** 40 (`"n_layer": 40`)
*   **Attention Heads:** 48 (`"n_head": 48`)
*   **Embedding Size:** 6144 (`"n_embd": 6144`)
*   **Vocabulary Size:** 49153 (`"vocab_size": 49153`)
*   **Context Length:** 8192 positions (`"n_positions": 8192`)
*   **Precision:** float16 (`"torch_dtype": "float16"`)

### Training details:
WizardCoder is not trained from scratch but is fine-tuned from pre-trained Code LLMs (StarCoder and CodeLlama-34B-Python) (Source: `2306.08568.pdf`, Page 5).

The fine-tuning process is distinguished by the `Code Evol-Instruct` method, which automatically enhances the complexity of code instructions. This process starts with the Code Alpaca dataset (~20k samples) and iteratively evolves it using OpenAI's `gpt3.5-turbo` to generate more complex and diverse instructions (Source: `2306.08568.pdf`, Pages 4, 5). The final evolved dataset contains approximately 78k samples (Source: `2306.08568.pdf`, Page 6).

The fine-tuning hyperparameters were (Source: `2306.08568.pdf`, Page 6):
*   **Batch Size:** 512
*   **Sequence Length:** 2048
*   **Fine-tuning Steps:** 200
*   **Warmup Steps:** 30
*   **Learning Rate:** 2e-5
*   **Scheduler:** Cosine learning rate scheduler
*   **Precision:** fp16 mixed precision

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   Luo, Z., Xu, C., Zhao, P., Sun, Q., Geng, X., Hu, W., Tao, C., Ma, J., Lin, Q., & Jiang, D. (2024). *WizardCoder: Empowering Code Large Language Models with Evol-Instruct*. Published as a conference paper at ICLR 2024. (Source: `2306.08568.pdf`)

The paper provides a detailed explanation of the `Code Evol-Instruct` methodology, the training process, extensive experimental results, and comparisons with other models.

### Citation details:
To cite the model and its underlying methodology, please refer to the associated paper. A BibTeX entry can be formulated as follows:
```bibtex
@inproceedings{luo2024wizardcoder,
  title={WizardCoder: Empowering Code Large Language Models with Evol-Instruct},
  author={Ziyang Luo and Can Xu and Pu Zhao and Qingfeng Sun and Xiubo Geng and Wenxiang Hu and Chongyang Tao and Jing Ma and Qingwei Lin and Daxin Jiang},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2024}
}
```
(Source: `2306.08568.pdf`, Page 1)

### License:
Insufficient information

### Contact:
For questions or feedback, the authors can be contacted via the email addresses provided in the paper (Source: `2306.08568.pdf`, Page 1):
*   `{cszyluo, majing}@comp.hkbu.edu.hk`
*   `{caxu,puzhao}@microsoft.com`
*   `{qins,xigeng,wenxh,chongyang.tao,qlin,djiang}@microsoft.com`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of WizardCoder is for code generation based on natural language instructions. It is designed to handle complex coding tasks and has demonstrated state-of-the-art performance among open-source models on various code generation benchmarks (Source: `2306.08568.pdf`, Page 1).

The model is capable of generating code in multiple programming languages, including Python, Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: `2306.08568.pdf`, Page 7). It can be applied to general programming problems as well as data science tasks (Source: `2306.08568.pdf`, Pages 7, 8).

The input-output structure involves providing a detailed instruction in natural language, and the model generates a code snippet that fulfills the request (Source: `2306.08568.pdf`, Page 5).

### Primary intended users:
The paper does not explicitly define the primary users, but based on the model's application, the intended users are likely AI researchers, software developers, and data scientists who require a powerful open-source tool for automated code generation.

### Out-of-scope uses:
The model is specifically fine-tuned for code-related tasks. Any application outside of code generation, understanding, or completion is considered out-of-scope. The paper does not discuss or evaluate the model's capabilities on general natural language tasks such as essay writing, translation, or general question-answering.

---

## How to Use
This section outlines how to use the model.

The model is designed to follow instructions provided in a specific prompt format. The format used for fine-tuning is as follows:
```
Below is an instruction that describes a task, paired with an input that provides further
context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```
(Source: `2306.08568.pdf`, Page 5)

For evaluation on benchmarks like HumanEval, a zero-shot prompt is used:
```
### Instruction:
Create a Python script for this problem:
{Question}

### Response:
```
(Source: `2306.08568.pdf`, Page 16)

**Example Input-Output:**
The model's capability is illustrated by its ability to handle increasingly complex instructions.
*   **Simple Instruction:** "Develop a Python program that creates a random password of length 8 characters."
*   **Evolved (Harder) Instruction:** "Develop a Python program that creates a random password of length 12 characters, including at least one uppercase letter, one lowercase letter, one digit, and one special character from the list (!@#$%^&*)."
*   **Example Output (for the harder instruction):**
```python
import random
import string

def generate_password(length):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*'
    password = ''
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice('!@#$%^&*')
    for i in range(length - 4):
        password += random.choice(chars)
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password

password = generate_password(12)
print(password)
```
(Source: `2306.08568.pdf`, Page 2, Figure 1)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The most significant factor identified as impacting the model's performance is **instruction complexity**. The core hypothesis of the research is that increasing the complexity of instructions during fine-tuning is pivotal for achieving exceptional coding performance (Source: `2306.08568.pdf`, Pages 1, 9). Other relevant factors include the programming language of the task and the specific domain (e.g., general programming vs. data science) (Source: `2306.08568.pdf`, Pages 7, 8).

### Evaluation factors:
The model's evaluation is primarily centered around the factor of instruction complexity. The performance is analyzed across:
*   Different programming languages (Java, JavaScript, C++, etc.) on the MultiPL-E benchmark (Source: `2306.08568.pdf`, Page 7).
*   Different coding domains, such as the data science libraries (e.g., pandas, numpy) in the DS-1000 benchmark (Source: `2306.08568.pdf`, Page 8).
*   The number of evolution rounds applied to the training data, which directly corresponds to the complexity of the training instructions (Source: `2306.08568.pdf`, Page 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model is **`pass@k`**, which measures the percentage of problems for which at least one of the first `k` generated code samples passes all unit tests. The paper focuses on **`pass@1`**, where only a single generated solution is considered for each problem (Source: `2306.08568.pdf`, Pages 7, 8).

### Decision thresholds:
The decision threshold for the `pass@1` metric is binary: the generated code either passes all associated unit tests or it fails. The paper reports results based on two settings:
1.  A single attempt using greedy decoding (Source: `2306.08568.pdf`, Page 6).
2.  Generating `n` samples (e.g., `n=200` or `n=40`) to estimate the `pass@1` score, using hyperparameters like `temperature=0.2` and `top_p=0.95` (Source: `2306.08568.pdf`, Pages 7, 8).

### Variation approaches:
To ensure robust measurements for `pass@1` on benchmarks like HumanEval and MBPP, the evaluation follows previous works by generating `n=200` samples for each problem to estimate the score (Source: `2306.08568.pdf`, Page 7). For other benchmarks like DS-1000, `n=40` samples are used (Source: `2306.08568.pdf`, Page 8). For the HumanEval+ leaderboard comparison, a single attempt with greedy decoding is used (Source: `2306.08568.pdf`, Page 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five prominent code generation benchmarks (Source: `2306.08568.pdf`, Pages 1, 6, 7):
*   **HumanEval:** A benchmark comprising 164 Python programming problems with an average of 9.6 test cases each (Source: `2306.08568.pdf`, Page 6).
*   **HumanEval+:** An extension of HumanEval that significantly increases the number of test cases to an average of 774.8 per problem to provide a more rigorous evaluation (Source: `2306.08568.pdf`, Page 6).
*   **MBPP (Mostly Basic Python Programming):** A dataset of 500 Python programming problems, each with three automated test cases (Source: `2306.08568.pdf`, Page 6).
*   **DS-1000:** A benchmark of 1,000 distinct data science problems spanning 7 Python libraries (e.g., NumPy, Pandas, Matplotlib) (Source: `2306.08568.pdf`, Page 7).
*   **MultiPL-E:** A multi-language benchmark used to assess performance across 8 different programming languages: Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: `2306.08568.pdf`, Page 7).

### Motivation:
These datasets were chosen because they are "prominent," "key," and "widely recognized" benchmarks in the field of Code LLMs. They provide a comprehensive and diverse evaluation of the model's capabilities in general-purpose programming, data science, and multi-language coding (Source: `2306.08568.pdf`, Pages 1, 6, 7).

### Preprocessing:
The paper does not detail specific preprocessing steps like normalization or filtering for the evaluation data. However, it specifies that distinct prompt formats were used for different benchmarks to align with standard evaluation practices (Source: `2306.08568.pdf`, Page 16).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training process began with the **Code Alpaca** dataset, which contains approximately 20,000 instruction-following samples (Source: `2306.08568.pdf`, Page 5). This initial dataset was then iteratively augmented using the `Code Evol-Instruct` method, resulting in a final fine-tuning dataset of approximately 78,000 samples (Source: `2306.08568.pdf`, Page 6).

### Motivation:
The motivation for creating a new training dataset was to address the relative lack of research into instruction fine-tuning for Code LLMs. The goal was to automatically increase the complexity and diversity of code instructions to better unlock the inherent coding abilities of powerful base models like StarCoder and CodeLlama (Source: `2306.08568.pdf`, Pages 1, 2).

### Preprocessing:
The primary data processing step was the **`Code Evol-Instruct`** method itself. This involved using `gpt3.5-turbo` to rewrite existing instructions to make them more challenging. Five heuristic methods were used for this evolution (Source: `2306.08568.pdf`, Page 5):
1.  Add new constraints and requirements.
2.  Replace a common requirement with a less common or more specific one.
3.  Add more reasoning steps if the problem is simple.
4.  Provide a piece of erroneous code as a reference to increase misdirection.
5.  Propose higher time or space complexity requirements.

Additionally, a **data filtering step** was implemented to prevent data leakage from the test sets. For each test sample, the top 5 most similar samples from the training data were retrieved using the `gte-large` embedding model. GPT-4 was then used to perform a binary classification ("yes" or "no") on whether the retrieved sample was a match. If a match was identified, the sample was excluded from the training data (Source: `2306.08568.pdf`, Page 17).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was evaluated across several benchmarks:
*   **HumanEval & MBPP (`pass@1`):**
    *   WizardCoder-15B: 57.3% (HumanEval), 51.8% (MBPP)
    *   WizardCoder-34B: 71.5% (HumanEval), 61.2% (MBPP)
    (Source: `2306.08568.pdf`, Page 7, Table 1)
*   **HumanEval & HumanEval+ (single attempt pass rate):**
    *   WizardCoder-34B: 73.2% (HumanEval), 73.2% (HumanEval+)
    (Source: `2306.08568.pdf`, Page 6, Figure 2)
*   **MultiPL-E (`pass@1`, WizardCoder-34B):**
    *   Java: 44.9%, JavaScript: 55.3%, C++: 47.2%, PHP: 47.2%, R: 39.8%, Julia: 41.5%, Swift: 44.3%, Rust: 46.2%
    (Source: `2306.08568.pdf`, Page 8, Table 2)
*   **DS-1000 (`pass@1` insertion, WizardCoder-15B):**
    *   Overall: 32.8%
    *   Scores by library: pandas (20.4%), numpy (35.1%), matplotlib (55.2%), etc.
    (Source: `2306.08568.pdf`, Page 8, Table 3)

### Intersectional results:
The paper analyzes performance based on the number of evolution rounds applied to the training data, showing how performance on HumanEval and MBPP changes as data complexity increases.
*   **Performance on HumanEval (`pass@1`) by evolution round:**
    *   Round 0 (seed data): 45.7%
    *   Rounds 0+1: 52.7%
    *   Rounds 0+1+2: 56.5%
    *   Rounds 0+1+2+3: 57.2%
    *   Rounds 0+1+2+3+4: 54.8%
    (Source: `2306.08568.pdf`, Page 9, Figure 3b)

The analysis shows that performance generally increases with more rounds of evolution, peaking at 3 rounds, before slightly decreasing. This highlights the intersection of data complexity and model performance.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper states that fine-tuning was performed using `fp16 mixed precision`, which implies the use of GPUs with support for half-precision computation (e.g., NVIDIA GPUs with Tensor Cores) (Source: `2306.08568.pdf`, Page 6). However, specific details about the hardware used (e.g., number of GPUs, GPU model, required VRAM) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided repository materials do not contain a dedicated section on ethical considerations. The paper does not mention the use of sensitive or personal data in the training process. Potential risks, common to all code generation models, include the generation of incorrect, inefficient, or insecure code. Users may inadvertently use such code in production systems without proper verification, leading to bugs or security vulnerabilities. The paper does not discuss any specific strategies used to mitigate these risks.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Gap with Closed-Source Models:** A key limitation is that while WizardCoder achieves state-of-the-art results among open-source models, its performance "still falls significantly behind the SOTA LLM, GPT4" (Source: `2306.08568.pdf`, Page 9).
*   **Benchmark Alignment Issues:** The authors note that they encountered "significant challenges in aligning our 34B model with this framework" for the DS-1000 benchmark. As a result, they only reported results for the 15B model on this specific benchmark (Source: `2306.08568.pdf`, Page 8, Footnote 6).
*   **Data Evolution Peak:** The analysis on data evolution rounds shows that performance does not increase indefinitely with more complexity. Performance on HumanEval peaked after three rounds of evolution and then began to decline, suggesting a limit to the benefit of this specific method (Source: `2306.08568.pdf`, Page 9, Figure 3).

### Recommendations:
*   **Verification of Generated Code:** As with any code generation model, users should carefully review, test, and verify all generated code before integrating it into production systems to mitigate risks of bugs or security flaws.
*   **Future Research:** The paper recommends that "future work will further augment the performance of our model," indicating that there is still room for improvement, particularly in closing the performance gap with top-tier closed-source models like GPT-4 (Source: `2306.08568.pdf`, Page 9).