## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from Tsinghua University and Zhipu AI (Source: `2408.06072.pdf`, Page 1). The development team is also referred to as the CogVideoX Model Team (Source: `LICENSE`, Section 1).

### Model date:
The associated academic paper was submitted to arXiv with a revision date of March 26, 2025 (Source: `2408.06072.pdf`, Page 1).

### Model version:
The model version is CogVideoX-5B (Source: `README.md`, Title). It is a larger, higher-quality version compared to the 2B introductory model. The key differences are:
*   **Size and Quality**: The 5B model has 5 billion parameters and is designed for higher video generation quality and better visual effects compared to the 2B model (Source: `README.md`, 模型介绍 table).
*   **Recommended Precision**: The 5B model is trained with BF16 precision, which is the recommended setting for inference, while the 2B model is trained with FP16 (Source: `README.md`, 模型介绍 table).
*   **Memory Consumption**: The 5B model requires more GPU memory for inference (starting from 5GB for BF16) and fine-tuning (starting from 63GB for LORA) compared to the 2B model (Source: `README.md`, 模型介绍 table).
*   **Positional Encoding**: The 5B model uses `3d_rope_pos_embed` while the 2B model uses `3d_sincos_pos_embed` (Source: `README.md`, 模型介绍 table).

### Model type:
CogVideoX is a large-scale, text-to-video generation model based on a diffusion transformer architecture (Source: `2408.06072.pdf`, Abstract). Its core components include:
*   **Text Encoder**: A `T5EncoderModel` to process input text prompts (Source: `config.json`).
*   **Tokenizer**: A `T5Tokenizer` for text tokenization (Source: `config.json`).
*   **Transformer**: A `CogVideoXTransformer3DModel` which acts as the main diffusion model backbone, utilizing an "expert transformer" design with expert adaptive LayerNorm to facilitate fusion between text and video modalities (Source: `config.json`; `2408.06072.pdf`, Section 2). It uses 3D full attention to model spatial and temporal dimensions simultaneously (Source: `2408.06072.pdf`, Section 2.2).
*   **Variational Autoencoder (VAE)**: An `AutoencoderKLCogVideoX` which is a 3D causal VAE designed to compress videos across both spatial and temporal dimensions (Source: `config.json`; `2408.06072.pdf`, Section 2.1).

**Model Size and Capabilities**:
*   **Parameters**: 5 billion (Source: `README.md`, 模型介绍 table).
*   **Supported Prompt Length**: Up to 226 tokens (Source: `README.md`, 模型介绍 table).
*   **Video Output**: The open-source model generates videos of up to 6 seconds in length, at a resolution of 720x480 and a frame rate of 8 fps (Source: `README.md`, 模型介绍 table).

### Training details:
The model was trained using a multi-stage, progressive training pipeline.
*   **Algorithm**: The model is a diffusion model that adopts v-prediction and a zero Signal-to-Noise Ratio (SNR) noise schedule (Source: `2408.06072.pdf`, Section 3).
*   **Architecture & Parameters**: The 5B model has 42 layers, 48 attention heads, and a hidden size of 3072. It uses Rotary Position Embedding (RoPE) (Source: `2408.06072.pdf`, Table 6).
*   **Training Precision**: The model was trained using BF16 precision (Source: `README.md`, 模型介绍 table).
*   **Methodologies**:
    *   **Progressive Training**: The model was first trained on low-resolution videos (256px) to learn semantics and then progressively trained on higher resolutions (up to 768px) to learn high-frequency details (Source: `2408.06072.pdf`, Section 3.2).
    *   **Multi-Resolution Frame Packing**: To handle videos of varying lengths and resolutions efficiently, videos of different durations were packed into the same batch, inspired by Patch'n Pack (Source: `2408.06072.pdf`, Section 3.1).
    *   **Explicit Uniform Sampling**: To stabilize the training loss, the diffusion timestep range was divided into intervals, with each parallel rank sampling uniformly from its assigned interval (Source: `2408.06072.pdf`, Section 3.3).
    *   **High-Quality Fine-Tuning**: In the final stage, the model was fine-tuned on a subset of higher-quality video data (20% of the total dataset) to remove artifacts like subtitles and watermarks (Source: `2408.06072.pdf`, Appendix A).

