## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by THL A29 Limited, a Tencent company (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.i; Notice.txt).

### Model date:
The Tencent Hunyuan model was released on May 14, 2024 (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT). The Acceptable Use Policy was also last modified on this date (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A).

### Model version:
Insufficient information. The documentation refers to the "Tencent Hunyuan version release date" but does not specify a version number (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 4).

### Model type:
Tencent Hunyuan is a collection of large-scale models, including large language models (LLMs), image generation models, and multimodal large language models (MLLMs) (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.j). The provided repository contains components for a multimodal model capable of dialogue generation and text-to-image (T2I) generation.

**Dialogue Generation Component (`dialoggen`):**
*   **Architecture:** The core architecture is `LlavaMistralForCausalLM`, indicating it is based on the LLaVA (Large Language and Vision Assistant) and Mistral models (dialoggen/config.json.txt).
*   **Key Parameters:**
    *   Hidden Size: 4096 (dialoggen/config.json.txt)
    *   Number of Hidden Layers: 32 (dialoggen/config.json.txt)
    *   Number of Attention Heads: 32 (dialoggen/config.json.txt)
    *   Intermediate Size: 14336 (dialoggen/config.json.txt)
    *   Vocabulary Size: 32000 (dialoggen/config.json.txt)
    *   Max Position Embeddings: 32768 (dialoggen/config.json.txt)
*   **Vision Tower:** It uses `openai/clip-vit-large-patch14-336` as its vision tower to process images (dialoggen/config.json.txt).
*   **Model Size:** The total size of the dialogue generation model weights is approximately 15.13 GB (15,132,446,720 bytes) (dialoggen/model.safetensors.index.json.txt).

**Text-to-Image Component (`t2i`):**
*   **Architecture:** The T2I component is a Diffusion Transformer (DiT) model, referred to as Hunyuan-DiT (asset/framework.png).
*   **Text Encoders:** It uses two text encoders to process text prompts: CLIP (specifically `hfl/chinese-roberta-wwm-ext-large`) and T5 (specifically `google/mt5-xl`) (asset/framework.png; t2i/clip_text_encoder/config.json.txt; t2i/mt5/config.json.txt).
*   **VAE (Variational Autoencoder):** It utilizes a VAE based on `stabilityai/sdxl-vae-fp16-fix` (t2i/sdxl-vae-fp16-fix/config.json.txt).

The overall framework supports multi-turn dialogue that can be grounded in images, leading to the generation of new images based on the conversation history (asset/mllm.png).

### Training details:
The model configuration files provide some hyperparameters used during development:
*   `attention_dropout`: 0.0 (dialoggen/config.json.txt)
*   `initializer_range`: 0.02 (dialoggen/config.json.txt)
*   `rms_norm_eps`: 1e-05 (dialoggen/config.json.txt)
*   `rope_theta`: 1,000,000.0 (dialoggen/config.json.txt)
*   `torch_dtype`: float16 (dialoggen/config.json.txt)

Information regarding the training algorithms (e.g., supervised learning, reinforcement learning), specific optimization techniques, or fairness constraints applied during training is not available in the repository.

### Paper or other resource for more information:
The model and its associated code are made publicly available by Tencent at the following repositories:
*   Hugging Face: https://huggingface.co/Tencent-Hunyuan/HunyuanDiT (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.j)
*   GitHub: https://github.com/Tencent/HunyuanDiT (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.j)

### Citation details:
Insufficient information.

### License:
The Tencent Hunyuan Works are licensed under the "Tencent Hunyuan Community License Agreement" (LICENSE.txt; TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT).

Key terms of the license include:
*   **Grant:** A non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, and create derivative works of the model and materials (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 2).
*   **Distribution:** If you distribute the Tencent Hunyuan Works, you must provide recipients with a copy of the license agreement, include prominent notices of any changes you made, and include a specific "Notice" text file with the distribution (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3).
*   **Commercial Use Restriction:** If the monthly active users (MAU) of your products or services using the model exceed 100 million, you must request a separate commercial license from Tencent (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 4).
*   **Use Restrictions:** The model cannot be used to improve any other large language model (other than Tencent Hunyuan or its derivatives) (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 5.b). Usage must also comply with the Acceptable Use Policy (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 5.a).
*   **Third-Party Components:** The model includes third-party components under various open-source licenses (e.g., Apache 2.0, BSD, MIT), and users must comply with their respective terms (Notice.txt).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a multimodal large language model intended for dialogue and text-to-image generation (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.j). Its capabilities include:
*   **Image-grounded Dialogue:** Engaging in multi-turn conversations about an input image. For example, a user can ask what an image contains and then follow up with requests to modify the scene described (asset/mllm.png).
*   **Text-to-Image Generation:** Based on a text prompt, which can be generated through a dialogue, the model can create new images using its Diffusion Transformer (DiT) component (asset/mllm.png; asset/framework.png).

The input-output structure involves providing an image and/or text as input, and the model produces a text response or a generated image as output (asset/mllm.png).

### Primary intended users:
The license agreement is granted to any "natural person or legal entity," suggesting a broad audience (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 1.e). Given the availability of the model on platforms like GitHub and Hugging Face, primary users likely include developers, researchers, and businesses looking to integrate multimodal AI capabilities into their applications.

