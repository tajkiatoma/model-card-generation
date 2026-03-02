## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from Stanford University and DataBricks (2403.18421.pdf, p. 1). The authors are Elliot Bolton, Abhinav Venigalla, Michihiro Yasunaga, David Hall, Betty Xiong, Tony Lee, Roxana Daneshjou, Jonathan Frankle, Percy Liang, Michael Carbin, and Christopher D. Manning (2403.18421.pdf, p. 1).

### Model date:
The model was made publicly available in December 2022 (2403.18421.pdf, p. 2). The associated research paper was submitted to arXiv on March 27, 2024 (2403.18421.pdf, p. 1). The pre-training process took 6.25 days to complete (2403.18421.pdf, p. 6).

### Model version:
The provided documents do not specify a version number. The model is referred to as BioMedLM (2403.18421.pdf, p. 1). It is a 2.7 billion parameter model trained specifically on biomedical text, which distinguishes it from architecturally similar models of the same size, such as GPT-Neo 2.7B, that were trained on general English corpora like The Pile (2403.18421.pdf, p. 2, 3).

### Model type:
BioMedLM is a GPT-style, autoregressive, decoder-only Transformer model based on the GPT-2 architecture (2403.18421.pdf, p. 1, 4; config.json.txt).

**Key Architectural Details:**
*   **Parameters:** 2.7 billion (2403.18421.pdf, p. 1).
*   **Layers:** 32 (`n_layer`) (2403.18421.pdf, p. 4, Table 1; config.json.txt).
*   **Attention Heads:** 20 (`n_head`) (2403.18421.pdf, p. 4, Table 1; config.json.txt).
*   **Hidden Size:** 2560 (`n_embd`) (2403.18421.pdf, p. 4, Table 1; config.json.txt).
*   **Context Length:** 1024 tokens (`n_ctx`) (2403.18421.pdf, p. 4, Table 1; config.json.txt).
*   **Vocabulary Size:** 28,896, using a custom Byte-Pair Encoding (BPE) tokenizer trained on PubMed abstracts (2403.18421.pdf, p. 4-5, Table 1; config.json.txt).
*   **Activation Function:** `gelu_new` (config.json.txt).
*   **Positional Embeddings:** The model uses learned absolute positional embeddings (2403.18421.pdf, p. 4).

### Training details:
The model was pre-trained on the task of predicting the next token, minimizing the standard cross-entropy loss (2403.18421.pdf, p. 6).

**Key Training Parameters and Methodologies:**
*   **Optimizer:** Decoupled AdamW (2403.18421.pdf, p. 6).
*   **Learning Rate:** 1.6e-4, with a cosine scheduler and a linear warmup of 100 batches (2403.18421.pdf, p. 6, Table 5).
*   **Batch Size:** 1024 sequences, with a sequence length of 1024, for a total of 1,048,576 tokens per batch (2403.18421.pdf, p. 6, Table 5).
*   **Total Training Tokens:** 300 billion (2403.18421.pdf, p. 6).
*   **Optimizer Hyperparameters:** Betas = [0.9, 0.95], Epsilon = 1e-8, Weight Decay = 1.6e-5 (2403.18421.pdf, p. 6, Table 5).
*   **Precision:** Mixed precision training was used. Computation was done in `bf16`, while parameter and optimizer states were stored in `fp32` (2403.18421.pdf, p. 6, Table 6).
*   **Efficiency:** The training process utilized Flash Attention to accelerate computation and reduce memory requirements (2403.18421.pdf, p. 6). The training was conducted using the Composer library and PyTorch FSDP (2403.18421.pdf, p. 6).

### Paper or other resource for more information:
*   **Academic Paper:** "BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text". This paper details the model's architecture, training process, and evaluation results (2403.18421.pdf).
*   **Hugging Face Hub:** The pre-trained model is available for download at: https://huggingface.co/stanford-crfm/BioMedLM (2403.18421.pdf, p. 1, 14).
*   **GitHub Repository:** The code used for pre-training and fine-tuning is available at: https://github.com/stanford-crfm/BioMedLM (2403.18421.pdf, p. 7, 14).