### Paper or other resource for more information:
*   **Academic Paper**: "CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer". This paper provides a detailed overview of the model's architecture, training process, and evaluation. Link: https://arxiv.org/pdf/2408.06072 (Source: `README.md`).
*   **GitHub Repository**: The official code repository, which includes technical details, prompt optimization guides, and tools. Link: https://github.com/THUDM/CogVideo (Source: `README.md`).
*   **Hugging Face Space**: A web demo for users to interact with the model. Link: https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space (Source: `README.md`).

### Citation details:
To cite the model, use the following BibTeX format (Source: `README.md`):
```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```

### License:
The model is released under the CogVideoX License (Source: `LICENSE`).
*   **Academic Use**: The license grants a non-exclusive, worldwide, royalty-free copyright license for academic research (Source: `LICENSE`, Section 2).
*   **Commercial Use**: Commercial use is permitted for free after registering and obtaining a basic commercial license. However, this is limited to services with fewer than 1 million visits per month. For higher traffic, a separate commercial license must be obtained (Source: `LICENSE`, Section 2).
*   **Restrictions**: Users are prohibited from using the software for any military or illegal purposes. It cannot be used for any act that may undermine China's national security, harm public interest, or infringe upon human rights (Source: `LICENSE`, Section 3).
*   **Disclaimer**: The software is provided "AS IS" without any warranty, and the authors or copyright holders are not liable for any claims or damages (Source: `LICENSE`, Section 4).

### Contact:
For questions related to the license and copyright, contact `license@zhipuai.cn` (Source: `LICENSE`).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of CogVideoX-5B is text-to-video synthesis (Source: `framework` and `task` metadata). It is designed to generate coherent, long-duration videos with rich semantics and dynamic motion from textual descriptions (Source: `2408.06072.pdf`, Abstract).

The model takes a text prompt as input and generates a video file as output. The open-source version can generate 6-second videos at 720x480 resolution (Source: `README.md`, 模型介绍 table). Examples of use cases include creating short video clips for artistic expression, storytelling, or content creation based on descriptive text (Source: `README.md`, 作品案例 section).

### Primary intended users:
The model is intended for:
1.  **Researchers** in the field of AI and video generation, who can use the model for academic purposes (Source: `LICENSE`, Section 2).
2.  **Developers and Businesses** who can integrate the model into commercial applications after obtaining the appropriate license (Source: `LICENSE`, Section 2).

### Out-of-scope uses:
The license explicitly prohibits the following uses:
*   Any military purposes (Source: `LICENSE`, Section 3).
*   Any illegal purposes (Source: `LICENSE`, Section 3).
*   Any activities that may undermine China's national security and unity, harm the public interest, or infringe upon the rights and interests of human beings (Source: `LICENSE`, Section 3).

---

## How to Use
This section outlines how to use the model.

The model can be used with the `diffusers` library in Python.

**1. Installation**
First, install the required dependencies:
```shell
pip install --upgrade transformers accelerate diffusers imageio-ffmpeg
```
(Source: `README.md`, 快速上手 section)

**2. Standard Inference (BF16/FP16)**
The following code snippet demonstrates how to generate a video from a text prompt using BF16 precision. To reduce memory usage, several optimizations like CPU offloading and VAE tiling are enabled.

```python
import torch
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video

prompt = "A panda, dressed in a small, red jacket and a tiny hat, sits on a wooden stool in a serene bamboo forest. The panda's fluffy paws strum a miniature acoustic guitar, producing soft, melodic tunes. Nearby, a few other pandas gather, watching curiously and some clapping in rhythm. Sunlight filters through the tall bamboo, casting a gentle glow on the scene. The panda's face is expressive, showing concentration and joy as it plays. The background includes a small, flowing stream and vibrant green foliage, enhancing the peaceful and magical atmosphere of this unique musical performance."

pipe = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-5b",
    torch_dtype=torch.bfloat16
)

# Optimizations to reduce memory consumption
pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()

video = pipe(
    prompt=prompt,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=49, # Corresponds to 6 seconds at ~8 fps
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```
(Source: `README.md`, 快速上手 section)

