## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers: Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos (2020.findings-emnlp.261.pdf, p. 1). Their affiliations include the Department of Informatics at Athens University of Economics and Business, the Institute of Informatics & Telecommunications at NCSR “Demokritos”, and the Computer Science Department at the University of Sheffield, UK (2020.findings-emnlp.261.pdf, p. 1).

### Model date:
The paper describing the model was published in the Findings of the Association for Computational Linguistics: EMNLP 2020, which took place from November 16-20, 2020 (2020.findings-emnlp.261.pdf, p. 1).

### Model version:
The repository describes LEGAL-BERT, which is a family of BERT models adapted for the legal domain. The primary versions are (2020.findings-emnlp.261.pdf, p. 1):
*   **LEGAL-BERT-FP (Further Pre-trained):** This model is an adaptation of BERT-BASE that undergoes additional pre-training on domain-specific legal corpora (2020.findings-emnlp.261.pdf, p. 1).
*   **LEGAL-BERT-SC (From Scratch):** This model is pre-trained from scratch on domain-specific legal corpora with a new vocabulary of sub-word units created from this data (2020.findings-emnlp.261.pdf, p. 1).
*   **LEGAL-BERT-SMALL:** This is a substantially smaller, lightweight model pre-trained from scratch on legal data, designed to be more efficient and have a smaller environmental footprint (2020.findings-emnlp.261.pdf, p. 2, 3). It is approximately 4 times faster to train than the base-sized models (2020.findings-emnlp.261.pdf, p. 3).

### Model type:
LEGAL-BERT models are based on the Transformer architecture, specifically the BERT (Bidirectional Encoder Representations from Transformers) model type (2020.findings-emnlp.261.pdf, p. 1). They are designed for language understanding in the legal domain.

The model specifications are as follows:
*   **LEGAL-BERT-FP and LEGAL-BERT-SC:** These models share the same architecture as BERT-BASE, with 12 layers, 768 hidden units, 12 attention heads, and 110 million parameters (2020.findings-emnlp.261.pdf, p. 3).
*   **LEGAL-BERT-SMALL:** This is a smaller model with 6 layers, 512 hidden units, 8 attention heads, and 35 million parameters (32% the size of BERT-BASE) (2020.findings-emnlp.261.pdf, p. 3).

All models support a maximum sequence length of 512 tokens (tokenizer_config.json.txt). The tokenizer is configured to convert text to lowercase (tokenizer_config.json.txt). The vocabulary consists of legal and general-purpose tokens (vocab.txt).

### Training details:
The LEGAL-BERT models were pre-trained using different strategies on a 12 GB corpus of diverse English legal text (2020.findings-emnlp.261.pdf, p. 2).
*   **Pre-training Algorithm:** The models were pre-trained using the same objectives as the original BERT (Masked Language Model and Next Sentence Prediction).
*   **LEGAL-BERT-FP** was initialized from BERT-BASE and further pre-trained on legal corpora for up to 500k steps (2020.findings-emnlp.261.pdf, p. 2).
*   **LEGAL-BERT-SC** and **LEGAL-BERT-SMALL** were pre-trained from scratch for 1 million steps (approximately 40 epochs) (2020.findings-emnlp.261.pdf, p. 3).
*   **Parameters:** The pre-training used the Adam optimizer with a learning rate of 1e-4, a batch size of 256 samples, and a maximum sequence length of 512 sentencepiece tokens (2020.findings-emnlp.261.pdf, p. 3).
*   **Fine-tuning:** For downstream tasks, the authors recommend an "enriched grid-search" strategy that explores a broader range of hyperparameters than the original BERT guidelines, including learning rates from {1e-5, 2e-5, 3e-5, 4e-5, 5e-5}, batch sizes from {4, 8, 16, 32}, and dropout rates of 0.1 or 0.2. This approach was found to have a substantial impact on performance (2020.findings-emnlp.261.pdf, p. 3).

### Paper or other resource for more information:
The primary resource is the academic paper provided:
*   Chalkidis, I., Fergadiotis, M., Malakasiotis, P., Aletras, N., & Androutsopoulos, I. (2020). "LEGAL-BERT: The Muppets straight out of Law School." In *Findings of the Association for Computational Linguistics: EMNLP 2020* (pp. 2898-2904) (2020.findings-emnlp.261.pdf).

