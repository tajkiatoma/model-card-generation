## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, CogVideoX, was developed by researchers from Tsinghua University and Zhipu AI (2408.06072.pdf, p. 1). The development team is also referred to as the "CogVideoX Model Team" (LICENSE.txt). The core contributors are listed as Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, and Xiaotao Gu (2408.06072.pdf, p. 1).

### Model date:
The academic paper describing the model was submitted to arXiv on August 12, 2024, with the provided version (v3) dated March 26, 2025 (2408.06072.pdf, p. 1).

### Model version:
The developers have released two versions of the model, differing in size (2408.06072.pdf, p. 2):
*   **CogVideoX-5B:** A 5 billion parameter model.
*   **CogVideoX-2B:** A 2 billion parameter model.

The paper indicates that the 5B model generally outperforms the 2B version across most evaluation metrics, demonstrating the scalability of the architecture (2408.06072.pdf, p. 2, 10). Both text-to-video and image-to-video versions have been publicly released (2408.06072.pdf, p. 3).

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer architecture (2408.06072.pdf, p. 1). Its core components are:

1.  **3D Variational Autoencoder (VAE):** An `AutoencoderKLCogVideoX` that compresses videos across both spatial and temporal dimensions to create a latent representation. It is designed to achieve an 8x8x4 compression from pixels to latents (2408.06072.pdf, p. 4). Key VAE configuration parameters include `latent_channels: 16` and `block_out_channels: [128, 256, 256, 512]` (vae/config.json.txt).
2.  **Text Encoder:** A `T5EncoderModel` is used to encode textual prompts into embeddings (model_index.json.txt; 2408.06072.pdf, p. 3). This T5 model has 24 layers, a model dimension (`d_model`) of 4096, 64 attention heads, and a vocabulary size of 32128 (text_encoder/config.json.txt). The total size of the text encoder is approximately 9.5 GB (text_encoder/model.safetensors.index.json.txt).
3.  **Expert Transformer:** The main diffusion model is a `CogVideoXTransformer3DModel` which processes the concatenated text and video latent embeddings (model_index.json.txt; 2408.06072.pdf, p. 3). It uses an "expert" design with Expert Adaptive LayerNorm to handle the different modalities (text and vision) independently within the same sequence (2408.06072.pdf, p. 5). It employs 3D full attention to model spatio-temporal dimensions comprehensively (2408.06072.pdf, p. 5).
    *   **CogVideoX-5B:** 42 layers, 48 attention heads, hidden size of 3072 (2408.06072.pdf, p. 16).
    *   **CogVideoX-2B:** 30 layers, 32 attention heads, hidden size of 1920 (2408.06072.pdf, p. 16).
    *   The transformer has a maximum text sequence length of 226 (transformer/config.json.txt). The total size of the transformer is approximately 11.1 GB (transformer/diffusion_pytorch_model.safetensors.index.json.txt).

The model can generate videos up to 10 seconds long at 16 fps, with resolutions as high as 768 × 1360 pixels (2408.06072.pdf, p. 1, 3).

### Training details:
The model was trained using a combination of images and videos, with a diffusion process that adopts v-prediction (2408.06072.pdf, p. 6; scheduler/scheduler_config.json.txt). Key training methodologies include:

*   **Progressive Training:** The model was first trained on low-resolution videos (256px) to learn semantics and then progressively trained on higher resolutions (up to 768px) to learn high-frequency details (2408.06072.pdf, p. 6). A final high-quality fine-tuning stage was performed on a curated 20% subset of the data (2408.06072.pdf, p. 15).
*   **Multi-Resolution Frame Packing:** To handle videos of varying lengths and resolutions efficiently, videos are packed together into batches with consistent shapes, inspired by the "Patch'n Pack" method (2408.06072.pdf, p. 6).
*   **Positional Encoding:** The model uses 3D Rotary Position Embedding (RoPE) to effectively model the spatio-temporal relationships in video data (2408.06072.pdf, p. 5).
*   **Explicit Uniform Sampling:** To stabilize the training loss, the diffusion timesteps (from 1 to T) are divided into intervals, and each parallel training rank samples a timestep from its assigned interval, ensuring a more uniform distribution (2408.06072.pdf, p. 7).
*   **Hyperparameters:** The model was trained with the Adam optimizer (`beta1=0.9`, `beta2=0.95`), a weight decay of 1e-4, and a cosine learning rate decay schedule. The training was done using BF16 precision (2408.06072.pdf, p. 16).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Zhuoyi Yang, et al. "COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER." arXiv preprint arXiv:2408.06072 (2024). Published as a conference paper at ICLR 2025 (2408.06072.pdf, p. 1).

