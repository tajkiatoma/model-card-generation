## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the MiniCPM-V Team at OpenBMB (arXiv:2408.01800v1.pdf, p. 1).

### Model date:
The MiniCPM-V series includes several models released in 2024 (arXiv:2408.01800v1.pdf, p. 2):
*   **MiniCPM-V 1.0:** Launched in February 2024.
*   **MiniCPM-V 2.0:** Introduced in April 2024.
*   **MiniCPM-Llama3-V 2.5:** Released in May 2024.

The associated research paper was submitted on August 3, 2024 (arXiv:2408.01800v1.pdf, p. 1).

### Model version:
This model is version 2.5 (config.json). It is the third model in the MiniCPM-V series and differs from previous versions in several key aspects (arXiv:2408.01800v1.pdf, Table 3, p. 13):
*   **Base LLM:** It uses Llama3-Instruct 8B as its base language model, whereas versions 1.0 and 2.0 used MiniCPM 2B.
*   **Alignment:** It employs RLAIF-V for alignment to reduce hallucinations, an improvement over version 2.0 which used RLHF-V, and version 1.0 which had no alignment phase.
*   **Resolution and Aspect Ratio:** Like version 2.0, it supports high-resolution images (1.8M pixels, e.g., 1344x1344) with any aspect ratio, an upgrade from version 1.0's fixed, lower resolution (0.2M pixels).
*   **Training:** It utilizes all three pre-training stages and both parts of the Supervised Fine-Tuning (SFT) data, similar to version 2.0.

### Model type:
The model is a Multimodal Large Language Model (MLLM) of type `MiniCPMV` (config.json). It is designed for multimodal dialogue tasks (task_summary.json).

**Architecture:**
The model's architecture consists of three main modules (arXiv:2408.01800v1.pdf, Section 3.1, p. 5):
1.  **Visual Encoder:** A SigLIP SoViT-400m/14 model is used to encode input images. It employs an adaptive visual encoding approach to handle high-resolution images of various aspect ratios (arXiv:2408.01800v1.pdf, p. 5).
2.  **Compression Layer:** A perceiver resampler with one layer of cross-attention compresses the visual tokens from the encoder into a smaller, fixed number of tokens (96 queries for this version) (arXiv:2408.01800v1.pdf, p. 6; config.json).
3.  **Large Language Model (LLM):** The compressed visual tokens are fed along with text input into a LlamaForCausalLM for conditional text generation (modeling_minicpmv.py). The base LLM for this version is Llama3-Instruct 8B (arXiv:2408.01800v1.pdf, Table 3, p. 13).

**Model Size and Parameters:**
*   **Total Size:** Approximately 34.15 GB (model.safetensors.index.json).
*   **LLM Hidden Size:** 4096 (config.json).
*   **LLM Number of Hidden Layers:** 32 (config.json).
*   **LLM Attention Heads:** 32 query heads and 8 key/value heads (config.json).
*   **Vision Hidden Size:** 1152 (config.json).
*   **Vision Number of Hidden Layers:** 27 (config.json).
*   **Vocabulary Size:** 128,256 (config.json).
*   **Context Length:** 8192 tokens (config.json).

### Training details:
The model's training process consists of three main phases: pre-training, supervised fine-tuning (SFT), and RLAIF-V alignment (arXiv:2408.01800v1.pdf, Section 4, p. 6).

**1. Pre-training:** This phase aims to align the visual modules with the LLM's input space and is divided into three stages (arXiv:2408.01800v1.pdf, Section 4.1, p. 7).
*   **Stage 1:** The compression layer is warmed up using 200M image-caption pairs, with other modules frozen. Image resolution is 224x224.
*   **Stage 2:** The visual encoder is trained to handle higher resolution (448x448) using an additional 200M image-caption pairs.
*   **Stage 3:** Both the compression layer and visual encoder are trained using the adaptive visual encoding strategy on high-resolution inputs. OCR data is introduced in this stage to enhance OCR capabilities. The LLM remains frozen.
*   **Techniques Used:**
    *   **Caption Rewriting:** A fine-tuned LLM is used to convert low-quality web captions into cleaner question-answer pairs.
    *   **Data Packing:** Multiple training samples are packed into a single fixed-length sequence to improve memory efficiency and accelerate training by 2-3 times.

