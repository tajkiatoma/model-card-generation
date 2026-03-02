## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Dongfu Jiang, Xiang Ren, and Bill Yuchen Lin from the Allen Institute for Artificial Intelligence, University of Southern California, and Zhejiang University (Source: 2306.02561.pdf, page 1).

### Model date:
The associated academic paper was submitted to arXiv on June 30, 2023 (Source: 2306.02561.pdf, page 1).

### Model version:
This model is the `PAIRRANKER` module from the LLM-BLENDER framework. LLM-BLENDER is an ensembling framework that also includes a `GENFUSER` module for fusing ranked outputs. This `PAIRRANKER` module is designed to compare pairs of candidate outputs from different Large Language Models (LLMs) and determine the superior one (Source: 2306.02561.pdf, Abstract, Section 2.3).

### Model type:
The model is a pairwise ranking model, specifically a `pairranker`, designed to rank text outputs from other language models (Source: ranker_config.json.txt).
*   **Architecture:** It is a Transformer-based model that employs a cross-attention encoder to jointly encode an input text and a pair of candidate outputs to determine which is better (Source: 2306.02561.pdf, Section 3). The backbone model is `microsoft/deberta-v3-large` (Source: ranker_config.json.txt; 2306.02561.pdf, Section 5.2). The architecture includes a five-layer multi-layer perceptron (MLP) with hyperbolic tangent activation function on top of the Transformer embeddings (Source: 2306.02561.pdf, Appendix A).
*   **Tokenizer:** The model uses a `DebertaV2Tokenizer` (Source: tokenizer_config.json.txt). The tokenizer is based on a Unigram model with a vocabulary size of 128,000 (Source: tokenizer_summary.json.txt).
*   **Context Length:** The model supports a source maximum length of 1224 tokens and a candidate maximum length of 412 tokens (Source: ranker_config.json.txt).

### Training details:
The `PAIRRANKER` module is trained to discern subtle differences between candidate outputs from various LLMs.
*   **Algorithm:** The model is trained using a pairwise comparison approach. It takes an input `x` and two candidate outputs `yi` and `yj` and learns to determine which candidate is better (Source: 2306.02561.pdf, Section 3.2). The training objective is treated as a multi-task classification problem, using a binary cross-entropy (BCE) loss (Source: 2306.02561.pdf, Section 3.3, Appendix A). The loss type is specified as `instructgpt` in the configuration (Source: ranker_config.json.txt).
*   **Parameters and Hyperparameters:**
    *   **Optimizer:** Adafactor optimizer (Source: 2306.02561.pdf, Appendix A).
    *   **Learning Rate:** Maximum learning rate of 1e-5 with a 5% warm-up ratio and a linear learning rate scheduler (Source: 2306.02561.pdf, Appendix A).
    *   **Epochs:** 5 epochs (Source: 2306.02561.pdf, Appendix A).
    *   **Batch Size:** 64 (Source: 2306.02561.pdf, Appendix A).
    *   **Dropout:** 0.05 (Source: ranker_config.json.txt).
    *   **Precision:** The model was trained with `fp16` precision (Source: ranker_config.json.txt).
*   **Sub-sampling:** During training, a sub-sampling strategy is used. The paper mentions using 5 pairs per input (Source: 2306.02561.pdf, Section 3.3), while the configuration file specifies a sub-sampling ratio of 0.4 for `all_pair` mode (Source: ranker_config.json.txt). To ensure consistency, the order of candidates within each training pair is shuffled (Source: 2306.02561.pdf, Section 3.3).

