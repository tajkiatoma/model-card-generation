## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh (2405.02246.pdf, p. 1). The developers are affiliated with Hugging Face and Sorbonne Université (2405.02246.pdf, p. 1).

### Model date:
The academic paper describing the model was submitted on May 3, 2024 (2405.02246.pdf, p. 1). The developers also mention removing opted-out content from the training data in January 2024 (2405.02246.pdf, p. 6).

### Model version:
The model is named Idefics2 (2405.02246.pdf, p. 1). It is an 8-billion parameter vision-language model that improves upon previous models by consolidating findings from extensive experiments on architecture, data, and training methods (2405.02246.pdf, p. 1). It achieves state-of-the-art performance in its size category and is more efficient at inference compared to its predecessor, Idefics1, and other models like OpenFlamingo (2405.02246.pdf, p. 6, 8). Base, instructed, and chat versions of the model have been released (2405.02246.pdf, p. 2).

### Model type:
Idefics2 is a foundational open-source Vision-Language Model (VLM) with 8 billion parameters (2405.02246.pdf, p. 1). It belongs to the category of conditional text generation models that can process both image and text inputs (config.json.txt; 2405.02246.pdf, p. 2).

**Architecture:**
The model uses a **fully autoregressive architecture**, where visual and text features are concatenated and fed into a language model decoder (2405.02246.pdf, p. 3; assets/Idefics2_flowchart.png). This architecture was chosen as it outperforms the cross-attention architecture when unimodal backbones are trained (2405.02246.pdf, p. 4). The core components are:
*   **Vision Encoder:** A pre-trained vision transformer, specifically SigLIP-SO400M, which processes input images (2405.02246.pdf, p. 6; config.json.txt). The vision model has 27 hidden layers, a hidden size of 1152, and 16 attention heads (config.json.txt). It supports image sizes up to 980x980 (config.json.txt).
*   **Vision-Language Connector:** This component bridges the vision and text modalities. It consists of:
    1.  A **Modality Projection** layer that maps vision features to the language model's embedding space (2405.02246.pdf, p. 3; assets/Idefics2_flowchart.png).
    2.  A **Perceiver Resampler** (pooling) that reduces the sequence of visual tokens to a fixed number (64 tokens in the standard configuration) to improve computational efficiency (2405.02246.pdf, p. 3, 5; processor_config.json.txt).
*   **Language Model (LLM) Decoder:** A pre-trained large language model, Mistral-7B-v0.1, which generates the text output based on the combined visual and text inputs (2405.02246.pdf, p. 6; config.json.txt). The text model has a vocabulary size of 32003 and supports a maximum position embedding of 32768 tokens (config.json.txt).

**Model Size:**
*   **Parameters:** 8 billion (2405.02246.pdf, p. 1).
*   **Total Size on Disk:** 33.61 GB (model.safetensors.index.json.txt).

### Training details:
The model was trained in multiple stages, starting from pre-trained SigLIP-SO400M (vision) and Mistral-7B-v0.1 (language) backbones (2405.02246.pdf, p. 6).

**Pre-training:**
The pre-training was decomposed into two stages to maximize compute efficiency:
1.  **Stage 1:** The model was trained with a max image resolution of 384 pixels and a global batch size of 2048. The data mixture was 70% interleaved image-text documents (OBELICS) and 30% image-text pairs (2405.02246.pdf, p. 7).
2.  **Stage 2:** The max image resolution was increased to 980 pixels. This stage introduced PDF documents into the training mixture, which consisted of 45% OBELICS, 35% image-text pairs, and 20% PDF documents (2405.02246.pdf, p. 7).

The entire model was trained during both stages, with some parameters adapted using **Low-Rank Adaptation (LoRA)** to stabilize training and improve expressivity, particularly for the fully autoregressive architecture (2405.02246.pdf, p. 4, 7). The training used a learning rate of 1e-4 for approximately 2 epochs, covering 1.5 billion images and 225 billion text tokens (2405.02246.pdf, p. 7).

