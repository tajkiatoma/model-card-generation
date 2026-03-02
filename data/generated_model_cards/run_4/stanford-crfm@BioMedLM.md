## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Stanford University and DataBricks (academic_paper.pdf, Page 1). The listed authors are Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (academic_paper.pdf, Page 1).

### Model date:
The model was made publicly available in December 2022 (academic_paper.pdf, Page 2, Section 2). The associated academic paper was published in March 2024 (academic_paper.pdf, Page 1).

### Model version:
The repository does not specify a version number. The model is described as BioMedLM, a 2.7 billion parameter language model (academic_paper.pdf, Page 1, Abstract). It is architecturally similar to GPT-Neo 2.7B but is trained exclusively on biomedical text, which leads to substantial performance improvements on biomedical question-answering tasks compared to GPT-Neo 2.7B (academic_paper.pdf, Page 12, Section 6.3, Figure 2).

### Model type:
BioMedLM is a GPT-style, autoregressive, decoder-only Transformer model with 2.7 billion parameters (academic_paper.pdf, Page 1, Abstract; Page 4, Section 3.1). It is similar in architecture to GPT-2 (academic_paper.pdf, Page 4, Section 3.1).

**Architecture Details:**
*   **Model Type:** gpt2 (config.json)
*   **Architecture:** GPT2LMHeadModel (config.json)
*   **Number of Layers (`n_layer`):** 32 (config.json; academic_paper.pdf, Page 4, Table 1)
*   **Hidden Size (`n_embd`):** 2560 (config.json; academic_paper.pdf, Page 4, Table 1)
*   **Number of Attention Heads (`n_head`):** 20 (config.json; academic_paper.pdf, Page 4, Table 1)
*   **Vocabulary Size (`vocab_size`):** 28896 (config.json; academic_paper.pdf, Page 4, Table 1)
*   **Context Length / Sequence Length (`n_ctx`):** 1024 (config.json; academic_paper.pdf, Page 4, Table 1)
*   **Activation Function:** gelu_new (config.json)
*   **Positional Embeddings:** Learned absolute positional embeddings (academic_paper.pdf, Page 4, Section 3.1)
*   **Tokenizer:** A custom Byte-Pair Encoding (BPE) tokenizer trained on PubMed abstracts (academic_paper.pdf, Page 5, Section 3.2).

### Training details:
The model was pre-trained to minimize the standard cross-entropy loss of the subsequent token using the Decoupled AdamW optimizer (academic_paper.pdf, Page 6). The training process utilized Flash Attention to accelerate and reduce memory requirements (academic_paper.pdf, Page 6).

**Key Hyperparameters:**
*   **Tokens Per Batch:** 1,048,576 (academic_paper.pdf, Page 6, Table 5)
*   **Learning Rate:** 1.6e-4 (academic_paper.pdf, Page 6, Table 5)
*   **Scheduler:** Cosine with linear warmup for the first 100 batches (academic_paper.pdf, Page 6, Table 5)
*   **AdamW Epsilon:** 1e-8 (academic_paper.pdf, Page 6, Table 5)
*   **AdamW Betas:** [0.9, 0.95] (academic_paper.pdf, Page 6, Table 5)
*   **Weight Decay:** 1.6e-5 (academic_paper.pdf, Page 6, Table 5)
*   **Total Tokens Trained On:** 300 billion (academic_paper.pdf, Page 6)

**Mixed Precision Settings:**
*   **Compute Precision:** bf16 (academic_paper.pdf, Page 6, Table 6)
*   **Parameter Storage:** fp32 (academic_paper.pdf, Page 6, Table 6)
*   **Optimizer Storage:** fp32 (academic_paper.pdf, Page 6, Table 6)
*   **Gradient Communication:** fp32 (academic_paper.pdf, Page 6, Table 6)

The total training run was completed in 6.25 days on 128 40GB Nvidia A100 GPUs (academic_paper.pdf, Page 6).

### Paper or other resource for more information:
*   **Academic Paper:** "BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text" provides a comprehensive overview of the model's design, training, and evaluation (academic_paper.pdf).
*   **Hugging Face Hub:** The pre-trained model is available at `https://huggingface.co/stanford-crfm/BioMedLM` (academic_paper.pdf, Page 1, Abstract; Page 14, Section 10).
*   **GitHub Repository:** Code for pre-training and fine-tuning is available at `https://github.com/stanford-crfm/BioMedLM` (academic_paper.pdf, Page 7, Section 3.4; Page 14, Section 10).

### Citation details:
Insufficient information.

### License:
The paper describes the model as "publicly available" and released to the "open source community" (academic_paper.pdf, Page 2, Section 2; Page 3, Section 2). However, a specific license (e.g., Apache 2.0, MIT) is not mentioned in the provided materials.