**2. Supervised Fine-tuning (SFT):** After pre-training, all model parameters are unfrozen and fine-tuned on high-quality visual question-answering datasets to learn knowledge and interaction capabilities (arXiv:2408.01800v1.pdf, Section 4.2, p. 8). The data is split into two parts, which are concatenated and fed sequentially:
*   **Part 1:** Focuses on basic recognition capabilities using traditional QA/captioning datasets with short responses.
*   **Part 2:** Enhances capabilities for generating detailed responses and following complex instructions, using datasets with long responses and complex interactions.

**3. RLAIF-V (AI Feedback Alignment):** To reduce hallucinations and improve trustworthiness, the model is aligned using AI feedback (arXiv:2408.01800v1.pdf, Section 4.3, p. 9).
*   **Response Generation:** The policy model generates multiple responses for a given instruction.
*   **Feedback Collection:** Responses are broken down into atomic claims. An open-source MLLM (LLaVA-NeXT-Yi 34B) scores the correctness of each claim.
*   **Optimization:** A preference dataset is constructed from the scored responses, and the model is optimized using Direct Preference Optimization (DPO).

### Paper or other resource for more information:
*   **Academic Paper:** "MiniCPM-V: A GPT-4V Level MLLM on Your Phone" provides a comprehensive overview of the model series, architecture, training, and evaluation (arXiv:2408.01800v1.pdf).
*   **GitHub Repository:** The official repository can be found at `https://github.com/OpenBMB/MiniCPM-V` (arXiv:2408.01800v1.pdf, p. 1).

### Citation details:
```bibtex
@misc{yao2024minicpmv,
      title={MiniCPM-V: A GPT-4V Level MLLM on Your Phone}, 
      author={Yuan Yao and Tianyu Yu and Ao Zhang and Chongyi Wang and Junbo Cui and Hongji Zhu and Tianchi Cai and Haoyu Li and Weilin Zhao and Zhihui He and Qianyu Chen and Huarong Zhou and Zhensheng Zou and Haoye Zhang and Shengding Hu and Zhi Zheng and Jie Zhou and Jie Cai and Xu Han and Guoyang Zeng and Dahai Li and Zhiyuan Liu and Maosong Sun},
      year={2024},
      eprint={2408.01800},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(Citation derived from arXiv:2408.01800v1.pdf)

### License:
The model code is licensed under the Apache License, Version 2.0 (configuration_minicpm.py).

### Contact:
For questions or feedback, contact `yaoyuanthu@gmail.com` (arXiv:2408.01800v1.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is an efficient, multimodal large language model intended for deployment on end-side devices like mobile phones, personal computers, vehicles, and robotics (arXiv:2408.01800v1.pdf, p. 2). Its primary use is for multimodal dialogue, combining image and text understanding to generate relevant text responses (task_summary.json).

Key capabilities include (arXiv:2408.01800v1.pdf, p. 3, 4):
*   **General Visual Understanding:** Answering questions about images and engaging in conversations about visual content.
*   **Strong OCR Capability:** Accurately reading and interpreting text within images, including screenshots, documents, and tables. It can perform tasks like converting tables to Markdown format.
*   **High-Resolution Image Perception:** The model can process images up to 1.8M pixels (e.g., 1344x1344) at any aspect ratio, enabling fine-grained detail recognition (arXiv:2408.01800v1.pdf, p. 3).
*   **Multilingual Support:** The model supports multimodal interaction in over 30 languages (arXiv:2408.01800v1.pdf, p. 3).
*   **Trustworthy Behavior:** The model is designed to have low hallucination rates, making it more reliable for real-world applications (arXiv:2408.01800v1.pdf, p. 3).

The model takes an image and a sequence of conversational messages as input and generates a text response (modeling_minicpmv.py, `chat` function).

### Primary intended users:
The primary users are developers and researchers building applications for end-side devices that require multimodal understanding. This includes applications in mobile computing, automotive systems, robotics, and personal computing where offline capability, privacy, and energy efficiency are important (arXiv:2408.01800v1.pdf, p. 2).

### Out-of-scope uses:
The model has several limitations that define its out-of-scope uses (arXiv:2408.01800v1.pdf, Section 7, p. 17):
*   **Non-Image Modalities:** The model is not designed to process video or audio inputs.
*   **High-Stakes Scenarios Requiring Perfect Accuracy:** While designed to be trustworthy, the model can still hallucinate. It should not be used in critical applications where errors could lead to harm without human oversight.
*   **Real-Time, Low-Latency Applications on Constrained Devices:** While optimized for on-device deployment, the model's inference speed and latency may not be sufficient for applications requiring real-time interaction, and its performance can be limited by device battery capacity.

---

## How to Use
This section outlines how to use the model.

The model can be used for multimodal chat via the `chat` method. This method takes an image, a list of messages, and a tokenizer as input. It processes the inputs and generates a text response.

Below is a code snippet demonstrating its usage (derived from `modeling_minicpmv.py`):
```python
import torch
from PIL import Image
import json
from transformers import AutoProcessor, AutoModel

