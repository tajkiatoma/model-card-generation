## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University and Zhipu AI (2408.06072.pdf, p. 1). The core contributors are listed as Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, and Xiaotao Gu (2408.06072.pdf, p. 1).

### Model date:
The associated academic paper was submitted to arXiv on August 12, 2024, with the latest version (v3) dated March 26, 2025. The paper is published as a conference paper at ICLR 2025 (2408.06072.pdf, p. 1).

### Model version:
The developers have released two versions of the model based on size: CogVideoX-2B (2 billion parameters) and CogVideoX-5B (5 billion parameters) (2408.06072.pdf, p. 2). Both text-to-video and image-to-video versions are available (2408.06072.pdf, p. 3). The paper states that as the model size, data volume, and training volume increase, performance improves, indicating that CogVideoX-5B is the more capable version (2408.06072.pdf, p. 2).

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer (DiT) architecture (2408.06072.pdf, p. 1).

**Core Components** (model_index.json.txt):
*   **Transformer:** A `CogVideoXTransformer3DModel` serves as the backbone of the diffusion model. It uses 3D full attention to model video across both temporal and spatial dimensions (2408.06072.pdf, p. 2, 5).
*   **Variational Autoencoder (VAE):** A 3D causal VAE (`AutoencoderKLCogVideoX`) is used to compress videos into a latent space, reducing computational load and helping to prevent flickering (2408.06072.pdf, p. 2, 3).
*   **Text Encoder:** A `T5EncoderModel` is used to encode text prompts (model_index.json.txt).
*   **Tokenizer:** A `T5Tokenizer` is used for processing input text (model_index.json.txt).

**Model Size and Parameters:**
*   **CogVideoX-2B:** 30 layers, 32 attention heads, and a hidden size of 1920 (2408.06072.pdf, Table 6, p. 16).
*   **CogVideoX-5B:** 42 layers, 48 attention heads, and a hidden size of 3072 (2408.06072.pdf, Table 6, p. 16).
*   The total size of the text encoder weights is 9.52 GB (text_encoder/model.safetensors.index.json.txt).
*   The total size of the transformer weights is 11.14 GB (transformer/diffusion_pytorch_model.safetensors.index.json.txt).

**Context Length:**
*   The tokenizer supports a maximum length of 226 tokens (`tokenizer/tokenizer_config.json.txt`).
*   The transformer model supports a maximum sequence length of 82,000 tokens (2408.06072.pdf, Table 6, p. 16).

### Training details:
The model is trained using a diffusion process with a v-prediction objective and a zero Signal-to-Noise Ratio (SNR) noise schedule (2408.06072.pdf, p. 6). Key methodologies include:

*   **Expert Adaptive LayerNorm:** To better fuse text and video information, the model uses an "expert" adaptive LayerNorm. This applies modulation from the diffusion timestep independently to the vision and text hidden states, helping to align their feature spaces (2408.06072.pdf, p. 5).
*   **Progressive Training:** The model is first trained on low-resolution (256px) videos to learn semantics and then progressively trained on higher resolutions (up to 768px) to learn high-frequency details (2408.06072.pdf, p. 6).
*   **Multi-Resolution Frame Packing:** To handle videos of varying lengths and resolutions efficiently, the model uses a "frame packing" technique. This allows videos of different durations and resolutions to be placed into the same batch, ensuring consistent data shapes for training (2408.06072.pdf, p. 6).
*   **Explicit Uniform Sampling:** To stabilize the training loss, the diffusion timestep range (1 to T) is divided into intervals, and each parallel training rank samples a timestep from its assigned interval. This ensures a more uniform distribution of timesteps across batches (2408.06072.pdf, p. 7).

Key hyperparameters include a cosine learning rate decay, a gradient clipping of 1.0, and BF16 training precision (2408.06072.pdf, Table 6, p. 16).

