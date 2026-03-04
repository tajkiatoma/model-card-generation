## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, UNI, was developed by a team of researchers primarily from the Department of Pathology at Brigham and Women’s Hospital, Harvard Medical School, and Massachusetts General Hospital. Other collaborating institutions include the Broad Institute of Harvard and MIT, Dana-Farber Cancer Institute, and Massachusetts Institute of Technology (MIT) (s41591-024-02857-3.pdf, p. 1, 13). The lead authors are Richard J. Chen, Tong Ding, Ming Y. Lu, and Drew F. K. Williamson, and the project was supervised by Faisal Mahmood (s41591-024-02857-3.pdf, p. 1, 24).

### Model date:
The development timeline for the model is indicated by the submission and publication dates of its associated academic paper:
*   **Received:** 28 August 2023 (s41591-024-02857-3.pdf, p. 1)
*   **Accepted:** 5 February 2024 (s41591-024-02857-3.pdf, p. 1)
*   **Published online:** 19 March 2024 (s41591-024-02857-3.pdf, p. 1)

### Model version:
The model is named UNI. The primary version is based on a Vision Transformer-Large (ViT-L) architecture pretrained on the Mass-100K dataset (s41591-024-02857-3.pdf, p. 2). The repository also describes ablations of the model to assess scaling trends, including:
*   **Data Scale Variants:** Models pretrained on subsets of the data, named Mass-22K (16 million images) and Mass-1K (1 million images) (s41591-024-02857-3.pdf, p. 2).
*   **Architecture Scale Variants:** A version using a smaller ViT-Base (ViT-B) architecture (s41591-024-02857-3.pdf, p. 2).

UNI is presented as a state-of-the-art foundation model for computational pathology, outperforming previous models such as CTransPath and REMEDIS on a wide range of tasks (s41591-024-02857-3.pdf, p. 2).

### Model type:
UNI is a general-purpose, self-supervised vision encoder for computational pathology (CPath) (s41591-024-02857-3.pdf, p. 1).
*   **Architecture:** The model uses a Vision Transformer-Large (ViT-L) architecture (s41591-024-02857-3.pdf, p. 2). The configuration file specifies `vit_large_patch16_224`, indicating a patch size of 16x16 pixels and a default input image size of 224x224 pixels (config.json.txt).
*   **Model Size:** The model has 1024 features in its embedding dimension (`num_features`) (config.json.txt).
*   **Functionality:** It is designed to learn objective characterizations of histopathological biomarkers from Hematoxylin and Eosin (H&E) stained whole-slide images (WSIs) to be applied to various downstream CPath tasks (s41591-024-02857-3.pdf, p. 2).

### Training details:
UNI was pretrained using a self-supervised learning approach called DINOv2 on the Mass-100K dataset (s41591-024-02857-3.pdf, p. 2).
*   **Algorithm:** The DINOv2 method is based on student-teacher knowledge distillation and utilizes two main loss objectives: a self-distillation loss (alignment) and a masked image modeling loss (reconstruction) (s41591-024-02857-3.pdf, p. 3, 14). The teacher network acts as an online tokenizer to provide prediction targets for the student network on masked patches (s41591-024-02857-3.pdf, p. 14).
*   **Training Iterations:** The model was pretrained for 125,000 total iterations. High-resolution fine-tuning was conducted during the last 12,500 iterations (s41591-024-02857-3.pdf, p. 15).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   Chen, R.J., Ding, T., Lu, M.Y. et al. "Towards a general-purpose foundation model for computational pathology." *Nature Medicine* 30, 850–862 (2024). https://doi.org/10.1038/s41591-024-02857-3 (s41591-024-02857-3.pdf, p. 1).

This paper introduces the UNI model, describes the creation of the Mass-100K pretraining dataset, and presents a comprehensive evaluation of the model on 34 computational pathology tasks.

### Citation details:
To cite the model, please use the following BibTeX entry:
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
(Derived from s41591-024-02857-3.pdf)

### License:
The model is released under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license (CC BY-NC-ND 4.0) (config.json.txt).

