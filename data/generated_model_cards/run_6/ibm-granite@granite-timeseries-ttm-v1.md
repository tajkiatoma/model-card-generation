## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from IBM Research: Vijay Ekambaram, Nam H. Nguyen, Arindam Jati, Wesley M. Gifford, Pankaj Dayama, Chandra Reddy, Sumanta Mukherjee, and Jayant Kalagnanam (2401.03955.pdf, p. 1).

### Model date:
The work was submitted to arXiv on January 8, 2024, and was accepted at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024). The version of the paper provided is dated November 7, 2024 (2401.03955.pdf, p. 1).

### Model version:
The paper describes four primary variants of the Tiny Time Mixer (TTM) model (2401.03955.pdf, p. 7, Section 4.3):
*   **TTM-Base (TTMB):** A 1M parameter model trained with a context length of 512 and a patch length of 64.
*   **TTM-Enhanced (TTME):** A 4M parameter model trained with a context length of 1024 and a patch length of 128.
*   **TTM-Advanced (TTMA):** A 5M parameter model trained with a context length of 1536 and a patch length of 128.
*   **Quick TTM (TTMQ):** A variant trained on a smaller subset of the pre-training data (~250 million samples) for faster pre-training (4-6 hours).

These models differ from other time series forecasting models by being significantly smaller and faster, designed for efficient zero/few-shot forecasting in resource-constrained environments (2401.03955.pdf, p. 1, Abstract).

### Model type:
The model is a Tiny Time Mixer (TTM), a compact model for multivariate time series forecasting (2401.03955.pdf, p. 1, Abstract). Its architecture is based on the light-weight TSMixer, which uses MLP-Mixer blocks interleaved with simple gated attention as an alternative to the self-attention blocks found in Transformers (2401.03955.pdf, p. 2).

Key architectural details from the configuration file, which corresponds to the TTM-Base (TTMB) variant, include (config.json.txt):
*   **Model Architecture:** `TinyTimeMixerForPrediction`
*   **Model Size (`d_model`):** 192
*   **Number of Layers:** 2 encoder layers, 2 decoder layers
*   **Context Length:** 512
*   **Prediction Length:** 96
*   **Patch Length:** 64
*   **Dropout:** 0.2
*   **Distribution Output:** `student_t`

The model incorporates several architectural innovations to handle heterogeneous datasets with a small model capacity, including adaptive patching (AP), diverse resolution sampling (DRS), and resolution prefix tuning (RPT) (2401.03955.pdf, p. 3).

### Training details:
The model is trained in a two-stage process: pre-training and fine-tuning (2401.03955.pdf, p. 4, Section 3.1).

**Pre-training:**
*   **Objective:** The model is pre-trained with a direct forecasting objective on a large collection of diverse public datasets (2401.03955.pdf, p. 4, Section 3.1).
*   **Loss Function:** Mean Squared Error (MSE) is used as the loss function, calculated over the forecast horizon (2401.03955.pdf, p. 4, Section 3.1; config.json.txt).
*   **Methodology:** Pre-training is done in a univariate fashion with independent channels. It incorporates several key techniques to handle diverse data with a small model (2401.03955.pdf, p. 3, 4-5):
    *   **Adaptive Patching (AP):** Different layers of the backbone operate at varying patch lengths to aid generalization across datasets with different resolutions.
    *   **Diverse Resolution Sampling (DRS):** High-resolution datasets are augmented by creating lower-resolution versions to balance the training data and improve coverage.
    *   **Resolution Prefix Tuning (RPT):** A learnable prefix is added to the input data to explicitly signal the time series resolution to the model.

**Fine-tuning:**
*   During fine-tuning, the model's backbone is frozen, and only the TTM head (decoder and forecast head) is updated (2401.03955.pdf, p. 6, Section 3.2).
*   The decoder can be fine-tuned with channel mixing enabled to capture cross-channel correlations in multivariate target data (2401.03955.pdf, p. 6, Section 3.2).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model:
*   Ekambaram, V., Nguyen, N. H., Jati, A., Gifford, W. M., Dayama, P., Reddy, C., ... & Kalagnanam, J. (2024). *Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series*. arXiv preprint arXiv:2401.03955. (2401.03955.pdf).

