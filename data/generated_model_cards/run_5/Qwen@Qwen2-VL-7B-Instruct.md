## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the Qwen Team at Alibaba Group (Source: 2409.12191v2.pdf, p. 1). The listed authors are Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du, Xuancheng Ren, Rui Men, Dayiheng Liu, Chang Zhou, Jingren Zhou, and Junyang Lin (Source: 2409.12191v2.pdf, p. 1).

### Model date:
The paper describing the model was submitted to arXiv on October 3, 2024 (Source: 2409.12191v2.pdf, p. 1). The cutoff date for the model's training data knowledge is June 2023 (Source: 2409.12191v2.pdf, p. 5).

### Model version:
This model is part of the Qwen2-VL Series, which is an advanced upgrade of the previous Qwen-VL models (Source: 2409.12191v2.pdf, p. 1). The series includes three open-weight models with different parameter counts: Qwen2-VL-2B, Qwen2-VL-7B, and Qwen2-VL-72B (Source: 2409.12191v2.pdf, p. 3).
- **Qwen2-VL-2B**: The most efficient model, with 1.5B LLM parameters, designed for on-device execution (Source: 2409.12191v2.pdf, p. 3, Table 1).
- **Qwen2-VL-7B**: A performance-optimized model with 7.6B LLM parameters, upgraded for text recognition and video understanding (Source: 2409.12191v2.pdf, p. 3, Table 1).
- **Qwen2-VL-72B**: The most capable model, with 72B LLM parameters, featuring improvements in visual reasoning, instruction-following, and agent capabilities (Source: 2409.12191v2.pdf, p. 3, Table 1).

The model was developed using `transformers` version 4.41.2 (Source: config.json, key: "transformers_version").

### Model type:
The model is a Large Vision-Language Model (LVLM) for conditional generation (Source: config.json, key: "architectures"). It follows a framework that integrates a vision encoder and a large language model (Source: 2409.12191v2.pdf, p. 3).

**Architecture Details:**
- **Model Type:** `qwen2_vl` (Source: config.json, key: "model_type").
- **Vision Encoder:** It uses a Vision Transformer (ViT) with approximately 675 million parameters to handle both image and video inputs (Source: 2409.12191v2.pdf, p. 4). The ViT was modified to use 2D Rotary Position Embedding (RoPE) to support dynamic image resolutions (Source: 2409.12191v2.pdf, p. 4).
- **Language Model:** The language processing component is based on the Qwen2 series of language models (Source: 2409.12191v2.pdf, p. 4).
- **Key Mechanisms:**
    - **Naive Dynamic Resolution:** Allows the model to process images of any resolution by dynamically converting them into a variable number of visual tokens (Source: 2409.12191v2.pdf, p. 4).
    - **Multimodal Rotary Position Embedding (M-RoPE):** Deconstructs rotary embedding into temporal, height, and width components to effectively model positional information across text, images, and videos (Source: 2409.12191v2.pdf, p. 5).

**Model Size and Parameters:**
- **Total Size:** The total size of the model weights is approximately 16.58 GB (Source: model.safetensors.index.json, key: "metadata.total_size"). The series includes models with 2B, 8B, and 72B parameters (Source: 2409.12191v2.pdf, p. 3).
- **LLM Parameters:**
    - Hidden Size: 3584 (Source: config.json, key: "hidden_size")
    - Number of Hidden Layers: 28 (Source: config.json, key: "num_hidden_layers")
    - Number of Attention Heads: 28 (Source: config.json, key: "num_attention_heads")
    - Intermediate Size: 18944 (Source: config.json, key: "intermediate_size")
- **Vision Encoder Parameters:**
    - Embedding Dimension: 1280 (Source: config.json, key: "vision_config.embed_dim")
    - Depth: 32 (Source: config.json, key: "vision_config.depth")
    - Number of Heads: 16 (Source: config.json, key: "vision_config.num_heads")
    - Patch Size: 14 (Source: config.json, key: "vision_config.patch_size")
- **Vocabulary Size:** 152064 (Source: config.json, key: "vocab_size").
- **Context Length:** The model supports a context length of 32768 tokens (Source: tokenizer_config.json, key: "model_max_length"; config.json, key: "max_position_embeddings").

### Training details:
The model was trained using a three-stage methodology (Source: 2409.12191v2.pdf, p. 5):
1.  **First Stage:** The Vision Transformer (ViT) component is trained on a large corpus of image-text pairs to learn semantic understanding.
2.  **Second Stage:** All parameters are unfrozen, and the model is trained on a wider range of data, including mixed image-text content and visual question-answering datasets.
3.  **Final Stage:** The ViT parameters are locked, and the LLM is exclusively fine-tuned using instructional datasets in the ChatML format.

