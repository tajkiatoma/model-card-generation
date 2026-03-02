## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, UNI, was developed by a team of researchers primarily from the Mahmood Lab. Key institutions involved include:
*   Department of Pathology, Brigham and Women's Hospital, Harvard Medical School, Boston, MA, USA
*   Department of Pathology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA
*   Cancer Program, Broad Institute of Harvard and MIT, Cambridge, MA, USA
*   Cancer Data Science Program, Dana-Farber Cancer Institute, Boston, MA, USA
*   Department of Biomedical Informatics, Harvard Medical School, Boston, MA, USA
*   Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA

The lead authors are Richard J. Chen, Tong Ding, Ming Y. Lu, and Drew F. K. Williamson. The research was supervised by Faisal Mahmood (Paper, page 1).

### Model date:
The development timeline, based on the associated academic paper, is as follows:
*   **Paper Received:** 28 August 2023
*   **Paper Accepted:** 5 February 2024
*   **Paper Published Online:** 19 March 2024
(Paper, page 1)

### Model version:
The primary version of the model is referred to as UNI, which utilizes a Vision Transformer-Large (ViT-L) architecture pretrained on the Mass-100K dataset (Paper, page 2). The model's tag is `uni_mass100k` (config.json).

This version is the largest and most performant. The developers also created smaller versions for ablation studies to assess data and model scaling laws, including:
*   **UNI on Mass-22K:** Pretrained on a subset of 16 million images from 21,444 whole-slide images (WSIs).
*   **UNI on Mass-1K:** Pretrained on a smaller subset of 1 million images from 1,404 WSIs.
*   **UNI with ViT-Base:** A version using a smaller ViT-Base architecture to assess model size impact.

UNI consistently outperforms other state-of-the-art models in computational pathology, such as CTransPath and REMEDIS, across 34 clinical tasks (Paper, page 2).

### Model type:
UNI is a general-purpose, self-supervised vision encoder foundation model for computational pathology (Paper, page 1).

*   **Architecture:** The model is a large Vision Transformer (ViT-L) (Paper, page 2). The specific architecture is `vit_large_patch16_224`, which processes images by dividing them into non-overlapping patches of 16x16 pixels (config.json).
*   **Functionality:** It functions as a feature extractor, converting histopathology image patches into high-dimensional feature vectors that can be used for various downstream tasks (Paper, page 3, Figure 1d).
*   **Model Size:** The model outputs a feature vector of 1024 dimensions (`num_features`: 1024) (config.json).
*   **Supported Context Length:** The model was trained on 224x224 pixel images but supports dynamic image sizes (`dynamic_img_size`: true), with evaluations performed on resolutions up to 1,792x1,792 pixels by interpolating positional embeddings (config.json; Paper, page 7, 16).

### Training details:
UNI was pretrained on the Mass-100K dataset using the DINOv2 self-supervised learning algorithm. This approach does not require manual annotations and is based on a student-teacher knowledge distillation framework (Paper, page 3, 14).

The training process involves two main loss objectives:
1.  **Self-Distillation Loss (Alignment Loss):** The student network is trained to match the output of the teacher network on different augmented views of the same image. This encourages the model to learn view-invariant representations (Paper, page 3, Figure 1b; page 14).
2.  **Masked Image Modeling Loss (Reconstruction Loss):** The model is trained to predict masked regions of an input image based on the visible context, using an online tokenizer provided by the teacher network. This helps the model learn high-level visual features and context (Paper, page 3, Figure 1b; page 14).

