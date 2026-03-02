## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Tencent Hunyuan (2405.08748.pdf, p. 1). The legal entity is THL A29 Limited, referred to as "Tencent" (LICENSE.txt, Section 1.i).

### Model date:
The Tencent Hunyuan Release Date is May 14, 2024 (LICENSE.txt). The associated academic paper was submitted on May 14, 2024 (2405.08748.pdf, p. 1).

### Model version:
Insufficient information.

### Model type:
Hunyuan-DiT is a text-to-image diffusion transformer model designed for generating high-quality, multi-resolution images from text prompts in both English and Chinese (2405.08748.pdf, p. 1).

**Architecture:**
*   The model is a diffusion model that operates in the latent space, using a pre-trained Variational Autoencoder (VAE) from SDXL to compress images (2405.08748.pdf, p. 7).
*   Its core is a diffusion transformer based on DiT, modified to use cross-attention for conditioning on text, similar to Stable Diffusion. The transformer architecture consists of encoder and decoder blocks containing self-attention, cross-attention, and feed-forward network modules. The decoder blocks also include a skip module for feature fusion, mimicking U-Net's skip connections (2405.08748.pdf, p. 7, Figure 7).
*   It employs a dual text encoder system, combining a bilingual (Chinese-English) CLIP and a multilingual T5 encoder to enhance language understanding and context length (2405.08748.pdf, p. 1, 7).
*   For multi-turn dialogue capabilities, the system uses a Multimodal Large Language Model (MLLM) based on the LlavaMistralForCausalLM architecture (2405.08748.pdf, p. 9; dialoggen/config.json.txt). This MLLM processes dialogue history to generate refined text prompts for the DiT model (2405.08748.pdf, p. 10, Figure 9).

**Model Size and Context Length:**
*   **Size:** The Hunyuan-DiT model has 1.5 billion parameters (2405.08748.pdf, p. 15). The dialogue generation component (MLLM) has a total size of approximately 15.13 GB (dialoggen/model.safetensors.index.json.txt).
*   **Context Length:** The model supports text understanding up to 256 tokens (2405.08748.pdf, p. 6). The MLLM component has a tokenizer model max length of 4096 (dialoggen/config.json.txt).

### Training details:
The model was trained using a latent diffusion approach with several key techniques and methodologies:

*   **Algorithm:** The model is trained as a diffusion model in the latent space of a pre-trained VAE. The training objective uses v-prediction (2405.08748.pdf, p. 7).
*   **Positional Encoding:** It uses a two-dimensional Rotary Positional Embedding (RoPE) to encode both absolute and relative positional information. For handling multi-resolution training data, a "Centralized Interpolative Positional Encoding" strategy is used to align images of different resolutions into a shared positional space, which improves learning efficiency (2405.08748.pdf, p. 7-8).
*   **Training Stability:** To ensure stable training, the following techniques were applied (2405.08748.pdf, p. 8):
    1.  **QK-Norm:** Layer normalization is added to all attention modules before computing queries (Q), keys (K), and values (V).
    2.  Layer normalization is also added after the skip module in the decoder blocks to prevent loss explosion.
    3.  Certain operations, like layer normalization, are switched to full precision (FP32) to avoid numerical overflow issues that can occur with FP16.
*   **Optimization:** The training process was accelerated using ZeRO, flash-attention, multi-stream asynchronous execution, activation checkpointing, and kernel fusion (2405.08748.pdf, p. 12).

### Paper or other resource for more information:
*   **Academic Paper:** "Hunyuan-DiT : A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding" provides a comprehensive overview of the model's architecture, data pipeline, and evaluation (2405.08748.pdf).
*   **Repositories:** Code and pretrained models are publicly available at:
    *   GitHub: `github.com/Tencent/HunyuanDiT` (2405.08748.pdf, p. 1)
    *   Hugging Face: `https://huggingface.co/Tencent-Hunyuan/HunyuanDiT` (LICENSE.txt, Section 1.j)

