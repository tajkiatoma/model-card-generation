## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University and Zhipu AI (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1). The development team is referred to as the "CogVideoX Model Team" in the license (The CogVideoX License, Section 1).

The core contributors listed in the research paper are Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, and Xiaotao Gu (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1).

### Model date:
The associated research paper was submitted as a conference paper to ICLR 2025, with the preprint version dated March 26, 2025 (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1).

### Model version:
The repository contains two versions of the CogVideoX model based on their size:
*   **CogVideoX-5B**: A 5 billion parameter model.
*   **CogVideoX-2B**: A 2 billion parameter model.

Both machine and human evaluations suggest that CogVideoX-5B outperforms well-known video models, and CogVideoX-2B is very competitive across most dimensions. The performance is noted to be scalable with model size (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 2).

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer architecture (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1). It is designed to generate long-duration, high-resolution videos that are coherent and semantically aligned with text prompts (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1). An image-to-video version of the model was also trained (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 3).

The model's architecture consists of several key components (pipeline.json; CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 3):
*   **Text Encoder**: A `T5EncoderModel` is used to encode textual input into embeddings (pipeline.json; text_encoder/config.json). It has 24 layers, a model dimension of 4096, and 64 attention heads (text_encoder/config.json).
*   **3D Variational Autoencoder (VAE)**: An `AutoencoderKLCogVideoX` compresses videos across both spatial and temporal dimensions into a latent space. It uses 3D convolutions and is designed to achieve a high compression ratio while maintaining video quality and continuity (pipeline.json; vae/config.json; CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1, 3). The VAE has 16 latent channels and achieves an 8x8x4 compression from pixels to latents (vae/config.json; CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 4).
*   **Expert Transformer**: A `CogVideoXTransformer3DModel` serves as the core of the diffusion model. It processes the concatenated text and video latent embeddings (pipeline.json; transformer/config.json). This transformer uses an "expert adaptive LayerNorm" to handle the different modalities (text and video) and employs 3D full attention to model the video across temporal and spatial dimensions (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1, 5). The 5B version has 42 layers and 48 attention heads (transformer/config.json; CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 16).
*   **Scheduler**: A `CogVideoXDDIMScheduler` is used in the diffusion process (pipeline.json; scheduler/scheduler_config.json).

The total size of the transformer weights is approximately 11.14 GB (transformer/diffusion_pytorch_model.safetensors.index.json), and the text encoder weights are approximately 9.52 GB (text_encoder/model.safetensors.index.json).

### Training details:
The training process for CogVideoX involved several key methodologies:
*   **Diffusion Setting**: The model uses a `v_prediction` objective and incorporates a zero Signal-to-Noise Ratio (SNR) noise schedule, following the approach used in Latent Diffusion Models (LDM) (scheduler/scheduler_config.json; CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 6). The training process uses 1000 timesteps (scheduler/scheduler_config.json).
*   **Progressive Training**: To efficiently utilize data and save computational costs, the model was first trained on low-resolution (256px) videos to learn semantics and then progressively trained on higher resolutions (up to 768px) to learn high-frequency details (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 6).
*   **Multi-Resolution Frame Packing**: To handle videos of varying lengths and resolutions within the same batch, the model employs a "Multi-Resolution Frame Pack" technique. This allows for full utilization of the training data and enhances the model's generalization capabilities (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 6).
*   **Explicit Uniform Sampling**: To stabilize the training loss curve, the model uses "Explicit Uniform Sampling". The total timestep range (1 to T) is divided into intervals equal to the number of data parallel ranks, and each rank samples a timestep uniformly from its assigned interval (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).
*   **Hyperparameters**: The 5B model has 42 layers, 48 attention heads, and a hidden size of 3072. It uses Rotary Position Embedding (RoPE). The training was performed with BF16 precision (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 16, Table 6).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   Zhuoyi Yang, Jiayan Teng, et al. "COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER." *arXiv preprint arXiv:2408.06072*, 2025. Published as a conference paper at ICLR 2025 (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1).

