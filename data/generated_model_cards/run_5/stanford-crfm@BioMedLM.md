## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Stanford University and DataBricks (BioMedLM.pdf, page 1). The authors are Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (BioMedLM.pdf, page 1).

### Model date:
The model was made publicly available in December 2022 (BioMedLM.pdf, page 2). The academic paper describing the model is dated March 2024 (BioMedLM.pdf, page 1).

### Model version:
The repository does not specify a version number. The model is described as BioMedLM, a 2.7 billion parameter GPT-style autoregressive model (BioMedLM.pdf, page 1). It is architecturally similar to GPT-Neo 2.7B but was trained exclusively on biomedical text, which results in substantially better performance on biomedical question-answering tasks (BioMedLM.pdf, page 12).

### Model type:
BioMedLM is an autoregressive, decoder-only Transformer language model with a GPT-2 style architecture (BioMedLM.pdf, page 4; config.json).

**Architecture Details:**
*   **Model Type:** gpt2 (config.json)
*   **Architecture:** GPT2LMHeadModel (config.json)
*   **Parameters:** 2.7 billion (BioMedLM.pdf, page 1)
*   **Layers:** 32 (config.json; BioMedLM.pdf, Table 1, page 4)
*   **Heads:** 20 (config.json; BioMedLM.pdf, Table 1, page 4)
*   **Hidden Size (Embedding Dimension):** 2560 (config.json; BioMedLM.pdf, Table 1, page 4)
*   **Vocabulary Size:** 28896 (config.json; BioMedLM.pdf, Table 1, page 4)
*   **Context Length (Sequence Length):** 1024 (config.json; BioMedLM.pdf, Table 1, page 4)
*   **Activation Function:** gelu_new (config.json)
*   **Positional Embeddings:** Learned absolute positional embeddings (BioMedLM.pdf, page 4)

The model uses a custom Byte-Pair Encoding (BPE) tokenizer trained specifically on biomedical text from PubMed abstracts (BioMedLM.pdf, page 5).

### Training details:
The model was trained to minimize the standard cross-entropy loss of the subsequent token (BioMedLM.pdf, page 6).

**Algorithm:**
*   **Optimizer:** Decoupled AdamW (Loshchilov and Hutter, 2019) (BioMedLM.pdf, page 6).
*   **Precision:** Mixed precision training was used. Computation was done in `bf16`, while parameters and optimizer states were stored in `fp32` (BioMedLM.pdf, page 6, Table 6).

**Key Parameters and Hyperparameters:**
*   **Total Training Tokens:** 300 billion (BioMedLM.pdf, page 6).
*   **Tokens per Batch:** 1,048,576 (BioMedLM.pdf, Table 5, page 6).
*   **Sequence Length:** 1024 (BioMedLM.pdf, page 6).
*   **Learning Rate:** 1.6e-4 (BioMedLM.pdf, Table 5, page 6).
*   **Scheduler:** Cosine with a linear warmup of 100 batches (BioMedLM.pdf, Table 5, page 6).
*   **AdamW Betas:** [0.9, 0.95] (BioMedLM.pdf, Table 5, page 6).
*   **AdamW Epsilon:** 1e-8 (BioMedLM.pdf, Table 5, page 6).
*   **Weight Decay:** 1.6e-5 (BioMedLM.pdf, Table 5, page 6).

The training utilized Flash Attention (Dao et al., 2022) to accelerate and reduce memory requirements (BioMedLM.pdf, page 6).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Title:** BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text
*   **Authors:** Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, et al.
*   **Date:** March 2024
*   **Summary:** The paper details the model's construction, training, and evaluation on various biomedical question-answering tasks. It demonstrates that smaller, domain-specific models can achieve results competitive with much larger models (BioMedLM.pdf, page 1).

**Other Resources:**
*   **Hugging Face Hub:** `https://huggingface.co/stanford-crfm/BioMedLM` (BioMedLM.pdf, page 1, 14)
*   **GitHub Repository:** `https://github.com/stanford-crfm/BioMedLM` (BioMedLM.pdf, page 7, 14)

