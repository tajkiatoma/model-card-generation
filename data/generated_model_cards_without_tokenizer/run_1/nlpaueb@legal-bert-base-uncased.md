## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, and Ion Androutsopoulos. The developers are affiliated with the following institutions (2020.findings-emnlp.261.pdf, p. 1):
*   Department of Informatics, Athens University of Economics and Business
*   Institute of Informatics & Telecommunications, NCSR “Demokritos”
*   Computer Science Department, University of Sheffield, UK

### Model date:
The paper introducing the model was published in the Findings of the Association for Computational Linguistics: EMNLP 2020, which took place from November 16-20, 2020 (2020.findings-emnlp.261.pdf, p. 1).

### Model version:
The repository releases LEGAL-BERT, which is a family of BERT models. The versions described are (2020.findings-emnlp.261.pdf, p. 1-2):
*   **LEGAL-BERT-FP (Further Pre-train):** This version takes the original BERT-BASE model and continues pre-training on a domain-specific legal corpus.
*   **LEGAL-BERT-SC (Scratch):** This version is pre-trained from scratch on a domain-specific legal corpus with a new vocabulary of sub-word units. It has the same architecture as BERT-BASE (12 layers, 768 hidden units, 12 attention heads, 110M parameters) (2020.findings-emnlp.261.pdf, p. 3).
*   **LEGAL-BERT-SMALL:** A substantially smaller model pre-trained from scratch on legal data. It has 6 layers, 512 hidden units, and 8 attention heads (35M parameters), making it approximately 4 times faster to train than BERT-BASE (2020.findings-emnlp.261.pdf, p. 3).

### Model type:
LEGAL-BERT is a family of models based on the BERT (Bidirectional Encoder Representations from Transformers) architecture, designed for the legal domain (2020.findings-emnlp.261.pdf, p. 1).

The specific configuration for the base version (LEGAL-BERT-SC) is a `BertForPreTraining` model with the following architectural details (config.json.txt; 2020.findings-emnlp.261.pdf, p. 3):
*   **Model Type:** `bert`
*   **Architecture:** Transformer-based
*   **Hidden Size:** 768
*   **Number of Hidden Layers:** 12
*   **Number of Attention Heads:** 12
*   **Intermediate Size:** 3072
*   **Hidden Activation Function:** `gelu`
*   **Attention Probabilities Dropout Probability:** 0.1
*   **Hidden Dropout Probability:** 0.1
*   **Vocabulary Size:** 30,522
*   **Max Position Embeddings (Context Length):** 512

The LEGAL-BERT-SMALL version has 6 layers, 512 hidden units, and 8 attention heads, with 35M parameters (2020.findings-emnlp.261.pdf, p. 3).

### Training details:
**Pre-training:**
The models were pre-trained using the official BERT code (2020.findings-emnlp.261.pdf, p. 3). The pre-training process for LEGAL-BERT involved the following (2020.findings-emnlp.261.pdf, p. 3):
*   **Steps:** 1 million steps (approximately 40 epochs) over all corpora.
*   **Batch Size:** 256 samples.
*   **Sequence Length:** Up to 512 sentencepiece tokens.
*   **Optimizer:** Adam.
*   **Learning Rate:** 1e-4.

**Fine-tuning:**
For fine-tuning on downstream tasks, the authors proposed an enriched hyper-parameter grid search strategy, as the default suggestions from the original BERT paper were found to be suboptimal. The expanded search space includes (2020.findings-emnlp.261.pdf, p. 3):
*   **Learning Rate:** {1e-5, 2e-5, 3e-5, 4e-5, 5e-5}
*   **Batch Size:** {4, 8, 16, 32}
*   **Dropout Rate:** {0.1, 0.2}
*   **Epochs:** Early stopping based on validation loss was used, without a fixed maximum number of epochs.

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Ilias Chalkidis, Manos Fergadiotis, Prodromos Malakasiotis, Nikolaos Aletras, Ion Androutsopoulos. 2020. *LEGAL-BERT: The Muppets straight out of Law School*. In Findings of the Association for Computational Linguistics: EMNLP 2020. (2020.findings-emnlp.261.pdf)

The models and code examples are available at:
*   https://huggingface.co/nlpaueb (2020.findings-emnlp.261.pdf, p. 2, footnote 1)

### Citation details:
The BibTeX format for citing the work is not explicitly provided in the paper, but can be constructed from the paper's details. A standard citation would be:
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
(2020.findings-emnlp.261.pdf, p. 1)

### License:
Insufficient information.

### Contact:
Contact can be made with the authors via the emails provided in the paper (2020.findings-emnlp.261.pdf, p. 1):
*   `[ihalk,fergadiotis,rulller,ion]@aueb.gr`
*   `n.aletras@sheffield.ac.uk`

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
LEGAL-BERT is a family of models intended to assist legal NLP research, computational law, and legal technology applications (2020.findings-emnlp.261.pdf, p. 1). The models are designed for transfer learning on downstream legal tasks. The paper demonstrates their capabilities on (2020.findings-emnlp.261.pdf, p. 3):
*   **Text Classification:** Including large-scale multi-label classification (e.g., assigning concepts to EU laws) and binary/multi-label classification (e.g., predicting violations in court cases).
*   **Sequence Tagging:** Specifically for Named Entity Recognition (NER) on legal contracts to extract elements like parties, dates, and jurisdictions.

