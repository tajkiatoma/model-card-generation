## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The primary author of the Geneformer package is Christina Theodoris (docs/source/conf.py, setup.py). The associated manuscripts list Christina V. Theodoris, L. Xiao, A. Chopra, M. D. Chaffin, Z. R. Al Sayed, M. C. Hill, H. Mantineo, E. Brydon, Z. Zeng, X. S. Liu, and P. T. Ellinor as authors for the first paper, and H. Chen, M. S. Venkatesh, J. Gomez Ortega, S. V. Mahesh, T. Nandi, R. Madduri, K. Pelka, and C. V. Theodoris for the second (docs/source/about.rst.txt). Christina Theodoris's contact email is provided as christina.theodoris@gladstone.ucsf.edu (setup.py).

### Model date:
The original 6-layer and 12-layer Geneformer models were pretrained in June 2021. An expanded model was trained in April 2024 (docs/source/about.rst.txt). The package version is listed as 0.1.0 (setup.py, docs/source/conf.py).

### Model version:
The repository contains several versions of the Geneformer model (docs/source/about.rst.txt):
*   **6-layer Geneformer (gf-6L-30M-i2048):** The original model pretrained on Genecorpus-30M. It has 6 hidden layers, a hidden size of 256, 4 attention heads, and a max input size of 2048 (docs/source/about.rst.txt, gf-6L-30M-i2048/config.json.txt).
*   **12-layer Geneformer (gf-12L-30M-i2048):** A scaled-up version with retained width:depth aspect ratio, also pretrained on Genecorpus-30M. It has 12 hidden layers, a hidden size of 512, 8 attention heads, and a max input size of 2048 (docs/source/about.rst.txt, gf-12L-30M-i2048/config.json.txt).
*   **Expanded 12-layer Geneformer (gf-12L-95M-i4096):** An expanded model trained on approximately 95 million transcriptomes. It has 12 hidden layers, a hidden size of 512, 8 attention heads, and a max input size of 4096 (docs/source/about.rst.txt, gf-12L-95M-i4096/config.json.txt).
*   **Expanded 20-layer Geneformer (gf-20L-95M-i4096):** A larger version with 20 hidden layers, a hidden size of 896, 14 attention heads, and a max input size of 4096 (gf-20L-95M-i4096/config.json.txt).

There is also a fine-tuned version for cancer cell line classification mentioned: `gf-12L-95M-i4096_CLcancer` (gf-12L-95M-i4096_CLcancer/config.json.txt).

### Model type:
Geneformer is a transformer-based deep learning model designed for network biology (setup.py, docs/source/about.rst.txt).

**Architecture:** The models are based on the BERT architecture for masked language modeling (`BertForMaskedLM`) (config.json.txt, gf-6L-30M-i2048/config.json.txt, gf-12L-30M-i2048/config.json.txt, gf-12L-95M-i4096/config.json.txt, gf-20L-95M-i4096/config.json.txt). The core components include multiple hidden layers, multi-head attention, and a ReLU activation function (`"hidden_act": "relu"`) (config.json.txt).

**Model Variants and Specifications:**
*   **gf-6L-30M-i2048:**
    *   Layers: 6 (`num_hidden_layers`)
    *   Embedding Dimensions: 256 (`hidden_size`)
    *   Attention Heads: 4 (`num_attention_heads`)
    *   Max Input Size: 2048 (`max_position_embeddings`)
    *   Vocabulary Size: 25,426 (`vocab_size`)
    *   (Source: gf-6L-30M-i2048/config.json.txt)
*   **gf-12L-30M-i2048:**
    *   Layers: 12 (`num_hidden_layers`)
    *   Embedding Dimensions: 512 (`hidden_size`)
    *   Attention Heads: 8 (`num_attention_heads`)
    *   Max Input Size: 2048 (`max_position_embeddings`)
    *   Vocabulary Size: 25,426 (`vocab_size`)
    *   (Source: gf-12L-30M-i2048/config.json.txt)
*   **gf-12L-95M-i4096:**
    *   Layers: 12 (`num_hidden_layers`)
    *   Embedding Dimensions: 512 (`hidden_size`)
    *   Attention Heads: 8 (`num_attention_heads`)
    *   Max Input Size: 4096 (`max_position_embeddings`)
    *   Vocabulary Size: 20,275 (`vocab_size`)
    *   (Source: gf-12L-95M-i4096/config.json.txt)
