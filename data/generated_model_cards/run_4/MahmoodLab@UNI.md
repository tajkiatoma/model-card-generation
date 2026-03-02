## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, named UNI, was developed by a team of researchers from various institutions, including the Department of Pathology at Brigham and Women’s Hospital, Harvard Medical School; Massachusetts General Hospital; the Cancer Program at the Broad Institute of Harvard and MIT; the Cancer Data Science Program at Dana-Farber Cancer Institute; the Department of Biomedical Informatics at Harvard Medical School; the Harvard John A. Paulson School of Engineering and Applied Sciences; Electrical Engineering and Computer Science at Massachusetts Institute of Technology (MIT); and the Department of Systems Biology at Harvard University (Paper, p. 1, 13). The corresponding author for the research is Faisal Mahmood (Paper, p. 1, 13).

### Model date:
The academic paper describing the model was received on August 28, 2023, accepted on February 5, 2024, and published online on March 19, 2024 (Paper, p. 1).

### Model version:
The model is named UNI, which is a large vision transformer (ViT-L) pretrained on the Mass-100K dataset (Paper, p. 2). The paper also evaluates other versions for ablation studies, including models trained on smaller subsets of the data (Mass-22K and Mass-1K) and a model with a smaller architecture (ViT-Base) (Paper, p. 2). UNI is presented as a state-of-the-art, general-purpose, self-supervised vision encoder for pathology, outperforming previous models like CTransPath and REMEDIS on 34 representative computational pathology (CPath) tasks (Paper, p. 1-2).

### Model type:
UNI is a general-purpose, self-supervised vision encoder model for computational pathology (Paper, p. 1).
*   **Architecture:** It is a large vision transformer (ViT-Large or ViT-L) (Paper, p. 2). The specific architecture is `vit_large_patch16_224`, indicating a patch size of 16x16 pixels and a default input image size of 224x224 pixels (config.json).
*   **Functionality:** It is designed to learn objective characterizations of histopathological entities from whole-slide images, serving as a foundation model for various downstream CPath tasks (Paper, p. 1).
*   **Size:** The model has 1024 features in its output embedding (config.json).
*   **Context Length:** The model supports dynamic image sizes (`dynamic_img_size: true`), meaning it is not restricted to a fixed input size (config.json). It can process high-resolution images by interpolating positional embeddings (Paper, p. 16).

### Training details:
UNI was pretrained using a self-supervised learning approach called DINOv2 on the Mass-100K dataset (Paper, p. 2).
*   **Algorithm:** The DINOv2 method is based on student-teacher knowledge distillation and uses two main loss objectives: a self-distillation loss (alignment loss) and a masked image modeling loss (reconstruction loss) (Paper, p. 3, 14). The teacher network acts as an online tokenizer to provide targets for the student network on masked image patches (Paper, p. 14).
*   **Parameters:** The model was pretrained for 125,000 iterations in total, with high-resolution fine-tuning conducted on the last 12,500 iterations (Paper, p. 15).
*   **Input Normalization:** The model expects input images to be normalized with a mean of `[0.485, 0.456, 0.406]` and a standard deviation of `[0.229, 0.224, 0.225]` (config.json).

### Paper or other resource for more information:
*   **Primary Paper:** The main resource is the academic paper "Towards a general-purpose foundation model for computational pathology," published in *Nature Medicine*. It provides a comprehensive overview of the model's development, training, and extensive evaluation (Paper, p. 1).
    *   DOI: `https://doi.org/10.1038/s41591-024-02857-3` (Paper, p. 1).
*   **Code Repository:** The code and model weights for academic research are available at: `https://github.com/mahmoodlab/UNI` (Paper, p. 22).

### Citation details:
A BibTeX citation for the paper can be formatted as follows, based on the information provided:
```bibtex
@article{Chen_2024,
    author = {Chen, Richard J. and Ding, Tong and Lu, Ming Y. and Williamson, Drew F. K. and Jaume, Guillaume and Song, Andrew H. and Chen, Bowen and Zhang, Andrew and Shao, Daniel and Shaban, Muhammad and Williams, Mane and Oldenburg, Lukas and Weishaupt, Luca L. and Wang, Judy J. and Vaidya, Anurag and Le, Long Phi and Gerber, Georg and Sahai, Sharifa and Williams, Walt and Mahmood, Faisal},
    title = {Towards a general-purpose foundation model for computational pathology},
    journal = {Nature Medicine},
    volume = {30},
    pages = {850--862},
    year = {2024},
    month = {Mar},
    doi = {10.1038/s41591-024-02857-3}
}
```
(Paper, p. 1).

