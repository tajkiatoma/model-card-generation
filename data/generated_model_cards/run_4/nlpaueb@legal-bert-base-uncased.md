## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos (Chalkidis et al., 2020, p. 1).

The affiliations of the developers are:
*   Department of Informatics, Athens University of Economics and Business (Chalkidis et al., 2020, p. 1).
*   Institute of Informatics & Telecommunications, NCSR “Demokritos" (Chalkidis et al., 2020, p. 1).
*   Computer Science Department, University of Sheffield, UK (Chalkidis et al., 2020, p. 1).

### Model date:
The academic paper describing the model was published in the Findings of the Association for Computational Linguistics: EMNLP 2020, with proceedings dated November 16-20, 2020 (Chalkidis et al., 2020, p. 1).

### Model version:
The repository contains a family of models named LEGAL-BERT. The paper describes several versions (Chalkidis et al., 2020, p. 1):
*   **LEGAL-BERT-FP**: The standard BERT-BASE model further pre-trained on domain-specific legal corpora (Chalkidis et al., 2020, p. 2).
*   **LEGAL-BERT-SC**: A BERT-BASE model pre-trained from scratch on domain-specific legal corpora with a new vocabulary (Chalkidis et al., 2020, p. 2, 3).
*   **LEGAL-BERT-SMALL**: A smaller, lightweight model (6 layers, 512 hidden units, 8 attention heads) pre-trained from scratch on legal data. It is approximately 3 times smaller and 4 times faster to train than the base models (Chalkidis et al., 2020, p. 3, 5).

The provided configuration files correspond to a BERT-base architecture, suggesting it is either the LEGAL-BERT-FP or LEGAL-BERT-SC version (config.json).

### Model type:
LEGAL-BERT is a family of language models based on the BERT (Bidirectional Encoder Representations from Transformers) architecture, which utilizes a multi-layer bidirectional Transformer encoder (Chalkidis et al., 2020, p. 1; config.json). It is designed for natural language processing tasks within the legal domain.

Key architectural details for the base model version are (config.json):
*   **Model Type:** bert
*   **Architecture:** BertForPreTraining
*   **Number of Layers:** 12
*   **Hidden Size:** 768
*   **Number of Attention Heads:** 12
*   **Intermediate Size:** 3072
*   **Activation Function:** gelu
*   **Vocabulary Size:** 30522
*   **Max Context Length:** 512 positions
*   **Parameters:** 110M (Chalkidis et al., 2020, p. 3)

A smaller version, LEGAL-BERT-SMALL, is also available with 6 layers, 512 hidden units, 8 attention heads, and 35M parameters (Chalkidis et al., 2020, p. 3).

### Training details:
The LEGAL-BERT models were pre-trained on a large corpus of legal text. Two main training strategies were employed (Chalkidis et al., 2020, p. 1):
1.  **Further Pre-training (FP):** The original BERT-BASE model was adapted through additional pre-training steps on the legal corpora for up to 500k steps (Chalkidis et al., 2020, p. 2).
2.  **Pre-training from Scratch (SC):** LEGAL-BERT-SC and LEGAL-BERT-SMALL were trained from scratch on the legal corpora for 1 million steps (approximately 40 epochs). This involved creating a new vocabulary from the domain-specific text (Chalkidis et al., 2020, p. 3).

For the from-scratch training, the following parameters were used (Chalkidis et al., 2020, p. 3):
*   **Optimizer:** Adam
*   **Learning Rate:** 1e-4
*   **Batch Size:** 256 samples
*   **Sequence Length:** Up to 512 tokens

The pre-training was conducted on v3 TPUs with 8 cores (Chalkidis et al., 2020, p. 3).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Chalkidis, I., Fergadiotis, M., Malakasiotis, P., Aletras, N., & Androutsopoulos, I. (2020). LEGAL-BERT: The Muppets straight out of Law School. In *Findings of the Association for Computational Linguistics: EMNLP 2020* (pp. 2898-2904).

