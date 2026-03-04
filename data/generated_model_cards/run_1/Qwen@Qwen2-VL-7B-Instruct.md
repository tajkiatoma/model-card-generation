## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the Qwen Team at Alibaba Group (2409.12191.pdf, p. 1). The copyright notice also attributes the work to Alibaba Cloud (LICENSE.txt).

### Model date:
- **Paper Submission (v2):** October 3, 2024 (2409.12191.pdf, p. 1).
- **Training Data Cutoff:** June 2023 (2409.12191.pdf, p. 5).

### Model version:
This is the Qwen2-VL series, which is an advanced upgrade of the previous Qwen-VL models (2409.12191.pdf, p. 1). The series includes three open-weight models with different parameter counts:
- **Qwen2-VL-2B:** The most efficient model, designed for on-device execution (2409.12191.pdf, p. 3, Table 1).
- **Qwen2-VL-7B:** A performance-optimized model with significant upgrades for text recognition and video understanding (2409.12191.pdf, p. 3, Table 1).
- **Qwen2-VL-72B:** The most capable model, with improvements in visual reasoning, instruction-following, and agent capabilities (2409.12191.pdf, p. 3, Table 1).

The model type is specified as `qwen2_vl` and was developed with `transformers_version` 4.41.2 (config.json.txt).

### Model type:
The model is a Large Vision-Language Model (LVLM) belonging to the `Qwen2VLForConditionalGeneration` architecture (config.json.txt). It follows a common LVLM structure of a visual encoder connected to a Large Language Model (LLM) via a cross-modal connector (2409.12191.pdf, p. 1).

**Key Components:**
- **Vision Encoder:** A Vision Transformer (ViT) with approximately 675 million parameters, which handles both image and video inputs (2409.12191.pdf, p. 4).
- **Language Model:** The Qwen2 series of language models (2409.12191.pdf, p. 4).

**Architectural Details:**
- **Parameters:** The series includes models with 2B, 8B, and 72B parameters (2409.12191.pdf, p. 3). The specific model in this repository has 28 hidden layers, a hidden size of 3584, an intermediate size of 18944, 28 attention heads, and 4 key-value heads (config.json.txt).
- **Context Length:** The model supports a maximum context length of 32,768 tokens (config.json.txt, tokenizer_config.json.txt).
- **Size:** The total size of the model weights is 16.58 GB (model.safetensors.index.json.txt).
- **Vocabulary Size:** 152,064 (config.json.txt).
- **Key Innovations:**
    - **Naive Dynamic Resolution:** Allows the model to process images of any resolution by converting them into a variable number of visual tokens (2409.12191.pdf, p. 4).
    - **Multimodal Rotary Position Embedding (M-RoPE):** A novel position embedding that decomposes embeddings into temporal, height, and width components to effectively model positional information for text, images, and videos (2409.12191.pdf, p. 4-5).

### Training details:
The model was trained using a three-stage methodology (2409.12191.pdf, p. 5):
1.  **Stage 1:** Training the Vision Transformer (ViT) component on a large corpus of image-text pairs to learn semantic understanding.
2.  **Stage 2:** Unfreezing all parameters and training with a wider range of data, including mixed image-text content and visual question-answering datasets.
3.  **Stage 3:** Locking the ViT parameters and performing exclusive fine-tuning of the LLM on instructional datasets.

**Training Data:**
- The model was pre-trained on a cumulative total of 1.4 trillion tokens, including both text and image tokens (2409.12191.pdf, p. 6).
- The instruction fine-tuning phase used the ChatML format to construct data for tasks like image QA, document parsing, video comprehension, and agent-based interactions (2409.12191.pdf, p. 6).

**Training Infrastructure:**
- **Hardware:** Trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service (2409.12191.pdf, p. 8).
- **Software:** Used PyTorch version 2.1.2 with CUDA 11.8, leveraging FlashAttention and other fused operators for efficiency (2409.12191.pdf, p. 8).
- **Parallelism:** Employed 3D parallelism, combining data parallelism (DP), tensor parallelism (TP), and pipeline parallelism (PP) to scale training (2409.12191.pdf, p. 8).

