## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from IBM Research (Paper, p. 1). The authors are Vijay Ekambaram, Nam H. Nguyen, Arindam Jati, Wesley M. Gifford, Pankaj Dayama, Chandra Reddy, Sumanta Mukherjee, and Jayant Kalagnanam (Paper, p. 1). The corresponding contact email is vijaye12@in.ibm.com (Paper, p. 1).

### Model date:
The work was submitted to arXiv on January 8, 2024, and accepted at the 38th Conference on Neural Information Processing Systems (NeurIPS 2024) (Paper, p. 1). The version of the paper provided is dated November 7, 2024 (Paper, p. 1).

### Model version:
The model is named Tiny Time Mixer (TTM). There are three primary pre-trained variants, which differ in size, context length (sl), and patch length (pl) (Paper, Section 4.3, p. 7):
*   **TTM-Base (TTMB):** A 1M parameter model trained with sl = 512 and pl = 64.
*   **TTM-Enhanced (TTME):** A 4M parameter model trained with sl = 1024 and pl = 128.
*   **TTM-Advanced (TTMA):** A 5M parameter model trained with sl = 1536 and pl = 128.

Additionally, a **Quick TTM (TTMQ)** variant was trained on a smaller dataset for secondary studies (Paper, Section 4.3, p. 7). The model is based on `transformers` version 4.37.2 (config.json; generation_config.json).

### Model type:
TTM is a pre-trained model for multivariate time series forecasting (Paper, Abstract, p. 1).

**Architecture:**
The model architecture is `TinyTimeMixerForPrediction` (config.json). It is based on the light-weight TSMixer, which uses MLPMixer blocks interleaved with simple gated attention as an alternative to self-attention blocks in Transformers (Paper, p. 2). TTM follows a multi-level architecture consisting of four key components (Paper, Section 2.1, p. 4):
1.  **TTM Backbone:** Assembled from TSMixer building blocks, it processes patched time series data.
2.  **TTM Decoder:** Follows the same architecture as the backbone but is smaller (10-20% of the size).
3.  **Forecast Head:** A linear head that produces the forecast output.
4.  **Optional Exogenous Mixer:** Fuses exogenous data into the forecasting process.

TTM incorporates several architectural innovations to handle heterogeneous datasets with a small model capacity (Paper, p. 3):
*   **Adaptive Patching (AP):** Different layers of the backbone operate at varying patch lengths, which aids generalization across datasets with different resolutions (Paper, p. 4, 5).
*   **Resolution Prefix Tuning (RPT):** A learnable prefix is added to the input data based on its resolution, providing an explicit signal to the model for resolution-conditioned modeling (Paper, p. 5).

**Model Size and Parameters:**
The model is designed to be compact, with the base version (TTMB) having 1 million parameters (Paper, p. 2). The specific configuration provided has the following parameters (config.json):
*   **Model Type:** `tinytimemixer`
*   **Model Dimension (`d_model`):** 192
*   **Number of Layers:** 2
*   **Context Length:** 512
*   **Prediction Length:** 96
*   **Patch Length:** 64
*   **Number of Patches:** 8
*   **Distribution Output:** `student_t`
*   **Dropout:** 0.2

### Training details:
TTM's training process involves two stages: pre-training and fine-tuning (Paper, Section 3.1, p. 4).

**Pre-training:**
*   **Objective:** The model is pre-trained with a direct forecasting objective using Mean Squared Error (MSE) loss (Paper, Section 3.1, p. 4; config.json).
*   **Methodology:** TTM is pre-trained on a large collection of diverse public datasets in a univariate fashion, meaning multivariate datasets are transformed into independent univariate time series. This is done to handle the varied channel counts in the pre-training data (Paper, Section 3.1, p. 4).
*   **Enhancements:** To handle heterogeneous, multi-resolution datasets with a small model, the following techniques are used during pre-training (Paper, p. 3):
    *   **Adaptive Patching (AP):** Allows different layers to operate at different patch configurations (Paper, p. 4).
    *   **Diverse Resolution Sampling (DRS):** An augmentation technique that creates lower-resolution data from high-resolution datasets to balance the training samples and improve coverage (Paper, p. 5).
    *   **Resolution Prefix Tuning (RPT):** Explicitly embeds resolution information into the input to aid resolution-conditioned modeling (Paper, p. 5).