### Contact:
For correspondence and requests for materials, contact Faisal Mahmood at `faisalmahmood@bwh.harvard.edu` (s41591-024-02857-3.pdf, p. 1, 13). Additional contact can be made with Richard Chen at `richardchen@g.harvard.edu` (requesting_access.png).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is a general-purpose foundation model intended to serve as a vision encoder for a wide range of computational pathology (CPath) tasks on H&E-stained tissue images (s41591-024-02857-3.pdf, p. 1). It is designed to be used as a frozen feature extractor, where its embeddings can be used for various downstream applications without requiring fine-tuning of the model itself (s41591-024-02857-3.pdf, p. 2).

Specific intended uses demonstrated in the paper include:
*   **Slide-Level Classification:** Weakly supervised classification for tasks like cancer metastasis detection, cancer subtyping (including up to 108 cancer types), and prostate cancer grading (s41591-024-02857-3.pdf, p. 2, 4).
*   **Region-of-Interest (ROI) Level Tasks:**
    *   **Classification:** Classifying tissue types, polyps, and cancer subtypes (s41591-024-02857-3.pdf, p. 5).
    *   **Segmentation:** Segmenting eight major cell types in tumor tissue, such as epithelial cells, lymphocytes, and red blood cells (s41591-024-02857-3.pdf, p. 7).
    *   **Image Retrieval:** Finding visually similar histology images based on feature representations (s41591-024-02857-3.pdf, p. 7).
*   **Few-Shot Learning:** Classifying slides or ROIs with a very limited number of training examples per class, using class prototypes (s41591-024-02857-3.pdf, p. 5, 8).
*   **Resolution-Agnostic Analysis:** The model has shown robustness to varying image resolutions, making it suitable for tasks where magnification is a key factor (s41591-024-02857-3.pdf, p. 7).

### Primary intended users:
The primary intended users are researchers and developers in the field of computational pathology and medical AI. These users are expected to have expertise in machine learning and pathology to apply the model's features to their specific clinical or research problems (s41591-024-02857-3.pdf, p. 1, 9).

### Out-of-scope uses:
The model has several known limitations and out-of-scope applications:
*   **Non-Pathology Images:** The model is trained exclusively on histopathology images and is not intended for use on natural images or other medical imaging modalities (s41591-024-02857-3.pdf, p. 1).
*   **Non-H&E Stains:** The pretraining was performed on H&E-stained images. Its performance on other staining methods is not evaluated (s41591-024-02857-3.pdf, p. 1).
*   **Multimodal Applications:** UNI is a unimodal (vision-only) model. Applications requiring integration with other data types like genomics or clinical text (e.g., cross-modal retrieval, visual question answering) are out of scope (s41591-024-02857-3.pdf, p. 10).
*   **Slide-Level or Patient-Level Architectures:** UNI is an ROI-level model. It is intended as a building block for, but is not itself, a complete slide-level or patient-level diagnostic system (s41591-024-02857-3.pdf, p. 10).
*   **Cytopathology and Hematopathology:** The evaluation did not include tasks in cytopathology or hematopathology, so its applicability to these domains is unknown (s41591-024-02857-3.pdf, p. 10).

---

## How to Use
This section outlines how to use the model.

The primary way to use UNI is as a frozen feature extractor for tissue patches (ROIs). The model takes a 224x224 pixel image patch as input and outputs a 1024-dimensional feature vector (config.json.txt).

**Input Preprocessing:**
Input images should be resized to 224x224 pixels and normalized using the following ImageNet statistics:
*   **Mean:** `[0.485, 0.456, 0.406]`
*   **Standard Deviation:** `[0.229, 0.224, 0.225]`
*   **Interpolation:** Bilinear
(config.json.txt)

**Example Usage Paradigms:**

1.  **ROI-Level Classification (Linear/KNN Probing):**
    *   Extract features for all ROIs in a training dataset using the pretrained UNI model.
    *   Train a simple classifier, such as Logistic Regression or a K-Nearest Neighbors (KNN) classifier, on these extracted features.
    *   For a new ROI, extract its features with UNI and use the trained classifier to predict its class.
    (s41591-024-02857-3.pdf, p. 5, 16)

