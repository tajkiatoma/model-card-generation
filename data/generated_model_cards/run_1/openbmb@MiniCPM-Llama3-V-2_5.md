## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the MiniCPM-V Team and OpenBMB (2408.01800.pdf, p. 1).

### Model date:
The MiniCPM-V series includes three models released in 2024:
*   **MiniCPM-V 1.0:** Launched in February 2024 (2408.01800.pdf, p. 2).
*   **MiniCPM-V 2.0:** Introduced in April 2024 (2408.01800.pdf, p. 2).
*   **MiniCPM-Llama3-V 2.5:** Released in May 2024 (2408.01800.pdf, p. 2).

The associated academic paper was submitted on August 3, 2024 (2408.01800.pdf, p. 1).

### Model version:
The model version is 2.5 (config.json.txt). This version is part of the MiniCPM-V series and builds upon previous versions with several key enhancements. Unlike versions 1.0 and 2.0 which used MiniCPM 2B as the base Large Language Model (LLM), version 2.5 uses Llama3-Instruct 8B. It also incorporates the RLAIF-V (Reinforcement Learning from AI Feedback for Vision) alignment technique to improve trustworthiness and reduce hallucinations, which was not used in version 1.0 (2408.01800.pdf, p. 13, Table 3).

### Model type:
The model is a Multimodal Large Language Model (MLLM) of type `MiniCPMV` (config.json.txt; 2408.01800.pdf, p. 1). It is designed for multimodal dialogue tasks (configuration.json.txt).

**Architecture:**
The model's architecture consists of three main components (2408.01800.pdf, p. 5, Section 3.1):
1.  **Visual Encoder:** A SigLIP SoViT-400m/14 model is used to encode input images. The visual encoder has a hidden size of 1152, 27 hidden layers, and 16 attention heads (config.json.txt; 2408.01800.pdf, p. 5). It processes images using an adaptive visual encoding approach to handle high-resolution inputs (up to 1.8M pixels, e.g., 1344x1344) of any aspect ratio (2408.01800.pdf, p. 3, 6).
2.  **Compression Layer:** A perceiver resampler structure with one layer of cross-attention compresses the visual tokens from the encoder. This module reduces the number of visual tokens for each image slice to 96 queries (config.json.txt; 2408.01800.pdf, p. 5-6).
3.  **Large Language Model (LLM):** The base LLM is Llama3-Instruct 8B (2408.01800.pdf, p. 12). The LLM part of the architecture has a hidden size of 4096, 32 hidden layers, 32 attention heads, and an intermediate size of 14336 (config.json.txt).

**Model Size:**
*   **Total Parameters:** 8.5 billion (2408.01800.pdf, p. 13, Table 4).
*   **Vocabulary Size:** 128,256 (config.json.txt).
*   **Context Length:** The model supports a maximum position embedding of 8192 tokens (config.json.txt).

### Training details:
The model's training process consists of three main phases: pre-training, supervised fine-tuning (SFT), and RLAIF-V alignment (2408.01800.pdf, p. 6, Section 4).

**1. Pre-training:**
This phase aims to align the visual modules with the LLM's input space. It is divided into three stages (2408.01800.pdf, p. 7, Section 4.1):
*   **Stage 1:** The compression layer is warmed up using 200M image-text pairs with a fixed image resolution of 224x224. Only the compression layer is trained.
*   **Stage 2:** The input resolution is extended to 448x448, and the entire visual encoder is trained using another 200M image-text pairs.
*   **Stage 3:** The model is trained with the adaptive visual encoding strategy to handle high-resolution inputs. Both the visual encoder and compression layer are trained, while the LLM remains frozen. OCR data is introduced in this stage to enhance OCR capabilities.
Techniques like **Caption Rewriting** (using a fine-tuned LLM to improve low-quality web captions) and **Data Packing** (packing multiple samples into a fixed-length sequence for efficiency) are used (2408.01800.pdf, p. 7).