The paper provides a comprehensive overview of the model's development, training, and evaluation. The models and code examples are available on Hugging Face at: https://huggingface.co/nlpaueb (Chalkidis et al., 2020, p. 2, footnote 1).

### Citation details:
To cite the model, please use the following BibTeX entry (Chalkidis et al., 2020):
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

### License:
Insufficient information

### Contact:
For questions or feedback, the developers can be contacted via the following emails provided in the paper (Chalkidis et al., 2020, p. 1):
*   `[ihalk,fergadiotis,rulller,ion]@aueb.gr`
*   `n.aletras@sheffield.ac.uk`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
LEGAL-BERT is intended to assist with legal NLP research, computational law, and legal technology applications (Chalkidis et al., 2020, p. 1). It is a foundational model designed to be fine-tuned for various downstream tasks in the legal domain, where it has been shown to perform better than BERT models trained on general-domain text (Chalkidis et al., 2020, p. 1, 4).

Example applications demonstrated in the paper include:
*   **Legal Text Classification:** Large-scale, multi-label classification of EU legislation (Chalkidis et al., 2020, p. 3).
*   **Legal Judgment Prediction:** Binary and multi-label classification of violations in cases from the European Court of Human Rights (ECHR) (Chalkidis et al., 2020, p. 3).
*   **Named Entity Recognition (NER):** Extracting key elements (e.g., parties, dates, governing law) from US contracts (Chalkidis et al., 2020, p. 3).

The model takes text as input and outputs contextualized embeddings for each token, which can be used for a variety of NLP tasks.

### Primary intended users:
The primary intended users are researchers and developers working in the fields of legal NLP, computational law, and legal technology (Chalkidis et al., 2020, p. 1). The `LEGAL-BERT-SMALL` version is specifically highlighted as being useful for practitioners with limited access to large computational resources (Chalkidis et al., 2020, p. 4).

### Out-of-scope uses:
The model is specialized for the legal domain using English text. Its performance on general-domain text or other specialized domains (e.g., biomedical, scientific) is expected to be lower than models specifically trained for those areas (Chalkidis et al., 2020, p. 1). The model is not intended for use with languages other than English.

---

## How to Use
This section outlines how to use the model.

The LEGAL-BERT models are available on the Hugging Face Hub and can be used with the `transformers` library. Below is a code snippet demonstrating how to load and use the model and tokenizer.

```python
from transformers import AutoTokenizer, AutoModel

# Load tokenizer and model from Hugging Face Hub
# Replace 'nlpaueb/legal-bert-base-uncased' with other versions if needed
tokenizer = AutoTokenizer.from_pretrained('nlpaueb/legal-bert-base-uncased')
model = AutoModel.from_pretrained('nlpaueb/legal-bert-base-uncased')

# Sample legal text
text = "This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware."

# Tokenize the text
inputs = tokenizer(text, return_tensors='pt')

# Get model outputs (embeddings)
outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state
```

For fine-tuning on downstream tasks, the authors recommend an expanded hyperparameter search space beyond the standard BERT guidelines. This "enriched grid-search" was found to have a substantial impact on performance (Chalkidis et al., 2020, p. 3, 5). The recommended ranges are:
*   **Learning Rate:** {1e-5, 2e-5, 3e-5, 4e-5, 5e-5}
*   **Batch Size:** {4, 8, 16, 32} (for relatively small datasets)
*   **Dropout Rate:** {0.1, 0.2}
*   **Number of Epochs:** Use early stopping based on validation loss instead of a fixed number of epochs.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary factor influencing the model's performance is the specific sub-domain of legal text it is applied to. The model was pre-trained on a diverse corpus including legislation, court cases, and contracts (Chalkidis et al., 2020, p. 2, Table 1). Experiments show that the optimal pre-training strategy and performance gains vary depending on the downstream task's sub-domain (e.g., EU law vs. US contracts) (Chalkidis et al., 2020, p. 4, Figure 3).