### Paper or other resource for more information:
- **Academic Paper:** Wang, P., Bai, S., Tan, S., Wang, S., Fan, Z., Bai, J., ... & Lin, J. (2024). *Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution*. arXiv preprint arXiv:2409.12191 (2409.12191.pdf).
- **Code Repository:** The official code is available at `https://github.com/QwenLM/Qwen2-VL` (2409.12191.pdf, p. 1).

### Citation details:
```bibtex
@misc{wang2024qwen2vl,
      title={Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution}, 
      author={Peng Wang and Shuai Bai and Sinan Tan and Shijie Wang and Zhihao Fan and Jinze Bai and Keqin Chen and Xuejing Liu and Jialin Wang and Wenbin Ge and Yang Fan and Kai Dang and Mengfei Du and Xuancheng Ren and Rui Men and Dayiheng Liu and Chang Zhou and Jingren Zhou and Junyang Lin},
      year={2024},
      eprint={2409.12191},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(Derived from 2409.12191.pdf, p. 1)

### License:
The model is licensed under the Apache License, Version 2.0. This license allows for commercial use, modification, distribution, and private use. Users must include a copy of the license and copyright notice and state any changes made to the files. The license does not grant trademark rights and is provided "AS IS" without warranties (LICENSE.txt).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The Qwen2-VL series is designed as a versatile, general-purpose Large Vision-Language Model (LVLM) with a wide range of capabilities (2409.12191.pdf, p. 1, 7). Its primary uses include:
- **General Visual Question Answering:** Answering questions based on the content of images and videos (2409.12191.pdf, p. 9).
- **Document and Diagram Understanding:** Comprehending text and graphical information in documents, charts, and infographics (2409.12191.pdf, p. 11).
- **Multilingual OCR:** Recognizing and understanding text in multiple languages within images, including English, Chinese, most European languages, Japanese, Korean, Arabic, and Vietnamese (2409.12191.pdf, p. 3, 11).
- **Mathematical Reasoning:** Solving math problems embedded in visual contexts (2409.12191.pdf, p. 11).
- **Video Understanding:** Comprehending content in videos up to 20 minutes in length, including question answering, dialogue, and content creation (2409.12191.pdf, p. 3, 11).
- **Visual Agent Capabilities:** Performing sequential decision-making tasks such as UI operations on mobile devices, robotic control, and navigation based on visual inputs and text instructions (2409.12191.pdf, p. 7).
- **Visual Grounding:** Localizing and referencing specific objects or regions within an image described by text (2409.12191.pdf, p. 6).

The model accepts interleaved text, image, and video inputs and generates textual responses (2409.12191.pdf, p. 1, 4).

### Primary intended users:
The model is intended for researchers and developers in the field of AI who wish to harness its capabilities for a variety of applications and research projects (2409.12191.pdf, p. 16).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model. 

The model uses a specific chat template for formatting inputs, which supports roles like `system`, `user`, and `assistant`. Multimodal inputs (images and videos) are incorporated using special tokens.

**Chat Template Structure:**
The input should be formatted as a sequence of messages. If the first message is not from the `system`, a default system prompt "You are a helpful assistant." is added. Each message is enclosed by `<|im_start|>` and `<|im_end|>` tokens.

- **Text Input:**
  `<|im_start|>user\nWhat is in the image?<|im_end|>\n`
- **Image/Video Input:**
  Image and video content is represented by special placeholder tokens within the user's message.
  - For an image: `<|vision_start|><|image_pad|><|vision_end|>`
  - For a video: `<|vision_start|><|video_pad|><|vision_end|>`

**Example of a multimodal conversation:**
```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Picture 1: <|vision_start|><|image_pad|><|vision_end|>What is this?<|im_end|>
<|im_start|>assistant
This is a cat.<|im_end|>
```
(chat_template.json.txt, tokenizer_config.json.txt)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
- **Image Resolution and Aspect Ratio:** The model is designed to handle images of any resolution and aspect ratio through its "Naive Dynamic Resolution" mechanism, which converts images into a variable number of tokens (2409.12191.pdf, p. 4).
- **Language:** The model supports multilingual context understanding within images, including English, Chinese, most European languages, Japanese, Korean, Arabic, and Vietnamese (2409.12191.pdf, p. 3).
- **Video Duration:** The model is capable of understanding videos over 20 minutes in length (2409.12191.pdf, p. 3).

### Evaluation factors:
The model was evaluated across the factors mentioned above:
- **Resolution:** Performance was tested on benchmarks requiring high-resolution understanding, such as DocVQA and OCRBench (2409.12191.pdf, p. 9, Table 2).
- **Language:** Multilingual OCR capabilities were evaluated on the MTVQA dataset and an internal benchmark covering Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (2409.12191.pdf, p. 9, Table 3).
- **Video Duration:** Video understanding was evaluated on benchmarks with varying video lengths, including Video-MME which contains videos up to one hour (2409.12191.pdf, p. 10, 12).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of metrics specific to different tasks and benchmarks (2409.12191.pdf, p. 9-10):
- **General VQA and Reasoning:** Accuracy or benchmark-specific scores are reported for datasets like MMMU, DocVQA, MMBench, and MathVista (2409.12191.pdf, p. 9, Table 2).
- **Agent Tasks:**
    - **Success Rate (SR):** The rate of successfully completing a task.
    - **Goal-Condition Success (GC):** The rate of satisfying all sub-goals of a task.
    - **Type Match (TM):** The accuracy of selecting the correct function or action type.
    - **Exact Match (EM):** The accuracy of both the function selection and its arguments.
    (2409.12191.pdf, p. 10, Table 5)

### Decision thresholds:
Insufficient information.

### Variation approaches:
The model's performance was measured on the official test or validation sets of the respective benchmarks mentioned in the paper (2409.12191.pdf, Section 3).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its diverse capabilities (2409.12191.pdf, Section 3, p. 9-13):
- **General VQA:** RealWorldQA, MMStar, MMVet, MMT-Bench, MMBench, MME, HallusionBench.
- **Document & OCR:** DocVQA, InfoVQA, ChartQA, TextVQA, OCRBench, MTVQA, AI2D.
- **Mathematical Reasoning:** MathVista, MathVision.
- **Referring Expression Comprehension:** RefCOCO, RefCOCO+, RefCOCOg.
- **Video Understanding:** MVBench, PerceptionTest, EgoSchema, Video-MME.
- **Agent Capabilities:** AITZ (UI Operations), ALFRED (Robotic Control), RL4VLM (Card Games), R2R and REVERIE (Vision-Language Navigation).

### Motivation:
These datasets were chosen to provide a comprehensive and rigorous evaluation of the model's performance across its intended use cases, including general visual perception, document understanding, multilingual recognition, video comprehension, and agent abilities (2409.12191.pdf, p. 9).

### Preprocessing:
- For the Video-MME benchmark, the maximum number of frames extracted per video was limited to 768 during evaluation (2409.12191.pdf, p. 12).
- For dynamic resolution evaluation, images were upscaled to surpass a specified `min_pixels` threshold before being input to the model (2409.12191.pdf, p. 14).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a cumulative total of 1.4 trillion tokens (2409.12191.pdf, p. 6). The training data is a diverse, multimodal corpus sourced from cleaned web pages, open-source datasets, and synthetic data (2409.12191.pdf, p. 5). The dataset types include:
- Image-text pairs
- Optical Character Recognition (OCR) data
- Interleaved image-text articles
- Visual Question Answering (VQA) datasets
- Video dialogues
- Image knowledge datasets
- Purely textual data (2409.12191.pdf, p. 5-6)

### Motivation:
The diverse data composition was chosen to develop a robust multimodal understanding capability, enabling the model to learn the intricate relationships between visual and textual information and handle a wide range of instructions and modalities (2409.12191.pdf, p. 5-6).

### Preprocessing:
- **Dialogue Formatting:** Instruction-tuning data was constructed using the ChatML format, where interactions are marked with `<|im_start|>` and `<|im_end|>` tokens (2409.12191.pdf, p. 6).
- **Visual Data Demarcation:** Visual inputs (images/videos) are demarcated by `<|vision_start|>` and `<|vision_end|>` tokens (2409.12191.pdf, p. 6).
- **Video Sampling:** Videos were sampled at two frames per second. To manage computational load, the resolution of each frame was dynamically adjusted to limit the total number of tokens per video to 16,384 (2409.12191.pdf, p. 5).
- **Image Processing:** Input images are normalized using a mean of `[0.48145466, 0.4578275, 0.40821073]` and a standard deviation of `[0.26862954, 0.26130258, 0.27577711]` (preprocessor_config.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the Qwen2-VL series was benchmarked across various tasks. Below are some key results for the 72B model compared to previous State-of-the-Art (SoTA) and other leading models.

**General & Document VQA Benchmarks (Accuracy %):**
| Benchmark | Previous SoTA | Qwen2-VL-72B |
|---|---|---|
| DocVQA | 94.1 | **96.5** |
| InfoVQA | 82.0 | **84.5** |
| TextVQA | 84.4 | **85.5** |
| RealWorldQA | 72.2 | **77.8** |
| MMStar | 67.1 | **68.3** |
| MathVista | 69.0 | **70.5** |
(2409.12191.pdf, p. 9, Table 2)

**Video Understanding Benchmarks (Accuracy %):**
| Benchmark | GPT-4o | Qwen2-VL-72B |
|---|---|---|
| MVBench | 73.6 | **73.6** |
| PerceptionTest | 68.0 | **68.0** |
| Video-MME | 71.9/77.2 | **71.2/77.8** |
(2409.12191.pdf, p. 10, Table 4)

**Multilingual OCR (Internal Benchmark, Accuracy %):**
| Language | GPT-4o | Qwen2-VL-72B |
|---|---|---|
| French | 89.7 | **94.1** |
| German | 88.3 | **91.5** |
| Italian | 74.1 | **89.8** |
| Russian | 96.8 | **97.2** |
(2409.12191.pdf, p. 9, Table 3)

**Agent Capabilities (Success Rate %):**
| Benchmark | Metric | GPT-4o | Qwen2-VL-72B |
|---|---|---|---|
| AITZ (UI) | EM | 35.3 | **72.1** |
| Number Line | SR | 91.5 | **100.0** |
| ALFRED (Robotics) | SR | - | **67.8** |
| R2R (Navigation) | SR | 43.7 | **51.7** |
(2409.12191.pdf, p. 10, Table 5)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
- The total size of the model weights is approximately 16.58 GB (model.safetensors.index.json.txt).
- The Qwen2-VL-2B model is specifically designed to be efficient enough for on-device execution (2409.12191.pdf, p. 3, Table 1).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service, a large-scale GPU cluster infrastructure (2409.12191.pdf, p. 8). The training process utilized:
- **Software:** PyTorch 2.1.2 and CUDA 11.8 (2409.12191.pdf, p. 8).
- **Parallelism Strategy:** A combination of data parallelism, tensor parallelism, and pipeline parallelism (3D parallelism) was used to scale training, indicating that training requires a multi-GPU, multi-node environment (2409.12191.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

Insufficient information.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
- **Performance Gaps:** The model's performance, while strong, still lags behind top-tier proprietary models like GPT-4o on certain complex, college-level reasoning benchmarks such as MMMU (2409.12191.pdf, p. 9).
- **Specialized Tasks:** For highly specialized tasks like Vision-Language Navigation (VLN), the model's performance is comparable to other generalist models but falls "significantly behind" specialized models. This is attributed to the challenge of accurately modeling 3D environments from 2D images (2409.12191.pdf, p. 13).
- **Long Video Evaluation:** When evaluating on very long videos (e.g., up to one hour in Video-MME), the number of extracted frames was limited to 768, which could potentially impact performance on tasks requiring comprehension of the entire video sequence (2409.12191.pdf, p. 12).

### Recommendations:
- **Future Work:** The developers plan to focus on extending the model to support longer sequences, which would improve its performance on long-video understanding tasks (2409.12191.pdf, p. 12).
- **Open Access:** The model weights are openly accessible to "enable researchers and developers to harness the full potential in a variety of applications and research projects" (2409.12191.pdf, p. 16).

---