**2. Supervised Fine-tuning (SFT):**
After pre-training, all model parameters are unfrozen for SFT on high-quality visual question-answering datasets. The data is split into two parts (2408.01800.pdf, p. 8, Section 4.2):
*   **Part 1:** Focuses on basic recognition capabilities using traditional QA/captioning datasets with short responses.
*   **Part 2:** Enhances capabilities for generating detailed responses and following complex instructions, using datasets with longer and more complex interactions.
The model's multilingual capabilities are generalized through a lightweight multilingual SFT on over 30 languages (2408.01800.pdf, p. 8).

**3. RLAIF-V (Reinforcement Learning from AI Feedback for Vision):**
To reduce hallucinations, the model is aligned using Direct Preference Optimization (DPO). This involves (2408.01800.pdf, p. 9, Section 4.3):
*   **Response Generation:** Sampling multiple responses from the policy model for a given instruction.
*   **Feedback Collection:** Using open-source models (LLaVA-NeXT-Yi 34B) to evaluate the correctness of atomic claims extracted from each response.
*   **Preference Optimization:** Constructing a preference dataset of 6K pairs and using DPO to train the model to prefer responses with higher factual correctness.

### Paper or other resource for more information:
*   **Academic Paper:** "MiniCPM-V: A GPT-4V Level MLLM on Your Phone" provides a detailed overview of the model series, architecture, training, and evaluation (2408.01800.pdf).
*   **GitHub Repository:** The official repository can be found at `https://github.com/OpenBMB/MiniCPM-V` (2408.01800.pdf, p. 1).

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
(Derived from 2408.01800.pdf)

### License:
The model code is licensed under the Apache License, Version 2.0 (configuration_minicpm.py).

