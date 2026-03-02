## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Christina Theodoris (setup.py; docs/source/about.rst.txt). The associated publications list Christina V. Theodoris, Lewyn Xiao, A. Chopra, M. D. Chaffin, Z. R. Al Sayed, M. C. Hill, H. Mantineo, E. Brydon, Z. Zeng, X. S. Liu, and P. T. Ellinor as authors for the first paper, and H. Chen, M. S. Venkatesh, J. Gomez Ortega, S. V. Mahesh, T. Nandi, R. Madduri, K. Pelka, and C. V. Theodoris for the second (docs/source/about.rst.txt). The author's email is provided as christina.theodoris@gladstone.ucsf.edu (setup.py).

### Model date:
The original 6-layer and 12-layer Geneformer models were pretrained in June 2021. An expanded model was trained on approximately 95 million transcriptomes in April 2024 (docs/source/about.rst.txt). The version in this repository is 0.1.0 (setup.py; docs/source/conf.py).

### Model version:
The version is 0.1.0 (setup.py; docs/source/conf.py). The repository describes several models (docs/source/about.rst.txt):
*   **6-layer Geneformer model:** The original model pretrained on Genecorpus-30M.
*   **12-layer Geneformer model:** A scaled-up version with a retained width:depth aspect ratio, also pretrained on Genecorpus-30M.
*   **Expanded model (95M model series):** Trained on ~95 million transcriptomes.

The 30M model series (6- and 12-layer) uses a model input size of 2048 and does not use special tokens (`<cls>`, `<eos>`). The 95M model series uses an input size of 4096 and requires special tokens (geneformer/tokenizer.py).

### Model type:
Geneformer is a transformer-based deep learning model with a BERT architecture (docs/source/about.rst.txt; examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py). It is pretrained as a `BertForMaskedLM` (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py). The model can be fine-tuned for various downstream tasks, resulting in different types (geneformer/in_silico_perturber.py):
*   `Pretrained`: The base masked language model.
*   `GeneClassifier`: A `BertForTokenClassification` model for gene-level predictions.
*   `CellClassifier`: A `BertForSequenceClassification` model for cell-level predictions.
*   `MTLCellClassifier`: A multi-task learning cell classifier based on `BertForMaskedLM`.
*   `MTLCellClassifier-Quantized`: An 8-bit quantized version of the `MTLCellClassifier`.

