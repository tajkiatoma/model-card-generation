## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Christina Theodoris (setup.py; docs/source/conf.py). The author's email is christina.theodoris@gladstone.ucsf.edu (setup.py). The associated papers list additional authors and their affiliations (docs/source/about.rst).

### Model date:
- The original 6-layer and 12-layer Geneformer models pretrained on Genecorpus-30M were pretrained in June 2021 (docs/source/about.rst).
- An expanded model trained on approximately 95 million transcriptomes was trained in April 2024 (docs/source/about.rst).
- The first manuscript was published in *Nature* on May 31, 2023 (docs/source/about.rst).
- A second manuscript was posted to *bioRxiv* on August 19, 2024 (docs/source/about.rst).

### Model version:
The package version is 0.1.0 (setup.py; docs/source/conf.py).

Multiple pretrained versions of the Geneformer model are available (docs/source/about.rst):
- **6-Layer Geneformer**: Pretrained on Genecorpus-30M. This model has 6 hidden layers, an embedding size of 256, 4 attention heads, and a maximum input size of 2048 tokens (pretrain_geneformer_w_deepspeed.py; model_configs/gf-6L-30M-i2048/config.json).
- **12-Layer Geneformer**: A scaled-up version also pretrained on Genecorpus-30M. This model has 12 hidden layers, an embedding size of 512, 8 attention heads, and a maximum input size of 2048 tokens (docs/source/about.rst; model_configs/gf-12L-30M-i2048/config.json).
- **Expanded 12-Layer Geneformer**: Trained on ~95 million transcriptomes. This model has 12 hidden layers, an embedding size of 512, 8 attention heads, and a maximum input size of 4096 tokens. This version also incorporates continual learning, multitask learning, and quantization strategies (docs/source/about.rst; config.json).

### Model type:
Geneformer is a foundation transformer model based on the BERT architecture, specifically `BertForMaskedLM` (config.json; pretrain_geneformer_w_deepspeed.py). It is pretrained on a large-scale corpus of single-cell transcriptomes to enable context-aware predictions in network biology (setup.py).

**Architecture Details:**
The model is an attention-based deep learning model that learns gene network dynamics in a self-supervised manner (docs/source/about.rst). Key architectural parameters vary by version:
- **6-Layer Model**:
    - `architectures`: ["BertForMaskedLM"]
    - `num_hidden_layers`: 6
    - `hidden_size`: 256
    - `num_attention_heads`: 4
    - `intermediate_size`: 512
    - `max_position_embeddings`: 2048
    - `vocab_size`: 25426
    (model_configs/gf-6L-30M-i2048/config.json)
- **12-Layer Model (Expanded)**:
    - `architectures`: ["BertForMaskedLM"]
    - `num_hidden_layers`: 12
    - `hidden_size`: 512
    - `num_attention_heads`: 8
    - `intermediate_size`: 1024
    - `max_position_embeddings`: 4096
    - `vocab_size`: 20275
    (config.json)

The model can be used as a pretrained model for masked language modeling or fine-tuned for downstream tasks like cell or gene classification using architectures like `BertForSequenceClassification` or `BertForTokenClassification` (examples/cell_classification_cardiomyopathy.ipynb; examples/gene_classification_dosage_sensitivity.ipynb). A multi-task version, `GeneformerMultiTask`, is also available, which uses multiple classification heads on top of the BERT model (geneformer/mtl/model.py).

### Training details:
Geneformer was pretrained in a self-supervised manner on a large corpus of single-cell transcriptomes (docs/source/about.rst). The objective was Masked Language Modeling (pretrain_geneformer_w_deepspeed.py).

**Training Data:**
- The original models were pretrained on Genecorpus-30M, which contains 27,406,208 single-cell transcriptomes after quality control filtering (pretrain_geneformer_w_deepspeed.py; docs/source/about.rst). This corpus consists of data from droplet-based sequencing platforms (geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb).
- An expanded model was trained on a corpus of ~95 million transcriptomes (docs/source/about.rst).

**Preprocessing:**
The training data was preprocessed into a rank value encoding. For each cell, raw gene counts were normalized by the total counts in that cell. These values were then normalized by the non-zero median expression value of each gene across the entire pretraining corpus. Finally, genes were ranked by this normalized expression value, and the sequence of ranked gene tokens was used as input to the model (geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb; geneformer/tokenizer.py).