### Citation details:
The following BibTeX citation is provided for referencing the model (2405.08748.pdf, p. 21):
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

### License:
The model is released under the **Tencent Hunyuan Community License Agreement** (LICENSE.txt).

Key terms of the license include:
*   **Grant:** A non-exclusive, worldwide, non-transferable, and royalty-free limited license is granted to use, reproduce, distribute, and create derivative works of the model and materials (LICENSE.txt, Section 2).
*   **Distribution:** When distributing the model or its derivatives, you must provide a copy of the license agreement, include notices of any modifications, and add a "Notice" text file with the required copyright and license information. Users are encouraged to publish a blog post about their experience and mark products as "Powered by Tencent Hunyuan" (LICENSE.txt, Section 3).
*   **Commercial Use:** If the monthly active users (MAU) of all products or services using the model exceed 100 million, a separate commercial license must be requested from Tencent (LICENSE.txt, Section 4).
*   **Restrictions:** Usage must comply with the **Acceptable Use Policy**, which prohibits use for illegal activities, harming minors, military purposes, generating false information, and other unethical applications. The model's outputs cannot be used to improve any other large language model (other than Hunyuan or its derivatives) (LICENSE.txt, Section 5 and Exhibit A).
*   **Third-Party Components:** The model distribution includes third-party components under various open-source licenses (e.g., Apache 2.0, BSD, MIT), and users must comply with their respective terms (Notice.txt).

