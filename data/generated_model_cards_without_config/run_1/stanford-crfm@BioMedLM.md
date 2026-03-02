## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Stanford University and DataBricks (originally, MosaicML) (2403.18421.pdf, Page 1, Page 13). The authors are Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (2403.18421.pdf, Page 1).

### Model date:
The model was made publicly available in December 2022 (2403.18421.pdf, Page 2). The associated academic paper was submitted in March 2024 (2403.18421.pdf, Page 1).

### Model version:
The model is referred to as BioMedLM (2403.18421.pdf, Page 1). No specific version number is provided. It is a domain-specific model trained exclusively on biomedical text, which differentiates it from general-purpose models of a similar size, such as GPT-Neo 2.7B, which was trained on the diverse English corpus "The Pile" (2403.18421.pdf, Page 3, Page 12).

### Model type:
BioMedLM is a GPT-style, autoregressive, decoder-only Transformer model (2403.18421.pdf, Page 1, Page 4).

**Architecture Details:**
*   **Parameters:** 2.7 billion (2403.18421.pdf, Page 1).
*   **Layers:** 32 (2403.18421.pdf, Table 1, Page 4).
*   **Heads:** 20 (2403.18421.pdf, Table 1, Page 4).
*   **Hidden Size:** 2560 (2403.18421.pdf, Table 1, Page 4).
*   **Context Length:** 1024 tokens (2403.18421.pdf, Table 1, Page 4; tokenizer_config.json.txt, "model_max_length").
*   **Positional Embeddings:** Learned absolute positional embeddings (2403.18421.pdf, Page 4).

**Tokenizer Details:**
*   **Type:** A custom Byte-Pair Encoding (BPE) tokenizer trained on PubMed abstracts (2403.18421.pdf, Page 5; tokenizer_summary.json.txt, "model.type").
*   **Vocabulary Size:** 28,896 (2403.18421.pdf, Table 1, Page 4). The tokenizer files specify a vocab size of 28,895 regular tokens and one special token, `<|endoftext|>` (tokenizer_summary.json.txt, "model.vocab_size", "special_tokens").
*   **Pre-tokenizer:** ByteLevel pre-tokenizer (tokenizer_summary.json.txt, "pre_tokenizer.type").

### Training details:
The model was pre-trained for 300 billion tokens on the PubMed abstracts and full articles subset of The Pile dataset (as of November 2022), which contained 34.6 billion tokens in total. The training run performed 8.67 passes through the data (2403.18421.pdf, Page 5).

**Algorithm and Parameters:**
*   **Algorithm:** The model was trained to minimize the standard cross-entropy loss of the subsequent token using the Decoupled AdamW optimizer (2403.18421.pdf, Page 6).
*   **Batch Size:** 1024 (2403.18421.pdf, Page 6).
*   **Sequence Length:** 1024 (2403.18421.pdf, Page 6).
*   **Learning Rate:** 1.6e-4 (2403.18421.pdf, Table 5, Page 6).
*   **Scheduler:** Cosine with a linear warmup over 100 batches (2403.18421.pdf, Table 5, Page 6).
*   **Betas:** [0.9, 0.95] (2403.18421.pdf, Table 5, Page 6).
*   **Epsilon:** 1e-8 (2403.18421.pdf, Table 5, Page 6).
*   **Weight Decay:** 1.6e-5 (2403.18421.pdf, Table 5, Page 6).

**Precision and Hardware:**
*   The training was done in bf16 mixed precision, with parameters and optimizer states stored in fp32 (2403.18421.pdf, Table 6, Page 6).
*   The model was trained on the MosaicML Cloud platform across 128 40GB Nvidia A100 GPUs for 6.25 days (2403.18421.pdf, Page 6).
*   The training code utilized Flash Attention to accelerate and reduce the memory requirements of the attention mechanism (2403.18421.pdf, Page 6).

### Paper or other resource for more information:
*   **Academic Paper:** Bolton, E., et al. "BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text." arXiv preprint arXiv:2403.18421 (2024). (2403.18421.pdf).
*   **Hugging Face Hub:** The model is available at `https://huggingface.co/stanford-crfm/BioMedLM` (2403.18421.pdf, Page 1, Page 14).
*   **GitHub Repository:** The code for pre-training and fine-tuning is available at `https://github.com/stanford-crfm/BioMedLM` (2403.18421.pdf, Page 7, Page 14).

### Citation details:
Insufficient information. The provided paper does not include a BibTeX citation block.

### License:
Insufficient information.

