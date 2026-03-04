## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from Stanford University and DataBricks (2403.18421.pdf, p. 1). The authors are listed as: Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (2403.18421.pdf, p. 1).

### Model date:
The model was made publicly available in December 2022 (2403.18421.pdf, p. 2). The accompanying academic paper was submitted in March 2024 (2403.18421.pdf, p. 1).

### Model version:
The model is named BioMedLM and is a 2.7 billion parameter GPT-style autoregressive model (2403.18421.pdf, p. 1, Abstract). It is architecturally similar to GPT-Neo 2.7B, with a nearly identical parameter count, but is trained exclusively on biomedical text, which leads to substantial performance improvements on biomedical question-answering tasks (2403.18421.pdf, p. 12).

### Model type:
BioMedLM is an autoregressive, decoder-only Transformer language model with a GPT-2 style architecture (2403.18421.pdf, p. 4).

**Architecture Details:**
*   **Model Type:** gpt2 (config.json.txt)
*   **Parameters:** 2.7 billion (2403.18421.pdf, p. 4)
*   **Layers:** 32 (config.json.txt; 2403.18421.pdf, p. 4, Table 1)
*   **Attention Heads:** 20 (config.json.txt; 2403.18421.pdf, p. 4, Table 1)
*   **Hidden Size (Embedding Dimension):** 2560 (config.json.txt; 2403.18421.pdf, p. 4, Table 1)
*   **Vocabulary Size:** 28,896 (config.json.txt; 2403.18421.pdf, p. 4, Table 1)
*   **Context Length (Sequence Length):** 1024 (config.json.txt; 2403.18421.pdf, p. 4, Table 1)
*   **Activation Function:** gelu_new (config.json.txt)

**Tokenizer:**
The model uses a custom Byte-Pair Encoding (BPE) tokenizer trained on PubMed abstracts (2403.18421.pdf, p. 5; tokenizer_summary.json.txt). This domain-specific tokenizer represents common biomedical terms as single tokens, whereas a traditional GPT-2 tokenizer would split them. For example, "thrombin" is a single token for BioMedLM but is split into "th", "rom", and "bin" by the GPT-2 tokenizer (2403.18421.pdf, p. 5, Table 3). This approach was shown to provide a meaningful improvement on the MedQA task (2403.18421.pdf, p. 5, Table 4). The tokenizer class is `GPT2Tokenizer` (tokenizer_config.json.txt).

### Training details:
BioMedLM was pre-trained on 300 billion tokens from its training corpus (2403.18421.pdf, p. 6). The training process used the following algorithms, parameters, and methodologies:

*   **Algorithm:** The model was trained to minimize the standard cross-entropy loss of the subsequent token using the Decoupled AdamW optimizer (2403.18421.pdf, p. 6). The training utilized Flash Attention to accelerate and reduce memory requirements (2403.18421.pdf, p. 6).
*   **Key Parameters and Hyperparameters** (2403.18421.pdf, p. 6, Table 5):
    *   **Tokens Per Batch:** 1,048,576
    *   **Sequence Length:** 1024
    *   **Learning Rate:** 1.6e-4
    *   **Scheduler:** Cosine with a linear warmup of 100 batches
    *   **Adam Epsilon:** 1e-8
    *   **Adam Betas:** [0.9, 0.95]
    *   **Weight Decay:** 1.6e-5
*   **Precision:** The model was trained using mixed precision. Parameters and optimizer states were stored in fp32, gradient communication was done in fp32, and the core computation was done in bf16 (2403.18421.pdf, p. 6, Table 6). This switch to bf16 resolved training loss divergences encountered in initial trial runs that used fp16 (2403.18421.pdf, p. 6).

### Paper or other resource for more information:
*   **Academic Paper:** Bolton, E., Venigalla, A., Yasunaga, M., et al. (2024). *BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text*. This paper details the model's architecture, training, and evaluation. Link: https://arxiv.org/abs/2403.18421 (2403.18421.pdf).
*   **Hugging Face Hub:** The pre-trained model is available for download from the Hugging Face Hub. Link: https://huggingface.co/stanford-crfm/BioMedLM (2403.18421.pdf, p. 1, 14).
*   **GitHub Repository:** The code used for pre-training and fine-tuning is available on GitHub. Link: https://github.com/stanford-crfm/BioMedLM (2403.18421.pdf, p. 7, 14).

### Citation details:
Insufficient information. (The paper provides a citation for itself, but not a specific BibTeX entry for the model artifact).

