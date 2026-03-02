## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the Qwen Team at Alibaba Group (2409.12191.pdf, p. 1). The authors of the corresponding research paper are Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Yang Fan, Kai Dang, Mengfei Du, Xuancheng Ren, Rui Men, Dayiheng Liu, Chang Zhou, Jingren Zhou, and Junyang Lin (2409.12191.pdf, p. 1).

### Model date:
The associated research paper was submitted to arXiv with its second version on October 3, 2024 (2409.12191.pdf, p. 1). The cutoff date for the model's data knowledge is June 2023 (2409.12191.pdf, p. 5).

### Model version:
This model is part of the Qwen2-VL Series, which is an advanced upgrade of the previous Qwen-VL models (2409.12191.pdf, p. 1). The series includes models with 2 billion, 8 billion, and 72 billion parameters (2409.12191.pdf, p. 3). This specific model is the Qwen2-VL-7B, a performance-optimized model upgraded for text recognition and video understanding capabilities (2409.12191.pdf, p. 3, Table 1). It differs from its predecessors by introducing a "Naive Dynamic Resolution" mechanism for processing images of varying resolutions and "Multimodal Rotary Position Embedding (M-RoPE)" for better fusion of positional information across text, images, and videos (2409.12191.pdf, p. 1).

### Model type:
The model is a Large Vision-Language Model (LVLM) of type `qwen2_vl` (2409.12191.pdf, p. 1; config.json.txt). Its architecture, `Qwen2VLForConditionalGeneration`, consists of a Vision Transformer (ViT) vision encoder and a Qwen2 large language model (LLM) decoder (config.json.txt; 2409.12191.pdf, p. 4).

**Key Architectural Details:**
*   **Vision Encoder (ViT):** It has approximately 675 million parameters, a depth of 32, an embedding dimension of 1280, and 16 attention heads. It is designed to handle both image and video inputs (2409.12191.pdf, p. 3-4; config.json.txt).
*   **Language Model (LLM):** Based on the Qwen2 series, this component has 28 hidden layers, a hidden size of 3584, 28 attention heads (with 4 key-value heads), and an intermediate size of 18944. It uses the "silu" activation function (config.json.txt; 2409.12191.pdf, p. 4).
*   **Naive Dynamic Resolution:** This mechanism allows the model to process images of any resolution by dynamically converting them into a variable number of visual tokens, moving away from a fixed-resolution approach (2409.12191.pdf, p. 4).
*   **Multimodal Rotary Position Embedding (M-RoPE):** An enhancement over traditional 1D-RoPE, M-RoPE decomposes embeddings into temporal, height, and width components to effectively model positional information for text, images, and videos (2409.12191.pdf, p. 4-5).

**Model Size and Context Length:**
*   **Size:** The total size of the model weights is approximately 16.58 GB (model.safetensors.index.json.txt).
*   **Context Length:** The model supports a maximum position embedding of 32768 tokens (config.json.txt).
*   **Vocabulary Size:** 152,064 tokens (config.json.txt).

### Training details:
The model was trained using a three-stage methodology on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service (2409.12191.pdf, p. 5, 8).

**Training Stages:**
1.  **Stage 1:** The Vision Transformer (ViT) component was trained on a vast corpus of image-text pairs to learn semantic understanding. The LLM parameters were frozen during this stage (2409.12191.pdf, p. 5).
2.  **Stage 2:** All model parameters were unfrozen and trained on a wider range of data, including mixed image-text content and visual question answering datasets, for more comprehensive learning (2409.12191.pdf, p. 5-6).
3.  **Stage 3:** The ViT parameters were locked, and the LLM was exclusively fine-tuned using instructional datasets in the ChatML format (2409.12191.pdf, p. 5-6).

**Training Data and Volume:**
*   The model was pre-trained on a cumulative total of 1.4 trillion tokens, comprising 600 billion tokens in the first phase and an additional 800 billion in the second (2409.12191.pdf, p. 5-6).
*   The LLM component was initialized from Qwen2, and the vision encoder was initialized from the ViT derived from DFN (2409.12191.pdf, p. 5).

**Infrastructure and Parallelism:**
*   The training was conducted using PyTorch version 2.1.2 with CUDA 11.8 (2409.12191.pdf, p. 8).
*   A 3D parallelism strategy was employed, combining data parallelism (DP), tensor parallelism (TP), and pipeline parallelism (PP). This was augmented with DeepSpeed's ZeRO-1 optimizer and sequence parallelism to manage memory usage effectively (2409.12191.pdf, p. 8).
*   Techniques like flash-attention and fused operators (LayerNorm, RMSNorm, Adam) were used to enhance training efficiency (2409.12191.pdf, p. 8).