### Contact:
For questions or feedback, contact `yaoyuanthu@gmail.com` (2408.01800.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is a general-purpose, multimodal language model intended for a wide range of applications, particularly in scenarios requiring on-device deployment. Its primary uses include (2408.01800.pdf, p. 2-3):
*   **Multimodal Dialogue:** Engaging in conversations that involve both text and images.
*   **Optical Character Recognition (OCR):** Strong capabilities in reading and transcribing text from images, including complex layouts like tables and documents.
*   **High-Resolution Image Understanding:** Perceiving and analyzing images with up to 1.8M pixels and at any aspect ratio.
*   **Multilingual Interaction:** Supporting conversations and understanding in over 30 languages.
*   **On-Device AI:** Deployment in mobile, offline, energy-sensitive, and privacy-protective scenarios such as on mobile phones, personal computers, vehicles, and robotics.

The model takes a text prompt and optional images as input and generates a text response (modeling_minicpmv.py, `chat` function).

### Primary intended users:
The primary users are developers, researchers, and businesses looking to build and deploy multimodal AI applications on end-side devices. This includes those working on applications for personal and industrial use where cloud-based deployment is not feasible or desirable (2408.01800.pdf, p. 2).

### Out-of-scope uses:
The model is not designed for the following uses:
*   **Non-image Modalities:** The model does not process video or audio inputs (2408.01800.pdf, p. 17).
*   **High-Stakes Factual Accuracy:** The model is prone to hallucinations, although efforts have been made to reduce them. It should not be used in critical applications where factual errors could lead to harm (e.g., autonomous driving, medical diagnosis) without human oversight (2408.01800.pdf, p. 9).
*   **Real-time, Low-Latency Applications:** While optimized for on-device use, the model's inference speed and latency may not be sufficient for applications requiring real-time responses (2408.01800.pdf, p. 17).

---

## How to Use
This section outlines how to use the model.

The model can be used for multimodal chat by providing a text prompt and an image. The processor handles the combination of text and image inputs, and the model generates a text response. Below is a conceptual code snippet based on the model's implementation (modeling_minicpmv.py; processing_minicpmv.py).

```python
import torch
from PIL import Image
from transformers import AutoModel, AutoProcessor

# Load the model and processor
model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

processor = AutoProcessor.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

# Prepare inputs
image = Image.open('path_to_your_image.jpg').convert('RGB')
# The user's text prompt
question = 'What is in this image?'
# A list of messages for conversation history
msgs = [{'role': 'user', 'content': question}]

# Generate a response
# The chat function handles tokenization and image processing internally
res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=processor.tokenizer,
    sampling=True, 
    temperature=0.7,
    max_new_tokens=1024,
    stream=False # Set to True for streaming output
)

print(res)

# Example with conversation history
msgs = [
    {'role': 'user', 'content': 'What is in this image?'},
    {'role': 'assistant', 'content': 'The image shows a street scene in Thailand with a blue and red tuk-tuk.'},
    {'role': 'user', 'content': 'What color is the building in the background?'}
]

# For follow-up questions, the image can be passed again or handled via context
res_follow_up = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=processor.tokenizer,
    sampling=True,
    temperature=0.7
)
print(res_follow_up)
```

The `chat_template` defines how conversational turns are formatted for the model (tokenizer_config.json.txt):
`{% set loop_messages = messages %}{% for message in loop_messages %}{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>\n\n'+ message['content'] | trim + '<|eot_id|>' %}{% if loop.index0 == 0 %}{% set content = bos_token + content %}{% endif %}{{ content }}{% endfor %}{{ '<|start_header_id|>assistant<|end_header_id|>\n\n' }}`

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model's performance varies across the 30+ languages it supports. The extent of performance improvement from multilingual fine-tuning is uneven across languages, potentially related to the base LLM's proficiency in each language (2408.01800.pdf, p. 15).
*   **Image Quality and Resolution:** The model is designed to handle high-resolution images, and its performance on fine-grained tasks like OCR depends on the clarity and resolution of the input image (2408.01800.pdf, p. 6).
*   **Task Complexity:** Performance differs across various tasks such as simple VQA, complex reasoning, mathematical problems, and OCR on structured documents (2408.01800.pdf, p. 13, Table 4).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Task Type:** Performance was measured on a wide range of tasks using benchmarks like OpenCompass (which includes MME, MM-Bench, MMMU, MathVista), OCR-Bench, TextVQA, DocVQA, and Object HalBench (2408.01800.pdf, p. 13, Section 6.2).
*   **Language:** The model's multilingual capabilities were evaluated by translating the LLaVA Bench into 15+ languages and using GPT-4-Turbo for scoring (2408.01800.pdf, p. 14, Figure 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of standard benchmarks and metrics tailored to different capabilities (2408.01800.pdf, p. 13, Section 6.2):
*   **General Multimodal Capability:** Measured using the **OpenCompass** benchmark, which is a comprehensive collection of 11 popular benchmarks including MME, MM-Bench, MMMU, MathVista, and LLaVA Bench. The specific metrics for each sub-benchmark are used, and an aggregate score is reported.
*   **OCR Capability:** Evaluated on **OCRBench**, **TextVQA**, and **DocVQA**, which measure the model's ability to read and understand text in images.
*   **Trustworthiness (Hallucination):** Measured using **Object HalBench**, which reports **response-level and mention-level hallucination rates**. Lower rates indicate better performance.
*   **Multilingual Performance:** Assessed using a translated version of **LLaVA Bench**, with responses evaluated by GPT-4-Turbo.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess its capabilities in various domains (2408.01800.pdf, p. 13, Section 6.2):
*   **General Multimodal Benchmarks:**
    *   **OpenCompass [26]:** A collection including:
        *   **MME [33]:** A comprehensive evaluation benchmark for multimodal large language models.
        *   **MM-Bench [63]:** A multi-task benchmark for evaluating multimodal models.
        *   **MMMU [113]:** A benchmark for massive multi-discipline multimodal understanding and reasoning.
        *   **MathVista [71]:** Evaluates mathematical reasoning in visual contexts.
        *   **LLaVA Bench [62]:** A benchmark for visual instruction tuning.
    *   **RealWorldQA:** For real-world spatial understanding capabilities.
*   **OCR Benchmarks:**
    *   **OCR-Bench [64]**
    *   **TextVQA [91]**
    *   **DocVQA [74]**
*   **Hallucination Benchmark:**
    *   **Object HalBench [85, 111]:** Evaluates object hallucination in model responses.
*   **Multilingual Benchmark:**
    *   A translated version of **LLaVA Bench [62]** was used to evaluate performance in over 15 languages.

### Motivation:
The datasets were chosen to provide a "comprehensive evaluation on popular benchmarks covering visual question answering, multimodal conversation, knowledge and reasoning, OCR, and hallucination" (2408.01800.pdf, p. 13, Section 6.2). This allows for a holistic assessment of the model's capabilities and its comparison against other open-source and proprietary models.

### Preprocessing:
For multilingual evaluation, the reference responses of the LLaVA Bench were translated into different languages to create evaluation sets (2408.01800.pdf, p. 14, Figure 8). Other preprocessing steps for evaluation data are not specified.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is extensive and sourced from a variety of public datasets, categorized into pre-training and supervised fine-tuning stages.

**Pre-training Data (2408.01800.pdf, p. 7, Table 1):**
*   **Image Captioning (410M English, 110M Chinese):** Includes datasets like COCO [59], Visual Genome [51], CC3M/CC12M [89, 17], LAION-2B [86], COYO [15], WuKong [35], and others.
*   **OCR and Knowledge (39M English, 11M Chinese):** Includes datasets like WIT [92], IDL [13], SynthText [37], ArxivCap [55], and an OCR-processed version of LAION-2B.

**Supervised Fine-tuning (SFT) Data (2408.01800.pdf, p. 8, Table 2):**
*   **Part-1 (Basic Recognition):** A collection of datasets for short captioning, VQA, knowledge, grounding, reasoning, math, OCR, and chat. Examples include Flickr-30K [81], VQAv2 [6], ScienceQA [70], RefCOCO [109], and DocVQA [74].
*   **Part-2 (Advanced Capabilities):** Datasets focused on instruction following and detailed responses, including LLaVA-Instruct-150K [62], ShareGPT4V [21], Ultra-Chat [30], and Alpaca [97].
*   **RLAIF-V Data:** A preference dataset of 6K pairs constructed from 3K unique images for DPO training (2408.01800.pdf, p. 9).

### Motivation:
*   **Pre-training:** The large-scale image-text pairs are used to "align the visual modules... with the input space of the LLM and learn foundational multimodal knowledge." OCR data is specifically included to "enhance the visual encoders' OCR capability" (2408.01800.pdf, p. 7).
*   **SFT:** High-quality annotated data is used to "further learn knowledge and interaction capability from human annotations." The two-part data strategy is designed to first build basic recognition skills and then develop more complex, detailed response generation (2408.01800.pdf, p. 8).
*   **RLAIF-V:** This phase is motivated by the need to address the "hallucination problem" and create a more trustworthy model (2408.01800.pdf, p. 9).

### Preprocessing:
Several preprocessing steps were applied to the training data to improve quality and efficiency (2408.01800.pdf, p. 7):
*   **Data Cleaning:** Image-text pairs with poor correlation and ill-formatted text were removed from the pre-training data.
*   **Caption Rewriting:** An auxiliary LLM, fine-tuned on a small set of GPT-4 annotations, was used to rewrite low-quality captions from web-crawled data into a more structured question-answer format.
*   **Data Packing:** To improve training efficiency and handle variable sample lengths, multiple samples were packed into a single fixed-length sequence. Position IDs and attention masks were modified accordingly to prevent interference between packed samples. This strategy resulted in a 2-3x acceleration in pre-training.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results are reported for different tasks and languages.

**Performance by Task:**
The model's performance on various benchmarks is presented in the paper.
*   **General Benchmarks (OpenCompass Score: 65.1):**
    *   MME: 2024.6
    *   MM-Bench (test, en): 77.2
    *   MMMU (val): 45.8
    *   MathVista: 54.3
    *   LLaVA Bench: 86.7
    *   Object HalBench (Response/Mention Hallucination Rate): 10.3% / 5.0%
    (2408.01800.pdf, p. 13, Table 4)
*   **OCR Benchmarks:**
    *   OCRBench: 725
    *   TextVQA (val): 76.6
    *   DocVQA (test): 84.8
    (2408.01800.pdf, p. 14, Table 5)

**Performance by Language:**
The model was evaluated on a translated version of LLaVA Bench. Below are scores for a selection of languages (out of 100):
*   English: ~87
*   German: ~84
*   French: ~83
*   Spanish: ~82
*   Japanese: ~80
*   Russian: ~78
*   Korean: ~75
(2408.01800.pdf, p. 14, Figure 8)

The impact of multilingual fine-tuning was also analyzed (LLaVA Bench scores):
*   **German:** 22.8 (without ML training) -> 76.5 (with ML training)
*   **Portuguese:** 53.0 (without ML training) -> 83.8 (with ML training)
*   **Japanese:** 13.8 (without ML training) -> 88.0 (with ML training)
*   **Korean:** 13.7 (without ML training) -> 67.9 (with ML training)
(2408.01800.pdf, p. 15, Table 7)

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **FP16 Version:** Requires 16-17 GB of memory (2408.01800.pdf, p. 10).
*   **4-bit Quantized Version (Q4_K_M):** Requires around 5 GB of memory, making it suitable for mobile phone deployment (2408.01800.pdf, p. 10).

### Deploying Requirements:
The model is designed for deployment on end-side devices. Performance has been evaluated on the following hardware (2408.01800.pdf, p. 12):
*   **Xiaomi 14 Pro (Snapdragon 8 Gen 3):** With full optimizations including NPU acceleration, achieves an encoding latency of 9.4s and a decoding throughput of 8.2 tokens/second.
*   **vivo X100 Pro (Mediatek Dimensity 9300):** Achieves an encoding latency of 13.9s and a decoding throughput of 4.9 tokens/second.
*   **Macbook Pro (M1):** Achieves an encoding latency of 10.4s and a decoding throughput of 16.9 tokens/second.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Hallucination Risk:** The developers acknowledge that MLLMs are "typically prone to hallucination problems," which poses significant risks in high-stakes scenarios like autonomous driving or assistance for visually impaired individuals. The model may generate responses that are not factually grounded in the input image (2408.01800.pdf, p. 9).
*   **Risk Mitigation for Hallucination:** To address this, the model was trained with the RLAIF-V (Reinforcement Learning from AI Feedback for Vision) method. This technique uses Direct Preference Optimization (DPO) to align the model towards more trustworthy behavior by learning from feedback generated by other AI models. This process was shown to reduce hallucination rates on the Object HalBench benchmark (2408.01800.pdf, p. 9, 15).
*   **Data Privacy:** The model is designed for on-device deployment, which is presented as a solution for "privacy/security protective scenarios" because it avoids the need to send user data to external cloud servers (2408.01800.pdf, p. 2).
*   **Use of Web-Sourced Data:** The model was pre-trained on large-scale datasets crawled from the web, such as LAION-2B (2408.01800.pdf, p. 7, Table 1). Such datasets may contain sensitive personal information, copyrighted material, or biased content, though the paper notes that data cleaning was performed to remove "image-text pairs with poor correlation and ill-formatted text data" (2408.01800.pdf, p. 7).
*   **Fraught Use Cases:** The paper highlights that use cases requiring high reliability, such as aiding visually impaired groups, are particularly fraught due to the risk of hallucination (2408.01800.pdf, p. 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers identify several limitations of the current model (2408.01800.pdf, p. 17, Section 7):
*   **Capability Depth and Efficiency:** There is still "plenty of room for improvement in enhancing multimodal understanding capability and inference efficiency."
*   **Modality Limitations:** The model is limited to the image modality and does not support other modalities like video or audio.
*   **Deployment Performance:** On-device "inference speed and latency are still far from good enough" for many real-time applications. Performance can also be constrained by the device's battery capacity.
*   **Sub-optimal Hardware Acceleration:** Existing deployment frameworks and on-device chips (like NPUs) are often optimized for older architectures (CNNs, LSTMs) and may not be optimal for Transformer-based MLLMs.

### Recommendations:
*   **Use with Caution in Critical Applications:** Due to the risk of hallucination, users should not rely solely on the model for high-stakes decisions and should incorporate human oversight.
*   **Future Research Directions:** The paper suggests that promising areas for improvement include developing more efficient visual encoding methods, using fewer visual tokens, and better leveraging on-device hardware like GPUs and NPUs for LLM acceleration (2408.01800.pdf, p. 12).
*   **On-Device Optimization:** Users deploying the model should consider quantization (e.g., 4-bit Q4_K_M) to reduce memory footprint and explore device-specific optimizations like compilation and NPU acceleration to improve performance (2408.01800.pdf, p. 10-12).

---