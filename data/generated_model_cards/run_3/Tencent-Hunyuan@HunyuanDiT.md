## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the Tencent Hunyuan team (Paper, p. 1). The authors of the associated paper are Zhimin Li, Jianwei Zhang, Qin Lin, Jiangfeng Xiong, Yanxin Long, Xinchi Deng, Yingfang Zhang, Xingchao Liu, Minbin Huang, Zedong Xiao, Dayou Chen, Jiajun He, Jiahao Li, Wenyue Li, Chen Zhang, Rongwei Quan, Jianxiang Lu, Jiabin Huang, Xiaoyan Yuan, Xiaoxiao Zheng, Yixuan Li, Jihong Zhang, Chao Zhang, Meng Chen, Jie Liu, Zheng Fang, Weiyan Wang, Jinbao Xue, Yangyu Tao, Jianchen Zhu, Kai Liu, Sihuan Lin, Yifu Sun, Yun Li, Dongdong Wang, Mingtao Chen, Zhichao Hu, Xiao Xiao, Yan Chen, Yuhong Liu, Wei Liu, Di Wang, Yong Yang, Jie Jiang, and Qinglin Lu (Paper, p. 1). The legal entity associated with the model is THL A29 Limited, a Tencent company (License, Section 1.i; License, Usage and Legal Notices).

### Model date:
The model was released on May 14, 2024 (License, Header; Paper, p. 1).

### Model version:
The version described is `v1`, as presented in the paper `arXiv:2405.08748v1` (Paper, p. 1). The paper compares Hunyuan-DiT with other state-of-the-art open-source models (Playground 2.5, PixArt-α, SDXL) and closed-source models (DALL-E 3, SD 3, MidJourney v6), demonstrating superior performance among open-source alternatives in Chinese-to-image generation (Paper, p. 15-16).

### Model type:
Hunyuan-DiT is a text-to-image diffusion transformer model designed for fine-grained understanding of both English and Chinese prompts (Paper, p. 1).

*   **Architecture**: It is a diffusion model that operates in the latent space, using a pre-trained Variational Autoencoder (VAE) from SDXL to compress images (Paper, p. 7). The core of the model is a diffusion transformer architecture, which modifies the baseline DiT by incorporating cross-attention to integrate text conditions, similar to Stable Diffusion (Paper, p. 7). The architecture consists of encoder and decoder transformer blocks, each containing self-attention, cross-attention, and feed-forward network modules. The decoder blocks also include a skip module to add information from the encoder block, mimicking U-Net skip-connections (Paper, p. 7).
*   **Text Encoders**: To enhance language understanding, the model combines two pre-trained text encoders: a bilingual (English and Chinese) CLIP and a multilingual T5 encoder (Paper, p. 1, 7).
*   **Positional Encoding**: It employs two-dimensional Rotary Positional Embedding (RoPE) to encode both absolute and relative position dependencies for image tokens (Paper, p. 7).
*   **Model Size**: The model has 1.5 billion parameters (Paper, p. 15).
*   **Context Length**: It supports text understanding for prompts up to 256 tokens (Paper, p. 6).

### Training details:
The model's training process is supported by a comprehensive data pipeline and specific optimization techniques.

*   **Training Algorithm**: The model is trained as a latent diffusion model using a v-prediction objective, which was found to yield better empirical performance (Paper, p. 7).
*   **Data Pipeline**: A four-stage data pipeline was built from scratch (Paper, p. 1, 8):
    1.  **Data Acquisition**: Data is sourced from external purchasing, open data downloading, and authorized partners (Paper, p. 8).
    2.  **Data Interpretation**: Raw data is tagged for attributes like clarity, aesthetics, toxicity, and image content (Paper, p. 8).
    3.  **Data Layering**: Data is stratified into three tiers (copper, silver, gold) to serve different training stages, from foundational model training to fine-tuning (Paper, p. 8).
    4.  **Data Application**: Data is used for iterative optimization through a 'data convoy' mechanism, which involves categorizing data, fine-tuning the model on balanced datasets, and performing category-level evaluations to guide further data updates (Paper, p. 9).
*   **Caption Refinement**: To improve data quality, a Multimodal Large Language Model (MLLM) is used to re-caption raw image-text pairs, generating detailed structural captions (Paper, p. 9).
*   **Training Stability**: To ensure stable training, three techniques were employed:
    1.  QK-Norm: Layer normalization is added in all attention modules before computing Q, K, and V (Paper, p. 8).
    2.  Layer normalization is added after the skip module in decoder blocks to prevent loss explosion (Paper, p. 8).
    3.  Certain operations, like layer normalization, are switched from FP16 to FP32 to avoid numerical errors (Paper, p. 8).