Additional resources mentioned in the paper include:
*   **Demo Website**: https://yzy-thu.github.io/CogVideoX-demo/ (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1)
*   **GitHub Repository**: https://github.com/THUDM/CogVideo (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 2)

### Citation details:
Insufficient information. No official BibTeX citation is provided.

### License:
The model is released under a custom license, "The CogVideoX License" (The CogVideoX License). Key terms include:
*   **Academic Use**: The license allows free use of all open-source models in the repository for academic research (The CogVideoX License, Section 2).
*   **Commercial Use**:
    *   Users must register at https://open.bigmodel.cn/mla/form to obtain a basic commercial license (The CogVideoX License, Section 2).
    *   With the basic license, commercial use is free for services with up to 1 million visits per month (The CogVideoX License, Section 2).
    *   For services exceeding this limit, users must contact the business team for additional commercial licenses (The CogVideoX License, Section 2).
*   **Restrictions**: The software cannot be used, copied, modified, or distributed for any military or illegal purposes. It also cannot be used for any act that may undermine China's national security, harm public interest, or infringe upon human rights (The CogVideoX License, Section 3).
*   **Distribution**: The copyright statement and license must be included in all copies or significant portions of the software (The CogVideoX License, Section 2).
*   **Disclaimer**: The software is provided "AS IS" without any warranty, and the authors or copyright holders are not liable for any claims or damages (The CogVideoX License, Section 4).

### Contact:
For questions related to the license and copyright, contact: license@zhipuai.cn (The CogVideoX License).
For academic inquiries, the corresponding author's email is: jietang@tsinghua.edu.cn (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of CogVideoX is large-scale, text-to-video generation. It is designed to generate coherent, long-duration videos with rich motion and semantics that are well-aligned with textual prompts (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1, 3).

**Capabilities:**
*   **Video Generation**: Can generate up to 10-second continuous videos at a frame rate of 16 fps (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1).
*   **High Resolution**: Supports resolutions up to 768 × 1360 pixels and can handle multiple aspect ratios (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 1, 3).
*   **Input-Output**: The model takes a text prompt as input and outputs a video. An image-to-video version is also available, which takes an image and a text prompt as input (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 3, 17).

### Primary intended users:
The model is intended for two primary groups of users, as outlined by its license:
*   **Academic Researchers**: Users can freely use the model for academic research purposes (The CogVideoX License, Section 2).
*   **Commercial Users**: Developers and businesses can use the model for commercial activities after registering for a license (The CogVideoX License, Section 2).

### Out-of-scope uses:
The license explicitly prohibits the following uses:
*   Any military purposes (The CogVideoX License, Section 3).
*   Any illegal purposes (The CogVideoX License, Section 3).
*   Any activities that may undermine China's national security and national unity, harm the public interest of society, or infringe upon the rights and interests of human beings (The CogVideoX License, Section 3).

---

## How to Use
This section outlines how to use the model.

Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development and training process identified several factors relevant to the model's performance:
*   **Data Quality**: The quality of the training data is a key factor. The developers implemented a filtering pipeline to remove videos with detrimental characteristics such as:
    *   Noticeable artificial editing or special effects.
    *   Lack of coherent motion (e.g., artificially spliced videos).
    *   Low visual quality (e.g., unclear visuals, excessive camera shake).
    *   "Lecture Type" videos with minimal motion.
    *   Videos dominated by large amounts of text.
    *   Noisy screen captures (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).
*   **Video Resolution and Duration**: The model's performance is affected by the resolution and duration of the video. These factors were addressed during training using progressive training and multi-resolution frame packing (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 6).
*   **Prompt Detail**: The level of detail in the text prompt can influence the output. The developers recommend upsampling user prompts to be more detailed and precise to match the distribution of the training data captions (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 23, Appendix F).

### Evaluation factors:
The model was evaluated on the following factors:
*   **Automated Metrics**:
    *   **Vbench Metrics**: Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
    *   **Dynamism Metrics**: Dynamic Quality and GPT4o-MTScore, which measure the dynamic content and metamorphic amplitude of videos (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10).
