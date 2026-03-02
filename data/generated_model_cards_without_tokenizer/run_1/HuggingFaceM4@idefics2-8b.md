## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh (2405.02246.pdf, p. 1). The developers are affiliated with Hugging Face and Sorbonne Université (2405.02246.pdf, p. 1).

### Model date:
The associated research paper was submitted to arXiv on May 3, 2024 (2405.02246.pdf, p. 1).

### Model version:
The model is named Idefics2 (2405.02246.pdf, p. 1). It is an 8-billion parameter model that improves upon its predecessor, Idefics1 (2405.02246.pdf, p. 1, 8). The repository includes base, instruction-tuned, and chat-optimized versions of the model (2405.02246.pdf, p. 1).

### Model type:
Idefics2 is a multimodal vision-language model (VLM) that takes images and texts as inputs and outputs text (2405.02246.pdf, p. 2). It has 8 billion parameters (2405.02246.pdf, p. 1).

**Architecture:**
The model uses a **fully autoregressive architecture** (2405.02246.pdf, p. 3; config.json.txt, `architectures`). It is composed of three main components (2405.02246.pdf, p. 3, Figure 2; assets/Idefics2_flowchart.png):
1.  **Vision Encoder:** A pre-trained vision transformer, specifically SigLIP-SO400M, processes input images (2405.02246.pdf, p. 6). It has 27 hidden layers and uses a patch size of 14x14 (config.json.txt, `vision_config`).
2.  **Vision-Language Connector:** This module maps the visual features to the language model's input space. It uses a Perceiver resampler for pooling to reduce the number of visual tokens to a fixed sequence of 64, followed by a modality projection layer (2405.02246.pdf, p. 3, 5; processor_config.json.txt, `image_seq_len`).
3.  **Language Model:** A pre-trained large language model, specifically Mistral-7B-v0.1, processes the concatenated sequence of text and visual tokens to generate a text output (2405.02246.pdf, p. 6; config.json.txt, `text_config`).

**Model Size and Context:**
*   **Parameters:** 8 billion (2405.02246.pdf, p. 1).
*   **Total Size on Disk:** 33.6 GB (model.safetensors.index.json.txt, `metadata.total_size`).
*   **Text Context Length:** 32,768 tokens (config.json.txt, `text_config.max_position_embeddings`).
*   **Image Context:** The model processes images by converting them into 64 visual tokens (processor_config.json.txt, `image_seq_len`).

### Training details:
The model was trained in multiple stages: a two-stage pre-training phase followed by an instruction fine-tuning phase (2405.02246.pdf, p. 3, 7).

**Pre-training:**
*   **Stage 1:** The model was trained on a mixture of interleaved image-text documents (OBELICS dataset) and image-text pairs (PMD, LAION COCO). The maximum image resolution was limited to 384 pixels with a global batch size of 2,048 (2405.02246.pdf, p. 7).
*   **Stage 2:** PDF documents (OCR-IDL, PDFA, Rendered Text) were introduced to the training mixture to improve OCR capabilities. The maximum image resolution was increased to 980 pixels (2405.02246.pdf, p. 7).
*   **Algorithm:** The training adapted the pre-trained vision and language backbones using Low-Rank Adaptation (LoRA) to ensure training stability (2405.02246.pdf, p. 4). The pre-training used a learning rate of 10⁻⁴ and ran for approximately 2 epochs over the data, corresponding to 1.5 billion images and 225 billion text tokens (2405.02246.pdf, p. 7).

**Instruction Fine-tuning:**
*   The base model was fine-tuned on "The Cauldron," a large collection of 50 vision-language datasets and several text-only instruction datasets (2405.02246.pdf, p. 8).
*   **Algorithm:** Fine-tuning was performed using DoRA (a variant of LoRA) (2405.02246.pdf, p. 8).
*   **Techniques:** To prevent overfitting, the process included adding noise to embeddings (NEFTune), randomly scaling image resolutions during training, and shuffling conversational turns (2405.02246.pdf, p. 8).

**Chat Model Optimization:**
*   After instruction tuning, the model was further trained for a few hundred steps on dialogue data (LLaVA-Conv, ShareGPT4V) to improve performance in conversational scenarios (2405.02246.pdf, p. 9).

### Paper or other resource for more information:
*   **Academic Paper:** "What matters when building vision-language models?" by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh. The paper details the experiments, architectural choices, and training procedures that led to Idefics2 (2405.02246.pdf).
*   **Hugging Face Collection:** A collection of resources for Idefics2, including the different model versions, is available at: `https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe` (2405.02246.pdf, p. 2).

