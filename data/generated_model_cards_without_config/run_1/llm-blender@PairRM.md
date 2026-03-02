## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The LLM-BLENDER framework was developed by Dongfu Jiang from Zhejiang University, Xiang Ren from the University of Southern California, and Bill Yuchen Lin from the Allen Institute for Artificial Intelligence (2306.02561.pdf, p. 1).

### Model date:
The associated academic paper is dated June 30, 2023 (2306.02561.pdf, p. 1).

### Model version:
The model is an ensembling framework named LLM-BLENDER, which consists of two main modules: PAIRRANKER and GENFUSER (2306.02561.pdf, p. 1).
*   **PAIRRANKER**: A pairwise ranking module with a DeBERTa (400m parameters) backbone (2306.02561.pdf, p. 7). It is designed to compare pairs of candidate outputs from different Large Language Models (LLMs) to determine the superior one (2306.02561.pdf, p. 1).
*   **GENFUSER**: A generative fusion module based on Flan-T5-XL (3b parameters) (2306.02561.pdf, p. 7). It merges the top-ranked candidates identified by PAIRRANKER to generate an improved, final output (2306.02561.pdf, p. 1, 6).

### Model type:
LLM-BLENDER is a post-hoc ensemble learning framework for ranking and fusing outputs from multiple LLMs (2306.02561.pdf, p. 9).

**Architecture Details:**
*   **PAIRRANKER**: This module uses a Transformer-based cross-attention encoder, specifically a DeBERTa backbone, to jointly encode an input text and a pair of candidate outputs (2306.02561.pdf, p. 2, 5, 7). It includes a five-layer multi-layer perceptron (MLP) with a hyperbolic tangent activation function to process embeddings and determine scores (2306.02561.pdf, p. 14).
*   **GENFUSER**: This is a seq2seq model that uses Flan-T5-XL (3b parameters) as its backbone. It is fine-tuned to take an input instruction and K top-ranked candidates to generate a fused, enhanced output (2306.02561.pdf, p. 6, 7).
*   **Tokenizer**: The tokenizer used for the PAIRRANKER module is a `DebertaV2Tokenizer` (tokenizer_config.json.txt). It employs a Unigram SentencePiece model with a vocabulary size of 128,000 (tokenizer_summary.json.txt). The model has a maximum length of 1000000000000000019884624838656 (tokenizer_config.json.txt).

### Training details:
**PAIRRANKER Training:**
*   **Algorithm**: The model is trained for 5 epochs using the Adafactor optimizer (2306.02561.pdf, p. 14). The training involves pairwise comparison, where the model learns to distinguish the better candidate between a pair (yi, yj) given an input x (2306.02561.pdf, p. 2).
*   **Parameters**: The training uses a maximum learning rate of 1e-5 with a 5% warm-up ratio and a linear learning rate scheduler. The batch size is 64 (2306.02561.pdf, p. 14).
*   **Methodology**: To ensure learning efficiency, a sub-sampling strategy is used, randomly selecting 5 pairs of candidates per input for comparison during training. The order of candidates within each pair is also shuffled to help the model learn to be consistent (2306.02561.pdf, p. 5, 6). The loss function is Binary Cross-Entropy (BCE) (2306.02561.pdf, p. 14).

**GENFUSER Training:**
*   **Algorithm**: GENFUSER is fine-tuned from a Flan-T5-XL model (2306.02561.pdf, p. 6).
*   **Methodology**: It is trained to fuse the top-3 BARTScore selections from the training data to generate an improved output (2306.02561.pdf, p. 14). The input is a concatenation of the original instruction and the K top-ranked candidates, separated by special tokens (2306.02561.pdf, p. 6).

### Paper or other resource for more information:
*   **Paper**: Jiang, D., Ren, X., & Lin, B. Y. (2023). *LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion*. arXiv preprint arXiv:2306.02561 (2306.02561.pdf).
*   **Project Website**: A toolkit and other resources are available at `https://yuchenlin.xyz/LLM-Blender` (2306.02561.pdf, p. 1).