### Out-of-scope uses:
The "Acceptable Use Policy" explicitly prohibits using the model for a wide range of applications. Users must not use Tencent Hunyuan or its derivatives for:
*   Any illegal activities or violation of laws and regulations (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 1).
*   Generating or disseminating verifiably false information with the intent to harm others or influence elections (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 6).
*   Exploiting, harming, or attempting to harm minors (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 5).
*   Discriminating against or harming individuals or groups based on protected characteristics (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 16).
*   Military purposes (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 18).
*   Making high-stakes automated decisions in domains like law enforcement, medicine, credit, employment, or housing (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 13).
*   Engaging in the unauthorized or unlicensed practice of professions such as finance, law, or medicine (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 19).

Additionally, the model must not be used to "improve any other large language model (other than Tencent Hunyuan or Model Derivatives thereof)" (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 5.b).

---

## How to Use
This section outlines how to use the model.

Insufficient information. The repository does not contain code snippets, tutorials, or detailed documentation on how to run the model.

However, the provided diagrams illustrate the model's functional flow (asset/mllm.png):
1.  A user provides an initial input, which can be an image and a text query (e.g., "What does the picture contain?").
2.  The model provides a text response describing the image.
3.  The user can continue the dialogue with a follow-up request (e.g., "Based on this image, add a puppy.").
4.  The model uses the dialogue history to generate a detailed text-to-image (T2I) prompt.
5.  This T2I prompt is fed into the Diffusion Transformer (DiT) component to generate a new image that reflects the user's request.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Insufficient information.

### Evaluation factors:
Insufficient information.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The repository includes a radar chart that compares "Hunyuan-Dit" against other models like Dalle3, Midjourney v6, and Stable Diffusion models (asset/radar.png). The performance is evaluated across the following qualitative dimensions:
*   Text-image consistency
*   Artifact
*   Clarity
*   Aesthetic

The specific quantitative metrics used to measure these dimensions (e.g., CLIP score, human preference scores) are not provided.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Insufficient information.

### Motivation:
Insufficient information.

### Preprocessing:
Insufficient information.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
Insufficient information.

### Motivation:
Insufficient information.

### Preprocessing:
Insufficient information.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The repository provides a radar chart comparing the performance of Hunyuan-DiT with other text-to-image models (asset/radar.png). The chart suggests that Hunyuan-DiT performs competitively, particularly in "Aesthetic" and "Clarity," where it scores similarly to Dalle3 and Midjourney v6. Its score for "Text-image consistency" appears slightly lower than Dalle3 but higher than other Stable Diffusion models shown.

No performance results for individual factors (e.g., demographic groups) are available.

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Model Size:** The dialogue generation component of the model has a total size of approximately 15.13 GB (15,132,446,720 bytes) (dialoggen/model.safetensors.index.json.txt).
*   **Data Type:** The model weights are stored in `float16` precision (dialoggen/config.json.txt).

Specific RAM/VRAM or CPU/GPU requirements are not specified.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The "Acceptable Use Policy" included in the license agreement outlines significant ethical considerations and risks associated with the model's usage. The policy mitigates these risks by contractually prohibiting users from applying the model in certain ways.

*   **Potential Risks and Mitigation:**
    *   **Harmful Content:** The policy prohibits using the model to harm oneself or others, exploit minors, defame or harass individuals, or promote violent extremism and terrorism (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Sections 2, 5, 8, 15).
    *   **Misinformation:** Generating or disseminating verifiably false information to harm others or influence elections is forbidden (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 6).
    *   **Bias and Discrimination:** The model must not be used to discriminate against or harm individuals or groups based on protected characteristics or personal attributes (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 16).
    *   **High-Stakes Decisions:** The use of the model for high-stakes automated decisions in critical areas such as law enforcement, migration, medicine, employment, and credit is out-of-scope (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 13).
    *   **Unauthorized Professional Practice:** The model should not be used for the unauthorized practice of professions like law, finance, or medicine (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, EXHIBIT A, Section 19).

*   **Responsibility for Outputs:** The license states that users are solely responsible for the outputs they generate and their subsequent use (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 6.d).

*   **Sensitive Data:** The provided materials do not specify whether sensitive data was used in the training of the model.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Data Transparency:** The repository provides no information about the datasets used for training or evaluating the model. This lack of transparency makes it difficult to assess potential biases, limitations, or gaps in the model's knowledge.
*   **Evaluation Gaps:** While a high-level comparative chart is provided (asset/radar.png), detailed quantitative metrics, benchmarks, and disaggregated performance analyses (e.g., across demographic groups) are missing.
*   **Usage Instructions:** The repository lacks specific code examples or documentation, which may make it challenging for users to implement and use the model effectively.

### Recommendations:
*   Users must carefully review and adhere to the "Tencent Hunyuan Community License Agreement," particularly the "Acceptable Use Policy," to mitigate ethical risks and ensure compliance (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT).
*   The license encourages users to publish a technology introduction blog post or public statement about their experience using the model (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3.c).
*   When developing products or services with the model, users are encouraged to indicate that the product/service is "Powered by Tencent Hunyuan" (TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT, Section 3.c).
*   Given the lack of information on training data, users should be cautious when deploying the model in contexts sensitive to societal biases and should conduct their own targeted evaluations to ensure fairness and safety for their specific use case.