## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, UNI, was developed by a team of researchers from several institutions, primarily:
*   Department of Pathology, Brigham and Women's Hospital, Harvard Medical School, Boston, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).
*   Department of Pathology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).
*   Cancer Program, Broad Institute of Harvard and MIT, Cambridge, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).
*   Cancer Data Science Program, Dana-Farber Cancer Institute, Boston, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).
*   Department of Biomedical Informatics, Harvard Medical School, Boston, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).
*   Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA (s41591-024-02857-3.pdf, p. 1, 13).

The research was supervised by Faisal Mahmood (s41591-024-02857-3.pdf, p. 1, 24).

### Model date:
The development timeline according to the associated academic paper is as follows:
*   **Received:** 28 August 2023 (s41591-024-02857-3.pdf, p. 1).
*   **Accepted:** 5 February 2024 (s41591-024-02857-3.pdf, p. 1).
*   **Published online:** 19 March 2024 (s41591-024-02857-3.pdf, p. 1).

### Model version:
The model is named UNI. The paper does not specify a version number, but the primary version described is a Vision Transformer-Large (ViT-L) model pretrained on the Mass-100K dataset (s41591-024-02857-3.pdf, p. 2). The paper also evaluates ablations of the model to assess scaling trends, including:
*   **Model Scale:** A Vision Transformer-Base (ViT-B) version was also trained (s41591-024-02857-3.pdf, p. 2).
*   **Data Scale:** The model was trained on subsets of the full dataset, named Mass-1K (1 million images) and Mass-22K (16 million images), to demonstrate performance improvements with more data (s41591-024-02857-3.pdf, p. 2).

UNI is designed as a general-purpose pathology foundation model and is shown to outperform previous state-of-the-art models like CTransPath and REMEDIS on 34 computational pathology tasks (s41591-024-02857-3.pdf, p. 1-2).

### Model type:
*   **Category:** UNI is a general-purpose, self-supervised vision encoder for computational pathology (CPath) (s41591-024-02857-3.pdf, p. 1-2). It is designed to learn powerful image representations from large-scale histopathology data, which can then be transferred to a wide range of downstream tasks.
*   **Architecture:** The model is based on the Vision Transformer (ViT) architecture. The primary version uses a ViT-Large (ViT-L) backbone (s41591-024-02857-3.pdf, p. 2). The ViT-L architecture processes images by splitting them into fixed-size patches, embedding them, and feeding them into a standard Transformer encoder (s41591-024-02857-3.pdf, p. 16).
*   **Size:** The paper evaluates ViT-Large and ViT-Base architectures. The specific number of parameters for the UNI model is not stated, but standard ViT-L models have approximately 307 million parameters.

### Training details:
*   **Algorithm:** UNI was pretrained using a self-supervised learning approach called DINOv2 (s41591-024-02857-3.pdf, p. 2). DINOv2 is based on a student-teacher knowledge distillation framework and uses two main loss objectives: a self-distillation loss (aligning representations of different views of an image) and a masked image modeling loss (reconstructing masked parts of an image) (s41591-024-02857-3.pdf, p. 3, 14).
*   **Dataset:** The model was pretrained on Mass-100K, a large-scale dataset created for this work. It contains over 100 million tissue patches extracted from 100,426 diagnostic H&E-stained whole-slide images (WSIs) across 20 major tissue types, totaling over 77 TB of data (s41591-024-02857-3.pdf, p. 1).
*   **Parameters:** The pretraining process involved 125,000 total iterations, with high-resolution fine-tuning conducted on the last 12,500 iterations (s41591-024-02857-3.pdf, p. 15). The model was trained using the AdamW optimizer (s41591-024-02857-3.pdf, p. 15-16).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model's development and evaluation:
*   **Paper:** Chen, R.J., Ding, T., Lu, M.Y. et al. "Towards a general-purpose foundation model for computational pathology". *Nature Medicine* 30, 850–862 (2024). https://doi.org/10.1038/s41591-024-02857-3 (s41591-024-02857-3.pdf, p. 1).
*   **Repository:** Code and model weights are available for academic research purposes at https://github.com/mahmoodlab/UNI (s41591-024-02857-3.pdf, p. 22).

