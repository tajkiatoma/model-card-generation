## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The Qwen2-VL model series was developed by the Qwen Team at Alibaba Group (2409.12191.pdf, p. 1). The copyright for the model is held by Alibaba Cloud (LICENSE.txt).

### Model date:
The model's knowledge cutoff date is June 2023 (2409.12191.pdf, p. 5). The associated academic paper was submitted on October 3, 2024 (2409.12191.pdf, p. 1).

### Model version:
This model is part of the Qwen2-VL Series, which is an advanced upgrade of the previous Qwen-VL models (2409.12191.pdf, p. 1). The series includes three models of different sizes:
*   **Qwen2-VL-2B:** The most efficient model, with 2 billion parameters (1.5B for the LLM and 675M for the vision encoder), designed for on-device execution. It is intended for scenarios with limited resources (2409.12191.pdf, p. 3, Table 1).
*   **Qwen2-VL-7B:** A performance-optimized model with 8 billion parameters (7.6B for the LLM and 675M for the vision encoder). It offers significant upgrades in text recognition and video understanding (2409.12191.pdf, p. 3, Table 1). This repository corresponds to the 7B version, with a total size of approximately 16.58 GB (model.safetensors.index.json.txt).
*   **Qwen2-VL-72B:** The most capable model, with 72 billion parameters. It features improvements in visual reasoning, instruction-following, and agent capabilities for complex tasks (2409.12191.pdf, p. 3, Table 1).

### Model type:
Qwen2-VL is a series of Large Vision-Language Models (LVLMs) (2409.12191.pdf, p. 1). The architecture consists of a Vision Transformer (ViT) vision encoder and a Qwen2 Large Language Model (LLM) decoder (2409.12191.pdf, p. 3-4).

*   **Architecture Details:**
    *   **Vision Encoder:** A Vision Transformer (ViT) with approximately 675 million parameters is used for handling both image and video inputs (2409.12191.pdf, p. 4).
    *   **Language Model:** The Qwen2 series of language models serves as the decoder (2409.12191.pdf, p. 4).
    *   **Key Mechanisms:** The model introduces two key architectural improvements:
        1.  **Naive Dynamic Resolution:** Allows the model to process images of any resolution by dynamically converting them into a variable number of visual tokens. This is supported by using 2D Rotary Position Embedding (2D-RoPE) in the ViT (2409.12191.pdf, p. 4).
        2.  **Multimodal Rotary Position Embedding (M-RoPE):** Decomposes the rotary embedding into temporal, height, and width components to effectively model positional information across text, images, and videos (2409.12191.pdf, p. 4-5).
*   **Model Size:** This repository contains the 7B version, which has a total size of 16,582,751,232 bytes (~16.58 GB) (model.safetensors.index.json.txt).
*   **Context Length:** The model supports a maximum context length of 32,768 tokens (tokenizer_config.json.txt).
*   **Tokenizer:** The model uses the Qwen2Tokenizer, which is a Byte-Pair Encoding (BPE) tokenizer with a vocabulary size of 151,643 (tokenizer_config.json.txt; tokenizer_summary.json.txt).

### Training details:
The model was trained using a three-stage methodology (2409.12191.pdf, p. 5):
1.  **Stage 1 (ViT Training):** The Vision Transformer (ViT) component is trained on a large corpus of image-text pairs to learn visual-textual correlations.
2.  **Stage 2 (Full-Model Pre-training):** All parameters are unfrozen, and the model is trained on a wider range of data, including mixed image-text content and visual question-answering datasets. The total pre-training data amounts to a cumulative 1.4 trillion tokens (p. 6).
3.  **Stage 3 (LLM Fine-tuning):** The ViT parameters are locked, and only the LLM is fine-tuned using instructional datasets in the ChatML format.

The training was performed on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service using 3D parallelism (Data Parallelism, Tensor Parallelism, and Pipeline Parallelism), DeepSpeed's ZeRO-1 optimizer, and Sequence Parallelism to manage memory usage. The software stack included PyTorch 2.1.2, CUDA 11.8, and flash-attention for efficient training (2409.12191.pdf, p. 8).

### Paper or other resource for more information:
*   **Academic Paper:** "Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution" provides a comprehensive overview of the model's architecture, training, and evaluation (2409.12191.pdf).
*   **Code Repository:** The official code is available at `https://github.com/QwenLM/Qwen2-VL` (2409.12191.pdf, p. 1).

