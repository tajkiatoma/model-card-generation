## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from IBM Research: Vijay Ekambaram, Nam H. Nguyen, Arindam Jati, Wesley M. Gifford, Pankaj Dayama, Chandra Reddy, Sumanta Mukherjee, and Jayant Kalagnanam (2401.03955.pdf, p. 1).

### Model date:
The work was submitted to arXiv on January 8, 2024, and was accepted at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024) (2401.03955.pdf, p. 1). The version of the paper provided is v8, dated November 7, 2024 (2401.03955.pdf, p. 1).

### Model version:
The paper introduces several variants of the Tiny Time Mixer (TTM) model, which differ in size, context length, and patch length (2401.03955.pdf, p. 7):
*   **TTM-Base (TTMB):** A 1M parameter model trained with a context length of 512 and a patch length of 64.
*   **TTM-Enhanced (TTME):** A 4M parameter model trained with a context length of 1024 and a patch length of 128.
*   **TTM-Advanced (TTMA):** A 5M parameter model trained with a context length of 1536 and a patch length of 128.
*   **Quick TTM (TTMQ):** A variant trained on a smaller dataset (~250 million samples) for secondary studies.

These models are significantly smaller and faster than other large pre-trained time series models like TimesFM, Moirai, and Chronos, while often providing more accurate forecasts (2401.03955.pdf, p. 2, Figure 1).

### Model type:
TTM is a compact, pre-trained model for multivariate time series forecasting (2401.03955.pdf, p. 1).