### Contact:
For questions or feedback, the corresponding author of the paper can be contacted at: `qinglinlu@tencent.com` (2405.08748.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Hunyuan-DiT is designed for high-quality, multi-resolution text-to-image generation with a strong understanding of both English and Chinese prompts (2405.08748.pdf, p. 1).

Its primary capabilities include:
*   **Text-to-Image Generation:** Generating images from detailed text descriptions. The model excels at understanding fine-grained details, abstract concepts, and Chinese cultural elements like ancient poetry and cuisine (2405.08748.pdf, p. 1, 6).
*   **Multi-turn Dialogue:** Engaging in interactive, multi-turn conversations with users to iteratively generate and refine images. Users can provide follow-up instructions to modify an existing image, such as changing the background, altering an object's material, or adding new elements (2405.08748.pdf, p. 1, 6, Figure 5).
*   **Prompt Enhancement:** The system can take simple or abstract user prompts (e.g., "a man from Qi who was haunted by the fear that the sky might fall") and enhance them into detailed, descriptive prompts suitable for generating high-quality images (2405.08748.pdf, p. 16, Figure 14).

The model takes a text prompt as input and outputs a generated image. In a dialogue context, it can also take the previous image and a new text instruction as input (2405.08748.pdf, p. 10, Figure 9).

### Primary intended users:
The model is intended for a broad audience, including natural persons and legal entities such as researchers, developers, and businesses who wish to incorporate advanced text-to-image generation into their applications and workflows (LICENSE.txt, Section 1.e; 2405.08748.pdf, p. 18).

### Out-of-scope uses:
The model is not designed for and must not be used for applications listed in the Acceptable Use Policy. Any use that violates laws or regulations is strictly prohibited. Out-of-scope uses include, but are not limited to (LICENSE.txt, Exhibit A):
*   Military purposes.
*   Generating or disseminating verifiably false information with the intent to harm others or influence elections.
*   Harming or exploiting minors.
*   Impersonating another individual without consent.
*   Making high-stakes automated decisions in domains affecting an individual's safety, rights, or well-being (e.g., law enforcement, medicine, credit, employment).
*   Discriminating against or harming individuals or groups based on protected characteristics.
*   Generating or disseminating malware.
*   Using the model or its outputs to improve any other large language model (other than Hunyuan-DiT or its derivatives) (LICENSE.txt, Section 5.b).

---

## How to Use
This section outlines how to use the model. 

The repository does not provide specific code snippets for direct use. However, the intended usage can be inferred from the paper's examples. The model functions as a text-to-image generator that can operate in a single-turn or multi-turn dialogue mode.

**Input-Output Structure:**
*   **Input:** A text prompt describing the desired image in English or Chinese. The prompt can be a simple phrase or a long, detailed paragraph (2405.08748.pdf, p. 1, 4). In a multi-turn setting, the input also includes the context of the previous conversation and generated image (2405.08748.pdf, p. 10).
*   **Output:** A generated image that corresponds to the input prompt.

**Example Usage (Multi-turn Dialogue):**
The following example illustrates the model's ability to refine an image over a multi-turn conversation (2405.08748.pdf, p. 6, Figure 5):

1.  **User Turn 1:** "Please draw a wooden bird and place it on a branch."
    *   **Model Output:** An image of a wooden bird on a branch.
2.  **User Turn 2:** "Change the bird's material to glass."
    *   **Model Output:** An image of a glass bird on a branch, maintaining the composition of the previous image.
3.  **User Turn 3:** "Now replace the bird in the picture with a ceramic texture."
    *   **Model Output:** An image of a ceramic bird on a branch.

This demonstrates the model's capacity to understand contextual instructions and perform iterative edits on a generated image.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by the content and style of the input prompts. The development process specifically focused on the following factors (2405.08748.pdf, p. 9):
*   **Subject:** The main subject of the image, covering a wide range of categories such as humans, landscapes, plants, animals, goods, and transportation.
*   **Style:** The artistic style of the generated image, including anime, 3D, painting, realistic, and traditional styles.
*   **Scene and Composition:** The background, setting, and layout of the elements within the image.
*   **Language:** The model is designed to understand both English and Chinese prompts.

### Evaluation factors:
During evaluation, the model's performance was analyzed and reported based on the following factors (2405.08748.pdf, p. 12):
*   **Text-image consistency:** How well the generated image matches the text prompt.
*   **AI artifacts:** The presence of visual distortions or unrealistic elements.
*   **Subject clarity:** The clarity and recognizability of the main subject in the image.
*   **Overall aesthetics:** The artistic quality and visual appeal of the image.
*   **Instruction compliance (for multi-turn):** How well the model follows user instructions in a dialogue.
*   **Subject consistency (for multi-turn):** The ability to maintain the identity of a subject across multiple edits.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using both automated metrics and a comprehensive human evaluation protocol:
*   **Human Evaluation:** The primary performance measure is a "pass rate" derived from human assessments. Multiple professional evaluators independently judge generated images across four dimensions: text-image consistency, AI artifacts, subject clarity, and overall aesthetics. An image is considered "acceptable" by an evaluator if it meets a certain quality standard. The pass rate for a prompt is the percentage of evaluators who deem the image acceptable (2405.08748.pdf, p. 13).
*   **Automated Metrics:** For ablation studies and quantitative comparisons, the following standard metrics were used (2405.08748.pdf, p. 16):
    *   **Frechet Inception Distance (FID):** A measure of image quality and diversity. Lower scores are better.
    *   **CLIP Score:** A measure of the semantic similarity between the text prompt and the generated image. Higher scores are better.

### Decision thresholds:
For human evaluation, the pass rate for a single prompt is calculated by aggregating the binary "acceptable" or "unacceptable" judgments from multiple evaluators. For example, "if 10 evaluators are involved and 7 of them consider the image acceptable, the pass rate for that prompt is 70%" (2405.08748.pdf, p. 13). The paper does not specify the exact criteria for an individual evaluator to mark an image as "acceptable."

### Variation approaches:
To ensure robust measurements and mitigate subjective bias, the following approaches were used (2405.08748.pdf, p. 13-14):
*   **Multi-Person Correction:** Multiple evaluators (from a team of over 50) independently assess the same set of images. The results are then aggregated to calculate pass rates.
*   **Hierarchical Aggregation:**
    1.  **Level-2 Category Scores:** The average of pass rates for all prompts within a subcategory (e.g., "Animals") is calculated.
    2.  **Level-1 Category Scores:** The average of the scores of all subordinate level-2 categories is taken.
    3.  **Overall Pass Rate:** A final overall score is calculated as a weighted average of the level-1 category scores. The weights are determined through discussions with users, designers, and experts.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
Two main types of datasets were used for evaluation:
1.  **Custom Human Evaluation Dataset:** A hierarchical dataset constructed specifically for this model. It contains over 3,000 prompts categorized into three difficulty levels (easy, medium, hard). The dataset is structured into 8 level-1 categories and over 70 level-2 categories, covering areas like functional applications, character roles, Chinese elements, and artistic styles. Each level-2 category contains 30-50 prompts. The prompts were created through a combination of AI generation (using LLMs) and human creation (2405.08748.pdf, p. 12-13).
2.  **MS COCO 2014 Validation Set:** For automated metric-based evaluations (FID and CLIP score), 30,000 images were generated using prompts from the MS COCO validation dataset. The generated images were 256x256 resolution (2405.08748.pdf, p. 16).

### Motivation:
*   The **custom dataset** was created to "holistically evaluate the generation ability" of the model across a wide and diverse range of scenarios relevant to user needs and expert opinions. The hierarchical structure and difficulty levels allow for a fine-grained analysis of the model's strengths and weaknesses (2405.08748.pdf, p. 12-13).
*   The **MS COCO dataset** was chosen for ablation studies as it is a standard and widely used benchmark in text-to-image generation research, allowing for direct comparison with prior work (2405.08748.pdf, p. 16).

### Preprocessing:
Insufficient information.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data was sourced and processed through a comprehensive, multi-stage pipeline (2405.08748.pdf, p. 8, Figure 20).
*   **Sources:** Data was acquired from "external purchasing, open data downloading, and authorized partner data" (2405.08748.pdf, p. 8).
*   **Structure (Data Layering):** The data is organized into a hierarchical structure based on quality:
    *   **Copper-Tier:** Billions of image-text pairs used to train foundational models like CLIP.
    *   **Silver-Tier:** A large, relatively high-quality subset screened from the copper-tier data, used for training the main generative model.
    *   **Gold-Tier:** The highest quality data, curated through machine screening and manual annotation, used for refining and optimizing the generative model (2405.08748.pdf, p. 9).
*   **Diversity:** The data covers a wide range of categories, including over ten thousand sub-categories for "Subject" (e.g., human, landscape, animals) and over a hundred styles for "Style" (e.g., anime, 3D, painting, realistic) (2405.08748.pdf, p. 9, Figure 18, Figure 19).

### Motivation:
The data pipeline was built from scratch to "update and evaluate data for iterative model optimization" (2405.08748.pdf, p. 1). The layered approach allows for efficient use of vast quantities of web-scale data for foundational understanding, while using progressively cleaner, higher-quality data to refine the final image generation quality and language understanding capabilities (2405.08748.pdf, p. 9). The focus on broad category coverage is to improve the model's versatility and appeal to users (2405.08748.pdf, p. 9).

### Preprocessing:
The raw data undergoes a significant preprocessing and refinement pipeline:
*   **Data Interpretation:** Raw data is automatically tagged with over ten types of labels, including image clarity, aesthetics, toxicity (indecency, violence), presence of watermarks, image classification, and image description (2405.08748.pdf, p. 8, Figure 20).
*   **Caption Refinement:** A key preprocessing step is to improve the quality of text captions associated with images. This is done using a specially trained Multimodal Large Language Model (MLLM). The MLLM generates new, more comprehensive "structural captions" by incorporating world knowledge. This is achieved through two methods (2405.08748.pdf, p. 9-10):
    1.  **Tag Injection:** Expert models (e.g., object detectors, landmark classifiers) and human labelers provide tags (e.g., "Shanghai Bund", "Close-up"). The MLLM then generates a descriptive caption that incorporates these tags.
    2.  **Raw Caption Fusion:** The MLLM takes both the image and its original (often noisy) raw caption as input to generate a corrected, higher-quality caption.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was compared against other open-source and closed-source models using a human evaluation protocol. The results are presented as pass rates (%) for four key dimensions (2405.08748.pdf, p. 16, Table 1).

**Hunyuan-DiT Performance:**
*   **Text-Image Consistency:** 74.2%
*   **Excluding AI Artifacts:** 74.3%
*   **Subject Clarity:** 95.4%
*   **Aesthetics:** 86.6%
*   **Overall:** 59.0%

These scores represent the highest performance among the open-source models evaluated (Playground 2.5, PixArt-α, SDXL) across all four dimensions (2405.08748.pdf, p. 16, Table 1).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
The paper notes that "Deploying Hunyuan-DiT for the users is expensive." To improve inference efficiency, multiple optimization strategies are used, including ONNX graph optimization, kernel optimization, operator fusion, precomputation, and GPU memory reuse. However, specific hardware requirements (e.g., VRAM, CPU) are not provided (2405.08748.pdf, p. 12).

### Training or Fine-tuning Requirements:
The paper states that training requires a "massive amount of image data" and involves a "large number of model parameters." To manage these demands, the training process was optimized with techniques such as ZeRO (for memory optimization), flash-attention, and activation checkpointing. Specific hardware configurations (e.g., number and type of GPUs, training time) are not detailed (2405.08748.pdf, p. 12).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Risk Mitigation in Development:** The data processing pipeline includes a "Toxicity Detection" stage to filter for indecency, vulgarity, and violence in the training data (2405.08748.pdf, p. 8, Figure 20). During evaluation, any generated images that raise safety concerns (e.g., pornography, politics, violence, bloodshed) are marked as "unacceptable" (2405.08748.pdf, p. 12).
*   **Risks in Model Usage and Mitigation:** The model's usage is governed by a detailed **Acceptable Use Policy** which aims to prevent misuse and mitigate potential harm. This policy is an integral part of the license agreement (LICENSE.txt, Section 5.a).
*   **Prohibited Uses:** The policy explicitly forbids using the model for activities that are illegal, harmful, or unethical. This includes, but is not limited to:
    *   Exploiting or harming minors.
    *   Generating or disseminating verifiably false information to harm others or influence elections.
    *   Intentionally defaming, disparaging, or harassing others.
    *   Generating malware.
    *   Discriminating against individuals or groups based on protected characteristics.
    *   Military purposes.
    *   Making high-stakes automated decisions in sensitive domains like law enforcement, medicine, or employment (LICENSE.txt, Exhibit A).
*   **Sensitive Data:** The repository does not specify whether sensitive personal data was used in training. However, given that data was acquired from broad sources including "open data downloading," it is possible that such data was present in the raw datasets (2405.08748.pdf, p. 8). The data filtering and interpretation steps are designed to mitigate risks associated with this (2405.08748.pdf, p. 8, Figure 20).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **VAE Limitations:** The model uses the VAE from SDXL. The authors note that while this VAE improves clarity and reduces over-saturation compared to older versions, they "will explore a better training paradigm for the VAE in the future," indicating a potential area for improvement (2405.08748.pdf, p. 7).
*   **Evolving Evaluation:** The evaluation protocol is under continuous optimization. The developers plan to introduce new evaluation dimensions, add more in-depth analysis to feedback (e.g., marking specific distortion locations), and improve efficiency by using machine evaluations in the future (2405.08748.pdf, p. 15).

### Recommendations:
*   Users should adhere strictly to the **Acceptable Use Policy** outlined in the license to prevent misuse and potential harm (LICENSE.txt, Exhibit A).
*   When distributing the model or derivative works, users are encouraged to:
    *   Publish a technology introduction blog post or public statement about their experience using the model.
    *   Mark any products or services developed with the model to indicate that they are "Powered by Tencent Hunyuan" (LICENSE.txt, Section 3.c).
*   The paper itself is presented as a "useful recipe for the community to train better text-to-image models," suggesting that the described methods for data processing, model architecture, and training can serve as best practices for other developers (2405.08748.pdf, p. 18).

---