### Citation details:
The provided repository does not contain a pre-formatted BibTeX citation. Based on the paper, a citation can be constructed as follows:

```bibtex
@misc{bolton2024biomedlm,
      title={BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text}, 
      author={Elliot Bolton and Abhinav Venigalla and Michihiro Yasunaga and David Hall and Betty Xiong and Tony Lee and Roxana Daneshjou and Jonathan Frankle and Percy Liang and Michael Carbin and Christopher D. Manning},
      year={2024},
      eprint={2403.18421},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(2403.18421.pdf, p. 1)

### License:
Insufficient information. The provided documents do not contain information about the model's license.

### Contact:
For correspondence, the developers can be contacted at:
*   elliotbolton@stanford.edu
*   manning@stanford.edu

(2403.18421.pdf, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BioMedLM is designed as a foundational model for biomedical NLP applications. Its primary intended uses include:
*   **Biomedical Question Answering:** The model shows strong performance on multiple-choice question-answering tasks like MedMCQA, MedQA, and MMLU after fine-tuning (2403.18421.pdf, p. 1).
*   **Long-Form Answer Generation:** After fine-tuning, the model can generate multi-sentence answers to medical questions posed by patients (2403.18421.pdf, p. 1, 8).
*   **Information Retrieval and Summarization:** The model is intended for applications such as retrieving and summarizing information from biomedical literature, physician notes in electronic health records, and radiology reports (2403.18421.pdf, p. 1).
*   **Privacy-Preserving NLP:** The model is small enough to be run on-premise, allowing organizations to build applications without sending sensitive patient data to third-party APIs, thus helping with HIPAA compliance (2403.18421.pdf, p. 2).
*   **Transparent and Economical AI:** It serves as a transparent alternative to closed-source models, as its training data is fully documented. Its smaller size makes it more economical and environmentally friendly to run (2403.18421.pdf, p. 1).

The model's input-output structure depends on the fine-tuning task. For multiple-choice QA, the input is a context and question, and the output is a selected choice. For generative QA, the input is a question, and the output is a generated text answer (2403.18421.pdf, p. 7-8).

### Primary intended users:
The primary intended users are:
*   **Biomedical and Healthcare Organizations:** Especially those with limited computational resources or strict data privacy requirements that prevent the use of cloud-based APIs (2403.18421.pdf, p. 2).
*   **Researchers and Practitioners:** Individuals in the NLP and biomedical fields who need a transparent, open-source model to study domain-specific language modeling and build specialized applications (2403.18421.pdf, p. 2-3).

### Out-of-scope uses:
*   **Direct use without fine-tuning:** The base BioMedLM model is trained to replicate text from PubMed articles and is not well-suited for question-answering or instruction-following tasks without being fine-tuned (2403.18421.pdf, p. 10).
*   **Unsupervised clinical decision-making:** The model can hallucinate, particularly with numerical values, and its answers can be vague. It should not be used in a patient-facing context or for clinical decisions without "additional safeguards" and human oversight (2403.18421.pdf, p. 12).
*   **General-purpose NLP:** The model is specialized for the biomedical domain and is not intended to compete with large, general-purpose models on non-biomedical tasks (2403.18421.pdf, p. 1).

---

## How to Use
This section outlines how to use the model.

The model can be accessed via the Hugging Face Hub and used with standard libraries. The code for pre-training and fine-tuning is available on GitHub: https://github.com/stanford-crfm/BioMedLM (2403.18421.pdf, p. 14).

The paper describes several fine-tuning approaches for specific tasks:

*   **For Multiple-Choice Question Answering (e.g., MedQA, MedMCQA):**
    1.  For each question, create multiple inputs by concatenating the question context with each of the possible answer options.
    2.  Process each concatenated sequence through the transformer model.
    3.  Use the hidden state at the final position of each sequence as input to a linear classifier.
    4.  The classifier generates a score for each option, and the option with the highest score is selected as the answer (2403.18421.pdf, p. 7).

*   **For Yes/No/Maybe Question Answering (e.g., PubMedQA, BioASQ):**
    1.  Concatenate the context and the question. To improve performance, structure the prompt with special tokens, for example: `[Context Token] "Text of context..." [Question Token] “Text of question ..." [Answer Token]` (2403.18421.pdf, p. 7-8).
    2.  Feed the hidden state corresponding to a special token at the end of the sequence into a linear classifier.
    3.  The classifier produces scores for the labels "yes", "no", and "maybe" (or just "yes"/"no") (2403.18421.pdf, p. 7).