**Architecture:**
*   The model is based on the light-weight TSMixer architecture, which uses MLP-Mixer blocks interleaved with gated attention instead of the quadratic time-consuming self-attention blocks found in Transformers (2401.03955.pdf, p. 2).
*   It follows a multi-level architecture with four key components: a TTM backbone, a TTM decoder (10-20% of the backbone's size), a forecast head (linear layer), and an optional exogenous mixer to fuse exogenous data (2401.03955.pdf, p. 4).
*   TTM incorporates several architectural innovations to handle pre-training on diverse datasets with minimal model capacity:
    *   **Adaptive Patching (AP):** Different layers of the backbone operate at varying patch lengths and numbers of patches to aid generalization across datasets with different resolutions (2401.03955.pdf, p. 3, 5).
    *   **Resolution Prefix Tuning (RPT):** Explicitly embeds resolution information as a learnable prefix into the input data to facilitate resolution-conditioned modeling (2401.03955.pdf, p. 3, 5).

**Size and Context Length:**
*   Model sizes start from 1 million parameters (2401.03955.pdf, p. 1).
*   The primary variants have the following sizes: TTMB (1M), TTME (4M), and TTMA (5M) (2401.03955.pdf, p. 7).
*   Supported context lengths (sl) for these variants are 512, 1024, and 1536, respectively (2401.03955.pdf, p. 7).

### Training details:
TTM's methodology involves a two-stage process: pre-training and fine-tuning (2401.03955.pdf, p. 4).

**Pre-training:**
*   **Algorithm:** The model is pre-trained on a large collection of diverse public datasets with a direct forecasting objective using a Mean Squared Error (MSE) loss function (2401.03955.pdf, p. 4). The pre-training is done in a univariate fashion, where channels are treated independently (2401.03955.pdf, p. 4).
*   **Key Methodologies:**
    *   **Diverse Resolution Sampling (DRS):** A data augmentation technique used to create datasets at lower resolutions from high-resolution sources, balancing the volume of samples across resolutions and improving model coverage (2401.03955.pdf, p. 3, 5).
*   **Hyperparameters:** Standard pre-training configurations include:
    *   Patch length (pl): 64, 128, or 8 depending on context length.
    *   Number of backbone levels (L): 3.
    *   Number of TTM blocks per level (M): 2.
    *   Number of decoder layers: 2.
    *   Batch size (b): 4500.
    *   Epochs (ep): 20.
    *   Dropout (do): 0.4 (2401.03955.pdf, p. 21).

**Fine-tuning:**
*   During fine-tuning, the TTM backbone is frozen, and only the TTM head (decoder and forecast head) is updated on the target dataset (2401.03955.pdf, p. 6).
*   The decoder can be fine-tuned with channel mixing enabled to explicitly capture cross-channel correlations in multivariate data (2401.03955.pdf, p. 6).
*   An optional exogenous mixer block can be applied to incorporate known future values of external variables (2401.03955.pdf, p. 6).
*   Fine-tuning is highly efficient, requiring only 1 GPU or even a CPU (2401.03955.pdf, p. 7).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Vijay Ekambaram, et al. "Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series." arXiv preprint arXiv:2401.03955, 2024 (2401.03955.pdf).

The paper also provides links to the model's resources (2401.03955.pdf, p. 1):
*   **Source Code and Usage Scripts:** [https://github.com/ibm-granite/TSFM](https://github.com/ibm-granite/TSFM)
*   **Model Weights (Research Use):** [https://huggingface.co/ibm-granite/granite-ttm-1m-base](https://huggingface.co/ibm-granite/granite-ttm-1m-base)
*   **Model Weights (Enterprise Use, Apache License):**
    *   Initial TTMovariant: [https://huggingface.co/ibm/TTM](https://huggingface.co/ibm/TTM)
    *   Latest Variants (TTMB, TTME, TTMA): [https://huggingface.co/collections/ibm/ttm-667b34526f0373b737a1d513](https://huggingface.co/collections/ibm/ttm-667b34526f0373b737a1d513)

### Citation details:
A BibTeX citation for the paper can be constructed as follows:
```bibtex
@misc{ekambaram2024tiny,
      title={Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series}, 
      author={Vijay Ekambaram and Nam H. Nguyen and Arindam Jati and Wesley M. Gifford and Pankaj Dayama and Chandra Reddy and Sumanta Mukherjee and Jayant Kalagnanam},
      year={2024},
      eprint={2401.03955},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
(2401.03955.pdf, p. 1).

### License:
The model weights are available under different licenses depending on the intended use (2401.03955.pdf, p. 1):
*   **Research Use:** Model weights are available for reproducibility and research purposes. The specific license is not detailed in the paper but can be found at the provided link.
*   **Enterprise Use:** The latest variants (TTMB, TTME, TTMA) and the initial TTMovariant are available for enterprise use under the Apache license.

### Contact:
For questions or feedback, the corresponding author can be contacted via email: vijaye12@in.ibm.com (2401.03955.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of TTM is for zero-shot and few-shot forecasting of multivariate time series (2401.03955.pdf, p. 1). It is designed to predict future values for multiple interrelated time series based on their historical values (2401.03955.pdf, p. 1).

**Capabilities:**
*   **Zero-shot Forecasting:** The pre-trained model can be used directly to make forecasts on new, unseen datasets without any fine-tuning (2401.03955.pdf, p. 6).
*   **Few-shot Forecasting:** The model can be quickly fine-tuned on a small portion (e.g., 5-10%) of a target dataset to improve accuracy, which is useful in data-constrained scenarios (2401.03955.pdf, p. 6, 8).
*   **Full-shot Forecasting (Head Probing):** The model head can be fine-tuned on the entire training split of a target dataset for enhanced performance while keeping the backbone frozen (2401.03955.pdf, p. 6, 8).
*   **Handling Multivariate Correlations:** The model can explicitly capture cross-channel correlations during fine-tuning (2401.03955.pdf, p. 3, 6).
*   **Incorporating Exogenous Variables:** TTM can infuse signals from exogenous variables (i.e., channels that influence the target variables and have known future values) into the forecast (2401.03955.pdf, p. 3, 6).

**Input-Output Structure:**
*   **Input:** A multivariate time series `X` of length `sl` (context length) and `c` channels (2401.03955.pdf, p. 3).
*   **Output:** A forecast `Y` of future values for `c'` target channels over a forecast length `fl` (horizon) (2401.03955.pdf, p. 3).

The model is particularly well-suited for resource-constrained environments as it is lightweight and can be executed on CPU-only machines (2401.03955.pdf, p. 1).

### Primary intended users:
The primary intended users are researchers and developers in the field of time series analysis and forecasting. Given its efficiency and small size, it is also intended for practitioners in industrial settings who face resource and cost constraints (2401.03955.pdf, p. 2).

### Out-of-scope uses:
The paper identifies several out-of-scope uses and limitations (2401.03955.pdf, p. 26-27):
*   **Other Downstream Tasks:** TTM is currently focused solely on forecasting. It is not designed for other time series tasks such as classification, regression, or anomaly detection.
*   **Probabilistic Forecasting:** The model currently only supports point forecasting (predicting a single value for each future time step). It does not provide probabilistic forecasts (i.e., a distribution of possible future values).
*   **Automatic Context Length Adaptation:** The model is sensitive to context length, and different variants are optimized for different settings. It does not automatically adapt to dynamically varying context lengths.

---

## How to Use
This section outlines how to use the model.

The source code for the TTM model, along with usage scripts, is available in a public repository: [https://github.com/ibm-granite/TSFM](https://github.com/ibm-granite/TSFM) (2401.03955.pdf, p. 1).

The general workflow for using TTM involves selecting a pre-trained model variant and applying it to a target dataset in one of three ways (2401.03955.pdf, p. 6):
1.  **Zero-shot forecasting:** Use the pre-trained model directly on the test data.
2.  **Few-shot forecasting:** Fine-tune the TTM head on a small portion (5-10%) of the training data before evaluating on the test data.
3.  **Full-shot forecasting (head probing):** Fine-tune the TTM head on the entire training data before evaluating on the test data.

During fine-tuning, the backbone remains frozen. If the target data is multivariate and cross-channel correlations are important, the channel-mixer block in the decoder should be enabled. If the data contains exogenous variables, the exogenous mixer block should be used (2401.03955.pdf, p. 6).

The paper also describes two techniques for adapting a model pre-trained for one forecast length (FL) to another (2401.03955.pdf, p. 11):
*   **Pruning:** To adapt to a shorter FL, take a model trained on a longer FL and prune its output layer. This is recommended for wider adaptations (e.g., from FL=720 to FL=96).
*   **Recursive:** To adapt to a longer FL, take a model trained on a shorter FL and apply it recursively. This is recommended for shorter adaptations (e.g., from FL=96 to FL=192).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development of TTM acknowledges that pre-training in the time series domain is challenging due to the diverse nature of available datasets. Key factors that influence the model and its performance include (2401.03955.pdf, p. 2):
*   **Domain:** Datasets come from various domains such as weather, traffic, retail, and energy.
*   **Temporal Resolution:** The sampling rate of the time series can range from seconds to days.
*   **Data Length:** The length of available historical data varies significantly.
*   **Number of Channels:** The dimensionality of the multivariate time series differs across datasets.

### Evaluation factors:
The model's evaluation is performed across a variety of these factors to demonstrate its robustness and generalization capabilities. The evaluation datasets are specifically chosen to cover (2401.03955.pdf, p. 6, 19-20):
*   **Different Domains:** The D1 and D2 evaluation sets include data from electricity transformers (ETT), weather, electricity consumption (ECL), traffic, bike sharing, carbon capture, and IT services.
*   **Presence of Exogenous Variables:** The D2 dataset is used specifically to evaluate the model's ability to handle exogenous and control variables, a factor not present in the D1 datasets.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess forecast accuracy is the **Mean Squared Error (MSE)** (2401.03955.pdf, p. 6).

In addition, two relative improvement metrics are used to compare TTM with baseline models (2401.03955.pdf, p. 6):
*   **Forecast improvement percentage (f-imp(%)):** The percentage improvement in MSE of TTM over a baseline, averaged across all datasets.
*   **Size improvement metric (s-imp(X)):** The ratio of the baseline model's size (total parameters) to the TTM model's size.

### Decision thresholds:
Insufficient information. This is not applicable as the model performs regression (forecasting) rather than classification.

### Variation approaches:
Model performance is typically reported as the MSE averaged across multiple forecast lengths (FL) to provide a comprehensive assessment (e.g., FL ∈ {96, 192, 336, 720}) (2401.03955.pdf, p. 7, Table 1 caption). All model hyperparameters are chosen based on performance on a validation set, with final results reported on the test set (2401.03955.pdf, p. 7).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The evaluation was conducted on eleven public datasets, divided into two sets (D1 and D2) (2401.03955.pdf, p. 6, 20).

**Set D1:** Seven popular multivariate datasets used for zero/few/full-shot evaluation. They do not contain exogenous variables.
*   **ETT (ETTH1, ETTH2, ETTM1, ETTM2):** Data from electrical transformers, with 7 channels, collected at hourly (H) and 15-minute (M) intervals.
*   **Weather:** 21 channels of weather indicators collected at 10-minute intervals.
*   **Electricity (ECL):** Hourly electricity consumption data for 321 clients.
*   **Traffic:** Hourly road occupancy rates from 862 sensors on San Francisco Freeways.

**Set D2:** Four datasets used to evaluate performance on tasks with exogenous or control variables.
*   **Bike Sharing (BS):** Hourly bike rental counts in Washington D.C., with 14 channels (3 target, 11 exogenous).
*   **Carbon Capture Plant (CC):** Emission profiles from a carbon capture plant, with 8 channels (2 target, 5 control/exogenous).
*   **Application (APP):** Business KPIs and IT events from a cloud application, with 39 channels (4 target, 35 exogenous).
*   **Service (SER):** Similar to APP but at the service level, with 107 channels (72 target, 35 exogenous).

These datasets are available from the repository of the Autoformer paper (2401.03955.pdf, p. 20).

### Motivation:
*   **Set D1** was chosen because its constituent datasets have been consistently used in prior state-of-the-art forecasting literature, providing a standard benchmark for comparison (2401.03955.pdf, p. 6).
*   **Set D2** was chosen specifically to validate the effectiveness of TTM's decoder channel mixing and exogenous mixer module, as these datasets contain known exogenous or control variables, a feature lacking in D1 (2401.03955.pdf, p. 6).

### Preprocessing:
For the D1 datasets, the same train/validation/test splitting protocol from previous literature was used to ensure fair comparison (2401.03955.pdf, p. 20). The standard preprocessing step applied to all data before it enters the model is instance normalization, where each time series instance is normalized to have zero mean and unit standard deviation for each channel (2401.03955.pdf, p. 4). This process is reversed at the end before computing the loss (2401.03955.pdf, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
TTM was pre-trained on a large-scale dataset of approximately 1 billion samples derived from the Monash and LibCity data repositories (2401.03955.pdf, p. 6, 18). The datasets were chosen to be diverse in domain, resolution, and length. A full list of the source datasets is provided in Table 8 of the paper, including (2401.03955.pdf, p. 19):
*   **From Monash:** `kaggle_web_traffic`, `nn5_daily`, `solar_10_minutes`, `australian_electricity_demand`, `solar_4_seconds`, `wind_4_seconds`, `us_births`, `kdd_cup_2018`, `wind_farms_minutely`, `london_smart_meters`, and others.
*   **From LibCity:** `PEMS03`, `PEMS04`, `PEMS07`, `PEMS08`, `PEMS_BAY`, `LOS_LOOP`, and others.

The Monash datasets are available under a Creative Commons Attribution 4.0 International license, and the LibCity datasets used were released under an Apache 2.0 license (2401.03955.pdf, p. 19). The pre-training datasets have no overlap with the evaluation datasets (2401.03955.pdf, p. 19).

### Motivation:
The datasets were chosen to create a large and diverse pre-training corpus, which is essential for building a general foundation model for time series forecasting that can transfer learning to new, unseen tasks (2401.03955.pdf, p. 2). The paper emphasizes that the quality and resolution diversity of the pre-training data are more crucial than sheer quantity for achieving good generalization with a small model (2401.03955.pdf, p. 11).

### Preprocessing:
Several preprocessing steps were applied to the training data (2401.03955.pdf, p. 4, 5, 19):
*   **Univariate Transformation:** Multivariate datasets were transformed into independent univariate time series for the channel-independent pre-training stage.
*   **Temporal Cross-Validation:** A moving window technique was used to create (context, horizon) pairs for training.
*   **Instance Normalization:** Each sample was normalized to have zero mean and unit standard deviation.
*   **Patching:** The normalized time series was divided into non-overlapping patches.
*   **Diverse Resolution Sampling (DRS):** This data augmentation technique was applied to high-resolution datasets to generate new, lower-resolution time series by averaging or decimating samples. This increases the diversity of resolutions in the training data and helps prevent the model from being biased towards high-frequency data.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results broken down by dataset and model variant.
*   **Zero-shot performance:** Table 1 shows the zero-shot MSE of TTMB, TTME, and TTMA on the ETTH1, ETTH2, ETTM1, ETTM2, Weather, and Electricity datasets, comparing them against Moirai and TimesFM variants (2401.03955.pdf, p. 7). Table 2 provides similar comparisons against Chronos and Lag-llama (2401.03955.pdf, p. 8).
*   **Few-shot performance:** Table 4 presents the 5% few-shot MSE for each TTM variant on the D1 datasets, benchmarked against GPT4TS, Time-LLM, and other popular architectures (2401.03955.pdf, p. 9).
*   **Exogenous Variable Performance:** Table 6 shows the performance of TTMQ-CM (with channel mixing and exogenous fusion) on the D2 datasets (BS, CC, APP, SER), demonstrating an 18% forecast improvement over baselines (2401.03955.pdf, p. 10).
*   **Ablation Studies:** The impact of key components is analyzed individually. For example, Table 7 shows that Adaptive Patching (AP) improves performance by 3% and Resolution Prefix Tuning (RPT) improves performance by 3% in the 1B data setting (2401.03955.pdf, p. 12).

### Intersectional results:
The paper presents results across combinations of factors, primarily model variant, dataset, and forecast length (FL).
*   Table 13 provides a detailed breakdown of zero-shot MSE for TTMB, TTME, and TTMA on all D1 datasets across four different forecast lengths: 96, 192, 336, and 720 (2401.03955.pdf, p. 25).
*   Table 15 shows a similar breakdown for shorter forecast lengths (24, 48, 60, 96, 192) when comparing TTM against Chronos and Lag-llama on the last test window (2401.03955.pdf, p. 27).
*   Table 16 details the 5% few-shot performance of TTM variants across all standard forecast lengths and D1 datasets (2401.03955.pdf, p. 28).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
During inference, the base model (TTMB) requires a maximum of **0.06 GB** of GPU memory (2401.03955.pdf, p. 9, Table 3).

### Deploying Requirements:
TTM models are lightweight and designed for efficient deployment, even in CPU-only environments (2401.03955.pdf, p. 1).
*   **GPU Inference:** On an NVIDIA A100 GPU, the inference time per batch (size 32) for TTMB is **4.7 ms** (2401.03955.pdf, p. 9, Table 3).
*   **CPU Inference:** On a 16-core CPU, the inference time per batch for TTMB is **0.01 seconds** (2401.03955.pdf, p. 9, Table 3).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training process is computationally intensive, requiring **24-30 hours** on a distributed setup with **6 NVIDIA A100 GPUs** and 50 CPUs (2401.03955.pdf, p. 7, 21). The smaller TTMQ variant can be pre-trained in 4-6 hours (2401.03955.pdf, p. 7).
*   **Fine-tuning:** The fine-tuning process is very fast and efficient, requiring only **1 NVIDIA A100 GPU** or even just a CPU (2401.03955.pdf, p. 7, 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information. The provided paper focuses on the technical aspects of the TTM model and its performance on publicly available, non-sensitive time series data (e.g., weather, traffic, electricity consumption) (2401.03955.pdf). It does not contain a discussion of ethical considerations, potential risks, or mitigation strategies.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper outlines several limitations of the current TTM models (2401.03955.pdf, p. 26-27):
*   **Task Specificity:** TTM is currently designed exclusively for forecasting and does not support other time series analysis tasks like classification or anomaly detection.
*   **Point Forecasting Only:** The model provides only point forecasts and does not support probabilistic forecasting to quantify uncertainty.
*   **Context Length Sensitivity:** The architecture is sensitive to the context length of the input data. Consequently, different model variants have been pre-trained for specific context lengths (e.g., 512, 1024). The model does not automatically adapt to different context lengths.

### Recommendations:
*   **Forecast Length Adaptation:** For forecasting at a horizon different from the one a model was pre-trained for, the paper suggests two approaches based on the scenario (2401.03955.pdf, p. 11):
    *   Use **recursive prediction** when adapting to a moderately longer forecast horizon (e.g., from 96 to 192).
    *   Use **pruning** of the output layer when adapting to a significantly shorter forecast horizon (e.g., from 720 to 96), as this provides more stable results.
*   **Future Work:** The authors plan to extend TTM to support other downstream tasks and to facilitate probabilistic forecasts (2401.03955.pdf, p. 27). They also aim to enhance the backbone to automatically adapt to varying context lengths (2401.03955.pdf, p. 27).