**Fine-tuning:**
*   During fine-tuning, the model's backbone is frozen, and only the TTM head (decoder and forecast head) is updated on the target dataset (Paper, Section 3.2, p. 6).
*   The slim decoder can be fine-tuned with channel mixing enabled to explicitly capture cross-channel correlations in multivariate target data (Paper, Section 3.2, p. 6).
*   An optional exogenous mixer block can be applied to incorporate future known values of exogenous variables (Paper, Section 3.2, p. 6).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model (Paper):
*   **Title:** Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series
*   **Link:** https://arxiv.org/abs/2401.03955

The paper's abstract also provides the following links (Paper, Abstract, p. 1):
*   **Model Weights (Research Use):** [here](https://github.com/ibm-granite/granite-ts-models)
*   **Model Weights (Enterprise Use):** [initial TTM variant](https://huggingface.co/ibm-granite/granite-ttm-v1), [latest variants](https://huggingface.co/ibm-granite) (preferred)
*   **Source Code and Usage Scripts:** [here](https://github.com/ibm-granite/granite-ts-models)

### Citation details:
A BibTeX citation for the associated paper can be formatted as follows:
```bibtex
@misc{ekambaram2024tinytimemixers,
      title={Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series}, 
      author={Vijay Ekambaram and Nam H. Nguyen and Arindam Jati and Wesley M. Gifford and Pankaj Dayama and Chandra Reddy and Sumanta Mukherjee and Jayant Kalagnanam},
      year={2024},
      eprint={2401.03955},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
(Derived from Paper, p. 1)

### License:
The model weights are available under different terms (Paper, Abstract, p. 1):
*   Weights for reproducibility and research use are available at the project's GitHub repository.
*   Enterprise-use weights are available under the Apache license.

The LibCity datasets used for pre-training were released under an Apache 2.0 license, and the Monash datasets were released under a Creative Commons Attribution 4.0 International license (Paper, Appendix C.1, p. 19).

### Contact:
For questions, issues, or feedback, contact the corresponding author at: `vijaye12@in.ibm.com` (Paper, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of TTM is for zero-shot and few-shot forecasting of multivariate time series (Paper, Abstract, p. 1). It is designed to predict future values for multiple interrelated time series based on their historical values (Paper, p. 1).

The model's key capabilities include (Paper, p. 3):
*   **Transfer learning:** Applying knowledge from a large pre-training corpus to new, unseen datasets with minimal or no fine-tuning.
*   **Handling channel correlations:** The model can be fine-tuned to capture correlations between different channels in a multivariate time series.
*   **Incorporating exogenous signals:** TTM can use external variables (e.g., weather data influencing sales) whose future values are known to improve forecast accuracy.

The model takes a historical time series context as input and outputs a forecast for a future horizon (Paper, p. 3). For the provided configuration, the input context length is 512 time steps, and the output prediction length is 96 time steps (config.json).

### Primary intended users:
The model is intended for a broad audience, including researchers and practitioners in the field of time series forecasting. Given its lightweight nature and ability to run on CPU-only machines, it is particularly suitable for users in resource-constrained environments (Paper, Abstract, p. 1). The availability of enterprise-use weights suggests that businesses are also a primary intended user group (Paper, Abstract, p. 1).

### Out-of-scope uses:
The model is currently designed exclusively for forecasting tasks. The following applications are considered out-of-scope (Paper, Section H, p. 26):
*   Other downstream time series tasks such as classification, regression, and anomaly detection.
*   Probabilistic forecasting (i.e., predicting a distribution of possible future values). The model currently only supports point forecasting (predicting a single future value).

---

## How to Use
This section outlines how to use the model.

The source code and usage scripts for the TTM model are available at the project's GitHub repository (Paper, Abstract, p. 1). The provided repository data does not include specific code snippets for model usage.

The general workflow for using the model can be inferred from the paper (Paper, Sections 2 & 3, p. 3-6):
1.  **Data Preprocessing:** Input time series data should be preprocessed. The model uses instance normalization (scaling each time series instance to have zero mean and unit standard deviation) and patching (dividing the time series into non-overlapping windows).
2.  **Model Inference/Fine-tuning:**
    *   For **zero-shot forecasting**, the pre-trained model can be used directly on the target data without any updates.
    *   For **few-shot or full-shot forecasting**, the model's head (decoder and forecast head) can be fine-tuned on a small portion or the entire training split of the target data, respectively. The backbone remains frozen.
3.  **Input/Output:** The model expects an input tensor representing the historical context and outputs a tensor representing the forecast horizon. Based on the provided configuration, the model takes a context of 512 time steps (`context_length`) to predict the next 96 time steps (`prediction_length`) (config.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the following factors:
*   **Temporal Resolution:** The pre-training data contains time series with diverse resolutions (ranging from seconds to days). The model's performance is sensitive to this, and it was designed with features like Diverse Resolution Sampling (DRS) and Resolution Prefix Tuning (RPT) to handle this diversity (Paper, p. 2, 5).
*   **Cross-Channel Correlations:** The model's ability to capture correlations between different variables in a multivariate time series is a key factor. This is handled by the channel-mixing mechanism in the decoder during fine-tuning (Paper, p. 2, 6).
*   **Exogenous Variables:** The presence and use of external variables that influence the target variables can significantly impact forecast accuracy. The model includes an optional exogenous mixer to incorporate these signals (Paper, p. 2, 6).
*   **Data Quality and Quantity:** The performance of the pre-trained model depends on the quality and diversity of the pre-training data. Experiments show that increasing resolution diversity is more crucial than simply increasing the quantity of data (Paper, Section 4.7, p. 10).

### Evaluation factors:
The model was evaluated across a range of factors to test its capabilities:
*   **Datasets:** Evaluation was performed on 11 different public datasets with varying characteristics such as domain (e.g., electricity, traffic, weather), number of channels, and temporal resolution (Paper, Section 4.1, p. 6; Appendix C.2, p. 19).
*   **Forecast Length:** The model's performance was measured across multiple forecast horizons, ranging from short-term (e.g., 24 steps) to long-term (e.g., 720 steps) (Paper, Table 1, p. 7).
*   **Exogenous Data:** The evaluation explicitly used a separate set of datasets (D2) to validate the model's effectiveness in handling exogenous variables and cross-channel correlations (Paper, Section 4.1, p. 6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The primary metric used to evaluate the model's forecast accuracy is **Mean Squared Error (MSE)** (Paper, Section 4.1, p. 6).

In addition, the following relative improvement metrics are used for comparing TTM to baseline models (Paper, Section 4.1, p. 6):
*   **Forecast improvement percentage (f-imp(%)):** The percentage improvement in MSE of TTM over a baseline model, averaged across all datasets.
*   **Size improvement metric (s-imp(X)):** The ratio of the baseline model's size (total parameters) to the TTM model's size.

### Decision thresholds:
The model performs forecasting, which is a regression task. Therefore, decision thresholds typically used for classification tasks are not applicable (Derived from model's task).

### Variation approaches:
Model performance is evaluated across all sliding windows of the test set for a standard test protocol (Paper, Appendix F.1, p. 23). For comparison with some specific benchmarks (like Chronos and Lag-llama), evaluation is performed only on the last test window, as recommended by those models' authors (Paper, p. 8). Hyperparameters for the model are chosen based on performance on a validation set (Paper, Section 4.3, p. 7).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on eleven public datasets, divided into two sets (Paper, Section 4.1, p. 6; Appendix C.2, p. 19-20).

**Set D1:** Used for general zero/few/full-shot evaluation. These datasets do not contain exogenous variables.
*   **ETT (Electricity Transformer Temperature):** ETTH1, ETTH2 (hourly), ETTM1, ETTM2 (15-minute). 7 channels each.
*   **Weather:** 10-minute intervals, 21 channels.
*   **Electricity (ECL):** Hourly electricity consumption of 321 clients.
*   **Traffic:** Hourly road occupancy rates from 862 sensors on San Francisco Freeways.

**Set D2:** Used to evaluate the model's effectiveness in handling cross-channel correlations and exogenous variables.
*   **Bike Sharing (BS):** Hourly bike rental counts in Washington D.C., with 11 weather-related features as exogenous variables.
*   **Carbon Capture Plant (CC):** Emission profiles collected every 2 minutes, with 5 control variables treated as exogenous.
*   **Service (SER) & Application (APP):** Business KPIs and IT events from a simulated e-commerce application, with IT events treated as exogenous variables.

A detailed breakdown of these datasets is available in Table 9 of the paper (Paper, p. 20).

### Motivation:
*   The **D1 datasets** were chosen because they are standard benchmarks that have been "popularly used in most prior state-of-the-art (SOTA) works" (Paper, Section 4.1, p. 6).
*   The **D2 datasets** were specifically selected because they "contain any exogenous variables nor exhibit cross-channel correlation benefits," allowing for a targeted evaluation of the decoder's channel mixing and the exogenous mixer module (Paper, Section 4.1, p. 6).

### Preprocessing:
For the D1 datasets, the same train/validation/test splitting protocol as used in prior literature was followed to ensure fair comparison (Paper, Appendix C.2, p. 20). The standard preprocessing steps applied to all data before being fed to the model are instance normalization and patching (Paper, Section 2.2, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a large corpus of approximately 1 billion samples derived from public time series datasets (Paper, Section 4.1, p. 6). The data comes from two main sources:
1.  **Monash Time Series Forecasting Archive:** A subset of datasets from this repository was used, excluding those with very short lengths (e.g., yearly, monthly) (Paper, Appendix C.1, p. 18).
2.  **LibCity:** All datasets released by the Moirai authors were used (Paper, Appendix C.1, p. 19).

A complete list of the pre-training datasets is provided in Table 8 of the paper (Paper, p. 19). These datasets are diverse in domain, temporal resolution, length, and number of channels. Importantly, there is no overlap between the pre-training datasets and the evaluation datasets (Paper, Appendix C.1, p. 19).

### Motivation:
The choice of a large and diverse collection of datasets was motivated by the goal of building a general pre-trained foundation model for time series that can effectively transfer learn to new, unseen tasks (Paper, p. 2). The paper highlights that "resolution diversity" in the pre-training data is a crucial factor for generalization, even more so than the sheer volume of data (Paper, Section 4.9, p. 11).

### Preprocessing:
The following preprocessing steps were applied to the training data:
*   **Univariate Transformation:** For pre-training, multivariate datasets were transformed into a collection of independent univariate time series to handle the varying number of channels across datasets (Paper, Section 3.1, p. 4).
*   **Instance Normalization:** Each time series instance is normalized to have zero mean and unit standard deviation to handle potential distribution shifts (Paper, Section 2.2, p. 4).
*   **Patching:** The normalized time series is divided into non-overlapping windows or "patches" (Paper, Section 2.2, p. 4).
*   **Diverse Resolution Sampling (DRS):** This data augmentation technique was applied to high-resolution datasets to generate new, lower-resolution samples. This helps to balance the dataset resolutions and improve model performance (Paper, Section 3.1.1, p. 5).
*   **Temporal Cross-Validation:** A moving window technique was used to create training pairs from the time series data (Paper, Appendix C.1.1, p. 19).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents extensive results disaggregated by individual factors.
*   **Performance per Dataset:** Tables 1 and 2 show the model's performance (MSE) on individual datasets like ETTH1, ETTH2, Weather, etc., comparing different TTM variants (TTMB, TTME, TTMA) against other SOTA models (Paper, p. 7-8).
*   **Impact of Architectural Components:** Table 7 analyzes the impact of Adaptive Patching (AP) and Resolution Prefix Tuning (RPT) by showing the change in MSE with and without these components (Paper, p. 12).
*   **Impact of Pre-training Data:** Figure 3 shows the improvement in MSE as the pre-training data is expanded from the Monash dataset to the full 1B sample dataset with DRS, demonstrating the impact of data quantity and quality (Paper, p. 11).

### Intersectional results:
The paper provides results across combinations of factors.
*   **Performance by Dataset and Forecast Length:** The appendix contains detailed tables showing MSE scores for each TTM variant on each of the D1 evaluation datasets across four different forecast lengths (FL ∈ {96, 192, 336, 720}). For example, Table 13 shows the zero-shot performance of TTMB, TTME, and TTMA on the ETTH1 dataset for FL=96, FL=192, etc. (Paper, Appendix F.2, p. 25).
*   **Performance by Dataset and Fine-tuning Strategy:** Table 4 shows the performance on D1 datasets when using a 5% few-shot fine-tuning strategy (Paper, p. 9). Table 5 shows performance using a full-shot head probing strategy (Paper, p. 10).
*   **Performance on Exogenous Datasets:** Table 6 shows the performance of TTMQ-CM (Quick TTM with Channel Mixing) on the D2 datasets (BS, CC, APP, SER), demonstrating the effectiveness of the exogenous fusion and channel mixing modules on datasets that have these specific characteristics (Paper, p. 10).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The maximum GPU memory required for inference with the TTMB (1M) variant is **0.06 GB** (Paper, Table 3, p. 9).

### Deploying Requirements:
The model is lightweight and designed for efficient deployment.
*   **CPU/GPU:** Inference can be executed on both GPUs and "CPU-only machines" (Paper, Abstract, p. 1).
*   **Inference Time:** For the TTMB variant with a batch size of 32, the inference time per batch is **4.7 ms on an A100 GPU** and **0.01 seconds on a CPU** (Paper, Table 3, p. 9; Appendix D.3, p. 21).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The primary TTM variants were pre-trained on **6 NVIDIA A100 GPUs**, a process that took **24-30 hours** (Paper, Section 4.3, p. 7).
*   **Fine-tuning:** The fine-tuning process is "highly efficient and fast, requiring only **1 GPU or even CPU execution**" (Paper, Section 4.3, p. 7). The paper specifies that fine-tuning experiments were executed on a single A100 GPU (Paper, Appendix D.2, p. 21).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided paper does not contain a dedicated section on ethical considerations. The datasets used for pre-training and evaluation are publicly available and primarily consist of non-personal data such as electricity consumption, weather patterns, and traffic metrics (Paper, Appendix C, p. 18-20). The Business and IT observability datasets (APP, SER) are from a simulated e-commerce application (Paper, Appendix C.2, p. 20). No use of sensitive or personally identifiable information is mentioned. Potential risks, misuse cases, and mitigation strategies are not discussed in the provided materials.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper identifies several limitations and areas for future work (Paper, Section H, p. 26-27):
*   **Task-Specific Focus:** TTM is currently focused solely on forecasting. It does not support other time series analysis tasks like classification, regression, or anomaly detection.
*   **Point Forecasting Only:** The model provides point forecasts (a single value) and does not currently support probabilistic forecasting (a distribution of possible outcomes).
*   **Context Length Sensitivity:** The model's architecture is sensitive to the context length of the input time series. Consequently, different model variants are optimized for different context lengths, and the backbone cannot automatically adapt to dynamically varying context lengths.

### Recommendations:
The paper provides the following recommendations for users:
*   **Adapting to Forecast Lengths:** If a pre-trained model is not available for a specific target forecast length (FL), users can adapt an existing TTM using two techniques:
    1.  **Pruning:** Take a model trained on a longer FL and prune its head to match the target FL. This works well for large differences in FL.
    2.  **Recursive Prediction:** Take a model trained on a shorter FL and apply it recursively to reach the target FL. This is effective for smaller adaptations.
    (Paper, Section 4.7, p. 10-11)
*   **Choosing a Fine-tuning Strategy:** Users can choose a fine-tuning strategy based on their data availability: zero-shot for no target data, few-shot for a small amount of data (5-10% of the training set), and full-shot head probing for when the entire training set is available (Paper, Section 3.2, p. 6).
*   **Use on Multivariate Data:** For multivariate forecasting tasks with cross-channel correlations or exogenous variables, it is recommended to enable the decoder's channel-mixing and the exogenous mixer module during fine-tuning to achieve the best performance (Paper, Section 4.6, p. 9).