**Instruction Fine-tuning:**
After pre-training, the base model was instruction-tuned on a massive collection of 50 vision-language datasets and several text-only instruction datasets, named "The Cauldron" (2405.02246.pdf, p. 8).
*   **Algorithm:** The fine-tuning was performed using **DoRA**, a variant of LoRA (2405.02246.pdf, p. 8).
*   **Techniques:** To prevent overfitting, the training employed **NEFTune** (adding noise to embeddings) and random scaling of image resolutions (2405.02246.pdf, p. 8). The loss was computed only on the answer tokens in the question-answer pairs (2405.02246.pdf, p. 8).

**Chat Fine-tuning:**
An instruction-tuned checkpoint was further fine-tuned for a few hundred steps on dialogue data (LLaVA-Conv, ShareGPT4V) to create the chat-optimized version (2405.02246.pdf, p. 9).

### Paper or other resource for more information:
*   **Academic Paper:** "What matters when building vision-language models?" by Laurençon et al. (2024). This paper details the experiments, architectural choices, training procedures, and evaluations that led to the development of Idefics2 (2405.02246.pdf).
*   **Model Repository:** The models and datasets are available on the Hugging Face Hub at `https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe` (2405.02246.pdf, p. 2).

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
Idefics2 is a versatile vision-language model designed for a wide range of multimodal tasks. The model takes images and text as interleaved inputs and outputs text (2405.02246.pdf, p. 2). Its primary capabilities include:
*   **Document Understanding:** Retrieving information from scanned PDFs and answering questions about them (2405.02246.pdf, p. 2, 7).
*   **Chart and Diagram Explanation:** Analyzing and explaining visual data representations (2405.02246.pdf, p. 2).
*   **Text Transcription (OCR):** Transcribing text from images (2405.02246.pdf, p. 2, 8).
*   **Object Counting:** Counting objects within a picture (2405.02246.pdf, p. 2).
*   **Code Generation from Screenshots:** Converting screenshots of webpages into functional code (2405.02246.pdf, p. 2).
*   **General Visual Question Answering (VQA):** Answering questions based on image content (2405.02246.pdf, p. 3).
*   **Image Captioning:** Generating descriptive captions for images (2405.02246.pdf, p. 3).
*   **Visual Reasoning:** Performing tasks that require reasoning about visual information, such as solving mathematical problems in visual contexts or spotting differences between images (2405.02246.pdf, p. 8).

The model can handle images in their original aspect ratio and at various resolutions, providing flexibility for different use cases (2405.02246.pdf, p. 5).

### Primary intended users:
The model is released as a resource for the VLM community, targeting researchers and developers in the field of artificial intelligence and machine learning (2405.02246.pdf, p. 2).

### Out-of-scope uses:
The model is not intended for applications where its potential for generating harmful, biased, or inaccurate content could cause harm. The developers identified several security risks and misuse cases during red-teaming exercises, which are out-of-scope for this model:
*   Generating content that promotes online harassment or offensive memes (2405.02246.pdf, p. 25).
*   Making judgments about individuals' professions, social status, or attractiveness based on visual appearance (2405.02246.pdf, p. 25).
*   Developing phishing schemes from screenshots of legitimate websites (2405.02246.pdf, p. 25).
*   Crafting guides for constructing explosives or manipulating firearms (2405.02246.pdf, p. 25).

Users should exercise critical thinking and discretion, as certain prompt formulations ("jailbreaks") can circumvent the model's safety mechanisms (2405.02246.pdf, p. 26).

---

## How to Use
This section outlines how to use the model. 

The model processes sequences of interleaved text and images. The input is formatted using a specific chat template.

**Chat Template:**
The following template is used to structure conversations with the model, including user queries and assistant responses with text and images (processor_config.json.txt):
```jinja
{% for message in messages %}{{message['role'].capitalize()}}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}<end_of_utterance>
{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}
```
Special tokens like `<image>` are used to denote image locations in the text, and `<end_of_utterance>` marks the end of a turn (special_tokens_map.json.txt).

**Example 1: Text Transcription** (2405.02246.pdf, p. 8)
*   **Input:**
    *   Image of a handwritten letter.
    *   Prompt: `<image>The content of the letter is:\n`
