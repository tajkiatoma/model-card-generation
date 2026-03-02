## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
Insufficient information

### Model date:
Insufficient information

### Model version:
The model is referred to as "M3-Embedding" and has several variants that produce different types of embeddings (Source: `long.jpg`, `imgs/miracl.jpg`, `imgs/nqa.jpg`):
*   **Dense**: Produces dense embeddings.
*   **Sparse**: Produces sparse embeddings.
*   **Multi-vec**: Produces multi-vector embeddings.
*   **Dense+Sparse**: A combination of dense and sparse embeddings.
*   **All**: A combination of all three embedding types, which consistently achieves the highest performance across evaluation benchmarks (Source: `long.jpg`, `imgs/miracl.jpg`, `imgs/nqa.jpg`).

Ablation versions are also mentioned, such as "Dense-w.o.long" (Dense model without long document training) and "Dense-w.o.long (MCLS)" (Source: `long.jpg`).

### Model type:
*   **Architecture**: The model is based on the XLM-RoBERTa architecture (Source: `config.json.txt`). It is structured as a sentence-transformer model composed of three main modules: a Transformer base, a Pooling layer, and a Normalize layer (Source: `modules.json.txt`).
*   **Category**: It is a text embedding model designed for multilingual and long-document information retrieval (Source: `imgs/miracl.jpg`, `imgs/long.jpg`).
*   **Size and Parameters**:
    *   **Hidden Size**: 1024 (Source: `config.json.txt`)
    *   **Number of Hidden Layers**: 24 (Source: `config.json.txt`)
    *   **Number of Attention Heads**: 16 (Source: `config.json.txt`)
    *   **Intermediate Size**: 4096 (Source: `config.json.txt`)
    *   **Vocabulary Size**: 250002 (Source: `config.json.txt`)
    *   **Embedding Dimension**: 1024 (Source: `1_Pooling/config.json.txt`)
*   **Context Length**: The model supports a maximum sequence length of 8192 tokens (Source: `sentence_bert_config.json.txt`, `tokenizer_config.json.txt`). The maximum position embeddings are set to 8194 (Source: `config.json.txt`).

### Training details:
The model's pooling strategy is configured to use the classification (CLS) token's output for sentence embeddings (`pooling_mode_cls_token` is set to `true`), while other pooling modes like mean or max pooling are disabled (Source: `1_Pooling/config.json.txt`). The existence of model variants like "Dense-w.o.long" suggests that training on long documents was a specific part of the training process for the final model (Source: `long.jpg`). No other details on training algorithms, hyperparameters, or optimization techniques are available.

### Paper or other resource for more information:
Insufficient information

### Citation details:
Insufficient information

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The M3-Embedding model is designed to generate text embeddings for information retrieval tasks. Its primary capabilities include:
*   **Multilingual Retrieval**: The model is evaluated on its ability to perform retrieval across a wide range of languages (Source: `imgs/miracl.jpg`).
*   **Cross-lingual Retrieval**: It is benchmarked on tasks where the query language may differ from the document language (Source: `imgs/mkqa.jpg`).
*   **Long-Document Retrieval**: The model is specifically designed to handle long documents, with a context length of 8192 tokens, and is evaluated on long-document retrieval datasets like MLDR and NarrativeQA (Source: `imgs/long.jpg`, `imgs/nqa.jpg`).

The model can output dense, sparse, and multi-vector embeddings, which can be used individually or combined to enhance retrieval performance (Source: `long.jpg`).

### Primary intended users:
The primary intended users are likely researchers and developers in the fields of Natural Language Processing (NLP) and Information Retrieval (IR) who require robust text embeddings for building search and retrieval systems, especially those that operate in multilingual or long-document contexts.

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses the `XLMRobertaTokenizer` (Source: `tokenizer_config.json.txt`). It processes text inputs up to a maximum length of 8192 tokens (Source: `sentence_bert_config.json.txt`). The tokenizer does not perform lower-casing (`do_lower_case` is `false`) (Source: `sentence_bert_config.json.txt`).

The model's special tokens are defined as follows (Source: `special_tokens_map.json.txt`):
*   `<s>`: `bos_token`, `cls_token`
*   `</s>`: `eos_token`, `sep_token`
*   `<pad>`: `pad_token`
*   `<mask>`: `mask_token`
*   `<unk>`: `unk_token`

No code snippets or detailed usage instructions are available in the repository.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language**: The model's performance is highly dependent on the language of the text. It has been evaluated across dozens of languages, showing significant performance variation among them (Source: `imgs/miracl.jpg`, `imgs/mkqa.jpg`, `long.jpg`).
*   **Document Length**: The model is specifically designed for long documents, and its performance on such tasks is a key evaluation point (Source: `imgs/long.jpg`, `imgs/nqa.jpg`).

