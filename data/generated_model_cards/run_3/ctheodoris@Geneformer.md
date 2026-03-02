## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Christina Theodoris (setup.py). The provided contact email, christina.theodoris@gladstone.ucsf.edu, suggests an affiliation with the Gladstone Institutes and/or the University of California, San Francisco (UCSF) (setup.py).

### Model date:
Insufficient information

### Model version:
The model version is 0.1.0 (setup.py). There is no information available about how it differs from other versions.

### Model type:
Geneformer is a transformer model based on the BERT (Bidirectional Encoder Representations from Transformers) architecture (setup.py, config.json). It is designed for masked language modeling (`BertForMaskedLM`) (config.json). The model was pretrained on a large-scale corpus of single-cell transcriptomes for applications in network biology (setup.py).

Key architectural details include:
*   **Model Type:** bert (config.json)
*   **Number of Hidden Layers:** 12 (config.json)
*   **Hidden Size:** 512 (config.json)
*   **Number of Attention Heads:** 8 (config.json)
*   **Intermediate Size:** 1024 (config.json)
*   **Activation Function:** relu (config.json)
*   **Vocabulary Size:** 20,275 (config.json)
*   **Maximum Position Embeddings (Context Length):** 4,096 (config.json)
*   **Position Embedding Type:** absolute (config.json)
*   **Type Vocabulary Size:** 2 (config.json)

### Training details:
The model was pretrained on a large-scale corpus of single-cell transcriptomes (setup.py).

Key training-related parameters from the model configuration are:
*   **Attention Probabilities Dropout:** 0.02 (config.json)
*   **Hidden Layer Dropout:** 0.02 (config.json)
*   **Initializer Range:** 0.02 (config.json)
*   **Layer Norm Epsilon:** 1e-12 (config.json)
*   **Torch Data Type:** float32 (config.json)

No other information is available regarding the training algorithm, fairness constraints, or optimization techniques.

### Paper or other resource for more information:
Insufficient information

### Citation details:
Insufficient information

### License:
Insufficient information

### Contact:
For questions or feedback, contact Christina Theodoris at christina.theodoris@gladstone.ucsf.edu (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Geneformer is intended to "enable context-aware predictions in settings with limited data in network biology" (setup.py). It is pretrained on single-cell transcriptomes, suggesting its use in analyzing and making predictions from gene expression data (setup.py).

### Primary intended users:
Insufficient information

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information

### Evaluation factors:
Insufficient information

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
Insufficient information

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Insufficient information

### Motivation:
Insufficient information

### Preprocessing:
Insufficient information

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was "pretrained on a large-scale corpus of single cell transcriptomes" (setup.py). No further details about the size, source, or composition of this corpus are provided. The repository includes several dictionary files which may relate to the training data tokens, such as `gene_median_dictionary_gc95M.pkl`, `gene_name_id_dict_gc95M.pkl`, `ensembl_mapping_dict_gc95M.pkl`, and `token_dictionary_gc95M.pkl` (MANIFEST.in).

### Motivation:
Insufficient information

### Preprocessing:
Insufficient information

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Insufficient information

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
Insufficient information

---