The input is legal text, and the output is task-specific (e.g., class labels for classification, entity tags for NER).

### Primary intended users:
The primary intended users are researchers and practitioners in the fields of legal NLP, computational law, and legal technology (2020.findings-emnlp.261.pdf, p. 2). The LEGAL-BERT-SMALL version is specifically highlighted as being important for users with limited access to large computational resources (2020.findings-emnlp.261.pdf, p. 4).

### Out-of-scope uses:
The models are pre-trained specifically on English legal text. Therefore, their use on non-legal text or text in other languages is out-of-scope, as they would likely underperform compared to models trained on general-domain corpora (2020.findings-emnlp.261.pdf, p. 1). The paper does not list other specific out-of-scope uses.

---

## How to Use
This section outlines how to use the model.

All models and code examples are available at https://huggingface.co/nlpaueb (2020.findings-emnlp.261.pdf, p. 2, footnote 1).

The model should be fine-tuned on a downstream task. The paper provides implementation details for the three evaluation tasks (2020.findings-emnlp.261.pdf, p. 6-7, Appendix B):
*   **EURLEX57K (Multi-label Text Classification):** A linear layer with sigmoid activations is placed on top of the final `[CLS]` token representation from LEGAL-BERT.
*   **ECHR-CASES (Binary/Multi-label Text Classification):** A hierarchical version of BERT is used. A shared LEGAL-BERT model encodes each fact of a case independently, producing N fact embeddings. A self-attention mechanism is applied over these embeddings to produce a final document representation, which is then fed to a linear layer with softmax activation.
*   **CONTRACTS-NER (Named Entity Recognition):** The final representations for all tokens in the input sequence are fed to a linear Conditional Random Fields (CRF) layer to predict the entity tags.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The primary factor investigated is the **domain of the text**. The model's performance is heavily influenced by whether the text is from the legal domain or a general domain. Within the legal domain, performance can also vary across different **sub-domains**, such as EU legislation, European Court of Human Rights (ECHR) cases, and US contracts (2020.findings-emnlp.261.pdf, p. 4).

### Evaluation factors:
The evaluation is disaggregated by legal sub-domain and task type. The factors analyzed are the different datasets, which represent distinct areas of law and NLP tasks (2020.findings-emnlp.261.pdf, p. 4, Figure 4):
*   EURLEX57K (EU legislation)
*   ECHR-CASES (Human rights case law)
*   CONTRACTS-NER (US contracts)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to assess model performance on downstream tasks (2020.findings-emnlp.261.pdf, p. 4, Figure 4):
*   **Perplexity (PPT):** Used to indicate how well a model variant predicts the language of an end-task.
*   **nDCG@5:** Used for the multi-label text classification task on the EURLEX57K dataset.
*   **F1 Score:** Used for the binary/multi-label classification task on ECHR-CASES and for the named entity recognition task on CONTRACTS-NER.

### Decision thresholds:
Insufficient information.

