## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Tencent Hunyuan (2405.08748.pdf, p. 1). The legal entity is THL A29 Limited, a Tencent company (LICENSE.txt, Section 1.i; Notice.txt). The development team includes Zhimin Li, Jianwei Zhang, Qin Lin, and numerous other contributors listed in the research paper (2405.08748.pdf, p. 1).

### Model date:
The Tencent Hunyuan release date is May 14, 2024 (LICENSE.txt). The associated research paper was also submitted on May 14, 2024 (2405.08748.pdf, p. 1).

### Model version:
The model is presented as Hunyuan-DiT in the associated paper (2405.08748.pdf, p. 1). It is a state-of-the-art text-to-image model with a strong understanding of both Chinese and English, and it supports multi-turn dialogue for interactive image generation and refinement (2405.08748.pdf, p. 1, 6).

### Model type:
Hunyuan-DiT is a text-to-image diffusion transformer model that operates in the latent space (2405.08748.pdf, p. 1, 7).

*   **Architecture:** It is based on the Diffusion Transformer (DiT) architecture, modified to use cross-attention for text conditioning, similar to Stable Diffusion (2405.08748.pdf, p. 7, Figure 7). The transformer blocks are divided into encoder and decoder blocks, with the decoder blocks including a skip module to fuse information from the encoder stage, mimicking U-Net's skip-connections (2405.08748.pdf, p. 7). It uses a two-dimensional Rotary Positional Embedding (RoPE) for positional encoding (2405.08748.pdf, p. 7).
*   **Components:**
    *   **VAE (Variational Autoencoder):** A pre-trained VAE from SDXL is used to compress images into a low-dimensional latent space (2405.08748.pdf, p. 7).
    *   **Text Encoders:** It combines two text encoders to enhance language understanding: a bilingual (Chinese-English) CLIP and a multilingual T5 encoder (2405.08748.pdf, p. 1, 7).
*   **Model Size:** The model has 1.5 billion parameters (2405.08748.pdf, p. 15).
*   **Context Length:** The model supports long text understanding up to 256 tokens (2405.08748.pdf, p. 6).

### Training details:
The model was trained using a comprehensive pipeline involving specialized data processing and advanced training techniques.

*   **Training Paradigm:** The model is trained as a latent diffusion model using v-prediction, which was found to yield better empirical performance (2405.08748.pdf, p. 7).
*   **Training Stability:** To stabilize training, three techniques were employed (2405.08748.pdf, p. 8):
    1.  **QK-Norm:** Layer normalization is added to all attention modules before computing queries, keys, and values.
    2.  Layer normalization is added after the skip module in the decoder blocks to prevent loss explosion.
    3.  Certain operations, like layer normalization, are switched to FP32 to avoid numerical errors that occur with FP16.
*   **Data Pipeline:** A four-stage data pipeline was built from scratch (2405.08748.pdf, p. 8, Figure 20):
    1.  **Data Acquisition:** Data was sourced from external purchasing, open data downloading, and authorized partners.
    2.  **Data Interpretation:** Raw data was tagged for attributes like image clarity, aesthetics, toxicity, and image content.
    3.  **Data Layering:** Data was structured into tiers. Billions of image-text pairs ("copper-tier") were used to train a foundational CLIP model. A higher-quality "silver-tier" was used for training the generative model, and the highest quality "gold-tier" was used for refinement.
    4.  **Data Application:** Data was used for iterative model optimization through a 'data convoy' mechanism.
*   **Caption Refinement:** To improve data quality, a Multimodal Large Language Model (MLLM) was used to re-caption raw image-text pairs with more comprehensive, structural descriptions, injecting world knowledge through tag injection and raw caption correction (2405.08748.pdf, p. 9-10).
*   **Efficiency Optimization:** Training speed was enhanced using ZeRO, flash-attention, multi-stream asynchronous execution, activation checkpointing, and kernel fusion (2405.08748.pdf, p. 12).