### Citation details:
```bibtex
@misc{wang2024qwen2vl,
      title={Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution}, 
      author={Peng Wang and Shuai Bai and Sinan Tan and Shijie Wang and Zhihao Fan and Jinze Bai and Keqin Chen and Xuejing Liu and Jialin Wang and Wenbin Ge and Yang Fan and Kai Dang and Mengfei Du and Xuancheng Ren and Rui Men and Dayiheng Liu and Chang Zhou and Jingren Zhou and Junyang Lin and Qwen Team},
      year={2024},
      eprint={2409.12191},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(2409.12191.pdf)

### License:
The model is licensed under the Apache License, Version 2.0. The license grants users a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare derivative works of, publicly display, perform, sublicense, and distribute the work. It also includes a grant of patent license under specific conditions. The license does not grant permission to use the trade names or trademarks of the licensor, Alibaba Cloud (LICENSE.txt).

### Contact:
For questions, issues, or feedback, users are directed to the model's official GitHub repository: `https://github.com/QwenLM/Qwen2-VL` (2409.12191.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The Qwen2-VL series is designed as a versatile, general-purpose Large Vision-Language Model (LVLM) with a wide range of capabilities (2409.12191.pdf, p. 1, 3). Its primary intended uses include:
*   **General Visual Comprehension:** Understanding and answering questions about images and videos (2409.12191.pdf, p. 1).
*   **Multilingual OCR:** Recognizing and understanding text within images across multiple languages, including English, Chinese, most European languages, Japanese, Korean, Arabic, and Vietnamese (2409.12191.pdf, p. 3).
*   **Document and Diagram Understanding:** Parsing and reasoning about content in documents, charts, and scientific diagrams (2409.12191.pdf, p. 11).
*   **Mathematical Reasoning:** Solving mathematical problems presented in visual contexts (2409.12191.pdf, p. 11).
*   **Video Analysis:** Comprehending and answering questions about videos, including extended-duration videos over 20 minutes in length (2409.12191.pdf, p. 3).
*   **Visual Grounding:** Linking textual descriptions to specific regions (bounding boxes) within an image (2409.12191.pdf, p. 6-7).
*   **Visual Agent Capabilities:** Performing sequential decision-making tasks by interacting with visual interfaces, such as mobile phone UI operations (2409.12191.pdf, p. 3, 7).

The model takes multimodal input (text, images, videos) and generates textual output (2409.12191.pdf, p. 1).

### Primary intended users:
The primary intended users are researchers and developers in the field of artificial intelligence who can harness the model's capabilities for a variety of applications and research projects (2409.12191.pdf, p. 16).

### Out-of-scope uses:
Insufficient information

---

## How to Use
This section outlines how to use the model.

The model uses a specific chat template for formatting conversational input. Special tokens are used to demarcate different parts of the input, such as user/assistant turns and visual content (2409.12191.pdf, p. 6).

**Chat Template:**
The model follows the ChatML format, where each message is enclosed by `<|im_start|>` and `<|im_end|>` tokens. Visual content (images/videos) is marked with `<|vision_start|>` and `<|vision_end|>` (tokenizer_config.json.txt; 2409.12191.pdf, p. 6).

```jinja
{% set image_count = namespace(value=0) %}{% set video_count = namespace(value=0) %}{% for message in messages %}{% if loop.first and message['role'] != 'system' %}<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n{% endif %}<|im_start|>{{ message['role'] }}\n{% if message['content'] is string %}{{ message['content'] }}<|im_end|>\n{% else %}{% for content in message['content'] %}{% if content['type'] == 'image' or 'image' in content or 'image_url' in content %}{% set image_count.value = image_count.value + 1 %}{% if add_vision_id %}Picture {{ image_count.value }}: {% endif %}<|vision_start|><|image_pad|><|vision_end|>{% elif content['type'] == 'video' or 'video' in content %}{% set video_count.value = video_count.value + 1 %}{% if add_vision_id %}Video {{ video_count.value }}: {% endif %}<|vision_start|><|video_pad|><|vision_end|>{% elif 'text' in content %}{{ content['text'] }}{% endif %}{% endfor %}<|im_end|>\n{% endif %}{% endfor %}{% if add_generation_prompt %}<|im_start|>assistant\n{% endif %}
```
(chat_template.json.txt)

