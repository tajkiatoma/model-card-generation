## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Microsoft and Hong Kong Baptist University (Source: 2306.08568.pdf, p. 1). The authors are:
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
The paper describing the model was published as a conference paper at ICLR 2024. The arXiv preprint was first submitted in June 2023 (Source: 2306.08568.pdf, p. 1).

### Model version:
The repository describes the WizardCoder models, which are instruction-finetuned versions of other base models. The paper details two primary versions (Source: 2306.08568.pdf, p. 5, Table 1):
*   **WizardCoder-15B**: Based on the StarCoder 15B model.
*   **WizardCoder-34B**: Based on the CodeLlama-34B-Python model.

These models are differentiated from their base models by being fine-tuned on a code instruction-following dataset generated through the "Code Evol-Instruct" method (Source: 2306.08568.pdf, p. 1).

### Model type:
WizardCoder models are large language models (LLMs) specifically fine-tuned for code generation and understanding tasks (Source: 2306.08568.pdf, p. 1).

*   **Architecture**: The models are based on existing open-source Code LLMs, namely StarCoder and CodeLlama, which are Transformer-based autoregressive language models (Source: 2306.08568.pdf, p. 2, 3, 5).
*   **Model Size**:
    *   WizardCoder-15B has 15 billion parameters (Source: 2306.08568.pdf, p. 7, Table 1).
    *   WizardCoder-34B has 34 billion parameters (Source: 2306.08568.pdf, p. 7, Table 1).
*   **Tokenizer**: The model uses a Byte-Pair Encoding (BPE) tokenizer with a vocabulary size of 49,152 (Source: tokenizer_summary.json.txt; tokenizer_config.json.txt). It includes 19 special tokens for code-specific contexts, such as `<filename>`, `<commit_msg>`, and `<jupyter_code>` (Source: special_tokens_map.json.txt; tokenizer_config.json.txt).
*   **Context Length**: The model supports a maximum sequence length of 2048 tokens (Source: tokenizer_config.json.txt; 2306.08568.pdf, p. 6).

### Training details:
The models were trained using an instruction fine-tuning approach called **Code Evol-Instruct**. This method automatically enhances the complexity and diversity of code instructions to improve the fine-tuning effectiveness of Code LLMs (Source: 2306.08568.pdf, p. 4).

*   **Base Models**: The training started with pre-trained StarCoder 15B and CodeLlama-34B-Python models (Source: 2306.08568.pdf, p. 5).
*   **Training Data**: The initial dataset was the Code Alpaca dataset (~20k samples), which was then iteratively evolved using the Code Evol-Instruct technique to produce a final dataset of approximately 78k samples (Source: 2306.08568.pdf, p. 5, 6). The evolution process used OpenAI's `gpt-3.5-turbo` to generate more complex instructions based on simpler ones (Source: 2306.08568.pdf, p. 6).
*   **Evolution Heuristics**: The Code Evol-Instruct process uses several heuristics to increase instruction difficulty, including adding new constraints, replacing common requirements with more specific ones, adding more reasoning steps, providing erroneous code for misdirection, and proposing higher time/space complexity requirements (Source: 2306.08568.pdf, p. 5).
*   **Fine-tuning Parameters**: The models were fine-tuned with a batch size of 512, a sequence length of 2048, for 200 steps with 30 warmup steps. The learning rate was 2e-5 with a Cosine learning rate scheduler and fp16 mixed precision (Source: 2306.08568.pdf, p. 6).
*   **Prompt Format**: The fine-tuning used the following prompt structure (Source: 2306.08568.pdf, p. 5):
    ```
    Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    {instruction}

    ### Response:
    ```

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   **Title**: WizardCoder: EMPOWERING CODE LARGE LANGUAGE MODELS WITH EVOL-INSTRUCT
*   **Link**: https://arxiv.org/abs/2306.08568
*   **Summary**: The paper introduces Code Evol-Instruct, a method for enhancing code language models by increasing the complexity of instruction data. It details the development and evaluation of the WizardCoder models, which outperform other open-source models on several code generation benchmarks (Source: 2306.08568.pdf).

### Citation details:
The paper was published at ICLR 2024. The authors recommend citing the ICLR version (Source: 2306.08568.pdf, p. 1). A BibTeX citation can be constructed from the paper's details.

```bibtex
@inproceedings{
  luo2024wizardcoder,
  title={WizardCoder: Empowering Code Large Language Models with Evol-Instruct},
  author={Ziyang Luo and Can Xu and Pu Zhao and Qingfeng Sun and Xiubo Geng and Wenxiang Hu and Chongyang Tao and Jing Ma and Qingwei Lin and Daxin Jiang},
  booktitle={The Twelfth International Conference on Learning Representations},
  year={2024},
  url={https://openreview.net/forum?id=D24JBuOBi3}
}
```

