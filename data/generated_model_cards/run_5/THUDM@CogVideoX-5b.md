## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University and Zhipu AI (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 1). The development team is also referred to as the "CogVideoX Model Team" (Source: The CogVideoX License).

### Model date:
The associated academic paper was published as a conference paper at ICLR 2025 and submitted to arXiv on March 26, 2025 (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 1).

### Model version:
The model has been released in two sizes: CogVideoX-5B (5 billion parameters) and CogVideoX-2B (2 billion parameters). The paper indicates that the 5B version outperforms the 2B version, suggesting that the model is scalable (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 2).

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer architecture (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Abstract, page 1).

**Architecture:**
The model's architecture consists of several key components (Source: `pipeline.json`):
*   **3D Variational Autoencoder (VAE):** A 3D causal VAE (`AutoencoderKLCogVideoX`) is used to compress videos across both spatial and temporal dimensions into a latent space. This VAE is composed of an encoder and a decoder with symmetrically arranged ResNet block stages that perform downsampling and upsampling (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 2.1, pages 3-4; `vae/config.json`).
*   **Expert Transformer:** The core of the model is an expert transformer (`CogVideoXTransformer3DModel`) that operates on the concatenated latent representations of video and text embeddings. It uses an "Expert Adaptive LayerNorm" to handle the different modalities and employs 3D full attention to model video across temporal and spatial dimensions (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 2.2, page 5).
*   **Text Encoder:** A T5 Encoder (`T5EncoderModel`) is used to encode the input text prompts into text embeddings (Source: `pipeline.json`; `text_encoder/config.json`).
*   **Tokenizer:** A T5 Tokenizer (`T5Tokenizer`) is used for text processing (Source: `pipeline.json`).
*   **Scheduler:** A `CogVideoXDDIMScheduler` is used in the diffusion process (Source: `pipeline.json`).

**Model Size and Context Length:**
*   **CogVideoX-5B:** The transformer has 42 layers, 48 attention heads, and a hidden size of 3072 (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 6, page 16; `transformer/config.json`). The text encoder has 24 layers and a model dimension of 4096 (Source: `text_encoder/config.json`). The total size of the transformer weights is approximately 11.1 GB, and the text encoder weights are approximately 9.5 GB (Source: `transformer/diffusion_pytorch_model.safetensors.index.json`; `text_encoder/model.safetensors.index.json`).
*   **CogVideoX-2B:** The transformer has 30 layers, 32 attention heads, and a hidden size of 1920 (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 6, page 16).
*   **Context Length:** The model supports a maximum text sequence length of 226 tokens (Source: `transformer/config.json`; `tokenizer/tokenizer_config.json`).

### Training details:
The model is trained using a diffusion framework with several innovative techniques:
*   **Diffusion Setting:** The training objective uses v-prediction and zero Signal-to-Noise Ratio (SNR), following the noise schedule from Latent Diffusion Models (LDM) (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3, page 6).
*   **Progressive Training:** The model is first trained on low-resolution (256px) videos to learn semantics and then progressively trained on higher resolutions (up to 768px) to learn high-frequency details (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.2, page 6).
*   **Multi-Resolution Frame Packing:** To handle videos of varying lengths and resolutions, the model uses a frame packing strategy. This allows videos of different durations to be placed into the same batch, ensuring consistent data shapes and maximizing data utilization (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.1, page 6).
*   **Positional Embedding:** The model uses 3D Rotary Position Embedding (3D-RoPE) to effectively model the spatial and temporal relationships in video data (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 2.2, page 5).
*   **Explicit Uniform Sampling:** To stabilize the training loss, the range of diffusion timesteps is divided into intervals, and each parallel training rank samples uniformly from its assigned interval. This ensures a more uniform distribution of timesteps and accelerates convergence (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.3, page 7).
*   **Hyperparameters:** Detailed hyperparameters for both the 2B and 5B models, including layer counts, attention heads, hidden sizes, and training steps per stage, are provided in the academic paper (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Tables 5 & 6, page 16).

### Paper or other resource for more information:
*   **Academic Paper:** The primary resource is the paper "COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER," published at ICLR 2025. It details the model architecture, training process, and evaluation results (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER).
*   **Demo Website:** A demo website is available at https://yzy-thu.github.io/CogVideoX-demo/ (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 1).
*   **Repository:** The code and model checkpoints are published at https://github.com/THUDM/CogVideo (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 2).

### Citation details:
Insufficient information. A BibTeX entry is not provided in the repository.