*   **Output:**
    *   `Dear Craig, Actually, I've never been big on letter writing, though it is nice to receive a hand written note from someone. I am afraid that the art of drawing, and the related ability to sketch an idea, are also being lost. But perhaps, as the cliche goes, what goes around comes around. Good luck with your project. Tom Cianfichi`

**Example 2: Chart Analysis and Calculation** (2405.02246.pdf, p. 1)
*   **Input:**
    *   Image of a financial table with data for 2014 and 2015.
    *   Prompt: `For 2024, the interest expense is twice what it was in 2014, and the long-term debt is 10% higher than its 2015 level. Can you calculate the combined total of the interest and long-term debt for 2024?`
*   **Output:**
    *   `Yes, I can help you calculate that. First, let's find out the interest expense for 2024: Interest Expense (2024) = 2 * Interest Expense (2014) = 2 * 630 = 1260. Next, let's find the long-term debt for 2024: Long-Term Debt (2024) = Long-Term Debt (2015) + 10% of Long-Term Debt (2015) = 19,260 + 0.1 * 19,260 = 19,260 + 1,926 = 21,186. Now, we can add these two amounts together to get the combined total of the interest and long-term debt for 2024: Combined Total (2024) = Interest Expense (2024) + Long-Term Debt (2024) = 1260 + 21,186 = 22,446. So, the combined total of the interest and long-term debt for 2024 is $22,446.`

**Example 3: Structured Data Extraction** (2405.02246.pdf, p. 24)
*   **Input:**
    *   Image of a resume.
    *   Prompt: `Extract the name, email, current job, and education. Output a JSON format.`
*   **Output:**
    *   A JSON object containing the extracted information for "name", "email", "current_job", and a list of "education" entries with "year", "degree", and "university".

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development paper identifies several key factors that influence the model's performance:
*   **Quality of Pre-trained Backbones:** The performance of the final VLM is highly dependent on the quality of the unimodal vision and language model backbones. The quality of the language model was found to have a higher impact than the quality of the vision backbone for a fixed parameter count (2405.02246.pdf, p. 4).
*   **Model Architecture:** The choice between a fully autoregressive architecture and a cross-attention architecture significantly impacts performance, training stability, and inference cost (2405.02246.pdf, p. 4).
*   **Backbone Training Method:** Whether the pre-trained unimodal backbones are kept frozen or fine-tuned (e.g., using LoRA) during multimodal training is a critical factor. Unfreezing the backbones with LoRA was found to significantly improve performance (2405.02246.pdf, p. 4).
*   **Number of Visual Tokens:** The quantity of visual tokens per image (controlled by the perceiver resampler) affects both computational efficiency and downstream performance (2405.02246.pdf, p. 5).
*   **Image Processing:** Strategies for handling image resolution and aspect ratio (e.g., resizing to fixed squares vs. preserving original aspect ratio) impact performance, especially on OCR tasks, as well as memory usage (2405.02246.pdf, p. 5).
*   **Data Mixture:** The composition of the training data, including the mix of interleaved documents, image-text pairs, and specialized data like PDFs, is crucial for developing specific capabilities like OCR (2405.02246.pdf, p. 6-7).

