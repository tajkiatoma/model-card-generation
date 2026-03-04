## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University and Zhipu AI (2408.06072.pdf, p. 1). The authors listed are Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang, Wenyi Hong, Xiaohan Zhang, Guanyu Feng, Da Yin, Yuxuan Zhang, Weihan Wang, Yean Cheng, Bin Xu, Xiaotao Gu, Yuxiao Dong, and Jie Tang (2408.06072.pdf, p. 1).

### Model date:
The associated academic paper was submitted to arXiv on March 26, 2025, and is noted as being published as a conference paper at ICLR 2025 (2408.06072.pdf, p. 1).

### Model version:
The model is released in two sizes: CogVideoX-5B and CogVideoX-2B (2408.06072.pdf, p. 2). The repository files were developed with `_diffusers_version`: "0.31.0.dev0" (model_index.json.txt).

The primary differences between the versions are the model parameters (2408.06072.pdf, p. 16, Table 6):
*   **CogVideoX-5B**: 42 layers, 48 attention heads, hidden size of 3072.
*   **CogVideoX-2B**: 30 layers, 32 attention heads, hidden size of 1920.

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer (DiT) architecture (2408.06072.pdf, p. 1). It is designed to generate coherent, long-duration videos with dynamic motion (2408.06072.pdf, p. 1).

The model's architecture consists of several key components (model_index.json.txt; 2408.06072.pdf, p. 3):
*   **3D Variational Autoencoder (VAE)**: An `AutoencoderKLCogVideoX` compresses videos across both spatial and temporal dimensions into a latent space. It uses a 8x8x4 compression from pixels to latents (2408.06072.pdf, p. 1, 4). The VAE has a scaling factor of 0.7 and the latent space has 16 channels (vae/config.json.txt).
*   **Text Encoder**: A `T5EncoderModel` (`t5-v1_1-xxl`) is used to encode text prompts into embeddings (model_index.json.txt; text_encoder/config.json.txt). It has 24 layers, 64 attention heads, and a model dimension of 4096 (text_encoder/config.json.txt).
*   **Tokenizer**: A `T5Tokenizer` is used for text processing, with a vocabulary size of 32,128 and a maximum length of 226 tokens (tokenizer/tokenizer_config.json.txt; text_encoder/config.json.txt).
*   **Expert Transformer**: A `CogVideoXTransformer3DModel` serves as the core of the diffusion model. It processes concatenated text and video latent embeddings. It features an "expert adaptive LayerNorm" to handle the different modalities and uses 3D full attention to model spatio-temporal relationships (2408.06072.pdf, p. 3, 5). The transformer uses Rotary Position Embedding (RoPE) (2408.06072.pdf, p. 16, Table 6).
*   **Scheduler**: A `CogVideoXDDIMScheduler` is used for the diffusion process, with a `v_prediction` type and 1000 training timesteps (scheduler/scheduler_config.json.txt).

The model is available in two sizes: 5 billion and 2 billion parameters (2408.06072.pdf, p. 2). The maximum text sequence length supported is 226 (transformer/config.json.txt).

### Training details:
CogVideoX was trained using a diffusion-based approach with several key methodologies (2408.06072.pdf, p. 6-7):
*   **Diffusion Setting**: The training objective uses v-prediction and zero Signal-to-Noise Ratio (SNR), following the noise schedule from Latent Diffusion Models (LDM) (2408.06072.pdf, p. 6).
*   **Progressive Training**: The model was first trained on low-resolution (256px) videos to learn semantics and then progressively trained on higher resolutions (512px, 768px) to learn high-frequency details (2408.06072.pdf, p. 6). A final high-quality fine-tuning stage was performed on 20% of the total dataset (2408.06072.pdf, p. 15).
*   **Multi-Resolution Frame Packing**: To handle videos of varying lengths and resolutions efficiently, videos are packed into the same batch to ensure consistent tensor shapes, inspired by Patch'n Pack (2408.06072.pdf, p. 6).
*   **Explicit Uniform Sampling**: To stabilize the training loss, the diffusion timesteps (from 1 to T) are divided into intervals, and each parallel training rank samples a timestep uniformly from its assigned interval. This ensures a more uniform distribution of timesteps across batches (2408.06072.pdf, p. 7).
*   **Hyperparameters**: The model was trained with the BF16 precision. Key hyperparameters for the 5B model include a batch size that decreases from 2000 to 100 as resolution increases, a cosine learning rate decay, and a gradient clipping of 1.0. The position encoding for the 5B model is RoPE, while the 2B model uses sinusoidal encoding (2408.06072.pdf, p. 16, Table 5 & 6).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   **Paper**: Zhuoyi Yang, et al. "COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER." arXiv preprint arXiv:2408.06072 (2025). The paper provides a comprehensive overview of the model's architecture, training process, and evaluation (2408.06072.pdf).
*   **Demo Website**: A demo website with more video examples is available at: https://yzy-thu.github.io/CogVideoX-demo/ (2408.06072.pdf, p. 1).
*   **Repository**: The paper mentions that the code and model checkpoints are published at: https://github.com/THUDM/CogVideo (2408.06072.pdf, p. 2).

