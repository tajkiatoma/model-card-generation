## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, named UNI, was developed by a team of researchers from various institutions, including:
*   Department of Pathology, Brigham and Women's Hospital, Harvard Medical School, Boston, MA, USA
*   Department of Pathology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA
*   Cancer Program, Broad Institute of Harvard and MIT, Cambridge, MA, USA
*   Cancer Data Science Program, Dana-Farber Cancer Institute, Boston, MA, USA
*   Department of Biomedical Informatics, Harvard Medical School, Boston, MA, USA
*   Harvard John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA
*   Electrical Engineering and Computer Science, Massachusetts Institute of Technology (MIT), Cambridge, MA, USA
*   Health Sciences and Technology, Harvard-MIT, Cambridge, MA, USA
*   Department of Systems Biology, Harvard University, Cambridge, MA, USA
*   Harvard Data Science Initiative, Harvard University, Cambridge, MA, USA

The lead authors are Richard J. Chen, Tong Ding, Ming Y. Lu, and Drew F. K. Williamson. The research was supervised by Faisal Mahmood (Towards a general-purpose foundation model for computational pathology, Page 1, 13).

### Model date:
The development timeline for the associated academic paper is as follows:
*   **Received:** 28 August 2023
*   **Accepted:** 5 February 2024
*   **Published online:** 19 March 2024
(Towards a general-purpose foundation model for computational pathology, Page 1).

### Model version:
The model is named UNI. The primary version is a Vision Transformer-Large (ViT-L) model pretrained on the Mass-100K dataset (Towards a general-purpose foundation model for computational pathology, Page 2).