### Paper or other resource for more information:
For more detailed information, please refer to the official research paper and code repository:
*   **Paper:** Wang, P., Bai, S., Tan, S., et al. (2024). *Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution*. arXiv:2409.12191 (2409.12191.pdf).
*   **Code Repository:** The official code is available at https://github.com/QwenLM/Qwen2-VL (2409.12191.pdf, p. 1).

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
(2409.12191.pdf)

### License:
The model is licensed under the Apache License, Version 2.0 (LICENSE.txt).

Under this license, you are permitted to:
*   Use, reproduce, and distribute the work and its derivative forms.
*   Create and distribute derivative works, provided you include a copy of the license, state that you changed the files, and retain original copyright notices.
*   Sublicense the work.

The license does not grant permission to use the trade names, trademarks, service marks, or product names of the licensor (Alibaba Cloud) (LICENSE.txt). The software is provided "AS IS" without warranties of any kind (LICENSE.txt).

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The Qwen2-VL series is designed as a versatile, general-purpose Large Vision-Language Model with a wide range of capabilities (2409.12191.pdf, p. 1, 3).

**Core Capabilities:**
*   **Visual Understanding:** The model can process and understand images of any resolution and aspect ratio, as well as videos with durations exceeding 20 minutes (2409.12191.pdf, p. 3). This includes general chat about images, video understanding, document parsing, and recognizing content in complex visual formats (2409.12191.pdf, p. 2, Figure 1).
*   **Multilingual Support:** It supports multilingual context understanding within images, covering English, Chinese, most European languages, Japanese, Korean, Arabic, and Vietnamese (2409.12191.pdf, p. 3).
*   **Reasoning:** The model demonstrates strong performance in tasks requiring complex reasoning, such as math and code reasoning based on visual inputs (2409.12191.pdf, p. 2, Figure 1).
*   **Agent Capabilities:** With advanced reasoning and decision-making abilities, the model can function as a visual agent for device operation (e.g., mobile phones) and other sequential decision-making tasks (2409.12191.pdf, p. 3, 7).

**Input-Output Structure:**
The model uses the ChatML format for interactions. Inputs can be a mix of text and visual content (images/videos). The model generates textual responses, which can include formatted text like bounding box coordinates for visual grounding tasks (2409.12191.pdf, p. 6-7).

### Primary intended users:
The model is intended for researchers and developers in the field of artificial intelligence who wish to build upon or utilize its capabilities in a variety of applications and research projects (2409.12191.pdf, p. 16).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model uses a specific chat template for formatting conversations, which is defined in `chat_template.json.txt`. The format, known as ChatML, structures the conversation with special tokens to delineate roles (system, user, assistant) and content (text, images, videos) (2409.12191.pdf, p. 6).

**Example of Dialogue Data Format (ChatML):**
```
<|im_start|>user
<|vision_start|>Picture1.jpg<|vision_end|><|vision_start|>Picture2.jpg<|vision_end|>What do the two pictures have in common?<|im_end|>
<|im_start|>assistant
Both pictures are of SpongeBob SquarePants.<|im_end|>
<|im_start|>user
What is happening in the video?<|vision_start|>video.mp4<|vision_end|><|im_end|>
<|im_start|>assistant
The protagonist in the video is frying an egg.<|im_end|>
```
(Source: 2409.12191.pdf, p. 6)

**Example of Visual Grounding Output:**
The model can generate bounding box coordinates to ground its textual descriptions in the image.
```
<|vision_start|>Picture1.jpg<|vision_end|>
<|object_ref_start|>the eyes on a giraffe<|object_ref_end|><|box_start|>(176,106),(232,160)<|box_end|>
```
(Source: 2409.12191.pdf, p. 7)

**Example of Visual Agent Usage:**
The model can be used for agent tasks by defining a set of actions and having the model generate function calls based on visual input.
```
<|im_start|>user
Find a pizza restaurant nearby in Map.<|vision_start|>Screenshot_1.jpg<|vision_end|><|im_end|>
<|im_start|>assistant
Several e-mails are displaying on the phone screen. To open Map, I need go back to the home screen and find the corresponding app icon.
*FUNCTION*: Home *ARGS*: {}
*RESULT*: <|vision_start|>Screenshot_2.jpg<|vision_end|>
*RETURN*: I return to the home screen. Next, I need to find the icon of Map and tap on it.
*FUNCTION*: Tap *ARGS*: {"point": (348,291)}
...
```
(Source: 2409.12191.pdf, p. 7)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Image Resolution and Size:** The model's performance is influenced by the resolution of input images. The "Naive Dynamic Resolution" feature is designed to handle this variability. Ablation studies show that performance on perceptual tasks like InfoVQA and OCRBench can be enhanced by increasing the image size (by upscaling smaller images), though excessively large images can sometimes degrade performance (2409.12191.pdf, p. 14).
*   **Video Length and Sequence Length:** The length of video inputs is a critical factor. The M-RoPE mechanism was introduced to improve the model's ability to handle and extrapolate to longer sequences than seen during training (2409.12191.pdf, p. 5, 15).
*   **Language:** The model's performance on OCR tasks varies by language, as shown in the multilingual OCR benchmarks (2409.12191.pdf, p. 9, Table 3).