The model was pretrained for 125,000 iterations, with high-resolution fine-tuning conducted on the last 12,500 iterations (Paper, page 2, 15).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   **Title:** Towards a general-purpose foundation model for computational pathology
*   **Authors:** Richard J. Chen, Tong Ding, Ming Y. Lu, et al.
*   **Journal:** *Nature Medicine*, Volume 30, pages 850–862 (2024)
*   **DOI:** [https://doi.org/10.1038/s41591-024-02857-3](https://doi.org/10.1038/s41591-024-02857-3)

The code and model weights are available for academic research at: [https://github.com/mahmoodlab/UNI](https://github.com/mahmoodlab/UNI) (Paper, page 22).

### Citation details:
To cite this model, please use the following BibTeX entry:
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
(Paper, page 1)

### License:
The model is released under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (`CC BY-NC-ND 4.0`) (config.json). The code and model weights are available for academic research purposes (Paper, page 22).

### Contact:
For correspondence and requests for materials, contact Faisal Mahmood at `faisalmahmood@bwh.harvard.edu` (Paper, page 1, 24). Additional contact can be made with Richard Chen at `richardchen@g.harvard.edu` (GitHub profile image).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is a foundation model designed for a wide range of computational pathology (CPath) tasks in anatomic pathology. It is intended to be used as a powerful, off-the-shelf feature extractor to build data-efficient AI models (Paper, page 1, 2).

Its capabilities include:
*   **Patch-level Classification:** Classifying small image patches, for example, to identify cancer subtypes like BRCA (Paper, page 3, Figure 1d).
*   **Patch-level Segmentation:** Delineating different cell or tissue types within an image patch (Paper, page 3, Figure 1d).
*   **Image Retrieval and Prototyping:** Finding visually and semantically similar tissue patches from a large database given a query image. This can be used for building few-shot classifiers (Paper, page 3, Figure 1d).
*   **Slide-level Classification:** When combined with an aggregator model (like an attention-based multiple instance learning algorithm), UNI's patch-level features can be used to classify whole-slide images (WSIs) (Paper, page 3, Figure 1d).

The model's input is a histopathology image patch (e.g., 224x224 pixels), and its output is a 1024-dimensional feature vector that captures the morphological characteristics of the tissue (config.json).

### Primary intended users:
The primary intended users are:
*   **Computational Pathology Researchers:** For developing and benchmarking new AI models for various pathology tasks.
*   **AI Developers:** For building clinical-grade AI tools for diagnostics, prognostics, and biomarker discovery.
*   **Pathologists:** As a potential component in future AI-assisted diagnostic workflows.
(Paper, page 1, 2)

### Out-of-scope uses:
The model has several limitations and is not intended for the following uses:
*   **Direct Clinical Decision-Making:** UNI is a research model and should not be used for making clinical diagnoses without further validation and regulatory approval.
*   **Multimodal Applications:** UNI is a unimodal (vision-only) model and does not support tasks that require integrating other data types like genomics or clinical text (Paper, page 10).
*   **Non-Histopathology Domains:** The model was trained exclusively on H&E-stained histopathology images. Its performance on other domains like cytopathology or hematopathology is unevaluated and not guaranteed (Paper, page 10).
*   **Direct Slide-Level Analysis:** UNI is an ROI-level model. It requires an additional aggregation mechanism to perform slide-level or patient-level tasks (Paper, page 10).

---

## How to Use
This section outlines how to use the model.

UNI is designed to be used as a frozen feature extractor. The typical workflow involves taking a histopathology image patch, preprocessing it, and feeding it into the UNI model to obtain a feature vector. This vector can then be used for various downstream machine learning tasks.

**Input-Output Structure:**
*   **Input:** An image patch of a histopathology slide (e.g., a NumPy array or PyTorch tensor). The model expects a 3-channel RGB image, typically resized to 224x224 pixels.
*   **Output:** A 1024-dimensional feature vector (a PyTorch tensor of shape `[1, 1024]`).

**Preprocessing:**
Input images should be normalized using the standard ImageNet mean and standard deviation:
*   `mean = [0.485, 0.456, 0.406]`
*   `std = [0.229, 0.224, 0.225]`
(config.json)

**Example Usage Paradigms:**

1.  **ROI-level Classification (Linear Probing):**
    *   Extract features for all image patches in a training dataset.
    *   Train a simple linear classifier (e.g., Logistic Regression) on these features and their corresponding labels.
    *   For a new image, extract its feature vector with UNI and use the trained linear classifier to predict the label.
    (Paper, page 5, 16)

2.  **Slide-level Classification (Weakly Supervised):**
    *   For a given whole-slide image (WSI), first segment the tissue regions and divide them into a bag of non-overlapping patches.
    *   Use UNI to extract a feature vector for each patch in the bag.
    *   Feed the bag of feature vectors into an aggregator model, such as an attention-based multiple instance learning (ABMIL) model, which is then trained to produce a single slide-level prediction.
    (Paper, page 2, 15)

**Example Outputs:**
The paper provides qualitative examples of UNI's performance. For instance, in prostate cancer tissue classification, the patch-level predictions generated from UNI's features show high concordance with ground-truth annotations provided by pathologists (Paper, page 6, Figure 3b; page 26, Extended Data Fig. 2).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance can be influenced by several factors inherent to histopathology data:
*   **Tissue and Organ Type:** The model was pretrained on a diverse set of 20 major tissue types to ensure broad applicability (Paper, page 1, Figure 1a). Its performance was evaluated across many different organs, including breast, colon, prostate, brain, and lung (Paper, page 3, Figure 1c).
*   **Disease Rarity:** The model's ability to classify rare diseases was a key consideration. The evaluation included tasks with up to 90 rare cancer types, where UNI showed significant performance gains over other models (Paper, page 9).
*   **Image Resolution:** Pathology tasks can be sensitive to image magnification. UNI's robustness to varying image resolutions was tested, showing less performance degradation at higher resolutions compared to other encoders (Paper, page 7).
*   **Stain Variability:** Hematoxylin and eosin (H&E) staining can vary significantly between labs and scanners. While not explicitly modeled, the large and diverse training set from multiple institutions (MGH, BWH, GTEx) is intended to provide robustness to such variations (Paper, page 2, 14).

### Evaluation factors:
The model was evaluated across a comprehensive set of 34 clinical tasks to analyze its performance against the relevant factors. These tasks were grouped by:
*   **Task Modality:** ROI-level classification, ROI-level segmentation, ROI retrieval, and slide-level classification (Paper, page 3, Figure 1d).
*   **Clinical Domain:** The tasks cover a wide range of applications, including cancer detection (CAMELYON16), cancer subtyping (BRCA, RCC, NSCLC), grading (Prostate ISUP), biomarker screening (CRC MSI), and organ transplant assessment (Heart transplant) (Paper, page 3, Figure 1c).
*   **Data Source and Potential Domain Shift:** For some tasks, the model was trained on one dataset (e.g., TCGA) and evaluated on external cohorts (e.g., CPTAC, EBRAINS) to assess out-of-domain generalization (Paper, page 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The choice of metric depends on the specific downstream task:
*   **Classification:**
    *   **Area Under the Receiver Operating Characteristic Curve (AUROC):** Used for binary and multi-class classification to measure discrimination performance independent of a decision threshold (Paper, page 3, 17).
    *   **Top-K Accuracy:** Used for multi-class tasks (e.g., OT-43, OT-108), where a prediction is correct if the true label is among the top K predicted labels (Paper, page 2, 17).
    *   **Balanced Accuracy:** The unweighted average of recall for each class, used for tasks with imbalanced classes (Paper, page 5, 17).
    *   **Weighted F1 Score:** The F1 score for each class, averaged and weighted by the number of true instances for each class (Paper, page 5, 17).
    *   **Quadratic Weighted Cohen's Kappa:** Used for ordinal classification tasks like prostate ISUP grading to measure agreement, with heavier penalties for larger errors (Paper, page 5, 17).
*   **Segmentation:**
    *   **Dice Score:** Used to measure the overlap between predicted and ground-truth segmentation masks (Paper, page 7, 17).
*   **Retrieval:**
    *   **Accuracy@K (Acc@K):** A retrieval is successful if at least one of the top-K retrieved images has the same class label as the query (Paper, page 7, 17).
    *   **Majority Vote Accuracy@5 (MVAcc@5):** A stricter metric where the majority class of the top-5 retrieved images must match the query's class (Paper, page 7, 17).

### Decision thresholds:
Insufficient information. The paper primarily uses threshold-independent metrics like AUROC or reports categorical accuracy metrics.

### Variation approaches:
To ensure robust measurements and quantify uncertainty, the following statistical methods were used:
*   **Bootstrapping:** 95% confidence intervals for performance metrics were estimated using non-parametric bootstrapping with 1,000 replicates (Paper, page 17).
*   **Repeated Experiments:** For few-shot learning evaluations, experiments were repeated over multiple runs (5 runs for slide-level, 1,000 for ROI-level) with different random samples of training data. Results are presented as box plots showing the distribution of outcomes (Paper, page 5, 17).
*   **Permutation Testing:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of performance differences between models (Paper, page 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
UNI was evaluated on 34 distinct tasks using a wide array of public and in-house datasets. A summary of key evaluation datasets includes:
*   **OncoTree Classification (OT-43, OT-108):** An in-house dataset from BWH with 5,564 WSIs for classifying 43 cancer types and 108 subtypes (Paper, page 2, 17).
*   **CAMELYON16:** Public dataset for breast cancer metastasis detection in lymph nodes (399 WSIs) (Paper, page 18).
*   **PANDA:** Public dataset for prostate cancer ISUP grading (9,555 WSIs) (Paper, page 19).
*   **EBRAINS Digital Tumor Atlas:** Public dataset for fine-grained brain tumor subtyping (2,319 WSIs) (Paper, page 19).
*   **TCGA (The Cancer Genome Atlas):** A large public resource used for multiple tasks, including NSCLC subtyping, RCC subtyping, and glioma biomarker prediction (Paper, page 18, 19).
*   **CPTAC (Clinical Proteomic Tumor Analysis Consortium):** Public datasets used as external validation cohorts for tasks like NSCLC and RCC subtyping (Paper, page 18).
*   **SegPath:** A public dataset for segmenting eight major cell types in tumor tissue (158,687 ROIs) (Paper, page 21).
*   **BWH-EMB:** An in-house dataset for cardiac transplant rejection assessment (5,021 WSIs) (Paper, page 19).
*   Other datasets include HunCRC, BRACS, CRC-100K, BACH, AGGC, and UniToPatho (Paper, page 18-21).

### Motivation:
The datasets were chosen to create a comprehensive and challenging benchmark that reflects the diversity of real-world anatomic pathology. The selection was motivated by the need to:
*   Assess generalization across many different tissue types and disease categories.
*   Evaluate performance on tasks of varying diagnostic difficulty, from binary classification to fine-grained subtyping of over 100 classes.
*   Test the model on both common and rare cancers.
*   Measure out-of-domain performance by using external validation cohorts.
(Paper, page 1, 2)

### Preprocessing:
For evaluation, a consistent preprocessing pipeline was applied:
*   **Image Resizing:** ROI images were typically resized to 224x224 pixels for feature extraction (Paper, page 15).
*   **Normalization:** All images were normalized using ImageNet mean and standard deviation (Paper, page 15).
*   **WSI Patching:** For slide-level tasks, the CLAM toolbox was used to perform tissue segmentation on low-resolution WSIs, followed by extraction of non-overlapping tissue patches at a specified magnification (Paper, page 15). For the OT-108 task, due to storage limitations, 200 representative patches per WSI were sampled via clustering (Paper, page 18).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
UNI was pretrained on **Mass-100K**, a large-scale, proprietary dataset curated by the developers (Paper, page 2).
*   **Size:** It contains over 100 million tissue patches (100,130,900 images) sampled from 100,426 diagnostic H&E-stained whole-slide images, totaling over 77 TB of data (Paper, page 1, 14).
*   **Source:** The WSIs were collected from three sources: Massachusetts General Hospital (MGH), Brigham and Women's Hospital (BWH), and the public Genotype-Tissue Expression (GTEx) consortium (Paper, page 2, 14).
*   **Diversity:** The dataset is highly diverse, spanning 20 major organ/tissue types, including lung, heart, kidney, bowel, brain, breast, and skin, among others. It includes cancerous tissue, normal tissue, and other pathologies (Paper, page 1, Figure 1a; page 9).

### Motivation:
The Mass-100K dataset was created to overcome the limitations of existing pretraining datasets in pathology, which are often limited in size and diversity (e.g., TCGA). The goal was to assemble a massive and varied dataset to train a true general-purpose foundation model that can learn robust representations and generalize well to a wide range of unseen tasks (Paper, page 2).

### Preprocessing:
The preprocessing of the WSIs for creating the Mass-100K patch dataset involved several steps using the CLAM toolbox:
1.  **Tissue Segmentation:** Tissue regions were identified on low-resolution versions of the WSIs by applying a binary threshold to the saturation channel of the HSV color space.
2.  **Contour Smoothing:** Morphological operations (closing, median blurring) were used to smooth tissue contours and remove small artifacts.
3.  **Patch Extraction:** Non-overlapping 256x256 pixel tissue patches were extracted from the segmented regions at x20 magnification. For high-resolution training, 512x512 pixel patches were also extracted.
(Paper, page 14)

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
UNI consistently outperformed other pretrained encoders (ResNet-50, CTransPath, REMEDIS) across nearly all 34 evaluated tasks.
*   **Slide-Level Classification:** Across 15 slide-level tasks, UNI showed average performance increases of +26.4% over ResNet-50, +8.3% over CTransPath, and +10.0% over REMEDIS. The improvements were particularly large on tasks with high diagnostic complexity or rare cancer types, such as brain tumor subtyping (Paper, page 5, Figure 2f).
*   **ROI-Level Classification:** Across 11 ROI-level tasks, UNI achieved average performance increases of +18.8% over ResNet-50, +7.58% over CTransPath, and +5.75% over REMEDIS using linear probing (Paper, page 5, Figure 3a).
*   **ROI-Level Segmentation:** On the SegPath dataset, UNI outperformed all other backbones on a majority of the 8 cell type segmentation tasks, achieving the highest overall average Dice score (Paper, page 7).
*   **Few-Shot Learning:** UNI demonstrated superior label efficiency. In many tasks, UNI using only 4 or 8 training examples per class outperformed other models trained on 32 or more examples (Paper, page 5, Figure 2g-j).

### Intersectional results:
The analysis includes results that examine performance across combinations of factors, such as task domain and data source.
*   **In-Domain vs. Out-of-Domain Performance:** The performance of models was compared on internal test sets (e.g., from TCGA) versus external, out-of-domain test sets (e.g., from CPTAC or EBRAINS). For NSCLC subtyping, REMEDIS performed better on the in-domain TCGA test set but UNI performed significantly better on the out-of-domain CPTAC set (96.3% vs 79.0%), suggesting UNI has better generalization capabilities (Paper, page 5).
*   **Performance on Rare Cancers:** UNI showed its largest performance gains on tasks involving rare diseases. On the OT-108 task, which includes 90 rare cancer types, UNI outperformed the next-best model (REMEDIS) by +10.8% in top-5 accuracy. Similarly, on the 30-class rare brain tumor subtyping task from EBRAINS, UNI outperformed REMEDIS by +16.1% (Paper, page 3, 5).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Downstream tasks and evaluations using the frozen UNI encoder were conducted on a **single NVIDIA 3090 GPU with 24 GB of VRAM** (Paper, page 21). This suggests that inference and fine-tuning of smaller downstream heads are feasible on consumer-grade to professional-grade GPUs.

### Training or Fine-tuning Requirements:
The full self-supervised pretraining of UNI is computationally intensive. It was performed on a high-performance computing cluster consisting of **4 nodes, each equipped with 8 NVIDIA A100 GPUs (80 GB VRAM each)**, using distributed data-parallel training (Paper, page 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Patient Privacy and Data Governance:** The in-house training data (Mass-100K) was collected under a protocol approved by the Mass General Brigham institutional review board. All patient data, including WSIs and reports, were de-identified prior to any analysis. For this retrospective study, informed consent was waived by the review board (Paper, page 14, 36).
*   **Potential for Bias:** The developers acknowledge that foundation models trained on large datasets can inherit biases. Potential sources of bias include data contamination (overlap between pretraining and public evaluation datasets) and image acquisition shift (differences in scanners and staining protocols). While Mass-100K was designed to not overlap significantly with public histology collections, the authors recommend that these biases "should be further studied if the same model is re-used across many applications, especially if it were to have a disparate impact on diverse populations" (Paper, page 10).
*   **Sensitive Data:** The training data consists of medical images, which are considered sensitive. The in-house OT-108 dataset included self-reported sex data (3080 Female, 2474 Male), but this was not used as a covariate in any analysis (Paper, page 36). No data on race or ethnicity was collected or used (Paper, page 36).
*   **Risk Mitigation:** The primary risk mitigation strategy for patient privacy was the de-identification of all data used for model development. By evaluating the model on a very broad range of 34 tasks, the developers aimed to create a robust and general-purpose tool, reducing the risk of a model that only performs well on a narrow, unrepresentative slice of the patient population.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers highlight several limitations of the current model:
*   **Architectural Limitations:** As a standard Vision Transformer, UNI lacks strong inductive biases for dense prediction tasks. While it performs well on segmentation, its performance gains are not as drastic as in classification tasks (Paper, page 10).
*   **Model Scale:** The study did not evaluate the even larger ViT-Giant architecture, which could potentially yield further performance improvements but would require more computational resources (Paper, page 10).
*   **Scope of Evaluation:** The 34 evaluation tasks, while extensive, do not cover all areas of pathology. Performance on tasks in cytopathology or hematopathology remains unknown (Paper, page 10).
*   **Unimodal Nature:** UNI is a vision-only model. It cannot perform multimodal tasks that integrate genomic, transcriptomic, or clinical text data (Paper, page 10).
*   **ROI-Level Focus:** UNI is fundamentally a patch-level (ROI) feature extractor. It is not, by itself, a slide-level or patient-level model and requires additional components for such tasks (Paper, page 10).

### Recommendations:
*   **Use as a Building Block:** Users are encouraged to use UNI as a strong feature-extractor backbone for building more complex, data-efficient models for specific clinical applications, including slide-level self-supervised models (Paper, page 10).
*   **Further Testing for Bias:** Users applying UNI in new contexts, especially for clinical deployment, should conduct further studies on potential biases related to data sources, image acquisition techniques, and performance across diverse patient populations (Paper, page 10).
*   **Shift Towards Generalist Models:** The authors hope that the success of UNI encourages a shift in the CPath field away from developing narrow, task-specific models and towards the creation of more generalist, reusable foundation models (Paper, page 10).