Several ablations and variations were created to assess scaling trends, including:
*   **Architecture variations:** A Vision Transformer-Base (ViT-B) version was also trained (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Training data variations:** The model was pretrained on subsets of the full dataset to evaluate data scaling. These versions are based on the Mass-1K (1 million images) and Mass-22K (16 million images) datasets, in addition to the full Mass-100K (100 million images) dataset (Towards a general-purpose foundation model for computational pathology, Page 2).

UNI outperforms previous state-of-the-art models in computational pathology, such as CTransPath and REMEDIS, across 34 clinical tasks (Towards a general-purpose foundation model for computational pathology, Page 2).

### Model type:
UNI is a general-purpose, self-supervised vision encoder for computational pathology (CPath) (Towards a general-purpose foundation model for computational pathology, Page 2).

*   **Architecture:** It is a large Vision Transformer (ViT-L) (Towards a general-purpose foundation model for computational pathology, Page 2). The specific architecture is `vit_large_patch16_224` (config.json).
*   **Model Size:** The model has 1024 features (`num_features`) (config.json).
*   **Functionality:** The model takes histopathology images as input and generates feature representations (embeddings) that can be used for a wide range of downstream tasks, including classification, segmentation, and retrieval (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Context Length:** The model supports dynamic image sizes (`dynamic_img_size: true`) and is not limited to a fixed input size (`fixed_input_size: false`) (config.json). It was evaluated on image resolutions from 224x224 up to 1,792x1,792 pixels (Towards a general-purpose foundation model for computational pathology, Page 7).

### Training details:
UNI was pretrained using a self-supervised learning approach called DINOv2 on the Mass-100K dataset (Towards a general-purpose foundation model for computational pathology, Page 2).

*   **Algorithm:** The DINOv2 algorithm is based on student-teacher knowledge distillation and utilizes two main loss objectives:
    1.  **Self-distillation loss:** An alignment loss that minimizes the predictive categorical distributions between the student and teacher networks on different augmented views of the same image.
    2.  **Masked image modeling loss:** A reconstruction loss where the model is trained to predict masked regions of an input image based on the remaining context.
    (Towards a general-purpose foundation model for computational pathology, Page 3, 14).
*   **Training Iterations:** The model was trained for 125,000 iterations, with high-resolution fine-tuning conducted on the last 12,500 iterations (Towards a general-purpose foundation model for computational pathology, Page 2, 15).

### Paper or other resource for more information:
*   **Primary Paper:** Chen, R.J., Ding, T., Lu, M.Y. et al. "Towards a general-purpose foundation model for computational pathology." *Nature Medicine* 30, 850–862 (2024). The paper provides a comprehensive overview of the model's development, training, and extensive evaluation. It can be accessed at: https://doi.org/10.1038/s41591-024-02857-3 (Towards a general-purpose foundation model for computational pathology, Page 1).
*   **Code Repository:** Code and model weights for academic research are available at: https://github.com/mahmoodlab/UNI (Towards a general-purpose foundation model for computational pathology, Page 22).

### Citation details:
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
(Derived from Towards a general-purpose foundation model for computational pathology, Page 1).

### License:
The model is released under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license (CC BY-NC-ND 4.0) (config.json).

### Contact:
For correspondence and requests for materials, contact Faisal Mahmood at `faisalmahmood@bwh.harvard.edu` (Towards a general-purpose foundation model for computational pathology, Page 1, 13, 24). An additional contact email for one of the lead authors is `richardchen@g.harvard.edu` (Additional emails screenshot).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
UNI is a foundation model designed for a wide range of computational pathology (CPath) tasks on H&E-stained whole-slide images (WSIs) (Towards a general-purpose foundation model for computational pathology, Page 1). Its primary purpose is to serve as a powerful, general-purpose feature extractor, enabling data-efficient development of AI models for anatomic pathology (Towards a general-purpose foundation model for computational pathology, Page 1).

The model's capabilities have been demonstrated on 34 clinical tasks, including:
*   **ROI-level tasks:** Classification, segmentation, and image retrieval (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Slide-level tasks:** Weakly supervised classification (e.g., cancer subtyping) (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Specific Applications:**
    *   Cancer detection (primary and metastatic) and subtyping (up to 108 cancer types).
    *   Cancer grading (e.g., prostate ISUP grading).
    *   Biomarker and molecular alteration prediction.
    *   Organ transplant assessment.
    (Towards a general-purpose foundation model for computational pathology, Page 2).

The model takes histopathology image patches as input and outputs a 1024-dimensional feature vector (embedding) that can be used by downstream models (config.json; Towards a general-purpose foundation model for computational pathology, Page 15).

### Primary intended users:
The primary intended users are AI researchers, developers, and clinicians in the field of computational pathology. The model is designed to facilitate the creation of specialized AI tools for diagnostically challenging tasks and clinical workflows (Towards a general-purpose foundation model for computational pathology, Page 1).

### Out-of-scope uses:
The model has several known limitations and out-of-scope applications:
*   **Non-Histopathology Tasks:** The model is trained specifically on H&E-stained tissue images and is not intended for use on natural images or other medical imaging modalities (Towards a general-purpose foundation model for computational pathology, Page 1).
*   **Non-H&E Stains:** The training data consists of H&E-stained WSIs, and its performance on other types of stains is not evaluated (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Multimodal Applications:** UNI is a unimodal (vision-only) model. Multimodal tasks, such as cross-modal retrieval between images and text or visual question answering, are out of scope (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Direct Slide- or Patient-Level Prediction:** UNI is an ROI-level (patch-level) model. While its features can be aggregated for slide-level tasks (e.g., via Multiple Instance Learning), it is not an end-to-end slide-level or patient-level model itself (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Cytopathology and Hematopathology:** The evaluation tasks do not include applications in cytopathology or hematopathology (Towards a general-purpose foundation model for computational pathology, Page 10).

---

## How to Use
This section outlines how to use the model.

The primary way to use UNI is as a feature extractor. The model's weights are frozen, and it is used to convert input image patches into fixed-size embeddings. These embeddings can then be used for various downstream tasks (Towards a general-purpose foundation model for computational pathology, Page 14).

**Input Preprocessing:**
Input images should be normalized using the standard ImageNet mean and standard deviation:
*   **Mean:** `[0.485, 0.456, 0.406]`
*   **Std:** `[0.229, 0.224, 0.225]`
(config.json).

The model was typically evaluated on 224x224 pixel image patches, but it supports dynamic image sizes (config.json; Towards a general-purpose foundation model for computational pathology, Page 15).

**Example Use Cases:**
1.  **Weakly Supervised Slide Classification:**
    *   Extract features for all tissue patches from a Whole-Slide Image (WSI).
    *   Use these patch embeddings as input to a Multiple Instance Learning (MIL) model, such as ABMIL, to predict a slide-level label.
    (Towards a general-purpose foundation model for computational pathology, Page 15).
2.  **ROI-Level Classification:**
    *   Extract features from Regions of Interest (ROIs).
    *   Train a simple linear classifier (e.g., logistic regression) or use a non-parametric method (e.g., K-Nearest Neighbors) on top of the extracted features.
    (Towards a general-purpose foundation model for computational pathology, Page 5, 16).
3.  **Few-Shot Prototyping:**
    *   For a new classification task, extract features for a few labeled examples ("shots") per class.
    *   Average the features for each class to create a "class prototype".
    *   Classify new, unseen images by finding the nearest class prototype based on Euclidean distance.
    (Towards a general-purpose foundation model for computational pathology, Page 7, 8).

Detailed code and usage examples are available in the official repository: https://github.com/mahmoodlab/UNI (Towards a general-purpose foundation model for computational pathology, Page 22).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data Diversity and Scale:** The model's generalization capabilities are highly dependent on the size and diversity of the pretraining data. Performance improves monotonically as the pretraining dataset size increases from Mass-1K to Mass-100K (Towards a general-purpose foundation model for computational pathology, Page 2, 4).
*   **Tissue and Cancer Type:** The model was trained on 20 major tissue types and evaluated on tasks involving up to 108 different cancer types. Its performance may vary across different histological contexts (Towards a general-purpose foundation model for computational pathology, Page 1, 2).
*   **Image Resolution:** Image resizing can alter morphological features. UNI was shown to be robust to changes in image resolution, outperforming other models on high-resolution inputs, suggesting it can encode meaningful features at various magnifications (Towards a general-purpose foundation model for computational pathology, Page 7).
*   **H&E Stain Variability:** Variation in H&E staining across different labs and scanners can affect model performance, particularly in few-shot learning scenarios where prototypes might be sensitive to the stain characteristics of the selected examples (Towards a general-purpose foundation model for computational pathology, Page 9).

### Evaluation factors:
The model was evaluated across several of the relevant factors:
*   **Data Scale:** Performance was explicitly compared for models trained on Mass-1K, Mass-22K, and Mass-100K datasets (Towards a general-purpose foundation model for computational pathology, Page 4, Fig 2c,e).
*   **Model Scale:** Performance was compared between ViT-Base and ViT-Large architectures (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Task Diversity:** The model was evaluated on 34 distinct tasks spanning ROI classification, slide classification, segmentation, and retrieval to assess its versatility (Towards a general-purpose foundation model for computational pathology, Page 1).
*   **Image Resolution:** A specific analysis was conducted to evaluate the model's performance on BRCA subtyping and CRC polyp classification at multiple image resolutions (from 224² to 1,792² pixels) (Towards a general-purpose foundation model for computational pathology, Page 7).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A variety of metrics were used depending on the task:
*   **Classification:**
    *   **Area Under the Receiver Operating Characteristic curve (AUROC):** Used for multi-class slide classification tasks (e.g., OT-43, OT-108) (Towards a general-purpose foundation model for computational pathology, Page 2).
    *   **Top-K Accuracy:** Reported for tasks with many classes, such as OT-108 (K=1, 3, 5) (Towards a general-purpose foundation model for computational pathology, Page 2).
    *   **Balanced Accuracy:** Used for ROI-level classification to account for class imbalance (Towards a general-purpose foundation model for computational pathology, Page 5).
    *   **Weighted F1 Score:** Used for ROI and slide classification tasks (Towards a general-purpose foundation model for computational pathology, Page 2, 5).
    *   **Quadratic Weighted Cohen's Kappa:** Used for ordinal classification tasks like prostate ISUP grading (Towards a general-purpose foundation model for computational pathology, Page 4, Fig 2 caption).
*   **Retrieval:**
    *   **Accuracy@K (Acc@K):** Measures if a correct item is within the top-K retrieved results (K=1, 3, 5) (Towards a general-purpose foundation model for computational pathology, Page 7).
    *   **Majority Vote Accuracy@5 (MVAcc@5):** A stricter metric where the majority class of the top-5 retrieved images must match the query's class (Towards a general-purpose foundation model for computational pathology, Page 7).
*   **Segmentation:**
    *   **Dice Score:** Used as the primary evaluation metric for cell type segmentation (Towards a general-purpose foundation model for computational pathology, Page 7).

### Decision thresholds:
Insufficient information

### Variation approaches:
*   **Statistical Significance:** A two-sided paired permutation test with 1,000 permutations was used to assess the statistical significance of performance differences between models (Towards a general-purpose foundation model for computational pathology, Page 17).
*   **Confidence Intervals:** 95% confidence intervals for performance metrics were estimated using non-parametric bootstrapping with 1,000 replicates (Towards a general-purpose foundation model for computational pathology, Page 17).
*   **Few-Shot Evaluation:** For few-shot learning experiments, results are reported as box plots showing the distribution of performance over multiple runs (5 runs for slide-level, 1,000 runs for ROI-level) with randomly sampled support sets to account for sampling variability (Towards a general-purpose foundation model for computational pathology, Page 17).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of 34 public and in-house datasets. Key examples include:
*   **OncoTree Classification (OT-43, OT-108):** An in-house dataset from Brigham and Women's Hospital (BWH) with 5,564 WSIs across 43 cancer types and 108 OncoTree codes (Towards a general-purpose foundation model for computational pathology, Page 2, 17).
*   **CAMELYON16:** A public dataset for breast cancer metastasis detection in lymph nodes (399 WSIs) (Towards a general-purpose foundation model for computational pathology, Page 18).
*   **PANDA:** A public challenge dataset for prostate cancer ISUP grading (9,555 WSIs) (Towards a general-purpose foundation model for computational pathology, Page 19).
*   **TCGA (The Cancer Genome Atlas):** Various subsets were used for tasks like pan-cancer classification, NSCLC subtyping, and glioma mutation prediction (Towards a general-purpose foundation model for computational pathology, Page 18, 19, 21).
*   **EBRAINS Digital Tumor Atlas:** A public dataset for fine-grained brain tumor subtyping (2,319 WSIs) (Towards a general-purpose foundation model for computational pathology, Page 19).
*   **SegPath:** The largest public ROI-level segmentation dataset, used for segmenting eight major cell types in tumor tissue (158,687 ROIs) (Towards a general-purpose foundation model for computational pathology, Page 7, 21).

A complete list of datasets and links to their sources is provided in the "Data availability" section and Supplementary Table 73 of the associated paper (Towards a general-purpose foundation model for computational pathology, Page 22).

### Motivation:
The evaluation datasets were chosen to be comprehensive and diverse, covering a wide range of tasks, tissue types, and diagnostic difficulties. This was done to rigorously assess the model's generalization capabilities and demonstrate its potential as a true "foundation model" for the field of computational pathology (Towards a general-purpose foundation model for computational pathology, Page 1, 2). Using external public datasets also allows for comparison with other state-of-the-art models and leaderboards (Towards a general-purpose foundation model for computational pathology, Page 7).

### Preprocessing:
For most evaluation tasks, a standardized preprocessing pipeline was applied:
*   **Patching:** For slide-level tasks, WSIs were segmented into non-overlapping tissue patches (Towards a general-purpose foundation model for computational pathology, Page 15).
*   **Resizing:** Image patches or ROIs were resized to 224 × 224 pixels for feature extraction (Towards a general-purpose foundation model for computational pathology, Page 15).
*   **Normalization:** All images were normalized using the ImageNet mean and standard deviation (Towards a general-purpose foundation model for computational pathology, Page 15).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
UNI was pretrained on **Mass-100K**, a large-scale, diverse dataset curated for this study.
*   **Size:** It contains over 100 million tissue image patches (>77 TB of data) sampled from 100,426 diagnostic H&E-stained WSIs (Towards a general-purpose foundation model for computational pathology, Page 1).
*   **Source:** The WSIs were collected from three main sources:
    1.  Massachusetts General Hospital (MGH) (in-house)
    2.  Brigham and Women's Hospital (BWH) (in-house)
    3.  The Genotype-Tissue Expression (GTEx) consortium (public)
    (Towards a general-purpose foundation model for computational pathology, Page 2).
*   **Diversity:** The dataset spans 20 major tissue types, including both cancerous and normal tissue (Towards a general-purpose foundation model for computational pathology, Page 1, 3). Public datasets like TCGA were purposefully excluded from pretraining to allow for unbiased external evaluation (Towards a general-purpose foundation model for computational pathology, Page 14).

### Motivation:
The Mass-100K dataset was created to address a key limitation of prior models in CPath, which were often trained on smaller, less diverse datasets (like TCGA alone). The motivation was to leverage a massive and varied data source to train a model with strong generalization capabilities that could transfer effectively to a wide range of unseen tasks and clinical settings (Towards a general-purpose foundation model for computational pathology, Page 2).

### Preprocessing:
The preprocessing pipeline for creating the Mass-100K dataset involved:
1.  **Tissue Segmentation:** A tissue segmentation algorithm (from the CLAM toolbox) was applied to each WSI at low resolution to identify tissue regions (Towards a general-purpose foundation model for computational pathology, Page 14).
2.  **Patch Extraction:** Non-overlapping 256 × 256 pixel tissue patches were extracted from the segmented regions at ×20 magnification. For high-resolution fine-tuning, additional 512 × 512 pixel patches were also extracted (Towards a general-purpose foundation model for computational pathology, Page 14).
3.  **Data Augmentation:** During training with the DINOv2 algorithm, two augmented "views" of each image patch are created for the student-teacher learning process (Towards a general-purpose foundation model for computational pathology, Page 14).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results broken down by various factors.
*   **By Task:** Performance is reported for each of the 34 evaluation tasks. For example, on the 15 slide-level tasks, UNI shows average performance increases of +26.4% over ResNet-50, +8.3% over CTransPath, and +10.0% over REMEDIS (Towards a general-purpose foundation model for computational pathology, Page 4, 5). On 11 ROI-level tasks, UNI shows average performance increases of +18.8% over ResNet-50, +7.58% over CTransPath, and +5.75% over REMEDIS (Towards a general-purpose foundation model for computational pathology, Page 5, 6).
*   **By Data Scale:** The impact of pretraining data size was analyzed on the OT-43 and OT-108 tasks. Scaling from Mass-1K to Mass-22K resulted in a +4.2% top-1 accuracy increase on OT-43. Scaling further from Mass-22K to Mass-100K yielded an additional +3.7% increase (Towards a general-purpose foundation model for computational pathology, Page 2, 4).
*   **By Image Resolution:** On the BRCA subtyping task, UNI's performance drop when moving from 224² to 1,344² pixel images was -6.3%, compared to much larger drops of -18.8% for CTransPath and -32.5% for REMEDIS, demonstrating its superior robustness to resolution changes (Towards a general-purpose foundation model for computational pathology, Page 7).

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
*   **Pretraining:** The large-scale pretraining of UNI on the Mass-100K dataset was performed on a high-performance computing cluster using **4 nodes, each with 8x 80GB NVIDIA A100 GPUs** (Towards a general-purpose foundation model for computational pathology, Page 21).
*   **Downstream Tasks:** All downstream experiments (e.g., training MIL models or linear probes on the extracted features) were conducted on **single 24GB NVIDIA 3090 GPUs** (Towards a general-purpose foundation model for computational pathology, Page 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Governance:** The use of internal patient data was approved by the Mass General Brigham institutional review board. All data, including pathology images and reports, were de-identified prior to analysis. Informed consent was waived for this retrospective study (Towards a general-purpose foundation model for computational pathology, Page 14; Reporting Summary, Page 36).
*   **Potential for Bias:** The developers acknowledge that biases related to data sources, such as "data contamination and image acquisition shift," should be studied further, especially if the model is applied across diverse populations where it could have a disparate impact (Towards a general-purpose foundation model for computational pathology, Page 10). The training data's demographic breakdown was not used in the analysis, but an aggregate of self-reported sex for the in-house data was provided (3080 Female, 2474 Male) (Reporting Summary, Page 36).
*   **Risk Mitigation:** To mitigate data leakage and produce a more generalizable model, the pretraining dataset (Mass-100K) was intentionally curated to not overlap significantly with most public histology collections used for evaluation (Towards a general-purpose foundation model for computational pathology, Page 10, 14).
*   **Beneficence:** A key ethical benefit of the model is its strong performance in classifying rare and underrepresented diseases. This could help address health disparities by enabling the development of AI tools for conditions that are often overlooked due to data scarcity (Towards a general-purpose foundation model for computational pathology, Page 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers highlight several limitations of the current model:
*   **Architecture Limitations:** As a standard Vision Transformer, UNI lacks vision-specific inductive biases, which may limit its performance on dense prediction tasks like segmentation compared to hierarchical or convolutional architectures (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Scope of Evaluation:** The study did not evaluate the largest ViT-Giant architecture, which could potentially offer better performance at the cost of more computational resources. Furthermore, clinical tasks in areas like cytopathology and hematopathology were not included in the evaluation (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Hyperparameter Tuning:** For the broad evaluation across 34 tasks, hyperparameters were fixed. Further task-specific tuning could likely improve performance (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Model Modality:** UNI is a unimodal (vision-only) and ROI-level model. It is not designed for multimodal tasks or for direct end-to-end slide-level analysis (Towards a general-purpose foundation model for computational pathology, Page 10).

### Recommendations:
*   **Use as a Foundation:** Users are encouraged to leverage UNI as a strong foundation for building more specialized models. The paper suggests a research shift away from developing task-specific models from scratch and towards using generalist models like UNI (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **Future Development:** The authors recommend future work focus on using UNI as a building block for developing slide-level self-supervised models and more general pathology AI systems (Towards a general-purpose foundation model for computational pathology, Page 10).
*   **In-House Model Development:** The scaling laws and principles demonstrated in the development of UNI are intended to "guide CPath practitioners in developing their own foundation models using private in-house slide collections" (Towards a general-purpose foundation model for computational pathology, Page 9).