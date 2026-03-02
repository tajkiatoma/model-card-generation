## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Tencent Hunyuan (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1). The legal entity is THL A29 Limited, referred to as "Tencent" (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.i). The development team includes Zhimin Li, Jianwei Zhang, Qin Lin, and numerous other contributors listed in the associated paper (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).

### Model date:
The Tencent Hunyuan release date is May 14, 2024 (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, p. 1). The associated academic paper was also submitted on May 14, 2024 (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).

### Model version:
The repository is for the initial public release of Hunyuan-DiT (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1). The model components were built using `transformers` version 4.37.2 (`config.json`).

### Model type:
Hunyuan-DiT is a text-to-image diffusion transformer model designed for fine-grained understanding of both English and Chinese prompts (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).

**Architecture Details:**
*   **Core Architecture:** It is a diffusion model that operates in the latent space, using a transformer architecture similar to DiT (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 7). The model structure is detailed in Figure 7 of the paper (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8).
*   **Text Encoders:** It combines two text encoders to enhance language understanding: a bilingual (Chinese-English) CLIP and a multilingual T5 encoder (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1, 7).
*   **Key Components:** The architecture uses cross-attention to combine text conditions, Rotary Positional Embedding (RoPE) for positional encoding, and skip modules between encoder and decoder blocks (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 7).
*   **Model Size:** The model has 1.5 billion parameters (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 15). The total size of the model weights is approximately 15.13 GB (`model.safetensors.index.json`).
*   **Context Length:** The model supports long text understanding up to 256 tokens (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 6).

The model type is specified as `llava_mistral` in its configuration, with 32 hidden layers, a hidden size of 4096, and 32 attention heads (`config.json`).

### Training details:
The model was trained as a diffusion model in the latent space, learning the data distribution from latents compressed by a pre-trained Variational Autoencoder (VAE) from SDXL (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 7).

*   **Algorithm:** The training uses a diffusion process with v-prediction, which was found to give better empirical performance (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 7).
*   **Training Stability:** To stabilize training, the developers implemented three techniques:
    1.  **QK-Norm:** Layer normalization is added in all attention modules before computing Q, K, and V.
    2.  Layer normalization is added after the skip module in the decoder blocks to prevent loss explosion.
    3.  Certain operations like layer normalization are switched to FP32 to avoid numerical errors and overflow (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8).
*   **Data Optimization:** The model is optimized iteratively using a "data convoy" mechanism, which involves categorizing training data, fine-tuning the model on category-balanced datasets, and performing category-level comparisons to guide data updates (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 9; Figure 21, p. 24).

### Paper or other resource for more information:
*   **Academic Paper:** "Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding" provides a comprehensive overview of the model's architecture, data pipeline, and evaluation (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding.pdf).
*   **Repositories:** The code and pretrained models are publicly available at:
    *   GitHub: `github.com/Tencent/HunyuanDiT` (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1)
    *   Hugging Face: `https://huggingface.co/Tencent-Hunyuan/HunyuanDiT` (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.j)

### Citation details:
Insufficient information. A BibTeX entry is not provided in the repository.

### License:
The model is licensed under the **Tencent Hunyuan Community License Agreement** (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT.pdf).

Key terms of the license include:
*   **Grant:** A non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, and create derivative works of the model and materials (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 2).
*   **Distribution:** If you distribute the Tencent Hunyuan Works, you must provide a copy of the license agreement to recipients and include a "Notice" text file with the copyright and license information (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3).
*   **Commercial Use:** If your products or services using the model have more than 100 million monthly active users, you must request a separate commercial license from Tencent (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 4).
*   **Use Restrictions:** Usage must comply with the **Acceptable Use Policy** (Exhibit A), which prohibits activities such as generating harmful content, spreading misinformation, military use, and making high-stakes automated decisions. Additionally, you must not use the model or its outputs to improve any other large language model (other than Tencent Hunyuan itself) (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 5).
*   **Third-Party Components:** The model includes various third-party components under different open-source licenses, including Apache 2.0, BSD 3-Clause, MIT, and HPND. Users must comply with the terms of these original licenses (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, p. 3-10).