The paper also states that all models and code examples are available at: `https://huggingface.co/nlpaueb` (2020.findings-emnlp.261.pdf, p. 2).

### Citation details:
To cite the model, please use the following BibTeX entry from the associated paper:
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
Insufficient information.

### Contact:
Contact information for the developers can be found in the paper: `[ihalk,fergadiotis,rulller,ion]@aueb.gr` and `n.aletras@sheffield.ac.uk` (2020.findings-emnlp.261.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
LEGAL-BERT is a family of models intended to "assist legal NLP research, computational law, and legal technology applications" (2020.findings-emnlp.261.pdf, p. 1, 2). The models are specifically adapted for the legal domain, which has distinct characteristics such as specialized vocabulary and formal syntax (2020.findings-emnlp.261.pdf, p. 1).

The models were evaluated on the following downstream tasks:
*   **Legal Text Classification:** Multi-label classification of EU legislation (EURLEX57K dataset) and binary/multi-label classification of violations in European Court of Human Rights cases (ECHR-CASES dataset) (2020.findings-emnlp.261.pdf, p. 3, 6).
*   **Named Entity Recognition (NER):** Extracting specific elements (e.g., parties, dates, jurisdictions) from US contracts (CONTRACTS-NER dataset) (2020.findings-emnlp.261.pdf, p. 3, 6).

### Primary intended users:
The primary users are researchers and practitioners in the fields of legal NLP, computational law, and legal technology (2020.findings-emnlp.261.pdf, p. 2). The LEGAL-BERT-SMALL version is particularly suited for users with limited access to large computational resources (2020.findings-emnlp.261.pdf, p. 4).

### Out-of-scope uses:
The models are specialized for the English legal domain. Using them for general-purpose NLP tasks or in other specialized domains (e.g., biomedical, scientific) may lead to suboptimal performance, as the pre-training data and vocabulary are tailored to legal text (2020.findings-emnlp.261.pdf, p. 1, 2). The models were trained on English text and are not intended for use with other languages.

---

## How to Use
This section outlines how to use the model.

The paper states that all models are publicly available through the Hugging Face model hub at `https://huggingface.co/nlpaueb` (2020.findings-emnlp.261.pdf, p. 2). Users can load and use these models with the `transformers` library, similar to other BERT-based models. The repository does not include specific code snippets, but usage would follow standard practices for fine-tuning BERT models on downstream tasks.

The tokenizer uses special tokens for classification (`[CLS]`), separation (`[SEP]`), padding (`[PAD]`), unknown (`[UNK]`), and masking (`[MASK]`) (special_tokens_map.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the specific sub-domain of legal text it is applied to. The training data includes a variety of legal documents, such as legislation, court cases, and contracts (2020.findings-emnlp.261.pdf, p. 2, Table 1). The paper shows that further pre-training on a specific sub-domain (e.g., ECHR cases or US contracts) can lead to better adaptation and performance on tasks within that sub-domain compared to pre-training on the full, mixed legal corpus (2020.findings-emnlp.261.pdf, p. 4, Figure 3).

### Evaluation factors:
The model was evaluated across different types of legal documents and tasks to analyze its performance on various factors:
*   **Task Type:** Text Classification (binary and multi-label) and Named Entity Recognition (2020.findings-emnlp.261.pdf, p. 3).
*   **Data Source / Legal Area:** EU legislation (EURLEX57K), European Court of Human Rights cases (ECHR-CASES), and US contracts (CONTRACTS-NER) (2020.findings-emnlp.261.pdf, p. 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The paper uses task-specific metrics to evaluate model performance:
*   **Perplexity (PPT):** Used as a general measure to indicate how well a model variant predicts the language of a downstream task (2020.findings-emnlp.261.pdf, p. 4, Figure 4).
*   **nDCG@5:** Used for the multi-label classification task on the EURLEX57K dataset (2020.findings-emnlp.261.pdf, p. 4, Figure 4).
*   **F1 Score:** Used for the binary and multi-label classification tasks on the ECHR-CASES dataset and for the Named Entity Recognition task on all subsets of the CONTRACTS-NER dataset (2020.findings-emnlp.261.pdf, p. 4, Figure 4).

### Decision thresholds:
Insufficient information.

### Variation approaches:
The reported results for end-tasks are averages over multiple runs. To show performance variation, the result charts include vertical black lines and transparent/opaque bars indicating the minimum and maximum scores achieved across these runs (2020.findings-emnlp.261.pdf, p. 4, Figure 4 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three publicly available legal NLP datasets (2020.findings-emnlp.261.pdf, p. 6, Appendix A):
*   **EURLEX57K:** Contains 57,000 legislative documents from EURLEX, annotated with concepts from the EUROVOC thesaurus. The dataset is split into 45k training, 6k development, and 6k test documents. On average, documents are 727 words long and have approximately 5 labels each (2020.findings-emnlp.261.pdf, p. 6).
*   **ECHR-CASES:** Contains approximately 11,500 cases from the European Court of Human Rights public database. Each case includes a list of facts and is mapped to articles of the Human Rights Convention that were violated, if any. This allows for both binary (violation vs. no violation) and multi-label (which articles were violated) classification (2020.findings-emnlp.261.pdf, p. 6).
*   **CONTRACTS-NER:** Contains approximately 2,000 US contracts from the EDGAR database. Documents are annotated with multiple contract elements (e.g., title, parties, dates, governing law). The elements are organized into three groups based on their typical position in a contract: contract header, dispute resolution, and lease details (2020.findings-emnlp.261.pdf, p. 6).

### Motivation:
These datasets were chosen to provide a comprehensive evaluation of LEGAL-BERT's capabilities on a diverse set of core legal NLP tasks (text classification and named entity recognition) across different types of legal documents (legislation, case law, and contracts) (2020.findings-emnlp.261.pdf, p. 3).

### Preprocessing:
The paper states that it replicates the experimental setups from previous work (Chalkidis et al., 2019c,a,d) (2020.findings-emnlp.261.pdf, p. 3). The tokenizer configuration indicates that all input text is converted to lowercase (tokenizer_config.json.txt). For specific tasks, different model architectures were used on top of the BERT encoder:
*   **EURLEX57K:** A linear layer with sigmoid activations was placed on top of the [CLS] token representation (2020.findings-emnlp.261.pdf, p. 6).
*   **ECHR-CASES:** A hierarchical version of BERT was used, where each fact is encoded separately, followed by a self-attention mechanism to produce the final document representation (2020.findings-emnlp.261.pdf, p. 7).
*   **CONTRACTS-NER:** The final representations of all tokens in the sequence are fed to a linear Conditional Random Field (CRF) layer (2020.findings-emnlp.261.pdf, p. 7).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a 12 GB corpus of diverse English legal text collected from several publicly available resources. The components of the training data are detailed in Table 1 of the paper (2020.findings-emnlp.261.pdf, p. 2):
*   **EU legislation:** 61,826 documents (1.9 GB) from EURLEX.
*   **UK legislation:** 19,867 documents (1.4 GB) from LEGISLATION.GOV.UK.
*   **European Court of Justice (ECJ) cases:** 19,867 documents (0.6 GB) from EURLEX.
*   **European Court of Human Rights (ECHR) cases:** 12,554 documents (0.5 GB) from HUDOC.
*   **US court cases:** 164,141 documents (3.2 GB) from the Case Law Access Project.
*   **US contracts:** 76,366 documents (3.9 GB) from SEC-EDGAR.

### Motivation:
The datasets were chosen to create a comprehensive language model for the legal domain. By including text from various fields (legislation, court cases, contracts), the model is exposed to the diverse vocabulary, syntax, and semantics characteristic of legal language (2020.findings-emnlp.261.pdf, p. 1, 2).

### Preprocessing:
The paper does not provide extensive details on the preprocessing of the training data. However, the tokenizer configuration file specifies that the text was lowercased (`"do_lower_case": true`) (tokenizer_config.json.txt). For the LEGAL-BERT-SC and LEGAL-BERT-SMALL models, a new vocabulary was created from scratch based on this domain-specific corpus (2020.findings-emnlp.261.pdf, p. 1, 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Figure 4 in the paper presents the performance of all model variants across the three evaluation datasets. A star (*) indicates when a LEGAL-BERT version performs better on average than the tuned BERT-BASE.
*   **EURLEX57K (nDCG@5):** LEGAL-BERT-FP achieves the best score on the "frequent" (84.9) and "few" (62.8) label sets. All LEGAL-BERT variants show slight improvements over the tuned BERT-BASE (82.2) on the "all labels" set (82.4 for FP, 82.2 for SC, 82.0 for SMALL) (2020.findings-emnlp.261.pdf, p. 4).
*   **ECHR-CASES (F1):** On the more difficult multi-label task, LEGAL-BERT-SC performs best (59.2), showing a 2.5% absolute improvement over the tuned BERT-BASE (56.7). On the binary task, performance is more comparable, with LEGAL-BERT-SC achieving a score of 83.2 (vs. 82.6 for tuned BERT-BASE) (2020.findings-emnlp.261.pdf, p. 4).
*   **CONTRACTS-NER (F1):** LEGAL-BERT-SC achieves the highest scores on "contract header" (94.6) and "lease details" (82.6). LEGAL-BERT-FP performs best on "dispute resolution" (81.4). All LEGAL-BERT variants outperform the tuned BERT-BASE across most subsets (2020.findings-emnlp.261.pdf, p. 4).
*   **LEGAL-BERT-SMALL** is shown to be highly competitive with the larger models across most tasks, e.g., achieving 92.7 F1 on "contract header" (vs. 94.6 for SC) and 58.2 F1 on ECHR multi-label (vs. 59.2 for SC) (2020.findings-emnlp.261.pdf, p. 4).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Table 2 provides a comparison of resource efficiency on a single 11GB NVIDIA 2080TI GPU. The maximum batch size that can fit in memory gives an indication of VRAM requirements for loading and inference (2020.findings-emnlp.261.pdf, p. 7):
*   **LEGAL-BERT (Base size):** Max batch size of 6.
*   **LEGAL-BERT-SMALL:** Max batch size of 26.

### Deploying Requirements:
Inference speed on a single 11GB NVIDIA 2080TI GPU (with batch size = 1) is (2020.findings-emnlp.261.pdf, p. 7, Table 2):
*   **LEGAL-BERT (Base size):** 1.00x (baseline speed).
*   **LEGAL-BERT-SMALL:** 1.70x faster than the baseline.

### Training or Fine-tuning Requirements:
*   **Pre-training:** The models were pre-trained on v3 TPUs with 8 cores from Google Cloud Compute Services (2020.findings-emnlp.261.pdf, p. 3).
*   **Fine-tuning:** Training speed on a single 11GB NVIDIA 2080TI GPU (with max batch size) is (2020.findings-emnlp.261.pdf, p. 7, Table 2):
    *   **LEGAL-BERT (Base size):** 1.00x (baseline speed).
    *   **LEGAL-BERT-SMALL:** 4.00x faster than the baseline.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information. The paper does not include a section on ethical considerations, potential risks, or biases. The training data consists of public records such as legislation, court cases, and corporate filings, which may contain sensitive information about individuals or entities. The potential societal impact or risks associated with deploying a language model trained on this data are not discussed.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The optimal strategy for adapting BERT to a new domain (further pre-training vs. training from scratch) may vary depending on the task and dataset (2020.findings-emnlp.261.pdf, p. 5).
*   Performance gains are more significant in more challenging, domain-specific tasks (e.g., multi-label classification in ECHR-CASES, NER on contracts) where in-domain knowledge is more critical (2020.findings-emnlp.261.pdf, p. 5). In tasks that are less domain-intensive, the improvements may be less substantial (2020.findings-emnlp.261.pdf, p. 4).

### Recommendations:
*   **Hyperparameter Tuning:** The authors strongly recommend adopting an expanded grid search for fine-tuning hyperparameters, as this was shown to have a "drastic impact on performance" compared to following the minimal tuning guidelines from the original BERT paper (2020.findings-emnlp.261.pdf, p. 3, 5).
*   **Use of Smaller Models:** For users with limited computational resources, LEGAL-BERT-SMALL is a highly competitive and efficient alternative to the larger models. It is 3 times smaller but achieves comparable performance on many tasks, making it easier to adopt in low-resource settings (2020.findings-emnlp.261.pdf, p. 4, 5).
*   **Future Work:** The authors intend to explore the performance of LEGAL-BERT on more legal datasets and tasks, and to investigate further pre-training on more specific legal sub-domains (e.g., only EU legislation) (2020.findings-emnlp.261.pdf, p. 5).