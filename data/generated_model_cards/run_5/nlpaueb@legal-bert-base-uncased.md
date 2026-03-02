## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos (LEGAL-BERT: The Muppets straight out of Law School, p. 1). Their affiliations are:
*   Department of Informatics, Athens University of Economics and Business (AUEB) (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   Institute of Informatics & Telecommunications, NCSR “Demokritos” (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   Computer Science Department, University of Sheffield, UK (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

### Model date:
The model was described in a paper published at the Findings of the Association for Computational Linguistics: EMNLP 2020, which took place from November 16-20, 2020 (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

### Model version:
The repository describes a family of BERT models named LEGAL-BERT. The provided configuration files correspond to the `LEGAL-BERT-SC` version, which was pre-trained from scratch on legal domain-specific corpora (LEGAL-BERT: The Muppets straight out of Law School, p. 3).

Other versions described in the associated paper include:
*   **LEGAL-BERT-FP**: This version was created by taking the general-domain BERT-BASE and conducting additional pre-training (further pre-training) on legal corpora (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   **LEGAL-BERT-SMALL**: A smaller and more efficient model with 6 layers, 512 hidden units, and 8 attention heads (35M parameters), also pre-trained from scratch on legal data. It is designed to be competitive with larger models while being approximately 4 times faster to train and requiring fewer hardware resources (LEGAL-BERT: The Muppets straight out of Law School, p. 3).

### Model type:
This model is a Transformer-based language model of the BERT type (`config.json`).
*   **Architecture**: It uses the `BertForPreTraining` architecture (`config.json`). It has 12 hidden layers, a hidden size of 768, 12 attention heads, and an intermediate size of 3072. The hidden activation function is GELU (`config.json`). This architecture is the same as BERT-BASE and contains 110M parameters (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Size**: The model has 110 million parameters (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Context Length**: The model supports a maximum context length of 512 tokens (`config.json`: `"max_position_embeddings": 512`).
*   **Vocabulary**: The model uses a custom vocabulary of 30,522 word pieces created from the legal training corpora (`config.json`: `"vocab_size": 30522`; LEGAL-BERT: The Muppets straight out of Law School, p. 3). The tokenizer converts text to lowercase (`tokenizer_config.json`: `"do_lower_case": true`).

### Training details:
The model was pre-trained from scratch on a large corpus of legal text.
*   **Algorithm**: The model was pre-trained using the objectives of Masked Language Modeling (MLM) and Next Sentence Prediction (NSP), consistent with the original BERT training procedure (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Parameters**: The pre-training was conducted for 1 million steps (approximately 40 epochs) with a batch size of 256 samples. The Adam optimizer was used with a learning rate of 1e-4 (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Hardware**: The model was trained on v3 TPUs with 8 cores from Google Cloud Compute Services (LEGAL-BERT: The Muppets straight out of Law School, p. 3).

### Paper or other resource for more information:
The primary resource for this model is the academic paper:
*   **Paper**: Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, Ion Androutsopoulos. 2020. "LEGAL-BERT: The Muppets straight out of Law School". In *Findings of the Association for Computational Linguistics: EMNLP 2020*, pages 2898–2904.
*   **Repository**: The paper states that all models and code examples are available at `https://huggingface.co/nlpaueb` (LEGAL-BERT: The Muppets straight out of Law School, p. 2, footnote 1).

### Citation details:
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
(LEGAL-BERT: The Muppets straight out of Law School)

### License:
Insufficient information.

### Contact:
Contact can be made via the emails provided in the research paper: `[ihalk,fergadiotis,rulller,ion]@aueb.gr` and `n.aletras@sheffield.ac.uk` (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
LEGAL-BERT is a language model pre-trained on English legal text, designed to be fine-tuned for various downstream tasks in the legal domain. Its primary purpose is to "assist legal NLP research, computational law, and legal technology applications" (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

The model was evaluated on and is intended for tasks such as:
*   **Legal Text Classification**: Assigning labels to legal documents. For example, classifying EU legislation with EUROVOC concepts or predicting violations in European Court of Human Rights cases (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Named Entity Recognition (NER)**: Extracting specific information from legal documents, such as identifying key elements in US contracts (e.g., parties, dates, governing law) (LEGAL-BERT: The Muppets straight out of Law School, p. 3).

The model takes English legal text as input and, after fine-tuning, outputs task-specific predictions like classification labels or entity tags.

### Primary intended users:
The primary intended users are researchers and developers working in the fields of:
*   Legal NLP research (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   Computational law (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   Legal technology applications (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

The `LEGAL-BERT-SMALL` version is particularly aimed at "researchers and practitioners with limited access to large computational resources" (LEGAL-BERT: The Muppets straight out of Law School, p. 4).

### Out-of-scope uses:
The model is specialized for the English legal domain. Its use is out-of-scope for:
*   **Non-legal domains**: The model's vocabulary and training data are specific to legal text. It is expected to underperform compared to general-domain models on generic text (e.g., news, social media) or other specialized domains like biomedical or scientific text (LEGAL-BERT: The Muppets straight out of Law School, p. 1).
*   **Languages other than English**: The training data consists entirely of English legal text, so the model is not suitable for other languages (LEGAL-BERT: The Muppets straight out of Law School, p. 2, Table 1).
*   **Use without fine-tuning**: As a pre-trained model, it must be fine-tuned on a downstream task-specific dataset to produce meaningful results.
*   **Providing legal advice**: The model is a tool for NLP tasks and should not be used to provide legal advice to end-users. Its outputs are predictions and may be incorrect.

---

## How to Use
This section outlines how to use the model.

The provided repository data indicates the model is compatible with the Hugging Face `transformers` library. The paper also provides a link to a Hugging Face repository for the models (`https://huggingface.co/nlpaueb`) (LEGAL-BERT: The Muppets straight out of Law School, p. 2, footnote 1).

While no specific code snippets are provided in the repository, a user would typically load the model and tokenizer using the library for a downstream task like text classification or token classification.

**Fine-tuning Recommendations:**
The paper recommends an "enriched grid-search" for fine-tuning hyperparameters, as the default suggestions from the original BERT paper may not be optimal for specialized domains. The suggested search space is:
*   **Learning rate**: {1e-5, 2e-5, 3e-5, 4e-5, 5e-5}
*   **Batch size**: {4, 8, 16, 32} (for relatively small datasets)
*   **Dropout rate**: {0.1, 0.2}
*   **Number of epochs**: Use early stopping based on validation loss without a fixed maximum number of epochs.
(LEGAL-BERT: The Muppets straight out of Law School, p. 3)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the specific sub-domain of legal text it is applied to. The training data is a diverse mix of legal documents, including legislation, court cases, and contracts from different jurisdictions (EU, UK, US) (LEGAL-BERT: The Muppets straight out of Law School, p. 2, Table 1). Therefore, performance may vary depending on the similarity of the target task's data to the training corpora. The paper shows that further pre-training on a specific sub-domain can improve adaptation to that sub-domain (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 3).

### Evaluation factors:
The model was evaluated across different legal sub-domains and tasks, which aligns with the relevant factors. The evaluation was disaggregated by dataset:
*   EU legislation (EURLEX57K)
*   European Court of Human Rights cases (ECHR-CASES)
*   US contracts (CONTRACTS-NER)
(LEGAL-BERT: The Muppets straight out of Law School, p. 3)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using the following metrics, specific to each evaluation task:
*   **Perplexity (PPT)**: Used to measure how well the language model predicts the language of the end-task datasets (LEGAL-BERT: The Muppets straight out of Law School, p. 4).
*   **nDCG@5**: Used for the multi-label classification task on the EURLEX57K dataset (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).
*   **F1 Score**: Used for the binary and multi-label classification tasks on the ECHR-CASES dataset, and for the NER task on all three subsets of the CONTRACTS-NER dataset (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To account for performance variations due to random initialization, the reported results are averages over multiple runs. The figures in the paper also show the minimum and maximum scores from these runs to indicate the range of performance (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three publicly available English legal NLP datasets:
1.  **EURLEX57K**: A dataset of 57,000 EU legislative documents for multi-label text classification. The documents are annotated with concepts from the EUROVOC thesaurus. The dataset is split into 45k training, 6k development, and 6k test documents (LEGAL-BERT: The Muppets straight out of Law School, p. 6, Appendix A).
2.  **ECHR-CASES**: A dataset of approximately 11,500 cases from the European Court of Human Rights. The task is to predict which articles of the Human Rights Convention were violated based on the facts of the case. It can be used for both binary (any violation vs. no violation) and multi-label classification (which specific articles were violated) (LEGAL-BERT: The Muppets straight out of Law School, p. 6, Appendix A).
3.  **CONTRACTS-NER**: A dataset of approximately 2,000 US contracts from the EDGAR database for Named Entity Recognition. It is organized into three subsets based on contract sections: contract header, dispute resolution, and lease details (LEGAL-BERT: The Muppets straight out of Law School, p. 6, Appendix A).

### Motivation:
These datasets were chosen to provide a comprehensive evaluation across different types of legal documents (legislation, court cases, contracts) and different NLP tasks (multi-label classification, binary classification, named entity recognition), demonstrating the model's versatility within the legal domain (LEGAL-BERT: The Muppets straight out of Law School, p. 3).

### Preprocessing:
The text was tokenized using a WordPiece tokenizer specific to the LEGAL-BERT model. All text was converted to lowercase during tokenization (`tokenizer_config.json`: `"do_lower_case": true`). The fine-tuning setup for each task followed previous work, involving specific model heads like a linear layer on the `[CLS]` token for classification or a linear CRF layer for NER (LEGAL-BERT: The Muppets straight out of Law School, p. 7, Appendix B).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a 12 GB corpus of diverse English legal text collected from several publicly available sources (LEGAL-BERT: The Muppets straight out of Law School, p. 2). The corpus consists of:
*   **EU legislation**: 1.9 GB from EURLEX.
*   **UK legislation**: 1.4 GB from legislation.gov.uk.
*   **European Court of Justice (ECJ) cases**: 0.6 GB from EURLEX.
*   **European Court of Human Rights (ECHR) cases**: 0.5 GB from HUDOC.
*   **US court cases**: 3.2 GB from the Case Law Access Project.
*   **US contracts**: 3.9 GB from SEC-EDGAR.
(LEGAL-BERT: The Muppets straight out of Law School, p. 2, Table 1)

### Motivation:
The motivation for using this collection of datasets was to create a language model adapted to the unique characteristics of legal text, which is often considered a 'sublanguage' with specialized vocabulary, syntax, and semantics. This domain-specific pre-training is intended to improve performance on downstream legal NLP tasks compared to models trained on general-domain corpora (LEGAL-BERT: The Muppets straight out of Law School, p. 1).

### Preprocessing:
A new vocabulary was created from scratch on the legal corpora using Google's sentencepiece library (LEGAL-BERT: The Muppets straight out of Law School, p. 3). During training, documents were tokenized into sequences of up to 512 tokens (LEGAL-BERT: The Muppets straight out of Law School, p. 3). All text was lowercased (`tokenizer_config.json`: `"do_lower_case": true`).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was evaluated against a tuned BERT-BASE model. LEGAL-BERT variants consistently outperformed the baseline across all tasks.
*   **EURLEX57K (nDCG@5)**: LEGAL-BERT-FP achieved a score of 82.4 on all labels, compared to 82.2 for the tuned baseline (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).
*   **ECHR-CASES (F1 Score)**: For the more difficult multi-label task, LEGAL-BERT-SC achieved an F1 of 58.6, a substantial improvement over the baseline's 56.7. For the binary task, the improvement was smaller (83.2 vs. 82.6) (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).
*   **CONTRACTS-NER (F1 Score)**: LEGAL-BERT-SC showed strong improvements, achieving an F1 of 94.6 on the contract header subset (vs. 92.4 baseline), 80.8 on dispute resolution (vs. 79.8 baseline), and 82.6 on lease details (vs. 81.5 baseline) (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).
*   **LEGAL-BERT-SMALL**: This smaller model was highly competitive, achieving scores comparable to the full-sized LEGAL-BERT models across most tasks (e.g., 82.0 nDCG@5 on EURLEX57K, 58.2 F1 on ECHR multi-label, 92.7 F1 on CONTRACTS-NER header) (LEGAL-BERT: The Muppets straight out of Law School, p. 4, Figure 4).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model has 110M parameters. For inference on a single 11GB NVIDIA-2080TI GPU, it can support a maximum batch size of 6 (LEGAL-BERT: The Muppets straight out of Law School, p. 7, Table 2). The smaller `LEGAL-BERT-SMALL` (35M parameters) can support a maximum batch size of 26 on the same hardware (LEGAL-BERT: The Muppets straight out of Law School, p. 7, Table 2).

### Deploying Requirements:
See Loading Requirements. The inference speed on a single 11GB NVIDIA-2080TI GPU is reported as 1.00x (baseline) for LEGAL-BERT and 1.70x for LEGAL-BERT-SMALL (LEGAL-BERT: The Muppets straight out of Law School, p. 7, Table 2).

### Training or Fine-tuning Requirements:
*   **Pre-training**: The original pre-training was performed on Google Cloud v3 TPUs with 8 cores (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Fine-tuning**: On a single 11GB NVIDIA-2080TI GPU, the fine-tuning speed of LEGAL-BERT is the same as BERT-BASE. LEGAL-BERT-SMALL is significantly faster, with a training speed of 2.43x (at batch size 1) to 4.00x (at max batch size) compared to the baseline (LEGAL-BERT: The Muppets straight out of Law School, p. 7, Table 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided repository does not contain specific information on ethical considerations. The training data consists of publicly available legal documents, including legislation, court cases, and contracts (LEGAL-BERT: The Muppets straight out of Law School, p. 2, Table 1). While court cases and contracts can contain sensitive personal information, the paper does not discuss whether any anonymization or de-identification steps were taken.

**Risks**:
*   **Bias**: Legal documents can reflect historical and societal biases. A model trained on this data may learn and perpetuate these biases. For example, biases in historical court rulings could be encoded in the model.
*   **Misuse**: The model is intended for legal NLP research and technology applications. If deployed in a real-world scenario (e.g., a tool for legal analysis or document review), its errors could have serious consequences. The model should not be used to provide automated legal advice.
*   **Privacy**: If the training data was not properly anonymized, the model could potentially memorize and reveal sensitive information from the legal cases or contracts it was trained on.

The provided materials do not discuss any steps taken to mitigate these risks.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Language Limitation**: The model is trained exclusively on English legal text and is not suitable for other languages (LEGAL-BERT: The Muppets straight out of Law School, p. 2, Table 1).
*   **Jurisdictional Scope**: While the training data is diverse (UK, EU, US), its performance on legal text from other jurisdictions or legal systems is untested.
*   **Task-Dependent Gains**: The performance improvement over general-domain models is more significant in more complex tasks where in-domain knowledge is crucial (e.g., multi-label classification on ECHR cases). For simpler tasks, the benefit may be less substantial (LEGAL-BERT: The Muppets straight out of Law School, p. 4-5).

### Recommendations:
*   **Hyperparameter Tuning**: Users should perform a thorough, expanded grid search when fine-tuning the model for a new task, as the default hyperparameters are often suboptimal for specialized domains (LEGAL-BERT: The Muppets straight out of Law School, p. 3).
*   **Consider Smaller Models**: For users with limited computational resources, `LEGAL-BERT-SMALL` is a highly competitive alternative that is much faster and more memory-friendly than the full-sized model (LEGAL-BERT: The Muppets straight out of Law School, p. 4).
*   **Domain-Specific Pre-training**: For tasks in a very specific legal sub-domain, users may benefit from conducting additional pre-training on a corpus from that sub-domain before fine-tuning (LEGAL-BERT: The Muppets straight out of Law School, p. 4).