2.  **Slide-Level Classification (Weakly Supervised MIL):**
    *   For each whole-slide image (WSI), segment the tissue regions and divide them into non-overlapping patches (e.g., 224x224 pixels).
    *   Use UNI to extract a feature vector for every patch in the slide. This creates a "bag" of instance features for the slide.
    *   Train a Multiple Instance Learning (MIL) model, such as Attention-Based MIL (ABMIL), which learns to aggregate the patch features to make a single prediction for the entire slide.
    (s41591-024-02857-3.pdf, p. 2, 15)

3.  **Few-Shot Classification (Prototyping):**
    *   For each class, extract features from a small number of support images (e.g., 1 to 32 ROIs).
    *   Create a "class prototype" by averaging the feature vectors for each class.
    *   To classify a new query image, extract its features and assign it the label of the class with the nearest prototype (based on Euclidean distance).
    (s41591-024-02857-3.pdf, p. 8)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data and Model Scale:** The size of the pretraining dataset (data scale) and the size of the model architecture (model scale) are key factors. Performance generally improves as both data and model size increase (s41591-024-02857-3.pdf, p. 2).
*   **Self-Supervised Learning (SSL) Algorithm:** The choice of SSL algorithm is highly impactful. The study found that DINOv2 significantly outperformed MoCoV3 for this application (s41591-024-02857-3.pdf, p. 2, 9).
*   **Image Resolution:** The resolution of input images (microns per pixel) can affect the interpretation of morphological features. UNI was found to be more robust to changes in image resolution compared to other models (s41591-024-02857-3.pdf, p. 7).
*   **H&E Stain Variability:** Variations in H&E staining across different labs and scanners can affect model performance, particularly in out-of-domain evaluations. UNI is potentially less sensitive to this variability than other encoders (s41591-024-02857-3.pdf, p. 9).
*   **Data Diversity:** The diversity of tissue types and disease categories in the pretraining data is crucial for the model's ability to generalize to a wide range of downstream tasks (s41591-024-02857-3.pdf, p. 2).

### Evaluation factors:
The model was evaluated by systematically varying the following factors:
*   **Pretraining Data Size:** Performance was compared for models trained on Mass-1K, Mass-22K, and Mass-100K datasets to establish scaling laws (s41591-024-02857-3.pdf, p. 2, Fig. 2c,e).
*   **Model Architecture:** ViT-Large was compared against ViT-Base to assess the impact of model size (s41591-024-02857-3.pdf, p. 2).
*   **Downstream Task Diversity:** The model was evaluated on 34 distinct CPath tasks, including classification, segmentation, and retrieval, across various organs and diseases to test its generalization capabilities (s41591-024-02857-3.pdf, p. 1).
*   **Image Resolution:** Performance was explicitly tested across multiple image resolutions for BRCA subtyping and CRC polyp classification tasks (s41591-024-02857-3.pdf, p. 7, Fig. 3d).
*   **Label Efficiency:** The model was evaluated in few-shot learning settings, using a varying number of training examples (from 1 to 32) per class (s41591-024-02857-3.pdf, p. 5, Fig. 2g-j).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A variety of metrics were used depending on the task:
*   **Classification:**
    *   **Area Under the Receiver Operating Characteristic Curve (AUROC):** Used for slide-level classification tasks to measure discriminative ability across thresholds (s41591-024-02857-3.pdf, p. 2).
    *   **Top-K Accuracy (K=1, 3, 5):** Used for multi-class classification tasks like OncoTree, where the prediction is correct if the true label is among the top K predicted labels (s41591-024-02857-3.pdf, p. 2).
    *   **Balanced Accuracy:** The unweighted average of recall for each class, used for ROI-level tasks to account for class imbalance (s41591-024-02857-3.pdf, p. 5, 17).
    *   **Weighted F1 Score:** The F1 score for each class, averaged and weighted by the number of true instances for each class (support) (s41591-024-02857-3.pdf, p. 2, 17).
    *   **Quadratic Weighted Cohen's Kappa (κ):** Used for ordinal classification tasks like prostate ISUP grading to measure inter-annotator agreement, where disagreements between distant grades are penalized more heavily (s41591-024-02857-3.pdf, p. 4, 17).
*   **Image Retrieval:**
    *   **Accuracy@K (Acc@K, K=1, 3, 5):** A retrieval is successful if at least one of the top-K retrieved images has the same label as the query image (s41591-024-02857-3.pdf, p. 7, 17).
    *   **Majority Vote Accuracy@5 (MVAcc@5):** A stricter metric where the retrieval is successful only if the majority class among the top-5 retrieved images matches the query's class (s41591-024-02857-3.pdf, p. 7, 17).