### Contact:
For questions or feedback, the corresponding author of the paper can be contacted at: `qinglinlu@tencent.com` (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Hunyuan-DiT is a text-to-image generative model intended for creating high-quality images from text prompts in both English and Chinese (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).

Its primary capabilities include:
*   **High-Quality Image Generation:** Generating detailed images in multiple resolutions based on text descriptions (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1, Figures 1-4).
*   **Fine-Grained Language Understanding:** Accurately interpreting complex prompts, including those with abstract semantics like ancient Chinese poetry and idioms (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 6, 12).
*   **Multi-Turn Dialogue:** Engaging in interactive, multi-turn conversations with users to iteratively generate and refine images based on the dialogue context (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1, Figure 5).

The input-output structure involves a user providing a text prompt (or an image and text in a multi-turn context), and the model outputting a generated image (`how_to_use.png`).

### Primary intended users:
The model is intended for a broad audience, including natural persons and legal entities such as researchers, developers, and businesses who wish to incorporate text-to-image generation capabilities into their applications or conduct research in this area (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.e; Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 18).

### Out-of-scope uses:
The model is not designed for any use that violates the **Acceptable Use Policy** (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Exhibit A). Prohibited uses include, but are not limited to:
*   Any illegal activities or violation of laws and regulations.
*   Generating or disseminating content intended to harm, exploit, defame, or harass individuals or groups.
*   Creating and spreading verifiably false information, malware, or personal identifiable information with malicious intent.
*   Impersonating individuals without consent.
*   Military purposes.
*   Making high-stakes automated decisions in critical domains such as law enforcement, migration, medicine, credit, employment, or housing.
*   Unauthorized or unlicensed practice of professions (e.g., legal, medical, financial advice).
*   Using the model or its outputs to improve any other large language model (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 5.b).

---

## How to Use
This section outlines how to use the model.

The repository provides a visual representation of how to use the model in a multi-turn dialogue setting (`how_to_use.png`). The process is as follows:

1.  **Initial Prompt:** A user can start with an image and a text query, such as asking what the image contains.
2.  **Model's Text Response:** The MLLM component analyzes the image and text, providing a descriptive answer.
3.  **Follow-up Instruction:** The user can then provide a follow-up instruction to modify the image, for example, "Based on this image, add a puppy."
4.  **Enhanced T2I Prompt Generation:** The MLLM processes the dialogue history and the new instruction to generate a detailed text-to-image prompt that incorporates the requested changes. For example: "Under the blue sky and white clouds, a puppy is playing on the green grass with blooming white wild-flowers growing on it. The lens is a panoramic shot and the style is real photography."
5.  **Image Generation:** The Hunyuan-DiT model takes this enhanced prompt and generates the final, refined image.

The model can also be used directly for text-to-image generation through a user interface, as suggested by the provided screenshot (`tencent_yuan_sheng_tu.png`), where a user can input a text prompt to generate an image.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is designed to understand both English and Chinese prompts, making language a key factor (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 1).
*   **Subject Matter:** The model's performance may vary depending on the subject of the prompt. The training data covers a wide range of subjects, including humans, landscapes, plants, animals, goods, and transportation (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 9, Figure 18).
*   **Artistic Style:** The requested style is another relevant factor. The model has been trained on over a hundred styles, such as anime, 3D, painting, realistic, and traditional styles (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 9, Figure 19).
*   **Prompt Complexity:** The difficulty of the prompt, including the number of descriptive elements and the presence of abstract semantics (e.g., poems, idioms), can influence performance (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12).

### Evaluation factors:
The factors analyzed and reported during model evaluation are:
*   **Text-Image Consistency:** How well the generated image matches the text prompt.
*   **AI Artifacts:** The presence of visual distortions or unnatural elements.
*   **Subject Clarity:** The clarity and recognizability of the main subject in the image.
*   **Overall Aesthetics:** The artistic and visual quality of the image.
*   **Instruction Compliance (for multi-turn):** How well the model follows user instructions in a dialogue.
*   **Subject Consistency (for multi-turn):** How consistent the subject remains across multiple turns of editing.
(Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using both automated metrics and a holistic human evaluation protocol (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 6, 12).
*   **Human Evaluation:** A team of over 50 professional evaluators assesses generated images across four dimensions: text-image consistency, AI artifacts, subject clarity, and overall aesthetics. The primary metric is the **Overall Pass Rate**, which is a weighted average of scores across different content categories (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 13-14, Table 2).
*   **Automated Metrics:** For ablation studies, the model is evaluated using standard text-to-image metrics:
    *   **Frechet Inception Distance (FID):** Measures the quality and diversity of generated images. Lower is better.
    *   **CLIP Score:** Measures the semantic similarity between the text prompt and the generated image. Higher is better.
    (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 16)

### Decision thresholds:
During human evaluation, a "pass rate" is calculated for each prompt. This is the percentage of evaluators who deem the generated image "acceptable". For example, if 7 out of 10 evaluators find an image acceptable, the pass rate for that prompt is 70%. This rate is then averaged across prompts within a category to determine the category score (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 13).

### Variation approaches:
To ensure robust measurements and mitigate subjective bias, the evaluation process includes a multi-person correction stage where multiple evaluators independently assess the same set of images. The results are then aggregated and analyzed (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 13). The final overall pass rate is a weighted average of scores from different high-level categories, with weights determined through discussions with users, designers, and experts (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 14, Table 2).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Two types of datasets were used for evaluation:
1.  **Custom Hierarchical Evaluation Dataset:** This is the primary dataset for the main quantitative analysis. It was constructed by combining AI-generated and human-created test prompts. It contains over 3,000 prompts in total, structured in a 3-level hierarchy with 8 level-1 categories and over 70 level-2 categories. Each level-2 category contains 30-50 prompts (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 13).
2.  **MS COCO Validation Dataset:** For ablation studies, the model was evaluated on the MS COCO 2014 validation dataset, generating 30,000 images from its prompts at a 256x256 resolution (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 16).

### Motivation:
*   The **custom dataset** was created to "holistically evaluate the generation ability of Hunyuan-DiT" with professionalism and practicality. It is categorized into three difficulty levels (easy, medium, hard) based on prompt richness and abstractness to test the model's capabilities in handling complex scenarios (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12).
*   The **MS COCO dataset** was used because it is a standard benchmark in prior research, allowing for comparable ablation study results (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 16).

### Preprocessing:
Insufficient information.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was sourced from "external purchasing, open data downloading, and authorized partner data" (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8). The data is structured into a hierarchical pipeline:
*   **Copper-Tier:** Billions of image-text pairs used to train the foundational bilingual CLIP model.
*   **Silver-Tier:** A relatively high-quality subset screened from the copper-tier data, used to train the main generative model.
*   **Gold-Tier:** The highest quality data, selected through machine screening and manual annotation, used for refining and optimizing the generative model.
(Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8-9, Figure 20).

The data covers a wide range of subjects (Figure 18) and styles (Figure 19), with over ten thousand subject sub-categories and over a hundred style categories (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 9, 22-23).

### Motivation:
The multi-tiered data pipeline was designed to serve different stages of model training effectively. Using a massive "copper-tier" dataset allows for robust training of the foundational CLIP model, while the higher-quality "silver" and "gold" tiers are used to train and refine the generative model to improve its quality and understanding capabilities. This layered approach supports iterative model optimization (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8-9).

### Preprocessing:
The data processing pipeline involves several key steps before the data is used for training (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8-10, Figure 20):
*   **Data Interpretation:** Raw data is tagged with over ten capabilities, including image clarity, aesthetics, indecency, violence, watermarks, image classification, and image description.
*   **Caption Refinement:** A fine-tuned Multimodal Large Language Model (MLLM) is used to "re-caption" raw image-text pairs to enhance data quality. This process generates comprehensive "structural captions" and can incorporate world knowledge through two methods:
    1.  **Tag Injection:** Tags from expert models or human labelers (e.g., "Shanghai Bund") are injected into the MLLM to generate more descriptive captions.
    2.  **Raw Caption Fusion:** The MLLM takes both the image and its original noisy caption as input to generate a corrected, higher-quality caption.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was compared against other state-of-the-art open-source and closed-source models. The results are disaggregated by four unitary evaluation factors, based on a human evaluation protocol.

**Hunyuan-DiT Performance:**
*   **Text-Image Consistency:** 74.2%
*   **Excluding AI Artifacts:** 74.3%
*   **Subject Clarity:** 95.4%
*   **Aesthetics:** 86.6%
*   **Overall Pass Rate:** 59.0%

Compared to other open-source models like Playground 2.5, PixArt-α, and SDXL, Hunyuan-DiT achieved the highest score across all four dimensions and the overall pass rate (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, Table 1, p. 16). A radar chart also visualizes this comparison (`performance_chart.png`).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is 15,132,446,720 bytes (approximately 15.1 GB) (`model.safetensors.index.json`). The model uses the `float16` data type, suggesting that at least 16 GB of VRAM would be required to load the model into memory (`config.json`).

### Deploying Requirements:
Deploying the model is described as "expensive." To improve inference efficiency, the developers adopted multiple optimization strategies, including ONNX graph optimization, kernel optimization, operator fusion, precomputation, and GPU memory reuse. Specific hardware requirements are not provided (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12).

### Training or Fine-tuning Requirements:
Training the model requires significant computational resources due to its large parameter count and the massive amount of data used. To enhance training speed, the following techniques were employed: ZeRO, flash-attention, multi-stream asynchronous execution, activation checkpointing, and kernel fusion. The paper notes that some training methods, like adversarial training, have a "severe demand of extra GPU memory and training time" (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12). Specific hardware configurations are not detailed.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development and use of Hunyuan-DiT are governed by an **Acceptable Use Policy** designed to promote safe and fair use (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Exhibit A).

*   **Risk Mitigation during Development:** The data processing pipeline includes a "Data Interpretation" step where data is tagged for harmful content such as "indecency, violence, sexual content" (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 8). This suggests an effort to filter such content from the training data. During evaluation, any generated images that raise safety concerns (e.g., involving pornography, politics, violence, or bloodshed) are marked as "unacceptable" (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 12).

*   **Risks in Model Usage and Mitigation:** The license explicitly prohibits using the model for a wide range of unethical or harmful applications. Affected groups could include minors, individuals targeted by harassment or misinformation, and groups subject to discrimination. Known high-risk use cases that are explicitly forbidden include:
    *   Exploiting or harming minors.
    *   Generating or disseminating verifiably false information to harm others or influence elections.
    *   Intentionally defaming, disparaging, or harassing others.
    *   Generating content for military purposes.
    *   Discriminating against or harming individuals or groups based on protected characteristics.
    *   Making high-stakes automated decisions in domains like law enforcement, medicine, employment, and credit.
    (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Exhibit A)

*   **Sensitive Data:** The repository does not specify if sensitive personal data was used in training. However, the Acceptable Use Policy prohibits the use of the model "to generate or disseminate personal identifiable information with the purpose of harming others" (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Exhibit A, Item 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **VAE Quality:** The quality of the Variational Autoencoder (VAE) latent space significantly influences the final generation quality. The developers note that they plan to "explore a better training paradigm for the VAE in the future," indicating this is a current area for improvement (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 7).
*   **Evaluation Protocol:** The evaluation protocol is described as being under "continuous optimization," with plans to introduce new dimensions, add more in-depth analysis, and dynamically adjust datasets. This suggests the current evaluation may have gaps (Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding, p. 15).

### Recommendations:
*   Users should adhere strictly to the **Acceptable Use Policy** to mitigate risks of misuse and potential harm (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Exhibit A).
*   Users are encouraged to provide feedback by publishing blog posts or public statements about their experience with the model (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3.c).
*   When using the model in products or services, it is encouraged to indicate that the product/service is "Powered by Tencent Hunyuan" (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3.c).
*   Users should be aware of the model's limitations and the ongoing nature of its development, particularly regarding the VAE and evaluation methods.