**Training Hyperparameters (for 6-layer model on Genecorpus-30M):**
- **Epochs**: 3
- **Batch Size**: 12 per GPU
- **Optimizer**: AdamW
- **Max Learning Rate**: 1e-3
- **Learning Rate Schedule**: Linear
- **Warmup Steps**: 10,000
- **Weight Decay**: 0.001
(pretrain_geneformer_w_deepspeed.py)

The model was pretrained using DeepSpeed on 12 GPUs (pretrain_geneformer_w_deepspeed.py).

### Paper or other resource for more information:
**Papers:**
- C V Theodoris #, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, P T Ellinor #. `Transfer learning enables predictions in network biology. <https://rdcu.be/ddrx0>`_ *Nature*, 31 May 2023. (# co-corresponding authors) (docs/source/about.rst).
- H Chen \*, M S Venkatesh \*, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka †, C V Theodoris † #. `Quantized multi-task learning for context-specific representations of gene network dynamics. <https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf>`_ *bioRxiv*, 19 Aug 2024. (\* co-first authors, † co-senior authors, # corresponding author) (docs/source/about.rst).

**Repository:**
- The model repository can be found at: https://huggingface.co/ctheodoris/Geneformer (docs/source/conf.py).

### Citation details:
The repository provides the following citations (docs/source/about.rst):

- C V Theodoris #, L Xiao, A Chopra, M D Chaffin, Z R Al Sayed, M C Hill, H Mantineo, E Brydon, Z Zeng, X S Liu, P T Ellinor #. `Transfer learning enables predictions in network biology. <https://rdcu.be/ddrx0>`_ *Nature*, 31 May 2023. (# co-corresponding authors)

- H Chen \*, M S Venkatesh \*, J Gomez Ortega, S V Mahesh, T Nandi, R Madduri, K Pelka †, C V Theodoris † #. `Quantized multi-task learning for context-specific representations of gene network dynamics. <https://www.biorxiv.org/content/10.1101/2024.08.16.608180v1.full.pdf>`_ *bioRxiv*, 19 Aug 2024. (\* co-first authors, † co-senior authors, # corresponding author)

### License:
Insufficient information

