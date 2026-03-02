## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. The developers are affiliated with Ludwig Maximilian University of Munich, IWR, Heidelberg University, and Runway ML (paper.pdf, page 1).

### Model date:
The academic paper describing the model was submitted on December 20, 2021, with a revised version submitted on April 13, 2022 (paper.pdf, page 1).

### Model version:
The repository contains information on multiple versions. A performance graph shows versions v1.1, v1.2, and v1.3, evaluated based on FID and CLIP scores (FID vs CLIP Scores.png). The associated paper analyzes different versions based on their downsampling factor `f`, denoted as LDM-`f` (e.g., LDM-1, LDM-4, LDM-8). LDM-1 is a pixel-based Diffusion Model, while versions with `f` > 1 are Latent Diffusion Models. The analysis suggests that LDM-{4-8} provide the best balance between efficiency and quality (paper.pdf, page 5, Sec. 4.1). The text-to-image model is a 1.45B parameter KL-regularized LDM-8 (paper.pdf, page 7, Sec. 4.3.1; page 6, Fig. 5).

### Model type:
The model is a Latent Diffusion Model (LDM), a type of generative model for high-resolution image synthesis (paper.pdf, Abstract, page 1). LDMs are probabilistic models designed to learn a data distribution by reversing a fixed Markov Chain of length T (paper.pdf, page 4, Sec. 3.2).

The architecture consists of several key components:
*   **Autoencoder:** An autoencoder, based on previous work on VQGAN, is used for perceptual compression. It consists of an encoder (E) that maps an image to a lower-dimensional latent representation and a decoder (D) that reconstructs the image from the latent space. It uses a combination of perceptual and patch-based adversarial losses (paper.pdf, page 3, Sec. 3.1; vae_config.json). The scaling factor for the latent space is 0.18215 (vae_config.json, "scaling_factor").
*   **UNet:** A time-conditional UNet is used as the backbone for the diffusion process in the latent space. It is built primarily from 2D convolutional layers (paper.pdf, page 4, Sec. 3.2; unet_config.json).
*   **Conditioning Mechanism:** The model is turned into a flexible generator by introducing cross-attention layers into the UNet architecture, allowing it to be conditioned on various inputs like text or semantic maps (paper.pdf, page 1, Abstract; page 4, Sec. 3.3).
*   **Text Encoder:** For text-to-image tasks, a CLIPTextModel is used as the text encoder (pipeline_model.json, "text_encoder"). It has a model_max_length of 77 tokens (tokenizer_config.json, "model_max_length"). The tokenizer is a CLIPTokenizer (pipeline_model.json, "tokenizer").
*   **Safety Checker:** A `StableDiffusionSafetyChecker` is included to check for sensitive content (pipeline_model.json, "safety_checker"; safety_checker_config.json).

### Training details:
The model is trained in a two-stage process:
1.  **Perceptual Compression Training:** An autoencoder is trained to provide an efficient, lower-dimensional latent space that is perceptually equivalent to the image space. This stage uses a perceptual loss and a patch-based adversarial objective (paper.pdf, page 3, Sec. 3.1). Two types of regularization are explored for the latent space: KL-regularization (KL-reg) and Vector Quantization (VQ-reg) (paper.pdf, page 4, Sec. 3.1).
2.  **Latent Diffusion Model Training:** The diffusion model is trained on the latent representations from the first stage. The objective is to predict a denoised variant of a noisy input `zt` (paper.pdf, page 4, Sec. 3.2). The model uses a PNDM scheduler with a `scaled_linear` beta schedule and 1000 training timesteps (scheduler_config_1.json, "beta_schedule", "num_train_timesteps"). For conditioning, a domain-specific encoder `τθ` (e.g., a transformer) maps conditioning inputs `y` to an intermediate representation, which is then connected to the UNet via cross-attention layers (paper.pdf, page 4, Sec. 3.3).

### Paper or other resource for more information:
The primary resource is the academic paper: "High-Resolution Image Synthesis with Latent Diffusion Models" by Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. The paper provides a detailed explanation of the model architecture, training process, and experimental results (paper.pdf).

A GitHub repository is also provided for pretrained models: https://github.com/CompVis/latent-diffusion (paper.pdf, page 1, page 2).

### Citation details:
Insufficient information.