# Load the model and processor
model_path = "openbmb/MiniCPM-Llama3-V-2_5"
model = AutoModel.from_pretrained(model_path, trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
model.eval()

# Prepare inputs
image = Image.open('your_image.jpg').convert('RGB')
# Note: msgs should be a list of dictionaries, with 'role' and 'content' keys.
# For a single-turn conversation, the list contains one message from the user.
msgs = [{'role': 'user', 'content': 'What is in this image?'}]

# Set generation parameters
# For sampling-based generation (e.g., for creative or varied responses)
generation_config_sampling = {
    "top_p": 0.8,
    "top_k": 100,
    "temperature": 0.7,
    "do_sample": True,
    "repetition_penalty": 1.05,
    "max_new_tokens": 1024
}

# For beam-search-based generation (e.g., for more deterministic responses)
generation_config_beam = {
    "num_beams": 3,
    "repetition_penalty": 1.2,
    "max_new_tokens": 1024
}

# Generate a response
# The model's chat function internally handles applying the chat template and preprocessing
with torch.inference_mode():
    response = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=processor.tokenizer,
        **generation_config_sampling # or generation_config_beam
    )

print(response)

# Example for streaming output
# Note: stream=True requires sampling=True
stream_response = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=processor.tokenizer,
    stream=True,
    **generation_config_sampling
)

for chunk in stream_response:
    print(chunk, end='', flush=True)