*   **gf-20L-95M-i4096:**
    *   Layers: 20 (`num_hidden_layers`)
    *   Embedding Dimensions: 896 (`hidden_size`)
    *   Attention Heads: 14 (`num_attention_heads`)
    *   Max Input Size: 4096 (`max_position_embeddings`)
    *   Vocabulary Size: 20,275 (`vocab_size`)
    *   (Source: gf-20L-95M-i4096/config.json.txt)

The model is designed to be pretrained on a large corpus of single-cell transcriptomes to gain a fundamental understanding of gene network dynamics (docs/source/about.rst.txt).

### Training details:
Geneformer is pretrained in a self-supervised manner on a large-scale corpus of single-cell transcriptomes (docs/source/about.rst.txt). The pretraining task is Masked Language Modeling (MLM), as indicated by the `BertForMaskedLM` architecture (config.json.txt).

An example pretraining script provides the following parameters (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py):
*   **Optimizer:** AdamW (`optimizer = "adamw"`)
*   **Learning Rate Schedule:** Linear (`lr_schedule_fn = "linear"`)
*   **Max Learning Rate:** 1e-3 (`max_lr = 1e-3`)
*   **Warmup Steps:** 10,000 (`warmup_steps = 10_000`)
*   **Epochs:** 3 (`epochs = 3`)
*   **Batch Size:** 12 (`geneformer_batch_size = 12`)
*   **Weight Decay:** 0.001 (`weight_decay = 0.001`)
*   **Dropout:** Attention probability dropout is 0.02, and hidden dropout probability is 0.02 (`attention_probs_dropout_prob`, `hidden_dropout_prob` in config.json.txt).

The pretraining is done using the `GeneformerPretrainer` class, which is a modification of the Hugging Face `Trainer` (geneformer/pretrainer.py). The training utilizes a `DataCollatorForLanguageModeling` with a masking probability of 15% (`mlm_probability = 0.15`) (geneformer/pretrainer.py).

### Paper or other resource for more information:
The model is described in two academic papers (docs/source/about.rst.txt):
1.  C V Theodoris et al. "Transfer learning enables predictions in network biology." *Nature*, 31 May 2023. This paper reports results for the original 6-layer Geneformer model. Link: https://rdcu.be/ddrx0
2.  H Chen et al. "Quantized multi-task learning for context-specific representations of gene network dynamics." *bioRxiv*, 19 Aug 2024. This paper provides details on the expanded model, continual learning, multitask learning, and quantization strategies. Link: https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf

Additional resources include:
*   **Hugging Face Repository:** https://huggingface.co/ctheodoris/Geneformer (docs/source/conf.py, docs/source/getstarted.rst.txt)
*   **Example Tutorials:** The repository includes examples for tokenizing data, pretraining, fine-tuning, and in silico perturbation. Link: https://huggingface.co/ctheodoris/Geneformer/tree/main/examples (docs/source/getstarted.rst.txt)
*   **Example Input Files:** Located in the dataset repository. Link: https://huggingface.co/datasets/ctheodoris/Genecorpus-30M/tree/main/example_input_files (docs/source/getstarted.rst.txt)

### Citation details:
The following citations are provided for referencing the model (docs/source/about.rst.txt):

*   C V Theodoris #, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, P T Ellinor #. `Transfer learning enables predictions in network biology. <https://rdcu.be/ddrx0>`_ *Nature*, 31 May 2023. (# co-corresponding authors)

*   H Chen \*, M S Venkatesh \*, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka †, C V Theodoris † #. `Quantized multi-task learning for context-specific representations of gene network dynamics. <https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf>`_ *bioRxiv*, 19 Aug 2024. (\* co-first authors, † co-senior authors, # corresponding author)

### License:
Insufficient information