### Evaluation factors:
The model was evaluated across different legal sub-domains and tasks to analyze its performance on varied legal text types. The evaluation datasets cover (Chalkidis et al., 2020, p. 3):
*   EU legislation (EURLEX57K dataset)
*   European Court of Human Rights cases (ECHR-CASES dataset)
*   US contracts (CONTRACTS-NER dataset)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to evaluate the model (Chalkidis et al., 2020, p. 4, Figure 4):
*   **Perplexity (PPT):** Used to measure how well the language model predicts the text of the downstream task datasets.
*   **nDCG@5:** Used for the multi-label classification task on the EURLEX57K dataset.
*   **F1 Score:** Used for the binary and multi-label classification tasks on the ECHR-CASES dataset, and for the named entity recognition task on the CONTRACTS-NER dataset.
*   **Training Loss:** Used to monitor performance during the pre-training phase (Chalkidis et al., 2020, p. 3, Figure 2).

### Decision thresholds:
Insufficient information

### Variation approaches:
To ensure robust measurements, the performance on downstream tasks was evaluated over multiple runs. The reported results include the average, minimum, and maximum scores across these runs, which accounts for performance variability due to random initialization (Chalkidis et al., 2020, p. 4, Figure 4).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three publicly available legal NLP datasets (Chalkidis et al., 2020, p. 3, 6):
1.  **EURLEX57K:** A dataset of 57,000 EU legislative documents for multi-label text classification. It is split into 45k training, 6k development, and 6k test documents. Documents are annotated with concepts from the EUROVOC thesaurus.
2.  **ECHR-CASES:** A dataset of approximately 11,500 cases from the European Court of Human Rights. It is used for binary classification (identifying if a violation occurred) and multi-label classification (identifying which articles were violated).
3.  **CONTRACTS-NER:** A dataset of approximately 2,000 US contracts from EDGAR for named entity recognition. It is organized into three subsets based on contract sections: contract header, dispute resolution, and lease details.

### Motivation:
These datasets were chosen to provide a comprehensive evaluation across different types of legal documents (legislation, court cases, contracts) and different NLP tasks (text classification, sequence tagging), demonstrating the model's versatility within the legal domain (Chalkidis et al., 2020, p. 3).

### Preprocessing:
The paper states that for evaluation, they replicate the experimental setups from previous work (Chalkidis et al., 2019c,a,d) (Chalkidis et al., 2020, p. 3). This involves using the model's specific tokenizer to process the text. For the ECHR-CASES task, a hierarchical model structure is used where each fact in a case is encoded independently. For the CONTRACTS-NER task, the final representations of tokens are fed to a linear CRF layer (Chalkidis et al., 2020, p. 7).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a 12 GB corpus of diverse English legal text collected from several publicly available sources. The composition of the training data is as follows (Chalkidis et al., 2020, p. 2, Table 1):
*   **EU legislation:** 1.9 GB from EUR-Lex.
*   **UK legislation:** 1.4 GB from legislation.gov.uk.
*   **European Court of Justice (ECJ) cases:** 0.6 GB from EUR-Lex.
*   **European Court of Human Rights (ECHR) cases:** 0.5 GB from HUDOC.
*   **US court cases:** 3.2 GB from the Case Law Access Project.
*   **US contracts:** 3.9 GB from SEC EDGAR.

### Motivation:
The training data was chosen to create a language model specifically adapted to the legal domain. Legal text has distinct characteristics, such as specialized vocabulary and formal syntax, which differ significantly from the general-domain text (e.g., Wikipedia) used to train standard BERT models. The diverse collection of sources ensures the model is exposed to various facets of legal language (Chalkidis et al., 2020, p. 1, 2).