A demo website is also available to view more video examples:
*   https://yzy-thu.github.io/CogVideoX-demo/ (2408.06072.pdf, p. 1).

### Citation details:
```bibtex
@article{yang2024cogvideox,
  title={COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Zhang, Yuxuan and Gu, Xiaotao and Hong, Wenyi and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```
(Derived from 2408.06072.pdf)

### License:
The model is released under a custom "The CogVideoX License" (LICENSE.txt).
*   **Academic Use:** The license allows free use of all open-source models in the repository for academic research (LICENSE.txt).
*   **Commercial Use:** For commercial purposes, users must register to obtain a basic commercial license. This allows free commercial use for services with up to 1 million visits per month. If this limit is exceeded, a separate business license must be obtained (LICENSE.txt).
*   **Restrictions:** Users are explicitly forbidden from using the software for any military or illegal purposes. It cannot be used for any act that may undermine China's national security, harm public interest, or infringe upon human rights (LICENSE.txt).
*   **Disclaimer:** The software is provided "AS IS" without any warranty, and the authors or copyright holders are not liable for any claims or damages arising from its use (LICENSE.txt).

### Contact:
For questions related to the license and copyright, the contact email is `license@zhipuai.cn` (LICENSE.txt). The corresponding author of the paper can be reached at `jietang@tsinghua.edu.cn` (2408.06072.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of CogVideoX is large-scale text-to-video synthesis. It is designed to generate high-quality, long-duration, and temporally coherent videos from textual descriptions (2408.06072.pdf, p. 1).

Specific capabilities include:
*   Generating 10-second continuous videos at 16 fps (2408.06072.pdf, p. 1).
*   Producing high-resolution videos, up to 768 × 1360 pixels, with multiple aspect ratios (2408.06072.pdf, p. 3).
*   Creating videos with coherent narratives, diverse shapes, and dynamic movements that align closely with the input text prompt (2408.06072.pdf, p. 1).
*   The model also has an image-to-video version, which can generate videos conditioned on a starting image in addition to a text prompt (2408.06072.pdf, p. 17).

### Primary intended users:
The primary intended users are researchers, developers, and content creators in the field of AI and multimedia generation. Given the separate licensing terms, both academic and commercial users are anticipated audiences (LICENSE.txt).

### Out-of-scope uses:
The license explicitly prohibits the following uses:
*   Any military purposes (LICENSE.txt).
*   Any illegal purposes (LICENSE.txt).
*   Any activities that may undermine China's national security and national unity, harm the public interest of society, or infringe upon the rights and interests of human beings (LICENSE.txt).

---

## How to Use
This section outlines how to use the model.

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper focuses on data quality as a key factor influencing performance. The developers designed a comprehensive data filtering pipeline to remove videos with detrimental characteristics, such as (2408.06072.pdf, p. 7):
*   **Editing:** Videos with noticeable artificial processing or special effects.
*   **Lack of Motion Connectivity:** Artificially spliced videos or those edited from static images.
*   **Low Quality:** Videos with unclear visuals or excessive camera shake.
*   **Lecture Type:** Videos with minimal motion, such as lectures or live streams.
*   **Text Dominated:** Videos containing a large amount of visible text.
*   **Noisy Screenshots:** Poor-quality videos captured from screens.

### Evaluation factors:
The model was evaluated on the following factors, derived from the Vbench benchmark and a custom human evaluation framework (2408.06072.pdf, p. 9, 10):
*   **Automated Evaluation:** Human Action, Scene, Dynamic Degree, Multiple Objects, Appearance Style, Dynamic Quality.
*   **Human Evaluation:** Sensory Quality, Instruction Following, Physics Simulation, Cover Quality.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of metrics:
*   **VAE Reconstruction Quality:** Peak Signal-to-Noise Ratio (PSNR) to measure restoration quality and a Flickering metric (L1 difference between adjacent frames) to measure temporal stability (2408.06072.pdf, p. 4, 9).
*   **Text-Video Alignment & Quality (Automated):**
    *   Metrics from Vbench: Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (2408.06072.pdf, p. 9).
    *   Dynamic Quality: A metric that integrates quality and dynamic scores to evaluate dynamism without penalizing for complexity (2408.06072.pdf, p. 10).
    *   GPT4O-MTScore: A metric using GPT-4o to measure the "metamorphic amplitude" of videos (2408.06072.pdf, p. 10).
    *   Fréchet Video Distance (FVD) and CLIP4Clip Score were used for ablation studies (2408.06072.pdf, p. 9).
*   **Human Evaluation:** A panel of evaluators scored videos on a scale from 0 to 1 across four aspects: Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality (2408.06072.pdf, p. 10, 28).

### Decision thresholds:
During training data preparation, optical flow scores and image aesthetic scores were calculated for all videos. The thresholds for these scores were dynamically adjusted during training to ensure the dynamic and aesthetic quality of the data used (2408.06072.pdf, p. 7).

### Variation approaches:
*   **Ablation Studies:** Conducted on a test set of 500 videos from the WebVid dataset (2408.06072.pdf, p. 9).
*   **Automated Evaluation:** Performed using the Vbench benchmark suite (2408.06072.pdf, p. 9).
*   **Human Evaluation:** A panel of evaluators assessed videos generated from 100 "meticulously crafted prompts" characterized by broad distribution and clear articulation (2408.06072.pdf, p. 28).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **WebVid:** A validation set of 500 videos from the WebVid dataset was used for VAE reconstruction evaluation and ablation studies (2408.06072.pdf, p. 9).
*   **Vbench:** The Vbench benchmark was used for the main automated evaluation of text-to-video generation capabilities (2408.06072.pdf, p. 9).
*   **Custom Prompts:** For human evaluation, a set of 100 meticulously crafted prompts was used (2408.06072.pdf, p. 28).

### Motivation:
The Vbench metrics were chosen because they are designed to be consistent with human perception of video quality (2408.06072.pdf, p. 9). The human evaluation framework was established to provide a more comprehensive assessment of general capabilities beyond automated metrics (2408.06072.pdf, p. 10).

### Preprocessing:
Insufficient information

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was a large-scale collection of video-text and image-text pairs (2408.06072.pdf, p. 7).
*   **Videos:** Approximately 35 million single-shot video clips after filtering. Each clip averages about 6 seconds in duration.
*   **Images:** 2 billion images from the LAION-5B and COYO-700M datasets were used to assist training.

### Motivation:
The large and diverse dataset was constructed to train a powerful, general-purpose text-to-video model. The inclusion of images allows for joint training, which can improve the model's understanding of visual concepts (2408.06072.pdf, p. 6). The extensive filtering and re-captioning efforts were motivated by the need for high-quality, accurately described data, which is often lacking in raw web-scraped videos (2408.06072.pdf, p. 7).

### Preprocessing:
The training data underwent an extensive and innovative preprocessing pipeline (2408.06072.pdf, p. 7-8):
1.  **Video Filtering:** Raw video data was filtered to remove low-quality or unsuitable content. A set of negative labels (e.g., "Low Quality," "Lecture Type," "Editing") was defined, and 20,000 videos were manually annotated. These annotations were used to train six classifier models based on Video-LLaMA to screen the entire video dataset.
2.  **Video Captioning:** Since most web videos lack descriptive text, a "Dense Video Caption Data Generation" pipeline was created:
    *   A video caption model generates an initial short caption.
    *   The CogVLM image model creates dense, frame-by-frame descriptions.
    *   GPT-4 is used to summarize the frame descriptions into a final, comprehensive video caption.
    *   To scale this process, a LLaMA2 model was fine-tuned on the GPT-4 summary data to automate the final caption generation.
    *   This process was further accelerated by fine-tuning an end-to-end video understanding model, CogVLM2-Caption.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was benchmarked against other state-of-the-art text-to-video models.

**Automated Evaluation Results (Table 3):**
CogVideoX-5B achieved the best performance in 5 out of 7 metrics compared to models like T2V-Turbo, VideoCrafter-2.0, and OpenSora V1.2.
*   **Human Action:** 96.8
*   **Scene:** 55.44
*   **Dynamic Degree:** 62.22
*   **Multiple Objects:** 70.95
*   **Appearance Style:** 24.44
*   **Dynamic Quality:** 69.5
*   **GPT4O-MTScore:** 3.36

**VAE Reconstruction Results (Table 2):**
The model's 3D VAE achieved the lowest (best) flickering score and the highest (best) PSNR compared to Open-Sora and Open-Sora-Plan VAEs.
*   **Flickering:** 85.5
*   **PSNR:** 29.1

**Human Evaluation Results (Table 4):**
CogVideoX-5B was compared against the closed-source model Kling and won the human preference across all evaluated aspects.
*   **Sensory Quality:** 0.722
*   **Instruction Following:** 0.495
*   **Physics Simulation:** 0.667
*   **Cover Quality:** 0.712
*   **Total Score:** 2.74

(Source for all results: 2408.06072.pdf, p. 9-10)

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The inference memory requirements provide an estimate for loading the model. For the 5B model, it requires at least 26 GB of memory for lower resolutions and up to 76 GB for higher resolutions (2408.06072.pdf, p. 16).

### Deploying Requirements:
Inference was evaluated on an H800 GPU with 50 inference steps. The memory and time consumption for generating videos are as follows (2408.06072.pdf, p. 16):

**CogVideoX-5B:**
*   **480x720, 6s video:** 113 seconds, 26 GB memory
*   **768x1360, 5s video:** 500 seconds, 76 GB memory

**CogVideoX-2B:**
*   **480x720, 6s video:** 49 seconds, 18 GB memory
*   **768x1360, 5s video:** 220 seconds, 53 GB memory

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model's license includes specific restrictions to mitigate ethical risks. Users are prohibited from using the model and its outputs for (LICENSE.txt):
*   Any military purposes.
*   Any illegal purposes.
*   Actions that could harm national security, public interest, or individual rights.

The development process included a significant data filtering stage. While the primary goal was to improve model performance by removing low-quality content, this process can also serve as a mitigation strategy against training on potentially harmful, biased, or inappropriate data by curating the training set (2408.06072.pdf, p. 7). The paper does not specify if sensitive data was used, but the training data sources (LAION-5B, COYO-700M, and web videos) are known to be large, uncurated datasets that may contain personal information or reflect societal biases. The potential risks associated with misuse of generative video technology, such as the creation of misinformation or harmful content, are not explicitly detailed in the provided documents beyond the license restrictions.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Semantic Degradation:** The final fine-tuning stage on a high-quality subset of data, while improving visual quality and removing artifacts like watermarks, was observed to cause a "slight degradation in the model's semantic ability" (2408.06072.pdf, p. 15).
*   **VAE Compression Limits:** The paper notes that exploring VAEs with even larger compression ratios is an area for future work, as overly aggressive compression was found to make model convergence difficult (2408.06072.pdf, p. 4).
*   **Computational Cost:** The model's use of 3D full attention, while beneficial for capturing large motions and ensuring temporal consistency, is more computationally intensive than separated 2D+1D attention mechanisms (2408.06072.pdf, p. 5, 16).

### Recommendations:
*   **Prompt Upsampling:** To achieve the best results, it is recommended to use a Large Language Model (LLM) to upsample short user prompts into more detailed and descriptive ones before feeding them to the model. This helps align the distribution of inference-time prompts with the detailed captions used during training (2408.06072.pdf, p. 23).