### Paper or other resource for more information:
The model is described in the academic paper "LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion". The paper introduces the LLM-BLENDER framework, which includes the `PAIRRANKER` (this model) and `GENFUSER` modules. It also introduces the `MixInstruct` benchmark for evaluation and presents results showing the framework's effectiveness.
*   **Paper:** [https://arxiv.org/abs/2306.02561](https://arxiv.org/abs/2306.02561) (Source: 2306.02561.pdf).
*   **Project Website:** [https://yuchenlin.xyz/LLM-Blender](https://yuchenlin.xyz/LLM-Blender) (Source: 2306.02561.pdf, page 1).

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
(Source: 2306.02561.pdf)

### License:
Insufficient information.

### Contact:
Contact information for the developers can be found in the associated paper:
*   dongfu@zju.edu.cn
*   xiangren@usc.edu
*   yuchenl@allenai.org

(Source: 2306.02561.pdf, page 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The `PAIRRANKER` model is intended to be used as part of an ensembling framework for Large Language Models (LLMs). Its primary purpose is to rank a list of candidate outputs generated by multiple LLMs for a given input instruction. It is designed to distinguish subtle differences between high-quality candidate outputs to select the best one (Source: 2306.02561.pdf, Abstract, Section 3). The model can be used to improve the overall quality, robustness, and reliability of responses in instruction-following tasks (Source: 2306.02561.pdf, Section 1).

The model takes a source input and a pair of candidate texts and outputs scores indicating which candidate is superior. These pairwise scores can then be aggregated to produce a full ranking of all candidates (Source: 2306.02561.pdf, Section 3.3).

### Primary intended users:
The primary intended users are researchers and practitioners in the field of Natural Language Processing and AI who are deploying or studying LLMs. The framework is intended to benefit those looking to improve the performance of LLMs through ensemble learning (Source: 2306.02561.pdf, Section 2, Section 7).

### Out-of-scope uses:
The model is a ranker, not a generative model. It should not be used to generate text from scratch. It is designed to rank existing candidate texts. The model was trained and evaluated on instruction-following tasks in English (and Chinese for translation). Its performance on other tasks, modalities, or languages is not guaranteed and would be considered out-of-scope (Source: 2306.02561.pdf, Section 5, Appendix C.1).

---

## How to Use
This section outlines how to use the model. 

The model is designed to compare a pair of candidate texts (`candidate1`, `candidate2`) for a given source input (`source`). The inputs should be concatenated into a single string using special separator tokens (Source: 2306.02561.pdf, Section 3.3).

**Input Format:**
The input sequence should be formatted as follows:
`<s><source> [source_text] </s> <candidate1> [candidate1_text] </s> <candidate2> [candidate2_text] </s>`

The special tokens `<|source|>`, `<|candidate1|>`, and `<|candidate2|>` are available in the tokenizer (Source: added_tokens.json.txt). The standard `<s>` and `</s>` tokens from the DeBERTa tokenizer should also be used for separation.

**Output:**
The model outputs logits that represent the comparison result. These logits can be used to compute a confidence score indicating which candidate is better. By performing pairwise comparisons for all candidate pairs, a full ranking can be inferred (Source: 2306.02561.pdf, Section 3.3).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors:
*   **Diversity of Ensembled LLMs:** The effectiveness of the ranking depends on the strengths and weaknesses of the pool of LLMs being ensembled. The framework is designed to leverage this diversity (Source: 2306.02561.pdf, Section 1).
*   **Task Type:** The model's performance was evaluated on instruction-following, summarization, machine translation, and constrained text generation. Performance may vary on other tasks (Source: 2306.02561.pdf, Section 5, Appendix C).
*   **Candidate Length:** The paper hypothesizes that the model performs better than baselines on shorter texts where differences are more subtle, as seen in its strong performance on CommonGen and WMT18 compared to the longer-text summarization task (Source: 2306.02561.pdf, Appendix C.4).

### Evaluation factors:
The model was evaluated based on:
*   **Ranking Correlation:** The correlation of its rankings with an oracle ranking (GPT-Rank) was measured (Source: 2306.02561.pdf, Table 3).
*   **Downstream Task Metrics:** The quality of the top-ranked candidate selected by the model was evaluated using standard NLG metrics like BERTScore, BARTScore, BLEURT, and CIDEr on various datasets (Source: 2306.02561.pdf, Tables 2, 4, 5, 6).
*   **Base Model Generalization:** The model's ability to rank outputs from models not seen during training (like GPT-3) was evaluated (Source: 2306.02561.pdf, Tables 4, 5, 6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The performance of the `PAIRRANKER` is assessed in two ways:
1.  **Rank Correlation:** To measure how well the model's rankings align with an oracle (ChatGPT-based) ranking, the following metrics are used:
    *   **Pearson Correlation Coefficient**
    *   **Spearman's Correlation**
    *   **Spearman's Footrule distance**
    (Source: 2306.02561.pdf, Table 3)
2.  **Quality of Top-Ranked Selection:** The quality of the candidate chosen by the ranker is evaluated using standard NLG metrics on downstream tasks. These include:
    *   **BERTScore, BARTScore, BLEURT:** For summarization and general instruction-following (Source: 2306.02561.pdf, Section 5.1, Table 2).
    *   **BLEU, CIDEr:** For machine translation and commonsense generation (Source: 2306.02561.pdf, Appendix C.1).
    *   **GPT-Rank:** A metric based on pairwise comparisons from ChatGPT, where a lower rank is better (Source: 2306.02561.pdf, Section 5.1).

### Decision thresholds:
During inference, the model produces a matrix `M` of pairwise scores. The final ranking is determined by aggregating these scores. Three aggregation methods are proposed:
*   **MaxLogits:** The score for a candidate is the sum of its comparison scores against all others. This is the default method as it yields the best performance.
*   **MaxWins:** The score is the number of "wins" in pairwise comparisons.
*   **Bubble Sort:** An efficient O(N) method that performs N-1 comparisons to find the best candidate.
(Source: 2306.02561.pdf, Section 3.3, Figure 4)

### Variation approaches:
The oracle ranking for evaluation, named GPT-Rank, is established by prompting ChatGPT to perform pairwise comparisons on all candidate pairs and determining the rank by the number of wins (Source: 2306.02561.pdf, Section 5.1). For training supervision on some tasks, automatic metrics like BARTScore are used to label the better candidate in a pair, as BARTScore was found to have the highest correlation with GPT-Rank (Source: 2306.02561.pdf, Section 5.2, Table 3).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several datasets:
1.  **MixInstruct:** A new benchmark dataset created for this work. It consists of 110k instruction-following examples from four sources (Alpaca-GPT4, Dolly-15K, GPT4All-LAION, ShareGPT). For each example, candidate outputs from 11 open-source LLMs are provided. The dataset is split into 100k training, 5k validation, and 5k test sets. The test set includes oracle pairwise comparisons from ChatGPT (Source: 2306.02561.pdf, Section 2.2, Table 1).
2.  **CNN/DailyMail:** A standard dataset for abstractive text summarization (Source: 2306.02561.pdf, Appendix C.1).
3.  **CommonGen:** A dataset for constrained commonsense generation, containing 79k descriptions (Source: 2306.02561.pdf, Appendix C.1).
4.  **WMT18 (zh-en):** A dataset for Chinese-to-English machine translation (Source: 2306.02561.pdf, Appendix C.1).

### Motivation:
*   **MixInstruct** was created specifically to provide a large-scale benchmark for training and evaluating LLM ensembling methods on diverse instruction-following tasks (Source: 2306.02561.pdf, Section 2.2).
*   **CNN/DM, CommonGen, and WMT18** were chosen as they are standard, public benchmarks for evaluating performance on conventional NLG tasks (summarization, generation, translation), allowing for comparison with prior work and testing the model's generalization capabilities (Source: 2306.02561.pdf, Appendix C.1).

### Preprocessing:
For the evaluation sets of all datasets, candidate outputs were generated from various base models (e.g., 11 LLMs for `MixInstruct`, PEGASUS for CNN/DM). For the `MixInstruct` test set, oracle pairwise comparisons were generated by prompting ChatGPT with a specific template to judge the better candidate between pairs (Source: 2306.02561.pdf, Section 2.2, Appendix E).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The primary training dataset is the 100k training split of the **MixInstruct** dataset. This dataset contains instruction-input pairs sourced from Alpaca-GPT4, Dolly-15K, GPT4All-LAION, and ShareGPT. For each input, the dataset includes candidate outputs generated by 11 popular open-source LLMs (including Vicuna, OpenAssistant, Alpaca, MPT, etc.) (Source: 2306.02561.pdf, Section 2.2, Table 1). For training on conventional NLG tasks (CNN/DM, CommonGen, WMT18), a special procedure was used where base models were fine-tuned on one half of the training data and then used to generate candidates on the other half, creating a full training set of generated candidates (Source: 2306.02561.pdf, Appendix C.3).

### Motivation:
The `MixInstruct` dataset was chosen to train the ranker on a diverse set of high-quality outputs from multiple strong LLMs, which is representative of the intended use case. This allows the model to learn to distinguish subtle but important differences between candidates for instruction-following tasks (Source: 2306.02561.pdf, Section 2.2).

### Preprocessing:
The training data was preprocessed by forming pairs of candidate outputs for each source input. A label indicating the better candidate was generated using automatic metrics (like BARTScore) or oracle judgments (from ChatGPT) (Source: 2306.02561.pdf, Section 2.3, 3.2). A sub-sampling strategy was applied, where 5 random pairs were selected per input for training efficiency (Source: 2306.02561.pdf, Section 3.3). The order of candidates in each pair was also shuffled during training to help the model learn consistently (Source: 2306.02561.pdf, Section 3.3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is presented against several individual LLMs and other ranking methods.
*   On the **MixInstruct** dataset, `PAIRRANKER` (with MaxLogits aggregation) achieves a GPT-Rank of 3.20, outperforming the best individual LLM, OpenAssistant (3.90), and other rankers like SimCLS (3.50) and SummaReranker (3.66). The top-1 selections from `PAIRRANKER` are better than or equal to Vicuna in 54.76% of cases and OpenAssistant in 57.79% of cases (Source: 2306.02561.pdf, Table 2).
*   On **CommonGen** with a T5-large base model, `PAIRRANKER` (max logits) improves the CIDEr score from 15.48 to 15.86 (a 2.45% gain) (Source: 2306.02561.pdf, Table 5).
*   On **WMT18 (zh-en)** with an Opus-MT base model, `PAIRRANKER` (max logits) improves the BLEU score from 19.29 to 20.47 (a 6.12% gain) (Source: 2306.02561.pdf, Table 6).
*   On **CNN/DailyMail** with a PEGASUS-large base model, `PAIRRANKER` (max logits) improves the Rouge-1 score from 44.56 to 47.39 (a 6.35% gain) (Source: 2306.02561.pdf, Table 4).

### Intersectional results:
Insufficient information. The paper does not provide performance results disaggregated by demographic or other intersectional factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The `PAIRRANKER` model was trained on a single RTX 8000 GPU. The training process took two days to complete for 5 epochs (Source: 2306.02561.pdf, Appendix A). Training was performed using `fp16` precision (Source: ranker_config.json.txt).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The authors state that "This work fully complies with the ACL Ethics Policy. We declare that there are no ethical issues in this paper, to the best of our knowledge." (Source: 2306.02561.pdf, *Ethical Statement).

The training data is derived from publicly available datasets created by other researchers. The model itself is a ranker and does not generate new content, but it selects from content generated by other LLMs. Therefore, potential risks are related to the biases inherent in the LLMs being ensembled. The `PAIRRANKER` could potentially learn to prefer certain types of biased or harmful content if the supervisory signal (e.g., BARTScore or ChatGPT's preferences) has such biases. The paper does not analyze the model for fairness or bias.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Efficiency:** The most effective aggregation method, `MaxLogits`, requires O(N²) pairwise comparisons for N candidates, which can be computationally expensive. While a more efficient `bubble sort` method is proposed (O(N)), it may result in slightly lower performance (Source: 2306.02561.pdf, *Limitations, Appendix C.4). However, the O(N²) inferences can be executed in parallel as they are independent (Source: 2306.02561.pdf, *Limitations).
*   **Evaluation Limitations:** The evaluation relies heavily on automatic metrics and ChatGPT-based ranking (GPT-Rank) instead of large-scale human evaluation, which was not performed due to its high cost. These proxy evaluators have their own limitations and biases (Source: 2306.02561.pdf, *Limitations).
*   **Model Consistency:** The model's output can be sensitive to the order of the two candidates in the input pair, though this was mitigated during training by shuffling pairs (Source: 2306.02561.pdf, Section 3.3, Appendix C.5).

### Recommendations:
*   For inference, there is a trade-off between performance and efficiency. The `bubble sort` method is recommended for most cases due to its efficiency. If marginal performance improvements are critical and parallel computation is available, the `MaxLogits` method is recommended (Source: 2306.02561.pdf, Appendix C.4).
*   The ranker is trained on candidates from specific models and tasks. While it shows good generalization to GPT-3 outputs, its performance may vary when applied to outputs from LLMs or on tasks that are very different from its training distribution.