### Contact:
For questions, issues, or feedback, the contact email provided is: christina.theodoris@gladstone.ucsf.edu (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Geneformer is a foundational model pretrained on single-cell transcriptomes to enable context-aware predictions in network biology, especially in settings with limited data (setup.py, docs/source/about.rst.txt). The model can be used directly for zero-shot learning or fine-tuned for specific downstream tasks (docs/source/about.rst.txt).

**Capabilities and Applications:**
The model is designed to gain a fundamental understanding of gene network dynamics (docs/source/about.rst.txt). Example applications demonstrated in the manuscripts include:

**Fine-tuning applications:**
*   Transcription factor dosage sensitivity
*   Chromatin dynamics (bivalently marked promoters)
*   Transcription factor regulatory range
*   Gene network centrality
*   Transcription factor targets
*   Cell type annotation
*   Batch integration
*   Cell state classification (e.g., across differentiation, disease classification)
*   In silico perturbation to determine disease-driving genes
*   In silico treatment to determine candidate therapeutic targets
(Source: docs/source/about.rst.txt)

**Zero-shot learning applications:**
*   Batch integration
*   Gene context specificity
*   In silico reprogramming and differentiation
*   In silico perturbation to determine impact on cell state, transcription factor targets, and transcription factor cooperativity
(Source: docs/source/about.rst.txt)

**Input-Output Structure:**
The model takes a rank value encoding of a single-cell transcriptome as input. This encoding is a sequence of tokens representing genes, ordered by their normalized expression value (examples/tokenizing_scRNAseq_data.ipynb.txt). The output depends on the task:
*   For **classification tasks**, it outputs class predictions (e.g., disease state, cell type) (examples/cell_classification.ipynb.txt, examples/gene_classification.ipynb.txt).
*   For **embedding extraction**, it outputs cell or gene embeddings (geneformer/emb_extractor.py).
*   For **in silico perturbation**, it outputs the impact of gene perturbations on cell embeddings (examples/in_silico_perturbation.ipynb.txt).

### Primary intended users:
The intended users are researchers and developers in the field of network biology (setup.py, docs/source/about.rst.txt).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

**Installation:**
First, ensure `git-lfs` is installed. Then, clone the repository and install the package (docs/source/getstarted.rst.txt).
```bash
git lfs install
git clone https://huggingface.co/ctheodoris/Geneformer
cd Geneformer
pip install .
```

**1. Tokenizing Single-Cell RNA-seq Data:**
Input data must be in `.loom` or `.h5ad` format with raw counts. The tokenizer converts this into a rank value encoding `.dataset` format. Genes are represented by Ensembl IDs (examples/tokenizing_scRNAseq_data.ipynb.txt).

```python
from geneformer import TranscriptomeTokenizer

# Define custom cell attributes to keep in the tokenized dataset
tk = TranscriptomeTokenizer({"cell_type": "cell_type", "organ_major": "organ"}, nproc=16)

# Tokenize data from a directory of .loom files
tk.tokenize_data("loom_data_directory", 
                 "output_directory", 
                 "output_prefix", 
                 file_format="loom")
```
(Source: examples/tokenizing_scRNAseq_data.ipynb.txt)

**2. Fine-tuning for Cell Classification:**
The model can be fine-tuned to classify cells based on their state (e.g., disease).

```python
from geneformer import Classifier

# Define output directory and prefix
output_prefix = "cm_classifier_test"
output_dir = "/path/to/output_dir/"

# Define training arguments (hyperparameters should be tuned)
training_args = {
    "num_train_epochs": 0.9,
    "learning_rate": 0.000804,
    "lr_scheduler_type": "polynomial",
    "warmup_steps": 1812,
    "weight_decay": 0.258828,
    "per_device_train_batch_size": 12,
    "seed": 73,
}

# Initialize the classifier
cc = Classifier(classifier="cell",
                cell_state_dict={"state_key": "disease", "states": "all"},
                filter_data={"cell_type":["Cardiomyocyte1","Cardiomyocyte2","Cardiomyocyte3"]},
                training_args=training_args,
                freeze_layers=2,
                nproc=16)

# Prepare data by filtering, labeling, and splitting
# Example uses a predefined train/test split
train_test_id_split_dict = {"attr_key": "individual",
                            "train": ["1447", "1600", ...],
                            "test": ["1437", "1516", ...]}
cc.prepare_data(input_data_file="/path/to/human_dcm_hcm_nf_2048_w_length.dataset",
                output_directory=output_dir,
                output_prefix=output_prefix,
                split_id_dict=train_test_id_split_dict)

# Train and validate the model
all_metrics = cc.validate(model_directory="/path/to/Geneformer",
                          prepared_input_data_file=f"{output_dir}/{output_prefix}_labeled_train.dataset",
                          id_class_dict_file=f"{output_dir}/{output_prefix}_id_class_dict.pkl",
                          output_directory=output_dir,
                          output_prefix=output_prefix)
```
(Source: examples/cell_classification.ipynb.txt)

**3. Fine-tuning for Gene Classification:**
The model can also be fine-tuned to classify genes (e.g., dosage-sensitive vs. -insensitive).

```python
from geneformer import Classifier
import pickle

# Load a dictionary defining gene classes
with open("/path/to/dosage_sensitivity_TFs.pickle", "rb") as fp:
    gene_class_dict = pickle.load(fp)

# Initialize the classifier for gene classification with 5-fold cross-validation
gc = Classifier(classifier="gene",
                gene_class_dict=gene_class_dict,
                max_ncells=10_000,
                freeze_layers=4,
                num_crossval_splits=5,
                nproc=16)

# Prepare data
gc.prepare_data(input_data_file="/path/to/gc-30M_sample50k.dataset",
                output_directory="/path/to/output_dir/",
                output_prefix="tf_dosage_sens_test")

# Train and validate
all_metrics = gc.validate(model_directory="/path/to/Geneformer",
                          prepared_input_data_file="/path/to/output_dir/tf_dosage_sens_test_labeled.dataset",
                          id_class_dict_file="/path/to/output_dir/tf_dosage_sens_test_id_class_dict.pkl",
                          output_directory="/path/to/output_dir/",
                          output_prefix="tf_dosage_sens_test")
```
(Source: examples/gene_classification.ipynb.txt)

**4. In Silico Perturbation:**
This feature simulates the effect of gene deletion or overexpression on cell embeddings.

```python
from geneformer import InSilicoPerturber, EmbExtractor, InSilicoPerturberStats

# Define cell states to model the shift from a start state to a goal state
cell_states_to_model = {"state_key": "disease", 
                      "start_state": "dcm", 
                      "goal_state": "nf", 
                      "alt_states": ["hcm"]}

# First, extract the average embeddings for the start, goal, and alt states
embex = EmbExtractor(model_type="CellClassifier", num_classes=3, max_ncells=1000)
state_embs_dict = embex.get_state_embs(cell_states_to_model,
                                       "path/to/model",
                                       "path/to/input_data",
                                       "path/to/output_directory",
                                       "output_prefix")

# Initialize the perturber to simulate gene deletion
isp = InSilicoPerturber(perturb_type="delete",
                        genes_to_perturb="all",
                        model_type="CellClassifier",
                        num_classes=3,
                        cell_states_to_model=cell_states_to_model,
                        state_embs_dict=state_embs_dict,
                        max_ncells=2000)

# Run the perturbation
isp.perturb_data("path/to/model",
                 "path/to/input_data",
                 "path/to/output_directory",
                 "output_prefix")

# Analyze the results
ispstats = InSilicoPerturberStats(mode="goal_state_shift",
                                  cell_states_to_model=cell_states_to_model)
ispstats.get_stats("path/to/input_data",
                   None,
                   "path/to/output_directory",
                   "output_prefix")
```
(Source: examples/in_silico_perturbation.ipynb.txt)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by biological and technical factors inherent in single-cell RNA-seq data. The example notebooks demonstrate consideration of the following factors for creating balanced data splits for fine-tuning and evaluation:
*   **Biological factors:** `disease`, `lvef` (left ventricular ejection fraction), `age`, `sex` (examples/cell_classification.ipynb.txt).
*   **Technical/Grouping factors:** `individual` (to group cells from the same person), `length` (number of tokens in the cell's transcriptome) (examples/cell_classification.ipynb.txt).
*   **Cell type:** The data is often filtered by `cell_type` before analysis (examples/cell_classification.ipynb.txt).

### Evaluation factors:
The provided examples focus on evaluating classification performance (accuracy, F1 score) on a held-out test set but do not report disaggregated results based on the factors listed above (examples/cell_classification.ipynb.txt, examples/gene_classification.ipynb.txt).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's classification performance is evaluated using the following metrics:
*   **Accuracy:** The proportion of correct predictions (examples/cell_classification.ipynb.txt).
*   **Macro F1 Score:** The unweighted mean of the F1 scores for each class, providing a balanced measure of precision and recall (examples/cell_classification.ipynb.txt).
*   **Confusion Matrix:** A table showing the distribution of predicted vs. true labels (examples/cell_classification.ipynb.txt).
*   **ROC AUC:** For binary classification, the Area Under the Receiver Operating Characteristic Curve is calculated to measure the model's ability to distinguish between classes (examples/gene_classification.ipynb.txt, geneformer/evaluation_utils.py).

### Decision thresholds:
Insufficient information

### Variation approaches:
For gene classification, performance is assessed using 5-fold cross-validation to ensure robustness of the measurements (examples/gene_classification.ipynb.txt). For cell classification, a single train/validation/test split is used in the example (examples/cell_classification.ipynb.txt).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The example notebooks demonstrate evaluation on held-out test sets derived from a larger dataset.
*   **Cardiomyopathy Disease Classification:** The evaluation uses a test set of 15% of the data, split by `individual` IDs. The example input data file is `human_dcm_hcm_nf.dataset`, which can be found at https://huggingface.co/datasets/ctheodoris/Genecorpus-30M/tree/main/example_input_files/cell_classification/disease_classification/human_dcm_hcm_nf.dataset (examples/cell_classification.ipynb.txt).
*   **Dosage-Sensitive TF Classification:** The evaluation is performed using 5-fold cross-validation on the `dosage_sensitivity_TFs.pickle` dataset. The input data is a sample from Genecorpus-30M (`gc-30M_sample50k.dataset`) (examples/gene_classification.ipynb.txt).

### Motivation:
These datasets were chosen to demonstrate the model's effectiveness on representative downstream tasks in network biology, such as classifying disease states from cell transcriptomes and classifying gene properties (docs/source/about.rst.txt, examples/cell_classification.ipynb.txt).

### Preprocessing:
The evaluation data is preprocessed using the `prepare_data` function in the `Classifier` class. This involves:
1.  **Filtering:** Selecting a subset of cells based on metadata (e.g., `cell_type`) (examples/cell_classification.ipynb.txt).
2.  **Labeling:** Assigning numerical labels to the target classes (e.g., disease states) (geneformer/classifier_utils.py).
3.  **Splitting:** The data is split into training and testing sets. This can be done randomly, stratified by a specific column, or based on predefined IDs (examples/cell_classification.ipynb.txt, geneformer/classifier.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The Geneformer models were pretrained on large-scale corpora of human single-cell transcriptomes (docs/source/about.rst.txt):
*   **Genecorpus-30M:** Used for the original 6-layer and 12-layer models. This corpus contains approximately 30 million single-cell transcriptomes.
*   **~95 Million Transcriptomes Corpus:** Used for the expanded 12-layer and 20-layer models.

The pretraining corpus is available at https://huggingface.co/datasets/ctheodoris/Genecorpus-30M (docs/source/getstarted.rst.txt).

### Motivation:
The goal of pretraining on a large and diverse corpus is for the model to gain a "fundamental understanding of gene network dynamics" in a self-supervised manner. This foundational knowledge can then be transferred to a wide array of downstream tasks (docs/source/about.rst.txt).

### Preprocessing:
The primary preprocessing step is the tokenization of single-cell transcriptomes into a rank value encoding format (examples/tokenizing_scRNAseq_data.ipynb.txt). This process involves:
1.  **Normalization:** Gene transcript counts in each cell are normalized by the total transcript count of that cell to account for varying sequencing depth (examples/pretraining_new_model/obtain_nonzero_median_digests.ipynb.txt).
2.  **Scaling:** The normalized counts for each gene are then scaled by the non-zero median expression value of that gene across the entire pretraining corpus (e.g., Genecorpus-30M). This prioritizes genes that uniquely distinguish cell states (examples/pretraining_new_model/obtain_nonzero_median_digests.ipynb.txt).
3.  **Ranking:** Genes within each cell are ordered by the rank of their normalized and scaled expression values (geneformer/tokenizer.py).
4.  **Tokenization:** The ranked list of genes is converted into a sequence of integer tokens using a predefined vocabulary (geneformer/tokenizer.py).

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
The documentation states that "GPU resources are required for efficient usage of Geneformer" (docs/source/getstarted.rst.txt).

### Training or Fine-tuning Requirements:
The example pretraining script was configured to run with deepspeed on 12 GPUs (`deepspeed --num_gpus=12`) (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py). Fine-tuning also requires GPU resources (docs/source/getstarted.rst.txt). Specific memory or hardware requirements (e.g., RAM/VRAM size) are not specified.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model was trained on and is intended for use with human single-cell transcriptome data, which can be sensitive. For example, one of the demonstrated use cases involves classifying human cardiomyopathy disease states (`dcm`, `hcm`, `nf`) using patient data (examples/cell_classification.ipynb.txt). Another application is to determine candidate therapeutic targets for diseases like cardiomyopathy (docs/source/about.rst.txt).

Potential risks include misdiagnosis if used in a clinical context, privacy concerns related to the use of patient data, and the potential for biased predictions if the training data is not representative of diverse populations. The repository does not explicitly detail risk mitigation strategies or potential harms, but the example for disease classification does mention balancing data splits by attributes like `age` and `sex`, which could be a step towards mitigating some biases (examples/cell_classification.ipynb.txt). The risks associated with using the model for therapeutic target discovery are not detailed.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
Insufficient information

### Recommendations:
The developers provide the following recommendations for users (docs/source/getstarted.rst.txt):
*   **Use GPU Resources:** "GPU resources are required for efficient usage of Geneformer."
*   **Tune Hyperparameters:** "we strongly recommend tuning hyperparameters for each downstream fine-tuning application as this can significantly boost predictive potential in the downstream task (e.g. max learning rate, learning schedule, number of layers to freeze, etc.)."