**Architecture Details (from pretraining script for a 6-layer model):**
*   **Model Type:** BERT (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Number of Layers:** 6 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Number of Attention Heads:** 4 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Embedding Dimensions:** 256 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Intermediate Size:** 512 (num_embed_dim * 2) (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Activation Function:** ReLU (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Vocabulary Size:** Length of the token dictionary (genes + 2 for `<mask>` and `<pad>`) (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py)
*   **Max Input Size (Context Length):** 2048 for 30M models, 4096 for 95M models (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py; geneformer/tokenizer.py).

### Training details:
The model was pretrained in a self-supervised manner (docs/source/about.rst.txt). The pretraining process for a 6-layer model used the following parameters (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py):
*   **Algorithm:** Masked Language Modeling (MLM) using `DataCollatorForLanguageModeling` (geneformer/pretrainer.py).
*   **Optimizer:** AdamW (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Learning Rate:** 1e-3 (max learning rate) (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **LR Schedule:** Linear decay with 10,000 warmup steps (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Epochs:** 3 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Batch Size:** 12 per device (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Weight Decay:** 0.001 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Dropout:** 0.02 for attention probabilities and hidden layers (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Initializer Range:** 0.02 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).

For multi-task fine-tuning, optimizers like AdamW are used with schedulers such as linear or cosine with warmup. Gradient clipping can also be applied (geneformer/mtl/train.py).

### Paper or other resource for more information:
The model is described in the following publications (docs/source/about.rst.txt):
*   Theodoris, C.V., Xiao, L., Chopra, A. et al. "Transfer learning enables predictions in network biology." *Nature* (2023). Available at: https://rdcu.be/ddrx0
*   Chen, H., Venkatesh, M.S., Gomez Ortega, J. et al. "Quantized multi-task learning for context-specific representations of gene network dynamics." *bioRxiv* (2024). Available at: https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf

The model repository is available on Hugging Face: https://huggingface.co/ctheodoris/Geneformer (docs/source/conf.py; docs/source/about.rst.txt).

### Citation details:
The following citation formats are provided (docs/source/about.rst.txt):

*   C V Theodoris #, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, P T Ellinor #. `Transfer learning enables predictions in network biology. <https://rdcu.be/ddrx0>`_ *Nature*, 31 May 2023. (# co-corresponding authors)

*   H Chen \*, M S Venkatesh \*, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka †, C V Theodoris † #. `Quantized multi-task learning for context-specific representations of gene network dynamics. <https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf>`_ *bioRxiv*, 19 Aug 2024. (\* co-first authors, † co-senior authors, # corresponding author)

### License:
Insufficient information

### Contact:
For questions or feedback, contact the author at: christina.theodoris@gladstone.ucsf.edu (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Geneformer is a foundational model designed to gain a fundamental understanding of gene network dynamics, which can then be applied to a wide array of downstream tasks in network biology (docs/source/about.rst.txt).

**Input-Output Structure:**
The model takes single-cell RNA-seq data as input. The data is first tokenized into a "rank value encoding" using the `TranscriptomeTokenizer`. This process involves normalizing raw gene counts by total cell counts and then by the non-zero median expression of each gene across a large corpus. Genes are then ranked by this normalized expression value for each cell. The output is a `.dataset` file containing these tokenized encodings (geneformer/tokenizer.py).

**Capabilities and Applications:**
The pretrained model can be used for both zero-shot learning and fine-tuning (docs/source/about.rst.txt).

**Fine-tuning applications include:**
*   Gene or cell state classification (e.g., disease classification, cell type annotation) (geneformer/classifier.py; docs/source/about.rst.txt).
*   Multi-task cell classification (e.g., simultaneously predicting cell type and disease state) (geneformer/mtl_classifier.py).
*   Predicting transcription factor dosage sensitivity, chromatin dynamics, and gene network centrality (docs/source/about.rst.txt).
*   *In silico* treatment to identify candidate therapeutic targets (docs/source/about.rst.txt).

**Zero-shot learning applications include:**
*   *In silico* perturbation analysis to determine the impact of gene deletion or overexpression on cell or gene embeddings (geneformer/in_silico_perturber.py; docs/source/about.rst.txt).
*   *In silico* reprogramming and differentiation (docs/source/about.rst.txt).
*   Batch integration and analyzing gene context specificity (docs/source/about.rst.txt).

### Primary intended users:
The primary intended users are researchers and developers in network biology and related fields who work with single-cell transcriptomics data (docs/source/getstarted.rst.txt; docs/source/about.rst.txt).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The general workflow involves tokenizing raw scRNA-seq data, and then using the pretrained model for fine-tuning or zero-shot applications like *in silico* perturbation.

### 1. Tokenizing scRNA-seq Data
Input data should be raw counts in `.loom` or `.h5ad` format, with genes labeled by Ensembl IDs (`ensembl_id`) and cells labeled with total read counts (`n_counts`) (geneformer/tokenizer.py).

```python
# From examples/tokenizing_scRNAseq_data.ipynb.txt
from geneformer import TranscriptomeTokenizer

# Custom cell attributes can be passed to the tokenized dataset.
# For example, to retain "cell_type" and "organ_major" attributes:
tk = TranscriptomeTokenizer({"cell_type": "cell_type", "organ_major": "organ"}, nproc=16)

# Tokenize data from a directory of .loom files
tk.tokenize_data("loom_data_directory", 
                 "output_directory", 
                 "output_prefix", 
                 file_format="loom")
```

### 2. Fine-tuning for Cell Classification
The model can be fine-tuned to classify cells into different states (e.g., disease states).

```python
# From examples/cell_classification.ipynb.txt
from geneformer import Classifier

# Example for classifying cardiomyopathy disease states
# Hyperparameters should be tuned for optimal performance
training_args = {
    "num_train_epochs": 0.9,
    "learning_rate": 0.000804,
    "lr_scheduler_type": "polynomial",
    "warmup_steps": 1812,
    "weight_decay": 0.258828,
    "per_device_train_batch_size": 12,
    "seed": 73,
}

cc = Classifier(classifier="cell",
                cell_state_dict={"state_key": "disease", "states": "all"},
                filter_data={"cell_type":["Cardiomyocyte1","Cardiomyocyte2","Cardiomyocyte3"]},
                training_args=training_args,
                freeze_layers=2,
                num_crossval_splits=1,
                nproc=16)

# Prepare data by splitting into training and testing sets
cc.prepare_data(input_data_file="/path/to/human_dcm_hcm_nf.dataset",
                output_directory="/path/to/output_dir/",
                output_prefix="cm_classifier_test",
                split_id_dict={"attr_key": "individual", "train": train_ids, "test": test_ids})

# Validate (train and evaluate) the model
all_metrics = cc.validate(model_directory="/path/to/Geneformer",
                          prepared_input_data_file="/path/to/output_dir/cm_classifier_test_labeled_train.dataset",
                          id_class_dict_file="/path/to/output_dir/cm_classifier_test_id_class_dict.pkl",
                          output_directory="/path/to/output_dir/",
                          output_prefix="cm_classifier_test")
```

### 3. In Silico Perturbation
This zero-shot application measures the impact of gene deletion or overexpression on cell embeddings.

```python
# From examples/in_silico_perturbation.ipynb.txt
from geneformer import InSilicoPerturber, EmbExtractor, InSilicoPerturberStats

# First, obtain embeddings for the start, goal, and alternative states
cell_states_to_model = {"state_key": "disease", 
                      "start_state": "dcm", 
                      "goal_state": "nf", 
                      "alt_states": ["hcm"]}
embex = EmbExtractor(model_type="CellClassifier", num_classes=3, max_ncells=1000)
state_embs_dict = embex.get_state_embs(cell_states_to_model,
                                       "path/to/model",
                                       "path/to/input_data",
                                       "path/to/output_directory",
                                       "output_prefix")

# Initialize and run the perturber
isp = InSilicoPerturber(perturb_type="delete",
                        model_type="CellClassifier",
                        num_classes=3,
                        emb_mode="cell",
                        cell_states_to_model=cell_states_to_model,
                        state_embs_dict=state_embs_dict,
                        max_ncells=2000,
                        nproc=16)

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

### 4. Multi-Task Cell Classification
The model can be fine-tuned to predict multiple cell attributes simultaneously.

```python
# From examples/multitask_cell_classification.ipynb.txt
from geneformer import MTLClassifier

# Define tasks and paths
task_columns = ["cell_type", "disease_state"]
mc = MTLClassifier(
    task_columns=task_columns,
    pretrained_path="/path/to/pretrained/Geneformer/model",
    train_path="/path/to/train/data.dataset",
    val_path="/path/to/val/data.dataset",
    # ... other parameters
)

# Run hyperparameter optimization
mc.run_optuna_study()

# Evaluate the best model on the test set
mc.load_and_evaluate_test_model()
```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by biological and technical factors present in single-cell RNA-seq data. The tokenization process normalizes gene expression by total read counts per cell and by the non-zero median expression of genes across the pretraining corpus, indicating that sequencing depth and baseline gene expression levels are key factors (geneformer/tokenizer.py).

For fine-tuning tasks, user-defined metadata are relevant factors. For example, in cell classification tasks, attributes such as `cell_type`, `disease`, `individual`, `age`, and `sex` can be used for filtering, splitting, and balancing data, indicating their relevance to model performance (geneformer/classifier.py; examples/cell_classification.ipynb.txt).

### Evaluation factors:
The provided materials demonstrate evaluation based on overall performance metrics like accuracy and F1-score (examples/cell_classification.ipynb.txt; geneformer/classifier_utils.py). There is no information available on disaggregated evaluation across different demographic or other factors.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
For classification tasks, the model's performance is assessed using the following metrics (geneformer/classifier_utils.py; geneformer/mtl/utils.py; examples/cell_classification.ipynb.txt):
*   **Accuracy:** The proportion of correct predictions.
*   **Macro F1-Score:** The unweighted mean of the F1-scores for each class, treating all classes equally.
*   **ROC AUC:** For binary classification, the Area Under the Receiver Operating Characteristic Curve is also used (geneformer/classifier_utils.py).

For *in silico* perturbation analysis, statistical significance is measured using (geneformer/in_silico_perturber_stats.py):
*   **Wilcoxon rank-sum test:** To compare the distribution of cosine similarity shifts between test and random/null perturbations.
*   **P-values and False Discovery Rate (FDR):** To assess the statistical significance of the observed shifts.

### Decision thresholds:
For classification, predictions are made by taking the `argmax` of the output logits, which implies a standard decision threshold (geneformer/classifier_utils.py). For statistical tests in perturbation analysis, an alpha of 0.05 is used for FDR correction (geneformer/in_silico_perturber_stats.py).

### Variation approaches:
For fine-tuning and evaluation, the data can be split into training, validation, and test sets. The `Classifier` supports 1-fold or 5-fold cross-validation to ensure robust measurements (geneformer/classifier.py). For binary classification tasks, cross-validated mean and standard deviation of ROC AUC are calculated (geneformer/classifier_utils.py).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The example notebooks use datasets derived from the Genecorpus-30M for fine-tuning and evaluation. For instance, the cell classification example uses a dataset for human cardiomyopathy disease states (examples/cell_classification.ipynb.txt).
*   **Dataset:** `human_dcm_hcm_nf.dataset`
*   **Source:** This dataset is available on Hugging Face at `https://huggingface.co/datasets/ctheodoris/Genecorpus-30M/tree/main/example_input_files/cell_classification/disease_classification/human_dcm_hcm_nf.dataset` (examples/cell_classification.ipynb.txt).
*   **Details:** The example shows this dataset being split into training, validation, and test sets based on individual patient IDs (examples/cell_classification.ipynb.txt).

### Motivation:
These datasets are chosen to demonstrate the model's capabilities on specific, relevant downstream tasks in network biology, such as classifying disease states from single-cell transcriptomes (docs/source/about.rst.txt; examples/cell_classification.ipynb.txt).

### Preprocessing:
The primary preprocessing step is the tokenization of raw scRNA-seq data into rank value encodings, as described in the Training Data section (geneformer/tokenizer.py). For evaluation, the `prepare_data` function in the `Classifier` class is used to split the tokenized data into training and test sets. This function can stratify the splits based on specified attributes (e.g., patient ID, disease state) to ensure balanced representation (geneformer/classifier.py; examples/cell_classification.ipynb.txt).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The Geneformer models were pretrained on Genecorpus-30M, a large-scale corpus of single-cell transcriptomes (docs/source/about.rst.txt).
*   **30M Model Series:** Pretrained on the `genecorpus_30M_2048.dataset`, which contains 27,406,208 single-cell transcriptomes after quality control filtering (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **95M Model Series:** Pretrained on an expanded corpus of approximately 95 million transcriptomes (docs/source/about.rst.txt).

The pretraining corpus was compiled from a broad range of human tissues and includes only data from droplet-based sequencing platforms to ensure comparability of expression values for normalization (examples/obtain_nonzero_median_digests.ipynb.txt).

### Motivation:
The pretraining corpus was chosen for its large scale and diversity, containing tens of millions of cells from a broad range of human tissues. This "richness of variable cell states" allows the model to learn fundamental patterns of gene network dynamics and enables the normalization factor to effectively prioritize genes that distinguish cell states (docs/source/about.rst.txt; examples/obtain_nonzero_median_digests.ipynb.txt).

### Preprocessing:
The raw scRNA-seq data (in `.loom` or `.h5ad` format) is converted into a "rank value encoding" using the `TranscriptomeTokenizer` (geneformer/tokenizer.py). This process involves several steps:
1.  **Normalization by Sequencing Depth:** Raw gene transcript counts in each cell are normalized by the total transcript count of that cell.
2.  **Normalization by Gene Median:** The values are then normalized by the non-zero median expression value of each gene across the entire Genecorpus-30M. This step prioritizes genes that uniquely distinguish cell states.
3.  **Ranking:** Genes within each cell are ordered by the rank of their normalized expression.
4.  **Tokenization:** The ranked list of genes is converted into a sequence of integer tokens, where each token corresponds to a unique Ensembl ID.
5.  **Formatting:** The final output is saved in the Hugging Face `.dataset` format (geneformer/tokenizer.py).

The tokenizer can also collapse duplicate Ensembl IDs by summing their counts (geneformer/tokenizer.py).

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
Specific memory requirements are not provided, but the documentation and examples indicate that GPU resources are necessary for efficient usage (docs/source/getstarted.rst.txt).
*   **Pretraining:** The pretraining script for the 30M model specifies using 12 GPUs across 3 nodes (`deepspeed --num_gpus=12 --num_nodes=3`) (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Fine-tuning:** The `Classifier` and `MTLClassifier` have `ngpu` and `batch_size` parameters that can be adjusted based on available GPU memory (geneformer/classifier.py; examples/multitask_cell_classification.ipynb.txt).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model was trained on a large corpus of human single-cell transcriptomes (docs/source/about.rst.txt; examples/obtain_nonzero_median_digests.ipynb.txt). Fine-tuning examples use datasets that include sensitive attributes such as `disease`, `age`, and `sex` (examples/cell_classification.ipynb.txt).

The intended applications of the model, such as disease classification and identifying candidate therapeutic targets, are in the healthcare domain, which carries significant ethical implications (docs/source/about.rst.txt).

The repository does not explicitly discuss potential risks, risk mitigation strategies, or groups that might be negatively affected by the model's application.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Model and Data Versioning:** Users should ensure that the correct token dictionary and gene median file are used for the corresponding model version (e.g., 30M vs. 95M series), as they are not interchangeable (geneformer/tokenizer.py).
*   **Normalization Factor Calculation:** The gene normalization factor (non-zero median expression) was calculated on a large, diverse corpus of droplet-based sequencing data. Recalculating this on smaller or less diverse datasets is not recommended. Mixing sequencing platforms (e.g., droplet-based and plate-based) for this calculation may lead to "unintended effects" (examples/obtain_nonzero_median_digests.ipynb.txt).
*   **Gene Balancing:** The automatic gene balancing feature for the gene classifier is only available for binary classification tasks (geneformer/classifier.py).

### Recommendations:
*   **Hyperparameter Tuning:** It is "strongly" and "highly" recommended to tune learning hyperparameters (e.g., learning rate, number of layers to freeze) for all downstream fine-tuning applications, as this can significantly improve model performance (docs/source/getstarted.rst.txt; examples/cell_classification.ipynb.txt).
*   **Use Provided Tokenizer:** To ensure consistency of the normalization factor used for each gene, users should use the provided `TranscriptomeTokenizer` to process new datasets and should not re-calculate the normalization factor (examples/obtain_nonzero_median_digests.ipynb.txt).
*   **Hardware:** GPU resources are required for efficient usage of Geneformer (docs/source/getstarted.rst.txt).

---