*   **Efficiency Optimization**: Training speed was enhanced using ZeRO, flash-attention, multi-stream asynchronous execution, activation checkpointing, and kernel fusion (Paper, p. 12).

### Paper or other resource for more information:
*   **Academic Paper**: Li, Z., Zhang, J., Lin, Q., et al. (2024). *Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding*. arXiv:2405.08748v1 [cs.CV]. This paper provides a detailed overview of the model's architecture, data pipeline, and evaluation (Paper, p. 1).
*   **Repositories**: Code and pretrained models are publicly available at:
    *   GitHub: `https://github.com/Tencent/HunyuanDiT` (Paper, p. 1; License, Section 1.j)
    *   Hugging Face: `https://huggingface.co/Tencent-Hunyuan/HunyuanDiT` (License, Section 1.j)

### Citation details:
Insufficient information. The provided repository does not contain a BibTeX citation.

### License:
The model is released under the **Tencent Hunyuan Community License Agreement** (License, Header).

*   **Permissions**: The license grants a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, create derivative works of (including Model Derivatives), and modify the model materials (License, Section 2).
*   **Distribution**: When distributing the model or works derived from it, you must provide recipients with a copy of the license agreement, include notices of any modifications, and include a "Notice" text file with the Tencent Hunyuan copyright and license information (License, Section 3).
*   **Commercial Use**: If the monthly active users (MAU) of all products or services using the model exceed 100 million, you must request a separate commercial license from Tencent (License, Section 4).
*   **Restrictions**: Use of the model must comply with the **Acceptable Use Policy** (License, Exhibit A). You must not use the model or its outputs to improve any other large language model (other than Tencent Hunyuan or its derivatives) (License, Section 5.b).
*   **Disclaimer**: The model is provided "AS IS" without any warranties. Tencent is not liable for any damages arising from the use of the model (License, Section 7).