### License:
Insufficient information

### Contact:
Contact information for the developers is available in the research paper (Source: 2306.08568.pdf, p. 1):
*   `{cszyluo, majing}@comp.hkbu.edu.hk`
*   `{caxu, puzhao, qins, xigeng, wenxh, chongyang.tao, qlin, djiang}@microsoft.com`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The WizardCoder models are primarily intended for code-related tasks, with a strong focus on code generation (Source: 2306.08568.pdf, p. 1). The model is designed to take a programming problem described in natural language and generate a corresponding code solution (Source: 2306.08568.pdf, p. 5). It has been evaluated on tasks involving Python programming problems and data science workflows across various libraries (Source: 2306.08568.pdf, p. 6, 7). The model also shows strong performance in multiple other programming languages, including Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: 2306.08568.pdf, p. 7, Table 2).

### Primary intended users:
The primary intended users are researchers and developers working with large language models for code.

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The repository does not provide direct code snippets for using the model. However, the research paper specifies the prompt format used for fine-tuning and evaluation, which serves as a guide for how to interact with the model.

**Input-Output Structure**: The model takes a natural language instruction describing a coding task and is expected to output the corresponding code.

**Prompt Template for Fine-Tuning/Inference** (Source: 2306.08568.pdf, p. 5):
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```
Here, `{instruction}` should be replaced with the natural language description of the coding problem. The model will then generate the code as its response.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary factor identified as relevant to the model's performance is **instruction complexity**. The core hypothesis of the work is that increasing the complexity and diversity of instruction data during fine-tuning enhances the model's coding capabilities (Source: 2306.08568.pdf, p. 1, 9).

### Evaluation factors:
The model's performance was evaluated across different factors:
*   **Programming Language**: Performance was measured across 8 distinct programming languages (Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust) on the MultiPL-E benchmark (Source: 2306.08568.pdf, p. 7, Table 2).
*   **Data Science Library**: Performance was measured across 7 different Python data science libraries (Matplotlib, Numpy, Pandas, Pytorch, Scipy, Scikit-learn, and Tensorflow) on the DS-1000 benchmark (Source: 2306.08568.pdf, p. 8, Table 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's performance is **pass@1**. This metric measures the percentage of problems for which the model generates a functionally correct solution in a single attempt (Source: 2306.08568.pdf, p. 7, Table 1).

### Decision thresholds:
Insufficient information

### Variation approaches:
The `pass@1` score was estimated using different generation strategies depending on the benchmark:
*   For HumanEval and MBPP benchmarks, the score was estimated by generating 200 samples per problem with a temperature of 0.2 and top_p of 0.95 (Source: 2306.08568.pdf, p. 7).
*   For HumanEval and HumanEval+ in direct comparison with closed-source models, a single attempt with greedy decoding was used (Source: 2306.08568.pdf, p. 6, Figure 2).
*   For the DS-1000 benchmark, the score was the average `pass@1` accuracy over 40 samples per problem, with a temperature of 0.2 and top_p of 0.5 (Source: 2306.08568.pdf, p. 8, Table 3).
*   For the MultiPL-E benchmark, the score was estimated by generating 50 samples per problem with a temperature of 0.2 and top_p of 0.95 (Source: 2306.08568.pdf, p. 8, Table 2).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five prominent code generation benchmarks (Source: 2306.08568.pdf, p. 2, 6):
*   **HumanEval**: A benchmark consisting of 164 Python programming problems with an average of 9.6 test cases each (Source: 2306.08568.pdf, p. 6).
*   **HumanEval+**: An extension of HumanEval that significantly increases the number of test cases to an average of 774.8 per problem to better test for functional correctness (Source: 2306.08568.pdf, p. 6).
*   **MBPP (Mostly Basic Python Programming)**: A benchmark of 500 test programming problems, each with three automated test cases (Source: 2306.08568.pdf, p. 6).
*   **DS-1000**: A benchmark comprising 1,000 distinct data science problems spanning 7 Python libraries (Source: 2306.08568.pdf, p. 7).
*   **MultiPL-E**: A benchmark for assessing performance across 8 distinct programming languages: Java, JavaScript, C++, PHP, R, Julia, Swift, and Rust (Source: 2306.08568.pdf, p. 7).

### Motivation:
These datasets were chosen because they are key, popular, and diverse benchmarks in the Code LLM field, allowing for a comprehensive assessment of the model's capabilities in Python programming, data science, and multilingual code generation (Source: 2306.08568.pdf, p. 2, 6, 7).

### Preprocessing:
The evaluation prompts were formatted to align with the specific requirements of each benchmark's evaluation harness. For example, for HumanEval, the prompt is structured to ask for a Python script for a given problem. For DS-1000 (Completion), the prompt asks to "Complete the Python code in '...'." (Source: 2306.08568.pdf, p. 16). To prevent data leakage, the training data was filtered to exclude any samples that were highly similar to the test samples from these evaluation datasets (Source: 2306.08568.pdf, p. 17).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training process started with the **Code Alpaca** dataset, which contains around 20,000 instruction-following samples (Source: 2306.08568.pdf, p. 5). This initial dataset was then iteratively evolved using the **Code Evol-Instruct** method, resulting in a final training dataset of approximately 78,000 samples (Source: 2306.08568.pdf, p. 6).

### Motivation:
The motivation for using the Code Evol-Instruct method was to automatically increase the complexity and diversity of the initial code instruction data. The goal was to create a more challenging training set that would better leverage the internal coding capabilities of the base Code LLMs (StarCoder and CodeLlama) and improve their performance on complex tasks (Source: 2306.08568.pdf, p. 2).

### Preprocessing:
The primary preprocessing step was the **Code Evol-Instruct** evolution process itself. This involved taking instructions from the Code Alpaca dataset and using `gpt-3.5-turbo` to rewrite them into more complex instructions based on a set of five code-specific heuristics (Source: 2306.08568.pdf, p. 4, 5). After each round of evolution, the newly generated data was merged with the data from all previous rounds (Source: 2306.08568.pdf, p. 5).

Additionally, a data filtering step was implemented to prevent data leakage. Test samples from the evaluation benchmarks were used as queries to retrieve the top 5 most similar samples from the training data. GPT-4 was then used to determine if there was a match, and if so, the matching training sample was excluded (Source: 2306.08568.pdf, p. 17).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by individual factors:

*   **By Programming Language (on MultiPL-E, pass@1)** (Source: 2306.08568.pdf, p. 8, Table 2):
    *   **WizardCoder-34B**: Java (44.9%), Js (55.3%), CPP (47.2%), PHP (47.2%), R (39.8%), Julia (41.5%), Swift (44.3%), Rust (46.2%).
    *   **WizardCoder-15B**: Java (35.8%), Js (41.9%), CPP (39.0%), PHP (39.3%), R (33.5%), Julia (34.0%), Swift (33.7%), Rust (27.1%).

*   **By Data Science Library (on DS-1000, pass@1)** (Source: 2306.08568.pdf, p. 8, Table 3):
    *   **WizardCoder-15B (Insertion)**: Matplotlib (55.2%), Numpy (35.1%), Pandas (20.4%), Pytorch (30.4%), Scipy (28.9%), Scikit-learn (32.3%), Tensorflow (37.8%). Overall: 32.8%.

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

The provided repository does not contain a specific section on ethical considerations. The training data was generated by evolving the Code Alpaca dataset, which itself was generated using OpenAI's models (Source: 2306.08568.pdf, p. 5, 6). Therefore, the model may inherit biases present in the original data sources and the models used for data generation. Potential risks include the generation of incorrect, inefficient, or insecure code. The paper does not detail any specific risk mitigation strategies beyond standard data filtering to prevent test set leakage (Source: 2306.08568.pdf, p. 17).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Gap with SOTA**: While WizardCoder models show state-of-the-art performance among open-source models, the paper notes that even the 34B version "still falls significantly behind the SOTA LLM, GPT4" (Source: 2306.08568.pdf, p. 9, Figure 2).
*   **Data Leakage**: Although a filtering process was implemented, there is still a possibility of data leakage from evaluation sets into the training data, which is a common challenge in training large language models (Source: 2306.08568.pdf, p. 17).
*   **Evaluation on DS-1000**: The paper notes that the DS-1000 benchmark and its evaluation codes are not designed for instruction-tuned models, which presented challenges in aligning the 34B model with the framework. As a result, only the 15B model's results are reported for this benchmark (Source: 2306.08568.pdf, p. 8).

### Recommendations:
The paper suggests that future work will focus on further augmenting the performance of the model, likely to close the gap with top-performing closed-source models like GPT-4 (Source: 2306.08568.pdf, p. 9). Users should be aware of the model's limitations and potential to generate incorrect code, and should test all generated code thoroughly.

---