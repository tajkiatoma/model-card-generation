## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Dongfu Jiang, Xiang Ren, and Bill Yuchen Lin. The affiliated institutions are the Allen Institute for Artificial Intelligence, the University of Southern California, and Zhejiang University (LLM-BLENDER paper, page 1).

### Model date:
The academic paper describing the model was submitted to arXiv on June 30, 2023 (LLM-BLENDER paper, page 1).

### Model version:
This model card describes the PAIRRANKER component of the LLM-BLENDER framework, as presented in the research paper "LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion" (LLM-BLENDER paper, page 1). PAIRRANKER is a specialized pairwise comparison model designed to rank outputs from multiple Large Language Models (LLMs) (LLM-BLENDER paper, page 2). It differs from list-wise or point-wise ranking methods by jointly encoding a pair of candidate responses to better capture subtle differences between them (LLM-BLENDER paper, page 2, 4).

### Model type:
The model is a pairwise ranking model (`"ranker_type": "pairranker"`) designed to compare and rank text sequences (config.json).

*   **Architecture**: The model's backbone is a DeBERTa V3 Large model (`"model_name": "microsoft/deberta-v3-large"`) (config.json; LLM-BLENDER paper, page 7, 14). It employs Transformer layers with a cross-attention mechanism to jointly encode an input prompt and a pair of candidate responses to determine the superior one (LLM-BLENDER paper, page 2, 5). The input sequence is formed by concatenating the source text and two candidate texts, separated by special tokens: `<s><source> x </s> <candidate1> yi </s> <candidate2> yj </s>` (LLM-BLENDER paper, page 5). The tokenizer class is `DebertaV2Tokenizer` (tokenizer_config.json).
*   **Size**: The backbone model is DeBERTa-v3-large, which has 400 million parameters (LLM-BLENDER paper, page 7).
*   **Context Length**: The model supports a maximum source length of 1224 tokens and a maximum candidate length of 412 tokens (config.json).

### Training details:
The PAIRRANKER model was trained using the following configuration:
*   **Algorithm**: The model is trained on a multi-task classification problem where it learns to predict which of two candidates is better based on various quality metrics (e.g., BERTScore, BARTScore) (LLM-BLENDER paper, page 5). The training objective uses a multi-objective loss function, though the appendix notes that Binary Cross-Entropy (BCE) loss is also effective (LLM-BLENDER paper, page 5, 14). The loss type is specified as `instructgpt` in the configuration (config.json).
*   **Parameters and Hyperparameters**:
    *   **Optimizer**: Adafactor optimizer (LLM-BLENDER paper, Appendix A, page 14).
    *   **Learning Rate**: Maximum learning rate of 1e-5 with a 5% warm-up ratio and a linear learning rate scheduler (LLM-BLENDER paper, Appendix A, page 14).
    *   **Epochs**: 5 epochs (LLM-BLENDER paper, Appendix A, page 14).
    *   **Batch Size**: 64 (LLM-BLENDER paper, Appendix A, page 14).
    *   **Dropout**: A dropout rate of 0.05 is used (config.json).
    *   **Precision**: The model was trained with `fp16` precision (config.json).
*   **Methodologies**: To ensure learning efficiency, a sub-sampling strategy is applied during training, where 5 pairs of candidates are randomly selected per input for comparison (LLM-BLENDER paper, page 5). To make the model robust to the order of inputs, the order of candidates within each training pair is shuffled (LLM-BLENDER paper, page 6).