The model was pre-trained on a cumulative total of 1.4 trillion tokens, which include both text and image tokens (Source: 2409.12191v2.pdf, p. 6). The training was performed on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service using PyTorch 2.1.2 with CUDA 11.8, leveraging 3D parallelism (DP, TP, PP), DeepSpeed's ZeRO-1, and FlashAttention (Source: 2409.12191v2.pdf, p. 8). The model uses `bfloat16` for its torch data type (Source: config.json, key: "torch_dtype").

### Paper or other resource for more information:
- **Academic Paper:** "Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution" provides a comprehensive overview of the model's architecture, training, and performance (Source: 2409.12191v2.pdf).
- **Code Repository:** The code is available at https://github.com/QwenLM/Qwen2-VL (Source: 2409.12191v2.pdf, p. 1).

### Citation details:
Insufficient information.

### License:
The model is licensed under the Apache License, Version 2.0 (Source: LICENSE). This license allows for use, reproduction, and distribution of the work and derivative works in source or object form, provided that certain conditions are met, such as retaining copyright notices and providing a copy of the license. It does not grant permission to use the trade names, trademarks, or service marks of the licensor (Source: LICENSE, Sections 2, 4, 6). The full license text is available at http://www.apache.org/licenses/LICENSE-2.0 (Source: LICENSE).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The Qwen2-VL series is designed as a versatile, general-purpose Large Vision-Language Model (LVLM) with a wide range of capabilities (Source: 2409.12191v2.pdf, p. 1, 3). Its primary intended uses include:
- **General Visual Question Answering:** Answering questions based on visual content from images and videos (Source: 2409.12191v2.pdf, p. 9).
- **Document and Diagram Understanding:** Comprehending text and graphical information in documents, infographics, and charts (Source: 2409.12191v2.pdf, p. 3, 11).
- **Multilingual Text Recognition (OCR):** Recognizing and understanding text in multiple languages within images, including English, Chinese, European languages, Japanese, Korean, Arabic, and Vietnamese (Source: 2409.12191v2.pdf, p. 3, 11).
- **Mathematical Reasoning:** Solving math problems embedded in visual contexts (Source: 2409.12191v2.pdf, p. 11).
- **Video Comprehension:** Understanding content in videos up to 20 minutes in length, enabling tasks like video-based dialogue and content creation (Source: 2409.12191v2.pdf, p. 3).
- **Visual Agent Capabilities:** Acting as a VL-Agent for sequential decision-making tasks such as UI operations on mobile phones, robotic control, and navigation based on visual inputs and text instructions (Source: 2409.12191v2.pdf, p. 3, 7).
- **Visual Grounding:** Localizing and referring to specific regions in an image described by text (Source: 2409.12191v2.pdf, p. 6).

The model takes multimodal input, including text, images, and videos, and generates text-based responses (Source: chat_template.json; 2409.12191v2.pdf, p. 1).

### Primary intended users:
The model is intended for researchers and developers in the field of artificial intelligence who are working on a variety of applications and research projects (Source: 2409.12191v2.pdf, p. 16).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model uses a specific chat template format called ChatML for structuring conversations (Source: 2409.12191v2.pdf, p. 6). Each message is enclosed within `<|im_start|>` and `<|im_end|>` tokens, with the role (e.g., `system`, `user`, `assistant`) specified at the beginning of the message. Visual inputs like images and videos are embedded within the user's text prompt using special tokens (Source: chat_template.json).

Below is an example of the input-output structure:
```json
[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": [
    {"type": "image", "image_url": "path_to_image.jpg"},
    {"type": "text", "text": "What is in this image?"}
  ]},
  {"role": "assistant", "content": "This is an image of..."}
]
```

The raw format for a user prompt with an image would look like this (Source: chat_template.json; 2409.12191v2.pdf, p. 6):
`<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>What is in this image?<|im_end|>\n<|im_start|>assistant\n`

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
- **Image Resolution and Aspect Ratio:** The model's performance is influenced by the resolution of input images. It introduces a "Naive Dynamic Resolution" mechanism to handle images of varying resolutions and aspect ratios, which can affect the number of visual tokens generated and subsequent processing (Source: 2409.12191v2.pdf, p. 4).
- **Model Size:** The model is available in 2B, 8B, and 72B parameter versions. Performance scales with model size, with larger models showing stronger capabilities, particularly in mathematical reasoning (Source: 2409.12191v2.pdf, p. 16, Figure 6a).
- **Training Data Volume:** Model performance improves as the number of training tokens increases, especially for tasks involving textual and graphical information understanding (Source: 2409.12191v2.pdf, p. 16, Figure 6b).