### License:
The model is released under a custom "The CogVideoX License" (Source: The CogVideoX License).
*   **Academic Use:** The license allows free use of all open-source models in the repository for academic research.
*   **Commercial Use:** Commercial use requires registration to obtain a basic commercial license. This license is free for commercial activities with service users (visits) not exceeding 1 million per month. For usage exceeding this limit, a separate commercial license must be obtained from the business team.
*   **Restrictions:** Users are prohibited from using the software for any military or illegal purposes. Additionally, the software cannot be used for any act that may undermine China's national security and national unity, harm the public interest, or infringe upon human rights.
*   **Disclaimer:** The software is provided "AS IS" without any warranty, and the authors or copyright holders are not liable for any claims or damages.
(Source: The CogVideoX License).

### Contact:
For questions related to the license and copyright, contact `license@zhipuai.cn` (Source: The CogVideoX License). For academic inquiries, contact the paper's authors at `{yangzy22, tengjy24}@mails.tsinghua.edu.cn` or the corresponding author at `jietang@tsinghua.edu.cn` (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed for large-scale text-to-video generation. Its primary purpose is to generate coherent, long-duration (up to 10 seconds), and high-resolution (up to 768x1360 pixels) videos with rich motion and semantics that align with text prompts (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Abstract, page 1). The model also has an image-to-video version, which can generate videos conditioned on both a text prompt and an input image (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Appendix D, page 17).

### Primary intended users:
The license terms indicate the intended users include:
*   **Academic Researchers:** For non-commercial research purposes (Source: The CogVideoX License).
*   **Developers and Businesses:** For commercial applications, with specific licensing tiers based on usage volume (Source: The CogVideoX License).

### Out-of-scope uses:
The license explicitly prohibits the following uses:
*   Any military purposes (Source: The CogVideoX License).
*   Any illegal purposes (Source: The CogVideoX License).
*   Any activities that may undermine China's national security and unity, harm social public interest, or infringe upon the rights and interests of human beings (Source: The CogVideoX License).

---

## How to Use
This section outlines how to use the model. 

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the quality of the training data. The development process involved extensive data filtering, suggesting that the following factors are relevant to generation quality:
*   **Motion and Dynamics:** The model is designed to capture dynamic scenes. Videos with a lack of motion connectivity or minimal effective motion (e.g., lecture-style videos) were filtered from the training data (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).
*   **Visual Quality:** Factors such as camera shake, unclear visuals, and poor quality from screen recordings were considered detrimental and filtered out (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).
*   **Content Type:** Videos with noticeable artificial editing, special effects, or a large amount of visible text were filtered to maintain visual integrity and focus on non-textual content (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).

### Evaluation factors:
The model was evaluated on the following factors:
*   **Automated Evaluation:** Human Action, Scene, Dynamic Degree, Multiple Objects, Appearance Style, Dynamic Quality, and GPT4O-MTScore (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 3, page 10).
*   **Human Evaluation:** Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 4.2.2, page 10).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a combination of automated metrics and human evaluation.
*   **Automated Metrics:**
    *   **Vbench Metrics:** Several metrics consistent with human perception were used, including Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 4.2.1, page 9).
    *   **Dynamism Metrics:** To evaluate motion richness, `Dynamic Quality` and `GPT4O-MTScore` were used (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, page 10).
    *   **VAE Reconstruction Metrics:** The 3D VAE's performance was measured using Peak Signal-to-Noise Ratio (PSNR) and a Flickering score (L1 difference between adjacent frames) (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 1, page 4; Section 4.2.1, page 9).
*   **Human Evaluation:**
    *   A comprehensive framework was established where human evaluators scored generated videos on four aspects: Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality. Scores were assigned on a scale of 0, 0.5, or 1 for each aspect based on detailed guidelines (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 4.2.2, page 10 and Appendix J, page 28).

### Decision thresholds:
During training, thresholds for optical flow scores and image aesthetic scores of training videos were dynamically adjusted to ensure the quality of the data. The lowest aesthetic value used for training was 4.5 (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7; Table 6, page 16).

### Variation approaches:
Insufficient information. The paper does not describe the use of statistical methods like cross-validation or bootstrapping for calculating performance metrics.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **WebVid Dataset:** The WebVid validation set was used to evaluate the VAE reconstruction effect. Ablation studies were conducted on a test set of 500 videos from WebVid (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 4.2.1, page 9; Figure 8 caption, page 9).
*   **Human Evaluation Prompts:** A set of 100 "meticulously crafted prompts" characterized by broad distribution and clear articulation was used for human evaluation (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Appendix J, page 28).

### Motivation:
Insufficient information. The paper does not specify the motivation for choosing the WebVid dataset for evaluation.

### Preprocessing:
Insufficient information. The paper does not describe any preprocessing steps applied to the evaluation data.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was a custom-curated collection comprising:
*   **Videos:** Approximately 35 million single-shot video clips, with an average duration of 6 seconds each, remained after a filtering process (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).
*   **Images:** 2 billion images from the LAION-5B and COYO-700M datasets were used to assist training (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).