### License:
The model is available under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0) (config.json).

### Contact:
*   For correspondence and requests for materials, contact Faisal Mahmood at `faisalmahmood@bwh.harvard.edu` (Paper, p. 1, 13, 24).
*   An additional contact email for one of the lead authors is `richardchen@g.harvard.edu` (GitHub screenshot).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is a general-purpose foundation model intended for a wide range of computational pathology (CPath) tasks on H&E-stained tissue images (Paper, p. 1). It is designed to be used as a frozen feature extractor, where its powerful representations can be applied to various downstream tasks without requiring end-to-end fine-tuning (Paper, p. 2, 7).
*   **Capabilities:** The model was evaluated on 34 clinical tasks, demonstrating capabilities in:
    *   **ROI-level Classification:** Classifying tissue regions of interest (e.g., cancer subtyping, tissue type identification) (Paper, p. 2, 5).
    *   **ROI-level Segmentation:** Segmenting different cell types, such as epithelial cells, lymphocytes, and red blood cells (Paper, p. 2, 7).
    *   **Image Retrieval:** Finding visually and semantically similar tissue patches from a database (Paper, p. 2, 7).
    *   **Slide-level Weakly Supervised Learning:** Classifying whole-slide images for tasks like cancer detection, grading, and molecular subtyping prediction (Paper, p. 2, 5).
    *   **Few-shot Learning:** Classifying new tasks with very few labeled examples by creating class prototypes (Paper, p. 2, 5, 7).
*   **Input-Output Structure:** The model takes an image patch as input and outputs a 1024-dimensional feature vector that serves as a rich representation of the image's content (config.json).

### Primary intended users:
The primary intended users are researchers and developers in the field of computational pathology and artificial intelligence in medicine (Paper, p. 1, 9). The model is designed to serve as a foundational tool to build more specialized, data-efficient AI models for clinical workflows (Paper, p. 1).

### Out-of-scope uses:
The paper explicitly lists several out-of-scope applications and limitations:
*   **Dense Prediction Tasks:** The model's ViT-L architecture lacks vision-specific inductive biases, which may limit its performance on dense prediction tasks like segmentation compared to hierarchical models (Paper, p. 10).
*   **Multimodal Capabilities:** UNI is a unimodal vision model and does not support multimodal tasks like cross-modal retrieval or visual question answering (Paper, p. 10).
*   **Slide-Level or Patient-Level Analysis:** UNI is an ROI-level model. It is intended as a building block for, but is not itself, a slide-level or patient-level model (Paper, p. 10).
*   **Non-Histopathology Tasks:** The model was trained exclusively on H&E-stained histopathology images and is not intended for use in other domains like natural images, cytopathology, or hematopathology (Paper, p. 1, 10).

---

## How to Use
This section outlines how to use the model.

The model is intended to be used as a feature extractor for downstream tasks in computational pathology. The official code and model weights are available in the GitHub repository: `https://github.com/mahmoodlab/UNI` (Paper, p. 22).

A typical workflow involves:
1.  **Image Preprocessing:** Input image patches (e.g., 224x224 pixels) should be normalized using the ImageNet mean `[0.485, 0.456, 0.406]` and standard deviation `[0.229, 0.224, 0.225]` (config.json; Paper, p. 15).
2.  **Feature Extraction:** Pass the preprocessed image patch through the UNI model to obtain a 1024-dimensional feature embedding (config.json).
3.  **Downstream Task Application:** Use the extracted features as input for other models or algorithms, such as:
    *   **Slide Classification:** Aggregate patch-level features from a whole-slide image and train a multiple instance learning (MIL) model like ABMIL (Paper, p. 2, 15).
    *   **ROI Classification:** Train a simple linear classifier (logistic regression) or a K-nearest neighbors (KNN) model on the extracted features (Paper, p. 5, 16).
    *   **Few-Shot Learning:** Create "class prototypes" by averaging the feature vectors of a few examples from each class. New images can then be classified by finding the nearest class prototype (Paper, p. 7, 16).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **H&E Stain Variability:** Hematoxylin and eosin (H&E) staining can vary significantly between institutions and batches, which can affect model performance. The paper notes that UNI is potentially less sensitive to H&E staining variability compared to other encoders (Paper, p. 9).