### Citation details:
Insufficient information. The provided repository does not contain a BibTeX citation.

### License:
The specific license is not named. However, the "Code availability" section states that "Code and model weights for UNI can be accessed for academic research purposes" (s41591-024-02857-3.pdf, p. 22). This suggests a custom, non-commercial license restricted to academic research.

### Contact:
*   **Primary Contact:** Correspondence and requests for materials should be addressed to Faisal Mahmood at `faisalmahmood@bwh.harvard.edu` (s41591-024-02857-3.pdf, p. 1, 13, 24).
*   **Additional Contact:** Richard J. Chen, the first author, can be contacted at `richardchen@g.harvard.edu` (requesting_access.png).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is intended as a general-purpose foundation model for computational pathology (CPath) (s41591-024-02857-3.pdf, p. 1). Its primary use is as a powerful feature extractor for histopathology images. The learned representations can be applied to a wide variety of downstream tasks without needing to train a new model from scratch for each task.

Specific intended uses demonstrated in the paper include:
*   **Slide-Level Classification:** Metastasis detection, cancer grading (e.g., Prostate ISUP grading), disease subtyping (e.g., 108 cancer types in the OncoTree system), and organ transplant assessment (s41591-024-02857-3.pdf, p. 2, 5).
*   **Region-of-Interest (ROI) Level Tasks:** Tissue classification, segmentation of cellular structures, and content-based image retrieval (s41591-024-02857-3.pdf, p. 2, 7).
*   **Data-Efficient Learning:** The model is particularly effective in few-shot learning scenarios, where only a small number of labeled examples are available (s41591-024-02857-3.pdf, p. 5). This includes prompt-based slide classification using class prototypes derived from a few ROI examples (s41591-024-02857-3.pdf, p. 9).
*   **Resolution-Agnostic Analysis:** The model demonstrates robustness to varying image resolutions, which is valuable for CPath tasks where optimal magnification can differ (s41591-024-02857-3.pdf, p. 7).

The model takes histopathology image patches as input and outputs a high-dimensional feature vector that captures the tissue morphology (s41591-024-02857-3.pdf, p. 15).

### Primary intended users:
The primary intended users are researchers and developers in the field of computational pathology and artificial intelligence in medicine (s41591-024-02857-3.pdf, p. 9). The model serves as a powerful tool for building and evaluating new AI models for pathology, especially for those working on rare diseases or with limited annotated data.

### Out-of-scope uses:
*   **Direct Clinical Diagnosis:** UNI is a research model and is not intended for direct clinical use without further extensive validation and regulatory approval (s41591-024-02857-3.pdf, p. 1).
*   **Non-Histopathology Imagery:** The model was trained exclusively on H&E-stained histopathology images and is not designed for use with other imaging modalities (e.g., natural images, radiology scans) or staining methods (s41591-024-02857-3.pdf, p. 1).
*   **Multimodal Applications:** UNI is a unimodal vision model. Applications requiring the integration of other data types, such as genomics or clinical text (e.g., cross-modal retrieval, visual question answering), are out of scope (s41591-024-02857-3.pdf, p. 10).
*   **Slide-Level Self-Supervision:** UNI is an ROI-level model. While it can be applied to slide-level tasks via aggregation (e.g., MIL), it was not trained with slide-level objectives (s41591-024-02857-3.pdf, p. 10).

---

## How to Use
The paper describes a general workflow for using UNI as a feature extractor for downstream tasks. The model is typically used in a "frozen" state, meaning its weights are not updated during downstream training (s41591-024-02857-3.pdf, p. 14).