### License:
Insufficient information.

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed for high-resolution image synthesis and is a general-purpose tool for various conditional and unconditional image generation tasks. Its primary uses include:
*   **Text-to-Image Synthesis:** Generating images from textual descriptions (paper.pdf, page 1, Abstract).
*   **Class-Conditional Image Synthesis:** Creating images based on a given class label, achieving state-of-the-art scores on datasets like ImageNet (paper.pdf, page 1, Abstract).
*   **Image Inpainting:** Filling in masked or missing regions of an image (paper.pdf, page 1, Abstract).
*   **Super-Resolution:** Upscaling low-resolution images to higher resolutions (paper.pdf, page 1, Abstract).
*   **Unconditional Image Generation:** Creating images without any specific input condition (paper.pdf, page 1, Abstract).
*   **Layout-to-Image Synthesis:** Generating images from semantic layouts or bounding boxes (paper.pdf, page 1, Abstract; page 7, Sec. 4.3.1).

The model can be applied in a convolutional manner to render large, consistent images of up to 1024x1024 pixels for densely conditioned tasks (paper.pdf, page 2, Sec. 1).

### Primary intended users:
The primary intended users are researchers and developers in the fields of computer vision and machine learning. The release of pretrained models is intended to enable exploration of diffusion models for various image synthesis tasks (paper.pdf, page 2, Sec. 1).

### Out-of-scope uses:
The paper discusses the societal impact of generative models, highlighting potential misuse cases. These can be considered out-of-scope uses:
*   **Creating and disseminating manipulated data or misinformation ("deep fakes").** The paper notes that generative models make it easier to create such content, and women are disproportionately affected by this misuse (paper.pdf, page 9, Sec. 5).
*   **Generating content that reproduces or exacerbates existing data biases.** The model may reflect biases present in the training data (paper.pdf, page 9, Sec. 5).
*   **Applications requiring high-precision, fine-grained accuracy in pixel space.** The model's reconstruction capability can be a bottleneck in such tasks due to the perceptual compression stage (paper.pdf, page 9, Sec. 5).

---

## How to Use
This section outlines how to use the model. 

Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the conditioning inputs provided. These factors are used to guide the image generation process.
*   **Text Prompts:** The model can be conditioned on natural language descriptions to generate corresponding images (paper.pdf, page 1, Abstract).
*   **Semantic Layouts/Maps:** The model can synthesize images based on semantic maps that define the spatial arrangement of objects (paper.pdf, page 7, Sec. 4.3.1).
*   **Class Labels:** For class-conditional generation, the input class label determines the object to be synthesized (paper.pdf, page 1, Abstract).
*   **Bounding Boxes:** The model can generate images based on the spatial locations of bounding boxes (paper.pdf, page 1, Abstract).
*   **Low-Resolution Images:** For tasks like super-resolution and inpainting, a low-resolution or masked image is used as a conditioning input (paper.pdf, page 7, Sec. 4.4; page 8, Sec. 4.5).

### Evaluation factors:
The model is evaluated across a variety of factors, primarily different image synthesis tasks and datasets. These include:
*   **Unconditional Image Generation** on CelebA-HQ, FFHQ, LSUN-Churches, and LSUN-Bedrooms (paper.pdf, page 5, Sec. 4.2).
*   **Class-Conditional Image Generation** on ImageNet (paper.pdf, page 5, Sec. 4.1).
*   **Text-to-Image Synthesis** on the MS-COCO dataset (paper.pdf, page 6, Table 2).
*   **Image Inpainting** on the Places dataset (paper.pdf, page 8, Sec. 4.5).
*   **Super-Resolution** on the ImageNet dataset (paper.pdf, page 8, Sec. 4.4).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a combination of quantitative metrics and human evaluation:
*   **Fréchet Inception Distance (FID):** Used to measure the quality and diversity of generated samples. Lower scores are better (paper.pdf, page 5, Sec. 4.1).
*   **Inception Score (IS):** Used to assess the quality and diversity of generated images. Higher scores are better (paper.pdf, page 7, Table 3).
*   **Precision and Recall:** Used to evaluate the coverage of the data manifold, measuring the fidelity (Precision) and diversity (Recall) of the generated samples (paper.pdf, page 5, Sec. 4.2).
*   **CLIP Score:** A metric used to evaluate the correspondence between a text prompt and a generated image (FID vs CLIP Scores.png).
*   **PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural Similarity Index Measure):** Used for super-resolution tasks, although the paper notes these metrics do not always align well with human perception (paper.pdf, page 8, Sec. 4.4).
*   **LPIPS (Learned Perceptual Image Patch Similarity):** Used for inpainting evaluation to measure perceptual similarity (paper.pdf, page 8, Table 7).
*   **User Studies:** A 2-alternative force-choice paradigm was used to assess human preference for super-resolution and inpainting tasks (paper.pdf, page 8, Table 4).