*   **For Long-Form Question Answering:**
    1.  Fine-tune the model on a dataset of medical question-answer pairs. The paper describes creating such a dataset from publicly available web sources and Wikipedia articles (2403.18421.pdf, p. 8, 10).
    2.  After fine-tuning, the model can take a medical question as input and generate a multi-sentence answer (2403.18421.pdf, p. 8).

**Sample Outputs for Long-Form QA:**
Below are example responses generated by the fine-tuned model for consumer health questions.

| Question | BioMedLM Answer |
| :--- | :--- |
| What does vitamin D do? | Vitamin D plays an important role in maintaining your bones and supporting your immune system. It's also involved in many other body processes... |
| What are good treatments for arthritis? | There are many treatments for arthritis. Your healthcare provider will recommend the treatment that's right for you based on your symptoms and the type of arthritis you have. Treatments for arthritis include: Medications... Physical therapy... Surgery... |
| How can I stop diarrhea? | The best way to stop diarrhea is to treat the cause. If you have an infection, your healthcare provider may prescribe antibiotics. If you have a food poisoning outbreak, you can go to the emergency room or call your healthcare provider to get help... |

(2403.18421.pdf, p. 11, Table 12)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Text Domain:** The model's performance is highly dependent on the domain of the text. It is specialized for biomedical text from PubMed and significantly outperforms an architecturally identical model (GPT-Neo 2.7B) trained on general English for biomedical tasks (2403.18421.pdf, p. 12). Performance can vary between sub-domains, such as formal research articles versus college-level biology topics (2403.18421.pdf, p. 12).
*   **Tokenizer:** The use of a custom, domain-specific tokenizer trained on PubMed abstracts was shown to provide a meaningful improvement in downstream task performance compared to a general-purpose GPT-2 tokenizer (2403.18421.pdf, p. 5, Table 4).
*   **Fine-tuning Data:** The model's ability to perform specific tasks like question-answering is entirely dependent on being fine-tuned on a relevant instruction dataset (2403.18421.pdf, p. 10).

### Evaluation factors:
The model was evaluated across different biomedical question-answering tasks, which represent distinct factors. For the MMLU benchmark, performance was disaggregated by the following subject areas:
*   Clinical Knowledge
*   Professional Medicine
*   College Biology
*   Medical Genetics

(2403.18421.pdf, p. 9, Table 9)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Accuracy:** This is the primary metric used to evaluate the model's performance on all downstream question-answering tasks (MedMCQA, MedQA, MMLU, PubMedQA, and BioASQ) (2403.18421.pdf, p. 8-10, Tables 7-11).
*   **Cross-Entropy Loss (Perplexity):** This metric was used during pre-training to monitor the model's learning progress on the training and validation sets (2403.18421.pdf, p. 6, Figure 1).

### Decision thresholds:
For classification-based fine-tuning tasks, the decision is made by selecting the class (e.g., the correct answer option) that receives the highest score from the final linear classifier layer. No specific numerical thresholds are mentioned (2403.18421.pdf, p. 7).