### Paper or other resource for more information:
The primary resource for this model is the academic paper:
*   **Title**: LLM-BLENDER: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion
*   **Authors**: Dongfu Jiang, Xiang Ren, Bill Yuchen Lin
*   **Link**: [arXiv:2306.02561v3](https://arxiv.org/abs/2306.02561)
The paper provides a comprehensive overview of the LLM-BLENDER framework, including the motivation, architecture, training process, and evaluation of the PAIRRANKER module (LLM-BLENDER paper, pages 1-18).

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
(LLM-BLENDER paper, page 1)

### License:
Insufficient information.

### Contact:
For questions or feedback, you can contact the authors via their emails provided in the paper: `dongfu@zju.edu.cn`, `xiangren@usc.edu`, `yuchenl@allenai.org` (LLM-BLENDER paper, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The PAIRRANKER model is intended to be used as a component in an ensemble learning framework for Large Language Models (LLMs). Its primary purpose is to rank a set of candidate outputs generated by multiple LLMs for a given input instruction (LLM-BLENDER paper, page 1). By comparing all candidates in a pairwise fashion, it can effectively discern subtle differences and select the highest-quality response (LLM-BLENDER paper, page 2).

The model is designed for instruction-following tasks and has also been evaluated on conventional Natural Language Generation (NLG) tasks, including:
*   Abstractive Summarization (LLM-BLENDER paper, Appendix C, page 15)
*   Machine Translation (LLM-BLENDER paper, Appendix C, page 15)
*   Constrained Text Generation (LLM-BLENDER paper, Appendix C, page 15)

The model takes a source text and a pair of candidate texts as input and outputs scores that determine which candidate is better (LLM-BLENDER paper, page 5).

### Primary intended users:
The primary users are researchers and practitioners in the field of AI and NLP who are interested in deploying, studying, or improving the performance of LLMs through ensemble methods (LLM-BLENDER paper, page 2).

### Out-of-scope uses:
This model is a **ranker**, not a text generator. It is not designed to produce text outputs on its own. Its purpose is to evaluate and rank existing text candidates generated by other models (LLM-BLENDER paper, page 9). Using it for any purpose other than ranking text pairs is out-of-scope.

---

## How to Use
This section outlines how to use the model.

The model is designed to compare two candidate texts (`candidate1`, `candidate2`) based on a source text (`source`).

**Input Structure:**
The input must be formatted as a single sequence with special tokens separating the three parts:
`<s><source> [source_text] </s> <candidate1> [candidate1_text] </s> <candidate2> [candidate2_text] </s>`
where `[source_text]`, `[candidate1_text]`, and `[candidate2_text]` are the corresponding text strings (LLM-BLENDER paper, page 5).

**Inference Process:**
During inference, the model is called for each pair of candidates `(yi, yj)` to obtain a comparison score `sij`, which represents the model's confidence that `yi` is better than `yj` (LLM-BLENDER paper, page 6). After comparing all pairs, these scores are collected into a comparison matrix `M`.

To determine the final ranking from the matrix `M`, one of three aggregation methods can be used:
1.  **MaxLogits**: Calculates a score for each candidate based on its cumulative logit difference against all other candidates. This method yields the best performance but requires O(N²) comparisons (LLM-BLENDER paper, page 6, 8).
2.  **MaxWins**: Calculates a score based on the number of "wins" for each candidate in pairwise comparisons (LLM-BLENDER paper, page 6).
3.  **Bubble Sort**: A more efficient method that performs a single run of bubble sort using pairwise comparisons to find the best candidate. This reduces the complexity to O(N) comparisons and is the default `inference_mode` in the configuration (config.json; LLM-BLENDER paper, page 6).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Task Type**: The model's performance is evaluated across different NLG tasks, such as instruction-following, summarization, and translation, indicating that the nature of the task is a relevant factor (LLM-BLENDER paper, page 7, 15-16).
*   **Quality of Candidate Models**: The performance of the ranker is inherently tied to the quality and diversity of the candidate outputs generated by the ensembled LLMs (LLM-BLENDER paper, page 1-2).
*   **Candidate Text Length**: The paper hypothesizes that the model's advantage over other rankers is more pronounced on tasks with shorter candidate texts (like translation or common sense generation) where direct attention between candidates is more effective at capturing subtle differences (LLM-BLENDER paper, Appendix C.4, page 16).

### Evaluation factors:
The model was evaluated by analyzing its performance across different:
*   **Base Models**: The ranker was applied to outputs from various models, including PEGASUS, T5-large, and GPT-3, to test its generalization capabilities (LLM-BLENDER paper, Appendix C.4, page 16).
*   **NLG Tasks**: The evaluation was conducted on the MixInstruct (instruction-following), CNN/DailyMail (summarization), CommonGen (constrained generation), and WMT18 (translation) datasets (LLM-BLENDER paper, page 7, 15-16).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using two main categories of metrics:

1.  **Ranking Correlation**: To measure how well the model's rankings align with oracle rankings (from ChatGPT), the following metrics are used:
    *   Pearson Correlation Coefficient
    *   Spearman's Correlation
    *   Spearman's Footrule distance
    (LLM-BLENDER paper, page 8, Table 3)

2.  **Quality of Top-Ranked Selection**: To evaluate the quality of the candidate selected by the ranker, the following metrics are used:
    *   **GPT-Rank**: An evaluation metric based on pairwise comparisons from ChatGPT, where a lower rank is better (LLM-BLENDER paper, page 6-7).
    *   **BERTScore**, **BARTScore**, **BLEURT**: Standard reference-based metrics for NLG evaluation (LLM-BLENDER paper, page 6-7).
    *   **Rouge-1, Rouge-2, Rouge-L**: For summarization tasks (LLM-BLENDER paper, Appendix C.1, page 15).
    *   **BLEU, CIDEr**: For generation and translation tasks (LLM-BLENDER paper, Appendix C.1, page 15).

### Decision thresholds:
Insufficient information. The model uses aggregation functions (MaxLogits, MaxWins, Bubble Sort) on pairwise comparison scores rather than a fixed decision threshold (LLM-BLENDER paper, page 6).

### Variation approaches:
Insufficient information. The paper reports performance on fixed test sets and does not mention the use of statistical methods like cross-validation or bootstrapping to estimate uncertainty.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several datasets:
*   **MixInstruct**: A benchmark dataset created for this work to evaluate LLM ensembling on instruction-following tasks. It contains 110k examples in total, with a 5k test set. The data is a mixture from four sources: Alpaca-GPT4, Dolly-15K, GPT4All-LAION, and ShareGPT. For each example, candidate outputs from 11 open-source LLMs are provided. The test set includes oracle pairwise comparisons from ChatGPT (LLM-BLENDER paper, page 3, Table 1).
*   **CNN/DailyMail**: A standard dataset for abstractive summarization (LLM-BLENDER paper, Appendix C.1, page 15).
*   **CommonGen**: A dataset for generative commonsense reasoning (LLM-BLENDER paper, Appendix C.1, page 15).
*   **WMT18 (zh-en)**: A dataset for Chinese-to-English machine translation (LLM-BLENDER paper, Appendix C.1, page 15).

### Motivation:
**MixInstruct** was created because there was a need for a large-scale benchmark to specifically train and evaluate ensembling methods for instruction-following LLMs (LLM-BLENDER paper, page 3, 9). The other datasets (CNN/DM, CommonGen, WMT18) were chosen as they are well-established benchmarks for conventional NLG tasks, allowing for evaluation of the model's generalization ability (LLM-BLENDER paper, Appendix C, page 15).

### Preprocessing:
For the MixInstruct test set, oracle rankings were obtained by prompting ChatGPT to perform pairwise comparisons for all 55 pairs of candidates for each input (LLM-BLENDER paper, page 3-4). The paper does not specify other preprocessing steps for the evaluation data.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was primarily trained on the **MixInstruct** dataset, which consists of 100k training examples and 5k validation examples (LLM-BLENDER paper, page 3, Table 1).

For experiments on conventional NLG tasks (summarization, translation, etc.), a specific training data generation strategy was used. The original training set (e.g., from CNN/DM) was split in half. Two separate base models were fine-tuned, each on one half of the data. Each model was then used to generate candidate outputs on the half of the data it had not seen. This process creates a training set of candidates that resembles the quality seen during inference, preventing the reranker from being over-optimized on artificially high-quality examples (LLM-BLENDER paper, Appendix C.3, page 15).

### Motivation:
The MixInstruct dataset was created to provide a large and diverse set of examples for training a model to rank outputs from multiple LLMs in instruction-following scenarios (LLM-BLENDER paper, page 3).

### Preprocessing:
The training data is structured into sequences of `“<s><source> x </s> <candidate1> yi </s> <candidate2> yj </s>”` (LLM-BLENDER paper, page 5). For the MixInstruct training set, supervision labels were generated by comparing candidates to a ground-truth response using automatic metrics like BERTScore, BLEURT, and BARTScore. The paper found that using BARTScore for supervision provided the highest correlation with the final oracle ranking (GPT-Rank) (LLM-BLENDER paper, page 4, 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is detailed in the paper:
*   **On MixInstruct**: PAIRRANKER achieves a GPT-Rank of 3.20, significantly outperforming the best individual LLM (OpenAssistant, 3.90) and other ranking methods like SimCLS (3.50) and SummaReranker (3.66). Its selections rank in the top 3 for 65.12% of examples (LLM-BLENDER paper, Table 2, page 7).
*   **Ranking Correlation**: PAIRRANKER achieves the highest correlation with oracle GPT-Rank across all metrics: Pearson (46.98), Spearman's (44.98), and Spearman's Footrule (27.52), surpassing all baseline metrics and other rankers (LLM-BLENDER paper, Table 3, page 8).
*   **On Conventional Tasks**:
    *   **Summarization (CNN/DM)**: Improves Rouge-1 score by 6.35% for PEGASUS and 6.64% for GPT-3 (LLM-BLENDER paper, Table 4, page 15).
    *   **Generation (CommonGen)**: Improves CIDEr score by 2.45% for T5-large and 26.53% for GPT-3 (LLM-BLENDER paper, Table 5, page 16).
    *   **Translation (WMT18)**: Improves BLEU score by 6.12% for Opus-MT and 11.65% for GPT-3 (LLM-BLENDER paper, Table 6, page 16).

### Intersectional results:
The paper analyzes the model's performance when applied to candidates generated by different base models (e.g., PEGASUS, T5-large, Opus-MT, GPT-3) across different tasks (summarization, generation, translation). The results consistently show that PAIRRANKER can generalize and improve the outputs of various models, even when not trained on their specific outputs (as in the GPT-3 experiments) (LLM-BLENDER paper, Tables 4, 5, 6, pages 15-16).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The training process for the PAIRRANKER model was completed on a single RTX 8000 GPU and took two days (LLM-BLENDER paper, Appendix A, page 14).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper includes an "Ethical Statement" section which states: "This work fully complies with the ACL Ethics Policy. We declare that there are no ethical issues in this paper, to the best of our knowledge" (LLM-BLENDER paper, page 10).

*   **Sensitive Data**: The paper does not mention the use of any sensitive or personally identifiable information. The training data was collected from publicly available open-source datasets (LLM-BLENDER paper, page 3).
*   **Risks and Mitigation**: The goal of the LLM-BLENDER framework is to improve LLM outputs by leveraging diverse strengths, which can help mitigate weaknesses, errors, and uncertainties present in individual models (LLM-BLENDER paper, page 2, 9). However, a potential risk is that an ensemble method could inadvertently amplify biases common across multiple underlying LLMs. The paper does not explicitly discuss bias mitigation strategies.
*   **Evaluation Limitations**: The authors acknowledge that the use of automatic metrics and ChatGPT for evaluation is a limitation compared to large-scale human evaluation, which was not feasible for the project (LLM-BLENDER paper, page 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Computational Cost**: A significant limitation is the efficiency of the ranking process. To achieve the best performance with the MaxLogits aggregation method, the model must be called O(N²) times for N candidates, which is computationally expensive. This can be a bottleneck when ensembling a large number of LLMs (LLM-BLENDER paper, page 9, 16).
*   **Evaluation Limitations**: The evaluation relies heavily on automatic metrics and ChatGPT-based rankings (GPT-Rank) rather than extensive human evaluation. While recent studies support using LLMs for evaluation, this approach has its own limitations and potential biases (LLM-BLENDER paper, page 10).
*   **Sub-optimal Efficient Inference**: The more efficient "bubble" inference method, which reduces complexity to O(N), provides strong but not optimal performance compared to the full comparison method (LLM-BLENDER paper, page 6, 17).

### Recommendations:
*   **Trade-off between Performance and Efficiency**: Users should choose an aggregation method based on their needs. For the highest possible performance, use the **MaxLogits** method and run the pairwise comparisons in parallel. For a more efficient solution with strong performance, use the **bubble sort** method (`inference_mode: "bubble"`), which requires only N-1 comparisons (LLM-BLENDER paper, page 6, 10, 17).
*   **Future Research**: The authors suggest that future work could involve developing more sophisticated ranking and fusion techniques and exploring the framework's transferability to other domains and non-text modalities (LLM-BLENDER paper, page 9).