### Variation approaches:
The reported results for downstream tasks are averages over multiple runs. The minimum and maximum scores from these runs are also indicated graphically in the results charts to show performance variation (2020.findings-emnlp.261.pdf, p. 4, Figure 4 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three legal NLP datasets (2020.findings-emnlp.261.pdf, p. 6, Appendix A):
1.  **EURLEX57K:** Contains 57k legislative documents from EURLEX, the official online repository for EU law. Documents are annotated with concepts from the EUROVOC thesaurus. The dataset is split into 45k training, 6k development, and 6k test documents.
2.  **ECHR-CASES:** Contains approximately 11.5k cases from the public database of the European Court of Human Rights. Each case includes a list of facts and is mapped to articles of the Human Rights Convention that were violated (if any). It is used for both binary (violation vs. no violation) and multi-label (which articles were violated) classification.
3.  **CONTRACTS-NER:** Contains approximately 2k US contracts from the EDGAR database. Contracts are annotated for multiple elements (e.g., title, parties, dates, governing law) organized into three groups based on their position: contract header, dispute resolution, and lease details.

### Motivation:
These datasets were chosen to evaluate the model's performance on a diverse set of downstream tasks (multi-label text classification, sequence tagging) within the legal domain (2020.findings-emnlp.261.pdf, p. 3).

### Preprocessing:
The paper states that for fine-tuning, it replicates the experiments of previous works (Chalkidis et al., 2019c,a,d), implying that the preprocessing steps from those works were followed (2020.findings-emnlp.261.pdf, p. 3, 6-7). Specific preprocessing steps for the evaluation data are not detailed in the paper.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
To pre-train the LEGAL-BERT models, a corpus of 12 GB of diverse English legal text was collected from publicly available resources. The composition of this corpus is as follows (2020.findings-emnlp.261.pdf, p. 2, Table 1):
*   **EU legislation:** 61,826 documents (1.9 GB) from EURLEX.
*   **UK legislation:** 19,867 documents (1.4 GB) from legislation.gov.uk.
*   **European Court of Justice (ECJ) cases:** 19,867 documents (0.6 GB) from EURLEX.
*   **European Court of Human Rights (ECHR) cases:** 12,554 documents (0.5 GB) from HUDOC.
*   **US court cases:** 164,141 documents (3.2 GB) from the Case Law Access Project.
*   **US contracts:** 76,366 documents (3.9 GB) from SEC-EDGAR.

All repositories have open access, except for the Case Law Access Project, where access is granted to researchers upon request (2020.findings-emnlp.261.pdf, p. 2, Table 1).

### Motivation:
The training data was chosen to create a language model specialized for the legal domain. Legal text has distinct characteristics (specialized vocabulary, formal syntax, domain-specific semantics) compared to the generic corpora (e.g., Wikipedia) used to train standard BERT, which has been shown to underperform in specialized domains (2020.findings-emnlp.261.pdf, p. 1).

### Preprocessing:
For the LEGAL-BERT-SC and LEGAL-BERT-SMALL models, a new vocabulary of 30k sub-words was created from the legal corpora using Google's sentencepiece library (2020.findings-emnlp.261.pdf, p. 3). During training, text was tokenized into sequences of up to 512 sentencepiece tokens (2020.findings-emnlp.261.pdf, p. 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance was analyzed for each dataset and task separately. Key findings include (2020.findings-emnlp.261.pdf, p. 4):
*   **General:** In all three datasets, a LEGAL-BERT variant almost always leads to better results than the tuned BERT-BASE.
*   **EURLEX57K:** Improvements are less substantial (0.2% in nDCG@5), which corresponds to a small drop in perplexity.
*   **ECHR-CASES:** A small improvement (0.8%) is seen on the binary classification task, but a more substantial improvement (2.5%) is observed on the more difficult multi-label task, indicating that LEGAL-BERT benefits from in-domain knowledge.
*   **CONTRACTS-NER:** The largest drop in perplexity is observed here, which is reflected in F1 score increases of 1.8% (contract header), 1.6% (dispute resolution), and 1.1% (lease details).
*   **LEGAL-BERT-SMALL:** This smaller model is impressively comparable to the larger LEGAL-BERT models across most datasets.

### Intersectional results:
The paper analyzes performance across different legal sub-domains (represented by the datasets). It finds that the optimal strategy for further pre-training (LEGAL-BERT-FP) varies across datasets. For instance, adapting the model on specific sub-domains (like ECHR cases or US contracts) leads to faster and better adaptation compared to using the full collection of legal corpora (2020.findings-emnlp.261.pdf, p. 4). No intersectional analysis across demographic or other social factors was performed.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Inference speed was benchmarked on a single 11GB NVIDIA-2080TI GPU. Compared to BERT-BASE, LEGAL-BERT has the same inference speed, while LEGAL-BERT-SMALL is 1.7 times faster (2020.findings-emnlp.261.pdf, p. 7, Table 2). The paper notes that LEGAL-BERT-SMALL "can fit in most modern GPU cards" (2020.findings-emnlp.261.pdf, p. 4).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The models were pre-trained using v3 TPUs with 8 cores from Google Cloud Compute Services (2020.findings-emnlp.261.pdf, p. 3).
*   **Fine-tuning:** Training speed was benchmarked on a single 11GB NVIDIA-2080TI GPU. With maximum batch size, LEGAL-BERT-SMALL trains 4 times faster than LEGAL-BERT-BASE, while LEGAL-BERT-BASE has the same training speed as the original BERT-BASE (2020.findings-emnlp.261.pdf, p. 7, Table 2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information. The paper does not include a section on ethical considerations, potential risks, or biases. The data used for training and evaluation consists of publicly available legal documents such as legislation and court cases (2020.findings-emnlp.261.pdf, p. 2, Table 1).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The best strategy for adapting BERT to a new domain (further pre-training vs. training from scratch) may vary depending on the specific domain and tasks (2020.findings-emnlp.261.pdf, p. 5).
*   Performance gains from using a domain-specific model like LEGAL-BERT are stronger in more challenging and domain-specific tasks (e.g., multi-label classification in ECHR-CASES, NER in CONTRACTS-NER) (2020.findings-emnlp.261.pdf, p. 5).

### Recommendations:
*   Users should always adopt an expanded hyper-parameter grid search when fine-tuning BERT for end-tasks, as it can have a drastic impact on performance (2020.findings-emnlp.261.pdf, p. 5).
*   Smaller, specialized models like LEGAL-BERT-SMALL should be considered, as they can be highly competitive with larger models while being more efficient and accessible for users with limited computational resources (2020.findings-emnlp.261.pdf, p. 5).
*   The authors plan to explore the performance of LEGAL-BERT in more legal datasets and tasks in future work (2020.findings-emnlp.261.pdf, p. 5).