**3. Quantized Inference (INT8)**
For environments with very low VRAM (e.g., T4 GPUs), the model's components can be quantized to INT8. This significantly reduces memory requirements but also increases inference time.

```python
import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXTransformer3DModel, CogVideoXPipeline
from diffusers.utils import export_to_video
from transformers import T5EncoderModel
from torchao.quantization import quantize_, int8_weight_only

# Define the quantization method
quantization = int8_weight_only

# Load and quantize each model component
text_encoder = T5EncoderModel.from_pretrained("THUDM/CogVideoX-5b", subfolder="text_encoder", torch_dtype=torch.bfloat16)
quantize_(text_encoder, quantization())

transformer = CogVideoXTransformer3DModel.from_pretrained("THUDM/CogVideoX-5b", subfolder="transformer", torch_dtype=torch.bfloat16)
quantize_(transformer, quantization())

vae = AutoencoderKLCogVideoX.from_pretrained("THUDM/CogVideoX-5b", subfolder="vae", torch_dtype=torch.bfloat16)
quantize_(vae, quantization())

# Create pipeline with quantized components
pipe = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-5b",
    text_encoder=text_encoder,
    transformer=transformer,
    vae=vae,
    torch_dtype=torch.bfloat16,
)
pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()

prompt = "A panda, dressed in a small, red jacket and a tiny hat, sits on a wooden stool in a serene bamboo forest..."

video = pipe(
    prompt=prompt,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=49,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```
(Source: `README.md`, Quantized Inference section)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors identified during its development and training:
*   **Prompt Quality**: The level of detail and clarity in the text prompt significantly affects the output. The training process involved a sophisticated captioning pipeline to generate detailed descriptions, and a similar upsampling process is recommended for user prompts at inference time (Source: `2408.06072.pdf`, Section 3.4 and Appendix F).
*   **Video Content Quality**: The training data was filtered to remove content with undesirable characteristics, such as artificial editing, lack of motion, poor visual quality, lecture-style videos, text-heavy videos, and noisy screen recordings. The model may perform poorly on prompts describing such content (Source: `2408.06072.pdf`, Section 3.4).
*   **Motion and Dynamics**: The model was trained to capture the "dynamic nature of the world." Its performance is sensitive to the amount and coherence of motion described in the prompt (Source: `2408.06072.pdf`, Section 3.4).

### Evaluation factors:
The model was evaluated on the following factors:
*   **Automated Evaluation**: Metrics from Vbench were used to assess `Human Action`, `Scene`, `Dynamic Degree`, `Multiple Objects`, and `Appearance Style` (Source: `2408.06072.pdf`, Section 4.2.1).
*   **Human Evaluation**: A human evaluation framework was established to score generated videos on four aspects: `Sensory Quality` (visual appeal, consistency), `Instruction Following` (alignment with prompt), `Physics Simulation` (realism of motion and interactions), and `Cover Quality` (clarity of individual frames) (Source: `2408.06072.pdf`, Section 4.2.2 and Appendix J).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to assess the model's performance:
*   **Text-to-Video Quality**: A suite of metrics from Vbench consistent with human perception was used, including `Human Action`, `Scene`, `Dynamic Degree`, `Multiple Objects`, and `Appearance Style` (Source: `2408.06072.pdf`, Section 4.2.1).
*   **Video Dynamism**: `Dynamic Quality` and `GPT4O-MTScore` were used to specifically measure the richness of motion and content changes in the generated videos (Source: `2408.06072.pdf`, Section 4.2.1).
*   **VAE Reconstruction Quality**: The 3D VAE was evaluated using `PSNR` (Peak Signal-to-Noise Ratio) to measure restoration quality and a `Flickering` metric (L1 difference between adjacent frames) to measure temporal stability (Source: `2408.06072.pdf`, Table 1 & 2).
*   **Ablation Study Metrics**: During development, `FVD` (Fréchet Video Distance) and `CLIP4Clip Score` were used to compare different architectural choices (Source: `2408.06072.pdf`, Figure 8 caption).