### Motivation:
The motivation for creating a custom dataset was to address the common issues of noise and lack of descriptive text in raw online video data. The goal was to construct a collection of relatively high-quality video clips with comprehensive text descriptions to train a robust text-to-video model (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).

### Preprocessing:
An extensive preprocessing pipeline was developed for both filtering and captioning the data.
*   **Video Filtering:** A set of negative labels was defined to identify low-quality content, including "Editing," "Lack of Motion Connectivity," "Low Quality," "Lecture Type," "Text Dominated," and "Noisy Screenshots." Classifiers based on Video-LLaMA were trained on 20,000 manually annotated videos to screen the dataset. Additionally, optical flow and image aesthetic scores were calculated and used to filter videos dynamically during training (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, page 7).
*   **Video Captioning:** A "Dense Video Caption Data Generation" pipeline was created to generate high-quality text descriptions. This involved:
    1.  Generating initial short captions for videos.
    2.  Using the CogVLM model to create dense image captions for extracted frames.
    3.  Employing GPT-4 to summarize the dense image captions into a final, comprehensive video caption.
    4.  Fine-tuning a LLaMA model on the GPT-4 summaries to scale up the caption generation process (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 3.4, pages 7-8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents several quantitative results for the model and its components:
*   **Comparative Performance:** Table 3 shows the performance of CogVideoX-5B and CogVideoX-2B against other text-to-video models across seven automated metrics. CogVideoX-5B achieved the best performance in five of these metrics (Human Action, Scene, Multiple Objects, Dynamic Quality, GPT4O-MTScore) (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 3, page 10).
*   **Human Evaluation:** Table 4 compares CogVideoX-5B with the Kling model, showing that CogVideoX-5B achieved higher scores across all four human evaluation aspects (Sensory Quality, Instruction Following, Physics Simulation, Cover Quality) (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 4, page 10).
*   **VAE Reconstruction:** Table 2 compares the model's 3D VAE with other open-source VAEs, showing it achieves the best PSNR (29.1) and the lowest flickering score (85.5) (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 2, page 9).
*   **Ablation Studies:** Figure 8 presents ablation results on the WebVid dataset, comparing different architectures (Expert AdaLN vs. MMDIT), attention mechanisms (3D Full vs. 2D+1D), and sampling methods (with vs. without Explicit Uniform Sampling) using FVD and CLIP4Clip scores (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Figure 8, page 9).

### Intersectional results:
Insufficient information. The paper does not provide performance results across combinations of factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Inference time and memory consumption were evaluated on an "H800" GPU with 50 inference steps.
*   **CogVideoX-5B:**
    *   At 480x720 resolution (6s video): 113 seconds, 26 GB memory.
    *   At 768x1360 resolution (5s video): 500 seconds, 76 GB memory.
*   **CogVideoX-2B:**
    *   At 480x720 resolution (6s video): 49 seconds, 18 GB memory.
    *   At 768x1360 resolution (5s video): 220 seconds, 53 GB memory.
(Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Table 7, page 16).

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The model's license includes specific restrictions to mitigate ethical risks. Users are prohibited from using the model, in whole or in part, for:
*   Any military purposes.
*   Any illegal purposes.
*   Any act that may undermine China's national security and national unity.
*   Any act that may harm the public interest of society.
*   Any act that may infringe upon the rights and interests of human beings.
(Source: The CogVideoX License).

The provided repository does not specify whether sensitive data was used during training or detail other risk mitigation strategies beyond the license restrictions. The potential risks associated with misuse of generative video models (e.g., creation of misinformation or harmful content) are not explicitly detailed, though the license restrictions aim to prevent such applications.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Semantic Degradation:** High-quality fine-tuning, while improving visual quality and removing artifacts like watermarks, was observed to cause a slight degradation in the model's semantic ability (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Appendix A, page 15).
*   **VAE Compression Limits:** While the 3D VAE improves performance, overly aggressive spatial-temporal compression ratios (e.g., 16x16x8) can make model convergence extremely difficult. Exploring VAEs with larger compression ratios is identified as future work (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Section 2.1, page 4).
*   **Attention Mechanism Instability:** The use of separated spatial and temporal attention (2D+1D) was found to be unstable and prone to collapse during training for large-scale models, unlike the more stable 3D full attention mechanism (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, "3D Full Attention" paragraph, page 9).

### Recommendations:
*   **Positional Encoding for Higher Resolutions:** When adapting the model to generate videos at higher resolutions than it was trained on, it is recommended to use extrapolation for the Rotary Position Embedding (RoPE). This approach was found to retain local details better than interpolation, which tends to generate blurry images (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, Appendix A, page 15).
*   **Training Stability:** For users training similar models, it is recommended to use "Explicit Uniform Sampling" for diffusion timesteps. This method leads to a more stable decrease in the loss curve, better performance, and can accelerate loss convergence (Source: Paper: COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER, "Explicit Uniform Sampling" paragraph, page 9).

---