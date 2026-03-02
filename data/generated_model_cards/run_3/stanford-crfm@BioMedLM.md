## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from Stanford University and DataBricks (BioMedLM_paper.pdf, p. 1). The authors are Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (BioMedLM_paper.pdf, p. 1).

### Model date:
The model was made publicly available in December 2022 (BioMedLM_paper.pdf, p. 2). The academic paper describing the model was released in March 2024 (BioMedLM_paper.pdf, p. 1). The total pre-training run was completed in 6.25 days (BioMedLM_paper.pdf, p. 6).

### Model version:
The model is a 2.7 billion parameter GPT-style model (BioMedLM_paper.pdf, p. 1). It is architecturally similar to the general-English model GPT-Neo 2.7B but is trained exclusively on biomedical text and uses a domain-specific tokenizer, which leads to substantial performance improvements on biomedical tasks (BioMedLM_paper.pdf, p. 2, 12). During development, smaller experimental versions, such as a 125 million parameter model, were used to test design choices like the tokenizer's impact on performance (BioMedLM_paper.pdf, p. 5).

### Model type:
BioMedLM is an autoregressive, decoder-only Transformer language model with a GPT-2 style architecture (BioMedLM_paper.pdf, p. 4).

**Key Architectural Details:**
*   **Parameters:** 2.7 billion (BioMedLM_paper.pdf, p. 1)
*   **Model Type:** `gpt2` (config.json)
*   **Architecture:** `GPT2LMHeadModel` (config.json)
*   **Layers:** 32 (config.json; BioMedLM_paper.pdf, p. 4, Table 1)
*   **Heads:** 20 (config.json; BioMedLM_paper.pdf, p. 4, Table 1)
*   **Hidden Size (Embedding Dimension):** 2560 (config.json; BioMedLM_paper.pdf, p. 4, Table 1)
*   **Vocabulary Size:** 28,896 (config.json; BioMedLM_paper.pdf, p. 4, Table 1)
*   **Context Length (Sequence Length):** 1024 (config.json; BioMedLM_paper.pdf, p. 4, Table 1)
*   **Activation Function:** `gelu_new` (config.json)
*   **Positional Embeddings:** Learned absolute positional embeddings (BioMedLM_paper.pdf, p. 4)

### Training details:
The model was pre-trained on the language modeling task of predicting the next token, using a standard cross-entropy loss minimization objective (BioMedLM_paper.pdf, p. 6).

**Key Training Parameters:**
*   **Optimizer:** Decoupled AdamW (BioMedLM_paper.pdf, p. 6)
*   **Learning Rate:** 1.6e-4 (BioMedLM_paper.pdf, p. 6, Table 5)
*   **Learning Rate Scheduler:** Cosine decay with a linear warmup of 100 batches (BioMedLM_paper.pdf, p. 6, Table 5)
*   **Batch Size:** 1024 sequences (BioMedLM_paper.pdf, p. 6)
*   **Sequence Length:** 1024 tokens (BioMedLM_paper.pdf, p. 6)
*   **Total Tokens Trained On:** 300 billion (BioMedLM_paper.pdf, p. 6)
*   **Weight Decay:** 1.6e-5 (BioMedLM_paper.pdf, p. 6, Table 5)
*   **Adam Betas:** [0.9, 0.95] (BioMedLM_paper.pdf, p. 6, Table 5)
*   **Adam Epsilon:** 1e-8 (BioMedLM_paper.pdf, p. 6, Table 5)

**Training Environment and Methodology:**
*   **Hardware:** Trained on the MosaicML Cloud platform using 128 40GB Nvidia A100 GPUs (BioMedLM_paper.pdf, p. 6).
*   **Precision:** Mixed precision training was used. Computation was done in `bf16`, while parameters and optimizer states were stored in `fp32` (BioMedLM_paper.pdf, p. 6, Table 6).
*   **Frameworks:** The training code utilized Hugging Face's GPT-2 implementation, the Composer training library, and PyTorch FSDP. Flash Attention was used to accelerate training and reduce memory requirements (BioMedLM_paper.pdf, p. 6).

### Paper or other resource for more information:
*   **Academic Paper:** Bolton, E., Venigalla, A., Yasunaga, M., et al. (2024). "BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text." This paper details the model's architecture, training process, and evaluation results (BioMedLM_paper.pdf).
*   **Hugging Face Hub:** The pre-trained model is available for download at https://huggingface.co/stanford-crfm/BioMedLM (BioMedLM_paper.pdf, p. 1, 14).
*   **GitHub Repository:** The code for pre-training and fine-tuning is available at https://github.com/stanford-crfm/BioMedLM (BioMedLM_paper.pdf, p. 7, 14).

