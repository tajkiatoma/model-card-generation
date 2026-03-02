## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Christina Theodoris (setup.py). The associated manuscripts list C V Theodoris, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, and P T Ellinor as authors for the first paper, and H Chen, M S Venkatesh, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka, and C V Theodoris for the second (docs/source/about.rst.txt).

### Model date:
The original 6-layer and 12-layer Geneformer models were pretrained in June 2021. An expanded model was trained in April 2024 (docs/source/about.rst.txt).

### Model version:
The package version is 0.1.0 (setup.py). The repository provides configurations for several model versions, which differ in size, training data, and context length (docs/source/about.rst.txt):

*   **Geneformer (6L-30M-i2048):** The original 6-layer model pretrained on the Genecorpus-30M dataset (docs/source/about.rst.txt). It has 6 hidden layers, a hidden size of 256, 4 attention heads, and supports a maximum input size of 2048 tokens (gf-6L-30M-i2048/config.json.txt).
*   **Geneformer (12L-30M-i2048):** A 12-layer model also pretrained on Genecorpus-30M (docs/source/about.rst.txt). It has 12 hidden layers, a hidden size of 512, 8 attention heads, and supports a maximum input size of 2048 tokens (gf-12L-30M-i2048/config.json.txt).
*   **Geneformer (12L-95M-i4096):** An expanded 12-layer model trained on approximately 95 million transcriptomes (docs/source/about.rst.txt). It has 12 hidden layers, a hidden size of 512, 8 attention heads, and supports a maximum input size of 4096 tokens (config.json.txt, gf-12L-95M-i4096/config.json.txt).
*   **Geneformer (20L-95M-i4096):** An expanded 20-layer model trained on approximately 95 million transcriptomes. It has 20 hidden layers, a hidden size of 896, 14 attention heads, and supports a maximum input size of 4096 tokens (gf-20L-95M-i4096/config.json.txt).

### Model type:
Geneformer is a foundation transformer model based on the BERT architecture, specifically `BertForMaskedLM` (docs/source/index.rst.txt, config.json.txt). It is designed for context-aware predictions in network biology using single-cell transcriptome data (docs/source/index.rst.txt).

The core architecture details vary by version:
*   **6L-30M-i2048:** 6 hidden layers, 4 attention heads, hidden size of 256, intermediate size of 512, and a max position embedding of 2048 (gf-6L-30M-i2048/config.json.txt).
*   **12L-30M-i2048:** 12 hidden layers, 8 attention heads, hidden size of 512, intermediate size of 1024, and a max position embedding of 2048 (gf-12L-30M-i2048/config.json.txt).
*   **12L-95M-i4096:** 12 hidden layers, 8 attention heads, hidden size of 512, intermediate size of 1024, and a max position embedding of 4096 (gf-12L-95M-i4096/config.json.txt).
*   **20L-95M-i4096:** 20 hidden layers, 14 attention heads, hidden size of 896, intermediate size of 1792, and a max position embedding of 4096 (gf-20L-95M-i4096/config.json.txt).

All versions use the "relu" hidden activation function and have a vocabulary size that includes genes plus special tokens like `<pad>` and `<mask>` (config.json.txt, geneformer/pretrainer.py).

### Training details:
The model was pretrained in a self-supervised manner on a large corpus of single-cell transcriptomes (docs/source/about.rst.txt). The training objective was masked language modeling (`BertForMaskedLM`) (config.json.txt).