### License:
Insufficient information.

### Contact:
For correspondence, the developers can be contacted at:
*   elliotbolton@stanford.edu
*   manning@stanford.edu
(2403.18421.pdf, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BioMedLM is a GPT-style autoregressive model designed as a foundation for biomedical Natural Language Processing (NLP) applications (2403.18421.pdf, p. 1). Its primary intended use is for downstream question-answering tasks after being fine-tuned. The model has demonstrated strong performance on multiple-choice biomedical question-answering benchmarks, including:
*   MedMCQA (questions from Indian medical school entrance exams) (2403.18421.pdf, p. 8)
*   MedQA (USMLE-style questions) (2403.18421.pdf, p. 8)
*   MMLU (tests on Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics) (2403.18421.pdf, p. 9)
*   PubMedQA and BioASQ (yes/no/maybe question answering on biomedical passages) (2403.18421.pdf, p. 9-10)

After fine-tuning on instruction datasets, the model is also capable of producing useful, multi-sentence answers to patient questions on medical topics (e.g., "What are good treatments for arthritis?") (2403.18421.pdf, p. 1, 10). The model is intended to serve as a transparent, privacy-preserving, and economical alternative to larger, closed models for applications in biomedicine (2403.18421.pdf, p. 1).

### Primary intended users:
The primary intended users are researchers, biomedical organizations, and healthcare organizations, particularly those with limited computational resources or strict privacy requirements that prevent the use of API-based models (2403.18421.pdf, p. 2).

### Out-of-scope uses:
The base, pre-trained BioMedLM model is not well-suited for direct question response without being fine-tuned on an instruction dataset, as it was trained to replicate text from PubMed articles (2403.18421.pdf, p. 10).

The model is prone to hallucination, especially around numerical values. For example, it incorrectly stated that 10% of people in the US have Vitamin D deficiency, when the actual figure is closer to 35% (2403.18421.pdf, p. 12). Therefore, it should not be used in applications that provide answers to patients without "additional safeguards to correct incorrect numerical values" (2403.18421.pdf, p. 12). It is not intended for direct use in clinical decision-making.

---

## How to Use
This section outlines how to use the model.

The pre-trained model is available on the Hugging Face Hub at https://huggingface.co/stanford-crfm/BioMedLM (2403.18421.pdf, p. 14). The code for pre-training and fine-tuning is available on GitHub at https://github.com/stanford-crfm/BioMedLM (2403.18421.pdf, p. 14).

The model is intended to be fine-tuned for specific downstream tasks. The paper describes several fine-tuning approaches:
*   **Multiple-Choice Question Answering (e.g., MedQA, MMLU):** For each question, the question context is concatenated with each answer option. Each of these combined sequences is run through the model, and the final hidden state is passed to a linear classifier to generate a score for each option. The option with the highest score is selected as the answer (2403.18421.pdf, p. 7).
*   **Yes/No/Maybe Question Answering (e.g., PubMedQA, BioASQ):** The input is formatted with special tokens to separate the context and the question. The hidden state corresponding to a special token at the end of the sequence is fed to a linear classifier to produce scores for "yes", "no", or "maybe" (2403.18421.pdf, p. 7). An example of the optimal format is:
    `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]` (2403.18421.pdf, p. 8)
*   **Long-Form Question Answering:** The model can be fine-tuned on a collection of medical question/answer pairs to generate multi-sentence answers (2403.18421.pdf, p. 8, 10). An example output for the question "What does vitamin D do?" is:
    > "Vitamin D plays an important role in maintaining your bones and supporting your immune system. It's also involved in many other body processes. Vitamin D is a fat-soluble vitamin. Your body needs to get this vitamin from your diet and/or your sun exposure. You can get vitamin D from foods that contain vitamin D, such as fatty fish, eggs and fortified milk. You can also get vitamin D from sun exposure. Your body needs to get enough vitamin D to function properly. Vitamin D deficiency can cause rickets in children and osteomalacia in adults. Vitamin D deficiency can also cause muscle weakness and an increased risk of falls and bone fractures. Vitamin D deficiency is a common condition. In the United States, about 1 in 10 people have vitamin D deficiency." (2403.18421.pdf, p. 11, Table 12)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Domain of Training Data:** The model's performance is heavily influenced by its domain-specific pre-training on biomedical text (PubMed). This is demonstrated by its substantial outperformance of the architecturally similar GPT-Neo 2.7B model, which was trained on a general English corpus (2403.18421.pdf, p. 12).
*   **Domain Drift:** The model's performance can be affected by shifts in domain between the training data and the evaluation task. For example, its performance is weaker on the MMLU College Biology topic, which is likely due to the "domain drift between college level biology topics and formal PubMed articles" (2403.18421.pdf, p. 12).

### Evaluation factors:
The model was evaluated across several biomedical sub-domains represented by different question-answering datasets. These include:
*   Clinical knowledge and professional medicine (MedQA, MedMCQA, MMLU Professional Medicine) (2403.18421.pdf, p. 8-9)
*   Fundamental biochemistry and medical genetics (MedMCQA, MMLU Medical Genetics) (2403.18421.pdf, p. 8-9)
*   College-level biology (MMLU College Biology) (2403.18421.pdf, p. 9)
*   Question answering based on biomedical abstracts (PubMedQA, BioASQ) (2403.18421.pdf, p. 9-10)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Accuracy:** The primary metric used to evaluate the model's performance on all downstream question-answering tasks (MedMCQA, MedQA, MMLU, PubMedQA, BioASQ) is test accuracy (2403.18421.pdf, p. 8-10, Tables 7-11).
*   **Cross-Entropy Loss:** During pre-training, the model's performance was tracked using cross-entropy loss on both the training and validation sets (2403.18421.pdf, p. 7, Figure 1).

### Decision thresholds:
For multiple-choice and classification tasks (MedQA, MedMCQA, MMLU, PubMedQA, BioASQ), a linear classifier is used on the final hidden state to produce scores for each possible answer. The answer with the highest score is chosen. This implies a "winner-takes-all" approach rather than a specific numerical threshold (2403.18421.pdf, p. 7).

### Variation approaches:
To test the impact of the custom tokenizer, experiments at the 125 million parameter scale were run over 5 random seeds to ensure the observed improvement was meaningful (2403.18421.pdf, p. 5). For the final 2.7B model results, the paper does not specify if they are averaged over multiple fine-tuning runs.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several standard biomedical question-answering benchmarks:
*   **MedMCQA:** Contains 182,822/4,183/6,150 train/dev/test questions from Indian medical school entrance exams (AIIMS PG and NEET PG). Questions are multiple-choice with four options (2403.18421.pdf, p. 8).
*   **MedQA:** Contains 10,178/1,272/1,273 train/dev/test questions from USMLE (US Medical Licensing Examination) questions found on the web. Questions present a medical scenario with four answer options (2403.18421.pdf, p. 8).
*   **MMLU (Massive Multitask Language Understanding):** A collection of subject tests. BioMedLM was evaluated on the biomedical-related exams: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (2403.18421.pdf, p. 9).
*   **PubMedQA:** Contains 450/50/500 train/dev/test questions constructed from PubMed article abstracts. Each question is answered with "yes", "no", or "maybe" (2403.18421.pdf, p. 9).
*   **BioASQ:** Contains 670/75/140 train/dev/test questions based on biomedical passages, with "yes" or "no" answers (2403.18421.pdf, p. 10).
*   **Consumer Health Questions:** For evaluating long-form answer generation, a dataset of over 53,000 medical question/answer pairs directed towards patients was collected from publicly available sources on the web (2403.18421.pdf, p. 8, 10).

### Motivation:
These datasets were chosen because they are standard benchmarks for biomedical NLP, allowing for direct comparison with other state-of-the-art models, including much larger ones like GPT-4 and Flan-PaLM (2403.18421.pdf, p. 8).

### Preprocessing:
For fine-tuning, the evaluation data was formatted into specific prompt structures:
*   For multiple-choice tasks, the question context was concatenated with each answer option to create separate inputs for the model (2403.18421.pdf, p. 7).
*   For yes/no/maybe tasks, special tokens (`[Context Token]`, `[Question Token]`, `[Answer Token]`) were introduced to structure the input, which was found to significantly improve performance (2403.18421.pdf, p. 7-8).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained exclusively on the subparts of The Pile dataset (as of November 2022) containing PubMed abstracts and full articles (2403.18421.pdf, p. 5). The training corpus contained 34.6 billion tokens (2403.18421.pdf, p. 5). The training run performed 8.67 passes through the data (2403.18421.pdf, p. 5).

### Motivation:
The choice of PubMed data was to create a domain-specific model for biomedicine. The goal was to investigate the value of domain specialization and the potential for smaller, targeted models to achieve strong performance on domain-specific tasks (2403.18421.pdf, p. 2).

### Preprocessing:
The primary preprocessing step was the creation and application of a custom Byte-Pair Encoding (BPE) tokenizer. This tokenizer was trained on PubMed abstracts to create a vocabulary of 28,896 tokens that is optimized for biomedical terminology (2403.18421.pdf, p. 5; tokenizer_summary.json.txt). During training, the data was processed into sequences of 1024 tokens (2403.18421.pdf, p. 6).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides disaggregated accuracy results for the MMLU benchmark across four biomedical and biological topics. The model was fine-tuned on MedMCQA and MedQA data before this evaluation (2403.18421.pdf, p. 9, Table 9).

| MMLU Topic | BioMedLM Accuracy |
| :--- | :--- |
| Clinical Knowledge | 59.6% |
| Professional Medicine | 63.1% |
| College Biology | 60.7% |
| Medical Genetics | 69.0% |

The paper notes that the model performs worst on College Biology, likely due to domain drift between the formal PubMed articles in its training data and college-level biology topics (2403.18421.pdf, p. 12).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper states that inference with the model can be run on a laptop, implying relatively low memory requirements for loading and inference (2403.18421.pdf, p. 2).

### Deploying Requirements:
Similar to loading, the model's small size allows it to be served internally by organizations, even on a laptop, without needing large compute clusters (2403.18421.pdf, p. 2).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training run was completed in 6.25 days on 128 40GB Nvidia A100 GPUs (2403.18421.pdf, p. 6).
*   **Fine-tuning:** The model's size allows it to be "comfortably fine-tuned on a single A100 GPU" (2403.18421.pdf, p. 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Privacy:** The model was developed as a privacy-preserving alternative to large, closed models that require users to send data over the internet. Since BioMedLM is small enough to be run locally (e.g., on a laptop or internal servers), organizations can use it without sending potentially sensitive patient data to third parties, helping to comply with regulations like HIPAA (2403.18421.pdf, p. 1-2).
*   **Data Transparency:** The model was trained exclusively on publicly available PubMed abstracts and full articles. This fully documented training data allows practitioners and researchers to have insight into the model's knowledge base, in contrast to closed models trained on secret data (2403.18421.pdf, p. 2). No sensitive or private data was used in pre-training.
*   **Risk of Hallucination:** A significant risk is the model's tendency to hallucinate, particularly with numerical values. The paper provides an example where the model generated an incorrect statistic about Vitamin D deficiency (2403.18421.pdf, p. 12). This poses a risk of providing misinformation, especially in a critical domain like healthcare. The developers note that any application using this model to provide answers to patients would need "additional safeguards to correct incorrect numerical values" (2403.18421.pdf, p. 12).
*   **Accessibility:** By creating a smaller, open-source model, the developers aim to make language model technology more accessible to biomedical and healthcare organizations that may have limited resources (2403.18421.pdf, p. 2).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Fine-tuning is Required:** The base pre-trained model is not suitable for direct question-answering. It was trained to replicate text from its source data (PubMed articles) and must be fine-tuned on an instruction-based dataset to perform question-answering tasks effectively (2403.18421.pdf, p. 10).
*   **Numerical Inaccuracy:** The model is prone to hallucinating numerical values. It should not be trusted to provide accurate statistics or other numbers without external fact-checking (2403.18421.pdf, p. 12).
*   **Domain Sensitivity:** The model's performance is best on tasks that are closely aligned with its training data of formal biomedical literature. It may perform worse on related but distinct domains, such as college-level biology, due to domain drift (2403.18421.pdf, p. 12).

### Recommendations:
*   **Use Safeguards for Patient-Facing Applications:** For any application that generates answers for patients or non-experts, users should implement additional safeguards to fact-check the model's output, especially for numerical claims (2403.18421.pdf, p. 12).
*   **Use Task-Specific Fine-tuning:** Users should fine-tune the model on data that is specific to their target task to achieve the best performance. The paper provides examples of specialized architectures for multiple-choice and classification tasks (2403.18421.pdf, p. 7).
*   **Consider Advanced Fine-tuning:** For tasks with small training sets like PubMedQA, performance might be improved by exploring a 2-phase fine-tuning approach, where the model is first tuned on related noisy or unlabeled data before being tuned on the target task's training data (2403.18421.pdf, p. 12).

---