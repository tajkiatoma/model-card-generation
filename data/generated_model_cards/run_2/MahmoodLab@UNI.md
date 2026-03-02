## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, UNI, was developed by a team of researchers primarily from the Department of Pathology at Brigham and Women's Hospital, Harvard Medical School. Other contributing institutions include Massachusetts General Hospital, the Broad Institute of Harvard and MIT, the Dana-Farber Cancer Institute, and the Massachusetts Institute of Technology (MIT) (chen_et_al_2024.pdf, p. 1, 13). The principal investigator and corresponding author for the project is Faisal Mahmood (chen_et_al_2024.pdf, p. 1). The lead authors are Richard J. Chen, Tong Ding, Ming Y. Lu, and Drew F. K. Williamson (chen_et_al_2024.pdf, p. 1, 13).

### Model date:
The development timeline for the model is as follows:
*   **Paper Received:** August 28, 2023
*   **Paper Accepted:** February 5, 2024
*   **Paper Published Online:** March 19, 2024
(chen_et_al_2024.pdf, p. 1)

### Model version:
This is the first version of the UNI model as introduced in the source paper (chen_et_al_2024.pdf, p. 1). The paper compares UNI's performance against other state-of-the-art models in computational pathology, including CTransPath, REMEDIS, and a ResNet-50 baseline pretrained on ImageNet. UNI was shown to outperform these models across 34 different computational pathology tasks (chen_et_al_2024.pdf, p. 2-3). The paper also evaluates ablations of UNI pretrained on smaller datasets (Mass-1K and Mass-22K) to demonstrate scaling laws (chen_et_al_2024.pdf, p. 2).

### Model type:
UNI is a general-purpose, self-supervised vision encoder model for computational pathology (chen_et_al_2024.pdf, p. 1).
*   **Architecture:** The model uses a Vision Transformer (ViT) architecture, specifically `vit_large_patch16_224` (ViT-Large) (chen_et_al_2024.pdf, p. 2; model_config.json). This architecture processes images by dividing them into a grid of patches.
*   **Model Size and Parameters:** It is a ViT-Large model with 1024 features in its embedding dimension (`num_features`) (model_config.json). It processes images divided into 16x16 pixel patches (`patch_size`) (model_config.json).
*   **Functionality:** It is designed to learn powerful visual representations from large-scale histopathology image data without explicit labels. These learned representations (features) can then be used for a wide variety of downstream tasks such as tissue classification, segmentation, cancer grading, and molecular subtyping (chen_et_al_2024.pdf, p. 2). The model supports dynamic image sizes (`dynamic_img_size: true`) (model_config.json).

### Training details:
UNI was pretrained on the Mass-100K dataset using the DINOv2 self-supervised learning algorithm (chen_et_al_2024.pdf, p. 2). This approach is based on student-teacher knowledge distillation and involves two main objectives:
1.  **Self-Distillation (Alignment Loss):** The model learns by matching the outputs of a "student" network with those of a "teacher" network (which is an exponential moving average of the student network). This encourages the model to learn consistent representations from different augmented views of the same image (chen_et_al_2024.pdf, p. 3, 14).
2.  **Masked Image Modeling (Reconstruction Loss):** The model is trained to predict masked regions of an input image based on the surrounding unmasked regions. This helps the model learn high-level visual features and context (chen_et_al_2024.pdf, p. 3, 14).

The pretraining was conducted for 125,000 iterations, with high-resolution fine-tuning applied during the last 12,500 iterations (chen_et_al_2024.pdf, p. 15).