### Evaluation factors:
The model's evaluation reports results disaggregated by:
- **Model Size:** Performance is compared across the 2B, 7B, and 72B versions of the model (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **Task Type:** The model is evaluated on a wide array of benchmarks categorized by capability, such as general VQA, document understanding, mathematical reasoning, and video comprehension (Source: 2409.12191v2.pdf, p. 15-16).
- **Language:** For OCR tasks, performance is evaluated across multiple languages including Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (Source: 2409.12191v2.pdf, p. 9, Table 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using various metrics specific to the evaluation benchmarks (Source: 2409.12191v2.pdf, Section 3). These include:
- **Accuracy:** Used for benchmarks like DocVQA, InfoVQA, MMBench, and MathVista (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **Success Rate (SR):** Used for agent-based tasks like Card Games, ALFRED, R2R, and REVERIE to measure if the task goal was achieved (Source: 2409.12191v2.pdf, p. 10, Table 5).
- **Goal-Condition Success (GC):** A metric for robotic control tasks (ALFRED) that measures the completion of sub-goals (Source: 2409.12191v2.pdf, p. 10, Table 5).
- **Type Match (TM) and Exact Match (EM):** Used for function calling tasks to evaluate the accuracy of the selected function and the correctness of its arguments, respectively (Source: 2409.12191v2.pdf, p. 10, Table 5).
- **Score:** Some benchmarks like MME and OCRBench use custom scoring systems (Source: 2409.12191v2.pdf, p. 9, Table 2).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess its capabilities across various domains (Source: 2409.12191v2.pdf, Section 3). These include:
- **General VQA:** RealWorldQA, MMStar, MMVet, MMT-Bench, MMBench, MME, HallusionBench (Source: 2409.12191v2.pdf, p. 9).
- **Document & OCR:** DocVQA, ChartQA, InfoVQA, TextVQA, AI2D, OCRBench, MTVQA (Source: 2409.12191v2.pdf, p. 11).
- **Mathematical Reasoning:** MathVista, MathVision (Source: 2409.12191v2.pdf, p. 11).
- **Referring Expression Comprehension:** RefCOCO, RefCOCO+, RefCOCOg (Source: 2409.12191v2.pdf, p. 11).
- **Video Understanding:** MVBench, PerceptionTest, EgoSchema, Video-MME (Source: 2409.12191v2.pdf, p. 11-12).
- **Agent Tasks:** AITZ (UI Operations), Number Line, BlackJack, EZPoint, Point24 (Card Games), ALFRED (Robotic Control), R2R, REVERIE (Vision-Language Navigation) (Source: 2409.12191v2.pdf, p. 13).

### Motivation:
The datasets were chosen to provide a rigorous and extensive evaluation of the model's capabilities in various aspects, from general visual perception and document understanding to multilingual recognition, video comprehension, and agent abilities (Source: 2409.12191v2.pdf, p. 8). For example, RealWorldQA was used to evaluate real-world spatial comprehension, while MathVista and MathVision were used to assess mathematical reasoning skills (Source: 2409.12191v2.pdf, p. 9, 11).

### Preprocessing:
- For evaluation, small images are upscaled to surpass a specified `min_pixels` threshold before being input into the model (Source: 2409.12191v2.pdf, p. 14, Figure 4).
- Images are normalized using a mean of `[0.48145466, 0.4578275, 0.40821073]` and a standard deviation of `[0.26862954, 0.26130258, 0.27577711]` (Source: preprocessor_config.json, keys: "image_mean", "image_std").
- For the Video-MME benchmark, the maximum number of frames extracted per video was limited to 768 during evaluation (Source: 2409.12191v2.pdf, p. 12).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a diverse dataset with a cumulative total of 1.4 trillion tokens (Source: 2409.12191v2.pdf, p. 6). The dataset sources primarily comprise cleaned web pages, open-source datasets, and synthetic data (Source: 2409.12191v2.pdf, p. 5). The data types include:
- Image-text pairs
- Optical Character Recognition (OCR) data
- Interleaved image-text articles
- Visual question answering datasets
- Video dialogues
- Image knowledge datasets
- Purely textual data (Source: 2409.12191v2.pdf, p. 5-6).

The instruction fine-tuning phase used a dataset constructed in the ChatML format, which included pure text-based dialogue and multimodal conversational data (image question-answering, document parsing, video comprehension, etc.) (Source: 2409.12191v2.pdf, p. 6).

### Motivation:
The diverse data composition was chosen to develop a robust multimodal understanding capability (Source: 2409.12191v2.pdf, p. 5). The comprehensive approach to data construction for fine-tuning aimed to enhance the model's ability to understand and execute a wide range of instructions across various modalities (Source: 2409.12191v2.pdf, p. 6).

### Preprocessing:
- **Text Preprocessing:** The text is normalized using NFC. The pre-tokenizer splits text based on a regex pattern and then applies Byte-Level BPE (Source: tokenizer.json, keys: "normalizer", "pre_tokenizer").
- **Video Preprocessing:** Videos are sampled at two frames per second. To balance computational demands with efficiency, the resolution of each video frame is dynamically adjusted to limit the total number of tokens per video to 16384 (Source: 2409.12191v2.pdf, p. 5).
- **Image Preprocessing:** Images are treated as two identical frames for consistency with video processing (Source: 2409.12191v2.pdf, p. 5). The model uses a "Naive Dynamic Resolution" approach, where images of varying resolutions are converted into a variable number of visual tokens (Source: 2409.12191v2.pdf, p. 4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive performance results across various benchmarks. Below are some highlights for the Qwen2-VL-72B model:
- **DocVQA (test):** 96.5% accuracy (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **TextVQA (val):** 85.5% accuracy (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **MathVista (testmini):** 70.5% accuracy (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **MMMU (val):** 64.5% accuracy (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **RealWorldQA:** 77.8 score (Source: 2409.12191v2.pdf, p. 9, Table 2).
- **MVBench (video):** 67.0 score (Source: 2409.12191v2.pdf, p. 10, Table 4).
- **AITZ (UI agent):** 89.6 Type Match, 72.1 Exact Match (Source: 2409.12191v2.pdf, p. 10, Table 5).
- **Multilingual OCR (internal benchmark):**
    - Japanese: 93.4% (Source: 2409.12191v2.pdf, p. 9, Table 3)
    - French: 94.1% (Source: 2409.12191v2.pdf, p. 9, Table 3)
    - German: 91.5% (Source: 2409.12191v2.pdf, p. 9, Table 3)

Performance consistently improves with model size (2B < 7B < 72B) across most benchmarks (Source: 2409.12191v2.pdf, p. 16, Figure 6a).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model uses the `bfloat16` data type (Source: config.json, key: "torch_dtype"). The total size of the weights for one version of the model is approximately 16.58 GB (Source: model.safetensors.index.json, key: "metadata.total_size"), suggesting that a GPU with sufficient VRAM is required to load it. The series includes 2B, 8B, and 72B parameter models, which will have varying memory requirements (Source: 2409.12191v2.pdf, p. 3).

### Deploying Requirements:
The Qwen2-VL-2B model is specifically designed to be efficient enough for on-device execution (Source: 2409.12191v2.pdf, p. 3, Table 1).

### Training or Fine-tuning Requirements:
The models were trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service (Source: 2409.12191v2.pdf, p. 8). The training process utilized PyTorch 2.1.2 with CUDA 11.8 and employed 3D parallelism (Data Parallelism, Tensor Parallelism, and Pipeline Parallelism) to scale the training across multiple GPUs. This indicates that training or significant fine-tuning requires a distributed, multi-GPU cluster environment (Source: 2409.12191v2.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
- **Performance on Specific Benchmarks:** On the MMMU benchmark for college-level problem-solving, the model still lags behind GPT-4o to some extent, indicating room for improvement in handling highly complex problems (Source: 2409.12191v2.pdf, p. 9).
- **Vision-Language Navigation:** The model's performance on VLN tasks (R2R, REVERIE) falls significantly behind specialized models. This is attributed to the challenge of accurately modeling maps and locations in a 3D environment from multiple images (Source: 2409.12191v2.pdf, p. 13).
- **Long Video Comprehension:** For the Video-MME benchmark, the number of frames extracted per video was limited to 768 during evaluation. This may impact performance on longer videos, and future work will focus on extending the model to support longer sequences (Source: 2409.12191v2.pdf, p. 12).
- **Image Resolution Impact:** While the model is robust to varying image sizes, excessive enlargement of very small images can cause them to deviate from the training data distribution, leading to a performance decline in certain tasks like OCR (Source: 2409.12191v2.pdf, p. 14).

### Recommendations:
Insufficient information.

---