The typical usage pattern is a two-stage process:
1.  **Feature Extraction:** Preprocess a whole-slide image (WSI) by segmenting tissue regions and tiling them into smaller patches (e.g., 224x224 pixels). Feed each patch through the UNI model to obtain a feature embedding for that patch (s41591-024-02857-3.pdf, p. 15).
2.  **Downstream Task Training:** Use the collection of patch embeddings for various tasks:
    *   **Slide-Level Classification:** Aggregate the patch embeddings for a WSI (a "bag" of instances) and train a small classifier, such as an attention-based multiple instance learning (ABMIL) model, on top of these features to predict a slide-level label (s41591-024-02857-3.pdf, p. 15).
    *   **ROI-Level Classification:** Train a simple linear classifier (linear probing) or use a non-parametric method like K-Nearest Neighbors (KNN) on the embeddings of individual ROIs (s41591-024-02857-3.pdf, p. 16).
    *   **Few-Shot Prototyping:** For a given class, average the feature embeddings of a few example ROIs to create a "class prototype." An unseen ROI or WSI can then be classified by finding the nearest class prototype (s41591-024-02857-3.pdf, p. 8-9, 17).

The paper does not provide specific code snippets, but points to the official repository for implementation details (s41591-024-02857-3.pdf, p. 22).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **H&E Stain Variability:** Hematoxylin and eosin (H&E) staining can vary significantly between labs and batches, potentially affecting model performance. The paper notes that UNI is potentially less sensitive to stain variability compared to other models, as seen in its stable performance across different hospital cohorts (s41591-024-02857-3.pdf, p. 9).
*   **Image Resolution (Microns per Pixel):** The model's ability to interpret morphological features can be affected by image resolution. UNI was evaluated across multiple resolutions and demonstrated strong robustness, often highlighting more fine-grained details at higher resolutions (s41591-024-02857-3.pdf, p. 7).
*   **Data Scale and Diversity:** The size and diversity of the pretraining dataset are critical factors. The paper demonstrates that performance scales with the amount of pretraining data (from Mass-1K to Mass-100K) (s41591-024-02857-3.pdf, p. 2).
*   **Disease Rarity:** The model's performance was evaluated on both common and rare diseases. UNI showed particularly strong performance on rare and underrepresented cancer types, highlighting its ability to generalize from diverse pretraining data (s41591-024-02857-3.pdf, p. 9).

### Evaluation factors:
The model was evaluated across a comprehensive set of factors to test its generalization capabilities:
*   **Task Diversity:** Performance was measured on 34 distinct CPath tasks, including classification, segmentation, and retrieval (s41591-024-02857-3.pdf, p. 1).
*   **Tissue and Disease Types:** The evaluation spanned numerous organ systems and up to 108 different cancer types, including 90 rare cancers (s41591-024-02857-3.pdf, p. 2, 9).
*   **Data Efficiency:** The model was evaluated in few-shot learning settings, using as few as 1 to 32 labeled examples per class (s41591-024-02857-3.pdf, p. 5).
*   **Image Resolution:** Specific tasks were evaluated at multiple image resolutions to test for robustness (s41591-024-02857-3.pdf, p. 7).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The choice of metric was tailored to the specific evaluation task:
*   **General Classification:** Area Under the Receiver Operating Characteristic curve (AUROC), balanced accuracy, and weighted F1 score (s41591-024-02857-3.pdf, p. 2, 17).
*   **Multi-Class Classification (OT-43, OT-108):** Top-K accuracy (for K=1, 3, 5) (s41591-024-02857-3.pdf, p. 2, 17).
*   **Prostate Cancer Grading (PANDA):** Quadratic weighted Cohen's kappa (κ), which measures inter-annotator agreement for ordinal tasks (s41591-024-02857-3.pdf, p. 5, 17).
*   **Image Retrieval:** Accuracy@K (Acc@K for K=1, 3, 5) and Majority Vote Accuracy@5 (MVAcc@5) (s41591-024-02857-3.pdf, p. 7, 17).
*   **Segmentation:** Dice score (equivalent to F1 score for segmentation masks) (s41591-024-02857-3.pdf, p. 7, 17).

### Decision thresholds:
The paper focuses on evaluating the model's representation quality for research purposes, not on deploying it for a specific decision-making task. Therefore, specific decision thresholds are not defined. The use of AUROC as a primary metric evaluates performance across all possible thresholds (s41591-024-02857-3.pdf, p. 17).