*   **Image Resolution:** The resolution of input images, measured in microns per pixel (mpp), can alter morphological features. The model's performance was evaluated at various resolutions, demonstrating robustness, particularly when compared to other models that showed significant performance degradation at different scales (Paper, p. 7).
*   **Data Source and Domain Shift:** The model's performance can be affected by shifts in the data distribution between the training set and the evaluation set (e.g., different hospitals, patient populations). The paper evaluates this by testing on external cohorts (Paper, p. 5, 9).

### Evaluation factors:
The model evaluation explicitly analyzed the following factors:
*   **Data and Model Scaling:** Performance was evaluated across different sizes of the pretraining dataset (Mass-1K, Mass-22K, Mass-100K) and different model architectures (ViT-B, ViT-L) to establish scaling laws (Paper, p. 2).
*   **Image Resolution:** Performance on BRCA subtyping and CRC polyp classification was systematically evaluated across multiple image resolutions (from 224x224 up to 1,792x1,792 pixels) (Paper, p. 7).
*   **Data Source:** For tasks like NSCLC and RCC subtyping, the model was trained on data from one source (e.g., TCGA) and evaluated on external cohorts from different sources (e.g., CPTAC, DHMC) to measure generalization (Paper, p. 5, 9).
*   **Disease Rarity:** The model's ability to classify rare and underrepresented diseases was a key evaluation factor, particularly in the OT-108 and EBRAINS brain tumor tasks (Paper, p. 2, 5, 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The selection of metrics was tailored to the specific downstream task:
*   **Slide-level and ROI-level Classification:**
    *   **Area Under the Receiver Operating Characteristic curve (AUROC):** Used to measure the trade-off between true positive and false positive rates (Paper, p. 2, 17).
    *   **Balanced Accuracy:** The unweighted average of recall for each class, accounting for class imbalance (Paper, p. 5, 17).
    *   **Weighted F1 Score:** The F1 score for each class, averaged and weighted by the number of true instances for each class (Paper, p. 5, 17).
    *   **Top-K Accuracy (K=1, 3, 5):** Used for multi-class tasks like OncoTree classification, where a prediction is correct if the true label is among the top K predicted labels (Paper, p. 2, 17).
*   **Prostate Cancer Grading (PANDA task):**
    *   **Quadratic Weighted Cohen's Kappa:** Measures inter-annotator agreement, suitable for ordinal classification tasks like Gleason grading (Paper, p. 5, 17).
*   **Image Retrieval:**
    *   **Accuracy@K (Acc@K for K=1, 3, 5):** A retrieval is successful if at least one of the top-K retrieved images has the same label as the query image (Paper, p. 7, 17).
    *   **Majority Vote Accuracy@5 (MVAcc@5):** A stricter metric where the majority class of the top-5 retrieved images must match the query's class (Paper, p. 7, 17).
*   **Cell Type Segmentation:**
    *   **Dice Score:** The primary metric used, which is equivalent to the F1 score for segmentation tasks (Paper, p. 7, 17).

### Decision thresholds:
Insufficient information. The paper focuses on evaluating the quality of the model's representations rather than deploying it with specific decision thresholds for clinical use.