### Paper or other resource for more information:
*   **Academic Paper:** The primary resource is the paper "COGVIDEOX: TEXT-TO-VIDEO DIFFUSION MODELS WITH AN EXPERT TRANSFORMER" (2408.06072.pdf). It provides a comprehensive overview of the model's architecture, training process, and evaluation.
*   **Demo Website:** Additional video examples can be found on the project's demo website: [https://yzy-thu.github.io/CogVideoX-demo/](https://yzy-thu.github.io/CogVideoX-demo/) (2408.06072.pdf, p. 1).
*   **Code Repository:** The code and model checkpoints are published at [https://github.com/THUDM/CogVideo](https://github.com/THUDM/CogVideo) (2408.06072.pdf, p. 2).

### Citation details:
The following BibTeX entry can be used to cite the model's paper:
```bibtex
@misc{yang2025cogvideox,
      title={CogVideoX: Text-to-Video Diffusion Models with an Expert Transformer}, 
      author={Zhuoyi Yang and Jiayan Teng and Jiazheng Xu and Da Yin and Yuanming Yang and Yuxuan Zhang and Xiaotao Gu and Wendi Zheng and Ming Ding and Wenyi Hong and Xiaohan Zhang and Weihan Wang and Yuxiao Dong and Yean Cheng and Jie Tang and Shiyu Huang and Guanyu Feng and Bin Xu},
      year={2025},
      eprint={2408.06072},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      note={Published as a conference paper at ICLR 2025}
}
```
(2408.06072.pdf, p. 1)

### License:
The model is released under the "CogVideoX License" (`LICENSE.txt`).
*   **Academic Use:** The license allows free use of all open-source models for academic research.
*   **Commercial Use:** Commercial use requires registration to obtain a basic commercial license. Use is free for commercial activities with service user visits not exceeding 1 million per month. For usage exceeding this limit, a separate commercial license must be obtained by contacting the business team.
*   **Restrictions:** Users are prohibited from using the software for any military or illegal purposes. It cannot be used for any act that may undermine China's national security, harm public interest, or infringe upon human rights.
*   **Disclaimer:** The software is provided "AS IS" without any warranty (`LICENSE.txt`).

### Contact:
For questions related to the license and copyright, contact `license@zhipuai.cn` (`LICENSE.txt`). For academic inquiries, the corresponding author is Jie Tang, who can be reached at `jietang@tsinghua.edu.cn` (2408.06072.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
CogVideoX is a large-scale model designed for generating high-quality, long-duration, and coherent videos from text prompts (text-to-video) or a combination of an image and a text prompt (image-to-video) (2408.06072.pdf, p. 1, 3).

**Capabilities:**
*   **Video Generation:** It can generate 10-second continuous videos at a frame rate of 16 fps (2408.06072.pdf, p. 1).
*   **High Resolution:** It supports generating videos with multiple aspect ratios, up to a resolution of 768x1360 pixels (2408.06072.pdf, p. 3).
*   **Dynamic Motion:** The model is specifically designed to generate videos with coherent narratives, diverse shapes, and dynamic movements (2408.06072.pdf, p. 1).

**Input-Output Structure:**
*   **Text-to-Video:** The input is a text prompt describing the desired video content. The output is a video file (2408.06072.pdf, p. 3).
*   **Image-to-Video:** The input is an image and a text prompt. The model generates a video that starts with the provided image and evolves according to the prompt (2408.06072.pdf, p. 17).

### Primary intended users:
The model is intended for a broad audience, including:
*   **Academic Researchers:** For studying and advancing the field of video generation (LICENSE.txt).
*   **Developers and Commercial Users:** For building applications that leverage text-to-video technology, subject to the terms of the commercial license (LICENSE.txt).

### Out-of-scope uses:
The license explicitly prohibits the use of the model for the following purposes:
*   Any military applications (`LICENSE.txt`).
*   Any illegal purposes (`LICENSE.txt`).
*   Activities that may harm China's national security and unity, damage social public interest, or infringe upon the rights and interests of human beings (`LICENSE.txt`).

---

## How to Use
This section outlines how to use the model.

Insufficient information. The provided repository does not include code snippets or a direct guide on how to run the model. However, the paper describes the model's functionality and provides numerous examples of generated videos from text prompts.

**Input-Output Structure:**
The model takes a text prompt as input and generates a video as output. For the image-to-video version, it takes an image and a text prompt (2408.06072.pdf, p. 3, 17).

**Example Outputs:**
*   **Text Prompt:** "A lightning bolt shatters a mountaintop stone—out leaps the Monkey King in battle robes. Energy erupts, winds howl."
    *   **Output:** A video depicting the described scene (2408.06072.pdf, p. 1).
*   **Text Prompt:** "A golden retriever with black sunglasses and long hair, with a rainy rooftop in the background, runs towards the camera from far to near"
    *   **Output:** A video of a golden retriever running towards the camera (2408.06072.pdf, p. 19).
*   **Text Prompt:** "Three dolphins leap out of the ocean at sunset, then splash into the water"
    *   **Output:** A video of dolphins leaping at sunset (2408.06072.pdf, p. 19).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper focuses on technical and data-related factors that influence performance. It does not discuss demographic or environmental factors. Relevant factors identified include:
*   **Video Quality:** The model's performance is sensitive to the quality of training data. The developers implemented a filtering system to remove videos with low quality, excessive camera shake, or noticeable artificial editing (2408.06072.pdf, p. 7).
*   **Motion and Dynamics:** The model is designed to capture dynamic motion. The training data was filtered to remove videos with minimal dynamic information (e.g., lectures) or a lack of motion connectivity (e.g., spliced videos) (2408.06072.pdf, p. 7).
*   **Text-Video Alignment:** The quality and detail of text descriptions are crucial. The developers created a custom captioning pipeline to generate dense, descriptive text for the training videos, which significantly improves the model's ability to understand semantics (2408.06072.pdf, p. 1, 8).

### Evaluation factors:
The model is evaluated on factors that assess its ability to generate high-quality, coherent, and prompt-aligned videos. These include:
*   **Automated Evaluation:** Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (2408.06072.pdf, p. 9).
*   **Human Evaluation:** Sensory Quality (visuals, consistency), Instruction Following (alignment with prompt), Physics Simulation (realism of motion and lighting), and Cover Quality (aesthetic quality of frames) (2408.06072.pdf, p. 10, 28-29).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a combination of automated metrics and human evaluation.
*   **Automated Metrics:**
    *   **Vbench Metrics:** The primary evaluation uses several metrics from the Vbench suite that are consistent with human perception: Human Action, Scene, Dynamic Degree, Multiple Objects, and Appearance Style (2408.06072.pdf, p. 9).
    *   **Dynamic Quality Metrics:** To specifically measure the dynamism of generated videos, the model is evaluated using Dynamic Quality and GPT4O-MTScore, which are designed to reward rich motion and mitigate biases against dynamic content (2408.06072.pdf, p. 10).
    *   **Ablation Study Metrics:** During development, Fréchet Video Distance (FVD) and CLIP4Clip Score were used to compare different architectural choices (2408.06072.pdf, p. 9).
*   **Human Evaluation:** A comprehensive framework where human evaluators score generated videos on a scale from 0 to 1 across four categories: Sensory Quality, Instruction Following, Physics Simulation, and Cover Quality (2408.06072.pdf, p. 10, 28).

### Decision thresholds:
During data preprocessing, thresholds for optical flow scores and image aesthetic scores were dynamically adjusted to ensure the quality of the training data (2408.06072.pdf, p. 7). The model card does not specify any decision thresholds for the model's output during inference.

### Variation approaches:
*   For VAE reconstruction evaluation, performance was measured on the validation set of the WebVid dataset (2408.06072.pdf, p. 9).
*   For ablation studies, performance was measured on a test set of 500 videos from the WebVid dataset (2408.06072.pdf, p. 9).
*   For human evaluation, a panel of evaluators scored videos generated from 100 meticulously crafted prompts designed to cover a broad distribution of concepts (2408.06072.pdf, p. 28).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **WebVid Dataset:** The validation set of WebVid was used for evaluating the VAE's reconstruction quality. A subset of 500 videos from the WebVid test set was used for ablation studies (2408.06072.pdf, p. 9).
*   **Custom Prompt Set:** For human evaluation, a set of 100 custom-crafted prompts was used. These prompts are described as having "broad distribution, clear articulation, and well-defined conceptual scope" (2408.06072.pdf, p. 28).

### Motivation:
The WebVid dataset is a standard benchmark for text-to-video models. The custom prompt set for human evaluation was created to thoroughly assess the model's capabilities in instruction following and generation quality across a wide range of scenarios (2408.06072.pdf, p. 28).

### Preprocessing:
Insufficient information. The paper does not describe any specific preprocessing steps applied to the evaluation datasets.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is a large-scale collection of video-text and image-text pairs.
*   **Video Data:** A collection of approximately 35 million single-shot video clips, with an average duration of 6 seconds each (2408.06072.pdf, p. 7).
*   **Image Data:** 2 billion images filtered for aesthetic quality from the LAION-5B and COYO-700M datasets (2408.06072.pdf, p. 7).

### Motivation:
The large and diverse dataset was constructed to train a powerful, general-purpose text-to-video model. The inclusion of image data allows for joint training, which can improve the model's understanding of visual concepts (2408.06072.pdf, p. 6). High-quality, descriptive captions were generated for the video data to enhance the model's ability to align video content with text semantics (2408.06072.pdf, p. 8).

### Preprocessing:
The training data underwent an extensive and innovative preprocessing pipeline.
*   **Video Filtering:** Raw video data was filtered to remove low-quality content. A set of classifiers were trained to identify and discard videos based on negative labels such as "Editing" (artificial effects), "Lack of Motion Connectivity," "Low Quality" (blurry, shaky), "Lecture Type," "Text Dominated," and "Noisy Screenshots" (2408.06072.pdf, p. 7).
*   **Video Captioning:** A "Dense Video Caption Data Generation" pipeline was created to produce high-quality text descriptions for the video clips. This process involved:
    1.  Generating short captions for videos.
    2.  Extracting frames and using an image captioning model (CogVLM) to create dense descriptions for each frame.
    3.  Using GPT-4 to summarize the dense frame captions into a final, comprehensive video caption.
    4.  Fine-tuning a LLaMA2 model on these summaries to scale up the captioning process (2408.06072.pdf, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results for the CogVideoX-5B and CogVideoX-2B models across several automated metrics and compares them against other state-of-the-art models.

**Automated Evaluation Results (Table 3):**
CogVideoX-5B achieved the highest scores in five of the seven metrics, including Scene (55.44), Dynamic Degree (62.22), Multiple Objects (70.95), Dynamic Quality (69.5), and GPT4O-MTScore (3.36) (2408.06072.pdf, p. 10).

**Human Evaluation Results (Table 4):**
In a head-to-head comparison with the Kling model, CogVideoX-5B was preferred by human evaluators across all four assessed categories:
*   **Sensory Quality:** 0.722
*   **Instruction Following:** 0.495
*   **Physics Simulation:** 0.667
*   **Cover Quality:** 0.712
*   **Total Score:** 2.74 (2408.06072.pdf, p. 10).

### Intersectional results:
Insufficient information. The paper does not provide intersectional performance results (e.g., performance across combinations of different factors).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The memory required to load and run the model for inference depends on the model version and the desired output resolution. The evaluation was performed on an H800 GPU with 50 inference steps (2408.06072.pdf, Table 7, p. 16).
*   **CogVideoX-2B (480x720, 6s video):** 18 GB
*   **CogVideoX-2B (768x1360, 5s video):** 53 GB
*   **CogVideoX-5B (480x720, 6s video):** 26 GB
*   **CogVideoX-5B (768x1360, 5s video):** 76 GB

### Deploying Requirements:
See "Loading Requirements" above. These figures represent the requirements for running inference.

### Training or Fine-tuning Requirements:
The paper specifies that training was conducted using BF16 precision (2408.06072.pdf, Table 6, p. 16). However, it does not provide details on the specific hardware configuration (e.g., number of GPUs, type of interconnect) used for training the model.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper does not include a dedicated section on ethical considerations. The information below is derived from the license and the description of the training data.

*   **Sensitive Data:** The model was trained on large-scale, web-crawled datasets (LAION-5B, COYO-700M) and a collection of video clips (2408.06072.pdf, p. 7). Such datasets may contain personal information, copyrighted material, or reflect societal biases. The paper describes a data filtering process, but it focuses on visual quality and motion dynamics rather than filtering for sensitive or harmful content (2408.06072.pdf, p. 7).
*   **Risks and Mitigation:** The primary risk mitigation strategy is outlined in the license, which explicitly prohibits the use of the model for malicious or harmful purposes.
    *   **Prohibited Uses:** The license forbids using the model for military applications, illegal activities, or any purpose that could harm national security, public interest, or human rights (`LICENSE.txt`).
    *   **Potential for Misuse:** As a generative model, CogVideoX could potentially be used to create misinformation, deepfakes, or other harmful content. The license restrictions are the main safeguard provided against such misuse. Users are responsible for the content they generate.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Semantic Degradation from Fine-tuning:** The paper notes that while fine-tuning on a high-quality subset of data improved visual quality (e.g., removing watermarks), it also caused a "slight degradation in the model's semantic ability" (2408.06072.pdf, p. 15).
*   **Architectural Instability:** The developers found that an alternative architecture using separated 2D (spatial) and 1D (temporal) attention was "unstable and prone to collapse" during large-scale training, highlighting the sensitivity of such models to design choices (2408.06072.pdf, p. 9).
*   **VAE Compression Limits:** The paper suggests that "exploring VAE with larger compression ratios is our future work," indicating that the current VAE design may have limitations that could be improved upon (2408.06072.pdf, p. 4).

### Recommendations:
*   **Prompt Engineering:** The model was trained on highly detailed and descriptive captions. To achieve the best results during inference, it is recommended to use a large language model to "upsample" short user prompts into more detailed descriptions that better match the training data distribution (2408.06072.pdf, p. 23).
*   **Positional Encoding for High Resolution:** When generating videos at resolutions different from the training data, the paper recommends using extrapolation for the 3D RoPE positional encoding. This method was found to better retain local details compared to interpolation, which tends to generate blurry images at higher resolutions (2408.06072.pdf, p. 6, 15).