### Variation approaches:
To ensure robust measurements and quantify uncertainty, the following methods were used:
*   **Confidence Intervals:** 95% confidence intervals were estimated for model performance using non-parametric bootstrapping with 1,000 replicates (s41591-024-02857-3.pdf, p. 17).
*   **Statistical Significance:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of performance differences between models (s41591-024-02857-3.pdf, p. 2, 17).
*   **Repeated Experiments:** For few-shot learning evaluations, experiments were repeated over multiple runs (5 runs for slide-level, 1,000 for ROI-level) with different random samples of training data to ensure stability. Results are reported using box plots showing the distribution of performance (s41591-024-02857-3.pdf, p. 5, 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
UNI was evaluated on a comprehensive suite of 34 tasks using numerous public and in-house datasets. A summary of key datasets includes:
*   **In-house BWH data:** Used for a large-scale cancer classification task (OT-43/OT-108) with 5,564 WSIs and a cardiac transplant assessment task (BWH-EMB) with 332 patients (s41591-024-02857-3.pdf, p. 2, 4, 17).
*   **Public Challenge Datasets:** CAMELYON16 (breast cancer metastasis), PANDA (prostate cancer grading), BACH (breast cancer subtyping), and AGGC (prostate tissue classification) (s41591-024-02857-3.pdf, p. 2, 5, 18-20).
*   **Large Cohorts:** TCGA (used for pan-cancer classification, subtyping, and MSI screening), CPTAC, and EBRAINS (brain tumor subtyping) (s41591-024-02857-3.pdf, p. 2, 5, 18-19).
*   **Other Public Datasets:** CRC-100K, HunCRC (colorectal cancer tasks), UniToPatho (colorectal polyp classification), and SegPath (cell type segmentation) (s41591-024-02857-3.pdf, p. 5, 7, 19-21).
A full list of all 20+ datasets, their sources, and sizes is available in the paper's Methods section and Supplementary Table 73 (s41591-024-02857-3.pdf, p. 17-22).

### Motivation:
The datasets were chosen to create a broad and challenging benchmark for foundation models in pathology. The selection was motivated by the need to:
*   Assess generalization across diverse tissue types, disease categories, and institutions (s41591-024-02857-3.pdf, p. 2).
*   Evaluate performance on a wide range of clinically relevant and diagnostically difficult tasks (s41591-024-02857-3.pdf, p. 1).
*   Test data efficiency and performance on rare diseases, which are critical challenges in CPath (s41591-024-02857-3.pdf, p. 5).

### Preprocessing:
For most evaluation tasks, a standardized preprocessing pipeline was applied:
1.  **Tissue Segmentation:** A tissue segmentation algorithm (from the CLAM toolbox) was used on low-resolution WSIs to identify tissue regions (s41591-024-02857-3.pdf, p. 15).
2.  **Patch Extraction:** Non-overlapping image patches were extracted from the segmented tissue regions (s41591-024-02857-3.pdf, p. 15).
3.  **Image Resizing and Normalization:** Patches were resized to 224x224 pixels and normalized using the mean and standard deviation from the ImageNet dataset (s41591-024-02857-3.pdf, p. 15).
For some tasks, Macenko stain normalization was applied to mitigate staining variability (s41591-024-02857-3.pdf, p. 21).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
UNI was pretrained on **Mass-100K**, a large-scale, diverse dataset curated for this study.
*   **Size and Composition:** It contains over 100 million tissue image patches sampled from 100,426 diagnostic H&E-stained WSIs, totaling over 77 TB of data (s41591-024-02857-3.pdf, p. 1).
*   **Diversity:** The WSIs cover 20 major tissue types, including cancerous tissue, normal tissue, and other pathologies (s41591-024-02857-3.pdf, p. 1, 9).
*   **Source:** The data was collected from internal archives at Massachusetts General Hospital (MGH) and Brigham and Women's Hospital (BWH), and supplemented with external data from the Genotype-Tissue Expression (GTEx) consortium (s41591-024-02857-3.pdf, p. 2, 14).
*   **Subsets:** Two smaller subsets, **Mass-22K** (16 million patches from 21,444 WSIs) and **Mass-1K** (1 million patches from 1,404 WSIs), were created to study data scaling laws (s41591-024-02857-3.pdf, p. 2, 14).

### Motivation:
The Mass-100K dataset was created to overcome the limitations of existing public datasets for pretraining, which are often constrained in size and diversity (e.g., TCGA primarily contains cancer slides) (s41591-024-02857-3.pdf, p. 2, 14). The motivation was to build a dataset large and varied enough to train a true foundation model capable of learning generalizable representations of tissue morphology for a wide array of downstream applications (s41591-024-02857-3.pdf, p. 14).

### Preprocessing:
The preprocessing pipeline for creating the Mass-100K patch dataset involved:
1.  **Tissue Segmentation:** The CLAM toolbox was used to perform tissue segmentation on low-resolution versions of the WSIs. This involved color space conversion (RGB to HSV), thresholding, and morphological operations to identify tissue regions and remove artifacts (s41591-024-02857-3.pdf, p. 14).
2.  **Patch Extraction:** Non-overlapping tissue patches of size 256x256 pixels were extracted at 20x magnification. For high-resolution fine-tuning, an additional set of 512x512 patches was also extracted (s41591-024-02857-3.pdf, p. 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results across individual factors.
*   **Performance per Task:** Figures 2f and 3a show UNI's performance compared to baselines across 15 slide-level and 11 ROI-level tasks, respectively. For example, on prostate ISUP grading (PANDA), UNI achieves a quadratic weighted Cohen's κ of 0.946, outperforming the next-best model (s41591-024-02857-3.pdf, p. 4-6).
*   **Performance by Data Scale:** Figures 2c and 2e show that UNI's top-1 accuracy on the OT-43 and OT-108 tasks monotonically increases as the pretraining data size grows from Mass-1K to Mass-22K to Mass-100K (s41591-024-02857-3.pdf, p. 4).
*   **Performance by Model Scale:** The paper notes that the ViT-L architecture consistently outperforms the ViT-B architecture when scaled to larger datasets (s41591-024-02857-3.pdf, p. 2).
*   **Performance by Image Resolution:** Figure 3d shows that UNI's performance on BRCA subtyping is more robust to changes in image resolution compared to other models, which show significant performance degradation at higher resolutions (s41591-024-02857-3.pdf, p. 6).
*   **Performance on Rare Diseases:** The paper highlights that UNI provides the largest performance gains on tasks involving rare cancer types, such as the 30 rare brain tumor diagnoses in the EBRAINS dataset and the 90 rare cancer types in the OT-108 benchmark (s41591-024-02857-3.pdf, p. 5, 9).

### Intersectional results:
The paper analyzes performance across combinations of factors, such as disease subtype and data source.
*   **NSCLC Subtyping (TCGA vs. CPTAC):** On NSCLC subtyping, the REMEDIS model outperforms UNI on the in-domain TCGA test set (97.3% vs 94.7%), but UNI significantly outperforms REMEDIS on the external CPTAC evaluation cohort (96.3% vs 79.0%), demonstrating UNI's superior out-of-domain generalization (s41591-024-02857-3.pdf, p. 5).
*   **Glioma Prediction (TCGA vs. EBRAINS):** Similarly, for glioma IDH1 mutation prediction, CTransPath and REMEDIS perform better on the in-domain TCGA test set, but UNI outperforms them on the external EBRAINS cohort (85.6% vs 83.6% and 79.2%) (s41591-024-02857-3.pdf, p. 5).
*   **OncoTree Classification:** The model was evaluated on classifying 108 cancer subtypes across 17 organ systems, an inherently intersectional task. UNI significantly outperformed all baselines on this task (s41591-024-02857-3.pdf, p. 2-3).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Downstream experiments (which simulate a deployment or fine-tuning scenario) were conducted on **single 24 GB NVIDIA 3090 GPUs** (s41591-024-02857-3.pdf, p. 21, 36).

### Training or Fine-tuning Requirements:
The self-supervised pretraining of UNI was computationally intensive and required a high-performance computing cluster. The hardware used was **4 nodes, each with 8x 80 GB NVIDIA A100 GPUs**, configured for multi-GPU, multi-node training (s41591-024-02857-3.pdf, p. 21, 36).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Governance:** The study was approved by the Mass General Brigham institutional review board. All internal patient data, including WSIs and reports, were de-identified prior to analysis. Informed consent was waived for the retrospective analysis of archival pathology data (s41591-024-02857-3.pdf, p. 14, 36).
*   **Sensitive Data:** The pretraining dataset (Mass-100K) was built from de-identified clinical pathology slides. The Reporting Summary notes that for the in-house data, the aggregate distribution of self-reported sex was 3080 Female and 2474 Male, but this information was not used as a covariate in any analysis. Covariates for race, ethnicity, or other social groupings were not collected or used (s41591-024-02857-3.pdf, p. 36).
*   **Risks and Mitigation:**
    *   **Bias:** The paper acknowledges the risk of biases such as "data contamination and image acquisition shift" if a model is reused across many applications, which could have a "disparate impact on diverse populations" (s41591-024-02857-3.pdf, p. 10). To mitigate this, the model was pretrained on a diverse multi-source dataset (MGH, BWH, GTEx) and extensively evaluated on external cohorts to test for generalization and robustness (s41591-024-02857-3.pdf, p. 5, 14).
    *   **Benefit to Underrepresented Groups:** A key ethical consideration was the model's utility for rare and underrepresented diseases, which often lack sufficient data to train bespoke models. The development of UNI addresses this challenge, showing strong performance on 90 rare cancer types, which could help democratize access to high-quality diagnostic AI (s41591-024-02857-3.pdf, p. 9).
*   **Misuse:** As a powerful foundation model, potential misuse is a risk. The model is released for "academic research purposes," which limits its application in unvalidated commercial or clinical settings (s41591-024-02857-3.pdf, p. 22).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The authors identify several limitations of the current model and study:
*   **Architectural Limitations:** The standard Vision Transformer architecture used in UNI lacks vision-specific inductive biases, which may limit its performance on dense prediction tasks like cell segmentation compared to hierarchical or convolutional models (s41591-024-02857-3.pdf, p. 10).
*   **Model Scale:** The study did not evaluate the even larger ViT-Giant architecture, which would likely yield better performance but requires significantly more computational resources for pretraining (s41591-024-02857-3.pdf, p. 10).
*   **Scope of Evaluation:** The 34 evaluation tasks, while extensive, do not cover all areas of pathology. Clinical tasks in cytopathology or hematopathology were not represented (s41591-024-02857-3.pdf, p. 10).
*   **Hyperparameter Tuning:** For fair comparison of encoder backbones, hyperparameters for downstream tasks were fixed and not extensively tuned for each specific task, which may leave some performance gains on the table (s41591-024-02857-3.pdf, p. 10).
*   **Model Modality:** UNI is a unimodal (vision-only) and ROI-level model. It cannot integrate other data modalities, and it is not a native slide-level model (s41591-024-02857-3.pdf, p. 10).

### Recommendations:
*   **Use Case:** UNI is recommended as a strong starting point or building block for developing AI models in computational pathology, especially for tasks with limited labeled data or those involving rare diseases (s41591-024-02857-3.pdf, p. 9).
*   **Future Research:** The authors suggest that future work should focus on using UNI as a building block for slide-level self-supervised models and generalist slide-level pathology AI (s41591-024-02857-3.pdf, p. 10).
*   **Responsible Development:** The authors recommend that CPath practitioners use the study's findings on scaling laws and algorithm choice to guide the development of their own foundation models on private, in-house data collections (s41591-024-02857-3.pdf, p. 9).
*   **Expectation Management:** Users should be aware that labels like "foundation model" can create misleading expectations, and like any model, UNI has specific strengths and limitations (s41591-024-02857-3.pdf, p. 10).