The paper's abstract also provides links to the model weights and source code (2401.03955.pdf, p. 1, Abstract).

### Citation details:
A BibTeX citation for the model can be formulated based on the provided paper:
```bibtex
@article{ekambaram2024tinytimemixers,
  title={Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series},
  author={Ekambaram, Vijay and Nguyen, Nam H. and Jati, Arindam and Gifford, Wesley M. and Dayama, Pankaj and Reddy, Chandra and Mukherjee, Sumanta and Kalagnanam, Jayant},
  journal={arXiv preprint arXiv:2401.03955},
  year={2024},
  note={Accepted at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024)}
}
```
(2401.03955.pdf, p. 1).

### License:
The model weights for research use are available, while enterprise-use weights are provided under the Apache license (2401.03955.pdf, p. 1, Abstract). The LibCity datasets used for pre-training were released under an Apache 2.0 license (2401.03955.pdf, p. 19).

### Contact:
For questions or feedback, the corresponding author can be contacted via email: `vijaye12@in.ibm.com` (2401.03955.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of TTM is for zero-shot, few-shot, and full-shot forecasting of multivariate time series (2401.03955.pdf, p. 1, Title). The model is designed to predict future values for multiple interrelated time series based on their historical values (2401.03955.pdf, p. 1, Introduction).

Its key capabilities include:
*   **Transfer Learning:** Applying knowledge from a wide range of public datasets to new, unseen forecasting tasks with minimal or no fine-tuning (2401.03955.pdf, p. 2).
*   **Handling Correlations:** It can explicitly model cross-channel correlations and incorporate exogenous signals (external variables that influence the target variables) during fine-tuning (2401.03955.pdf, p. 3).
*   **Resource-Constrained Environments:** Due to its small size and computational efficiency, it is well-suited for deployment on CPU-only machines or environments with limited resources (2401.03955.pdf, p. 1, Abstract).

The model takes a historical time series `X` as input and predicts future values `Y` for a specified forecast horizon (2401.03955.pdf, p. 3, Section 2).

### Primary intended users:
The primary intended users include researchers, developers, and businesses in domains like weather, traffic, retail, and energy who require time series forecasting capabilities (2401.03955.pdf, p. 1, Introduction). The model is particularly aimed at users in "real-world industrial settings" and those operating in "resource-constrained environments" who can benefit from a lightweight, efficient, and easy-to-use pre-trained model (2401.03955.pdf, p. 2, 3).

### Out-of-scope uses:
The model is currently designed exclusively for forecasting tasks. The following applications are considered out-of-scope (2401.03955.pdf, p. 26-27, Section H):
*   **Other Downstream Tasks:** The model is not intended for classification, regression (on non-time-series data), or anomaly detection, although future work may extend its capabilities to these areas.
*   **Probabilistic Forecasting:** The model currently supports only point forecasting (predicting a single value for each future time step) and does not provide probabilistic forecasts (a distribution of possible future values).

---

## How to Use
This section outlines how to use the model.

The model is designed to be used in a pre-training and fine-tuning workflow (2401.03955.pdf, p. 4, Section 3.1). Users can leverage the pre-trained weights and adapt the model to their specific target dataset. The paper outlines three primary usage workflows for a target domain (2401.03955.pdf, p. 6, Section 3.2):

1.  **Zero-shot Forecasting:** The pre-trained model is used directly to make predictions on the target dataset's test set without any fine-tuning. This is useful when no training data is available for the target domain.
2.  **Few-shot Forecasting:** A small portion (e.g., 5-10%) of the target dataset's training data is used to quickly update the weights of the TTM head (while the backbone remains frozen). This enhances accuracy in data-constrained scenarios.
3.  **Full-shot Forecasting (Head Probing):** The entire training part of the target dataset is used to fine-tune the TTM head. This provides the best performance when a full training set is available.

The source code and usage scripts are noted as being available, which would provide concrete code examples for implementation (2401.03955.pdf, p. 1, Abstract). However, no code snippets are present in the provided repository files.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model was specifically designed to handle the challenges posed by diverse time series data. Key factors that influence its performance and that it is built to accommodate include (2401.03955.pdf, p. 2):
*   **Temporal Resolution:** The sampling rate of the time series (e.g., seconds, minutes, hourly, daily). The model uses Diverse Resolution Sampling (DRS) and Resolution Prefix Tuning (RPT) to handle this diversity.
*   **Data Domain:** The application area of the data (e.g., weather, traffic, retail, energy).
*   **Number of Channels:** The dimensionality of the multivariate time series.
*   **Cross-Channel Correlations:** The interdependencies between different channels in a multivariate time series.
*   **Exogenous Variables:** The presence of external variables that influence the target channels.

### Evaluation factors:
The model's evaluation was conducted across a range of these factors to test its robustness and capabilities. The evaluation datasets were chosen to represent (2401.03955.pdf, p. 6, Section 4.1; p. 20, Table 9):
*   **Multiple Domains:** Datasets from electricity, traffic, weather, bike sharing, and business/IT observability were used.
*   **Varying Resolutions:** Datasets with resolutions from 10 seconds to 1 hour were included.
*   **Presence of Exogenous Variables:** A specific set of datasets (D2) was used to evaluate the model's ability to leverage exogenous information.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to assess the model's forecast accuracy is the **Mean Squared Error (MSE)** (2401.03955.pdf, p. 6, Section 4.1).

In addition, two relative improvement metrics are used for comparing TTM to baseline models (2401.03955.pdf, p. 6, Section 4.1):
*   **Forecast improvement percentage (f-imp(%)):** The percentage improvement in MSE of TTM over a baseline, averaged across datasets.
*   **Size improvement metric (s-imp(X)):** The ratio of a baseline model's size (total parameters) to the TTM model's size.

### Decision thresholds:
As TTM is a forecasting model that performs a regression task (predicting continuous values), decision thresholds are not applicable (2401.03955.pdf, p. 3, Section 2).

### Variation approaches:
Model performance is reported as the MSE averaged across multiple forecast lengths (FLs), such as {96, 192, 336, 720}, to provide a comprehensive assessment of its long-term forecasting capabilities (2401.03955.pdf, p. 7, Table 1 caption). The datasets are split chronologically into training, validation, and test sets to ensure that the model is evaluated on data that occurs after the training data (2401.03955.pdf, p. 19, Section C.1.1).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on eleven public time series datasets, divided into two sets (2401.03955.pdf, p. 6, Section 4.1; p. 20, Table 9).

**Set D1:** Seven popular benchmark datasets used for general zero/few/full-shot evaluation.
*   **ETT (Electricity Transformer Temperature):** ETTH1, ETTH2 (hourly, 7 channels), ETTM1, ETTM2 (15-minute, 7 channels).
*   **Weather:** 10-minute intervals, 21 channels.
*   **ECL (Electricity Consuming Load):** Hourly, 321 channels.
*   **Traffic:** Hourly road occupancy rates, 862 channels.

**Set D2:** Four datasets containing exogenous variables, used to evaluate cross-channel and exogenous modeling.
*   **BS (Bike Sharing):** Hourly bike rental counts with 11 weather-related exogenous variables.
*   **CC (Carbon Capture Plant):** 2-minute emission profiles with 5 control variables.
*   **APP (Application) & SER (Service):** 10-second business KPIs with 35 IT event variables.

### Motivation:
The **D1 datasets** were chosen because they are standard benchmarks that have been "consistently been employed in the literature" for state-of-the-art model comparisons (2401.03955.pdf, p. 6, 19). The **D2 datasets** were specifically selected to "assess the effectiveness of the proposed TTM model in extracting information from exogenous channels," a critical capability for many real-world applications that is lacking in many other pre-trained models (2401.03955.pdf, p. 6, 20).

### Preprocessing:
For evaluation, the datasets were split into training, validation, and test sets following the same chronological splits used in previous literature to ensure fair comparison (2401.03955.pdf, p. 20). The primary preprocessing step applied to the data before it is fed to the model is **instance normalization**, where each time series channel is independently normalized to have zero mean and unit standard deviation. This process is reversed on the model's output before the final loss is computed (2401.03955.pdf, p. 4, Section 2.2).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a large and diverse collection of public time series datasets, comprising approximately 1 billion samples in total (2401.03955.pdf, p. 2). The data was sourced from two main repositories:
*   **Monash Time Series Forecasting Archive:** A collection of datasets from various domains. This contributed ~250M samples (2401.03955.pdf, p. 18, Section C.1).
*   **LibCity:** A repository primarily focused on traffic prediction datasets. This contributed the remaining ~750M samples (2401.03955.pdf, p. 18, Section C.1).

A detailed list of the specific datasets used from these repositories is provided in the paper (2401.03955.pdf, p. 19, Table 8). The datasets used for evaluation were explicitly excluded from the pre-training data (2401.03955.pdf, p. 6, Section 4.1).

### Motivation:
The choice of training data was motivated by the need to expose the model to a wide variety of time series characteristics. The datasets exhibit "considerable diversity in characteristics, such as different domains, temporal resolutions (ranging from seconds to days), lengths, and numbers of channels" (2401.03955.pdf, p. 2). This diversity is crucial for training a compact model that can learn general temporal patterns and successfully transfer its knowledge to new, unseen forecasting tasks (2401.03955.pdf, p. 11, Section 4.9).

### Preprocessing:
Several preprocessing steps were applied to the training data to prepare it for the model (2401.03955.pdf, p. 4-5):
*   **Univariate Transformation:** Multivariate datasets were transformed into a collection of independent univariate time series to simplify the pre-training process, as modeling multivariate correlations is challenging across diverse datasets (2401.03955.pdf, p. 4, Section 3.1).
*   **Instance Normalization:** Each time series instance is normalized to have zero mean and unit standard deviation to handle potential distribution shifts (2401.03955.pdf, p. 4, Section 2.2).
*   **Patching:** The normalized time series is divided into non-overlapping windows or "patches" (2401.03955.pdf, p. 4, Section 2.2).
*   **Diverse Resolution Sampling (DRS):** To prevent the model from being biased towards high-resolution data (which naturally contains more samples), high-resolution datasets were downsampled (e.g., by averaging or decimation) to generate new, lower-resolution datasets. This increases the diversity and coverage of resolutions in the training data (2401.03955.pdf, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results for the model's performance on individual datasets and across different forecast lengths.
*   **Zero-shot Performance:** In zero-shot forecasting, TTM variants consistently outperform larger pre-trained models. For example, TTMA (5M parameters) outperforms Moirai variants (14M-311M parameters) by 4-10% and TimesFM (200M parameters) by 19% in terms of MSE. The smallest variant, TTMB (1M parameters), outperforms Chronos (8M-709M parameters) by 17-32% (2401.03955.pdf, p. 7-8, Tables 1 & 2).
*   **Few-shot Performance:** In a 5% few-shot setting, TTMB (1M parameters) surpasses GPT4TS (84M parameters) by 15% and Time-LLM (7B parameters) by 10% (2401.03955.pdf, p. 9, Table 4).
*   **Exogenous Data Performance:** When fine-tuned on datasets with exogenous variables (the D2 set), the TTM-CM variant (with channel mixing and exogenous fusion) shows significant performance gains, outperforming models like PatchTST and TSMixer by a margin of 15-20% (2401.03955.pdf, p. 10, Table 6).

### Intersectional results:
The paper presents results disaggregated by dataset and forecast length (FL). For instance, Table 11 shows the zero-shot MSE for all TTM variants on each of the seven D1 datasets across four different forecast lengths (FL = 96, 192, 336, 720) (2401.03955.pdf, p. 23, Table 11). This allows for an analysis of how performance varies based on the combination of data characteristics (e.g., Traffic vs. Weather) and task difficulty (shorter vs. longer forecast horizons). The results generally show that MSE increases with the forecast length, and performance varies significantly across datasets, highlighting the different challenges posed by each.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model is lightweight and designed for efficiency. For inference with the TTMB (1M parameter) variant, the requirements are (2401.03955.pdf, p. 9, Table 3):
*   **GPU Memory:** 0.06 GB
*   **Hardware:** Can be executed on standard CPUs.

### Deploying Requirements:
The model is designed for deployment in resource-constrained environments, including on CPU-only machines (2401.03955.pdf, p. 1, Abstract). Inference is very fast (2401.03955.pdf, p. 9, Table 3):
*   **CPU Inference Time (per batch of 32):** 0.01 seconds
*   **GPU Inference Time (per batch of 32 on A100):** 4.7 milliseconds

### Training or Fine-tuning Requirements:
*   **Pre-training:** The full pre-training process for the primary TTM variants required significant resources, taking 24-30 hours on 6 NVIDIA A100 GPUs (2401.03955.pdf, p. 7, Section 4.3).
*   **Fine-tuning:** The fine-tuning process is "highly efficient and fast," requiring only a single GPU or even just a CPU. The paper specifies that fine-tuning experiments were executed on just one A100 GPU (2401.03955.pdf, p. 7, Section 4.3; p. 21, Section D.2).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided paper does not contain a dedicated section on ethical considerations. The model was pre-trained on publicly available datasets from the Monash and LibCity repositories, which primarily contain non-personal data related to topics like electricity demand, weather, and traffic (2401.03955.pdf, p. 18-19, Section C.1). There is no indication that sensitive or personally identifiable information was used in the development or training of the model.

Potential risks would be associated with the application of the model in critical domains where inaccurate forecasts could lead to negative consequences (e.g., financial markets, energy grid management). However, the paper does not discuss these risks or any mitigation strategies. The focus is on the technical aspects of creating an efficient and accurate forecasting model.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper identifies several limitations and areas for future work (2401.03955.pdf, p. 26-27, Section H):
*   **Task Specificity:** The model is currently focused solely on forecasting. It does not support other time series analysis tasks such as classification, regression, or anomaly detection.
*   **Context Length Sensitivity:** The architecture is sensitive to context length, meaning different model variants are optimized for different input sequence lengths. The backbone does not automatically adapt to dynamically varying context lengths.
*   **Point Forecasting Only:** The model provides point forecasts (a single predicted value) and does not currently support probabilistic forecasting, which quantifies uncertainty by predicting a range or distribution of possible outcomes.

### Recommendations:
*   **Use in Resource-Constrained Environments:** The model is highly recommended for applications where computational resources (CPU, GPU, memory) are limited, due to its small size and high inference speed (2401.03955.pdf, p. 1, Abstract).
*   **Forecast Length Adaptation:** For forecasting at a horizon different from the one a pre-trained model was designed for, the paper suggests two adaptation strategies (2401.03955.pdf, p. 11, Section 4.7):
    *   For small changes in forecast length (e.g., from 96 to 192), using the model **recursively** yields the best performance.
    *   For larger changes (e.g., adapting a model trained for FL=720 down to FL=96), **pruning** the model's output head provides more stable and accurate results.
*   **Leverage Fine-tuning:** Users are encouraged to fine-tune the model head on their target data (even a small amount) to significantly improve performance for their specific task (2401.03955.pdf, p. 8, Section 4.5).