### Variation approaches:
To evaluate the impact of the custom tokenizer, experiments were run five times with different random seeds to ensure the observed performance improvement was statistically meaningful (2403.18421.pdf, p. 5). For other evaluation results, the paper does not specify if they are an average of multiple runs.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on five standard biomedical question-answering datasets:
*   **MedMCQA:** A large-scale dataset with 182,822 training, 4,183 development, and 6,150 test questions drawn from Indian medical entrance exams (AIIMS PG and NEET PG) (2403.18421.pdf, p. 8).
*   **MedQA:** Contains 10,178 training, 1,272 development, and 1,273 test questions drawn from USMLE (United States Medical Licensing Examination) questions found on the web (2403.18421.pdf, p. 8).
*   **MMLU (Massive Multitask Language Understanding):** A broad collection of exam questions. Evaluation focused on four biomedical-related subjects: Clinical Knowledge, Professional Medicine, College Biology, and Medical Genetics (2403.18421.pdf, p. 9).
*   **PubMedQA:** A dataset with 450 training, 50 development, and 500 test questions constructed from PubMed article abstracts, where answers are "yes", "no", or "maybe" (2403.18421.pdf, p. 9).
*   **BioASQ:** Contains 670 training, 75 development, and 140 test questions where answers are "yes" or "no" (2403.18421.pdf, p. 10).

For evaluating long-form answer generation, a dataset of over 53,000 question-answer pairs was collected from publicly available sources on the web (2403.18421.pdf, p. 8).

### Motivation:
These datasets were chosen because they are "standard biomedical NLP QA tasks," allowing for direct comparison with other models and providing a comprehensive benchmark of the model's capabilities in the biomedical question-answering space (2403.18421.pdf, p. 8).

### Preprocessing:
The evaluation data was preprocessed by formatting it into specific prompt structures suitable for the model. This involved concatenating question contexts with answer options for multiple-choice tasks and using special tokens (`[Context Token]`, `[Question Token]`) to structure the input for yes/no tasks. This reorganization was found to significantly improve performance (2403.18421.pdf, p. 7-8).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
BioMedLM was trained "exclusively on PubMed abstracts and full articles" (2403.18421.pdf, p. 1). The specific data source was the PubMed subset of **The Pile** dataset (as of November 2022) (2403.18421.pdf, p. 5). The training corpus contained 34.6 billion tokens. The model was trained for 300 billion tokens, which corresponds to 8.67 passes over the entire dataset (2403.18421.pdf, p. 5).

### Motivation:
The choice of training data was motivated by the goal of investigating the "value of domain specialization" (2403.18421.pdf, p. 2). By training a medium-sized model exclusively on high-quality, domain-specific text, the developers aimed to create a powerful tool for biomedical NLP that would be more transparent, private, and economical than very large, general-purpose models trained on undisclosed data (2403.18421.pdf, p. 2).