### Citation details:
```bibtex
@misc{jiang2023llmblender,
      title={LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion}, 
      author={Dongfu Jiang and Xiang Ren and Bill Yuchen Lin},
      year={2023},
      eprint={2306.02561},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(Derived from 2306.02561.pdf)

### License:
The paper states the framework is open-sourced, but does not specify a particular license (2306.02561.pdf, p. 9).

### Contact:
Contact can be made with the developers via their emails:
*   Dongfu Jiang: `dongfu@zju.edu.cn` (2306.02561.pdf, p. 1)
*   Xiang Ren: `xiangren@usc.edu` (2306.02561.pdf, p. 1)
*   Bill Yuchen Lin: `yuchenl@allenai.org` (2306.02561.pdf, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
LLM-BLENDER is an ensembling framework designed to dynamically combine the outputs of multiple open-source Large Language Models (LLMs) to achieve consistently superior performance on instruction-following tasks (2306.02561.pdf, p. 1, 3). Its primary capabilities are:
1.  **Ranking (PAIRRANKER)**: To compare and rank candidate responses generated by various LLMs for a given input instruction, identifying the most suitable response (2306.02561.pdf, p. 2).
2.  **Fusion (GENFUSER)**: To merge multiple top-ranked candidate responses into a single, improved output that capitalizes on their strengths and mitigates their weaknesses (2306.02561.pdf, p. 2, 6).

The framework is intended to improve robustness, generalization, and accuracy, and to alleviate biases and errors present in individual LLMs (2306.02561.pdf, p. 2).

**Input-Output Structure:**
*   **Input**: The framework takes a user's instruction/input `x` (2306.02561.pdf, p. 3).
*   **Intermediate Steps**: It generates N candidate outputs from N different LLMs. The PAIRRANKER module takes pairs of these candidates along with the original input `x` to produce a ranking. The GENFUSER module takes the original input `x` along with the top K ranked candidates (2306.02561.pdf, p. 3, Figure 2).
*   **Output**: The final output is a single, fused response `ŷ` generated by GENFUSER (2306.02561.pdf, p. 3, Figure 2).

### Primary intended users:
The primary users are practitioners and researchers who are deploying and studying LLMs, particularly those interested in ensemble learning techniques (2306.02561.pdf, p. 2).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model. 

The framework operates in a two-stage pipeline (2306.02561.pdf, p. 3, Figure 2):

1.  **Candidate Generation**: For a given input `x`, generate `N` candidate outputs using `N` different LLMs.
2.  **Pairwise Ranking (PAIRRANKER)**:
    *   For each pair of candidates `(yi, yj)`, create an input sequence for the PAIRRANKER model. The paper found the format `<s><source> x </s> <candidate1> yi </s> <candidate2> yj </s>` to be effective (2306.02561.pdf, p. 5, 14). The tokenizer also supports a template format of `[CLS] A [SEP]` for single sequences and `[CLS] A [SEP] B [SEP]` for pairs (tokenizer_summary.json.txt).
    *   Run inference for all pairs to obtain a comparison matrix `M`, where `Mij` represents the model's confidence that `yi` is better than `yj` (2306.02561.pdf, p. 6).
    *   Use an aggregation function (e.g., MaxLogits, MaxWins, or Bubble Sort) on the matrix `M` to rank all `N` candidates (2306.02561.pdf, p. 6).
3.  **Generative Fusion (GENFUSER)**:
    *   Select the top `K` candidates from the ranking (e.g., `K=3`) (2306.02561.pdf, p. 2).
    *   Concatenate the original input `x` and the `K` candidates using separator tokens (e.g., `<extra_id_i>`) (2306.02561.pdf, p. 6).
    *   Feed this concatenated sequence into the GENFUSER model to generate the final, improved output `ŷ` (2306.02561.pdf, p. 3, Figure 2).

**Special Tokens:**
The tokenizer uses several special tokens, including:
*   `[CLS]`: Beginning of sequence token (special_tokens_map.json.txt).
*   `[SEP]`: Separator token (special_tokens_map.json.txt).
*   `[PAD]`: Padding token (special_tokens_map.json.txt).
*   `[UNK]`: Unknown token (special_tokens_map.json.txt).
*   `[MASK]`: Mask token (added_tokens.json.txt).
*   `<|source|>`, `<|candidate1|>`, `<|candidate2|>`, `<|candidate|>`: Added tokens for structuring inputs (added_tokens.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Source LLM Diversity**: The performance of the ensembling framework depends on the diverse strengths and weaknesses of the underlying LLMs used to generate candidates. These variations arise from differences in training data, architectures, and hyperparameters (2306.02561.pdf, p. 1).
*   **Task Type**: The framework's effectiveness was evaluated on instruction-following tasks as well as conventional NLG tasks like summarization, translation, and constrained generation, with performance varying across them (2306.02561.pdf, p. 8, 15).
*   **Number of Comparisons**: For the PAIRRANKER module, the number of pairwise comparisons performed during inference is a key factor. Using more comparisons (e.g., with the MaxLogits method) can lead to better performance at the cost of efficiency, creating a trade-off (2306.02561.pdf, p. 17, Figure 6).
*   **Candidate Quality**: The overall performance is constrained by the quality of the initial candidate pool generated by the individual LLMs (2306.02561.pdf, p. 6).

### Evaluation factors:
The evaluation analyzed performance across different individual LLMs (e.g., Vicuna, OpenAssistant, Alpaca) and various ranking methods (e.g., Random, MLM-Scoring, SimCLS, SummaReranker, PairRanker) (2306.02561.pdf, p. 7, Table 2).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using two main groups of metrics:
1.  **NLG Metrics**: Conventional automatic metrics for Natural Language Generation tasks are used, including:
    *   BERTScore (Zhang et al., 2020b) (2306.02561.pdf, p. 6)
    *   BLEURT (Sellam et al., 2020) (2306.02561.pdf, p. 6)
    *   BARTScore (Yuan et al., 2021) (2306.02561.pdf, p. 6)
    *   For specific tasks, ROUGE-1, ROUGE-2, ROUGE-L, BLEU, and CIDEr are also used (2306.02561.pdf, p. 15).
2.  **GPT-Rank**: A metric based on prompting ChatGPT for pairwise comparisons of all candidate outputs. The final rank is determined by the number of wins in these comparisons (2306.02561.pdf, p. 6).

To evaluate the ranking quality of the PAIRRANKER module specifically, the following correlation metrics are used to compare its rankings with the oracle GPT-Rank:
*   Pearson Correlation Coefficient (2306.02561.pdf, p. 8)
*   Spearman's Correlation (2306.02561.pdf, p. 8)
*   Spearman's Footrule distance (2306.02561.pdf, p. 8)

### Decision thresholds:
*   For creating training labels for the ranker, a candidate `yi` is considered better than `yj` if its quality score `Q(yi, y)` is greater than or equal to `Q(yj, y)` (2306.02561.pdf, p. 5).
*   During inference with the `MaxWins` aggregation method, a candidate `yi` wins a comparison against `yj` if the score `sij > 0` (2306.02561.pdf, p. 6).

### Variation approaches:
During inference, PAIRRANKER's results from pairwise comparisons are aggregated to produce a final ranking. Three aggregation methods are proposed and evaluated (2306.02561.pdf, p. 6):
*   **MaxLogits**: Computes a score for each candidate based on the sum of confidence scores from its comparisons against all other candidates.
*   **MaxWins**: Calculates the number of victories for each candidate in its pairwise comparisons.
*   **Bubble Sort**: An efficient method that performs a single run of bubble sort using pairwise comparisons to find the best candidate, reducing inference time from O(N²) to O(N).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **MixInstruct**: A benchmark dataset introduced in the paper for evaluating ensembling methods on instruction-following tasks. The test set contains 5,000 examples. For each example, it includes candidate outputs from 11 popular open-source LLMs (including Vicuna, OpenAssistant, Alpaca, etc.) and oracle pairwise comparisons for all candidate pairs provided by ChatGPT (2306.02561.pdf, p. 2, 3).
*   **Conventional NLG Datasets**:
    *   **CNN/DailyMail**: A dataset for abstractive summarization, consisting of news articles (2306.02561.pdf, p. 15). The test set has 11,490 examples (2306.02561.pdf, p. 17, Table 7).
    *   **CommonGen**: A dataset for constrained commonsense generation, containing 1,497 test examples (2306.02561.pdf, p. 15, 17, Table 7).
    *   **WMT18 (zh-en)**: A dataset for Chinese-to-English machine translation, with 3,981 test examples (2306.02561.pdf, p. 15, 17, Table 7).

### Motivation:
*   **MixInstruct** was created specifically to provide a benchmark for training and evaluating LLM ensembling methods, as no such dataset previously existed (2306.02561.pdf, p. 3, 9).
*   **CNN/DM, CommonGen, and WMT18** were chosen to test the task generalization ability of the PAIRRANKER module on standard, conventional NLG tasks (2306.02561.pdf, p. 15, 16).

### Preprocessing:
For all evaluation datasets, candidate responses were generated from the respective base models. For the conventional NLG tasks, 15 candidates were generated for each input using beam search and diverse beam search (2306.02561.pdf, p. 16). For MixInstruct, 11 candidates were generated from 11 different LLMs (2306.02561.pdf, p. 3).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The framework is trained on **MixInstruct**, a large-scale dataset created by the authors. It consists of 110,000 examples in total, split into 100,000 for training and 5,000 for validation (2306.02561.pdf, p. 3, Table 1). The dataset is a mixture of instructions from four sources (2306.02561.pdf, p. 3, Table 1):
*   **Alpaca-GPT4**: 22,862 examples
*   **Dolly-15K**: 7,584 examples
*   **GPT4All-LAION**: 76,552 examples
*   **ShareGPT**: 3,002 examples

For each instruction, the dataset contains `N=11` candidate outputs generated from popular open-source LLMs (2306.02561.pdf, p. 3).

### Motivation:
The MixInstruct dataset was created to provide a large-scale, high-quality benchmark for training and evaluating LLM ensembling methods on instruction-following tasks (2306.02561.pdf, p. 3, 9).

### Preprocessing:
*   **Candidate Generation**: For each of the 110k instructions, outputs were generated from 11 different open-source LLMs (2306.02561.pdf, p. 3).
*   **Pairing and Structuring**: For training PAIRRANKER, candidate outputs are paired. A sub-sampling strategy of using 5 pairs per input is employed. The input to the model is a single concatenated sequence: `<s><source> x </s> <candidate1> yi </s> <candidate2> yj </s>` (2306.02561.pdf, p. 5). The order of candidates `yi` and `yj` is shuffled during training to ensure the model learns to be consistent (2306.02561.pdf, p. 6).
*   **Normalization**: The tokenizer applies stripping of whitespace and replaces sequences of 2 or more spaces with a single space (tokenizer_summary.json.txt).
*   **Pre-tokenization**: A Metaspace pre-tokenizer is used, which adds a prefix space and replaces whitespace with a special ` ` character (tokenizer_summary.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Table 2 of the paper presents performance results for individual LLMs and various ranking methods on the MixInstruct dataset (2306.02561.pdf, p. 7). Key results for the top-performing individual LLM (Open Assistant) and the proposed methods are shown below:

| Method | BERTScore↑ | BARTScore↑ | BLEURT↑ | GPT-Rank↓ | Top-3(%)↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Open Assistant (best LLM) | 74.68 | -3.45 | -0.39 | 3.90 | 51.98 |
| PairRanker (selection) | 72.97 | -3.14 | -0.37 | 3.20 | 65.12 |
| LLM-BLENDER (PR + GF) | 79.09 | -3.02 | -0.17 | 3.01 | 68.59 |

(2306.02561.pdf, p. 7, Table 2)

The paper also provides results on conventional NLG tasks. For example, on CommonGen, the base T5-large model achieves a CIDEr score of 15.48, while PAIRRANKER (max logits) improves it to 15.86 (2306.02561.pdf, p. 16, Table 5). On WMT18 (zh-en), the base Opus-MT model achieves a BLEU score of 19.29, which PAIRRANKER (max logits) improves to 20.47 (2306.02561.pdf, p. 16, Table 6).

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
*   **PAIRRANKER**: Training was completed on a single RTX 8000 GPU in two days (2306.02561.pdf, p. 14). The backbone model is DeBERTa-v3-large (400m parameters) (2306.02561.pdf, p. 7).
*   **GENFUSER**: This module is based on Flan-T5-XL, which has 3 billion parameters (2306.02561.pdf, p. 6, 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The paper includes an "Ethical Statement" section which declares that the work fully complies with the ACL Ethics Policy and that, to the best of the authors' knowledge, there are no ethical issues in the paper (2306.02561.pdf, p. 10).

One of the stated goals of the ensembling framework is to reduce biases, errors, and uncertainties found in individual models, yielding outputs that are better aligned with human feedback (2306.02561.pdf, p. 9). The paper does not mention the use of any sensitive data.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Efficiency**: The PAIRRANKER module, when used for optimal performance with the `MaxLogits` method, may require O(N²) inference calls to build the full comparison matrix, which can be computationally expensive. However, these inferences can be executed in parallel (2306.02561.pdf, p. 9, 10).
*   **Evaluation Limitations**: The evaluation relies on automatic metrics and ChatGPT for pairwise comparisons. The authors acknowledge that large-scale human evaluation was not affordable but would provide more reliable results (2306.02561.pdf, p. 10).
*   **Performance Bound**: The effectiveness of the selection-based part of the framework (PAIRRANKER) is ultimately constrained by the quality of the candidate outputs generated by the initial set of LLMs (2306.02561.pdf, p. 6).

### Recommendations:
*   For users concerned about inference efficiency, the paper recommends using the **bubble sort** aggregation method. It requires only N-1 comparisons and achieves high performance, making it a more efficient approach for most applications (2306.02561.pdf, p. 17).
*   To achieve the highest possible performance and pursue marginal improvements, users can apply the **MaxLogits** aggregation method, which leverages the full comparison matrix. This can be done with parallel computing to manage the increased number of inferences (2306.02561.pdf, p. 17).