Key pretraining parameters for the 30M models include:
*   **Max Input Size:** 2048 tokens (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Epochs:** 3 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Batch Size:** 12 per device (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Learning Rate:** Max LR of 1e-3 with a linear schedule and 10,000 warmup steps (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Optimizer:** AdamW with a weight decay of 0.001 (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).

For fine-tuning, the model can be adapted for classification tasks. Default hyperparameters for multi-task fine-tuning include a learning rate between 1e-5 and 1e-3, a warmup ratio of 0.005 to 0.01, and weight decay between 0.01 and 0.1 (geneformer/mtl_classifier.py). The number of initial layers to freeze during fine-tuning is also a key parameter (geneformer/classifier.py).

### Paper or other resource for more information:
The model and its applications are described in two primary manuscripts:

1.  **"Transfer learning enables predictions in network biology."** *Nature*, 31 May 2023. This paper details the original Geneformer model, its pretraining on Genecorpus-30M, and its application to various downstream tasks through fine-tuning and zero-shot learning (docs/source/about.rst.txt). Link: https://rdcu.be/ddrx0 (docs/source/about.rst.txt).
2.  **"Quantized multi-task learning for context-specific representations of gene network dynamics."** *bioRxiv*, 19 Aug 2024. This paper describes the expanded model trained on ~95 million transcriptomes, as well as continual learning, multitask learning, and quantization strategies (docs/source/about.rst.txt). Link: https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf (docs/source/about.rst.txt).

Additional resources include example notebooks and tutorials available in the repository (docs/source/getstarted.rst.txt).

### Citation details:
The following citations are provided for referencing the model and its associated research (docs/source/about.rst.txt):

*   C V Theodoris #, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, P T Ellinor #. `Transfer learning enables predictions in network biology. <https://rdcu.be/ddrx0>`_ *Nature*, 31 May 2023. (# co-corresponding authors)
*   H Chen \*, M S Venkatesh \*, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka †, C V Theodoris † #. `Quantized multi-task learning for context-specific representations of gene network dynamics. <https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf>`_ *bioRxiv*, 19 Aug 2024. (\* co-first authors, † co-senior authors, # corresponding author)

### License:
Insufficient information

### Contact:
For questions or feedback, the contact email is christina.theodoris@gladstone.ucsf.edu (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Geneformer is a foundational model for network biology, designed to be used either directly via zero-shot learning or by fine-tuning for specific downstream tasks. The model takes single-cell transcriptomes represented as "Geneformer rank value encodings" as input (geneformer/mtl_classifier.py).

**Fine-tuning applications include:**
*   Cell state classification (e.g., disease classification, cell type annotation) (docs/source/about.rst.txt, examples/cell_classification.ipynb.txt).
*   Gene classification (e.g., transcription factor dosage sensitivity, gene network centrality) (docs/source/about.rst.txt, examples/gene_classification.ipynb.txt).
*   *In silico* perturbation to identify disease-driving genes (docs/source/about.rst.txt).
*   *In silico* treatment to discover candidate therapeutic targets (docs/source/about.rst.txt).
*   Other tasks such as chromatin dynamics, batch integration, and transcription factor target prediction (docs/source/about.rst.txt).

**Zero-shot learning applications include:**
*   *In silico* perturbation to determine the impact of gene deletion or overexpression on cell or gene embeddings (docs/source/about.rst.txt, geneformer/in_silico_perturber.py).
*   Analysis of transcription factor targets and cooperativity (docs/source/about.rst.txt).
*   *In silico* reprogramming and differentiation (docs/source/about.rst.txt).
*   Batch integration and analysis of gene context specificity (docs/source/about.rst.txt).

### Primary intended users:
The intended users are researchers and developers in network biology, computational biology, bioinformatics, and drug discovery (docs/source/about.rst.txt).

### Out-of-scope uses:
The model is pretrained on single-cell gene expression data and is not designed for applications outside of genomics and transcriptomics. It should not be used for general natural language processing, image analysis, or other non-biological tasks.

---

## How to Use
This section outlines how to use the model.

The model can be used for various tasks, including cell classification, gene classification, and in silico perturbation. Below are example usage snippets.

**1. Cell State Classification**

This example demonstrates fine-tuning the model to classify cardiomyopathy disease states. The input is a `.dataset` file of tokenized single-cell transcriptomes (examples/cell_classification.ipynb.txt).

```python
from geneformer import Classifier

# Define training arguments and filters
filter_data_dict={"cell_type":["Cardiomyocyte1","Cardiomyocyte2","Cardiomyocyte3"]}
training_args = {
    "num_train_epochs": 0.9,
    "learning_rate": 0.000804,
    "lr_scheduler_type": "polynomial",
    "warmup_steps": 1812,
    "weight_decay":0.258828,
    "per_device_train_batch_size": 12,
    "seed": 73,
}

# Initialize the cell classifier
cc = Classifier(classifier="cell",
                cell_state_dict = {"state_key": "disease", "states": "all"},
                filter_data=filter_data_dict,
                training_args=training_args,
                freeze_layers = 2,
                num_crossval_splits = 1)

# Prepare data by labeling and splitting
# Example input: https://huggingface.co/datasets/ctheodoris/Genecorpus-30M/tree/main/example_input_files/cell_classification/disease_classification/human_dcm_hcm_nf.dataset
cc.prepare_data(input_data_file="/path/to/human_dcm_hcm_nf_2048_w_length.dataset",
                output_directory="/path/to/output_dir/",
                output_prefix="cm_classifier_test",
                split_id_dict=train_test_id_split_dict) # dictionary defining train/test splits

# Fine-tune and validate the model
# Example model: https://huggingface.co/ctheodoris/Geneformer/blob/main/model.safetensors
all_metrics = cc.validate(model_directory="/path/to/Geneformer",
                          prepared_input_data_file=f"/path/to/output_dir/cm_classifier_test_labeled_train.dataset",
                          output_directory="/path/to/output_dir/",
                          output_prefix="cm_classifier_test")
```
(examples/cell_classification.ipynb.txt)

**2. Multi-Task Cell Classification**

This example shows how to fine-tune a model on multiple cell classification tasks simultaneously (e.g., cell type and disease state) (examples/multitask_cell_classification.ipynb.txt).

```python
from geneformer import MTLClassifier

# Define paths and task columns
pretrained_path = "/path/to/pretrained/Geneformer/model"
train_path = "/path/to/train/data.dataset"
val_path = "/path/to/val/data.dataset"
task_columns = ["cell_type", "disease_state"]

# Initialize the multi-task classifier
mc = MTLClassifier(
    task_columns=task_columns,
    pretrained_path=pretrained_path,
    train_path=train_path,
    val_path=val_path,
    # ... other parameters
)

# Run hyperparameter optimization and training
mc.run_optuna_study()

# Evaluate the best model on the test set
mc.load_and_evaluate_test_model()
```
(examples/multitask_cell_classification.ipynb.txt, geneformer/mtl_classifier.py)

**3. In Silico Perturbation**

This example demonstrates how to simulate the effect of gene deletions on cell state embeddings (geneformer/in_silico_perturber.py, examples/in_silico_perturbation.ipynb.txt).

```python
from geneformer import InSilicoPerturber, EmbExtractor, InSilicoPerturberStats

# First, extract embeddings for the cell states of interest
cell_states_to_model={"state_key": "disease", "start_state": "dcm", "goal_state": "nf"}
embex = EmbExtractor(model_type="CellClassifier", num_classes=3)
state_embs_dict = embex.get_state_embs(cell_states_to_model,
                                       "path/to/model",
                                       "path/to/input_data",
                                       "path/to/output_directory",
                                       "output_prefix")

# Initialize the perturber
isp = InSilicoPerturber(perturb_type="delete",
                        genes_to_perturb="all",
                        model_type="CellClassifier",
                        num_classes=3,
                        emb_mode="cell",
                        cell_states_to_model=cell_states_to_model,
                        state_embs_dict=state_embs_dict)

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
(geneformer/in_silico_perturber.py, examples/in_silico_perturbation.ipynb.txt)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance can be influenced by biological and technical factors present in single-cell data. The provided tools allow for filtering and stratifying by various attributes. Examples of relevant factors identified in the repository include:
*   **Biological factors:** `cell_type`, `disease` state, `age`, `sex`, `lvef` (left ventricular ejection fraction) (examples/cell_classification.ipynb.txt, geneformer/in_silico_perturber.py).
*   **Technical factors:** `individual` or `patient_id` (to account for donor variability), `length` of the token sequence (representing number of expressed genes) (examples/cell_classification.ipynb.txt, geneformer/classifier.py).

### Evaluation factors:
During fine-tuning for classification, the model's performance is evaluated based on its ability to correctly predict categorical labels. The primary evaluation factor shown in the examples is the `disease` state for cell classification (examples/cell_classification.ipynb.txt). The framework also supports balancing data splits by attributes like `age`, `sex`, and `lvef` to mitigate their confounding effects during evaluation (geneformer/classifier_utils.py).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metrics used to evaluate the classification performance of fine-tuned models are:
*   **Macro F1 Score:** Used to assess the model's effectiveness across all classes, giving equal weight to each class. This is the main metric for hyperparameter optimization (geneformer/classifier_utils.py, geneformer/mtl/eval_utils.py).
*   **Accuracy:** The proportion of correctly classified instances (geneformer/classifier_utils.py).
*   **ROC AUC (Area Under the Receiver Operating Characteristic Curve):** Used for binary classification tasks to measure the model's ability to distinguish between classes (geneformer/evaluation_utils.py).
*   **Confusion Matrix:** Used to visualize the performance of a classification model by showing the counts of true vs. predicted labels for each class (geneformer/evaluation_utils.py).

### Decision thresholds:
Insufficient information

### Variation approaches:
To ensure robust performance measurement, the following approaches are used:
*   **Train/Validation/Test Splits:** Data is partitioned to train the model, tune hyperparameters on a validation set, and report final performance on a held-out test set (geneformer/classifier.py).
*   **Cross-Validation:** The framework supports 5-fold cross-validation to estimate model performance more robustly by training and evaluating on different subsets of the data (geneformer/classifier.py). For binary classification, ROC metrics like the mean true positive rate (TPR) and the standard deviation of the AUC are calculated across folds (geneformer/evaluation_utils.py).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The example notebooks use the following datasets for evaluating fine-tuned models:
*   **Cardiomyopathy Dataset:** A dataset of human cardiomyocytes for classifying disease states (non-failing, dilated cardiomyopathy, hypertrophic cardiomyopathy). An example file is `human_dcm_hcm_nf.dataset`, which is available at https://huggingface.co/datasets/ctheodoris/Genecorpus-30M/tree/main/example_input_files/cell_classification/disease_classification/human_dcm_hcm_nf.dataset (examples/cell_classification.ipynb.txt). The data is split by the `individual` attribute to ensure patient-level separation between training and testing sets (examples/cell_classification.ipynb.txt).
*   **Dosage-Sensitive TF Dataset:** A sample of 50,000 cells from Genecorpus-30M (`gc-30M_sample50k.dataset`) is used to evaluate the classification of transcription factors as dosage-sensitive or -insensitive. The labels are provided in a separate pickle file (`dosage_sensitivity_TFs.pickle`) (examples/gene_classification.ipynb.txt).

### Motivation:
These datasets were chosen to demonstrate the model's capabilities on real-world biological problems:
*   The cardiomyopathy dataset is used to show the model's effectiveness in disease state classification, a critical application in translational medicine (examples/cell_classification.ipynb.txt).
*   The dosage-sensitive TF dataset is used to showcase the model's ability to learn fundamental gene regulatory properties for gene-level classification (examples/gene_classification.ipynb.txt).

### Preprocessing:
The evaluation data undergoes several preprocessing steps before being used:
*   **Filtering:** Data can be filtered to include specific cell types or other attributes. For instance, the cardiomyopathy example filters for cardiomyocytes (`filter_data_dict={"cell_type":["Cardiomyocyte1","Cardiomyocyte2","Cardiomyocyte3"]}`) (examples/cell_classification.ipynb.txt).
*   **Labeling:** Categorical labels (e.g., "nf", "hcm", "dcm") are converted to numerical IDs. A dictionary mapping these IDs back to the class names is saved (geneformer/classifier.py).
*   **Splitting:** The data is split into training, validation, and/or test sets. This can be done randomly, stratified by a specific column, or based on predefined IDs (e.g., patient IDs) to prevent data leakage (geneformer/classifier.py, examples/cell_classification.ipynb.txt).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Geneformer was pretrained on large-scale corpora of human single-cell transcriptomes (docs/source/about.rst.txt):
*   **Genecorpus-30M:** The original models were pretrained on a corpus of ~30 million cells. An example dataset file mentioned is `genecorpus_30M_2048.dataset` (docs/source/about.rst.txt, examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Expanded Corpus:** Later models were trained on an expanded corpus of ~95 million transcriptomes (docs/source/about.rst.txt).

### Motivation:
The motivation for pretraining on a large and diverse corpus was to allow the model to "gain a fundamental understanding of gene network dynamics" in a self-supervised manner. This foundational knowledge can then be transferred to a wide array of downstream tasks, enabling context-specific predictions even in settings with limited data (docs/source/about.rst.txt).

### Preprocessing:
The primary preprocessing step is the tokenization of single-cell transcriptomes into rank value encodings. This process involves (examples/pretraining_new_model/obtain_nonzero_median_digests.ipynb.txt):
1.  **Normalization by Sequencing Depth:** Gene transcript counts in each cell are normalized by the total transcript count of that cell.
2.  **Normalization by Median Expression:** The depth-normalized counts are then further normalized by the non-zero median expression value of each gene across the entire pretraining corpus (e.g., Genecorpus-30M). This step prioritizes genes that uniquely distinguish cell states.
3.  **Rank Value Encoding:** The normalized genes in each cell are ordered by the rank of their normalized expression value. This ranked list of gene tokens forms the input sequence for the model.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The example notebooks provide performance results for specific fine-tuning tasks:

*   **Cardiomyopathy Cell Classification:** On a held-out test set, a fine-tuned model achieved a **macro F1 score of 0.843** and an **accuracy of 0.864** for classifying cells as non-failing (nf), hypertrophic cardiomyopathy (hcm), or dilated cardiomyopathy (dcm) (examples/cell_classification.ipynb.txt). The confusion matrix for one run was:
    | True/Pred | nf | hcm | dcm |
    |---|---|---|---|
    | **nf** | 3794 | 385 | 328 |
    | **hcm** | 562 | 8680 | 566 |
    | **dcm** | 13 | 485 | 2415 |
    (examples/cell_classification.ipynb.txt)

*   **Dosage-Sensitive TF Gene Classification:** In a 5-fold cross-validation setup, the model achieved the following macro F1 scores for each fold: **[0.849, 0.864, 0.912, 0.818, 0.791]**. The overall ROC AUC was **0.914 ± 0.032** (examples/gene_classification.ipynb.txt).

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
*   **Pretraining:** Pretraining the model is computationally intensive. The provided pretraining script specifies using a distributed setup with **3 nodes** and **12 GPUs** in total (examples/pretraining_new_model/pretrain_geneformer_w_deepspeed.py).
*   **Fine-tuning:** The documentation states that "GPU resources are required for efficient usage of Geneformer" (docs/source/getstarted.rst.txt). The example notebooks suggest adjusting the `forward_batch_size` and `per_device_train_batch_size` parameters based on available GPU memory (examples/cell_classification.ipynb.txt, examples/multitask_cell_classification.ipynb.txt). The framework also supports data parallelization (`use_data_parallel`) for multi-GPU setups (geneformer/mtl_classifier.py).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model is trained on human single-cell transcriptome data, which can be considered sensitive personal information (docs/source/about.rst.txt). The example applications involve classifying cells based on attributes such as `disease`, `age`, and `sex`, which are protected attributes (examples/cell_classification.ipynb.txt).

The primary intended use is in healthcare, including disease classification and the identification of therapeutic targets (docs/source/about.rst.txt). The application of this model in such critical areas carries potential risks, such as misdiagnosis or the development of therapies that are not equitable across different demographic groups.

The repository provides tools for risk mitigation. The `Classifier` includes functionality to stratify data splits by specified attributes (`stratify_splits_col`) and to balance splits across multiple potential confounding variables (`attr_to_balance`), such as `age` and `sex` (geneformer/classifier.py, geneformer/classifier_utils.py). This helps ensure that the model is trained and evaluated on balanced cohorts, reducing the risk of performance biases. However, users should remain aware of the potential for the model to perpetuate or amplify existing biases in the training data.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   The model requires significant computational resources, and "GPU resources are required for efficient usage" (docs/source/getstarted.rst.txt).
*   The performance of fine-tuned models is highly dependent on the choice of hyperparameters (docs/source/getstarted.rst.txt).

### Recommendations:
*   It is "strongly recommend[ed] tuning hyperparameters for each downstream fine-tuning application as this can significantly boost predictive potential in the downstream task" (docs/source/getstarted.rst.txt, examples/cell_classification.ipynb.txt). This includes parameters like learning rate, learning schedule, and the number of layers to freeze (docs/source/getstarted.rst.txt).
*   Users should adjust batch sizes for training and inference based on their available GPU memory to avoid out-of-memory errors (examples/multitask_cell_classification.ipynb.txt).