### Preprocessing:
The primary preprocessing step was tokenization. The text was processed using a custom **Byte-Pair Encoding (BPE) tokenizer** that was trained from scratch on PubMed abstracts (2403.18421.pdf, p. 5). This custom tokenizer was designed to better handle domain-specific terminology (e.g., "thrombin", "cytotoxicity") by representing them as single tokens, which was shown to improve downstream performance (2403.18421.pdf, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results are reported for individual tasks and for different subject areas within the MMLU benchmark.

**Performance by Task (Accuracy):**
*   **MedMCQA:** 57.3% (2403.18421.pdf, p. 8, Table 7)
*   **MedQA:** 54.7% (when fine-tuned with MedMCQA data) (2403.18421.pdf, p. 9, Table 8)
*   **PubMedQA:** 74.4% (2403.18421.pdf, p. 9, Table 10)
*   **BioASQ:** 95.7% (2403.18421.pdf, p. 10, Table 11)

**Performance by MMLU Subject (Accuracy):**
*   **Clinical Knowledge:** 59.6%
*   **Professional Medicine:** 63.1%
*   **College Biology:** 60.7%
*   **Medical Genetics:** 69.0%

(2403.18421.pdf, p. 9, Table 9)

### Intersectional results:
Insufficient information. The provided documents do not contain performance results across combinations of factors (e.g., by demographic and task).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The paper states that the model's size allows for "inference to be run on a laptop," but does not provide specific RAM or VRAM requirements (2403.18421.pdf, p. 2).

### Deploying Requirements:
Similar to loading, the model is designed for inference on a laptop, suggesting modest hardware requirements for deployment compared to larger models (2403.18421.pdf, p. 2).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The model was pre-trained on the MosaicML Cloud using **128 40GB Nvidia A100 GPUs**. The full pre-training run was completed in 6.25 days (2403.18421.pdf, p. 6).
*   **Fine-tuning:** The model is designed to be "comfortably fine-tuned on a **single A100 GPU**" (2403.18421.pdf, p. 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Sensitive Data Usage:** The model was trained on publicly available PubMed abstracts and articles, which are not expected to contain sensitive, personally identifiable information (PII) (2403.18421.pdf, p. 1, 5). This contrasts with closed models trained on unknown data sources, which may pose a higher risk (2403.18421.pdf, p. 1).
*   **Data Privacy in Application:** A key ethical motivation for creating BioMedLM was to mitigate the privacy risks associated with using large, API-based models in healthcare. Such models require sending potentially sensitive patient data over the internet, which can conflict with regulations like HIPAA. BioMedLM is small enough to be hosted internally by an organization, ensuring that private data does not leave their secure network (2403.18421.pdf, p. 2).
*   **Transparency and Reliability:** The use of a fully documented, public training dataset (PubMed) increases the model's transparency. This allows users and researchers to better understand the model's capabilities and limitations, mitigating the uncertainty associated with models trained on secret data (2403.18421.pdf, p. 2).
*   **Risk of Inaccurate Information (Hallucination):** The model is known to hallucinate, particularly with numerical data. For example, it incorrectly stated that 10% of people in the US have Vitamin D deficiency, when the figure is closer to 35% (2403.18421.pdf, p. 12). Deploying the model in a patient-facing application without safeguards to detect and correct such errors could lead to harm. The primary affected group would be patients or healthcare consumers who might receive incorrect medical information.
*   **Mitigation Strategies:** The developers explicitly recommend that any application using the model to provide answers to patients must include "additional safeguards to correct incorrect numerical values" (2403.18421.pdf, p. 12). The model's tendency to sometimes provide vague answers and refer users to a medical professional is also noted (2403.18421.pdf, p. 12).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Hallucination of Facts:** The model is prone to hallucination, especially regarding numerical values. Its generated responses are not guaranteed to be factually accurate and must be verified, particularly in any sensitive application (2403.18421.pdf, p. 12).
*   **Requires Fine-Tuning for Usefulness:** The base pre-trained model is not an instruction-following or question-answering model. It "needs to be fine-tuned on an instruction data set" to be useful for such tasks (2403.18421.pdf, p. 10).
*   **Performance Limitations:** While competitive with larger models on some tasks, BioMedLM is significantly outperformed by state-of-the-art models like GPT-4 and Med-PaLM 2 on benchmarks such as MedQA (2403.18421.pdf, p. 9, Table 8).
*   **Domain Drift:** The model's performance can be weaker on topics that drift from its core training data of formal PubMed articles. For example, it performs worse on college-level biology questions compared to topics with more direct medical emphasis (2403.18421.pdf, p. 12).

### Recommendations:
*   **Use with Human Oversight and Fact-Checking:** Due to the risk of hallucination, the model should not be used as a sole source of medical information. Any application, especially patient-facing ones, must incorporate safeguards and ideally human-in-the-loop processes to verify the accuracy of its outputs (2403.18421.pdf, p. 12).
*   **Fine-Tune for Specific Tasks:** Users should fine-tune the model on data specific to their target application to achieve the best performance (2403.18421.pdf, p. 10).
*   **Consider for Privacy-Sensitive Applications:** The model is a good candidate for biomedical NLP applications where data privacy is a major concern, as it can be deployed on-premise (2403.18421.pdf, p. 2).
*   **Future Research:** The paper suggests that performance on certain tasks like PubMedQA could potentially be improved by exploring a two-phase fine-tuning approach that incorporates noisy or unlabeled data, which is noted as a "promising future direction" (2403.18421.pdf, p. 12).