### Preprocessing:
For the models trained from scratch (LEGAL-BERT-SC and LEGAL-BERT-SMALL), a new SentencePiece vocabulary was created from the 12 GB legal corpus. For the model that was further pre-trained (LEGAL-BERT-FP), the original BERT-BASE tokenizer was used (Chalkidis et al., 2020, p. 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the LEGAL-BERT family of models compared to a tuned BERT-BASE baseline is presented in Figure 4 of the paper (Chalkidis et al., 2020, p. 4). The results are broken down by dataset and sub-task.

*   **EURLEX57K (nDCG@5):** LEGAL-BERT-FP achieves a score of 82.4 on all labels, compared to 82.2 for the tuned BERT-BASE.
*   **ECHR-CASES (F1 Score):**
    *   Binary Classification: LEGAL-BERT-SC achieves 83.2, compared to 82.6 for the tuned BERT-BASE.
    *   Multi-Label Classification: LEGAL-BERT-SC achieves 58.6, a more substantial improvement over the 56.7 of the tuned BERT-BASE.
*   **CONTRACTS-NER (F1 Score):**
    *   Contract Header: LEGAL-BERT-SC achieves 94.6, compared to 92.4 for the tuned BERT-BASE.
    *   Dispute Resolution: LEGAL-BERT-FP achieves 81.4, compared to 79.8 for the tuned BERT-BASE.
    *   Lease Details: LEGAL-BERT-SC achieves 82.6, compared to 81.5 for the tuned BERT-BASE.

Impressively, LEGAL-BERT-SMALL is shown to be competitive with the larger models across most tasks (Chalkidis et al., 2020, p. 4).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The resource efficiency of the models was benchmarked on a single 11GB NVIDIA-2080TI GPU. The maximum batch size that can be loaded for training/inference gives an indication of memory requirements (Chalkidis et al., 2020, p. 7, Table 2):
*   **LEGAL-BERT (base size):** Max batch size of 6.
*   **LEGAL-BERT-SMALL:** Max batch size of 26.

### Deploying Requirements:
Inference speed was benchmarked relative to BERT-BASE on a 2080TI GPU (Chalkidis et al., 2020, p. 7, Table 2):
*   **LEGAL-BERT (base size):** 1.00x (baseline speed).
*   **LEGAL-BERT-SMALL:** 1.70x faster than the base model.

### Training or Fine-tuning Requirements:
The pre-training was performed on Google Cloud TPUs (v3-8) (Chalkidis et al., 2020, p. 3). Fine-tuning can be performed on consumer-grade GPUs. The training speed of LEGAL-BERT-SMALL is approximately 4 times faster than the base-sized model on a 2080TI GPU (Chalkidis et al., 2020, p. 3, 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The training data consists of publicly available legal documents, including legislation, court cases, and contracts (Chalkidis et al., 2020, p. 2, Table 1). While these documents can contain sensitive information, the sources they are drawn from (e.g., HUDOC, EDGAR) are official repositories that often have procedures for anonymization or redaction. The paper does not explicitly discuss the use of sensitive data or any steps taken to further anonymize it.

A potential risk is that the model may learn and perpetuate existing biases present in the legal system. For example, if the training data reflects historical biases in judicial decisions, a model fine-tuned for judgment prediction could replicate those biases. The paper does not address this risk or describe any mitigation strategies. Users should be aware of this potential for bias amplification when deploying the model in sensitive applications.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model is specialized for the English legal domain and is not expected to perform well on other languages or non-legal domains (Chalkidis et al., 2020, p. 1).
*   The performance gains over a general-domain BERT model vary by task. While significant improvements are seen in more complex tasks (e.g., multi-label classification on ECHR cases, NER on contracts), the gains are less substantial on others (e.g., classification on EURLEX) (Chalkidis et al., 2020, p. 4).
*   The optimal strategy for adapting BERT to a new domain (further pre-training vs. training from scratch) may vary, and there is no one-size-fits-all solution (Chalkidis et al., 2020, p. 5).

### Recommendations:
*   **Hyperparameter Tuning:** It is strongly recommended to perform an expanded grid search for hyperparameters when fine-tuning the model for downstream tasks. This was shown to have a significant impact on performance (Chalkidis et al., 2020, p. 5).
*   **Use of Smaller Model:** For users with limited computational resources, `LEGAL-BERT-SMALL` is a highly competitive and much more efficient alternative to the larger models (Chalkidis et al., 2020, p. 5).
*   **Future Research:** The authors suggest that the model's performance should be explored on a wider range of legal datasets and tasks (Chalkidis et al., 2020, p. 5).