**Example Usage (Visual Grounding):**
To specify a bounding box for a region in an image, the coordinates are normalized to a [0, 1000) range and formatted as `(X_top_left, Y_top_left), (X_bottom_right, Y_bottom_right)`. The description is enclosed in `<|object_ref_start|>`/`<|object_ref_end|>` and the coordinates in `<|box_start|>`/`<|box_end|>` (2409.12191.pdf, p. 6-7).

*   **Input:**
    `<|vision_start|>Picture1.jpg<|vision_end|>`
    `<|object_ref_start|>the red car<|object_ref_end|><|box_start|>(701,531),(869,675)<|box_end|>`
*   **Sample Output:** The model can identify and locate the specified object in the image (2409.12191.pdf, p. 43, Figure 24).

**Example Usage (Visual Agent):**
The model can act as a visual agent by generating a sequence of actions in a specific format.

*   **Input:**
    `Find a pizza restaurant nearby in Map. <|vision_start|>Screenshot_1.jpg<|vision_end|>`
*   **Sample Output:**
    `*FUNCTION*: Home *ARGS*: {}`
    `*RESULT*: <|vision_start|>Screenshot_2.jpg<|vision_end|>`
    `*RETURN*: I return to the home screen. Next, I need to find the icon of Map and tap on it.`
    (2409.12191.pdf, p. 7)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Model Scale:** The model's performance varies with its size. The series includes 2B, 7B, and 72B parameter versions, with larger models generally showing better performance on complex tasks (2409.12191.pdf, p. 3, 16).
*   **Image Resolution:** The model is designed to handle images of varying resolutions and aspect ratios through its Naive Dynamic Resolution mechanism. Performance can be influenced by the input image size, though the model shows robustness to these variations (2409.12191.pdf, p. 4, 14).
*   **Language:** The model supports multiple languages, and its performance on OCR tasks can vary across them (2409.12191.pdf, p. 3, 9).
*   **Task Complexity:** Performance differs across task types, such as general VQA, document understanding, and mathematical reasoning (2409.12191.pdf, p. 16, Figure 6).

### Evaluation factors:
The model was evaluated based on its performance across a wide array of benchmarks, categorized by capability:
*   General Visual Question Answering
*   Document and Diagram Understanding
*   Mathematical Reasoning
*   Referring Expression Comprehension
*   Video Understanding
*   Visual Agent Capabilities
*   Multilingual OCR
(2409.12191.pdf, p. 9-12)

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The choice of performance metrics is specific to the evaluation benchmark:
*   **Agent Tasks (e.g., AITZ, ALFRED):** Success Rate (SR), Goal-Condition Success (GC), Type Match (TM), and Exact Match (EM) are used (2409.12191.pdf, p. 10, Table 5).
*   **Code Generation (e.g., HumanEval):** Pass@1 scores are reported (2409.12191.pdf, p. 15, Table 18).
*   **General Benchmarks (e.g., DocVQA, MMBench):** Accuracy or benchmark-specific scores are used to measure performance (2409.12191.pdf, p. 9, Table 2).

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess its diverse capabilities. These include, but are not limited to:
*   **General VQA:** RealWorldQA, MMStar, MMVet, MMT-Bench, MMBench, MME, HallusionBench (2409.12191.pdf, p. 9).
*   **Document & Diagram Understanding:** DocVQA, ChartQA, InfoVQA, TextVQA, AI2D, OCRBench (2409.12191.pdf, p. 11).
*   **Mathematical Reasoning:** MathVista, MathVision (2409.12191.pdf, p. 11).
*   **Referring Expression Comprehension:** RefCOCO, RefCOCO+, RefCOCOg (2409.12191.pdf, p. 11).
*   **Video Understanding:** MVBench, PerceptionTest, EgoSchema, Video-MME (2409.12191.pdf, p. 10, 11).
*   **Agent Tasks:** AITZ, ALFRED (in AI2THOR), R2R, REVERIE, and card game environments from RL4VLM (2409.12191.pdf, p. 10, 13).
*   **Multilingual OCR:** MTVQA and an internal benchmark (2409.12191.pdf, p. 9, 11).

### Motivation:
The datasets were chosen to provide a rigorous and extensive evaluation of the model's performance across a wide array of capabilities, including "general visual perception, document understanding, multilingual recognition in images, video comprehension, and agent abilities" (2409.12191.pdf, p. 11).

