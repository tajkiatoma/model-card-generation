## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from IBM Research (Paper, p. 1). The authors are Vijay Ekambaram, Nam H. Nguyen, Arindam Jati, Wesley M. Gifford, Pankaj Dayama, Chandra Reddy, Sumanta Mukherjee, and Jayant Kalagnanam (Paper, p. 1).

### Model date:
The work was submitted to arXiv on January 8, 2024, with the latest version dated November 7, 2024 (Paper, p. 1). It was accepted for publication at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024) (Paper, p. 1).

### Model version:
The model is named Tiny Time Mixer (TTM). The repository provides details for a specific configuration of the `TinyTimeMixerForPrediction` architecture (config.json). The research paper describes several pre-trained variants of TTM (Paper, Section 4.3):
*   **TTM-Base (TTM<sub>B</sub>):** A 1M parameter model trained with a context length of 512 and a patch length of 64.
*   **TTM-Enhanced (TTM<sub>E</sub>):** A 4M parameter model trained with a context length of 1024 and a patch length of 128.
*   **TTM-Advanced (TTM<sub>A</sub>):** A 5M parameter model trained with a context length of 1536 and a patch length of 128.
*   **Quick TTM (TTM<sub>Q</sub>):** A variant trained on a smaller dataset (~250 million samples) for secondary studies.

These versions differ in size, context length, and the amount of data they were trained on, offering a trade-off between model capacity and computational requirements (Paper, Section 4.3).

### Model type:
Tiny Time Mixer (TTM) is a pre-trained model designed for zero/few-shot forecasting of multivariate time series (Paper, Title, Abstract).

**Architecture:**
*   It is based on the lightweight TSMixer architecture, which uses MLP-Mixer blocks interleaved with simple gated attention as an alternative to the self-attention blocks found in Transformers (Paper, p. 2).
*   The architecture incorporates several innovations for pre-training on heterogeneous datasets:
    1.  **Adaptive Patching (AP):** Different layers of the model's backbone operate at varying patch lengths and numbers of patches to aid generalization across datasets with different resolutions (Paper, Section 3.1.1).
    2.  **Diverse Resolution Sampling (DRS):** A data augmentation technique to balance training samples across different time series resolutions (Paper, Section 3.1.1).
    3.  **Resolution Prefix Tuning (RPT):** A learnable prefix is added to the input data to explicitly signal the input resolution to the model (Paper, Section 3.1.1).
*   The model follows a multi-level structure consisting of a TTM backbone, a smaller TTM decoder, a forecast head, and an optional exogenous mixer (Paper, Section 2.1).

**Model Size and Parameters (from `config.json` and paper):**
*   **Model Type:** `tinytimemixer` (config.json).
*   **Architecture Class:** `TinyTimeMixerForPrediction` (config.json).
*   **Model Size (TTM<sub>B</sub>):** Starts from 1 million parameters (Paper, p. 2).
*   **Context Length:** 512 (config.json).
*   **Prediction Length:** 96 (config.json).
*   **Hidden Size (`d_model`):** 192 (config.json).
*   **Number of Layers:** 2 (config.json).
*   **Patch Length:** 64 (config.json).
*   **Dropout:** 0.2 (config.json).

### Training details:
The model is trained in a two-stage process: pre-training and fine-tuning (Paper, Section 3.1).

**Pre-training:**
*   **Objective:** The model is pre-trained on a direct forecasting task using Mean Squared Error (MSE) loss (Paper, Section 3.1; config.json).
*   **Methodology:** TTM is pre-trained in a channel-independent, univariate fashion on a large collection of diverse public datasets. This allows the model to capture common temporal dynamics and seasonal patterns (Paper, Section 3.1).
*   **Key Techniques:** The pre-training workflow is enhanced with Adaptive Patching (AP), Diverse Resolution Sampling (DRS), and Resolution Prefix Tuning (RPT) to handle heterogeneous, multi-resolution datasets with a small model capacity (Paper, Section 3.1.1).
*   **Hyperparameters:** Pre-training was performed with a batch size of 4500 for 20 epochs, with a dropout of 0.4. The backbone consists of 3 levels, with 2 TTM blocks per level (Paper, Appendix D.1).