### Decision thresholds:
The model uses classifier-free guidance with a scale `s` to improve sample quality. For text-to-image synthesis, a scale of `s = 10.0` was used (paper.pdf, page 6, Fig. 5). For class-conditional ImageNet generation, scales of `s = 3.0` and `s = 5.0` were used (paper.pdf, page 38, Fig. 27; page 37, Fig. 26).

### Variation approaches:
For quantitative metrics like FID and IS, statistics are estimated based on 50k generated samples compared against the entire training set of each dataset (paper.pdf, page 26, Sec. E.3.1). For efficiency, some analyses were conducted on 5k samples (paper.pdf, page 27, Sec. E.3.5). Human evaluation was conducted via a user study where subjects were asked for their preference between two generated images or between a generated image and the ground truth (paper.pdf, page 8, Table 4; page 27, Sec. E.3.6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on several publicly available, large-scale datasets:
*   **ImageNet:** Used for class-conditional synthesis, super-resolution, and inpainting. It is a large-scale hierarchical image database (paper.pdf, page 5, Sec. 4.1).
*   **CelebA-HQ:** A high-quality version of the CelebA dataset of celebrity faces, used for unconditional image generation (paper.pdf, page 5, Sec. 4.2).
*   **FFHQ:** A high-quality dataset of human faces, used for unconditional image generation (paper.pdf, page 5, Sec. 4.2).
*   **LSUN-Churches and LSUN-Bedrooms:** Subsets of the Large-scale Scene Understanding dataset, used for unconditional image generation (paper.pdf, page 5, Sec. 4.2).
*   **MS-COCO:** A large-scale object detection, segmentation, and captioning dataset. The validation set was used to evaluate text-to-image and layout-to-image synthesis (paper.pdf, page 7, Sec. 4.3.1).
*   **Places:** A 10 million image database for scene recognition, used for evaluating inpainting (paper.pdf, page 8, Sec. 4.5).
*   **DIV2K:** A dataset for super-resolution, used for evaluating the autoencoder's reconstruction quality (paper.pdf, page 1, Fig. 1).

### Motivation:
These datasets were chosen because they are standard benchmarks for various image synthesis tasks, allowing for direct comparison with state-of-the-art methods (paper.pdf, Sec. 4). They cover a wide range of domains, including faces, objects, and complex scenes, which tests the model's versatility and performance.

### Preprocessing:
*   **Super-Resolution:** For 4x upscaling on ImageNet, low-resolution images were created using bicubic interpolation with anti-aliasing (paper.pdf, page 8, Sec. 4.4).
*   **Inpainting:** The evaluation followed the protocol of LaMa [88], using a fixed set of 2k validation and 30k testing samples from Places, with synthetic masks generated using code from [88] (paper.pdf, page 26, Sec. E.2.2).
*   **Layout-to-Image:** For MS-COCO, 2048 unaugmented examples from the COCO Segmentation Challenge split were used (paper.pdf, page 27, Sec. E.3.3).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a variety of large-scale, publicly available datasets depending on the task:
*   **LAION-400M:** A dataset of 400 million CLIP-filtered image-text pairs, used for training the large-scale text-to-image model (paper.pdf, page 7, Sec. 4.3.1).
*   **OpenImages:** A large dataset with unified image classification, object detection, and visual relationship detection. Used for training the autoencoder and layout-to-image models (paper.pdf, page 7, Sec. 4.3.1; page 8, Sec. 4.4).
*   **ImageNet:** Used for training the class-conditional models (paper.pdf, page 5, Sec. 4.1).
*   **CelebA-HQ and FFHQ:** Used for training unconditional models on human faces (paper.pdf, page 5, Sec. 4.2).
*   **LSUN-Churches and LSUN-Bedrooms:** Used for training unconditional models on specific scene categories (paper.pdf, page 5, Sec. 4.2).
*   **COCO:** Used for training and fine-tuning layout-to-image models (paper.pdf, page 7, Sec. 4.3.1).

### Motivation:
The choice of datasets was to train powerful and flexible generators. Large-scale datasets like LAION-400M and OpenImages were used to train general-purpose models capable of handling a wide variety of concepts and styles. Task-specific datasets like ImageNet and CelebA-HQ were used for benchmarking against other state-of-the-art models in specific domains (paper.pdf, Sec. 4).

### Preprocessing:
For semantic synthesis, the model was trained on an input resolution of 256x256, using crops from 384x384 images (paper.pdf, page 7, Sec. 4.3.1). For inpainting, random crops of size 256x256 were used during training (paper.pdf, page 26, Sec. E.2.2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents extensive quantitative results disaggregated by task and dataset.
*   **Unconditional Image Generation (256x256):**
    *   CelebA-HQ: FID 5.11 (paper.pdf, page 6, Table 1).
    *   FFHQ: FID 4.98 (paper.pdf, page 6, Table 1).
    *   LSUN-Churches: FID 4.02 (paper.pdf, page 6, Table 1).
    *   LSUN-Bedrooms: FID 2.95 (paper.pdf, page 6, Table 1).
*   **Class-Conditional Image Generation on ImageNet (256x256):**
    *   LDM-4-G (with classifier-free guidance): FID 3.60, IS 247.67 (paper.pdf, page 7, Table 3).
*   **Text-to-Image Synthesis on MS-COCO (256x256):**
    *   LDM-KL-8-G (with classifier-free guidance): FID 12.63, IS 30.29 (paper.pdf, page 6, Table 2).
*   **Image Inpainting on Places (512x512):**
    *   LDM-4 (big, w/ ft): FID 9.39, LPIPS 0.246 (paper.pdf, page 9, Table 7).
*   **Super-Resolution on ImageNet (64->256):**
    *   LDM-4 (100 steps): FID 4.8 (train split) / 2.8 (val split) (paper.pdf, page 8, Table 5).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Inference is expensive due to sequential evaluations over many steps (25-1000) (paper.pdf, page 2, Sec. 1). However, LDMs significantly increase sample throughput compared to pixel-based models. For example, on CelebA-HQ, LDM-4 achieves a throughput of ~25 samples/sec for 200 DDIM steps, whereas LDM-1 (pixel-based) is below 5 samples/sec (paper.pdf, page 6, Fig. 7). Inference was assessed on a single NVIDIA A100 GPU (paper.pdf, page 28, Table 18).

### Training or Fine-tuning Requirements:
Training powerful diffusion models is computationally intensive, often consuming hundreds of GPU days (paper.pdf, page 1, Sec. 1). The LDM approach significantly reduces these requirements.
*   The class-conditional LDM-4-G model was trained for 178k steps with a batch size of 1200, which corresponds to approximately 35 V100 days (paper.pdf, page 28, Table 18; page 22, Fig. 17). This is a significant reduction from the 916 V100 days required for the pixel-based ADM-G model (paper.pdf, page 28, Table 18).
*   Unconditional models were trained on a single NVIDIA A100 GPU (paper.pdf, page 24, Table 12).
*   The large text-to-image model was trained on the LAION dataset for 390k steps with a batch size of 680 on a NVIDIA A100 (paper.pdf, page 25, Table 15).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The paper includes a "Societal Impact" section that discusses ethical considerations (paper.pdf, page 9, Sec. 5).
*   **Misinformation and "Deep Fakes":** The authors acknowledge that generative models make it easier to create and disseminate manipulated data, which can be used for misinformation and spam. They specifically mention the problem of "deep fakes" and note that women are disproportionately affected by this form of misuse.
*   **Data Bias:** The models may reproduce or exacerbate biases present in the training data. The extent to which the two-stage approach of LDMs misrepresents the data is noted as an important research question.
*   **Data Privacy:** Generative models can sometimes reveal their training data. This is a significant concern if the data contains sensitive or personal information collected without explicit consent. The extent to which this applies to diffusion models for images is not yet fully understood.
*   **Democratization of Technology:** By reducing the computational cost of training and inference, the LDM approach makes this technology more accessible, which can both enable creative applications and potentially lower the barrier for creating harmful content.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The paper explicitly lists several limitations in Section 5 (paper.pdf, page 9):
*   **Slower Sampling Speed:** While significantly faster than pixel-based diffusion models, the sequential sampling process of LDMs is still slower than that of GANs.
*   **Precision Bottleneck:** The perceptual compression stage, while generally preserving high-fidelity details, can be a bottleneck for tasks that require extremely fine-grained accuracy in pixel space. The reconstruction may not be perfect, which can affect precision-critical applications. This is noted as a potential limitation for the super-resolution models.
*   **Loss of Detail:** The autoencoder removes high-frequency details which are considered perceptually irrelevant. While this makes training more efficient, it means the model cannot be used for tasks that rely on analyzing these subtle details.

### Recommendations:
The paper does not provide explicit recommendations for users. However, based on the caveats and ethical considerations, the following can be inferred:
*   Users should be aware of the potential for the model to generate biased or harmful content and should not use it for creating malicious "deep fakes" or spreading misinformation.
*   For applications requiring perfect pixel-level accuracy, this model may not be suitable due to its latent-space nature.
*   Users should consider the trade-off between sampling speed and quality when choosing the number of DDIM steps for inference. More steps generally lead to higher quality but take longer.