### Variation approaches:
*   **Confidence Intervals:** For most experiments, 95% confidence intervals were estimated for performance metrics using non-parametric bootstrapping with 1,000 replicates (Paper, p. 17).
*   **Statistical Significance:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of observed performance differences between models (Paper, p. 17).
*   **Few-Shot Evaluation:** For few-shot learning experiments, performance was evaluated over multiple runs (5 for slide-level, 1,000 for ROI-level) with randomly sampled support sets. Results are reported using box plots to show the median, quartiles, and range of performance (Paper, p. 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of 34 public and in-house CPath tasks (Paper, p. 1). Key datasets include:
*   **OncoTree Classification (OT-43 & OT-108):** An in-house dataset from BWH with 5,564 WSIs for classifying 43 cancer types and 108 rare cancer subtypes (Paper, p. 2, 17).
*   **CAMELYON16:** Breast cancer metastasis detection in lymph nodes (Paper, p. 2).
*   **PANDA:** Prostate cancer ISUP grading (Paper, p. 5).
*   **EBRAINS:** Brain tumor subtyping with 30 rare cancer types (Paper, p. 5).
*   **TCGA:** A large public dataset used for multiple tasks, including NSCLC subtyping, glioma biomarker prediction, and pan-cancer tissue classification (Paper, p. 2, 5).
*   **CPTAC & DHMC:** External validation cohorts for NSCLC and RCC subtyping tasks (Paper, p. 5).
*   **SegPath:** A public dataset for segmenting eight major cell types in tumor tissue (Paper, p. 7).
*   **BACH:** Breast carcinoma subtyping (Paper, p. 7).
A full list of all evaluation datasets and links to their sources is provided in Supplementary Table 73 of the paper (Paper, p. 22).

### Motivation:
The datasets were chosen to demonstrate the versatility and generalization capabilities of UNI across a wide range of diagnostically challenging tasks, diverse tissue types, and different machine learning settings (e.g., slide-level, ROI-level, segmentation, few-shot) (Paper, p. 2). The inclusion of tasks with many rare cancer types (e.g., OT-108, EBRAINS) was specifically motivated by the need to assess the model's performance in clinically relevant but data-scarce scenarios (Paper, p. 2, 5).

### Preprocessing:
For slide-level tasks, tissue regions in WSIs were segmented, and non-overlapping patches were extracted. For all tasks, images were resized (typically to 224x224 pixels) and normalized using ImageNet mean and standard deviation parameters before feature extraction (Paper, p. 15). For some TCGA-based tasks, Macenko stain normalization was applied to mitigate potential biases from site-specific staining variability (Paper, p. 21).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on **Mass-100K**, a large-scale, diverse dataset curated for this study (Paper, p. 2).
*   **Size and Content:** It consists of more than 100 million tissue patches sampled from 100,426 diagnostic H&E-stained whole-slide images (WSIs), totaling over 77 TB of data (Paper, p. 1).
*   **Diversity:** The data spans 20 major tissue types, including cancerous tissue, normal tissue, and other pathologies (Paper, p. 1, 9).
*   **Source:** The WSIs were collected from internal archives at Massachusetts General Hospital (MGH) and Brigham and Women's Hospital (BWH), as well as the public Genotype-Tissue Expression (GTEx) consortium (Paper, p. 2). Public datasets like TCGA were purposefully excluded to allow for external validation (Paper, p. 14).

### Motivation:
The Mass-100K dataset was created to overcome the limitations of existing public datasets in CPath, which are often constrained in size and diversity (e.g., TCGA comprises mostly primary cancer slides) (Paper, p. 2). The goal was to pretrain a foundation model on a massive and varied dataset to enable better generalization and transfer learning to a wide range of clinical tasks (Paper, p. 1, 14).

### Preprocessing:
The preprocessing pipeline for the training data involved several steps using the CLAM toolbox:
1.  **Tissue Segmentation:** WSIs were processed at a low resolution to identify tissue regions by applying a binary threshold to the saturation channel of the HSV color space (Paper, p. 14).
2.  **Contour Smoothing:** Median blurring and morphological closing were used to smooth tissue contours and remove small artifacts (Paper, p. 14).
3.  **Patch Extraction:** Non-overlapping tissue patches of size 256x256 pixels were extracted from the segmented regions at x20 magnification (Paper, p. 14). An additional set of 512x512 patches was also sampled for high-resolution fine-tuning (Paper, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results broken down by various factors.
*   **By Downstream Task:** Performance is reported individually for each of the 34 evaluation tasks. For example, on prostate ISUP grading (PANDA), UNI achieves a quadratic weighted Cohen's κ of 0.946 (Paper, p. 5). On 32-class pan-cancer tissue classification, UNI achieves a balanced accuracy of 65.7% and an AUROC of 0.975 (Paper, p. 7). Detailed results for all tasks are available in the paper's figures and supplementary tables (Paper, p. 4, 6).
*   **By Image Resolution:** For BRCA subtyping, UNI's performance (KNN probe) shows only a minor decrease from ~85% to ~79% accuracy as resolution increases from 224² to 1344², while competitor models drop more significantly (e.g., REMEDIS drops from ~75% to ~42%) (Paper, p. 7, Figure 3d).
*   **By Data Source (Domain):** On NSCLC subtyping, REMEDIS outperforms UNI on the in-domain TCGA test set (97.3% vs. 94.7%), but UNI significantly outperforms REMEDIS on the external CPTAC cohort (96.3% vs. 79.0%), demonstrating superior generalization (Paper, p. 5).

### Intersectional results:
The paper analyzes performance across combinations of factors, primarily focusing on the intersection of task and data domain.
*   **Task x Data Source:** The evaluation of models trained on TCGA and tested on external cohorts like CPTAC, DHMC, and EBRAINS represents an intersectional analysis. For glioma IDH1 mutation prediction, CTransPath and REMEDIS outperform UNI on the in-domain TCGA evaluation, but UNI outperforms both on the external EBRAINS evaluation (85.6% vs. 83.6% and 79.2%), highlighting how performance varies at the intersection of a specific task and the data domain (Paper, p. 5).
*   **Task x Disease Rarity:** The model's performance is analyzed in the context of rare versus common diseases. UNI shows particularly strong performance improvements over baselines on tasks involving many rare cancer types, such as the OT-108 classification and brain tumor subtyping tasks (Paper, p. 5, 9).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Downstream experiments, which involve loading the model for feature extraction and training smaller classifiers, were conducted on **single 24 GB NVIDIA 3090 GPUs** (Paper, p. 21). This suggests that deploying the model for inference is feasible on a single high-end GPU.

### Training or Fine-tuning Requirements:
The large-scale visual pretraining of UNI on the Mass-100K dataset was computationally intensive, requiring **4 nodes, each with 8x 80GB NVIDIA A100 GPUs**, configured for multi-GPU, multi-node training (Paper, p. 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The study was conducted with institutional oversight. The retrospective analysis of internal pathology images and reports was approved by the Mass General Brigham institutional review board (Paper, p. 14).
*   **Sensitive Data:** All internal patient data, including whole-slide images and reports, were de-identified before computational analysis and model development (Paper, p. 14). Informed consent was waived for the retrospective analysis of archival pathology slides, and patients were not directly involved or recruited for the study (Paper, p. 14).
*   **Risk Mitigation:** To mitigate the risk of data contamination and inflated performance, the training dataset (Mass-100K) was intentionally curated to not overlap with most public histology collections used for evaluation (Paper, p. 10, 14).
*   **Risks in Usage:** The paper acknowledges that biases such as data contamination and image acquisition shift should be further studied if the model is reused across many applications, especially if it could have a disparate impact on diverse populations (Paper, p. 10). The authors also caution that labels like "foundation model" may create misleading expectations about the model's capabilities (Paper, p. 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors explicitly state several limitations of the model and the study:
*   **Architectural Limitations:** The ViT-L architecture lacks vision-specific biases that are beneficial for dense prediction tasks like segmentation, where its performance gains were not as drastic as in classification tasks (Paper, p. 10).
*   **Gaps in Evaluation:** The evaluation did not include clinical tasks from other domains like cytopathology or hematopathology (Paper, p. 10).
*   **Fixed Hyperparameters:** Due to the breadth of the evaluation (34 tasks), hyperparameters for downstream models were fixed and not tuned for each specific task, meaning results could likely be improved with further optimization (Paper, p. 10).
*   **Potential Biases:** Biases related to data contamination and shifts in image acquisition across different sites should be studied more deeply if the model is to be widely deployed (Paper, p. 10).
*   **Model Scope:** UNI is an ROI-level model, and future work is needed to extend it to slide-level and patient-level self-supervised learning (Paper, p. 10).

### Recommendations:
*   **Use as a Building Block:** The authors recommend that UNI be used as a building block for developing more specialized slide-level self-supervised models and general pathology AI systems (Paper, p. 10).
*   **Guidance for Practitioners:** The study's findings on data and model scaling are intended to guide CPath practitioners in developing their own foundation models using private, in-house slide collections (Paper, p. 9).
*   **Shift in Research Direction:** The authors hope the success of a general-purpose encoder like UNI will shift research in CPath away from developing narrow, task-specific models and towards more flexible, generalist AI models (Paper, p. 10).