### Citation details:
Insufficient information. The provided repository does not contain a BibTeX citation.

### License:
The model is released under the "CogVideoX License" (LICENSE.txt). Key terms include:
*   **Academic Use**: The license allows free use of all open-source models in the repository for academic research (LICENSE.txt).
*   **Commercial Use**: For commercial use, users must register to obtain a basic commercial license. This license is free but is limited to services with fewer than 1 million visits per month. For services exceeding this limit, a separate commercial license must be obtained from the business team (LICENSE.txt).
*   **Restrictions**: The software cannot be used, copied, modified, or distributed for any military or illegal purposes. It also cannot be used for any act that may undermine China's national security, harm public interest, or infringe upon human rights (LICENSE.txt).
*   **Disclaimer**: The software is provided "AS IS" without any warranty, and the authors or copyright holders are not liable for any claims or damages arising from its use (LICENSE.txt).

### Contact:
For questions related to the license and copyright, the contact email is `license@zhipuai.cn` (LICENSE.txt). The corresponding author of the paper is Jie Tang, who can be reached at `jietang@tsinghua.edu.cn` (2408.06072.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
CogVideoX is a text-to-video synthesis model designed for generating high-quality, long-duration videos from textual descriptions (2408.06072.pdf, p. 1). Its capabilities include:
*   **Text-to-Video Generation**: Generating 10-second continuous videos at 16 fps with resolutions up to 768x1360 pixels. The model excels at creating videos with coherent narratives, diverse shapes, and dynamic movements (2408.06072.pdf, p. 1).
*   **Image-to-Video Generation**: A fine-tuned version of the model can generate videos conditioned on an initial image in addition to a text prompt (2408.06072.pdf, p. 17).
*   **Video-to-Video Generation**: By chaining CogVideoX with the CogVLM2-Caption model, it can be used for video-to-video tasks where a source video is first captioned and then used to generate a new video (2408.06072.pdf, p. 26).

The model takes a text prompt as input and outputs a video file. For the image-to-video version, the input is a text prompt and an image (2408.06072.pdf, p. 1, 17).

### Primary intended users:
The license specifies terms for two main groups of users (LICENSE.txt):
*   **Academic Researchers**: Who can use the model freely for research purposes.
*   **Commercial Users/Developers**: Who can use the model for commercial activities, with specific licensing tiers based on usage volume.

### Out-of-scope uses:
The license explicitly prohibits the following uses (LICENSE.txt):
*   Any military purposes.
*   Any illegal purposes.
*   Any activities that may undermine China's national security and unity, harm social public interest, or infringe upon human rights and interests.

---

## How to Use
This section outlines how to use the model. 

Insufficient information. The provided repository does not include code snippets, tutorials, or a `README.md` file with usage instructions. The model's input is a text prompt and its output is a generated video (2408.06072.pdf, p. 1).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The developers identified several factors in the training data that can impact the quality of video generation. A filtering pipeline was developed to handle data with these characteristics (2408.06072.pdf, p. 7):
*   **Editing**: Videos with noticeable artificial processing, re-editing, or special effects.
*   **Lack of Motion Connectivity**: Videos with incoherent motion, often from artificially spliced clips.
*   **Low Quality**: Videos with unclear visuals or excessive camera shake.
*   **Lecture Type**: Videos with minimal motion, such as lectures or live-streamed discussions.
*   **Text Dominated**: Videos containing a large amount of visible text.
*   **Noisy Screenshots**: Poor-quality videos captured from phone or computer screens.

### Evaluation factors:
The model's performance was evaluated based on the following factors (2408.06072.pdf, p. 10):
*   **Automated Evaluation**: Human Action, Scene, Dynamic Degree, Multiple Objects, Appearance Style, Dynamic Quality, and GPT4o-MTScore.
*   **Human Evaluation**: Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a combination of automated metrics and human evaluation (2408.06072.pdf, p. 9-10):
*   **Vbench Metrics**: A suite of metrics consistent with human perception, including Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (2408.06072.pdf, p. 9).
*   **Dynamic Quality**: A metric that integrates various quality measures with dynamic scores to mitigate biases against videos with high motion (2408.06072.pdf, p. 10).
*   **GPT4o-MTScore**: A metric using GPT-4o to measure the metamorphic amplitude of videos, particularly for time-lapse-style content (2408.06072.pdf, p. 10).
*   **Fréchet Video Distance (FVD)** and **CLIP4Clip Score**: Used for ablation studies to measure video quality and text-video alignment (2408.06072.pdf, p. 9).
*   **Peak Signal-to-Noise Ratio (PSNR)** and **Flickering**: Used to evaluate the reconstruction quality of the VAE (2408.06072.pdf, p. 4, 9).
*   **Human Evaluation Framework**: Evaluators scored videos on a scale from 0 to 1 across four aspects: Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality (2408.06072.pdf, p. 10, 28).

### Decision thresholds:
*   During training, thresholds for optical flow scores and image aesthetic scores were dynamically adjusted to ensure the quality of the training data (2408.06072.pdf, p. 7).
*   The lowest aesthetic value for data used in training was set to 4.5 (2408.06072.pdf, p. 16, Table 6).
*   For human evaluation, a detailed rubric was provided with score levels of 0, 0.5, and 1 for different criteria (e.g., Sensory Quality, Instruction Following) (2408.06072.pdf, p. 28-29).

### Variation approaches:
The evaluation was conducted on specific test sets. For ablation studies, the WebVid test set (500 videos) was used. For VAE reconstruction evaluation, the WebVid validation set was used (2408.06072.pdf, p. 9). For human evaluation, a set of 100 "meticulously crafted prompts" was used (2408.06072.pdf, p. 28).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **WebVid**: The WebVid validation set was used for evaluating VAE reconstruction, and a 500-video subset of the WebVid test set was used for ablation studies (2408.06072.pdf, p. 9).
*   **Vbench**: The Vbench benchmark was used for automated metric evaluation against other models (2408.06072.pdf, p. 9).
*   **Custom Prompts**: For human evaluation, a set of 100 custom-crafted prompts was used, designed to have broad distribution and clear articulation (2408.06072.pdf, p. 28).

### Motivation:
The Vbench metrics were chosen because they are designed to be consistent with human perception (2408.06072.pdf, p. 9). The human evaluation framework was established to provide a comprehensive assessment of general capabilities, with a particular emphasis on instruction-following (2408.06072.pdf, p. 10, 28).

### Preprocessing:
Insufficient information. The paper does not specify the preprocessing steps applied to the evaluation data.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was a custom-curated collection from multiple sources (2408.06072.pdf, p. 7):
*   **Videos**: Approximately 35 million single-shot video clips, with an average duration of 6 seconds each.
*   **Images**: 2 billion images sourced from LAION-5B and COYO-700M, filtered for aesthetic quality.

### Motivation:
The goal was to construct a large-scale, high-quality dataset of video-text pairs to train a model capable of capturing the dynamic nature of the world. Since most video data lacks descriptive text, a significant effort was made to filter videos and generate comprehensive captions (2408.06072.pdf, p. 7-8).

### Preprocessing:
The data underwent an extensive preprocessing pipeline (2408.06072.pdf, p. 7-8):
*   **Video Filtering**: A set of 6 classifiers based on Video-LLaMA were trained to screen out low-quality videos. These classifiers identified negative attributes such as artificial editing, lack of motion, poor quality, lecture-style content, text dominance, and noisy screen recordings. Additionally, optical flow and image aesthetic scores were calculated and used for dynamic filtering during training (2408.06072.pdf, p. 7).
*   **Video Captioning**: A "Dense Video Caption Data Generation" pipeline was created to generate detailed text descriptions for the videos. This process involved:
    1.  Generating initial short captions using an existing video caption model.
    2.  Extracting frames and using the CogVLM model to create dense image captions for each frame.
    3.  Using GPT-4 to summarize the dense image captions into a final, comprehensive video caption.
    4.  Fine-tuning a LLaMA2 model on the GPT-4 summaries to scale up the caption generation process (2408.06072.pdf, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of CogVideoX-5B and CogVideoX-2B was benchmarked against other text-to-video models. The results are presented in Table 3 of the paper (2408.06072.pdf, p. 10).

**CogVideoX-5B Performance:**
*   **Human Action**: 96.8
*   **Scene**: 55.44
*   **Dynamic Degree**: 62.22
*   **Multiple Objects**: 70.95
*   **Appearance Style**: 24.44
*   **Dynamic Quality**: 69.5
*   **GPT4o-MTScore**: 3.36

Human evaluation results comparing CogVideoX-5B to the Kling model are shown in Table 4 (2408.06072.pdf, p. 10):
*   **Sensory Quality**: 0.722
*   **Instruction Following**: 0.495
*   **Physics Simulation**: 0.667
*   **Cover Quality**: 0.712
*   **Total Score**: 2.74

### Intersectional results:
Insufficient information. The provided materials do not contain performance results across combinations of factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The memory required for inference on a single H800 GPU with 50 inference steps is provided in Table 7 (2408.06072.pdf, p. 16):
*   **CogVideoX-5B**:
    *   26 GB for 480x720 resolution (6s video)
    *   76 GB for 768x1360 resolution (5s video)
*   **CogVideoX-2B**:
    *   18 GB for 480x720 resolution (6s video)
    *   53 GB for 768x1360 resolution (5s video)

### Deploying Requirements:
See "Loading Requirements" above. The paper notes that inference time for the 5B model at 768x1360 resolution is 500 seconds on an H800 GPU (2408.06072.pdf, p. 16, Table 7).

### Training or Fine-tuning Requirements:
Insufficient information. The paper mentions distributing computation across multiple devices using context parallel for 3D convolutions but does not specify the exact hardware configuration (e.g., number or type of GPUs) used for training (2408.06072.pdf, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The training data includes large web-scraped datasets (LAION-5B, COYO-700M), which may contain sensitive or personal information, though the data was filtered for aesthetics (2408.06072.pdf, p. 7). The paper does not specify if other sensitive data was used or how it was handled.

Potential risks associated with text-to-video models include the generation of misinformation, harmful content, or non-consensual deepfakes. The primary risk mitigation strategy provided is the model's license, which explicitly prohibits use for military, illegal, or rights-infringing purposes (LICENSE.txt). The license states that users must not use the software for any act that may "undermine China's national security and national unity, harm the public interest of society, or infringe upon the rights and interests of human beings" (LICENSE.txt).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Semantic Degradation**: The final fine-tuning stage on high-quality data, while improving visual quality, led to a "slight degradation in the model's semantic ability" (2408.06072.pdf, p. 15).
*   **VAE Compression Limits**: The developers found that overly aggressive spatio-temporal compression (e.g., 16x16x8) made the VAE model's convergence "extremely difficult." Exploring VAEs with larger compression ratios is identified as an area for future work (2408.06072.pdf, p. 4).
*   **Attention Mechanism Instability**: Ablation studies showed that an alternative 2D+1D attention mechanism (separating spatial and temporal attention) was "unstable and prone to collapse" during training for large models, highlighting the importance of the chosen 3D full attention architecture (2408.06072.pdf, p. 9).

### Recommendations:
*   **Prompt Upsampling**: To achieve the best results, it is recommended to use a large language model to upsample short user prompts into more detailed and descriptive ones. This helps align the input distribution during inference with the detailed captions used during training (2408.06072.pdf, p. 23).
*   **Adherence to License**: Users should carefully review and adhere to the usage restrictions outlined in the CogVideoX License, particularly the prohibitions on military, illegal, and harmful applications (LICENSE.txt).