### Evaluation factors:
The provided evaluations are disaggregated by **language**, with performance metrics reported for each language individually on the MIRACL, MKQA, and MLDR datasets (Source: `imgs/miracl.jpg`, `imgs/mkqa.jpg`, `long.jpg`).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using the following standard information retrieval metrics:
*   **nDCG@10 (Normalized Discounted Cumulative Gain at 10)**: Used for evaluating performance on the MIRACL, MLDR, and NarrativeQA datasets (Source: `imgs/miracl.jpg`, `long.jpg`, `imgs/nqa.jpg`).
*   **Recall@100**: Used for evaluating performance on the MKQA dataset (Source: `imgs/mkqa.jpg`).
*   **MRR (Mean Reciprocal Rank)**: Used in a comparative evaluation against other models (Source: `imgs/others.webp`).

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on the following publicly known datasets:
*   **MIRACL dev set**: For multilingual retrieval (Source: `imgs/miracl.jpg`).
*   **MLDR test set**: For multilingual long-document retrieval (Source: `long.jpg`).
*   **MKQA**: For cross-lingual retrieval (Source: `imgs/mkqa.jpg`).
*   **NarrativeQA**: For long-document retrieval (Source: `imgs/nqa.jpg`).

### Motivation:
The datasets were chosen to comprehensively evaluate the model's core intended uses: MIRACL and MKQA assess its multilingual and cross-lingual capabilities, while MLDR and NarrativeQA test its effectiveness in handling long documents (Source: `imgs/miracl.jpg`, `imgs/mkqa.jpg`, `long.jpg`, `imgs/nqa.jpg`).

### Preprocessing:
The text was tokenized using an XLM-R tokenizer (Source: `imgs/bm25.jpg`). The tokenizer is configured not to convert text to lowercase (Source: `sentence_bert_config.json.txt`). No other preprocessing steps are described.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Insufficient information

### Motivation:
Insufficient information

### Preprocessing:
Insufficient information

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance of the "All" variant of M3-Embedding is reported across various languages and datasets.

**MIRACL dev set (nDCG@10)** (Source: `imgs/miracl.jpg`):
*   **Avg**: 71.5
*   **ar**: 80.2
*   **bn**: 59.6
*   **en**: 81.5
*   **es**: 59.7
*   **fa**: 63.4
*   **fi**: 80.4
*   **fr**: 61.2
*   **hi**: 63.3
*   **id**: 59.0
*   **ja**: 75.2
*   **ko**: 72.1
*   **ru**: 71.7
*   **sw**: 79.6
*   **te**: 88.1
*   **th**: 83.7
*   **zh**: 64.9
*   **de**: 59.8
*   **yo**: 83.5

**MLDR test set (nDCG@10)** (Source: `long.jpg`):
*   **Avg**: 65.0
*   **ar**: 64.7
*   **de**: 57.9
*   **en**: 86.8
*   **es**: 83.9
*   **fr**: 52.2
*   **hi**: 75.5
*   **it**: 60.1
*   **ja**: 55.7
*   **ko**: 85.4
*   **pt**: 73.8
*   **ru**: 44.7
*   **th**: 40.0

**MKQA (Recall@100)** (Source: `imgs/mkqa.jpg`):
*   **Avg**: 75.5
*   **ar**: 71.5
*   **da**: 76.3
*   **de**: 76.9
*   **es**: 75.5
*   **fi**: 75.3
*   **fr**: 72.5
*   **he**: 73.0
*   **hu**: 76.5
*   **it**: 75.0
*   **ja**: 68.8
*   **km**: 69.2
*   **ko**: 75.2
*   **ms**: 77.4
*   **nl**: 77.4
*   **no**: 77.2
*   **pl**: 76.4
*   **pt**: 76.5
*   **ru**: 73.6
*   **sv**: 76.6
*   **th**: 76.0
*   **tr**: 76.6
*   **vi**: 76.8
*   **zh_cn**: 75.0
*   **zh_hk**: 74.3
*   **zh_tw**: 73.6

**NarrativeQA (nDCG@10)** (Source: `imgs/nqa.jpg`):
*   **All**: 61.7

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
*   **Performance Disparity Across Languages**: The model exhibits significant performance variation between different languages. For example, on the MLDR dataset, the nDCG@10 score for English is 86.8, while for Chinese it is 40.0 (Source: `long.jpg`). Similarly, on MIRACL, the score for Swedish is 88.1, while for Bengali it is 59.6 (Source: `imgs/miracl.jpg`). Users should be aware of these disparities when applying the model to low-resource or less-represented languages in the evaluation sets.

### Recommendations:
Insufficient information