### Evaluation factors:
The model was evaluated across several distinct capability dimensions:
*   **General Visual Question Answering:** Assessed using benchmarks like RealWorldQA, MMStar, and MMBench (2409.12191.pdf, p. 9).
*   **Document and Diagram Reading:** Assessed using OCR and document understanding benchmarks like DocVQA, InfoVQA, and OCRBench (2409.12191.pdf, p. 11).
*   **Mathematical Reasoning:** Assessed using MathVista and MathVision datasets (2409.12191.pdf, p. 11).
*   **Video Comprehension:** Assessed using benchmarks like MVBench and Video-MME (2409.12191.pdf, p. 11).
*   **Agent Abilities:** Assessed on tasks including UI operations, robotic control, card games, and navigation (2409.12191.pdf, p. 10, 12-13).
*   **Multilingual OCR:** Performance was specifically evaluated across Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (2409.12191.pdf, p. 9, Table 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of metrics specific to each evaluation benchmark. These include:
*   **Accuracy:** Used for benchmarks like DocVQA, InfoVQA, and MMBench (2409.12191.pdf, p. 9, Table 2).
*   **Score:** A cumulative or benchmark-specific score is used for datasets like MME and OCRBench (2409.12191.pdf, p. 9, Table 2).
*   **Success Rate (SR):** Used to evaluate agent tasks such as card games (e.g., BlackJack) and navigation (e.g., R2R) (2409.12191.pdf, p. 10, Table 5).
*   **Goal-Condition Success (GC):** Used in robotic control tasks like ALFRED to measure sub-goal completion (2409.12191.pdf, p. 10, Table 5).
*   **Type Match (TM) and Exact Match (EM):** Used to evaluate the accuracy of function calling in agent tasks, where TM measures correct function selection and EM measures the correctness of the arguments (2409.12191.pdf, p. 10, 12).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess its diverse capabilities. These include, but are not limited to:
*   **General VQA:** RealWorldQA, MMStar, MMVet, MMT-Bench, MMBench, MME, HallusionBench (2409.12191.pdf, p. 9).
*   **Document & Diagram Reading:** DocVQA, InfoVQA, AI2D, ChartQA, TextVQA, OCRBench (2409.12191.pdf, p. 9).
*   **Multilingual OCR:** MTVQA and an internal benchmark covering 8 languages (2409.12191.pdf, p. 9).
*   **Mathematical Reasoning:** MathVista, MathVision (2409.12191.pdf, p. 9).
*   **Video Understanding:** MVBench, PerceptionTest, EgoSchema, Video-MME (2409.12191.pdf, p. 10).
*   **Agent & Grounding:** AITZ (UI Operations), ALFRED (Robotic Control), R2R & REVERIE (Navigation), RefCOCO/+/g (Referring Expression Comprehension) (2409.12191.pdf, p. 10, 12).

### Motivation:
These datasets were chosen to provide an extensive and rigorous evaluation of the model's performance across a wide array of tasks and modalities. The selection covers general perception, complex reasoning, multilingual capabilities, and agentic behaviors to demonstrate the model's advantages and position it against other state-of-the-art models (2409.12191.pdf, p. 8-9).

### Preprocessing:
*   For the Video-MME benchmark, which includes videos up to one hour long, the maximum number of frames extracted per video was limited to 768 during evaluation (2409.12191.pdf, p. 12).
*   In the dynamic resolution ablation study, small images were upscaled to meet a specified `min_pixels` threshold before being input to the model (2409.12191.pdf, p. 14).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pre-trained on a diverse, large-scale dataset with a cumulative total of 1.4 trillion tokens (2409.12191.pdf, p. 6). The data sources primarily consist of cleaned web pages, open-source datasets, and synthetic data (2409.12191.pdf, p. 5). The types of data include:
*   Image-text pairs
*   Optical Character Recognition (OCR) data
*   Interleaved image-text articles
*   Visual question answering datasets
*   Video dialogues
*   Image knowledge datasets
*   Purely textual data (to maintain linguistic proficiency) (2409.12191.pdf, p. 5-6).

For the instruction fine-tuning phase, a dataset in ChatML format was constructed, which included both pure text-based dialogues and multimodal conversational data (e.g., image question-answering, document parsing, video comprehension, and agent-based interactions) (2409.12191.pdf, p. 6).

### Motivation:
The diverse composition of the training data was chosen to be "instrumental in developing a robust multimodal understanding capability" (2409.12191.pdf, p. 5). The inclusion of various data types and tasks aims to build a versatile and robust model capable of handling complex, real-world scenarios and a wide range of instructions across different modalities (2409.12191.pdf, p. 6).

### Preprocessing:
*   **Video Data:** Videos were sampled at two frames per second. To balance computational demand with information preservation, the resolution of each video frame was dynamically adjusted to limit the total number of tokens per video to 16,384 (2409.12191.pdf, p. 5).
*   **Image Data:** For consistency with video processing, each image was treated as two identical frames (2409.12191.pdf, p. 5).
*   **Image Processor:** The image processor normalizes images using a mean of `[0.48145466, 0.4578275, 0.40821073]` and a standard deviation of `[0.26862954, 0.26130258, 0.27577711]` (preprocessor_config.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The research paper provides extensive results disaggregated by benchmark and model size.
*   **Performance by Task:** Table 2 shows the performance of the Qwen2-VL-72B, 7B, and 2B models across 19 different benchmarks, including DocVQA (94.5 on test for 7B), MME (2326.8 for 7B), and RealWorldQA (70.1 for 7B) (2409.12191.pdf, p. 9).
*   **Performance by Language:** Table 3 shows the multilingual OCR performance of the 72B model on an internal benchmark. For example, it scores 94.5 in Korean, 93.4 in Japanese, and 94.1 in French (2409.12191.pdf, p. 9).
*   **Performance by Model Size:** Figure 6(a) illustrates how performance scales with model size (2B, 8B, 72B) across five capability dimensions: Math, MMMU, General VQA, Video, and OCR. Performance generally improves with model size, especially for mathematical abilities (2409.12191.pdf, p. 16).
*   **Performance by Training Data Amount:** Figure 6(b) shows the performance of the Qwen2-VL-7B model on five benchmarks (AI2D, InfoVQA, RealWorldQA, MMStar, MMMU) as the number of training tokens increases during the second pre-training stage (2409.12191.pdf, p. 16).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   The model weights are stored in `bfloat16` format (config.json.txt).
*   The total size of the model on disk is approximately 16.58 GB (model.safetensors.index.json.txt). Loading the model would require at least this amount of RAM or VRAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
*   The models were trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service, which is a large-scale GPU cluster (2409.12191.pdf, p. 8).
*   The training process utilized a 3D parallelism strategy (Data, Tensor, and Pipeline Parallelism) and required PyTorch 2.1.2 with CUDA 11.8, indicating the need for a multi-GPU environment with significant computational resources (2409.12191.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Insufficient information.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Complex Reasoning:** On the MMMU benchmark for massive multi-discipline understanding, the model still lags behind some closed-source models like GPT-4o, indicating room for improvement in handling highly complex and challenging problem sets (2409.12191.pdf, p. 9).
*   **Long Video Processing:** During the evaluation on the Video-MME benchmark, the number of frames extracted per video was limited to 768. This may have negatively impacted performance on very long videos (2409.12191.pdf, p. 12).
*   **Vision-Language Navigation:** The model's performance on navigation tasks (R2R, REVERIE) is comparable to other generalist models but falls significantly behind specialized VLN models. This gap is attributed to the challenge of generating complete and structured map information from a series of images (2409.12191.pdf, p. 13).
*   **Image Resolution Impact:** While the model is robust to varying image sizes, performance on OCRBench was observed to decline severely if the `min_pixels` threshold was set too high, likely because excessive enlargement of small images pushed them into an out-of-distribution domain (2409.12191.pdf, p. 14).

### Recommendations:
*   **Appropriate Resolution:** Users should be aware that merely increasing image size does not always improve performance. It is important to choose an appropriate resolution for different image types and tasks (2409.12191.pdf, p. 14).
*   **Future Research:** The paper suggests that future work will focus on extending the model to support longer sequences to better accommodate long videos (2409.12191.pdf, p. 12).
*   **Open Access:** The model weights are openly accessible, enabling researchers and developers to use them for a wide variety of applications and research projects (2409.12191.pdf, p. 16).

---