### Contact:
Christina Theodoris: christina.theodoris@gladstone.ucsf.edu (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Geneformer is a foundational deep learning model pretrained on a large-scale corpus of human single-cell transcriptomes to gain a fundamental understanding of gene network dynamics. It is designed to enable context-aware predictions in network biology, especially in settings with limited data (setup.py; docs/source/about.rst).

The model can be used for two main types of tasks (docs/source/about.rst):

**1. Fine-tuning:** The pretrained model can be fine-tuned for specific downstream tasks with limited task-specific data. Examples include:
- Transcription factor dosage sensitivity
- Chromatin dynamics (bivalently marked promoters)
- Transcription factor regulatory range
- Gene network centrality
- Transcription factor targets
- Cell type annotation
- Batch integration
- Cell state classification across differentiation
- Disease classification
- In silico perturbation to determine disease-driving genes
- In silico treatment to determine candidate therapeutic targets

**2. Zero-shot learning:** The pretrained model can be used directly without fine-tuning. Examples include:
- Batch integration
- Gene context specificity
- In silico reprogramming
- In silico differentiation
- In silico perturbation to determine impact on cell state, transcription factor targets, and transcription factor cooperativity

The model takes a rank value encoding of a single-cell transcriptome as input. This encoding is a sequence of tokens representing genes, ranked by their normalized expression values (geneformer/tokenizer.py).

### Primary intended users:
The primary intended users are researchers and developers in network biology (setup.py; docs/source/about.rst).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

**Installation:**
Make sure you have git-lfs installed (https://git-lfs.com).
```bash
git lfs install
git clone https://huggingface.co/ctheodoris/Geneformer
cd Geneformer
pip install .
```
(docs/source/getstarted.rst)

**1. Tokenizing Single-Cell RNA-seq Data:**
Input data should be raw counts in `.loom` or `.h5ad` format, with genes labeled by "ensembl_id" and cells by "n_counts" (total reads) (examples/tokenizing_scRNAseq_data.ipynb).
```python
from geneformer import TranscriptomeTokenizer

# Define custom attributes to keep from the original data
tk = TranscriptomeTokenizer({"cell_type": "cell_type", "organ_major": "organ"}, nproc=16)

# Tokenize all .loom files in a directory
tk.tokenize_data("loom_data_directory", 
                 "output_directory", 
                 "output_prefix", 
                 file_format="loom")
```
(examples/tokenizing_scRNAseq_data.ipynb)

**2. Fine-tuning for Cell Classification:**
This example shows fine-tuning for classifying cardiomyopathy disease states (examples/cell_classification_cardiomyopathy.ipynb).
```python
from geneformer import Classifier

# Define training hyperparameters
training_args = {
    "num_train_epochs": 0.9,
    "learning_rate": 0.000804,
    "lr_scheduler_type": "polynomial",
    "warmup_steps": 1812,
    "weight_decay":0.258828,
    "per_device_train_batch_size": 12,
    "seed": 73,
}

# Initialize the classifier
cc = Classifier(classifier="cell",
                cell_state_dict = {"state_key": "disease", "states": "all"},
                filter_data={"cell_type":["Cardiomyocyte1","Cardiomyocyte2","Cardiomyocyte3"]},
                training_args=training_args,
                freeze_layers = 2,
                num_crossval_splits = 1,
                nproc=16)

# Prepare the data (filtering, labeling, splitting)
cc.prepare_data(input_data_file="/path/to/human_dcm_hcm_nf_2048_w_length.dataset",
                output_directory="/path/to/output_dir/",
                output_prefix="cm_classifier_test",
                split_id_dict={"attr_key": "individual", "train": train_ids+eval_ids, "test": test_ids})

# Train and validate the model
all_metrics = cc.validate(model_directory="/path/to/Geneformer",
                          prepared_input_data_file=f"/path/to/output_dir/cm_classifier_test_labeled_train.dataset",
                          id_class_dict_file=f"/path/to/output_dir/cm_classifier_test_id_class_dict.pkl",
                          output_directory="/path/to/output_dir/",
                          output_prefix="cm_classifier_test",
                          split_id_dict={"attr_key": "individual", "train": train_ids, "eval": eval_ids})
```
(examples/cell_classification_cardiomyopathy.ipynb)

**3. In Silico Perturbation:**
This example shows how to determine genes whose deletion in a diseased state shifts the cell embedding towards a healthy state (examples/in_silico_perturbation.ipynb).
```python
from geneformer import InSilicoPerturber, EmbExtractor, InSilicoPerturberStats

# Define cell states to model
cell_states_to_model={"state_key": "disease", 
                      "start_state": "dcm", 
                      "goal_state": "nf", 
                      "alt_states": ["hcm"]}

# First, obtain embeddings for the start, goal, and alternative states
embex = EmbExtractor(model_type="CellClassifier", num_classes=3, max_ncells=1000)
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
(examples/in_silico_perturbation.ipynb)

Tutorials for pretraining, hyperparameter tuning, extracting embeddings, and multi-task learning are also available in the `examples` directory (docs/source/getstarted.rst).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model is trained on single-cell transcriptome data. Relevant factors that can influence its performance include cell type, tissue of origin, disease state of the cells, and the sequencing platform used (e.g., droplet-based vs. plate-based) (geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb; examples/cell_classification_cardiomyopathy.ipynb). The pretraining corpus was specifically curated to include only droplet-based sequencing platforms to ensure comparability of expression values for normalization (geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb).

### Evaluation factors:
The provided examples demonstrate evaluation based on:
- **Disease state**: Classifying cardiomyocytes as non-failing (nf), hypertrophic cardiomyopathy (hcm), or dilated cardiomyopathy (dcm) (examples/cell_classification_cardiomyopathy.ipynb).
- **Gene properties**: Classifying transcription factors as dosage-sensitive or dosage-insensitive (examples/gene_classification_dosage_sensitivity.ipynb).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics are used to evaluate the model's performance in downstream classification tasks:
- **Accuracy**: The proportion of correct predictions (geneformer/classifier_utils.py).
- **Macro F1 Score**: The unweighted mean of the F1 scores for each class, suitable for imbalanced datasets (geneformer/classifier_utils.py).
- **ROC AUC**: The area under the Receiver Operating Characteristic curve, used for binary classification tasks (examples/gene_classification_dosage_sensitivity.ipynb).
- **Confusion Matrix**: A table showing the performance of a classification model on a set of test data for which the true values are known (examples/cell_classification_cardiomyopathy.ipynb).

### Decision thresholds:
Insufficient information

### Variation approaches:
The model's performance is evaluated using cross-validation. The examples demonstrate using a single train/validation split or a 5-fold cross-validation approach to ensure robust measurements (geneformer/classifier.py; examples/gene_classification_dosage_sensitivity.ipynb).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The example notebooks use specific datasets for evaluation, though the full datasets are not provided in the repository. Example input files are available in a separate dataset repository (docs/source/getstarted.rst).
- **Cardiomyopathy Classification**: A dataset of human heart cells (`human_dcm_hcm_nf.dataset`) is used to evaluate the model's ability to classify disease states. The data is filtered for cardiomyocytes (examples/cell_classification_cardiomyopathy.ipynb).
- **Dosage Sensitivity Classification**: A dataset (`gc-30M_sample50k.dataset`) and a dictionary of dosage-sensitive vs. -insensitive transcription factors (`dosage_sensitivity_TFs.pickle`) are used to evaluate gene classification (examples/gene_classification_dosage_sensitivity.ipynb).

### Motivation:
These datasets were chosen to demonstrate the model's capabilities on diverse and relevant downstream tasks in network biology, such as disease classification and identifying properties of key network regulators (docs/source/about.rst).

### Preprocessing:
The evaluation data is preprocessed using the `prepare_data` method of the `Classifier` class. This involves:
- **Filtering**: Selecting specific cells based on metadata (e.g., `cell_type`) (examples/cell_classification_cardiomyopathy.ipynb).
- **Labeling**: Assigning numerical labels to the target classes (geneformer/classifier_utils.py).
- **Splitting**: The data is split into training, validation, and test sets. This can be done randomly, stratified by a specific column, or based on predefined IDs (e.g., patient IDs) (examples/cell_classification_cardiomyopathy.ipynb; geneformer/classifier.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
- **Genecorpus-30M**: The original 6-layer and 12-layer models were pretrained on this corpus, which consists of 27,406,208 single-cell transcriptomes from various human tissues after quality control filtering. The data was sourced from droplet-based sequencing platforms (pretrain_geneformer_w_deepspeed.py; geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb).
- **~95 Million Transcriptome Corpus**: An expanded model was trained on a larger corpus of approximately 95 million transcriptomes (docs/source/about.rst).

### Motivation:
The goal of pretraining on a large-scale, diverse corpus of human single-cell transcriptomes was for the model to gain a fundamental understanding of gene network dynamics. This foundational knowledge can then be transferred to a wide array of downstream tasks, accelerating the discovery of key network regulators and therapeutic targets (docs/source/about.rst).

### Preprocessing:
The raw count data from single-cell transcriptomes was converted into a rank value encoding for model training. The process involved three main steps:
1.  **Normalization by Total Counts**: Gene transcript counts in each cell were normalized by the total transcript count of that cell to account for varying sequencing depth.
2.  **Normalization by Gene Median**: The values were then normalized by the non-zero median expression of each gene across the entire Genecorpus-30M. This step prioritizes genes that uniquely distinguish cell states.
3.  **Ranking**: The normalized gene expression values within each cell were ranked, and the sequence of ranked gene tokens was used as the input for the model.
(geneformer/gene_expression_tokenization_and_pretraining/get_gene_median_dataset.ipynb; geneformer/tokenizer.py)

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The example notebooks provide performance results for specific fine-tuning tasks:
- **Cardiomyopathy Disease Classification**: On a held-out test set, the model achieved a macro F1 score of 0.843 and an accuracy of 0.864 (examples/cell_classification_cardiomyopathy.ipynb).
- **Dosage-Sensitive TF Classification**: Across a 5-fold cross-validation, the model achieved a mean ROC AUC of 0.914 (examples/gene_classification_dosage_sensitivity.ipynb).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
GPU resources are required for efficient usage of Geneformer (docs/source/getstarted.rst). The example notebooks suggest adjusting the `forward_batch_size` based on available GPU memory (examples/mtl_classifier_cardiomyopathy.ipynb).

### Training or Fine-tuning Requirements:
- **Pretraining**: The model was pretrained using DeepSpeed on 12 GPUs (pretrain_geneformer_w_deepspeed.py).
- **Fine-tuning**: GPU resources are recommended. The example notebooks suggest adjusting the `batch_size` based on available GPU memory (docs/source/getstarted.rst; examples/mtl_classifier_cardiomyopathy.ipynb).

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
- **Hyperparameter Tuning**: It is strongly recommended to tune hyperparameters for each downstream fine-tuning application, as this can significantly boost predictive potential. Key hyperparameters to tune include max learning rate, learning schedule, and the number of layers to freeze (docs/source/getstarted.rst; examples/cell_classification_cardiomyopathy.ipynb).
- **Hardware**: GPU resources are required for efficient usage of Geneformer (docs/source/getstarted.rst).

---