### Citation details:
Insufficient information. (The paper does not provide a BibTeX entry).

### License:
Insufficient information. (The paper describes the model as "publicly available" but does not specify a license).

### Contact:
For correspondence, contact Elliot Bolton at elliotbolton@stanford.edu or Christopher D. Manning at manning@stanford.edu (BioMedLM_paper.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BioMedLM is a foundational model designed for the biomedical domain. Its primary intended use is to be fine-tuned for specific downstream biomedical NLP tasks (BioMedLM_paper.pdf, p. 1).

**Specific capabilities and use cases include:**
*   **Biomedical Question Answering:** The model achieves strong performance on multiple-choice question-answering benchmarks like MedMCQA, MedQA, and MMLU Medical Genetics (BioMedLM_paper.pdf, p. 2).
*   **Long-Form Answer Generation:** After fine-tuning on question-answer pairs, the model can generate useful, multi-sentence answers to consumer health questions (e.g., "What are the best ways to treat plantar fasciitis?") (BioMedLM_paper.pdf, p. 2, 10).
*   **Information Retrieval and Summarization:** The model is intended for applications involving information retrieval and summarization from biomedical literature and clinical information like physician notes (BioMedLM_paper.pdf, p. 1).
*   **Relation Extraction:** The model has been shown to perform well on tasks like identifying protein-protein interactions and microbiome-disease interactions (BioMedLM_paper.pdf, p. 13).

**Input-Output Structure:**
*   **Base Model:** The pre-trained model takes a sequence of text as input and outputs the likelihood of the next token in the sequence (BioMedLM_paper.pdf, p. 1).
*   **Fine-tuned for Classification/MCQA:** The model takes a formatted prompt containing context and a question (and answer choices, if applicable) as input and outputs a classification (e.g., "yes/no/maybe") or a selection from the choices (BioMedLM_paper.pdf, p. 7).
*   **Fine-tuned for Generation:** The model takes a question as input and generates a free-text, paragraph-level answer (BioMedLM_paper.pdf, p. 10).

### Primary intended users:
The primary intended users are researchers, developers, and organizations in the biomedical and healthcare fields. The model is particularly aimed at those with limited computational resources or strict privacy requirements that prevent the use of large, proprietary, API-based models (BioMedLM_paper.pdf, p. 2).

### Out-of-scope uses:
*   **Direct Clinical Use without Safeguards:** The model can hallucinate, especially with numerical values. It should not be used for direct patient advice or in clinical decision-making without additional safeguards and human oversight (BioMedLM_paper.pdf, p. 12).
*   **General-Purpose Chatbot:** The model is trained exclusively on biomedical text and is not intended for general-purpose conversation or tasks outside of the biomedical domain (BioMedLM_paper.pdf, p. 1).
*   **Use without Fine-Tuning:** The base pre-trained model is trained to replicate text from PubMed articles and is not well-suited for question-answering or other instruction-following tasks without being fine-tuned (BioMedLM_paper.pdf, p. 10).

---

## How to Use
This section outlines how to use the model.

The pre-trained model is available on the Hugging Face Hub, and the code for fine-tuning is available on GitHub (BioMedLM_paper.pdf, p. 14). The model must be fine-tuned for specific downstream tasks.

**Fine-tuning for Multiple-Choice Question Answering (e.g., MedQA, MedMCQA):**
A specialized architecture is recommended for these tasks. For each question, the input context is concatenated with each of the possible answer options. Each of these combined sequences is passed through the model. The final hidden state at the end of each sequence is then fed into a linear classifier to generate a score for that specific ending. The answer with the highest score is selected (BioMedLM_paper.pdf, p. 7).

**Fine-tuning for Yes/No/Maybe Question Answering (e.g., PubMedQA, BioASQ):**
This task is treated as a sequence classification problem. The context and question are concatenated into a single input sequence. The paper found that performance improves significantly when using special tokens to structure the input in the following format (BioMedLM_paper.pdf, p. 7):
`[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]`
The hidden state corresponding to a special token at the end of this sequence is then passed to a linear classifier to produce scores for "yes", "no", or "maybe" (BioMedLM_paper.pdf, p. 7).

**Fine-tuning for Long-Form Answer Generation:**
To enable the model to generate paragraph-level answers to medical questions, it should be fine-tuned on a dataset of question-answer pairs. The paper describes creating such a dataset from FAQ pages and Wikipedia articles (BioMedLM_paper.pdf, p. 10). An example question is "What are the best ways to treat plantar fasciitis?", with the model generating a detailed, multi-sentence response (BioMedLM_paper.pdf, p. 8, 11).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary relevant factor identified is the specific sub-domain within biomedicine. The model's training on formal PubMed articles leads to different performance characteristics on different types of tasks. For example, there is a "domain drift between college level biology topics and formal PubMed articles," which affects performance on biology-related questions (BioMedLM_paper.pdf, p. 13). The model's specialized training also leads to better performance on biology-related tasks compared to more general clinical tasks (BioMedLM_paper.pdf, p. 13).

### Evaluation factors:
The model was evaluated across different biomedical subject areas. For the MMLU benchmark, performance was disaggregated and reported for the following subjects: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (BioMedLM_paper.pdf, p. 9, Table 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess the model's effectiveness on all question-answering tasks (MedMCQA, MedQA, MMLU, PubMedQA, BioASQ) is **accuracy** (BioMedLM_paper.pdf, p. 8, 9, 10). In post-release evaluations by other researchers cited in the paper, **F1-score** was used for named entity recognition tasks, and **precision** and **accuracy** were used for relation extraction tasks (BioMedLM_paper.pdf, p. 13).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To test the impact of the custom tokenizer, experiments on a smaller 125-million-parameter version of the model were run over 5 random seeds to ensure the observed improvement was meaningful (BioMedLM_paper.pdf, p. 5). For the final 2.7B model, the number of runs or variation measures are not specified.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several standard biomedical question-answering benchmarks:
*   **MedMCQA:** Contains questions from Indian medical school entrance exams (AIIMS PG and NEET PG). The dataset split used was 182,822 for training, 4,183 for development, and 6,150 for testing (BioMedLM_paper.pdf, p. 8).
*   **MedQA:** Contains questions from US Medical Licensing Exam (USMLE). The dataset split used was 10,178 for training, 1,272 for development, and 1,273 for testing (BioMedLM_paper.pdf, p. 8).
*   **MMLU (Massive Multitask Language Understanding):** A broad collection of subject tests. The model was evaluated on a selection of biomedical topics: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (BioMedLM_paper.pdf, p. 9).
*   **PubMedQA:** A yes/no/maybe question-answering dataset where questions are derived from the titles of PubMed abstracts. The dataset split is 450 for training, 50 for development, and 500 for testing (BioMedLM_paper.pdf, p. 9).
*   **BioASQ:** A yes/no question-answering dataset constructed from biomedical passages. The dataset split is 670 for training, 75 for development, and 140 for testing (BioMedLM_paper.pdf, p. 10).
*   **Consumer Health Questions:** For evaluating long-form generation, a dataset of over 53,000 question-answer pairs was collected from publicly available sources on the web (BioMedLM_paper.pdf, p. 8).

### Motivation:
These datasets were chosen because they are standard benchmarks for biomedical NLP, allowing for direct comparison with other state-of-the-art models, including much larger ones like GPT-4 and Flan-PaLM (BioMedLM_paper.pdf, p. 8).

### Preprocessing:
The evaluation data was formatted into specific prompt structures depending on the task.
*   For multiple-choice tasks (MedQA, MedMCQA, MMLU), the question context was concatenated with each answer choice individually to create multiple input sequences per question (BioMedLM_paper.pdf, p. 7).
*   For yes/no tasks (PubMedQA, BioASQ), the context and question were concatenated using special tokens to clearly delineate the different parts of the input for the model (BioMedLM_paper.pdf, p. 7).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained exclusively on the PubMed abstracts and full articles subset of **The Pile** dataset (as of November 2022) (BioMedLM_paper.pdf, p. 1, 5). The training corpus consisted of 34.6 billion tokens (BioMedLM_paper.pdf, p. 5). The training run performed 8.67 passes over this data (BioMedLM_paper.pdf, p. 5).

### Motivation:
The choice of training data was motivated by the goal of investigating the value of domain specialization. By training a medium-sized model exclusively on a high-quality, domain-specific corpus (biomedical text), the developers aimed to achieve strong performance on biomedical tasks without the massive scale and general-purpose data of larger models (BioMedLM_paper.pdf, p. 2).

### Preprocessing:
The training data was processed using a custom **Byte-Pair Encoding (BPE) tokenizer** that was specifically trained on PubMed abstracts (BioMedLM_paper.pdf, p. 5). This tokenizer was designed to represent common biomedical terms (e.g., "thrombin", "cytotoxicity") as single tokens, which improves the model's handling of domain-specific terminology compared to a general-purpose tokenizer (BioMedLM_paper.pdf, p. 5, Table 3). The tokenizer has a vocabulary size of 28,896 and was trained using the Hugging Face Tokenizers library (BioMedLM_paper.pdf, p. 5, Table 2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance was measured by accuracy on several standard biomedical QA benchmarks:
*   **MedMCQA (test):** 57.3% (BioMedLM_paper.pdf, p. 8, Table 7)
*   **MedQA (test):** 54.7% (when fine-tuned on MedMCQA data first) (BioMedLM_paper.pdf, p. 9, Table 8)
*   **PubMedQA (test):** 74.4% (BioMedLM_paper.pdf, p. 9, Table 10)
*   **BioASQ (test):** 95.7% (BioMedLM_paper.pdf, p. 10, Table 11)

### Intersectional results:
Performance on the MMLU benchmark was reported across four different biomedical subjects:
*   **Clinical Knowledge:** 59.6%
*   **Professional Medicine:** 63.1%
*   **College Biology:** 60.7%
*   **Medical Genetics:** 69.0%
(Source: BioMedLM_paper.pdf, p. 9, Table 9)

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper states that inference can be "run on a laptop," but does not specify the exact RAM or VRAM requirements (BioMedLM_paper.pdf, p. 2).

### Deploying Requirements:
The paper states that organizations can serve the model internally, which is possible due to its relatively small size, but does not provide specific hardware requirements for deployment (BioMedLM_paper.pdf, p. 2).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training run required a cluster of **128 40GB Nvidia A100 GPUs** and was completed in 6.25 days (BioMedLM_paper.pdf, p. 6).
*   **Fine-tuning:** The model can be "comfortably fine-tuned on a **single A100 GPU**" (BioMedLM_paper.pdf, p. 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development of BioMedLM was motivated by a desire to address some of the ethical and practical challenges posed by very large, closed-source language models (BioMedLM_paper.pdf, p. 2).

*   **Data Transparency:** The model was trained exclusively on a fully documented, publicly available dataset (PubMed abstracts and articles), in contrast to proprietary models trained on unknown data sources. This transparency allows users and researchers to better understand the model's knowledge base and potential biases (BioMedLM_paper.pdf, p. 2). No sensitive or personal data was used for pre-training.
*   **Privacy:** Because of its smaller size, BioMedLM can be run locally or on-premise, allowing organizations to use it without sending sensitive patient data over the internet to a third-party API. This is described as a "privacy-preserving" approach that aligns with the needs of healthcare and the requirements of regulations like HIPAA (BioMedLM_paper.pdf, p. 1, 2).
*   **Accessibility and Cost:** The model is presented as an "economical and environmentally friendly" alternative to massive-scale models. Its smaller size reduces the computational cost of training and inference, making it more accessible to organizations with limited resources (BioMedLM_paper.pdf, p. 1, 2).
*   **Risks in Model Usage:** A known risk is **hallucination**, particularly around numerical values. The paper provides an example where the model incorrectly states a statistic about Vitamin D deficiency. It is noted that any application built on this model for providing answers to patients would require "additional safeguards to correct incorrect numerical values" (BioMedLM_paper.pdf, p. 12). Use cases involving direct medical advice without human oversight are especially fraught with risk.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Requires Fine-Tuning:** The base, pre-trained BioMedLM model is not suitable for direct use in question-answering tasks. It has been trained to replicate the style of PubMed text and must be fine-tuned on a specific instruction dataset to perform well on downstream tasks (BioMedLM_paper.pdf, p. 10).
*   **Numerical Hallucination:** The model is prone to generating incorrect numerical values. For example, it incorrectly stated that 1 in 10 people in the US have Vitamin D deficiency, when the actual figure is closer to 35% (BioMedLM_paper.pdf, p. 12).
*   **Domain Drift:** The model's performance can be affected by shifts in the specific sub-domain of the text. It performs worse on college-level biology questions compared to topics more aligned with its formal PubMed training data (BioMedLM_paper.pdf, p. 13).
*   **Performance on Limited Data:** On tasks with very small fine-tuning datasets like PubMedQA, the model's performance, while strong, does not match that of other models that have used more complex fine-tuning strategies involving additional noisy or unlabeled data (BioMedLM_paper.pdf, p. 12).

### Recommendations:
*   **Always Fine-Tune:** Users should always fine-tune the model on data specific to their target task before deployment.
*   **Implement Safeguards:** For any application that provides information to patients or clinicians, it is crucial to implement additional safeguards, such as fact-checking mechanisms, especially for numerical data, to mitigate the risk of hallucination (BioMedLM_paper.pdf, p. 12).
*   **Consider Two-Phase Fine-Tuning:** For tasks with limited labeled data, users could explore a two-phase fine-tuning approach (first on a larger, related dataset, then on the target dataset) to potentially improve performance (BioMedLM_paper.pdf, p. 12).
*   **Use for Privacy-Sensitive Applications:** The model is well-suited for applications in healthcare and biomedical research where data privacy is a primary concern, as it can be hosted and run locally (BioMedLM_paper.pdf, p. 2).

---