### Paper or other resource for more information:
*   **Research Paper:** A detailed description of the model, its architecture, training process, and evaluation is available in the paper: "Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding" (2405.08748.pdf).
*   **Repository:** The code and pretrained models are publicly available at: `github.com/Tencent/HunyuanDiT` (2405.08748.pdf, p. 1).

### Citation details:
```bibtex
@misc{li2024hunyuandit,
      title={Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding}, 
      author={Zhimin Li and Jianwei Zhang and Qin Lin and Jiangfeng Xiong and Yanxin Long and Xinchi Deng and Yingfang Zhang and Xingchao Liu and Minbin Huang and Zedong Xiao and Dayou Chen and Jiajun He and Jiahao Li and Wenyue Li and Chen Zhang and Rongwei Quan and Jianxiang Lu and Jiabin Huang and Xiaoyan Yuan and Xiaoxiao Zheng and Yixuan Li and Jihong Zhang and Chao Zhang and Meng Chen and Jie Liu and Zheng Fang and Weiyan Wang and Jinbao Xue and Yangyu Tao and Jianchen Zhu and Kai Liu and Sihuan Lin and Yifu Sun and Yun Li and Dongdong Wang and Mingtao Chen and Zhichao Hu and Xiao Xiao and Yan Chen and Yuhong Liu and Wei Liu and Di Wang and Yong Yang and Jie Jiang and Qinglin Lu},
      year={2024},
      eprint={2405.08748},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(2405.08748.pdf)

### License:
The Tencent Hunyuan Works are licensed under the "Tencent Hunyuan Community License Agreement" (LICENSE.txt).

*   **Permissions:** You are granted a non-exclusive, worldwide, non-transferable, and royalty-free limited license to use, reproduce, distribute, create derivative works of (including Model Derivatives), and modify the Materials (LICENSE.txt, Section 2).
*   **Distribution Conditions:** When distributing the Tencent Hunyuan Works, you must provide a copy of the license, include notices of any modifications, and include a "Notice" text file with the specified copyright and license information (LICENSE.txt, Section 3).
*   **Commercial Use:** If the monthly active users (MAU) of your products or services using the model exceed 100 million, you must request a separate commercial license from Tencent (LICENSE.txt, Section 4).
*   **Restrictions:** Your use must comply with the "Acceptable Use Policy" (detailed in the Out-of-scope uses section). You must not use the model or its outputs to improve any other large language model (other than Hunyuan-DiT or its derivatives) (LICENSE.txt, Section 5).
*   **Third-Party Components:** The model distribution includes third-party components licensed under Apache 2.0, BSD 3-Clause, MIT, and HPND licenses. Users must comply with the terms of these original licenses (Notice.txt).

### Contact:
For questions or feedback, you can contact the corresponding author of the research paper: Qinglin Lu at `qinglinlu@tencent.com` (2405.08748.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Hunyuan-DiT is a text-to-image generative model designed for the following primary uses:

*   **High-Quality Image Generation:** Generating detailed, high-quality images in multiple resolutions from text prompts in both English and Chinese (2405.08748.pdf, p. 1).
*   **Chinese-to-Image Generation:** The model has a fine-grained understanding of Chinese prompts and excels at generating images with Chinese cultural elements, such as ancient poetry, idioms, and cuisine (2405.08748.pdf, p. 1, 6, Figure 1).
*   **Multi-Turn Dialogue and Image Refinement:** The model can engage in multi-turn, multimodal dialogue with users. It can generate an initial image and then iteratively refine it based on subsequent user instructions (e.g., "add a puppy," "change the background to a frozen polar region") (2405.08748.pdf, p. 1, 6, Figure 5, Figure 9).
*   **Prompt Enhancement:** The model's MLLM component can transform simple or abstract user instructions into detailed, semantically coherent text prompts to generate higher-quality images (2405.08748.pdf, p. 11, 16, Figure 14).

The input-output structure involves providing a text prompt (and optionally an image and dialogue history) to the model, which then outputs a generated image (2405.08748.pdf, p. 10, Figure 9).

### Primary intended users:
The model is intended for the open-source community, including researchers, developers, and other entities or individuals interested in text-to-image generation (2405.08748.pdf, p. 1; LICENSE.txt). The license is available to any "natural person or legal entity" (LICENSE.txt, Section 1.e), though commercial use at a very large scale (over 100 million monthly active users) requires a separate license (LICENSE.txt, Section 4).

### Out-of-scope uses:
Users must adhere to the Acceptable Use Policy, which prohibits using the model for the following purposes (LICENSE.txt, Exhibit A):

*   In any way that violates laws or regulations.
*   To harm oneself or others.
*   To generate or disseminate verifiably false information to harm others or influence elections.
*   To intentionally defame, disparage, or harass others.
*   To generate or disseminate malware.
*   To generate or disseminate personally identifiable information for harmful purposes.
*   For military purposes.
*   To make high-stakes automated decisions in domains like law enforcement, medicine, credit, employment, etc.
*   To perform, facilitate, or encourage violent extremism or terrorism.
*   For any use intended to discriminate against or harm individuals or groups based on protected characteristics.
*   To engage in the unauthorized or unlicensed practice of any profession (e.g., financial, legal, medical).
*   To improve any other large language model (other than Hunyuan-DiT or its derivatives) (LICENSE.txt, Section 5.b).

---

## How to Use
This section outlines how to use the model. 

The model and its code are publicly available at `github.com/Tencent/HunyuanDiT` (2405.08748.pdf, p. 1). While specific code snippets are not provided in the repository files, the intended usage can be understood from the paper's examples.

The model can be used for single-turn text-to-image generation or multi-turn interactive generation.

**Single-Turn Generation:**
Users provide a detailed text prompt in English or Chinese, and the model generates a corresponding image. The model can handle long, descriptive prompts and generate images with high fidelity to the text.

*   **Example Input (Chinese Prompt):** "一幅细致的油画描绘了一只年轻獾轻轻嗅着一朵明亮的黄色玫瑰时错综复杂的皮毛。背景是一棵大树干的粗糙纹理，獾的爪子轻轻地挖进树皮。在柔和的背景中，一个宁静的瀑布倾泻而下，它的水在绿色植物中闪烁着蓝色。" (2405.08748.pdf, p. 4)
*   **Example Input (English Prompt):** "A detailed oil painting captures the intricate fur of a young badger as it gently sniffs at a bright yellow rose. The scene is set against the rough texture of a large tree trunk, with the badger's claws slightly digging into the bark. In the softly painted background, a tranquil waterfall cascades down, its waters a shimmering blue amidst the greenery." (2405.08748.pdf, p. 4)
*   **Example Output:** An image corresponding to the detailed description. (See Figure 3 in 2405.08748.pdf, p. 4)

**Multi-Turn Interactive Generation:**
The model supports a conversational interface where users can iteratively refine an image.

*   **Step 1: Initial Generation**
    *   **User Input:** "设计一个城市夜景画面，画面主角是一只猫咪在屋顶上眺望远方的明亮城市，风格是写实风格。" (Design a city night scene. The protagonist of the picture is a cat on the roof looking at the bright city in the distance. The style is realistic.) (2405.08748.pdf, p. 6)
    *   **Model Output:** An image of a cat on a roof overlooking a city at night.
*   **Step 2: First Refinement**
    *   **User Input:** "请将背景更换为冰冻的极地，猫咪看向镜头。" (Please change the background to a frozen polar region and the cat looks at the camera.) (2405.08748.pdf, p. 6)
    *   **Model Output:** An image of the same cat, now looking at the camera, in a frozen polar environment.
*   **Step 3: Second Refinement**
    *   **User Input:** "现在请你将背景改为繁华的东京街景，其中包括高楼大厦。" (Now please change the background to a bustling Tokyo street scene, including high-rise buildings.) (2405.08748.pdf, p. 6)
    *   **Model Output:** An image of the same cat in a bustling Tokyo street scene.

This process is enabled by an MLLM that interprets the dialogue history and the user's new instruction to generate an updated, detailed prompt for the DiT model (2405.08748.pdf, p. 10, Figure 9).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The performance and output of the model are influenced by the composition of its training data. The developers identified two fundamental data categories as key factors (2405.08748.pdf, p. 9):

*   **Subject:** The main object or theme of the image. The training data covers a wide range of subjects, including human, landscape, plants, animals, goods, transportation, and games, with over ten thousand sub-categories (2405.08748.pdf, p. 9, 22, Figure 18).
*   **Style:** The artistic or visual style of the image. The model was trained on over a hundred styles, including anime, 3D, painting, realistic, and traditional styles (2405.08748.pdf, p. 9, 23, Figure 19).

The model's ability to generate specific subjects or styles accurately is dependent on their coverage in the training data.

### Evaluation factors:
During model evaluation, performance is analyzed and reported based on the following factors (2405.08748.pdf, p. 12):

*   **Text-Image Consistency:** How well the generated image matches the text prompt.
*   **AI Artifacts:** The presence of visual glitches or unnatural elements in the image.
*   **Subject Clarity:** The clarity and recognizability of the main subject in the image.
*   **Overall Aesthetics:** The general visual appeal and quality of the image.
*   **Multi-Turn Interaction:** For dialogue-based generation, additional factors are assessed:
    *   **Instruction Compliance:** How well the model follows the user's editing instructions.
    *   **Subject Consistency:** Whether the main subject remains consistent across multiple refinement steps.
    *   **Prompt Enhancement Performance:** The quality of the detailed prompts generated by the MLLM from user instructions.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is primarily assessed through a multi-dimensional human evaluation protocol (2405.08748.pdf, p. 12).

*   **Human Evaluation:** A team of over 50 professional evaluators assesses generated images across four dimensions: text-image consistency, AI artifacts, subject clarity, and overall aesthetics (2405.08748.pdf, p. 12-13). The core metric is the **Overall Pass Rate**, which is the weighted average of pass rates across different content categories. The pass rate for a single prompt is the percentage of evaluators who deem the generated image "acceptable" (2405.08748.pdf, p. 13-14).
*   **Automated Metrics:** For ablation studies, the following automated metrics are used (2405.08748.pdf, p. 16):
    *   **Frechet Inception Distance (FID):** Measures the quality and diversity of generated images compared to a reference dataset. Lower is better.
    *   **CLIP Score:** Measures the semantic correspondence between the text prompt and the generated image. Higher is better.

### Decision thresholds:
The evaluation protocol uses an "acceptability" threshold determined by human evaluators. For a given prompt, the pass rate is calculated as the percentage of evaluators who find the image acceptable. For example, if 7 out of 10 evaluators find an image acceptable, the pass rate is 70% (2405.08748.pdf, p. 13). This rate is then averaged across prompts and categories to derive final scores.

### Variation approaches:
To ensure robust measurements and mitigate subjective bias, the evaluation process includes a multi-person correction stage. In this stage, multiple evaluators independently assess the same set of images. The results are then aggregated and analyzed to produce a more objective score (2405.08748.pdf, p. 13). The overall pass rate is a weighted average of scores from different level-1 categories, with weights determined through discussion with users, designers, and experts (2405.08748.pdf, p. 14, 25, Table 2).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Two main types of datasets were used for evaluation:

1.  **Custom Hierarchical Evaluation Dataset:** A proprietary dataset constructed by combining AI-generated and human-created prompts. It contains over 3,000 prompts in total, structured in a 3-level hierarchy with 8 top-level categories and over 70 sub-categories (e.g., functional applications, character roles, Chinese elements, artistic styles) (2405.08748.pdf, p. 13). The prompts are also categorized by difficulty (easy, medium, hard) (2405.08748.pdf, p. 12).
2.  **MS COCO Validation Dataset:** For ablation studies, the standard MS COCO 2014 validation dataset was used. 30,000 images were generated at a 256x256 resolution from prompts in this dataset (2405.08748.pdf, p. 16).

### Motivation:
*   The custom hierarchical dataset was created to **holistically evaluate** the model's capabilities across a wide and diverse range of scenarios, including complex prompts and abstract semantics, which are common in real-world usage (2405.08748.pdf, p. 12-13). Relying on LLMs for prompt generation helped enhance diversity and difficulty while reducing manual labor (2405.08748.pdf, p. 12).
*   The MS COCO dataset was used for ablation studies to follow the **standard practice in prior research**, allowing for comparable and reproducible results when evaluating different model variants (2405.08748.pdf, p. 16).

### Preprocessing:
The custom evaluation prompts were constructed by combining "bad cases" and "business needs" based on the data category system. The usability of these prompts was assured through human annotation, which checked for reasonableness, logic, and comprehensiveness (2405.08748.pdf, p. 9).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was prepared using a comprehensive, multi-stage pipeline (2405.08748.pdf, p. 8-9).

*   **Source:** Data was acquired from external purchasing, open data downloading, and authorized partners (2405.08748.pdf, p. 8).
*   **Structure and Size:** The data is structured in a hierarchical, multi-tier system:
    *   **Copper-Tier:** Billions of image-text pairs used to train a foundational bilingual CLIP model.
    *   **Silver-Tier:** A relatively high-quality subset screened from the copper-tier, used to train the main generative model.
    *   **Gold-Tier:** The highest quality data, selected through machine screening and manual annotation, used for model refinement and optimization.
*   **Diversity:** The data covers a vast range of categories, including over ten thousand sub-categories for subjects (e.g., human, landscape, animals) and over a hundred styles (e.g., anime, 3D, painting, realistic) (2405.08748.pdf, p. 9, 22-23, Figures 18 & 19).
*   **Multi-Turn Dialogue Data:** A specific dataset of ~15,000 samples was generated using GPT-4 to train the model for multi-turn dialogue capabilities. This dataset covers 13 topics and 7 image editing methods (2405.08748.pdf, p. 11, Figure 10).

### Motivation:
The goal of the data pipeline was to construct a large-scale, high-quality, and diverse dataset crucial for training an accurate text-to-image model with fine-grained understanding of both English and Chinese (2405.08748.pdf, p. 9). The tiered approach allows for efficient use of data at different stages of training, from foundational model pre-training to fine-grained optimization (2405.08748.pdf, p. 8-9).

### Preprocessing:
The training data underwent extensive preprocessing and refinement (2405.08748.pdf, p. 8-10):

*   **Initial Processing:** Raw data was preprocessed through deduplication, video extraction, and chopping (2405.08748.pdf, p. 24, Figure 20).
*   **Data Interpretation:** Data was automatically tagged for over ten attributes, including image clarity, aesthetics, toxicity (indecency, violence), watermarks, and content classification (2405.08748.pdf, p. 8).
*   **Caption Refinement:** A key step was improving the quality of text captions. A fine-tuned Multimodal Large Language Model (MLLM) was used to re-caption raw image-text pairs. This process included:
    *   **Structural Captioning:** Generating comprehensive, descriptive captions.
    *   **Tag Injection:** Using tags from expert models (e.g., object detectors, landmark classifiers) or human labels to inject specific world knowledge into the captions.
    *   **Raw Caption Fusion:** Correcting noisy raw captions by taking image information into account.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model was evaluated against other open-source and closed-source models on a custom evaluation set. The performance was measured by the pass rate (%) across four dimensions, as assessed by human evaluators.

**Hunyuan-DiT Performance:** (2405.08748.pdf, p. 16, Table 1)
*   **Text-Image Consistency:** 74.2%
*   **Excluding AI Artifacts:** 74.3%
*   **Subject Clarity:** 95.4%
*   **Aesthetics:** 86.6%
*   **Overall:** 59.0%

These scores were the highest among all compared open-source models (Playground 2.5, PixArt-α, SDXL) across all four dimensions (2405.08748.pdf, p. 15-16, Table 1). A radar chart also visualizes this comparison, showing Hunyuan-DiT's strong performance relative to other open-source models like Stable Diffusion 3, Playground 2.5, and Stable Diffusion XL (asset/radar.png).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
The paper notes that deploying Hunyuan-DiT is "expensive" and that engineering optimization strategies were adopted to improve inference efficiency, including ONNX graph optimization, kernel optimization, operator fusion, precomputation, and GPU memory reuse (2405.08748.pdf, p. 12). Specific hardware requirements are not provided.

### Training or Fine-tuning Requirements:
Training the model requires significant computational resources due to the large number of parameters (1.5B) and the massive amount of image data (2405.08748.pdf, p. 12, 15). The training process utilized techniques to manage memory and speed, such as ZeRO for memory optimization and flash-attention (2405.08748.pdf, p. 12). However, specific hardware configurations (e.g., number/type of GPUs, VRAM requirements) are not specified.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Risk Mitigation in Development:** The developers implemented several measures to promote safe use. The data processing pipeline includes a "Toxicity Detection" stage to filter for indecency, vulgarity, and violence in the training data (2405.08748.pdf, p. 8, 24, Figure 20). The evaluation protocol also explicitly marks any generated content that raises safety concerns (e.g., involving pornography, politics, violence, or bloodshed) as "unacceptable" (2405.08748.pdf, p. 12).
*   **Risks in Model Usage:** The license agreement includes a comprehensive "Acceptable Use Policy" that outlines known risks and misuse cases. Users are prohibited from using the model to (LICENSE.txt, Exhibit A):
    *   Generate or disseminate verifiably false information with the intent to harm others or influence elections.
    *   Intentionally defame, disparage, or harass others.
    *   Generate content for the purpose of harming electronic systems (e.g., malware).
    *   Discriminate against or harm individuals or groups based on protected characteristics.
    *   Perform, facilitate, or encourage violent extremism or terrorism.
    *   Make high-stakes automated decisions in sensitive domains such as law enforcement, medicine, credit, or employment.
    *   Use for military purposes.
*   **Affected Groups:** The use restrictions aim to protect various groups from potential harm, including minors, individuals targeted by false information or harassment, and groups vulnerable to discrimination based on age, social, physical, or mental characteristics (LICENSE.txt, Exhibit A).
*   **Sensitive Data:** The model was trained on data from various sources, including open data downloads and external purchasing (2405.08748.pdf, p. 8). While not explicitly stated, this data may contain personal or sensitive information, which is why toxicity and content filtering were part of the data pipeline. The Acceptable Use Policy prohibits generating or disseminating personally identifiable information with the purpose of harming others (LICENSE.txt, Exhibit A).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **VAE Limitations:** The model uses a pre-trained VAE from SDXL. While this improved performance over previous versions, the developers note that they "will explore a better training paradigm for the VAE in the future," indicating that the VAE's latent space may still be a limiting factor for generation quality (2405.08748.pdf, p. 7).
*   **Evaluation Gaps:** The developers plan to continuously evolve their evaluation protocol by "introducing new evaluation dimensions" and "adding in-depth analysis in the evaluation feedback," suggesting that the current evaluation may not capture all aspects of model performance (2405.08748.pdf, p. 15).
*   **Deployment Cost:** Deploying the model is described as "expensive," which may be a limitation for users with limited computational resources (2405.08748.pdf, p. 12).

### Recommendations:
*   **Adherence to Use Policy:** Users must use the model in accordance with the "Tencent Hunyuan Community License Agreement" and the "Acceptable Use Policy" to prevent misuse and potential harm (LICENSE.txt, Section 5.a).
*   **Attribution:** Users who distribute or create services with the model are encouraged to indicate that their product/service is "Powered by Tencent Hunyuan" (LICENSE.txt, Section 3.c).
*   **Community Feedback:** Users are encouraged to share their experience by publishing blog posts or public statements, which can contribute to the broader understanding and development of the model (LICENSE.txt, Section 3.c).
*   **Commercial Licensing:** Organizations with products or services that have over 100 million monthly active users must request a separate commercial license from Tencent before using the model (LICENSE.txt, Section 4).

---