### Citation details:
The paper does not provide a BibTeX entry. A standard citation can be formatted as:
Bolton, E., Venigalla, A., Yasunaga, M., Hall, D., Xiong, B., Lee, T., Daneshjou, R., Frankle, J., Liang, P., Carbin, M., & Manning, C. D. (2024). *BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text*. arXiv preprint arXiv:2403.18421. (BioMedLM.pdf, page 1)

### License:
Insufficient information

### Contact:
For correspondence, contact Elliot Bolton at `elliotbolton@stanford.edu` or Christopher D. Manning at `manning@stanford.edu` (BioMedLM.pdf, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BioMedLM is a GPT-style autoregressive model intended for biomedical Natural Language Processing (NLP) applications. It was designed to be a transparent, privacy-preserving, and economical foundation model for tasks in biomedicine (BioMedLM.pdf, page 1).

**Capabilities:**
*   **Biomedical Question-Answering:** After fine-tuning, the model can perform strongly on multiple-choice question-answering tasks such as MedMCQA, MedQA, and MMLU Medical Genetics (BioMedLM.pdf, page 1).
*   **Yes/No Question-Answering:** It can be fine-tuned for tasks like PubMedQA and BioASQ that require a "yes", "no", or "maybe" answer based on a provided context (BioMedLM.pdf, page 7).
*   **Long-Form Answer Generation:** When fine-tuned on an instruction dataset of medical questions and answers, the model can generate useful, multi-sentence answers to patient questions on medical topics (BioMedLM.pdf, page 1, 10).
*   **Other Biomedical NLP Tasks:** The model can be used for information retrieval, summarization from biomedical literature, and analysis of clinical information like physician notes and radiology reports (BioMedLM.pdf, page 1).

The input-output structure depends on the fine-tuning task. For multiple-choice QA, the input is typically a context and question concatenated with each answer option, and the output is a score for each option. For generative QA, the input is a question, and the output is a generated text answer (BioMedLM.pdf, page 7).

### Primary intended users:
The primary intended users are researchers and organizations in the biomedical and healthcare fields, especially those with limited computational resources or strict privacy requirements that prevent the use of large, closed models accessed via APIs (BioMedLM.pdf, page 2).

### Out-of-scope uses:
The model is not intended for direct use in patient-facing applications without significant safeguards and oversight. The model is known to hallucinate, particularly around numerical values, and may produce factually incorrect information (BioMedLM.pdf, page 12). The base pre-trained model is not well-suited for question-answering without being fine-tuned on an appropriate instruction dataset (BioMedLM.pdf, page 10). It should not be used as a source of medical advice.

---

## How to Use
This section outlines how to use the model. 

The pre-trained model is available on the Hugging Face Hub at `https://huggingface.co/stanford-crfm/BioMedLM` (BioMedLM.pdf, page 14). Code for pre-training and fine-tuning is available on GitHub at `https://github.com/stanford-crfm/BioMedLM` (BioMedLM.pdf, page 14).

The model is a standard GPT-2 style autoregressive model and can be used with the Hugging Face `transformers` library.

**Fine-tuning for Multiple-Choice QA (e.g., MedQA, MMLU):**
A specialized architecture is recommended for improved performance. For each question, the input context is concatenated with each answer option. Each of these combined sequences is run through the transformer, and the final hidden state is passed to a linear classifier to generate a score for that option. The option with the highest score is selected as the answer (BioMedLM.pdf, page 7).

**Fine-tuning for Yes/No QA (e.g., PubMedQA, BioASQ):**
The recommended input format uses special tokens to structure the prompt:
`[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]`
The hidden state corresponding to a special token at the end of the sequence is fed to a linear classifier to produce scores for "yes", "no", or "maybe" (BioMedLM.pdf, pages 7-8).

**Fine-tuning for Generative QA:**
The model can be fine-tuned on a collection of medical question-answer pairs to generate multi-sentence answers. An example question is "What are the best ways to treat plantar fasciitis?" (BioMedLM.pdf, page 2, 10).

**Example Outputs (Generated for Consumer Health Questions):**
*   **Question:** "What are the common causes of lower back pain?"
*   **Sample Output:** "The most common causes of lower back pain include: Degenerative disk disease... Spinal stenosis... Scoliosis... Herniated disk... Spinal infection... Pregnancy... Trauma..." (BioMedLM.pdf, Table 12, page 11).
*   **Question:** "What does vitamin D do?"
*   **Sample Output:** "Vitamin D plays an important role in maintaining your bones and supporting your immune system... Vitamin D is a fat-soluble vitamin... Your body needs to get enough vitamin D to function properly... Vitamin D deficiency is a common condition. In the United States, about 1 in 10 people have vitamin D deficiency." (BioMedLM.pdf, Table 12, page 11).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Training Data Domain:** The model's performance is heavily influenced by its training on domain-specific biomedical text (PubMed). This leads to substantially better performance on biomedical tasks compared to an architecturally identical model (GPT-Neo 2.7B) trained on a general English corpus (BioMedLM.pdf, page 12).
*   **Domain Drift:** Performance can be affected by the specific sub-domain of the task. For example, the model performs worse on college-level biology topics compared to formal PubMed articles, which is likely due to this domain drift (BioMedLM.pdf, page 12).

### Evaluation factors:
The model was evaluated across several biomedical domains and academic levels, including:
*   Clinical Knowledge (BioMedLM.pdf, Table 9, page 9)
*   Professional Medicine (BioMedLM.pdf, Table 9, page 9)
*   College Biology (BioMedLM.pdf, Table 9, page 9)
*   Medical Genetics (BioMedLM.pdf, Table 9, page 9)
*   General biomedical questions from sources like USMLE, AIIMS PG, and NEET PG exams (BioMedLM.pdf, page 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess the model's performance on question-answering tasks is **accuracy** (BioMedLM.pdf, Tables 7, 8, 9, 10, 11). For other tasks mentioned in the literature where BioMedLM has been evaluated, metrics include **F1-score** (for named entity recognition) and **precision** (for relation extraction) (BioMedLM.pdf, page 13).

### Decision thresholds:
Insufficient information

### Variation approaches:
For the experiment analyzing the impact of the custom tokenizer, the evaluation was run over 5 random seeds to ensure the results were meaningful (BioMedLM.pdf, page 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several standard biomedical question-answering benchmarks:
*   **MedMCQA:** Contains 182,822 training, 4,183 development, and 6,150 test questions from Indian medical entrance exams (AIIMS PG and NEET PG) (BioMedLM.pdf, page 8).
*   **MedQA:** Contains 10,178 training, 1,272 development, and 1,273 test questions from USMLE (United States Medical Licensing Examination) questions found on the web (BioMedLM.pdf, page 8).
*   **MMLU (Massive Multitask Language Understanding):** A collection of exams covering a wide variety of subjects. The evaluation focused on biomedical-related exams: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (BioMedLM.pdf, page 9).
*   **PubMedQA:** Contains 450 training, 50 development, and 500 test questions constructed from PubMed article abstracts, requiring a "yes/no/maybe" answer (BioMedLM.pdf, page 9).
*   **BioASQ:** Contains 670 training, 75 development, and 140 test questions requiring a "yes/no" answer based on biomedical passages (BioMedLM.pdf, page 10).
*   **Health Question-Answer Pairs:** For generative evaluation, a dataset of over 53,000 medical knowledge question/answer pairs was collected from publicly available sources on the web, including FAQ pages and Wikipedia articles (BioMedLM.pdf, page 10).

### Motivation:
These datasets were chosen because they are standard benchmarks for biomedical NLP, allowing for direct comparison with other state-of-the-art models, including much larger ones like GPT-4 and Flan-PaLM (BioMedLM.pdf, page 8).

### Preprocessing:
The preprocessing steps were tailored to the model's architecture and the specific task:
*   **Multiple-Choice (MedQA, MedMCQA, MMLU):** For each question, the question context was concatenated with each answer option individually. Each resulting sequence was processed by the model, and a linear classifier on the final hidden state produced a score for each option (BioMedLM.pdf, page 7).
*   **Yes/No/Maybe (PubMedQA, BioASQ):** The input was structured using special tokens: `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]`. A linear classifier was then used on the final hidden state to produce scores for the possible answers (BioMedLM.pdf, pages 7-8).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained exclusively on the PubMed abstracts and full articles portion of The Pile dataset (as of November 2022) (Gao et al., 2020) (BioMedLM.pdf, page 5). The training corpus contained 34.6 billion tokens (BioMedLM.pdf, page 5).

The custom tokenizer was trained on PubMed abstracts (BioMedLM.pdf, page 5).

### Motivation:
The choice of training data was motivated by the goal of building a smaller, domain-specific model focused on biomedical text. This was done to investigate the value of domain specialization and to create a transparent, privacy-preserving, and economical model for biomedical applications (BioMedLM.pdf, page 2).

### Preprocessing:
A custom Byte-Pair Encoding (BPE) tokenizer was trained on PubMed abstracts using the Hugging Face Tokenizers library (BioMedLM.pdf, page 5).
*   **Tokenizer Type:** Byte-Pair Encoding (BPE) (tokenizer.json).
*   **Vocabulary Size:** 28,896 (BioMedLM.pdf, Table 2, page 5).
*   **Minimum Frequency:** 2 (BioMedLM.pdf, Table 2, page 5).
*   **Pre-tokenizer:** ByteLevel (tokenizer.json).
This custom tokenizer was designed to represent common biomedical terms as single tokens, which was shown to improve downstream task performance (BioMedLM.pdf, page 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance was evaluated on several biomedical QA benchmarks. The results are presented as accuracy.

**MedMCQA (Test Accuracy)** (BioMedLM.pdf, Table 7, page 8)
*   **BioMedLM (2.7B, fine-tune):** 57.3%
*   *For comparison:*
    *   GPT-4 (few-shot): 72.4%
    *   Flan-PaLM (540B, few-shot): 57.6%
    *   Galactica (120B, zero-shot): 52.9%

**MedQA (Test Accuracy)** (BioMedLM.pdf, Table 8, page 9)
*   **BioMedLM (2.7B, fine-tune):** 54.7%
*   *For comparison:*
    *   Med-PaLM 2 (closed, few-shot): 85.4%
    *   GPT-4 (closed, few-shot): 81.4%
    *   GPT-Neo 2.7B (fully open, fine-tune): 37.7%

**PubMedQA (Test Accuracy)** (BioMedLM.pdf, Table 10, page 9)
*   **BioMedLM (2.7B, fine-tune):** 74.4%
*   *For comparison:*
    *   BioGPT (1.5B, fine-tune w/ extra data): 81.0%
    *   Flan-PaLM (540B, few-shot): 79.0%
    *   GPT-4 (zero-shot): 75.2%
    *   GPT-Neo 2.7B (2.7B, fine-tune): 66.1%

**BioASQ (Test Accuracy)** (BioMedLM.pdf, Table 11, page 10)
*   **BioMedLM (2.7B, fine-tune):** 95.7%
*   *For comparison:*
    *   DRAGON (360M, fine-tune): 96.4%
    *   BioLinkBERT (340M, fine-tune): 94.9%
    *   Galactica (120B, zero-shot): 94.3%
    *   GPT-Neo 2.7B (2.7B, fine-tune): 67.1%

**MMLU (Accuracy on biomedical topics)** (BioMedLM.pdf, Table 9, page 9)
| Subject | BioMedLM (2.7B, fine-tune) | Flan-PaLM (540B, few-shot) | GPT-4 (few-shot) |
| :--- | :--- | :--- | :--- |
| Clinical Knowledge | 59.6% | 80.4% | 86.4% |
| Professional Medicine | 63.1% | 83.8% | 93.8% |
| College Biology | 60.7% | 88.9% | 93.8% |
| Medical Genetics | 69.0% | 75.0% | 92.0% |

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper notes that inference can be run on a laptop, suggesting relatively low requirements for loading and running the model compared to larger models (BioMedLM.pdf, page 2).

### Deploying Requirements:
The model's small size allows organizations to serve it internally without needing giant compute clusters (BioMedLM.pdf, page 2).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The model was pre-trained on the MosaicML Cloud across 128 40GB Nvidia A100 GPUs for 6.25 days (BioMedLM.pdf, page 6).
*   **Fine-tuning:** The model is designed to be "comfortably fine-tuned on a single A100 GPU" (BioMedLM.pdf, page 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Transparency:** BioMedLM was developed as a transparent alternative to closed, proprietary models. Its training data is fully documented (exclusively PubMed), and its architecture is public, allowing researchers to better understand its capabilities and limitations (BioMedLM.pdf, page 1, 2).
*   **Privacy:** The model is small enough to be run locally ("on-device inference"), which is a critical feature for healthcare applications. This allows organizations to use the model without sending sensitive patient data over the internet to third-party APIs, preserving patient privacy in line with regulations like HIPAA (BioMedLM.pdf, page 1, 2).
*   **Risk of Hallucination:** The developers acknowledge that the model can hallucinate, especially with numerical values. For example, in a generated answer, it incorrectly stated that 10% of people in the US have Vitamin D deficiency, when the actual figure is closer to 35%. This highlights the risk of providing factually incorrect information (BioMedLM.pdf, page 12).
*   **Mitigation Strategies:** The paper recommends that any application built on top of BioMedLM, especially one intended to provide answers to patients, must include "additional safeguards to correct incorrect numerical values" and other potential factual errors (BioMedLM.pdf, page 12). The model is not intended for direct medical advice.
*   **Sensitive Data:** The model was trained on publicly available data from PubMed abstracts and articles, so no private or sensitive patient data was used in its development (BioMedLM.pdf, page 5).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Factual Accuracy and Hallucination:** The model is prone to hallucination, particularly with numerical data. Generated outputs may be factually incorrect and should be verified before use in any critical application (BioMedLM.pdf, page 12).
*   **Requirement for Fine-tuning:** The base BioMedLM model was trained to replicate text from PubMed articles and is not well-suited for question-answering tasks out-of-the-box. It requires instruction fine-tuning to be useful for question response (BioMedLM.pdf, page 10).
*   **Domain Specificity:** While strong in the biomedical domain, the model's performance may degrade on related but distinct topics. For instance, it performs worse on college-level biology questions compared to formal medical genetics questions, likely due to the domain drift between the training data and the evaluation task (BioMedLM.pdf, page 12).

### Recommendations:
*   **Use Safeguards:** For any application, especially patient-facing ones, users should implement robust fact-checking and other safeguards to mitigate the risk of incorrect information generated by the model (BioMedLM.pdf, page 12).
*   **Instruction Fine-tuning:** To use the model for question-answering, it is essential to fine-tune it on a relevant instruction dataset of question-answer pairs (BioMedLM.pdf, page 10).
*   **Task-Specific Architectures:** For multiple-choice tasks, performance can be significantly improved by using a specialized fine-tuning architecture where each answer choice is scored independently, rather than relying on pure text generation (BioMedLM.pdf, page 7).
*   **Further Performance Improvement:** The paper suggests that a 2-phase fine-tuning approach, which involves training on noisy and unlabeled data first, could be a promising direction to further improve performance on tasks like PubMedQA (BioMedLM.pdf, page 12).

---