### Decision thresholds:
Insufficient information.

### Variation approaches:
*   **Human Evaluation**: A panel of evaluators scored generated videos on a scale from 0 to 1 across four different quality aspects. The guidelines for scoring were detailed to ensure consistency (Source: `2408.06072.pdf`, Appendix J).
*   **Automated Evaluation**: The automated metrics were calculated on standard test datasets to ensure comparability with other models (Source: `2408.06072.pdf`, Section 4.2.1).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Ablation Studies**: The WebVid validation set, containing 500 videos, was used for ablation studies comparing different model architectures and training strategies (Source: `2408.06072.pdf`, Figure 8 caption).
*   **Human Evaluation**: A set of 100 "meticulously crafted prompts" characterized by broad distribution and clear articulation was used for the human evaluation framework (Source: `2408.06072.pdf`, Appendix J).
*   **Automated Benchmarking**: The model was evaluated using the Vbench benchmark suite, though the specific underlying dataset for the reported scores is not detailed (Source: `2408.06072.pdf`, Section 4.2.1).

### Motivation:
Insufficient information is available on why these specific datasets were chosen, beyond their status as standard benchmarks in the field.

### Preprocessing:
To better align the inference-time text distribution with the training data, user prompts are preprocessed using a large language model. This "upsampling" step makes the prompts more detailed and precise before they are fed into the model (Source: `2408.06072.pdf`, Appendix F).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale, custom-curated dataset consisting of both videos and images.
*   **Video Data**: A collection of approximately 35 million single-shot video clips, with an average duration of 6 seconds each. This data was obtained after a rigorous filtering process (Source: `2408.06072.pdf`, Section 3.4).
*   **Image Data**: 2 billion images from the LAION-5B and COYO-700M datasets were used to assist in training. These images were filtered based on aesthetics scores (Source: `2408.06072.pdf`, Section 3.4).

### Motivation:
The custom dataset was created because most publicly available video data lacks comprehensive and accurate textual descriptions. Furthermore, raw web data often contains significant noise (e.g., artificial edits, poor quality) that is detrimental to training a high-quality video generation model. The goal was to create a high-quality, clean dataset with rich, descriptive captions to improve semantic alignment and generation quality (Source: `2408.06072.pdf`, Section 3.4).

### Preprocessing:
The training data underwent an extensive preprocessing pipeline:
*   **Video Filtering**: A set of six classifiers based on Video-LLaMA were trained to identify and filter out low-quality videos. The negative labels included: `Editing` (artificial effects), `Lack of Motion Connectivity`, `Low Quality` (camera shake), `Lecture Type`, `Text Dominated`, and `Noisy Screenshots`. Optical flow and image aesthetic scores were also used to ensure the dynamic and aesthetic quality of the training data (Source: `2408.06072.pdf`, Section 3.4).
*   **Video Captioning**: A "Dense Video Caption Data Generation" pipeline was established to create high-quality text descriptions. This involved:
    1.  Generating short captions for videos.
    2.  Extracting frames and using an image captioning model (CogVLM) to create dense, frame-by-frame descriptions.
    3.  Using GPT-4 (and a fine-tuned Llama 2 model for scalability) to summarize the dense image captions into a single, comprehensive video caption (Source: `2408.06072.pdf`, Section 3.4 and Figure 7).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of CogVideoX-5B was benchmarked against other text-to-video models across several individual metrics. The results are presented in Table 3 of the academic paper.
*   **Human Action**: 96.8
*   **Scene**: 55.44
*   **Dynamic Degree**: 62.22
*   **Multiple Objects**: 70.95
*   **Appearance Style**: 24.44
*   **Dynamic Quality**: 69.5
*   **GPT4O-MTScore**: 3.36
(Source: `2408.06072.pdf`, Table 3)