*   **Human Evaluation**:
    *   **Sensory Quality**: Perceptual quality, subject consistency, frame continuity, and stability (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 28).
    *   **Instruction Following**: Alignment with the prompt, including accuracy of subject, quantity, and details (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 28).
    *   **Physics Simulation**: Adherence to physical laws, such as lighting, object interactions, and fluid dynamics (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 28).
    *   **Cover Quality**: Aesthetic quality, clarity, and fidelity of single frames (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 29).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a combination of automated metrics and human evaluation:
*   **Vbench**: A suite of metrics consistent with human perception, including Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   **Dynamic Quality**: An integrated metric that combines video quality with dynamic scores to evaluate the richness of content (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10).
*   **GPT4o-MTScore**: A metric that uses GPT-4o to measure the "metamorphic amplitude" of videos, particularly for time-lapse-style changes (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10).
*   **Fréchet Video Distance (FVD)**: Used in ablation studies to measure video quality (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   **CLIP4Clip Score**: Used in ablation studies to measure text-video alignment (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   **Peak Signal-to-Noise Ratio (PSNR)**: Used to evaluate the reconstruction quality of the 3D VAE (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 4, 9).
*   **Flickering**: Measured as the L1 difference between adjacent frames to evaluate the temporal consistency of the VAE reconstruction (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 4, 9).

### Decision thresholds:
Insufficient information

### Variation approaches:
Performance was evaluated on standard benchmarks and custom test sets:
*   The 3D VAE was evaluated on the validation set of the WebVid dataset (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   Ablation studies were conducted on a 500-video test set from WebVid (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   Human evaluation was conducted by a panel of evaluators scoring generated videos based on 100 meticulously crafted prompts across four aspects (Sensory Quality, Instruction Following, Physics Simulation, Cover Quality) (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 28).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **WebVid**: The validation set of WebVid was used for evaluating the 3D VAE's reconstruction effect and for ablation studies of the main transformer model (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   **Vbench**: The Vbench benchmark was used for automated metric evaluation of text-to-video generation performance (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   **Custom Prompts**: A set of 100 "meticulously crafted prompts" with broad distribution and clear conceptual scope was used for the human evaluation framework (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 28).

### Motivation:
*   The Vbench metrics were chosen because they "are consistent with human perception" (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).
*   The human evaluation framework was established to "assess the general capabilities of video generation models" and to complement automated evaluations by emphasizing instruction-following capabilities (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, 28).

### Preprocessing:
Insufficient information

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data consists of a large collection of video-text and image-text pairs:
*   **Videos**: Approximately 35 million single-shot video clips, with an average duration of 6 seconds each. This dataset was constructed from a collection of web videos that underwent a filtering process (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).
*   **Images**: 2 billion images from the LAION-5B and COYO-700M datasets were used to assist in training (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).

### Motivation:
The goal was to construct a collection of "relatively high-quality video clips with text descriptions" to train a model capable of capturing the dynamic nature of the world (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7). Mixing images and videos during training helps the model learn semantic and low-frequency knowledge efficiently (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 6).

### Preprocessing:
The training data underwent an extensive preprocessing pipeline:
*   **Video Filtering**: Raw video data was filtered to remove low-quality or detrimental content. A set of negative labels was developed, including "Editing," "Lack of Motion Connectivity," "Low Quality," "Lecture Type," "Text Dominated," and "Noisy Screenshots." Classifiers based on Video-LLaMA were trained to screen out data based on these labels. Additionally, optical flow and image aesthetic scores were calculated for all videos, and their acceptance thresholds were dynamically adjusted during training (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).
*   **Video Captioning**: Since most video data lacks descriptive text, a "Dense Video Caption Data Generation" pipeline was established. This process involved:
    1.  Generating short captions for videos using an existing video caption model.
    2.  Extracting frames and using the CogVLM image recaptioning model to create dense image captions.
    3.  Using GPT-4 to summarize the dense image captions into a final, comprehensive video caption.
    4.  To scale this process, a LLaMA2 model was fine-tuned on the GPT-4 summary data, and eventually, an end-to-end video understanding model, CogVLM2-Caption, was developed to accelerate caption generation (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was benchmarked against other text-to-video models.
*   **Automated Evaluation**: In a comparison with seven other models, CogVideoX-5B achieved the best performance in five out of seven automated metrics: Human Action (96.8), Scene (55.44), Multiple Objects (70.95), Dynamic Quality (69.5), and GPT4o-MTScore (3.36) (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, Table 3).
*   **Human Evaluation**: In a direct comparison with the Kling model, CogVideoX-5B was preferred by human evaluators across all four evaluated aspects: Sensory Quality (0.722 vs. 0.638), Instruction Following (0.495 vs. 0.367), Physics Simulation (0.667 vs. 0.561), and Cover Quality (0.712 vs. 0.668) (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 10, Table 4).
*   **VAE Reconstruction**: The model's 3D VAE achieved a PSNR of 29.1 and a Flickering score of 85.5, outperforming other open-source VAEs in reconstruction quality and temporal stability (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9, Table 2).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The memory required to load the model for inference on an H800 GPU is as follows (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 16, Table 7):
*   **CogVideoX-5B**: 26 GB for 480x720 resolution; 76 GB for 768x1360 resolution.
*   **CogVideoX-2B**: 18 GB for 480x720 resolution; 53 GB for 768x1360 resolution.

### Deploying Requirements:
The memory and hardware requirements for running inference are the same as for loading. The model was evaluated on an H800 GPU with 50 inference steps (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 16, Table 7).

### Training or Fine-tuning Requirements:
Insufficient information. The paper notes that training on long-duration videos requires "excessive GPU memory usage" and that context parallelism was used to "distribute computation among multiple devices," but specific hardware configurations or memory requirements for training are not provided (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The training data includes large, web-crawled datasets (LAION-5B, COYO-700M, and a custom web video collection), which may contain personal information, copyrighted material, and societal biases (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7). The data filtering process focused on visual and motion quality, not explicitly on removing harmful or biased content (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 7).

Potential risks associated with the model's use include the generation of harmful, biased, illegal, or otherwise malicious content. To mitigate these risks, the model is governed by a license that places explicit restrictions on its application.

**Risk Mitigation Strategies:**
*   **Usage Restrictions**: The license strictly prohibits using the model for any military or illegal purposes. It also forbids use cases that could "undermine China's national security and national unity, harm the public interest of society, or infringe upon the rights and interests of human beings" (The CogVideoX License, Section 3). These restrictions serve as the primary risk mitigation strategy.
*   **Commercial Licensing**: A registration process is required for commercial use, which may provide a mechanism for accountability (The CogVideoX License, Section 2).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Semantic Degradation**: The final fine-tuning stage on high-quality data, while improving visual quality and removing artifacts like watermarks, was observed to cause a "slight degradation in the model's semantic ability" (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 15, Appendix A).
*   **VAE Compression Limits**: The developers noted that while their 3D VAE is effective, exploring even larger compression ratios is future work. They found that being too aggressive with spatial-temporal compression (e.g., 16x16x8) made model convergence "extremely difficult" (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 4).
*   **Architectural Instability**: During ablation studies, a 2D+1D attention mechanism (as an alternative to 3D full attention) was found to be "unstable and prone to collapse" during training for large models, highlighting its unsuitability for this scale of video generation (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 9).

### Recommendations:
*   **Prompt Engineering**: To achieve the best results, users should provide detailed and descriptive text prompts. The developers recommend using a large language model to "upsample" shorter user inputs to better match the detailed captions the model was trained on (CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer, p. 23, Appendix F).
*   **License Compliance**: All users must adhere to the terms of the CogVideoX License. This includes registering for commercial use and including the copyright and license statement in any distributions of the software (The CogVideoX License, Section 2).
*   **Acknowledge Limitations**: Users should be aware of the model's limitations, such as potential for minor semantic drift and the challenges associated with generating highly complex, long-form narratives purely from a text prompt.