```
(modeling_minicpmv.py, `chat` function)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model's performance varies across the 30+ languages it supports. Its pre-training was focused on English and Chinese, with multilingual capabilities extended through supervised fine-tuning (arXiv:2408.01800v1.pdf, p. 8).
*   **Hardware Device:** The model's performance, particularly latency and throughput, is highly dependent on the end-side device it is deployed on. Factors include the type of processor (CPU, GPU, NPU), available memory, and the specific deployment framework used (arXiv:2408.01800v1.pdf, Section 5, p. 10-12).
*   **Image Resolution and Aspect Ratio:** The model is designed to handle high-resolution images with various aspect ratios, but performance on fine-grained details may still be affected by these properties (arXiv:2408.01800v1.pdf, p. 6).

### Evaluation factors:
The model was evaluated across different languages and hardware devices (arXiv:2408.01800v1.pdf).
*   **Language:** Performance was measured on a translated version of the LLaVA Bench across more than 15 languages, including German, French, Japanese, Korean, and Spanish (arXiv:2408.01800v1.pdf, Figure 8, p. 14).
*   **Hardware Device:** Latency and throughput were evaluated on different devices, including Xiaomi 14 Pro (Snapdragon 8 Gen 3), vivo X100 Pro (Mediatek Dimensity 9300), and Macbook Pro (M1) (arXiv:2408.01800v1.pdf, Figure 7, p. 12).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a wide range of standard academic benchmarks (arXiv:2408.01800v1.pdf, Section 6.2, p. 13):
*   **General Multimodal Capability:** Evaluated using **OpenCompass**, a comprehensive collection of 11 benchmarks including MME, MM-Bench, MMMU, MathVista, and LLaVA Bench.
*   **OCR Capability:** Measured on **OCR-Bench**, **TextVQA**, and **DocVQA**.
*   **Trustworthiness (Hallucination):** Assessed using **Object HalBench**, which reports response-level and mention-level hallucination rates. Lower rates are better.
*   **Multilingual Capability:** Performance on the **LLaVA Bench**, translated into various languages, was evaluated using GPT-4-Turbo as a judge.

### Decision thresholds:
Insufficient information

### Variation approaches:
Insufficient information

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess various capabilities (arXiv:2408.01800v1.pdf, Section 6.2, p. 13; Table 4, p. 13; Table 5, p. 14):
*   **General Benchmarks (via OpenCompass):**
    *   **MME:** A comprehensive evaluation benchmark for multimodal large language models.
    *   **MM-Bench:** A benchmark to evaluate multi-modal models on their reasoning and perception abilities.
    *   **MMMU:** A massive multi-discipline multimodal understanding and reasoning benchmark.
    *   **MathVista:** A benchmark for evaluating mathematical reasoning in visual contexts.
    *   **LLaVA Bench:** A benchmark for evaluating visual instruction following.
    *   **RealWorldQA:** A benchmark for real-world spatial understanding.
*   **OCR Benchmarks:**
    *   **OCR-Bench:** A benchmark for evaluating OCR capabilities.
    *   **TextVQA:** A dataset for visual question answering that requires reading text in images.
    *   **DocVQA:** A dataset for visual question answering on document images.
*   **Hallucination Benchmark:**
    *   **Object HalBench:** A benchmark designed to evaluate object hallucination in model responses.

### Motivation:
These datasets were chosen to provide a comprehensive evaluation across a wide range of fundamental multimodal tasks, including visual question answering, conversation, knowledge and reasoning, OCR, and trustworthiness (hallucination), which are critical for real-world applications (arXiv:2408.01800v1.pdf, p. 13).

### Preprocessing:
Insufficient information

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is composed of large-scale datasets for pre-training and high-quality datasets for supervised fine-tuning.

**Pre-training Data** (arXiv:2408.01800v1.pdf, Table 1, p. 7):
*   **Image Captioning (English):** 410M pairs from COCO, VG, CC3M, CC12M, LAION-COCO, COYO, and LAION-2B.
*   **Image Captioning (Chinese):** 110M pairs from AIC, LAION-2B-Chinese, WuKong, and Zero-Chinese.
*   **OCR+Knowledge (English):** 39M pairs from WIT, IDL, SynthText, SynthDoG-en, and ArxivCap.
*   **OCR+Knowledge (Chinese):** 11M pairs from WIT and LAION-2B-OCR.

**Supervised Fine-tuning (SFT) Data** (arXiv:2408.01800v1.pdf, Table 2, p. 8):
*   **Part-1 (Basic Recognition):** A collection of datasets for tasks like Short Caption (560K), VQA (1.4M), Knowledge (60K), Grounding (570K), Reasoning (135K), Math (125K), OCR (1.7M), and Chat (780K). Sources include Flickr-30K, VQAv2, OKVQA, RefCOCO, DocVQA, etc.
*   **Part-2 (Advanced Capabilities):** A collection of datasets for OCR (690K from sources like ArxivQA, LLaVAR), Instruction Following (1.9M from SVIT, LLaVA-Instruct-150K, ShareGPT4V), and Text-Only conversations (from Ultra-Chat, Alpaca, ShareGPT, etc.).
*   **Multilingual Data:** 90K multilingual data points covering over 36 languages were used for post-SFT to boost multilingual conversation capability (arXiv:2408.01800v1.pdf, p. 9).
*   **RLAIF-V Data:** A preference dataset of 6K pairs was constructed from 3K unique images for DPO (arXiv:2408.01800v1.pdf, p. 9).

### Motivation:
The pre-training data was chosen to align the model's visual and language components and to build a foundation of multimodal knowledge (arXiv:2408.01800v1.pdf, p. 7). The SFT data was selected to impart more specific knowledge and conversational abilities from human annotations. The data was divided into two parts to first bolster basic recognition and then enhance more complex, detailed response generation (arXiv:2408.01800v1.pdf, p. 8).

### Preprocessing:
Several preprocessing techniques were applied during training (arXiv:2408.01800v1.pdf, p. 7):
*   **Data Cleaning:** Image-text pairs with poor correlation or ill-formatted text were removed from the pre-training data.
*   **Caption Rewriting:** An auxiliary LLM, fine-tuned on a small set of GPT-4 annotated samples, was used to rewrite low-quality web captions into a question-answer format to improve data quality.
*   **Data Packing:** To improve efficiency, multiple samples from different sources were packed into a single fixed-length sequence. Position IDs and attention masks were adjusted to prevent interference between packed samples. This strategy resulted in a 2-3x acceleration in the pre-training phase.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the model is reported across various benchmarks and factors.

**Performance on General Benchmarks** (arXiv:2408.01800v1.pdf, Table 4, p. 13):
*   **OpenCompass:** 65.1
*   **MME:** 2024.6
*   **MM-Bench (en):** 77.2
*   **MM-Bench (cn):** 74.2
*   **MMMU (val):** 45.8
*   **MathVista:** 54.3
*   **LLaVA Bench:** 86.7
*   **Object HalBench (Res./Men.):** 10.3% / 5.0%

**Performance on OCR Benchmarks** (arXiv:2408.01800v1.pdf, Table 5, p. 14):
*   **OCRBench:** 725
*   **TextVQA val:** 76.6
*   **DocVQA test:** 84.8

**Performance by Language** (on LLaVA Bench, evaluated by GPT-4-Turbo) (arXiv:2408.01800v1.pdf, Table 7, p. 15):
*   **French:** 72.7
*   **German:** 76.5
*   **Portuguese:** 83.8
*   **Spanish:** 73.9
*   **Japanese:** 88.0
*   **Korean:** 67.9
*   **Thai:** 61.9

**Ablation Study Results** (arXiv:2408.01800v1.pdf, Table 6, p. 15):
*   **With RLAIF-V:** OpenCompass score of 65.1
*   **Without RLAIF-V:** OpenCompass score of 64.5

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **FP16 Precision:** The model in its standard fp16 version requires 16-17 GB of memory (RAM/VRAM) (arXiv:2408.01800v1.pdf, p. 10).
*   **4-bit Quantized:** Using a 4-bit quantization strategy (Q4_K_M mode in GGML), the memory requirement is reduced to around 5 GB, making it suitable for mobile phone deployment (arXiv:2408.01800v1.pdf, p. 10).

### Deploying Requirements:
The model is designed for deployment on end-side devices. It has been tested on various hardware (arXiv:2408.01800v1.pdf, p. 12):
*   **Mobile Phones:** Xiaomi 14 Pro (Snapdragon 8 Gen 3), vivo X100 Pro (Mediatek Dimensity 9300).
*   **Personal Computers:** Macbook Pro (M1).

Performance varies by device and optimization. For example, on a Xiaomi 14 Pro with NPU acceleration, the model achieves an encoding latency of 9.4s and a decoding throughput of 8.2 tokens/s (arXiv:2408.01800v1.pdf, Figure 6 & 7, p. 11-12).

### Training or Fine-tuning Requirements:
Insufficient information

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

A key focus of the model's development was to create a "trustworthy" MLLM with low hallucination rates (arXiv:2408.01800v1.pdf, p. 3).

**Risks and Mitigation:**
*   **Hallucination:** MLLMs are prone to generating responses that are not factually grounded in the input image. This risk is particularly severe in high-stakes scenarios like autonomous driving or assistance for visually impaired users (arXiv:2408.01800v1.pdf, p. 9).
*   **Mitigation Strategy:** To address this, the developers employed RLAIF-V (Reinforcement Learning from AI Feedback for Vision), a technique that uses feedback from other open-source AI models to align the model's behavior and reduce hallucinations. This involves a divide-and-conquer strategy where responses are broken into atomic claims, which are then verified by another MLLM. The model is then optimized on this feedback using Direct Preference Optimization (DPO) (arXiv:2408.01800v1.pdf, Section 4.3, p. 9). This process was shown to effectively reduce hallucination rates on the Object HalBench benchmark (arXiv:2408.01800v1.pdf, Table 6, p. 15).

**Data Considerations:**
The model was pre-trained on large-scale, web-crawled datasets like LAION-2B (arXiv:2408.01800v1.pdf, Table 1, p. 7). While the paper mentions "data cleaning is performed to remove image-text pairs with poor correlation and ill-formatted text data" (p. 7), the use of such datasets could potentially include sensitive or personal information, biases, or harmful content not fully filtered by the cleaning process.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge several limitations with the current model (arXiv:2408.01800v1.pdf, Section 7, p. 17):
*   **Capability Depth:** There is still significant room for improvement in the model's multimodal understanding capabilities and its inference efficiency.
*   **Capability Width:** The model is limited to the image modality and does not support other modalities like video or audio.
*   **On-Device Performance:** Despite optimizations, inference speed and latency on end-side devices are "still far from good enough." Performance can also be constrained by the device's battery capacity.
*   **Framework Optimization:** Existing deployment frameworks are often designed for older architectures (like CNNs) and may be sub-optimal for Transformer-based MLLMs.

### Recommendations:
Based on the paper's discussion, users and developers should consider the following (arXiv:2408.01800v1.pdf, p. 12, 17):
*   **Use with Human Oversight:** Due to the risk of hallucination, the model should not be deployed in high-stakes applications without a human in the loop.
*   **Hardware-Specific Optimization:** To achieve the best performance on end-side devices, users should leverage hardware-specific optimizations, such as NPU acceleration where available. The paper highlights that techniques like memory usage optimization, compilation optimization, and configuration optimization can significantly improve performance.
*   **Future Research:** The paper suggests that promising areas for future work include developing more efficient visual encoding methods that produce fewer tokens and better leveraging GPU/NPU acceleration for the LLM component to overcome current performance bottlenecks.