### Contact:
For correspondence, the developers can be contacted at `elliotbolton@stanford.edu` and `manning@stanford.edu` (2403.18421.pdf, Page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed for biomedical Natural Language Processing (NLP) tasks, particularly question-answering. After fine-tuning, it can be used for:
*   **Multiple-Choice Question Answering:** Answering questions from medical exams and biomedical research literature, such as those found in MedMCQA, MedQA, and MMLU Medical Genetics (2403.18421.pdf, Page 2, Page 8).
*   **Yes/No Question Answering:** Answering questions based on biomedical abstracts, as in the PubMedQA and BioASQ tasks (2403.18421.pdf, Page 9, Page 10).
*   **Long-Form Question Answering:** Generating useful, multi-sentence answers to patient questions on medical topics after being fine-tuned on an appropriate instruction dataset (2403.18421.pdf, Page 2, Page 10).
*   **General Biomedical NLP:** The paper notes its use by other researchers since its release for tasks like named entity recognition, relation extraction, and text generation of medical systematic reviews (2403.18421.pdf, Page 13).

The model is intended to serve as a transparent, privacy-preserving, and economical foundation for these applications, especially in biomedicine (2403.18421.pdf, Page 1).

### Primary intended users:
The primary intended users are researchers and developers in the biomedical and healthcare fields. The model is specifically positioned for organizations with limited resources and strict privacy requirements that may find larger, closed models inaccessible or non-viable (2403.18421.pdf, Page 2).

### Out-of-scope uses:
*   **Direct Use Without Fine-Tuning:** The base pre-trained model is trained to replicate text from PubMed articles and is "not well suited for question response" without being fine-tuned on a specific task (2403.18421.pdf, Page 10).
*   **Unsupervised Clinical Advice:** The model can hallucinate, especially around numerical values (e.g., statistics about disease prevalence). Therefore, it should not be used as a standalone tool for providing answers directly to patients without "additional safeguards to correct incorrect numerical values" (2403.18421.pdf, Page 12).

---

## How to Use
This section outlines how to use the model.

The pre-trained model is available on the Hugging Face Hub at `https://huggingface.co/stanford-crfm/BioMedLM` (2403.18421.pdf, Page 14). The code for pre-training and fine-tuning is available on GitHub at `https://github.com/stanford-crfm/BioMedLM` (2403.18421.pdf, Page 14).

The model must be fine-tuned for downstream tasks. The paper describes two main fine-tuning architectures:

1.  **Multiple-Choice Classification:** For tasks like MedQA and MedMCQA, each question context is concatenated with each answer option. These combined sequences are run through the transformer, and the final hidden state is passed to a linear classifier to score each option. The option with the highest score is selected as the answer (2403.18421.pdf, Page 7).

2.  **Sequence Classification:** For yes/no tasks like PubMedQA and BioASQ, the context and question are concatenated. A special token is placed at the end of the sequence, and its corresponding hidden state is fed to a linear classifier to produce scores for the possible answers ("yes", "no", "maybe") (2403.18421.pdf, Page 7). An optimal input format for these tasks was found to be:
    `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]` (2403.18421.pdf, Page 8).

3.  **Long-Form Generation:** To generate paragraph-level answers, the model was fine-tuned on a dataset of question-answer pairs derived from web FAQ pages and Wikipedia articles (2403.18421.pdf, Page 10). Example outputs for consumer health questions are provided in the paper (2403.18421.pdf, Table 12, Page 11). For instance:
    *   **Input Question:** "What are good treatments for arthritis?"
    *   **Sample Output:** "There are many treatments for arthritis. Your healthcare provider will recommend the treatment that's right for you based on your symptoms and the type of arthritis you have. Treatments for arthritis include: Medications: Your healthcare provider may prescribe medications to reduce pain and inflammation. Common medications include: Nonsteroidal anti-inflammatory drugs (NSAIDs). Corticosteroids. Pain relievers. Physical therapy: Physical therapy can help you manage arthritis symptoms... Surgery: You may need surgery if your arthritis is severe or you don't respond to other treatments..." (2403.18421.pdf, Table 12, Page 11).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Domain of Text:** The model's performance is influenced by the domain of the text it is evaluated on. It was trained on formal biomedical text from PubMed, which leads to better performance on biology-related tasks compared to clinical tasks (2403.18421.pdf, Page 13).
*   **Domain Drift:** Performance can be lower on topics that drift from the training data's domain, such as the "domain drift between college level biology topics and formal PubMed articles," which likely contributed to weaker performance on the MMLU College Biology exam (2403.18421.pdf, Page 12).
*   **Tokenizer:** Using a domain-specific tokenizer trained on biomedical text was shown to provide a meaningful improvement in downstream task performance compared to a general-purpose tokenizer (2403.18421.pdf, Table 4, Page 5).

### Evaluation factors:
The model was evaluated based on its performance on a variety of standard biomedical question-answering benchmarks. The factors analyzed were the specific tasks and their respective domains, including:
*   **Medical Exams:** MedMCQA, MedQA, MMLU (Clinical Knowledge, Professional Medicine, Medical Genetics, College Biology) (2403.18421.pdf, Pages 8-9).
*   **Biomedical Literature QA:** PubMedQA, BioASQ (2403.18421.pdf, Pages 9-10).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Accuracy:** The primary metric used for evaluating performance on all question-answering tasks (MedMCQA, MedQA, MMLU, PubMedQA, BioASQ) is accuracy (2403.18421.pdf, Tables 7, 8, 9, 10, 11, Pages 8-10).
*   **Cross-Entropy Loss:** This metric was used during pre-training to monitor the model's learning progress on both the training and validation sets (2403.18421.pdf, Figure 1, Page 7).
*   **Precision and F1-Score:** While not used in the primary evaluation, the paper notes that other researchers have evaluated BioMedLM using precision and micro F1-score on tasks like relation extraction and named entity recognition (2403.18421.pdf, Page 13).

### Decision thresholds:
For multiple-choice and sequence classification tasks, the decision is made by selecting the class with the highest score produced by a linear classifier head attached to the model during fine-tuning. No specific numerical threshold is used; the model selects the most probable answer (2403.18421.pdf, Page 7).

### Variation approaches:
To ensure the robustness of some design choices, experiments were run multiple times with different initializations. For example, the impact of the custom tokenizer was tested on the MedQA task over 5 random seeds (2403.18421.pdf, Page 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several publicly available biomedical question-answering datasets:
*   **MedMCQA:** Contains 182,822/4,183/6,150 train/dev/test questions from Indian medical school entrance exams (AIIMS PG and NEET PG) (2403.18421.pdf, Page 8).
*   **MedQA:** Contains 10,178/1,272/1,273 train/dev/test questions from USMLE questions found on the web (2403.18421.pdf, Page 8).
*   **MMLU (Massive Multitask Language Understanding):** The model was evaluated on several biomedical-related exams from this collection, including Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (2403.18421.pdf, Page 9).
*   **PubMedQA:** Contains 450/50/500 train/dev/test questions constructed from PubMed article abstracts, with yes/no/maybe answers (2403.18421.pdf, Page 9).
*   **BioASQ:** Contains 670/75/140 train/dev/test questions from biomedical passages, with yes/no answers (2403.18421.pdf, Page 10).
*   **Consumer Health Questions:** For long-form generation, the model was fine-tuned and evaluated on a collection of over 53,000 medical question/answer pairs directed towards patients, collected from public web sources (2403.18421.pdf, Page 8).

### Motivation:
These datasets were chosen because they are "standard biomedical NLP QA tasks" that allow for comparison with other state-of-the-art models (2403.18421.pdf, Page 8). They cover a wide variety of topics, from clinical questions to fundamental biochemistry, and represent different question formats (multiple-choice, yes/no, long-form) (2403.18421.pdf, Page 8).

### Preprocessing:
The preprocessing steps involved formatting the questions and answers for the model's fine-tuning architecture:
*   For multiple-choice tasks (MedQA, MedMCQA, MMLU), the question context was concatenated with each answer option to create separate input sequences for the model (2403.18421.pdf, Page 7).
*   For yes/no tasks (PubMedQA, BioASQ), the context and question were concatenated using special tokens to delineate the different parts of the input, in the format: `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]` (2403.18421.pdf, Pages 7-8).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained exclusively on the biomedical subset of The Pile dataset (as of November 2022), which consists of PubMed abstracts and full articles (2403.18421.pdf, Page 1, Page 5). The training corpus contained 34.6 billion tokens (2403.18421.pdf, Page 5).

### Motivation:
The goal was to build a smaller, domain-specific model focused on biomedical text to investigate the value of domain specialization and to provide a transparent, privacy-preserving, and economical alternative to very large, closed-source language models (2403.18421.pdf, Page 1, Page 2).

### Preprocessing:
The primary preprocessing step was tokenization. A custom Byte-Pair Encoding (BPE) tokenizer was trained on PubMed abstracts (2403.18421.pdf, Page 5). This tokenizer was designed to represent common biomedical terms (e.g., "thrombin", "cytotoxicity") as single tokens, which was shown to improve downstream task performance compared to a general GPT-2 tokenizer that would split them into sub-words (2403.18421.pdf, Table 3, Page 5). The tokenizer settings included a vocabulary size of 28,896 and a minimum token frequency of 2 (2403.18421.pdf, Table 2, Page 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was evaluated on several individual tasks, with results reported as test accuracy.

**Multiple-Choice QA:**
*   **MedMCQA:** 57.3% accuracy (fine-tuned) (2403.18421.pdf, Table 7, Page 8).
*   **MedQA:** 54.7% accuracy (fine-tuned on MedMCQA data + classifier) (2403.18421.pdf, Table 8, Page 9).
*   **MMLU - Clinical Knowledge:** 59.6% accuracy (fine-tuned) (2403.18421.pdf, Table 9, Page 9).
*   **MMLU - Professional Medicine:** 63.1% accuracy (fine-tuned) (2403.18421.pdf, Table 9, Page 9).
*   **MMLU - College Biology:** 60.7% accuracy (fine-tuned) (2403.18421.pdf, Table 9, Page 9).
*   **MMLU - Medical Genetics:** 69.0% accuracy (fine-tuned) (2403.18421.pdf, Table 9, Page 9).

**Yes/No QA:**
*   **PubMedQA:** 74.4% accuracy (fine-tuned) (2403.18421.pdf, Table 10, Page 9).
*   **BioASQ:** 95.7% accuracy (fine-tuned) (2403.18421.pdf, Table 11, Page 10).

**Comparison to Baseline:**
*   On MedQA, BioMedLM (50.3%) substantially outperforms the architecturally similar GPT-Neo 2.7B (37.7%) (2403.18421.pdf, Figure 2, Page 12; Table 8, Page 9).
*   On PubMedQA, BioMedLM (74.4%) outperforms GPT-Neo 2.7B (66.1%) (2403.18421.pdf, Figure 2, Page 12; Table 10, Page 9).
*   On BioASQ, BioMedLM (95.7%) outperforms GPT-Neo 2.7B (67.1%) (2403.18421.pdf, Figure 2, Page 12; Table 11, Page 10).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper states that inference can be run on a laptop, but does not provide specific RAM/VRAM requirements (2403.18421.pdf, Page 2).

### Deploying Requirements:
The paper states that inference can be run on a laptop, but does not provide specific RAM/VRAM requirements (2403.18421.pdf, Page 2).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full model was pre-trained on 128 40GB Nvidia A100 GPUs (2403.18421.pdf, Page 6).
*   **Fine-tuning:** The model can be "comfortably fine-tuned on a single A100 GPU" (2403.18421.pdf, Page 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Transparency:** The model was trained exclusively on publicly available PubMed abstracts and full articles. The training data is fully documented, allowing practitioners and researchers to have insight into the model's knowledge base, which contrasts with closed models trained on unknown data sources (2403.18421.pdf, Page 1, Page 2).
*   **Privacy:** BioMedLM is designed to be small enough to be run locally ("on-device inference" on a laptop or on an organization's internal servers). This makes it a "privacy-preserving" alternative to large, API-based models that require users to send potentially sensitive data (such as patient information) over the internet, which can conflict with regulations like HIPAA (2403.18421.pdf, Page 1, Page 2).
*   **Risk of Hallucination:** The model is known to hallucinate, particularly with numerical values. For example, in a generated answer, it incorrectly stated that 10% of people in the US have Vitamin D deficiency, when the actual figure is much higher. This poses a risk if the model is used to provide information directly to patients without human oversight or fact-checking safeguards (2403.18421.pdf, Page 12).
*   **Accessibility and Cost:** The model is presented as an "economical and environmentally friendly" foundation for NLP applications. By being smaller and open-source, it aims to make language model technology more accessible to organizations with limited resources (2403.18421.pdf, Page 1, Page 2).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Requires Fine-Tuning:** The base pre-trained model is not suitable for direct use in question-answering tasks. It must be fine-tuned on a task-specific dataset to achieve good performance (2403.18421.pdf, Page 10).
*   **Numerical Hallucinations:** The model has a tendency to generate incorrect numerical values. This is a significant limitation for any application that requires factual accuracy, especially in a medical context (2403.18421.pdf, Page 12).
*   **Domain Sensitivity:** The model's performance is best on topics closely related to its training data (formal biomedical literature). It performs worse on related but distinct domains, such as college-level biology, indicating limitations in its ability to generalize (2403.18421.pdf, Page 12).
*   **Performance Gaps:** While competitive, the model does not match the performance of the largest state-of-the-art models (like GPT-4 or Med-PaLM 2) on several benchmarks, particularly MedQA (2403.18421.pdf, Table 8, Page 9).

### Recommendations:
*   **Always Fine-Tune:** Users should always fine-tune the model on their specific task before deployment (2403.18421.pdf, Page 10).
*   **Implement Safeguards:** For any application that provides information to users (especially patients), "additional safeguards to correct incorrect numerical values" are necessary to mitigate the risk of hallucination (2403.18421.pdf, Page 12).
*   **Use Optimal Input Formatting:** For yes/no question-answering tasks like PubMedQA, performance can be significantly improved by using special tokens and a structured input format as described in the "How to Use" section (2403.18421.pdf, Pages 7-8).
*   **Further Research:** The paper suggests that a 2-phase fine-tuning approach, similar to that used by BioGPT, could be a "promising future direction" to improve performance on tasks with small training sets like PubMedQA (2403.18421.pdf, Page 12).