### Paper or other resource for more information:
The primary resource for the model is the academic paper published in *Nature Medicine*:
*   **Title:** Towards a general-purpose foundation model for computational pathology
*   **Authors:** Richard J. Chen, Tong Ding, Ming Y. Lu, et al.
*   **Link:** [https://doi.org/10.1038/s41591-024-02857-3](https://doi.org/10.1038/s41591-024-02857-3) (chen_et_al_2024.pdf, p. 1)

The model's code and weights are available for academic research at the following GitHub repository:
*   **Link:** [https://github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI) (chen_et_al_2024.pdf, p. 22)

### Citation details:
To cite the model in academic work, please use the following BibTeX entry:
```bibtex
@article{chen2024towards,
  title={Towards a general-purpose foundation model for computational pathology},
  author={Chen, Richard J and Ding, Tong and Lu, Ming Y and Williamson, Drew FK and Jaume, Guillaume and Song, Andrew H and Chen, Bowen and Zhang, Andrew and Shao, Daniel and Shaban, Muhammad and others},
  journal={Nature Medicine},
  volume={30},
  number={3},
  pages={850--862},
  year={2024},
  publisher={Nature Publishing Group US}
}
```
(chen_et_al_2024.pdf, p. 1)

### License:
The model is released under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license (CC BY-NC-ND 4.0) (model_config.json). This license generally allows for non-commercial redistribution of the work as long as it is passed along unchanged and in whole, with credit to the creator.

### Contact:
For questions, issues, or feedback, contact the corresponding author, Faisal Mahmood, at `faisalmahmood@bwh.harvard.edu` (chen_et_al_2024.pdf, p. 1, 13). The lead author, Richard J. Chen, can be reached at `richardchen@g.harvard.edu` (contact_info.png).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is intended as a general-purpose foundation model for computational pathology (CPath). Its primary use is as a powerful feature extractor for histopathology images. The model takes H&E-stained whole-slide image (WSI) patches as input and outputs a high-dimensional feature vector (embedding) that captures rich morphological information (chen_et_al_2024.pdf, p. 2).

These features can be used for a wide range of downstream CPath tasks, including:
*   **Cancer Detection:** Identifying metastatic cancer in lymph nodes (e.g., CAMELYON16) (chen_et_al_2024.pdf, p. 2).
*   **Cancer Grading and Subtyping:** Classifying cancer into different subtypes and grades, such as prostate ISUP grading, renal cell carcinoma (RCC) subtyping, and classifying up to 108 different cancer types (chen_et_al_2024.pdf, p. 2).
*   **Biomarker and Molecular Prediction:** Screening for molecular alterations from histology (chen_et_al_2024.pdf, p. 2).
*   **Image Segmentation and Retrieval:** Segmenting different cell types and retrieving visually similar tissue patches (chen_et_al_2024.pdf, p. 2).
*   **Few-Shot Learning:** The model enables classification tasks with very few labeled examples (e.g., 1-32 slides per class) by creating "class prototypes" (chen_et_al_2024.pdf, p. 2, 5).

### Primary intended users:
The primary intended users are researchers and developers in the fields of computational pathology, medical imaging, and artificial intelligence. These users are expected to have expertise in machine learning and pathology to effectively apply the model's features to their specific research questions or clinical applications.

### Out-of-scope uses:
The model has several out-of-scope applications and limitations:
*   **Direct Clinical Diagnosis:** UNI is a research model and is not a standalone diagnostic tool. It should not be used for making clinical decisions without further validation and regulatory approval.
*   **Non-Histopathology Modalities:** The model was trained exclusively on H&E-stained tissue images. It is not intended for use on other pathology modalities like cytopathology or hematopathology, or other medical imaging types like radiology scans (chen_et_al_2024.pdf, p. 10).
*   **Multimodal Tasks:** UNI is a unimodal vision model. It is not designed for tasks that require integrating information from other modalities, such as genomics or clinical text (chen_et_al_2024.pdf, p. 10).
*   **Direct Slide- or Patient-Level Prediction:** UNI is an ROI-level (patch-level) model. While its features can be aggregated for slide-level tasks (e.g., using Multiple Instance Learning), it does not perform slide- or patient-level predictions on its own (chen_et_al_2024.pdf, p. 10).

---

## How to Use
This section outlines how to use the model.

UNI is designed to be used as a "frozen" feature extractor. The typical workflow involves taking a histopathology image patch, preprocessing it, and feeding it into the UNI model to obtain a feature embedding. This embedding can then be used as input for simpler machine learning models to perform a specific task.

**Input-Output Structure:**
*   **Input:** An image patch of a histopathology slide. The model was trained on 224x224 pixel patches, but it can handle dynamic image sizes (model_config.json; chen_et_al_2024.pdf, p. 7). Input images should be normalized using the standard ImageNet mean `[0.485, 0.456, 0.406]` and standard deviation `[0.229, 0.224, 0.225]` (model_config.json).
*   **Output:** A 1024-dimensional feature vector (`num_features`) that represents the visual content of the input patch (model_config.json).

**Example Usage Workflow (for ROI classification):**
1.  **Data Collection:** Gather a dataset of labeled image patches (ROIs) for your specific task (e.g., classifying tumor vs. normal tissue).
2.  **Feature Extraction:** For each image patch in your dataset, pass it through the pretrained UNI model to extract its 1024-dimensional feature vector. The model weights should be frozen (not updated).
3.  **Downstream Model Training:** Train a simple classifier (e.g., logistic regression, k-nearest neighbors) on the extracted feature vectors and their corresponding labels (chen_et_al_2024.pdf, p. 5).
4.  **Inference:** To classify a new, unseen image patch, first extract its feature vector using UNI, then feed the vector into your trained downstream classifier to get a prediction.

For detailed implementation, users should refer to the code provided in the official GitHub repository: [https://github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI) (chen_et_al_2024.pdf, p. 22).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The performance of UNI can be influenced by several factors inherent to digital pathology data and model training:
*   **Data Diversity and Scale:** The model's generalization capability is dependent on the size and diversity of the pretraining data. The paper demonstrates that performance improves as the pretraining dataset scales from Mass-1K to Mass-100K (chen_et_al_2024.pdf, p. 2).
*   **Image Resolution:** Resizing images can alter morphological features. UNI was shown to be more robust to changes in image resolution compared to other models, even improving performance on some tasks with higher-resolution inputs (chen_et_al_2024.pdf, p. 7).
*   **H&E Stain Variability:** Variations in staining protocols across different labs and hospitals can affect model performance. The model may be sensitive to these variations, especially in few-shot learning scenarios where prototypes are learned from a small number of examples (chen_et_al_2024.pdf, p. 9).
*   **Tissue and Disease Type:** The model's performance varies across different tasks and cancer types, with greater improvements observed on tasks involving rare cancer types or higher diagnostic complexity (chen_et_al_2024.pdf, p. 5).

### Evaluation factors:
The model was evaluated across a comprehensive set of factors to test its generalization and robustness:
*   **Task Diversity:** Performance was measured across 34 distinct clinical tasks, including ROI-level classification, segmentation, retrieval, and slide-level classification (chen_et_al_2024.pdf, p. 1).
*   **Data Scale:** The impact of pretraining data size was evaluated by training versions of the model on subsets of the Mass-100K dataset (Mass-1K and Mass-22K) (chen_et_al_2024.pdf, p. 2).
*   **Image Resolution:** The model's robustness was tested by evaluating its performance on tasks with varying input image resolutions (e.g., from 224x224 up to 1,792x1,792 pixels) (chen_et_al_2024.pdf, p. 7).
*   **Out-of-Domain Generalization:** The model was evaluated on external cohorts and datasets that were not used in training to assess its ability to generalize to unseen data sources (e.g., testing on CPTAC after training on TCGA) (chen_et_al_2024.pdf, p. 5).
*   **Label Efficiency:** Performance was evaluated in few-shot learning settings, using a limited number of training examples (1 to 32) per class to measure how efficiently the model can learn new tasks (chen_et_al_2024.pdf, p. 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A variety of metrics were used to assess the model's performance, tailored to the specific nature of each evaluation task:
*   **Classification:**
    *   **AUROC (Area Under the Receiver Operating Characteristic Curve):** Used to measure the trade-off between true positive and false positive rates, providing a threshold-independent measure of performance (chen_et_al_2024.pdf, p. 2).
    *   **Top-K Accuracy:** Measures whether the correct label is among the top K predictions. Used for large multi-class tasks like OncoTree classification (chen_et_al_2024.pdf, p. 2).
    *   **Balanced Accuracy:** The unweighted average of recall for each class, suitable for imbalanced datasets (chen_et_al_2024.pdf, p. 5).
    *   **Weighted F1 Score:** The F1 score (harmonic mean of precision and recall) for each class, weighted by the number of true instances for each class (chen_et_al_2024.pdf, p. 5).
*   **Grading:**
    *   **Quadratic Weighted Cohen's Kappa:** Measures inter-rater agreement for ordinal tasks like ISUP grading, where disagreements of different magnitudes are penalized differently (chen_et_al_2024.pdf, p. 5).
*   **Image Retrieval:**
    *   **Accuracy@K (Acc@K):** The proportion of queries for which at least one of the top K retrieved images has the correct label (chen_et_al_2024.pdf, p. 7).
    *   **MVAcc@5:** A stricter metric where the majority vote of the top 5 retrieved images must match the query's label (chen_et_al_2024.pdf, p. 7).
*   **Segmentation:**
    *   **Dice Score:** Measures the overlap between the predicted segmentation mask and the ground truth mask (equivalent to the F1 score) (chen_et_al_2024.pdf, p. 7).

### Decision thresholds:
Insufficient information. The paper primarily reports threshold-independent metrics like AUROC or accuracy metrics where the decision is based on the highest-scoring class, so specific decision thresholds are not discussed.

### Variation approaches:
To ensure robust measurements and quantify uncertainty, the following statistical methods were used:
*   **Confidence Intervals:** 95% confidence intervals for model performance were estimated using nonparametric bootstrapping with 1,000 replicates (chen_et_al_2024.pdf, p. 17).
*   **Statistical Significance:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of observed differences in performance between models (chen_et_al_2024.pdf, p. 17).
*   **Repeated Experiments:** For few-shot learning evaluations, experiments were repeated over multiple runs (e.g., 5 runs for slide-level, 1,000 runs for ROI-level) with different random samples of training data to account for variability. Results are reported using box plots to show the distribution of outcomes (chen_et_al_2024.pdf, p. 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of 34 public and in-house computational pathology tasks to assess its generalization capabilities. Key evaluation datasets include:
*   **OncoTree Classification (OT-43, OT-108):** An in-house dataset from Brigham and Women's Hospital (BWH) comprising 5,564 WSIs for classifying 43 cancer types and 108 fine-grained OncoTree codes (chen_et_al_2024.pdf, p. 2).
*   **CAMELYON16:** A public dataset for detecting breast cancer metastases in lymph node WSIs (chen_et_al_2024.pdf, p. 2).
*   **PANDA:** A public challenge dataset for prostate cancer ISUP grading from biopsies (chen_et_al_2024.pdf, p. 5).
*   **TCGA (The Cancer Genome Atlas):** Various subsets were used for tasks like pan-cancer classification, NSCLC subtyping, and glioma mutation prediction (chen_et_al_2024.pdf, p. 2, 5).
*   **External Cohorts (CPTAC, EBRAINS, DHMC):** Public datasets used as external validation sets to test out-of-domain performance for tasks like NSCLC, RCC, and brain tumor subtyping (chen_et_al_2024.pdf, p. 5).
*   **ROI-level Datasets:** Including CRC-100K, HunCRC, BACH, and SegPath for tasks like tissue classification, subtyping, and cell segmentation (chen_et_al_2024.pdf, p. 5, 7).

A full list of the datasets, their sources, and links can be found in the supplementary materials of the source paper (chen_et_al_2024.pdf, p. 22, Supplementary Table 73).

### Motivation:
The datasets were chosen to create a large-scale, diverse, and challenging benchmark for pretrained models in pathology. The motivation was to move beyond evaluations limited to a few tasks or primarily on TCGA data, and instead assess the model's ability to generalize across a wide range of tissue types, disease entities, and diagnostic difficulties that are representative of real-world anatomic pathology workflows (chen_et_al_2024.pdf, p. 1-2).

### Preprocessing:
For evaluation, a consistent preprocessing pipeline was applied:
*   **Slide-level Tasks:** Whole-slide images were processed using the CLAM toolbox. This involves segmenting tissue regions at a low resolution to distinguish them from the background, followed by extracting non-overlapping image patches from these regions (chen_et_al_2024.pdf, p. 15).
*   **Image Resizing and Normalization:** All extracted patches and ROI images were resized to 224x224 pixels (unless evaluating at different resolutions) and normalized using the standard ImageNet mean and standard deviation parameters (chen_et_al_2024.pdf, p. 15).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
UNI was pretrained on **Mass-100K**, a large-scale, diverse, private dataset curated for this study.
*   **Size and Content:** It consists of over 100 million tissue patches sampled from 100,426 diagnostic H&E-stained whole-slide images (WSIs), totaling over 77 TB of data (chen_et_al_2024.pdf, p. 1).
*   **Diversity:** The data spans 20 major tissue types, including cancerous tissue, normal tissue, and other pathologies (chen_et_al_2024.pdf, p. 1, 9).
*   **Source:** The WSIs were collected from internal archives at Massachusetts General Hospital (MGH) and Brigham and Women's Hospital (BWH), as well as the public Genotype-Tissue Expression (GTEx) consortium (chen_et_al_2024.pdf, p. 2). The dataset was intentionally curated to not overlap significantly with most public histology collections used for evaluation (chen_et_al_2024.pdf, p. 10).

### Motivation:
The Mass-100K dataset was created to address a key limitation in computational pathology: the lack of massive, diverse datasets for pretraining powerful foundation models. Existing public datasets like TCGA were considered constrained in size and diversity. The goal was to build one of the largest and most diverse histology collections to date to enable the training of a truly general-purpose model that can learn robust representations and generalize well to a wide range of downstream tasks (chen_et_al_2024.pdf, p. 2).

### Preprocessing:
The preprocessing of the raw WSIs to create the Mass-100K patch dataset involved several steps adapted from the CLAM toolbox:
1.  **Tissue Segmentation:** WSIs were processed at a low resolution to identify tissue regions using color-space thresholding and morphological operations.
2.  **Patch Extraction:** Non-overlapping tissue patches were extracted from the segmented regions at x20 magnification.
3.  **Patch Sizing:** The majority of patches were 256x256 pixels. An additional set of 24 million patches were sampled at 512x512 pixels to be used for high-resolution fine-tuning during the final stages of pretraining.
(chen_et_al_2024.pdf, p. 14)

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was analyzed across numerous individual factors. UNI consistently outperformed other pretrained encoders (REMEDIS, CTransPath, ResNet-50) across most of the 34 evaluated tasks.
*   **Slide-level Tasks:** On average across 15 slide-level tasks, UNI showed performance increases of +10.0% over REMEDIS and +8.3% over CTransPath. The largest gains were on challenging tasks involving rare cancers, such as fine-grained brain tumor subtyping (+16.1% over the next best model) (chen_et_al_2024.pdf, p. 4-5).
*   **ROI-level Tasks:** Across 11 ROI-level tasks using linear probing, UNI achieved average performance increases of +5.75% over REMEDIS and +7.58% over CTransPath (chen_et_al_2024.pdf, p. 5-6).
*   **Image Retrieval:** UNI demonstrated superior retrieval performance on all evaluated tasks. For example, on a 32-class pan-cancer task, UNI outperformed the next-best encoder by +4.6% on Acc@1 (chen_et_al_2024.pdf, p. 7).

### Intersectional results:
Performance was also analyzed across combinations of factors to understand the model's scaling properties and robustness.
*   **Model and Data Scaling:** Performance on the OncoTree classification tasks (OT-43 and OT-108) showed a clear positive trend with increasing data and model size. Scaling the pretraining data from Mass-1K to Mass-100K resulted in a +7.9% increase in top-1 accuracy on OT-43. Using the larger ViT-L architecture over ViT-B also consistently improved performance (chen_et_al_2024.pdf, p. 2, Fig 2c,e).
*   **Image Resolution:** On the BRCA subtyping task, UNI's performance degradation at higher resolutions was minimal (-6.3%) compared to REMEDIS (-32.5%) and CTransPath (-18.8%). On the CRC polyp classification task, UNI's performance actually increased by +5.1% at higher resolutions, demonstrating its ability to leverage finer-grained details that are lost in down-sampled images (chen_et_al_2024.pdf, p. 7, Fig 3d).
*   **Label Efficiency (Few-Shot Learning):** UNI demonstrated superior label efficiency. In many tasks, the 8-shot performance of UNI (using 8 examples per class) exceeded the 128-shot or 256-shot performance of the next-best models, indicating it can learn new concepts from significantly less data (chen_et_al_2024.pdf, p. 9, Extended Data Fig. 8).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Downstream tasks and evaluations (which involve loading the model for feature extraction) were conducted on **single 24 GB NVIDIA 3090 GPUs** (chen_et_al_2024.pdf, p. 21). This suggests that a GPU with at least 24 GB of VRAM is sufficient for inference and fine-tuning on downstream tasks.

### Training or Fine-tuning Requirements:
The full pretraining of the UNI model from scratch is computationally intensive. The process was performed on a high-performance computing cluster using **4 nodes, each equipped with eight 80 GB NVIDIA A100 GPUs** (a total of 32 A100 GPUs) configured for multi-node, multi-GPU training (chen_et_al_2024.pdf, p. 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Governance and Privacy:** The internal data used for pretraining (Mass-100K) was sourced from retrospective analyses of pathology images. The study was approved by the Mass General Brigham institutional review board. All patient data, including images and reports, were de-identified prior to use, and the requirement for informed consent was waived for the retrospective analysis of archival slides (chen_et_al_2024.pdf, p. 14).
*   **Potential for Bias:** The developers acknowledge that foundation models trained on large datasets can inherit and amplify biases present in the data. Potential sources of bias include data contamination (overlap between training and public test sets) and image acquisition shift (differences in scanners or protocols). These factors should be carefully studied if the model is to be reused across many applications to prevent a "disparate impact on diverse populations" (chen_et_al_2024.pdf, p. 10).
*   **Risks in Model Usage:** The model is intended for research use only and is not a certified medical device. A primary risk would be the misuse of the model for direct clinical decision-making without rigorous, prospective clinical validation. The model's performance may vary on populations or data sources not represented in its training and evaluation sets, which could lead to erroneous or biased outcomes if deployed naively. Use cases involving rare and underrepresented diseases, while a strength of the model, are also fraught with risk due to the inherent scarcity of evaluation data.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers highlight several limitations of the current model:
*   **Architectural Limitations:** As a standard Vision Transformer, UNI lacks vision-specific inductive biases that are beneficial for dense prediction tasks like segmentation. While it performs competitively, its performance gains on segmentation are not as significant as on classification tasks (chen_et_al_2024.pdf, p. 10).
*   **Gaps in Evaluation:** The evaluation, while extensive, does not include clinical tasks in other pathology domains such as cytopathology or hematopathology. The performance on these tasks is unknown (chen_et_al_2024.pdf, p. 10).
*   **Fixed Hyperparameters:** For the broad evaluation across 34 tasks, hyperparameters for downstream models were fixed and not tuned for each specific task. Further tuning could likely improve performance on individual tasks (chen_et_al_2024.pdf, p. 10).
*   **Potential for Dataset Bias:** Although the Mass-100K dataset is large and diverse, it may contain unknown biases related to the patient populations of the source hospitals or specific image acquisition hardware. Further study of these potential biases is needed (chen_et_al_2024.pdf, p. 10).

### Recommendations:
*   **Use as a Generalist Tool:** The results highlight the strength of using a better-pretrained generalist encoder versus developing highly specialized, task-specific models. Researchers are encouraged to leverage UNI as a strong starting point for a wide variety of CPath problems (chen_et_al_2024.pdf, p. 10).
*   **Further Testing:** Users should perform rigorous testing on their own datasets, especially if they differ significantly from the data sources used in the paper's evaluation.
*   **Future Development:** The paper suggests that UNI can serve as a powerful building block for future work on slide-level self-supervised models and general slide-level pathology AI development (chen_et_al_2024.pdf, p. 10). Practitioners are also encouraged to use the findings on scaling laws to guide the development of their own foundation models using private, in-house data collections (chen_et_al_2024.pdf, p. 9).