### Contact:
For correspondence, the paper lists Elliot Bolton (`elliotbolton@stanford.edu`) and Christopher D. Manning (`manning@stanford.edu`) (academic_paper.pdf, Page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed for biomedical Natural Language Processing (NLP) applications (academic_paper.pdf, Page 1, Abstract). Its primary intended uses include:
*   **Biomedical Question-Answering:** The model shows strong performance on multiple-choice question-answering tasks like MedMCQA, MedQA, and MMLU Medical Genetics (academic_paper.pdf, Page 1, Abstract).
*   **Long-Form Answer Generation:** After fine-tuning, the model can produce useful, multi-sentence answers to patient questions on medical topics (academic_paper.pdf, Page 1, Abstract; Page 10, Section 5).
*   **Foundation for Specialized Applications:** It is intended to serve as a "transparent, privacy-preserving, economical and environmentally friendly" foundation model for applications in biomedicine, particularly for organizations with limited resources or strict privacy requirements (academic_paper.pdf, Page 1, Abstract; Page 2, Section 2).

The model is autoregressive, taking a sequence of text as input and generating subsequent text as output (academic_paper.pdf, Page 4, Section 3.1).

### Primary intended users:
The primary intended users are researchers, biomedical organizations, and healthcare organizations, especially those with limited computational resources and strict privacy needs that prevent the use of large, proprietary, API-based models (academic_paper.pdf, Page 2, Section 2).

### Out-of-scope uses:
The provided materials do not explicitly list out-of-scope uses. However, based on the model's design and reported limitations, certain uses are discouraged:
*   **General-Purpose Chatbot:** The model is trained exclusively on biomedical text and is not intended for general-domain conversation (academic_paper.pdf, Page 1, Abstract).
*   **Direct Medical Advice without Safeguards:** The model can hallucinate, especially around numerical values. Therefore, it should not be used as a standalone tool for providing medical advice to patients without "additional safeguards to correct incorrect numerical values" (academic_paper.pdf, Page 12, Section 6.2).
*   **Use without Fine-tuning:** The base model was trained to replicate text from PubMed articles and is "not well suited for question response" without being fine-tuned on an instruction dataset (academic_paper.pdf, Page 10, Section 5).

---

## How to Use
This section outlines how to use the model. 

The pre-trained model is available on the Hugging Face Hub at `https://huggingface.co/stanford-crfm/BioMedLM` (academic_paper.pdf, Page 14, Section 10). Code for pre-training and fine-tuning is available on GitHub at `https://github.com/stanford-crfm/BioMedLM` (academic_paper.pdf, Page 14, Section 10).

The model must be fine-tuned for specific downstream tasks. The paper describes two main fine-tuning architectures:
1.  **Multiple-Choice Question Answering (for MedQA, MedMCQA, MMLU):** For each question, the input context is concatenated with each answer option separately. Each full sequence is passed through the model, and the final hidden state is fed to a linear classifier. The option with the highest score is selected as the answer (academic_paper.pdf, Page 7, Section 3.4).
2.  **Sequence Classification (for PubMedQA, BioASQ):** The context and question are concatenated, and the hidden state of a special token at the end of the sequence is fed to a linear classifier to produce scores for "yes/no/maybe" or "yes/no" (academic_paper.pdf, Page 7, Section 3.4). The paper notes that for these tasks, performance improves when using special tokens to structure the input in the format: `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]` (academic_paper.pdf, Page 8).
3.  **Long-Form Generation:** The model can be fine-tuned on a collection of medical question/answer pairs to generate multi-sentence answers (academic_paper.pdf, Page 8, Section 4). An example question is "What are the best ways to treat plantar fasciitis?" (academic_paper.pdf, Page 8, Section 4). Example outputs for consumer health questions are provided in the paper (academic_paper.pdf, Page 11, Table 12).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary relevant factor identified is the **domain of the text**. The model's performance is heavily influenced by its domain-specific pre-training on biomedical text (PubMed) and its use of a domain-specific tokenizer. This specialization leads to substantial performance gains on biomedical tasks compared to an architecturally similar model (GPT-Neo 2.7B) trained on general English text (academic_paper.pdf, Page 12, Section 6.3). The paper also notes a potential "domain drift between college level biology topics and formal PubMed articles," which affects performance on certain tasks (academic_paper.pdf, Page 12, Section 6.1).

### Evaluation factors:
The model is evaluated across several factors corresponding to different sub-domains and task types within biomedicine. These include:
*   **Medical Board Exam Questions:** Performance on USMLE-style questions (MedQA dataset) and Indian medical entrance exams (MedMCQA dataset) (academic_paper.pdf, Page 8, Sections 4.1, 4.2).
*   **Academic Medical Subjects:** Performance is broken down by MMLU exam subjects, including Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (academic_paper.pdf, Page 9, Table 9).
*   **Biomedical Research Literature QA:** Performance on question answering over PubMed abstracts (PubMedQA and BioASQ datasets) (academic_paper.pdf, Pages 9-10, Sections 4.4, 4.5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess performance on all question-answering tasks is **Accuracy** (academic_paper.pdf, Tables 7, 8, 9, 10, 11).

In the "Usage of BioMedLM since release" section, the paper also mentions other metrics used in subsequent studies of the model:
*   **Micro F1-score** for named entity recognition tasks (academic_paper.pdf, Page 13, Section 7).
*   **Precision** for microbiome-disease interaction extraction (academic_paper.pdf, Page 13, Section 7).

### Decision thresholds:
For multiple-choice and sequence classification tasks, the model uses a linear classifier on top of the final hidden state to generate scores for each possible answer. The decision is made by selecting the answer with the highest score. The paper does not specify any absolute numerical thresholds for these decisions (academic_paper.pdf, Page 7, Section 3.4).

### Variation approaches:
To ensure robust measurements for the impact of the tokenizer, the paper mentions running multiple experiments "over 5 random seeds" on the MedQA task for the 125M parameter version of the model (academic_paper.pdf, Page 5, Section 3.2).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several standard biomedical question-answering datasets:
*   **MedMCQA:** Contains questions from Indian postgraduate medical entrance exams. The dataset split used is 182,822 train, 4,183 dev, and 6,150 test questions (academic_paper.pdf, Page 8, Section 4.1).
*   **MedQA:** Contains questions from USMLE (United States Medical Licensing Examination). The dataset split is 10,178 train, 1,272 dev, and 1,273 test questions (academic_paper.pdf, Page 8, Section 4.2).
*   **MMLU (Massive Multitask Language Understanding):** A collection of subject tests. The evaluation focused on biomedical-related exams: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (academic_paper.pdf, Page 9, Section 4.3).
*   **PubMedQA:** A question-answering dataset derived from PubMed abstracts. The split is 450 train, 50 dev, and 500 test questions (academic_paper.pdf, Page 9, Section 4.4).
*   **BioASQ:** A dataset of questions on biomedical passages, answerable with "yes/no". The split is 670 train, 75 dev, and 140 test questions (academic_paper.pdf, Page 10, Section 4.5).
*   **Consumer Health Questions:** For evaluating long-form answer generation, a dataset of over 53,000 question-answer pairs was collected from publicly available sources on the web (academic_paper.pdf, Page 8, Section 4).

### Motivation:
These datasets were chosen because they are "standard biomedical NLP QA tasks" that allow for benchmarking the model's capabilities against other prominent models in the biomedical QA space (academic_paper.pdf, Page 8, Section 4). They cover a wide variety of topics, from clinical scenarios to fundamental biochemistry (academic_paper.pdf, Page 8, Section 4.1).

### Preprocessing:
The evaluation data was formatted into specific prompts for fine-tuning:
*   For multiple-choice tasks (MedQA, MedMCQA, MMLU), the question context was concatenated with each answer option individually. Each of these combined sequences was processed by the model (academic_paper.pdf, Page 7, Section 3.4).
*   For yes/no tasks (PubMedQA, BioASQ), the context and question were concatenated using special tokens (`[Context Token]`, `[Question Token]`, `[Answer Token]`) to structure the input for the unidirectional model (academic_paper.pdf, Page 7-8, Section 3.4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained "exclusively on PubMed abstracts and full articles" (academic_paper.pdf, Page 1, Abstract). This data was sourced from The Pile dataset (as of November 2022). The total training corpus size was 34.6 billion tokens (academic_paper.pdf, Page 5, Section 3.3).

### Motivation:
The choice of training data was motivated by the goal of investigating the "value of domain specialization" (academic_paper.pdf, Page 2, Section 2). By training a medium-sized model exclusively on a high-quality, domain-specific corpus, the developers aimed to create a performant model for biomedical tasks that could serve as a transparent and privacy-preserving alternative to larger, general-domain models (academic_paper.pdf, Page 1, Abstract).

### Preprocessing:
The training data was processed with a custom Byte-Pair Encoding (BPE) tokenizer. This tokenizer was trained on PubMed abstracts to create a vocabulary tailored to biomedical terminology, which improves downstream task performance (academic_paper.pdf, Page 5, Section 3.2). The tokenizer has a vocabulary size of 28,896 and was trained with a minimum token frequency of 2 (academic_paper.pdf, Page 5, Table 2; config.json).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results disaggregated by task and dataset. For the MMLU benchmark, results are further broken down by specific medical and biological subjects.

*   **MedMCQA Test Accuracy:** 57.3% (academic_paper.pdf, Page 8, Table 7)
*   **MedQA Test Accuracy:** 50.3% (classifier), 54.7% (when fine-tuned with MedMCQA data) (academic_paper.pdf, Page 9, Table 8)
*   **PubMedQA Test Accuracy:** 74.4% (academic_paper.pdf, Page 9, Table 10)
*   **BioASQ Test Accuracy:** 95.7% (academic_paper.pdf, Page 10, Table 11)
*   **MMLU Accuracy by Subject:**
    *   Clinical Knowledge: 59.6%
    *   Professional Medicine: 63.1%
    *   College Biology: 60.7%
    *   Medical Genetics: 69.0%
    (Source: academic_paper.pdf, Page 9, Table 9)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper states that inference can be "run on a laptop," but does not specify the exact RAM or VRAM requirements (academic_paper.pdf, Page 2, Section 2).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training run was conducted on "128 40GB Nvidia A100 GPUs" and took 6.25 days (academic_paper.pdf, Page 6).
*   **Fine-tuning:** The model is designed to be "comfortably fine-tuned on a single A100 GPU" (academic_paper.pdf, Page 2, Section 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The development of BioMedLM was motivated by a desire to address some of the ethical and practical challenges posed by very large, closed-source language models (academic_paper.pdf, Page 2, Section 2).

*   **Privacy:** The model is designed to be "privacy-preserving." Because of its smaller size, organizations can host and run it internally, eliminating the need to send potentially sensitive patient data over the internet to a third-party API. This helps align with privacy requirements like HIPAA (academic_paper.pdf, Page 1, Abstract; Page 2, Section 2).
*   **Transparency:** The model is presented as a "transparent" alternative to proprietary models. Its training data (PubMed) is fully documented, allowing researchers and practitioners to better understand the model's knowledge base and potential biases (academic_paper.pdf, Page 1, Abstract; Page 2, Section 2). The model architecture and training process are also detailed in the paper.
*   **Risk of Hallucination:** The developers identify that the model is prone to hallucination, "especially around numerical values." For example, a generated answer stated that 10% of people in the US have Vitamin D deficiency, when the actual figure is closer to 35%. This poses a risk if the model is used for patient-facing applications (academic_paper.pdf, Page 12, Section 6.2).
*   **Risk Mitigation:** To mitigate the risk of providing incorrect information, the developers recommend that any complete application built on this model "would need additional safeguards to correct incorrect numerical values" (academic_paper.pdf, Page 12, Section 6.2). The model is not intended to be used for direct medical advice without such safeguards and human oversight.
*   **Accessibility:** By creating a smaller, open-source model, the developers aim to make powerful language model technology more accessible to organizations with limited computational resources (academic_paper.pdf, Page 2, Section 2).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Numerical Inaccuracy:** The model has a known issue with hallucinating numerical values. Fact-checking of generated numbers is essential, as shown by an incorrect statistic about Vitamin D deficiency (academic_paper.pdf, Page 12, Section 6.2).
*   **Requires Fine-tuning for QA:** The base pre-trained model is not suitable for question-answering tasks out-of-the-box. It was trained to replicate PubMed text and must be fine-tuned on an instruction dataset to enable question-response capabilities (academic_paper.pdf, Page 10, Section 5).
*   **Domain Specificity:** The model's specialization is also a limitation. It performs worse on topics that have a "domain drift" from formal PubMed articles, such as college-level biology questions (academic_paper.pdf, Page 12, Section 6.1). It is not designed for general-purpose conversation.
*   **Performance on Small Training Sets:** For tasks with very small fine-tuning datasets like PubMedQA, the model's performance is further from the state-of-the-art, suggesting it may be less sample-efficient than models that undergo more complex fine-tuning stages (academic_paper.pdf, Page 12, Section 6.1).

### Recommendations:
*   **Use Safeguards for Applications:** For any application that provides answers to patients or clinicians, users should implement "additional safeguards to correct incorrect numerical values" and other potential hallucinations (academic_paper.pdf, Page 12, Section 6.2).
*   **Fine-tune on Instruction Data:** To use the model for question-answering, users must fine-tune it on a relevant dataset of questions and answers (academic_paper.pdf, Page 10, Section 5).
*   **Use Optimal Prompt Formats:** For yes/no tasks like PubMedQA and BioASQ, users should structure the input with special tokens (`[Context Token]`, `[Question Token]`) to achieve better performance (academic_paper.pdf, Page 7-8, Section 3.4).
*   **Further Research:** The paper suggests that a 2-phase fine-tuning approach, similar to that used by BioGPT, could be a "promising future direction" to improve performance on tasks like PubMedQA (academic_paper.pdf, Page 12, Section 6.1).