*   **Segmentation:**
    *   **Dice Score:** Used as the primary evaluation metric, equivalent to the F1 score for measuring the overlap between predicted and ground truth segmentation masks (s41591-024-02857-3.pdf, p. 7).

### Decision thresholds:
The paper reports AUROC, which evaluates performance across all possible decision thresholds. However, it does not specify or recommend particular decision thresholds for operational use (s41591-024-02857-3.pdf, p. 17).

### Variation approaches:
*   **Confidence Intervals:** 95% confidence intervals for model performance were estimated using non-parametric bootstrapping with 1,000 replicates (s41591-024-02857-3.pdf, p. 17).
*   **Statistical Significance:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of performance differences between models (s41591-024-02857-3.pdf, p. 2, 17).
*   **Few-Shot Evaluation:** For few-shot experiments, performance was evaluated over multiple runs (5 for slide-level, 1,000 for ROI-level) with different random samples of training data. Results are reported using box plots showing the median, quartiles, and range of performance to capture variance (s41591-024-02857-3.pdf, p. 5, 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of 34 public and in-house computational pathology (CPath) tasks (s41591-024-02857-3.pdf, p. 1). These datasets cover a wide range of tissue types, disease categories, and task formats. Key evaluation datasets include:
*   **OncoTree Classification (OT-43 & OT-108):** An in-house dataset from BWH with 5,564 WSIs for classifying 43 cancer types and 108 fine-grained OncoTree codes, including many rare cancers (s41591-024-02857-3.pdf, p. 2).
*   **CAMELYON16:** A public dataset for breast cancer metastasis detection in lymph node WSIs (129 test slides) (s41591-024-02857-3.pdf, p. 4).
*   **PANDA:** A public challenge dataset for prostate cancer ISUP grading from core needle biopsies (954 test slides) (s41591-024-02857-3.pdf, p. 4).
*   **EBRAINS Digital Tumor Atlas:** A public dataset for subtyping brain tumors, including 30 rare cancer types (573 test slides) (s41591-024-02857-3.pdf, p. 5).
*   **TCGA (The Cancer Genome Atlas):** Multiple tasks were derived from TCGA, including pan-cancer tissue classification (32 classes, 55,360 test ROIs) and NSCLC subtyping (s41591-024-02857-3.pdf, p. 5, 21).
*   **SegPath:** The largest public ROI-level segmentation dataset for CPath, used for segmenting eight major cell types (s41591-024-02857-3.pdf, p. 7).
*   **CRC-100K:** A public dataset of 107,180 ROIs for 9-class colorectal cancer tissue classification (s41591-024-02857-3.pdf, p. 19).

A full list of datasets and their sources is available in the supplementary materials of the paper (s41591-024-02857-3.pdf, p. 22, Table 73).

### Motivation:
The datasets were chosen to comprehensively assess the model's generalization capabilities across diverse tissue types, disease categories, and diagnostic challenges. This was a deliberate move away from benchmarks that focus on a single organ or binary disease states, aiming to better reflect the complexity of real-world anatomic pathology (s41591-024-02857-3.pdf, p. 2). The inclusion of tasks with many rare cancer types was specifically intended to test the model's performance in data-scarce scenarios (s41591-024-02857-3.pdf, p. 2).

### Preprocessing:
For most evaluation tasks, a consistent preprocessing pipeline was applied:
*   **Image Resizing:** Input images (ROIs or patches from WSIs) were resized to 224 × 224 pixels (s41591-024-02857-3.pdf, p. 15).
*   **Normalization:** Images were normalized using the standard ImageNet mean and standard deviation values (s41591-024-02857-3.pdf, p. 15).
*   **Stain Normalization:** For some TCGA-based tasks, Macenko stain normalization was applied to mitigate potential biases from site-specific H&E staining variability (s41591-024-02857-3.pdf, p. 21).
*   **Patching:** For slide-level tasks, tissue regions on WSIs were segmented and divided into non-overlapping patches for feature extraction (s41591-024-02857-3.pdf, p. 15).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
UNI was pretrained on **Mass-100K**, a large-scale, diverse dataset created specifically for this work.
*   **Size and Content:** It contains over 100 million tissue patches (totaling >77 TB of data) sampled from 100,426 diagnostic H&E-stained whole-slide images (WSIs) (s41591-024-02857-3.pdf, p. 1).
*   **Diversity:** The dataset spans 20 major tissue types, including both cancerous and normal tissue, sourced from three distinct cohorts to ensure diversity (s41591-024-02857-3.pdf, p. 1, Fig 1a).
*   **Sources:** The WSIs were collected from:
    1.  Massachusetts General Hospital (MGH)
    2.  Brigham and Women's Hospital (BWH)
    3.  The Genotype-Tissue Expression (GTEx) consortium (publicly available)
    (s41591-024-02857-3.pdf, p. 2)
*   **Public Availability:** The in-house data from MGH and BWH is not publicly available due to patient privacy, but requests for access are evaluated on a case-by-case basis. The GTEx data is publicly accessible (s41591-024-02857-3.pdf, p. 22).

### Motivation:
The Mass-100K dataset was created to address the limitations of existing public datasets in pathology, which are often constrained in size and diversity. The goal was to build a large and varied pretraining dataset that would enable the development of a true foundation model capable of generalizing across a wide range of clinical tasks and workflows, similar to how large datasets like ImageNet have spurred progress in general computer vision (s41591-024-02857-3.pdf, p. 2).

### Preprocessing:
The preprocessing pipeline for creating the Mass-100K patch dataset involved:
1.  **Tissue Segmentation:** A pipeline adapted from the CLAM toolbox was used to identify tissue regions on each WSI at low resolution. This involved converting from RGB to HSV color space, thresholding the saturation channel, and applying morphological operations to refine the tissue mask (s41591-024-02857-3.pdf, p. 14).
2.  **Patch Extraction:** Non-overlapping tissue patches were extracted from the segmented regions at ×20 magnification.
3.  **Image Sizes:** The dataset includes 75,832,905 patches at 256 × 256 pixels and an additional 24,297,995 patches at 512 × 512 pixels for high-resolution training stages, totaling 100,130,900 images (s41591-024-02857-3.pdf, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was analyzed across numerous individual factors. UNI consistently outperformed other pretrained encoders (REMEDIS, CTransPath, ResNet-50) across the majority of the 34 evaluated tasks.
*   **OncoTree Classification (OT-108):** UNI achieved a top-1 accuracy of 53.7% and an AUROC of 0.972, significantly outperforming the next-best model, REMEDIS (42.9% accuracy, 0.952 AUROC) (s41591-024-02857-3.pdf, p. 2, 4, Supplementary Table 15).
*   **Prostate ISUP Grading (PANDA):** UNI achieved a quadratic weighted Cohen's κ of 0.946, outperforming REMEDIS (0.932) (s41591-024-02857-3.pdf, p. 5, Supplementary Table 29).
*   **Brain Tumor Subtyping (EBRAINS, 30-class):** UNI achieved a balanced accuracy of 49.5%, a +16.1% improvement over the next-best model (s41591-024-02857-3.pdf, p. 5, Supplementary Table 34).
*   **ROI Pan-Cancer Classification (TCGA, 32-class):** UNI achieved the highest balanced accuracy (65.7%) and AUROC (0.975), a +4.7% improvement in accuracy over REMEDIS (s41591-024-02857-3.pdf, p. 7).
*   **Cell Type Segmentation (SegPath):** Across eight cell types, UNI achieved the best overall average Dice score of 0.721, outperforming all other backbones (s41591-024-02857-3.pdf, p. 7).

### Intersectional results:
The paper does not present intersectional results based on demographic factors. However, its evaluation on fine-grained classification tasks can be viewed as an analysis of performance across intersections of disease categories.
*   **OncoTree Classification:** The model was evaluated on classifying 108 distinct cancer subtypes, which are hierarchically organized by organ and cell of origin. This task inherently tests the model's ability to distinguish between closely related but distinct cancer types (s41591-024-02857-3.pdf, p. 2).
*   **Brain Tumor Subtyping:** The model was evaluated on classifying 12 coarse-grained and 30 fine-grained brain tumor subtypes from the EBRAINS dataset, many of which are rare, demonstrating its utility in complex, multi-class diagnostic scenarios (s41591-024-02857-3.pdf, p. 5).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Downstream tasks (e.g., training linear probes or MIL models on extracted features) were conducted on single **24 GB NVIDIA 3090 GPUs** (s41591-024-02857-3.pdf, p. 21). This suggests that deploying the model for inference or training simple downstream classifiers requires a GPU with at least 24 GB of VRAM.

### Training or Fine-tuning Requirements:
The self-supervised pretraining of the UNI model required significant computational resources: **4 nodes, each with 8x 80 GB NVIDIA A100 GPUs**, configured for multi-GPU, multi-node distributed data-parallel training (s41591-024-02857-3.pdf, p. 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Privacy and Consent:** The in-house training data was sourced retrospectively from the Mass General Brigham health system. The institutional review board (IRB) approved the study and waived the need for informed consent. All patient data, including WSIs and reports, was de-identified prior to any analysis to protect patient privacy (s41591-024-02857-3.pdf, p. 14). No patient recruitment was performed (s41591-024-02857-3.pdf, p. 36).
*   **Data Contamination Risk:** The developers acknowledge that foundation models trained on large datasets risk "data contamination," where test data may inadvertently be included in the training set, leading to inflated performance metrics. They took steps to mitigate this by evaluating on external cohorts where possible and noting where performance on TCGA-based tasks might be inflated for models that were also pretrained on TCGA (s41591-024-02857-3.pdf, p. 5, 15).
*   **Bias and Fairness:** The paper notes that biases related to data sources, such as "image acquisition shift," should be studied further if the model is reused across many applications, especially if it could have a "disparate impact on diverse populations" (s41591-024-02857-3.pdf, p. 10). The training data for the in-house OT cancer classification task had a self-reported sex distribution of 3080 Female and 2474 Male; no other demographic data was collected or used (s41591-024-02857-3.pdf, p. 36).
*   **Misleading Nomenclature:** The authors caution that labels like "foundation model" may create misleading expectations and that UNI should be understood within the context of its specific architecture and training data (s41591-024-02857-3.pdf, p. 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors identify several limitations of the UNI model and the study:
*   **Architecture Limitations:** The ViT-L architecture lacks the inductive biases of convolutional or hierarchical models, which may limit its performance on dense prediction tasks like segmentation. Performance gains on segmentation were not as drastic as on other tasks (s41591-024-02857-3.pdf, p. 10).
*   **Scope of Evaluation:** The study did not evaluate the largest ViT-Giant architecture from the DINOv2 paper, which might yield further performance gains. Additionally, clinical domains such as cytopathology and hematopathology were not included in the evaluation (s41591-024-02857-3.pdf, p. 10).
*   **Fixed Hyperparameters:** For the broad evaluation across 34 tasks, hyperparameters were fixed. Task-specific tuning would likely improve performance further (s41591-024-02857-3.pdf, p. 10).
*   **Unimodal and ROI-Level:** UNI is a vision-only, ROI-level model. It does not incorporate multimodal data and is not an end-to-end slide-level or patient-level model (s41591-024-02857-3.pdf, p. 10).
*   **Potential for Bias:** Biases from data contamination or shifts in image acquisition protocols across institutions should be carefully considered when applying the model, as these were not exhaustively studied (s41591-024-02857-3.pdf, p. 10).

### Recommendations:
*   **Use as a Building Block:** Users are encouraged to use UNI as a strong foundational building block for developing more complex, slide-level self-supervised models and general-purpose pathology AI systems (s41591-024-02857-3.pdf, p. 10).
*   **Guidance for Custom Models:** The study's findings on data/model scaling and SSL algorithm choice are intended to "guide CPath practitioners in developing their own foundation models using private in-house slide collections" (s41591-024-02857-3.pdf, p. 9).
*   **Consider Task-Specific Tuning:** While the model performs well out-of-the-box, users may achieve better results by tuning downstream classifiers and MIL models on their specific tasks (s41591-024-02857-3.pdf, p. 10).
*   **Future Research:** The authors recommend future work to focus on extending UNI to slide-level self-supervised learning and developing multimodal capabilities (s41591-024-02857-3.pdf, p. 10).