### Contact:
For inquiries, the corresponding author of the paper can be contacted at: `qinglinlu@tencent.com` (Paper, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Hunyuan-DiT is a text-to-image generative model intended for creating high-quality, detailed images from text prompts in both English and Chinese (Paper, p. 1). Its primary capabilities include:

*   **Text-to-Image Generation**: Generating images that correspond to fine-grained text descriptions. It shows strong performance in understanding Chinese elements, such as ancient poetry and cuisine (Paper, p. 2, 6).
*   **Multi-Resolution Generation**: The model can generate images in various resolutions (Paper, p. 1, 5).
*   **Long-Text Understanding**: It can process and generate images from text prompts up to 256 tokens long (Paper, p. 4, 6).
*   **Multi-Turn Dialogue**: The model can engage in multi-turn conversations with users to interactively generate and refine images based on the dialogue context (Paper, p. 1, 6). For example, a user can ask to generate an image of a cat on a roof and then, in a subsequent turn, ask to change the background to a polar region (Paper, p. 6).

The model's input is typically a text prompt, and the output is an image. In multi-turn mode, the input can be a combination of text and the previously generated image (Paper, p. 10).

### Primary intended users:
The model is intended for a broad audience, including researchers, developers, and creators who are interested in text-to-image generation, particularly with a focus on Chinese language and culture (Paper, p. 18). The license addresses any "natural person or legal entity" using the model, indicating its availability for both individual and organizational use (License, Section 1.e).

### Out-of-scope uses:
The **Acceptable Use Policy** explicitly prohibits using the model for a wide range of applications (License, Exhibit A). Any use that violates these terms is considered out-of-scope. Prohibited uses include, but are not limited to:

*   Any activity that violates applicable laws or regulations.
*   Generating content to harm, exploit, defame, or harass individuals or groups.
*   Creating or disseminating verifiably false information with the intent to harm others or influence elections.
*   Generating malware, ransomware, or other malicious content.
*   Discriminating against individuals or groups based on protected characteristics.
*   Military purposes.
*   Making high-stakes automated decisions in domains like law enforcement, medicine, credit, or employment.
*   The unauthorized or unlicensed practice of professions (e.g., legal, medical, financial advice).
*   Using the model or its outputs to train or improve any competing large language model (License, Section 5.b).

---

## How to Use
This section outlines how to use the model.

The provided documents do not include specific code snippets for implementation. However, they state that code and pretrained models are available at `https://github.com/Tencent/HunyuanDiT` (Paper, p. 1). The paper provides numerous examples of the model's input-output behavior.

**Input-Output Structure:**
*   **Input**: A text prompt in English or Chinese (Paper, p. 1). For multi-turn dialogue, the input can also include the dialogue history and the previously generated image (Paper, p. 10).
*   **Output**: A generated image corresponding to the input prompt (Paper, p. 1).

**Example Use Cases from the Paper:**

*   **Generating images from Chinese cultural prompts**:
    *   **Input Prompt (Chinese)**: `枯藤老树昏鸦,小桥流水人家` (Withered vines, old trees, there are some crows at dusk; A small bridge, flowing water, some huts.)
    *   **Output**: An image depicting the described poetic scene (Paper, p. 2).
*   **Generating images from fine-grained descriptions**:
    *   **Input Prompt (English)**: "A Puss in Boots, armed with a bright silver sword and clad in armor, stood on top of a pile of gold coins. The background was a dark-colored cave, and the image was dotted with gold coins."
    *   **Output**: An image of Puss in Boots matching the detailed description (Paper, p. 3).
*   **Multi-turn image editing**:
    *   **Turn 1 Input**: "Please draw a wooden bird and place it on a branch."
    *   **Turn 1 Output**: An image of a wooden bird on a branch.
    *   **Turn 2 Input**: "Change the bird's material to glass."
    *   **Turn 2 Output**: The same image, but the bird is now made of glass (Paper, p. 6).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The performance of Hunyuan-DiT is influenced by the composition and quality of the training data. Key factors identified include:
*   **Data Categories**: The model's ability to generate diverse content depends on the coverage of data categories. The training data is structured around two fundamental categories:
    *   **Subject**: Covers a wide range of topics including human, landscape, plants, animals, goods, transportation, and games, with over ten thousand sub-categories (Paper, p. 9, 22).
    *   **Style**: Includes over a hundred styles such as anime, 3D, painting, realistic, and traditional styles (Paper, p. 9, 23).
*   **Prompt Complexity**: The model's performance is also affected by the complexity of the input prompt, including the richness of content, the number of descriptive elements (subject, modifiers, background, style), and the presence of abstract semantics like poems or idioms (Paper, p. 12).

### Evaluation factors:
The model was evaluated on a specific set of factors to measure its performance comprehensively:
*   **For single-turn generation**:
    *   **Text-image consistency**: How well the generated image aligns with the text prompt.
    *   **AI artifacts**: The absence of visual glitches or unnatural elements.
    *   **Subject clarity**: How clearly and accurately the main subject is depicted.
    *   **Overall aesthetics**: The artistic quality and visual appeal of the image (Paper, p. 12).
*   **For multi-turn dialogue**:
    *   **Instruction compliance**: How well the model follows the user's editing instructions.
    *   **Subject consistency**: Maintaining the identity and characteristics of the subject across multiple turns.
    *   **Prompt enhancement performance**: The quality of the refined text prompts generated by the MLLM for the diffusion model (Paper, p. 12).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Human Evaluation**: The primary evaluation method is a human-led protocol involving over 50 professional evaluators (Paper, p. 1, 13). The core metric is the **Overall Pass Rate**, which is the weighted percentage of evaluators who deem a generated image "acceptable" based on the evaluation dimensions (text-image consistency, AI artifacts, subject clarity, aesthetics) (Paper, p. 13-14).
*   **Automated Metrics (for Ablation Studies)**: For internal ablation studies on a smaller version of the model, the following automated metrics were used:
    *   **Frechet Inception Distance (FID)**: To measure the quality and diversity of generated images. Lower is better (Paper, p. 16).
    *   **CLIP Score**: To measure the correspondence between the generated image and the text prompt. Higher is better (Paper, p. 16).

### Decision thresholds:
The evaluation process does not use a single binary decision threshold. Instead, it calculates a "pass rate" for each prompt, which is the percentage of evaluators who find the image acceptable. For example, if 7 out of 10 evaluators approve an image, the pass rate for that prompt is 70% (Paper, p. 13). These pass rates are then averaged across categories to produce final scores (Paper, p. 14).

### Variation approaches:
To ensure robust and reliable measurements, the evaluation process incorporates several approaches to handle variation and subjectivity:
*   **Multi-Person Correction**: Multiple evaluators independently assess the same set of images. The results are then aggregated and analyzed to mitigate individual subjective biases (Paper, p. 13).
*   **Hierarchical Scoring**: Scores are calculated at three levels. First, a pass rate is determined for each individual prompt. These are then averaged to get scores for level-2 categories (e.g., "animals," "vehicles"). Finally, the level-2 scores are averaged to get scores for level-1 categories (e.g., "Subject and Details," "Artistic Styles") (Paper, p. 14).
*   **Weighted Overall Score**: The final overall pass rate is a weighted average of the level-1 category scores, with weights determined through discussions with users, designers, and experts (Paper, p. 14, 25).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Primary Evaluation Dataset**: A custom, hierarchical evaluation dataset was constructed by combining AI-generated and human-created test prompts. This dataset contains over 3,000 prompts in total, categorized into three difficulty levels (easy, medium, hard). The prompts are structured into a 3-level hierarchy with 8 level-1 categories (e.g., Human Characters, Chinese Elements, Artistic Styles) and over 70 level-2 categories (e.g., animals, plants, vehicles) (Paper, p. 12-13).
*   **Ablation Study Dataset**: For ablation studies, the **MS COCO 256 × 256 validation dataset** was used. The evaluation involved generating 30,000 images from prompts in this validation set (Paper, p. 16).

### Motivation:
The primary evaluation dataset was created to "holistically evaluate the generation ability of Hunyuan-DiT" (Paper, p. 12). The categories were selected based on an analysis of common user prompts, interviews with users, and opinions from expert designers to ensure the evaluation covers a wide range of practical and creative use cases (Paper, p. 13). The inclusion of different difficulty levels and abstract semantics (like poems and idioms) was motivated by the need to test the model's capabilities in handling complex and nuanced scenarios (Paper, p. 12). The MS COCO dataset was used for ablation studies to follow standard practices in prior research (Paper, p. 16).

### Preprocessing:
The paper does not detail specific preprocessing steps for the evaluation prompts. It does mention that Large Language Models (LLMs) were used to "enhance the diversity and difficulty of the test prompts, rapidly iterate on prompt generation, and reduce manual labor" during the dataset's construction (Paper, p. 12).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was collected from three primary sources: **external purchasing, open data downloading, and authorized partner data** (Paper, p. 8). The data is organized into a hierarchical system with two main categories:
*   **Subject**: This category includes over 10,000 sub-categories such as human, landscape, plants, animals, goods, transportation, and games (Paper, p. 9, 22).
*   **Style**: This category covers over 100 styles, including anime, 3D, painting, realistic, and traditional styles (Paper, p. 9, 23).

The data is further stratified into three quality tiers:
*   **Copper-tier**: Billions of image-text pairs used to train the foundational CLIP model (Paper, p. 8).
*   **Silver-tier**: A high-quality subset screened from the copper-tier data, used to train the generative model (Paper, p. 8).
*   **Gold-tier**: The highest quality data, selected via machine screening and manual annotation, used for refining and optimizing the generative model (Paper, p. 8-9).

### Motivation:
The choice of a large and diverse dataset was motivated by the finding that "the coverage of the data categories in the training data [is] crucial for training accurate text-to-image models" (Paper, p. 9). The data layering strategy was designed to efficiently serve the different stages of model training, using vast amounts of data for foundational understanding and progressively higher-quality data for refining generation capabilities (Paper, p. 8).

### Preprocessing:
The training data undergoes a significant preprocessing and refinement pipeline:
*   **Data Interpretation**: Raw data is processed and tagged for over ten attributes, including image clarity, aesthetics, toxicity (indecency, violence), sexual content, watermarks, image classification, and image description (Paper, p. 8).
*   **Caption Refinement**: A key step is improving the quality of text captions associated with images. A specialized Multimodal Large Language Model (MLLM) is used to re-caption the raw image-text pairs. This process aims to create comprehensive "structural captions" that better describe the image content (Paper, p. 9). Two methods are used to inject world knowledge into the captions:
    1.  **Re-captioning with Tag Injection**: Expert models (e.g., object detectors, landmark classifiers) and human labelers provide tags for an image, which are then used by the MLLM to generate a more detailed caption (Paper, p. 10).
    2.  **Re-captioning with Raw Captions**: The MLLM takes both the image and its original (often noisy) raw caption as input to generate a corrected, more accurate caption (Paper, p. 10).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of Hunyuan-DiT was evaluated by human reviewers across four dimensions. The model achieved the following pass rates, which were the highest among all tested open-source models (Playground 2.5, PixArt-α, SDXL) (Paper, p. 16, Table 1).

*   **Text-Image Consistency**: 74.2%
*   **Excluding AI Artifacts**: 74.3%
*   **Subject Clarity**: 95.4%
*   **Aesthetics**: 86.6%
*   **Overall**: 59.0%

### Intersectional results:
Insufficient information. The provided documents do not contain performance results for combinations of factors (e.g., accuracy for a specific style within a specific subject category).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
The paper states that "Deploying Hunyuan-DiT for the users is expensive" and mentions the use of optimization strategies like ONNX graph optimization, kernel optimization, and GPU memory reuse to improve inference efficiency (Paper, p. 12). However, specific memory or hardware requirements (e.g., VRAM, RAM) are not provided.

### Training or Fine-tuning Requirements:
The paper notes the "large number of model parameters in Hunyuan-DiT and the massive amount of image data required for training" (Paper, p. 12). It also mentions the use of advanced optimization techniques to enhance training speed, such as ZeRO (for memory optimization), flash-attention, and activation checkpointing (Paper, p. 12). This implies that training requires a significant multi-GPU setup, but specific hardware configurations or memory footprints are not detailed.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Sensitive Data**: The training data includes a "human" category, and the data interpretation pipeline involves "Face Recognition" (for gender, age, face count), indicating that data containing personal characteristics was used (Paper, p. 8-9). The Acceptable Use Policy prohibits the generation or dissemination of personally identifiable information "with the purpose of harming others" (License, Exhibit A, item 10).
*   **Risk Mitigation**: Several strategies were implemented to mitigate risks:
    *   **Toxicity Detection**: The data pipeline includes automated detection for "indecency, vulgar, violence" and "sexual content" in the training data (Paper, p. 8).
    *   **Safety in Evaluation**: During evaluation, any generated images that raise safety concerns (e.g., "pornography, politics, violence, or bloodshed") are marked as unacceptable (Paper, p. 12).
    *   **Acceptable Use Policy**: The license includes a comprehensive Acceptable Use Policy that strictly prohibits the use of the model for harmful, unethical, or illegal purposes. This includes generating false information, harassment, discrimination, and content for military use (License, Exhibit A).
*   **Risks in Model Usage**: The Acceptable Use Policy highlights numerous potential risks and misuses. Known high-risk use cases that are explicitly forbidden include:
    *   **Disinformation**: Generating "verifiably false information and/or content with the purpose of harming others or influencing elections" (License, Exhibit A, item 6).
    *   **Harassment**: Intentionally defaming, disparaging, or harassing others (License, Exhibit A, item 8).
    *   **High-Stakes Automated Decisions**: Using the model for decisions affecting an individual's safety, rights, or well-being in domains like law enforcement, migration, medicine, employment, or credit (License, Exhibit A, item 13).
*   **User Responsibility**: The license clarifies that users are "solely responsible for Outputs and their subsequent uses" (License, Section 6.d).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **VAE Quality Dependence**: The model's generation quality is highly dependent on the latent space of the pre-trained VAE (from SDXL). The developers note that they "will explore a better training paradigm for the VAE in the future" (Paper, p. 7).
*   **Acceleration Method Limitations**: The paper notes that some considered acceleration techniques have drawbacks. For instance, adversarial training can be unstable, and Latent Consistency Models may only be suitable for low-step generation, limiting flexibility (Paper, p. 12).
*   **Evolving Evaluation**: The evaluation protocol is subject to continuous improvement. Future plans include introducing new evaluation dimensions and improving efficiency with machine evaluations (Paper, p. 15).

### Recommendations:
*   **Adherence to License**: Users should carefully read and adhere to the **Tencent Hunyuan Community License Agreement**, especially the **Acceptable Use Policy**, to ensure responsible use (License, Section 5.a).
*   **Attribution**: When distributing the model or derivative works, users must provide a copy of the license and a "Notice" text file with the appropriate copyright information (License, Section 3). The developers also encourage users to mark products or services with "Powered by Tencent Hunyuan" (License, Section 3.c).
*   **Transparency**: The Acceptable Use Policy recommends that if machine-generated content is placed in a public context, it should be "expressly and conspicuously" identified as such (License, Exhibit A, item 11).
*   **Avoid Prohibited Uses**: Users must not use the model for any of the out-of-scope applications listed in the Intended Use section, particularly those involving high-stakes decisions, harassment, disinformation, or military purposes (License, Exhibit A).