### Evaluation factors:
The evaluation factors analyzed are the same as the relevant factors listed above. The paper presents a series of ablation studies to measure the impact of each of these factors on downstream benchmark performance (2405.02246.pdf, p. 3-5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard metrics tailored to different tasks:
*   **VQA accuracy (VQA acc.):** Used for general visual question answering benchmarks like VQAv2 and OKVQA, and for OCR-based VQA on TextVQA (2405.02246.pdf, p. 3, 8).
*   **CIDEr:** Used to evaluate performance on the COCO captioning task (2405.02246.pdf, p. 8).
*   **MMMU score:** A specific metric for the MMMU benchmark, which covers multi-discipline college-level problems (2405.02246.pdf, p. 8-9).
*   **Accuracy:** Used for the MMBench benchmark (2405.02246.pdf, p. 9).
*   **Average Normalized Levenshtein Similarity (ANLS):** Used for the DocVQA benchmark (2405.02246.pdf, p. 9).

The selection of these metrics is justified by their common adoption in the VLM literature for evaluating specific capabilities such as general reasoning, OCR, knowledge-based answering, and captioning (2405.02246.pdf, p. 3).

### Decision thresholds:
Insufficient information.

### Variation approaches:
The model was evaluated under different few-shot settings to ensure robust measurements:
*   **4-shot performance:** For the initial ablation studies, the average score across four downstream benchmarks was reported based on 4-shot performance (2405.02246.pdf, p. 3).
*   **8 random in-context examples:** For evaluating the final base model, 8 random in-context examples were used for VQA tasks (2405.02246.pdf, p. 8).
*   **Zero-shot:** For the final instruction-tuned models, evaluations were performed in a zero-shot setting (2405.02246.pdf, p. 9).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its diverse capabilities:
*   **VQAv2:** For general visual question answering (2405.02246.pdf, p. 3).
*   **TextVQA:** For OCR abilities, requiring the model to read text in images to answer questions (2405.02246.pdf, p. 3).
*   **OKVQA:** For questions requiring external knowledge to be answered (2405.02246.pdf, p. 3).
*   **COCO Captioning:** For image captioning (2405.02246.pdf, p. 3).
*   **MMMU:** A benchmark for multi-discipline college-level problems (2405.02246.pdf, p. 8).
*   **MathVista:** For mathematical reasoning in visual contexts (2405.02246.pdf, p. 8).
*   **MMBench:** For various perception and reasoning tasks (2405.02246.pdf, p. 9).
*   **DocVQA:** For document understanding (2405.02246.pdf, p. 9).

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks in the VLM community and collectively measure a wide range of different capabilities, from general perception and reasoning to specialized skills like OCR, mathematical reasoning, and knowledge-based answering (2405.02246.pdf, p. 3, 8-9).

### Preprocessing:
The evaluation data undergoes preprocessing steps consistent with the model's training.
*   **Image Resizing and Normalization:** Images are resized, with an option to preserve the original aspect ratio. The pixel values are normalized using a mean of `[0.5, 0.5, 0.5]` and a standard deviation of `[0.5, 0.5, 0.5]` (preprocessor_config.json.txt).
*   **Image Splitting:** For some evaluations of the instruction-tuned model, an image splitting strategy is used where an image is decomposed into 4 crops plus the original image, resulting in 320 visual tokens per image instead of the standard 64. This is particularly useful for benchmarks requiring high resolution to read text, like TextVQA (2405.02246.pdf, p. 6, 9).
*   **Prompt Formatting:** All datasets are prompted into a shared question/answer format. For multi-turn datasets, question/answer pairs are concatenated (2405.02246.pdf, p. 8).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a mixture of publicly available and newly created datasets across three main categories (2405.02246.pdf, p. 6-7):

**Pre-training Data:**
*   **Interleaved Image-Text Documents:**
    *   **OBELICS:** A web-scale dataset with 350 million images and 115 billion text tokens from long documents (Laurençon et al., 2023, as cited in 2405.02246.pdf, p. 6).
*   **Image-Text Pairs:**
    *   **PMD (Public Multimodal Dataset):** A combination of high-quality annotated pairs (Singh et al., 2022, as cited in 2405.02246.pdf, p. 7).
    *   **LAION-COCO:** A dataset with synthetic captions generated by a model trained on COCO, used for its higher quality compared to raw alt-text (Schuhmann et al., 2022, as cited in 2405.02246.pdf, p. 7).
*   **PDF Documents:**
    *   **OCR-IDL:** 19 million industry documents (Biten et al., 2022, as cited in 2405.02246.pdf, p. 7).
    *   **PDFA:** 18 million pages from PDF documents (2405.02246.pdf, p. 7).
    *   **RenderedText:** A dataset of texts written with a wide variety of fonts, colors, and backgrounds (2405.02246.pdf, p. 7).

**Instruction Fine-tuning Data:**
*   **The Cauldron:** A collection of 50 vision-language datasets and several text-only instruction datasets created by the authors. This includes datasets for VQA, captioning, OCR, chart understanding, reasoning, and more. A full list is available in the paper's appendix (2405.02246.pdf, p. 8, 21-22).

**Chat Fine-tuning Data:**
*   **LLaVA-Conv** (Liu et al., 2023) and **ShareGPT4V** (Chen et al., 2023) were used for dialogue-specific tuning (2405.02246.pdf, p. 9).

### Motivation:
The choice of datasets was motivated by the goal of creating a versatile VLM.
*   **OBELICS** was used to preserve the language model's performance and teach it to handle arbitrary sequences of images and text (2405.02246.pdf, p. 6).
*   **Image-text pairs** were included to learn the fundamental alignment between images and their descriptions (2405.02246.pdf, p. 7).
*   **PDF and RenderedText datasets** were specifically included to boost the model's OCR and document understanding abilities (2405.02246.pdf, p. 7).
*   **The Cauldron** and text-only instruction datasets were used to teach the model to follow task-oriented instructions and solve complex problems (2405.02246.pdf, p. 8).

### Preprocessing:
Several preprocessing steps were applied to the training data to improve quality and efficiency:
*   **Content Filtering:** The OBELICS dataset was filtered to remove documents with high perplexity scores and newly opted-out content (2405.02246.pdf, p. 6). The LAION-COCO dataset was filtered using a NSFW classifier, removing 7% of the samples (2405.02246.pdf, p. 7).
*   **Image Preprocessing:** Images are resized, rescaled, and normalized. The standard configuration resizes images to a maximum of 980 pixels on the longest edge (preprocessor_config.json.txt). During the second pre-training stage, images were also randomly scaled up to cover a wider distribution of sizes (2405.02246.pdf, p. 7).
*   **Text Tokenization:** Text is tokenized using a LlamaTokenizer with a vocabulary of 32,003 tokens (tokenizer_config.json.txt; config.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides several ablation studies on the impact of individual factors on the average score across VQAv2, TextVQA, OKVQA, and COCO benchmarks.
*   **Language Model Backbone:** Replacing LLaMA-1-7B with Mistral-7B as the language backbone increased the average score from 62.5 to 67.6 (2405.02246.pdf, p. 3, Table 1).
*   **Vision Encoder Backbone:** Switching the vision encoder from CLIP-ViT-H to SigLIP-SO400M increased the average score from 57.4 to 60.7 (2405.02246.pdf, p. 4, Table 2).
*   **Pooling Strategy:** Using a Perceiver resampler for pooling visual tokens yielded a score of 60.3, significantly outperforming a simple Linear Projection (44.5) and a Mapping Network (51.8) (2405.02246.pdf, p. 5, Table 11).
*   **Number of Visual Tokens:** Increasing the number of visual tokens from 64 to 128 did not show a significant performance gain (71.7 vs 71.2) (2405.02246.pdf, p. 5, Table 4).
*   **Aspect Ratio Preservation:** Preserving the original aspect ratio of images resulted in a slight decrease in average score (72.1) compared to resizing to square images (73.1), but offered significant gains in computational flexibility (2405.02246.pdf, p. 5, Table 5).

### Intersectional results:
The paper analyzes performance across combinations of factors:
*   **Architecture and Backbone Training:**
    *   With **frozen** backbones, the cross-attention architecture (66.7 avg. score) outperformed the fully autoregressive architecture (60.3 avg. score).
    *   With backbones trained using **LoRA**, the fully autoregressive architecture (69.5 avg. score) outperformed the cross-attention architecture (67.3 avg. score) (2405.02246.pdf, p. 4, Table 3).
*   **OCR Data and Image Resolution:** The combination of training with OCR data and using a higher image resolution (768) significantly boosted performance on DocVQA from 22.6 (without OCR data, 384 res) to 49.9 (with OCR data, 768 res) (2405.02246.pdf, p. 7, Table 7).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is approximately 33.61 GB (model.safetensors.index.json.txt). Loading the model would require RAM/VRAM exceeding this size.

### Deploying Requirements:
The model's fully autoregressive architecture with a perceiver resampler is computationally efficient at inference.
*   The standard configuration uses only 64 visual tokens per image, reducing the sequence length fed to the LLM (2405.02246.pdf, p. 5).
*   The ability to preserve aspect ratio allows for saving GPU memory by not resizing all images to a fixed high resolution (2405.02246.pdf, p. 5).
*   The use of LoRA for training means the adapted weights can be merged back into the original layers, adding no additional cost at inference (2405.02246.pdf, p. 4).

### Training or Fine-tuning Requirements:
*   Training the unimodal backbones using LoRA requires only a fraction of the GPU memory cost compared to full fine-tuning (2405.02246.pdf, p. 4).
*   The pre-training was conducted with a global batch size of 2048. Increasing image resolution from 384 to 980 pixels required a decrease in the per-device batch size, compensated by gradient accumulation (2405.02246.pdf, p. 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

**Data Filtering:**
*   The developers performed filtering on the training data to mitigate risks. The LAION-COCO dataset was filtered with a NSFW classifier, removing 7% of the samples (2405.02246.pdf, p. 7). The OBELICS dataset was filtered to exclude content from creators who opted out as of September 2023, with an additional removal of newly opted-out content in January 2024 (2405.02246.pdf, p. 6).

**Red-Teaming and Risk Identification:**
A red-teaming exercise was conducted on the chat-optimized model to evaluate its propensity to generate inaccurate, biased, or offensive responses (2405.02246.pdf, p. 23). Key risks identified include:
*   **Perpetuating Harmful Stereotypes:** The model can make speculative judgments about individuals' professions, social status, or personal attributes based on visual cues like age, attire, and gender, potentially reinforcing historical disparities and harmful stereotypes (2405.02246.pdf, p. 25).
*   **Generating Harmful Content:** The model can be prompted to generate content that promotes online harassment or offensive memes (2405.02246.pdf, p. 25).
*   **Security Risks:**
    *   **Solving CAPTCHAs:** The model can successfully solve CAPTCHAs with distorted text (2405.02246.pdf, p. 25).
    *   **Phishing Schemes:** It can be used to develop phishing schemes from screenshots of legitimate websites (2405.02246.pdf, p. 25).
    *   **Dangerous Instructions:** It can be prompted to craft step-by-step guides for constructing small-scale explosives or manipulating firearms (2405.02246.pdf, p. 25).

**Risk Mitigation and Model Behavior:**
*   The model often encourages user caution or flags problematic queries. For instance, when prompted for a racist comment, it may provide the response but follow up with a disclaimer about the harm of stereotyping (2405.02246.pdf, p. 26).
*   However, the paper notes that certain formulations ("jailbreaks") can bypass these cautionary prompts, highlighting the interaction between vision and language vulnerabilities (2405.02246.pdf, p. 26).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Jailbreaking:** Certain prompt formulations can circumvent the model's safety mechanisms, leading to the generation of harmful or problematic content (2405.02246.pdf, p. 26).
*   **OCR Limitations:** The security risks associated with generating dangerous instructions are noted to be "currently limited by the model's occasional inability to accurately read text within images," implying that improvements in OCR could heighten these risks (2405.02246.pdf, p. 25).
*   **Vision Encoder Gap:** The authors note that the "open VLM community is missing a large well-trained vision encoder," suggesting that model performance could be further improved with better foundational vision models (2405.02246.pdf, p. 4).
*   **Evaluation Metric Penalties:** Standard VQA metrics strongly penalize models for generating answers that are semantically correct but not in the exact format as the ground truth (e.g., "large" vs. "big"). This can make performance differences appear larger than they are in a qualitative sense (2405.02246.pdf, p. 23).

### Recommendations:
*   Users should exercise **critical thinking and discretion** when engaging with the model's outputs, as it can perpetuate harmful stereotypes or be jailbroken to produce offensive content (2405.02246.pdf, p. 26).
*   For tasks requiring high-resolution text extraction (like TextVQA or DocVQA), using the image splitting inference strategy (320 visual tokens) is recommended for better performance (2405.02246.pdf, p. 6, 9).
*   Users can leverage the model's ability to handle various resolutions to trade off computational cost and performance based on the specific requirements of their task (2405.02246.pdf, p. 5).

---