Human evaluation scores were also presented, broken down by category:
*   **Sensory Quality**: 0.722
*   **Instruction Following**: 0.495
*   **Physics Simulation**: 0.667
*   **Cover Quality**: 0.712
*   **Total Score**: 2.74
(Source: `2408.06072.pdf`, Table 4)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
With `diffusers` library optimizations (like CPU offload) enabled:
*   **BF16 Precision**: Requires a minimum of 5 GB of GPU VRAM.
*   **INT8 Quantized**: Requires a minimum of 4.4 GB of GPU VRAM.
(Source: `README.md`, 模型介绍 table)

### Deploying Requirements:
*   **Single GPU Inference**:
    *   **Memory**: 15 GB of VRAM is required for multi-GPU inference with BF16 precision (Source: `README.md`, 模型介绍 table).
    *   **Speed**: On a single NVIDIA A100 GPU, generating a video takes approximately 180 seconds. On an H100, it takes approximately 90 seconds (with memory optimizations enabled) (Source: `README.md`, 模型介绍 table).
*   **Hardware**: The model is tested on NVIDIA Ampere architecture GPUs (e.g., A100, H100) or newer. Using FP8 precision on H100 or newer devices requires a source installation of PyTorch and related libraries (Source: `README.md`, 数据解释 section).

### Training or Fine-tuning Requirements:
The following per-GPU VRAM is required for fine-tuning:
*   **LoRA (batch size 1)**: 63 GB
*   **LoRA (batch size 2)**: 80 GB
*   **Supervised Fine-Tuning (SFT, batch size 1)**: 75 GB
(Source: `README.md`, 模型介绍 table)

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers have put explicit restrictions in the model's license to mitigate risks and prevent misuse.
*   **Prohibited Uses**: The license strictly forbids using the model for any military or illegal purposes. It also prohibits any use that could endanger China's national security, harm public interest, or violate human rights (Source: `LICENSE`, Section 3). This indicates that the developers have considered the potential for malicious use and have established a legal framework to prevent it.
*   **Data Filtering**: The training data was filtered to remove low-quality content, which may have incidentally removed some harmful or biased content, although this was not an explicit goal of the filtering process described (Source: `2408.06072.pdf`, Section 3.4).
*   **Sensitive Data**: There is no mention of the use of sensitive or personally identifiable information in the training data. The data sources are large-scale, public web datasets (LAION-5B, COYO-700M) and a curated collection of video clips (Source: `2408.06072.pdf`, Section 3.4).

Potential risks in model usage include the generation of misinformation, deepfakes, or other harmful content, which falls under the "illegal purposes" restriction in the license. Users are responsible for the content they generate and must adhere to the license terms.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Degradation with Fine-Tuning**: The final fine-tuning stage, while improving visual quality by removing artifacts, also caused a "slight degradation in the model's semantic ability" (Source: `2408.06072.pdf`, Appendix A).
*   **Language Limitation**: The model only supports English prompts. For other languages, it is recommended to translate them to English first (Source: `README.md`, 数据解释 section).
*   **Quantization Trade-off**: Using INT8 quantization to reduce memory usage will significantly slow down inference speed (Source: `README.md`, 数据解释 section).
*   **Resolution and Length Limits**: The public open-source model is limited to generating 6-second videos at 720x480 resolution and 8 fps, which is lower than the capabilities of the full model described in the research paper (10 seconds, 16 fps, 768x1360 resolution) (Source: `README.md`, 模型介绍 table; `2408.06072.pdf`, Abstract).

### Recommendations:
*   **Use Recommended Precision**: For best results, use the model with its native training precision, which is `BF16` for the 5B version (Source: `README.md`, 数据解释 section).
*   **Optimize Prompts**: For a better experience and higher-quality video generation, users are encouraged to visit the project's GitHub repository for guides on prompt optimization and conversion (Source: `README.md`, 快速上手 section).
*   **Memory Management**: For systems with limited GPU memory, use the provided optimization functions such as `pipe.enable_model_cpu_offload()` and `pipe.vae.enable_tiling()` (Source: `README.md`, 快速上手 section). Note that `enable_model_cpu_offload()` should be disabled for multi-GPU inference (Source: `README.md`, 数据解释 section).