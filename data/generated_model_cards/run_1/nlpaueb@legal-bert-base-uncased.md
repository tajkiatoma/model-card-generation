## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos (2020.findings-emnlp.261.pdf, p. 1). The developers are affiliated with the Department of Informatics at Athens University of Economics and Business, the Institute of Informatics & Telecommunications at NCSR “Demokritos”, and the Computer Science Department at the University of Sheffield, UK (2020.findings-emnlp.261.pdf, p. 1).

### Model date:
The paper describing the model was published at the EMNLP 2020 conference, which took place from November 16-20, 2020 (2020.findings-emnlp.261.pdf, p. 1).

### Model version:
The repository describes LEGAL-BERT, which is a family of BERT models adapted for the legal domain. The family includes several versions (2020.findings-emnlp.261.pdf, p. 1):
*   **LEGAL-BERT-FP (Further Pre-trained):** This version takes the original BERT-BASE model and continues its pre-training on domain-specific legal corpora (2020.findings-emnlp.261.pdf, p. 2).
*   **LEGAL-BERT-SC (From Scratch):** This version is pre-trained from scratch on domain-specific legal corpora with a new vocabulary created from this data (2020.findings-emnlp.261.pdf, p. 1, 3).
*   **LEGAL-BERT-SMALL:** A substantially smaller and more efficient model pre-trained from scratch on legal data. It is approximately 4 times faster to train than the base models (2020.findings-emnlp.261.pdf, p. 2, 3).

These models are intended to improve performance on legal NLP tasks compared to using a generic BERT model "out of the box" (2020.findings-emnlp.261.pdf, p. 1).

### Model type:
LEGAL-BERT is a family of models based on the BERT (Bidirectional Encoder Representations from Transformers) architecture (2020.findings-emnlp.261.pdf, p. 1). The core architecture is a multi-layer bidirectional Transformer encoder (config.json.txt).

Key architectural details:
*   **LEGAL-BERT-FP and LEGAL-BERT-SC:** These models share the same architecture as BERT-BASE:
    *   **Architecture:** BertForPreTraining (config.json.txt)
    *   **Layers:** 12 hidden layers (config.json.txt)
    *   **Attention Heads:** 12 (config.json.txt)
    *   **Hidden Size:** 768 (config.json.txt)
    *   **Total Parameters:** 110M (2020.findings-emnlp.261.pdf, p. 3)
    *   **Vocabulary Size:** 30,522 (config.json.txt)
*   **LEGAL-BERT-SMALL:** This is a lightweight version with:
    *   **Layers:** 6 hidden layers (2020.findings-emnlp.261.pdf, p. 3)
    *   **Attention Heads:** 8 (2020.findings-emnlp.261.pdf, p. 3)
    *   **Hidden Size:** 512 (2020.findings-emnlp.261.pdf, p. 3)
    *   **Total Parameters:** 35M (2020.findings-emnlp.261.pdf, p. 3)

The models support a maximum context length of 512 tokens (config.json.txt; tokenizer_config.json.txt). The tokenizer converts text to lowercase (tokenizer_config.json.txt).

### Training details:
The LEGAL-BERT models were developed using two main pre-training strategies on a 12 GB corpus of diverse English legal text (2020.findings-emnlp.261.pdf, p. 2):

1.  **Further Pre-training (FP):** The publicly available BERT-BASE model was subjected to additional pre-training steps (up to 500k) on the legal corpora (2020.findings-emnlp.261.pdf, p. 2).
2.  **Pre-training from Scratch (SC):** The LEGAL-BERT-SC and LEGAL-BERT-SMALL models were randomly initialized and trained from scratch for 1 million steps (approximately 40 epochs) on the legal corpora. For LEGAL-BERT-SC, a new vocabulary of 30k sub-words was created from the legal text using Google's sentencepiece library (2020.findings-emnlp.261.pdf, p. 2, 3).

**Pre-training Hyperparameters:**
*   **Optimizer:** Adam (2020.findings-emnlp.261.pdf, p. 3)
*   **Learning Rate:** 1e-4 (2020.findings-emnlp.261.pdf, p. 3)
*   **Batch Size:** 256 samples (2020.findings-emnlp.261.pdf, p. 3)
*   **Max Sequence Length:** 512 tokens (2020.findings-emnlp.261.pdf, p. 3)