**Fine-tuning:**
*   During fine-tuning, the model's backbone is frozen, and only the TTM head (decoder and forecast head) is updated (Paper, Section 3.2).
*   The decoder can be fine-tuned with channel mixing enabled to capture cross-channel correlations in the target multivariate dataset (Paper, Section 3.2).
*   An optional exogenous mixer block can be applied to incorporate known future values of external variables (Paper, Section 3.2).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Title:** Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series (Paper, p. 1).
*   **arXiv Link:** https://arxiv.org/abs/2401.03955 (Paper, p. 1).

The paper's abstract also provides links to the following resources:
*   **Source Code and Usage Scripts:** Available [here](https://github.com/ibm-granite/granite-ts-models) (Paper, Abstract).
*   **Model Weights (Research Use):** Available [here](https://huggingface.co/ibm-granite/granite-timeseries-ttm-v1) (Paper, Abstract).
*   **Model Weights (Enterprise Use):** Available [here](https://github.com/ibm-granite/granite-ts-models) (Paper, Abstract).

### Citation details:
A BibTeX citation for the paper can be formulated as follows, based on the information provided:
```bibtex
@article{ekambaram2024tiny,
  title={Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series},
  author={Ekambaram, Vijay and Nguyen, Nam H. and Jati, Arindam and Gifford, Wesley M. and Dayama, Pankaj and Reddy, Chandra and Mukherjee, Sumanta and Kalagnanam, Jayant},
  journal={arXiv preprint arXiv:2401.03955},
  year={2024},
  note={Accepted at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)}
}
```
(Paper, p. 1).

### License:
The model weights for enterprise use are available under the Apache license (Paper, Abstract). The pre-training data from the LibCity repository was released under an Apache 2.0 license, and data from the Monash repository is available under a Creative Commons Attribution 4.0 International license (Paper, Appendix C.1).

### Contact:
For questions or feedback, contact the corresponding author at `vijaye12@in.ibm.com` (Paper, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of TTM is multivariate time series forecasting, particularly in zero-shot and few-shot learning scenarios (Paper, Title, Abstract). The model is designed to predict future values for multiple interrelated time series based on their historical values (Paper, p. 1).

**Capabilities:**
*   **Zero-shot Forecasting:** The pre-trained model can be used directly to make forecasts on unseen datasets without any fine-tuning (Paper, Section 3.2).
*   **Few-shot/Full-shot Forecasting:** The model can be quickly fine-tuned on a small portion (5-10%) or the entirety of a target dataset to improve performance (Paper, Section 3.2).
*   **Cross-channel Correlation Modeling:** The model can explicitly capture correlations between different channels (variables) in a multivariate time series during fine-tuning (Paper, p. 3).
*   **Exogenous Variable Infusion:** TTM can incorporate external variables (channels with known future values) to improve forecast accuracy (Paper, p. 3).

**Input-Output Structure:**
*   **Input:** A historical multivariate time series `X` of shape `(channels, context_length)` (Paper, Section 2). The provided configuration specifies a `context_length` of 512 (config.json).
*   **Output:** A forecast of future values `Y` of shape `(forecast_channels, prediction_length)` (Paper, Section 2). The provided configuration specifies a `prediction_length` of 96 (config.json).

### Primary intended users:
The model is intended for a broad audience, including:
*   **Researchers** in the field of time series analysis and forecasting (Paper, Abstract).
*   **Developers and businesses** looking for efficient and accurate forecasting models that can be deployed in resource-constrained environments, including on CPU-only machines (Paper, Abstract, p. 3). The availability of "enterprise-use weights" further supports this (Paper, Abstract).

### Out-of-scope uses:
The model is currently designed exclusively for forecasting tasks (Paper, Appendix H). Other downstream tasks are considered out-of-scope, though they are areas for future work. These include:
*   Time series classification
*   Time series regression
*   Anomaly detection

The paper also notes that the current version of TTM only supports point forecasting, not probabilistic forecasting (Paper, Appendix H).

---

## How to Use
This section outlines how to use the model. 

The model can be used in one of three primary modes, depending on the availability of target domain data (Paper, Section 3.2):

1.  **Zero-Shot Forecasting:** The pre-trained model is used directly for evaluation on a target dataset. No fine-tuning is performed.
2.  **Few-Shot Forecasting:** A small portion (e.g., 5-10%) of the training data from the target domain is used to update the weights of the TTM head (the decoder and forecast head), while the pre-trained backbone remains frozen. This quickly adapts the model to the new data.
3.  **Full-Shot Forecasting (Head Probing):** The entire training set of the target domain is used to fine-tune the TTM head, with the backbone still frozen.

**Incorporating Exogenous Variables:**
If the target dataset contains exogenous variables (i.e., variables whose future values are known), the `Exogenous Mixer Block` can be enabled during fine-tuning. This block fuses the known future values of the exogenous channels with the model's initial forecasts to produce a more accurate final prediction for the target channels (Paper, Section 3.2).

The model's source code and usage scripts are available in its official repository (Paper, Abstract). The provided configuration specifies an input `context_length` of 512 and an output `prediction_length` of 96 (config.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model was specifically designed to be robust to a variety of factors inherent in time series data, making these factors relevant to its performance and application (Paper, p. 2). These include:
*   **Temporal Resolution:** The sampling rate of the time series (e.g., seconds, minutes, hourly, daily). The model was pre-trained on datasets with diverse resolutions (Paper, p. 2).
*   **Data Domain:** The application area of the data (e.g., weather, traffic, retail, energy) (Paper, p. 1).
*   **Number of Channels:** The dimensionality of the multivariate time series.
*   **Series Length:** The length of the historical data available.
*   **Exogenous Variables:** The presence of external variables that influence the target variables (Paper, Section 2).

### Evaluation factors:
The model's evaluation was conducted across these relevant factors to demonstrate its capabilities (Paper, Section 4.1).
*   **Datasets:** The model was evaluated on 11 different public datasets from various domains (e.g., electricity, traffic, weather, bike sharing) to test its generalization (Paper, Section 4.1, Table 9).
*   **Exogenous Signals and Channel Correlations:** A specific set of four datasets (D2) was used to explicitly evaluate the model's ability to handle exogenous variables and model cross-channel correlations (Paper, Section 4.1, Section 4.6).
*   **Forecast Lengths:** Performance was evaluated and reported across multiple forecast horizons (e.g., 96, 192, 336, 720 steps) (Paper, Table 1 caption).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's forecast accuracy is **Mean Squared Error (MSE)** (Paper, Section 4.1).

In addition, two relative improvement metrics are used to compare TTM against baseline models (Paper, Section 4.1):
1.  **Forecast Improvement Percentage (f-imp(%)):** The percentage improvement in MSE of TTM over a baseline, averaged across all datasets.
2.  **Size Improvement Metric (s-imp(X)):** The ratio of a baseline model's size (total parameters) to the TTM model's size.

### Decision thresholds:
As TTM is a forecasting model that performs a regression task (predicting continuous values), decision thresholds are not applicable (Paper, Section 2).

### Variation approaches:
Model hyperparameters were selected based on performance on a validation set, with final results reported on the test set (Paper, Section 4.3). For benchmark comparisons, performance is often averaged across multiple forecast lengths (e.g., FL ∈ {96, 192, 336, 720}) to provide a comprehensive assessment (Paper, Table 1 caption). The evaluation datasets are split chronologically to ensure the test data occurs after the training and validation data (Paper, Appendix C.1.1).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on eleven public datasets, divided into two groups (Paper, Section 4.1, Appendix C.2).

**Set D1:** Seven datasets commonly used in time series forecasting literature, which do not contain exogenous variables (Paper, Section 4.1, Appendix C.2).
*   **ETT (Electricity Transformer Temperature):** ETTH1, ETTH2 (hourly, 7 channels), ETTM1, ETTM2 (15-minute, 7 channels).
*   **Weather:** 10-minute intervals, 21 channels.
*   **Electricity (ECL):** Hourly consumption data for 321 clients.
*   **Traffic:** Hourly road occupancy rates from 862 sensors.

**Set D2:** Four datasets used to evaluate performance on tasks with exogenous variables and cross-channel correlations (Paper, Section 4.1, Appendix C.2).
*   **Bike Sharing (BS):** Hourly bike rental counts with 11 weather-related features as exogenous variables.
*   **Carbon Capture Plant (CC):** 2-minute interval emission profiles with 5 control variables.
*   **Service (SER) & Application (APP):** 10-second interval business KPIs and IT events from an e-commerce application.

A full breakdown of dataset characteristics is available in Table 9 of the paper (Paper, p. 20).

### Motivation:
*   **Set D1** was chosen because its constituent datasets are popular benchmarks used in prior state-of-the-art forecasting research, allowing for direct comparison with existing models (Paper, Section 4.1).
*   **Set D2** was chosen specifically to validate the model's effectiveness in handling exogenous signals and modeling cross-channel correlations, which are critical requirements for many real-world industrial applications and are features lacking in many other pre-trained models (Paper, Section 4.1, p. 2).

### Preprocessing:
The evaluation data undergoes the same preprocessing as the training data (Paper, Section 2.2):
1.  **Instance Normalization:** Each time series instance is normalized per-channel to have zero mean and unit standard deviation. This helps mitigate distribution shifts.
2.  **Patching:** The normalized historical data is divided into non-overlapping windows (patches). This preserves local semantic information and reduces computation.
The normalization is reversed before the final loss is computed (Paper, Section 2.2). For the D1 datasets, the standard train/validation/test splits from the literature were used (Paper, Appendix C.2).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a large and diverse collection of public time series datasets, comprising approximately 1 billion samples in total (Paper, p. 2). The data was sourced from two main repositories:
1.  **Monash Time Series Forecasting Archive:** A subset of datasets from this repository was used, accounting for ~250 million samples. Datasets with very short lengths (e.g., yearly, monthly) were excluded (Paper, Appendix C.1).
2.  **LibCity:** A collection of traffic prediction datasets (Paper, Appendix C.1).

A detailed list of the pre-training datasets is provided in Table 8 of the paper. These datasets cover a wide range of resolutions (from 4-seconds to daily) and domains (e.g., solar energy, web traffic, electricity demand) (Paper, Table 8). The datasets used for evaluation were explicitly excluded from the pre-training corpus (Paper, Section 4.1).

### Motivation:
The datasets were chosen to create a heterogeneous and diverse pre-training corpus. The goal was to build a single, compact pre-trained model capable of generalizing to a wide variety of unseen forecasting tasks, which is a significant challenge due to the diverse nature of time series data across different applications (Paper, p. 2). The paper finds that "resolution diversity" in the pre-training data is crucial for generalization (Paper, Section 4.9).

### Preprocessing:
The following preprocessing steps were applied to the training data:
1.  **Univariate Transformation:** Multivariate datasets were transformed into a collection of independent univariate time series to facilitate channel-independent pre-training (Paper, Section 3.1).
2.  **Instance Normalization and Patching:** As with the evaluation data, each series was normalized and patched (Paper, Section 2.2).
3.  **Diverse Resolution Sampling (DRS):** This is a key data augmentation step where high-resolution datasets (e.g., sampled every few seconds) are downsampled (by averaging or decimation) to create new, lower-resolution datasets (e.g., minutely, hourly). This technique increases the diversity and coverage of resolutions in the training data, preventing the model from being biased towards high-frequency data and improving overall performance (Paper, Section 3.1.1, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results disaggregated by dataset and forecast length.
*   **Zero-shot Performance:** Table 1 and Table 2 show the MSE of TTM variants on each of the seven D1 datasets, averaged over multiple forecast lengths (Paper, p. 7-8). Table 11 in the appendix provides a more granular breakdown, showing MSE for each dataset at four different forecast lengths (96, 192, 336, 720) (Paper, p. 23).
*   **Few-shot Performance:** Table 4 shows the MSE for TTM variants on each D1 dataset after fine-tuning on 5% of the training data (Paper, p. 9).
*   **Exogenous Data Performance:** Table 6 shows the MSE for TTM on the four D2 datasets (BS, CC, APP, SER), demonstrating its performance on data with exogenous variables (Paper, p. 10).
*   **Ablation Studies:** Table 7 shows the impact of Adaptive Patching (AP) and Resolution Prefix Tuning (RPT) on performance, disaggregated by dataset (Paper, p. 12).

### Intersectional results:
The paper does not provide intersectional analysis in the sense of evaluating performance across combinations of demographic or sensitive factors. The analysis is disaggregated by data characteristics like dataset source, forecast length, and model configuration, rather than intersecting factors of a population.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
For the 1M parameter TTM<sub>B</sub> model, the maximum GPU memory usage during inference is **0.06 GB** (Paper, Table 3).

### Deploying Requirements:
TTM models are designed to be lightweight and efficient for deployment.
*   **Environment:** They can be executed on both GPU and CPU-only machines (Paper, Abstract).
*   **Inference Time (per batch of 32):**
    *   **GPU (A100):** 4.7 ms for TTM<sub>B</sub> (Paper, Table 3).
    *   **CPU:** 0.01 seconds for TTM<sub>B</sub> (Paper, Table 3).
This makes the model suitable for resource-constrained environments (Paper, Abstract).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training process for the 1B sample dataset takes **24-30 hours using 6 NVIDIA A100 GPUs** (Paper, Section 4.3).
*   **Fine-tuning:** The fine-tuning process is significantly faster and more efficient, requiring only **1 GPU or even just a CPU** (Paper, Section 4.3). The paper specifies that fine-tuning experiments were executed on a single A100 GPU (Paper, Appendix D.2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The provided paper does not include a dedicated section on ethical considerations or potential societal impacts. The datasets used for pre-training and evaluation are publicly available and primarily consist of non-personal data related to domains like weather, electricity consumption, and traffic (Paper, Appendix C). No use of sensitive or personally identifiable information is mentioned. Potential risks associated with the model's application in critical domains are not discussed.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper's "Limitations and Future Work" section (Appendix H) outlines several caveats:
*   **Task Specificity:** The model is currently focused only on forecasting. Its capabilities do not extend to other time series tasks like classification or anomaly detection.
*   **Context Length Sensitivity:** The model's architecture is sensitive to the context length of the input. Different models need to be trained for different context lengths.
*   **Point Forecasting Only:** TTM currently only provides point forecasts (a single predicted value for each future time step) and does not support probabilistic forecasting (predicting a distribution of possible future values).

### Recommendations:
*   **Adapting to Forecast Lengths:** Users do not necessarily need to pre-train a new model for every required forecast length (FL). The paper recommends two **Forecast Length Adaptation (FLA)** techniques to adapt an existing TTM to a new FL (Paper, Section 4.7):
    1.  **Recursive Prediction:** For adapting to a longer FL, use a model trained on a shorter FL and apply it recursively. This works best for smaller forecast horizon changes.
    2.  **Pruning:** For adapting to a shorter FL, use a model trained on a longer FL and prune its output head. This provides more stable results for larger changes.
*   **Use in Resource-Constrained Environments:** Given its small size and fast inference on CPUs, TTM is recommended for applications where computational resources are limited (Paper, Abstract).
*   **Fine-tuning for Performance:** For best performance on a specific target domain, users are encouraged to perform few-shot or full-shot fine-tuning (head probing), which is computationally inexpensive and significantly boosts accuracy (Paper, Section 4.5).