### Preprocessing:
*   For video evaluation on the Video-MME benchmark, a maximum of 768 frames were extracted per video (2409.12191.pdf, p. 12).
*   For dynamic resolution evaluation, small images were upscaled to surpass a specified `min_pixels` threshold before being input to the model (2409.12191.pdf, p. 14).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a diverse, large-scale dataset totaling approximately 1.4 trillion tokens. The data sources include cleaned web pages, open-source datasets, and synthetic data (2409.12191.pdf, p. 5-6). The dataset is composed of:
*   Image-text pairs
*   Optical Character Recognition (OCR) data
*   Interleaved image-text articles
*   Visual Question Answering (VQA) datasets
*   Video dialogues
*   Image knowledge datasets
*   Purely textual data

The instruction fine-tuning dataset was constructed in the ChatML format and includes multimodal conversational data for tasks like image VQA, document parsing, video comprehension, and agent-based interactions (2409.12191.pdf, p. 6).

### Motivation:
The diverse data composition was chosen to develop a "robust multimodal understanding capability" and to enable the model to handle a wide range of instructions across various modalities (2409.12191.pdf, p. 5-6).

### Preprocessing:
*   **Video Data:** Videos were sampled at two frames per second. To balance computational load and comprehension, the resolution of each video frame was dynamically adjusted to limit the total number of tokens per video to 16,384 (2409.12191.pdf, p. 5).
*   **Image Data:** Images are treated as two identical frames for consistency with video processing (2409.12191.pdf, p. 5). The Naive Dynamic Resolution mechanism processes images of varying resolutions into a variable number of tokens. A simple MLP layer is used to compress adjacent 2x2 visual tokens into a single token to reduce sequence length before entering the LLM (2409.12191.pdf, p. 4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the Qwen2-VL series is reported for each model size (2B, 7B, and 72B) across various benchmarks.
*   **General Benchmark Performance:** Table 2 in the paper shows scores for all three model sizes on benchmarks like MMMU, DocVQA, TextVQA, RealWorldQA, and MMStar. For example, on RealWorldQA, the scores are 62.9 (2B), 70.1 (7B), and 77.8 (72B) (2409.12191.pdf, p. 9).
*   **Multilingual OCR Performance:** Table 3 shows the 72B model's OCR performance across Korean (94.5), Japanese (93.4), French (94.1), German (91.5), Italian (89.8), Russian (97.2), Vietnamese (73.0), and Arabic (70.7) (2409.12191.pdf, p. 9).
*   **Video Benchmark Performance:** Table 4 shows scores for all three models on benchmarks like MVBench and PerceptionTest. For MVBench, the scores are 63.2 (2B), 67.0 (7B), and 73.6 (72B) (2409.12191.pdf, p. 10).
*   **Performance by Capability:** Figure 6a illustrates how performance scales with model size across five capability dimensions: OCR, Video, General VQA, MMMU, and Math. Math capabilities show a strong positive correlation with model size (2409.12191.pdf, p. 16).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   The Qwen2-VL-2B model is the most efficient and is designed to run on-device (2409.12191.pdf, p. 3, Table 1).
*   The total size of the Qwen2-VL-7B model weights is approximately 16.58 GB (model.safetensors.index.json.txt).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The models were trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service, a large-scale GPU cluster (2409.12191.pdf, p. 8). The training process utilized:
*   **Software:** PyTorch 2.1.2, CUDA 11.8, flash-attention, and various fused operators (2409.12191.pdf, p. 8).
*   **Parallelism:** A combination of 3D parallelism (data, tensor, and pipeline parallelism), sequence parallelism, and ZeRO-1 optimizer was used, indicating that training requires a multi-GPU, multi-node environment (2409.12191.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Complex Reasoning:** On the MMMU benchmark, which assesses college-level problem-solving, the model still lags behind some top-tier proprietary models like GPT-4o, indicating room for improvement in handling highly complex and challenging problems (2409.12191.pdf, p. 9).
*   **Long Video Comprehension:** During evaluation on the Video-MME benchmark, the number of frames extracted per video was limited to 768. This may impact the model's performance on videos longer than what this limit allows (approximately 6.4 minutes at 2 FPS) (2409.12191.pdf, p. 12).
*   **Vision-Language Navigation:** The model's performance on navigation tasks (R2R, REVERIE) falls significantly behind specialized models. This is attributed to the challenge of accurately modeling maps and locations in a 3D environment from 2D images (2409.12191.pdf, p. 13).

### Recommendations:
*   The open-weight models are provided to "enable researchers and developers to harness the full potential in a variety of applications and research projects" (2409.12191.pdf, p. 16).
*   Future work will focus on extending the model's capabilities to support longer video sequences (2409.12191.pdf, p. 12).