### Paper or other resource for more information:
The primary resource is the academic paper describing the model's development and evaluation:
*   **Paper:** Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, Ion Androutsopoulos. 2020. "LEGAL-BERT: The Muppets straight out of Law School". In *Findings of the Association for Computational Linguistics: EMNLP 2020*, pages 2898–2904 (2020.findings-emnlp.261.pdf).
*   **Repository:** The models and code examples are available at `https://huggingface.co/nlpaueb` (2020.findings-emnlp.261.pdf, p. 2).

### Citation details:
To cite the model, please use the following BibTeX entry based on the provided paper:
```bibtex
@inproceedings{chalkidis-etal-2020-legal,
    title = "{LEGAL}-{BERT}: The Muppets straight out of Law School",
    author = "Chalkidis, Ilias  and
      Fergadiotis, Manos  and
      Malakasiotis, Prodromos  and
      Aletras, Nikolaos  and
      Androutsopoulos, Ion",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.findings-emnlp.261",
    pages = "2898--2904",
}
```
(2020.findings-emnlp.261.pdf)

### License:
Insufficient information

### Contact:
Contact information for the developers can be found in the associated paper: `[ihalk,fergadiotis,rulller,ion]@aueb.gr` and `n.aletras@sheffield.ac.uk` (2020.findings-emnlp.261.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The LEGAL-BERT family of models is intended to assist legal NLP research, computational law, and legal technology applications (2020.findings-emnlp.261.pdf, p. 1). The models are designed to be fine-tuned for specific downstream tasks in the legal domain. The paper evaluates their performance on:
*   **Multi-label Text Classification:** Assigning concepts to EU legislation (2020.findings-emnlp.261.pdf, p. 3, 6).
*   **Binary and Multi-label Text Classification:** Predicting violations of the Human Rights Convention based on case facts (2020.findings-emnlp.261.pdf, p. 3, 6).
*   **Named Entity Recognition (NER):** Extracting elements such as parties, dates, and jurisdictions from US contracts (2020.findings-emnlp.261.pdf, p. 3, 6).

The input is a sequence of text (e.g., a legal document or clause), and the output depends on the fine-tuning task (e.g., a set of labels for classification, or a sequence of entity tags for NER).

### Primary intended users:
The primary users are researchers and practitioners in the fields of Natural Language Processing (NLP), computational law, and legal technology (2020.findings-emnlp.261.pdf, p. 1, 2).

### Out-of-scope uses:
The models are specialized for the legal domain. Using them on generic or other specialized domains (e.g., biomedical) without further adaptation is out-of-scope and may lead to suboptimal performance, as they were pre-trained on legal text and vocabulary (2020.findings-emnlp.261.pdf, p. 1, 2; vocab.txt).

---

## How to Use
This section outlines how to use the model.

The models are publicly available and can be used through the Hugging Face platform at `https://huggingface.co/nlpaueb` (2020.findings-emnlp.261.pdf, p. 2).

The primary use case is to fine-tune the model on a downstream legal task. The paper's authors recommend an expanded hyper-parameter search space for fine-tuning, as the default guidelines suggested for BERT are not always optimal for specialized domains. The recommended search space is (2020.findings-emnlp.261.pdf, p. 3):
*   **Batch Size:** {4, 8, 16, 32}
*   **Learning Rate:** {1e-5, 2e-5, 3e-5, 4e-5, 5e-5}
*   **Dropout Rate:** {0.1, 0.2}
*   **Epochs:** Use early stopping based on validation loss, without a fixed maximum number of epochs.

The paper provides examples of fine-tuning setups for different tasks (2020.findings-emnlp.261.pdf, p. 6-7):
*   **For text classification (EURLEX57K):** A linear layer with sigmoid activations is placed on top of the `[CLS]` token's final representation.
*   **For case-based classification (ECHR-CASES):** A hierarchical version is used where a shared BERT encodes each fact, followed by a self-attention mechanism to produce the final document representation.
*   **For sequence tagging (CONTRACTS-NER):** The final representations for all tokens in the sequence are fed to a linear CRF layer.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary relevant factor is the domain of the text. The model is specialized for legal text, and its performance is expected to be superior in this domain compared to generic text (2020.findings-emnlp.261.pdf, p. 1). The specific sub-domain of legal text (e.g., EU legislation vs. US contracts) also influences which pre-training strategy is optimal (2020.findings-emnlp.261.pdf, p. 4).

### Evaluation factors:
The model was evaluated across different legal sub-domains and task types to analyze its performance. The evaluation factors correspond to the datasets used (2020.findings-emnlp.261.pdf, p. 3):
*   EU legislation (EURLEX57K dataset)
*   European Court of Human Rights cases (ECHR-CASES dataset)
*   US contracts (CONTRACTS-NER dataset)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using the following metrics (2020.findings-emnlp.261.pdf, p. 4, 7):
*   **Perplexity (PPT):** Used to indicate how well a model predicts the language of an end-task.
*   **nDCG@5:** Used for the multi-label classification task on the EURLEX57K dataset.
*   **F1-Score:** Used for the binary and multi-label classification tasks on the ECHR-CASES dataset and for the named entity recognition task on the CONTRACTS-NER dataset.

### Decision thresholds:
Insufficient information

### Variation approaches:
The reported results for the end-tasks on test data are averages over multiple runs. The minimum and maximum scores are also shown to indicate variance (2020.findings-emnlp.261.pdf, p. 4, Figure 4).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three publicly available legal NLP datasets (2020.findings-emnlp.261.pdf, p. 3, 6):
1.  **EURLEX57K:** Contains 57k legislative documents from EURLEX, annotated with concepts from the EUROVOC thesaurus. The dataset is split into 45k training, 6k development, and 6k test documents. The average document length is 727 words (2020.findings-emnlp.261.pdf, p. 6).
2.  **ECHR-CASES:** Contains approximately 11.5k cases from the European Court of Human Rights public database. Each case includes a list of facts and is mapped to articles of the Human Rights Convention that were violated, if any (2020.findings-emnlp.261.pdf, p. 6).
3.  **CONTRACTS-NER:** Contains approximately 2k US contracts from EDGAR, annotated for multiple contract elements (e.g., title, parties, dates, governing law). The dataset is organized into three groups based on element position: contract header, dispute resolution, and lease details (2020.findings-emnlp.261.pdf, p. 6).

### Motivation:
These datasets were chosen to provide a comprehensive evaluation across different legal NLP tasks (multi-label classification, sequence tagging) and various sub-domains of legal text (legislation, court cases, contracts) (2020.findings-emnlp.261.pdf, p. 3).

### Preprocessing:
The paper states that for fine-tuning, the experiments of previous works (Chalkidis et al., 2019c,a,d) were replicated, but does not provide specific details on the preprocessing of the evaluation data (2020.findings-emnlp.261.pdf, p. 3).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The models were pre-trained on a collection of 12 GB of diverse English legal text scraped from publicly available resources. The corpora include (2020.findings-emnlp.261.pdf, p. 2, Table 1):
*   **EU legislation:** 61,826 documents (1.9 GB) from EURLEX.
*   **UK legislation:** 19,867 documents (1.4 GB) from legislation.gov.uk.
*   **European Court of Justice (ECJ) cases:** 19,867 documents (0.6 GB) from EURLEX.
*   **European Court of Human Rights (ECHR) cases:** 12,554 documents (0.5 GB) from HUDOC.
*   **US court cases:** 164,141 documents (3.2 GB) from the Case Law Access Project.
*   **US contracts:** 76,366 documents (3.9 GB) from SEC-EDGAR.

### Motivation:
The datasets were chosen to create a large and diverse corpus of legal text, covering multiple fields (legislation, case law, contracts) and jurisdictions (EU, UK, US) to pre-train a robust language model for the legal domain (2020.findings-emnlp.261.pdf, p. 2).

### Preprocessing:
For the "from scratch" models (LEGAL-BERT-SC and LEGAL-BERT-SMALL), a new vocabulary was created from the training corpora using Google's sentencepiece library (2020.findings-emnlp.261.pdf, p. 3). During pre-training, documents were tokenized into sequences of up to 512 sentencepiece tokens (2020.findings-emnlp.261.pdf, p. 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Figure 4 of the paper presents the performance of LEGAL-BERT variants compared to a tuned BERT-BASE on the test sets of the evaluation datasets. All LEGAL-BERT variants almost always lead to better results than the tuned BERT-BASE (2020.findings-emnlp.261.pdf, p. 4).

**EURLEX57K (nDCG@5):**
*   BERT-BASE (tuned): 82.2
*   LEGAL-BERT-FP: 82.4
*   LEGAL-BERT-SC: 82.2
*   LEGAL-BERT-SMALL: 82.0

**ECHR-CASES (F1-Score):**
*   Binary Classification:
    *   BERT-BASE (tuned): 82.6
    *   LEGAL-BERT-FP: 82.6
    *   LEGAL-BERT-SC: 83.2
*   Multi-label Classification:
    *   BERT-BASE (tuned): 56.7
    *   LEGAL-BERT-FP: 58.6
    *   LEGAL-BERT-SC: 59.2

**CONTRACTS-NER (F1-Score):**
*   Contract Header:
    *   BERT-BASE (tuned): 92.4
    *   LEGAL-BERT-FP: 94.1
    *   LEGAL-BERT-SC: 94.6
*   Dispute Resolution:
    *   BERT-BASE (tuned): 79.8
    *   LEGAL-BERT-FP: 81.4
    *   LEGAL-BERT-SC: 80.8
*   Lease Details:
    *   BERT-BASE (tuned): 81.5
    *   LEGAL-BERT-FP: 82.3
    *   LEGAL-BERT-SC: 82.6

Impressively, LEGAL-BERT-SMALL achieves performance comparable to the larger models across most datasets (2020.findings-emnlp.261.pdf, p. 4).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Table 2 in the paper provides a comparison of model efficiency on a single 11GB NVIDIA-2080TI GPU. LEGAL-BERT-SMALL (35M parameters) can handle a max batch size of 26 for inference, while the larger LEGAL-BERT models (110M parameters) can handle a max batch size of 6. LEGAL-BERT-SMALL has an inference speed 1.7x faster than the base models (2020.findings-emnlp.261.pdf, p. 7, Table 2).

### Deploying Requirements:
See Loading Requirements. The smaller footprint and faster inference speed of LEGAL-BERT-SMALL make it more suitable for deployment in resource-constrained environments (2020.findings-emnlp.261.pdf, p. 4, 7).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The models were pre-trained using v3 TPUs with 8 cores from Google Cloud Compute Services (2020.findings-emnlp.261.pdf, p. 3).
*   **Fine-tuning:** On an 11GB NVIDIA-2080TI GPU, LEGAL-BERT-SMALL trains approximately 4 times faster than the base models at maximum batch size (2020.findings-emnlp.261.pdf, p. 7, Table 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The optimal pre-training strategy (further pre-training vs. training from scratch) may vary depending on the specific downstream task and dataset. The paper shows that one strategy does not consistently outperform the other across all evaluations (2020.findings-emnlp.261.pdf, p. 5).
*   The performance gains are more substantial in more challenging tasks where in-domain knowledge is more important (e.g., multi-label classification in ECHR-CASES, NER on contracts) (2020.findings-emnlp.261.pdf, p. 4, 5).

### Recommendations:
*   **Expanded Hyperparameter Search:** Users should adopt an expanded grid search when fine-tuning for end-tasks, as this can have a drastic impact on performance. The default ranges suggested by the original BERT paper are not always optimal (2020.findings-emnlp.261.pdf, p. 3, 5).
*   **Use of LEGAL-BERT-SMALL:** For users with limited access to large computational resources, LEGAL-BERT-SMALL is a highly competitive and efficient alternative to the larger models. It can be adopted more easily in low-resource test-beds and provides a more memory-friendly basis for complex hierarchical architectures (2020.findings-emnlp.261.pdf, p. 4, 5).