### Citation details:
The following BibTeX entry can be used to cite the work (2405.02246.pdf, p. 1):
```bibtex
@misc{laurencon2024matters,
      title={What matters when building vision-language models?}, 
      author={Hugo Laurençon and Léo Tronchon and Matthieu Cord and Victor Sanh},
      year={2024},
      eprint={2405.02246},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Idefics2 is a foundational vision-language model designed for a wide range of tasks that require understanding both images and text (2405.02246.pdf, p. 1). Its capabilities include:
*   Answering questions about images (visual question answering) (2405.02246.pdf, p. 3).
*   Describing images (captioning) (2405.02246.pdf, p. 3).
*   Retrieving information from scanned documents and PDFs (2405.02246.pdf, p. 2).
*   Explaining charts, diagrams, and tables (2405.02246.pdf, p. 1, Figure 1).
*   Transcribing text from images (Optical Character Recognition - OCR) (2405.02246.pdf, p. 2, Figure 3).
*   Converting screenshots of webpages into code (2405.02246.pdf, p. 2).
*   Following multi-turn conversational instructions involving images and text (2405.02246.pdf, p. 8).

The model accepts a sequence of interleaved images and text as input and generates text as output (2405.02246.pdf, p. 2).

### Primary intended users:
The primary intended users are researchers and developers in the vision-language and broader AI community (2405.02246.pdf, p. 2).

### Out-of-scope uses:
The model is not designed for applications that require perfect factual accuracy or are safety-critical without human oversight. A red-teaming analysis identified several potential misuse cases and harmful capabilities (2405.02246.pdf, p. 25):
*   **Perpetuating Harmful Stereotypes:** The model may generate speculative judgments about individuals' professions, social status, or other attributes based on visual cues like age, gender, or attire (2405.02246.pdf, p. 25).
*   **Generating Harmful Content:** The model can be prompted to create content for online harassment or offensive memes (2405.02246.pdf, p. 25).
*   **Security Risks:**
    *   Solving CAPTCHAs with distorted text.
    *   Developing phishing schemes from screenshots of websites.
    *   Crafting step-by-step guides for dangerous activities, such as constructing small-scale explosives (2405.02246.pdf, p. 25).

Users should exercise critical thinking and discretion, as certain prompts can circumvent the model's safety filters ("jailbreaking") (2405.02246.pdf, p. 26).

---

## How to Use
This section outlines how to use the model.

The model processes a sequence of text and images. The input should be formatted according to the model's chat template. The special token `<image>` is used as a placeholder for images in the text prompt.

**Chat Template:**
The following template is used to format conversational input for the model (processor_config.json.txt, `chat_template`):
```jinja
{% for message in messages %}{{message['role'].capitalize()}}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}<end_of_utterance>
{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}
```
This template structures the input into turns for "User" and "Assistant", with `<image>` tokens indicating where images are placed.

**Generation Configuration:**
*   **BOS (Beginning-of-Sequence) Token ID:** 1 (generation_config.json.txt, `bos_token_id`).
*   **EOS (End-of-Sequence) Token IDs:** 2, 32002 (generation_config.json.txt, `eos_token_id`).
*   **PAD (Padding) Token ID:** 0 (generation_config.json.txt, `pad_token_id`).
*   **Bad Words IDs:** `[[32000], [32001]]` are specified to be avoided during generation (generation_config.json.txt, `bad_words_ids`).

**Example Input-Output:**
*   **Task:** Extracting structured information from a resume.
    *   **Prompt:** "User: <image>\nExtract the name, email, current job, and education. Output a JSON format.<end_of_utterance>\nAssistant:"
    *   **Output:** A JSON object containing the requested fields extracted from the resume image (2405.02246.pdf, p. 24, Figure 5).
*   **Task:** Answering a question about a scientific diagram.
    *   **Prompt:** "User: <image>\nWhat happens to fish if pelicans increase?<end_of_utterance>\nAssistant:"
    *   **Output:** "If pelicans increase, they may consume more fish, which could lead to a decrease in the fish population or an imbalance in the ecosystem. This could potentially affect other species that rely on fish for food, such as seals, dolphins, and humans who fish for consumption." (2405.02246.pdf, p. 25, Figure 7).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development paper identifies several key factors that influence the performance of vision-language models (2405.02246.pdf, p. 2):
*   **Quality of Pre-trained Backbones:** The performance of the final VLM is highly dependent on the quality of the initial unimodal vision and language models. The language model backbone was found to have a higher impact than the vision backbone for a fixed parameter count (2405.02246.pdf, p. 3-4).
*   **Model Architecture:** The choice between a fully autoregressive architecture and a cross-attention architecture significantly impacts performance and training stability. The fully autoregressive architecture was found to outperform the cross-attention one when the unimodal backbones are trained (2405.02246.pdf, p. 4).
*   **Number of Visual Tokens:** The quantity of visual tokens used to represent an image affects both computational cost and performance. Using a Perceiver resampler to reduce tokens to 64 was found to improve performance and efficiency compared to using a larger number of tokens (e.g., 729) (2405.02246.pdf, p. 5).
*   **Image Resolution and Aspect Ratio:** Handling images at their native resolution and aspect ratio, rather than resizing to a fixed square, maintains performance while improving efficiency and reducing memory usage (2405.02246.pdf, p. 5-6).
*   **Image Splitting:** Decomposing an image into sub-images (e.g., 4 crops plus the original) can boost performance on tasks requiring high-resolution detail, such as reading text, at the cost of increased computational load (2405.02246.pdf, p. 6).

### Evaluation factors:
The model was evaluated by analyzing the impact of the factors listed above. Ablation studies were conducted to measure performance changes when varying:
*   Language model backbone (Llama-1-7B vs. Mistral-7B) (2405.02246.pdf, p. 3, Table 1).
*   Vision encoder backbone (CLIP-ViT-H vs. EVA-CLIP-5B vs. SigLIP-SO400M) (2405.02246.pdf, p. 4, Table 2).
*   Architecture and training method (cross-attention vs. fully autoregressive, with frozen vs. LoRA-trained backbones) (2405.02246.pdf, p. 4, Table 3).
*   Pooling strategy and number of visual tokens (2405.02246.pdf, p. 5, Table 4).
*   Image processing (square resizing vs. aspect ratio preserving) (2405.02246.pdf, p. 5, Table 5).
*   Inference-time image splitting (64 vs. 320 tokens per image) (2405.02246.pdf, p. 9, Table 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard benchmarks and metrics tailored to different tasks (2405.02246.pdf, p. 8-9, 24):
*   **Visual Question Answering (VQA):**
    *   **VQAv2:** VQA accuracy (`VQA acc.`) on the `testdev` split.
    *   **TextVQA:** VQA accuracy (`VQA acc.`) on the `val` split for tasks requiring reading text.
    *   **OKVQA:** VQA accuracy (`VQA acc.`) on the `val` split for tasks requiring external knowledge.
*   **Image Captioning:**
    *   **COCO:** CIDEr score on the `test` split.
*   **Document Understanding:**
    *   **DocVQA:** Average Normalized Levenshtein Similarity (`ANLS`) on the `test` split.
*   **Multidisciplinary Reasoning:**
    *   **MMMU:** MMMU score on `val` and `test` splits for college-level problems.
    *   **MathVista:** MMMU score on the `testmini` split for mathematical reasoning in visual contexts.
*   **General Perception and Reasoning:**
    *   **MMBench:** Accuracy on the `test` split.

### Decision thresholds:
Insufficient information

### Variation approaches:
Evaluations were conducted under zero-shot and few-shot settings (2405.02246.pdf, p. 8-9):
*   **Base Model:** Evaluated using 8 random in-context examples (few-shot) in an open-ended setting for VQA tasks (2405.02246.pdf, p. 8).
*   **Instruction-Tuned Model:** Evaluated in a zero-shot setting (2405.02246.pdf, p. 9, 24).
*   All evaluations were performed with a batch size of 1 and greedy decoding (2405.02246.pdf, p. 23).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess its capabilities across various domains (2405.02246.pdf, p. 8-9, Table 9):
*   **VQAv2:** For general visual question answering (Goyal et al., 2017).
*   **TextVQA:** For visual question answering that requires reading text in images (Singh et al., 2019).
*   **OKVQA:** For visual question answering requiring external knowledge (Marino et al., 2019).
*   **COCO:** For image captioning (Lin et al., 2014).
*   **MMMU:** A benchmark for massive multi-discipline multimodal understanding and reasoning (Yue et al., 2024).
*   **MathVista:** For mathematical reasoning in visual contexts (Lu et al., 2024).
*   **MMBench:** For evaluating various perception and reasoning tasks (Liu et al., 2023).
*   **DocVQA:** For question answering on document images (Mathew et al., 2021).

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks in the VLM community and collectively cover a wide range of essential capabilities, from basic perception and captioning to complex reasoning, OCR, and knowledge-based understanding (2405.02246.pdf, p. 3, 8-9).

### Preprocessing:
For evaluation, a standard prompt format was used for each task type (e.g., multi-choice vs. open-ended) (2405.02246.pdf, p. 23). For some evaluations, an image splitting strategy was employed where each image was processed as a sequence of 5 images (the original plus four crops), resulting in 320 visual tokens instead of the standard 64. This was done to test performance on tasks requiring higher resolution (2405.02246.pdf, p. 6, 9).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained in two phases using distinct data mixtures.

**Pre-training Data:**
The pre-training stage utilized a combination of three data types (2405.02246.pdf, p. 6-7):
1.  **Interleaved Image-Text Documents:**
    *   **OBELICS:** An open, web-scale dataset with 350 million images and 115 billion text tokens from long-form documents (Laurençon et al., 2023).
2.  **Image-Text Pairs:**
    *   **PMD:** A dataset of high-quality human-annotated image-text pairs (Singh et al., 2022).
    *   **LAION COCO:** A version of the LAION dataset where images are captioned by a model trained on COCO, providing synthetic captions (Schuhmann et al., 2022).
3.  **PDF Documents:**
    *   **OCR-IDL:** 19 million industry documents (Biten et al., 2022).
    *   **PDFA:** 18 million pages from publicly available documents (2405.02246.pdf, p. 7).
    *   **RenderedText:** A dataset of text rendered with diverse fonts, colors, and backgrounds (2405.02246.pdf, p. 7).

**Instruction Fine-tuning Data:**
The fine-tuning stage used a newly created and released dataset:
*   **The Cauldron:** A massive collection of 50 vision-language datasets and several text-only instruction datasets, covering tasks like VQA, captioning, OCR, document understanding, chart reasoning, and code generation. A detailed breakdown of the datasets and their mixture proportions is provided in the paper's appendix (2405.02246.pdf, p. 8, 21-23, Table 14).

### Motivation:
The choice of training data was motivated by the goal of building a versatile VLM:
*   **OBELICS** was used to teach the model to handle an arbitrary number of interleaved images and text in long contexts (2405.02246.pdf, p. 6).
*   **Image-text pairs** were used to learn the fundamental alignment between visual concepts and their textual descriptions (2405.02246.pdf, p. 7).
*   **PDF and rendered text documents** were included to build strong OCR and document understanding capabilities (2405.02246.pdf, p. 7).
*   **The Cauldron** was curated to teach the model to follow complex instructions across a diverse range of multimodal tasks (2405.02246.pdf, p. 8).

### Preprocessing:
Several preprocessing steps were applied to the training data to ensure quality and efficiency:
*   **Image Preprocessing:** Images are resized (preserving aspect ratio with a longest edge of 980), padded, normalized, and rescaled (preprocessor_config.json.txt). During pre-training, images were randomly scaled up to cover a distribution of sizes (2405.02246.pdf, p. 7).
*   **Data Filtering:**
    *   **OBELICS:** Content that was opted-out of was removed using the Spawning API. The 5% of documents with the highest perplexity scores were also removed (2405.02246.pdf, p. 6).
    *   **LAION COCO:** A NSFW classifier was used to filter and remove 7% of the samples (2405.02246.pdf, p. 7).
*   **Deduplication:** The instruction fine-tuning set (The Cauldron) was deduplicated against the evaluation sets to minimize contamination (2405.02246.pdf, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents several ablation studies analyzing the impact of individual design choices on a 4-benchmark average score (VQAv2, TextVQA, OKVQA, COCO) (2405.02246.pdf, p. 3):
*   **Language Model Backbone:** Switching from Llama-1-7B to Mistral-7B improved the average score from 62.5 to 67.6 (2405.02246.pdf, p. 3, Table 1).
*   **Vision Encoder Backbone:** Switching from CLIP-ViT-H (224 res) to SigLIP-SO400M (384 res) improved the average score from 57.4 to 60.7 (2405.02246.pdf, p. 4, Table 2).
*   **Pooling Strategy:** Using a Perceiver resampler (71.7 avg. score) significantly outperformed no pooling (60.3 avg. score) (2405.02246.pdf, p. 4-5, Table 3, 4).
*   **Image Aspect Ratio:** Preserving aspect ratio (72.1 avg. score) performed comparably to resizing to square images (73.1 avg. score) while being more efficient (2405.02246.pdf, p. 5, Table 5).
*   **Image Splitting (Inference):** Using image splitting (320 tokens) improved TextVQA score from 70.4 to 73.0 and DocVQA from 67.3 to 74.0, showing its benefit for OCR-heavy tasks (2405.02246.pdf, p. 9, 24, Table 9, 15).

### Intersectional results:
The paper compares performance across different architectures and training methods:
*   **Architecture vs. Training Method:**
    *   With **frozen** backbones, the cross-attention architecture (66.7 avg. score) outperformed the fully autoregressive one (60.3 avg. score).
    *   With **LoRA-trained** backbones, the fully autoregressive architecture (69.5 avg. score) outperformed the cross-attention one (67.3 avg. score) (2405.02246.pdf, p. 4, Table 3).

The final model's performance is reported across multiple benchmarks simultaneously, comparing it against other state-of-the-art models (2405.02246.pdf, p. 24, Table 15). For example, Idefics2 (8B, 64 tokens) achieves:
*   **MMMU (val/test):** 43.5/37.9
*   **MathVista (testmini):** 51.6
*   **TextVQA (val):** 70.4
*   **MMBench (test):** 76.8
*   **DocVQA (test):** 67.3
*   **VQAv2 (testdev):** 80.8

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper notes that using LoRA to adapt pre-trained backbones allows training "at a fraction of the GPU memory cost of full fine-tuning" (2405.02246.pdf, p. 4). Similarly, adapting the vision encoder to preserve aspect ratio "allows for saving GPU memory" (2405.02246.pdf, p. 6). However, specific hardware configurations or memory values (e.g., VRAM in GB) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

A red-teaming exercise was conducted to evaluate the model's propensity to generate inaccurate, biased, or offensive responses (2405.02246.pdf, p. 23). No sensitive personal data was explicitly mentioned as being used for training, but the web-crawled nature of datasets like OBELICS and LAION implies the potential presence of such data.

**Risks and Mitigation:**
*   **Harmful Stereotypes and Bias:** The model can perpetuate harmful stereotypes related to professions, social status, or personal attributes based on visual cues. It may also generate content for online harassment (2405.02246.pdf, p. 25). As a mitigation, the model often encourages user caution or flags the problematic nature of a query. For instance, when prompted for a racist comment, it may respond but also point out the harmful history of such stereotyping (2405.02246.pdf, p. 26).
*   **Data Filtering:** To reduce the risk of training on harmful content, a NSFW classifier was used to filter 7% of the LAION COCO dataset, and an additional removal of opted-out content was performed on the OBELICS dataset (2405.02246.pdf, p. 6-7).
*   **Security Risks:** The model demonstrated capabilities that pose security risks, including solving CAPTCHAs, creating phishing schemes from screenshots, and generating instructions for building explosives. The paper notes that this risk is currently limited by the model's occasional inability to read text accurately (2405.02246.pdf, p. 25).
*   **Jailbreaking:** The model's safety mechanisms can be circumvented by certain prompt formulations ("jailbreaking"), highlighting the interaction between vision and language vulnerabilities (2405.02246.pdf, p. 26).

The developers emphasize the need for users to apply critical thinking and discretion when using the model (2405.02246.pdf, p. 26).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Vision Encoder Quality:** The authors note that the open VLM community is "missing a large well-trained vision encoder," suggesting that model performance could be further improved with better vision backbones (2405.02246.pdf, p. 4).
*   **OCR Reliability:** The model's ability to perform harmful tasks like creating phishing schemes is "currently limited by the model's occasional inability to accurately read text within images." As OCR capabilities improve, these risks may become more severe (2405.02246.pdf, p. 25).
*   **Evaluation Metric Sensitivity:** For benchmarks like VQAv2, the evaluation metric strongly penalizes answers that are semantically correct but not in the exact format of the ground truth. This means that a 5-point difference in scores may not correspond to a barely noticeable difference in generation quality (2405.02246.pdf, p. 23).
*   **Stereotypes and Bias:** Despite safety measures, the model can perpetuate harmful stereotypes, especially when presented with ambiguous visual inputs (2405.02246.pdf, p. 25).

### Recommendations:
*   **Critical Engagement:** Users should exercise "critical thinking and discretion when engaging with the model's outputs," as safety prompts can be circumvented (2405.02246.pdf, p. 26).
*   **Task-Specific Evaluation:** For tasks requiring high-resolution understanding (e.g., document analysis), users should consider using the image-splitting technique at inference time, which processes an image with 320 visual tokens instead of 64, as this can significantly improve performance (2405.02246.pdf, p. 6, 9).
*   **Human Oversight:** The model should not be used in high-stakes, safety-critical applications without human oversight and validation of its outputs.

---