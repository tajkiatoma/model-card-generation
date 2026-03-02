## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the MiniCPM-V Team at OpenBMB (Source: arXiv_paper.pdf, page 1).

### Model date:
The MiniCPM-V series of models, to which this model belongs, has seen several releases in 2024:
*   **February 2024:** MiniCPM-V 1.0 was launched.
*   **April 2024:** MiniCPM-V 2.0 was introduced.
*   **May 2024:** MiniCPM-Llama3-V 2.5 was released.
The associated research paper is dated August 3, 2024 (Source: arXiv_paper.pdf, page 1, 2).

### Model version:
The model version is 2.5 (Source: config.json). This version is part of the MiniCPM-V series and is distinguished from previous versions (1.0 and 2.0) by its use of Llama3-Instruct 8B as the base Large Language Model (LLM) and the application of the RLAIF-V (Reinforcement Learning from AI Feedback for Vision) technique for alignment to reduce hallucinations (Source: arXiv_paper.pdf, Table 3, page 13).

### Model type:
The model is a Multimodal Large Language Model (MLLM) of type `minicpmv` designed for multimodal dialogue (Source: config.json, merlin_metadata.json).

**Architecture:**
The model's architecture consists of three main components (Source: arXiv_paper.pdf, Section 3.1, page 5):
1.  **Visual Encoder:** A SigLIP SoViT-400m/14 model is used to encode the input image. It employs an adaptive visual encoding approach to handle high-resolution images of various aspect ratios (Source: arXiv_paper.pdf, Section 3.1, page 5). The vision model configuration is based on `idefics2` with 27 hidden layers and a hidden size of 1152 (Source: config.json).
2.  **Compression Layer:** A perceiver resampler structure with one layer of cross-attention compresses the visual tokens from the encoder into a fixed number of queries (96 queries for this version) (Source: config.json; arXiv_paper.pdf, Section 3.2, page 6).
3.  **Large Language Model (LLM):** The compressed visual tokens are fed along with text input into a LlamaForCausalLM for conditional text generation (Source: modeling_minicpmv.py). For version 2.5, the base LLM is Llama3-Instruct 8B (Source: arXiv_paper.pdf, Table 3, page 13).

**Model Size and Parameters:**
*   **LLM Parameters:**
    *   Total Parameters: 8.5B (Source: arXiv_paper.pdf, Table 4, page 13)
    *   Hidden Size: 4096
    *   Number of Hidden Layers: 32
    *   Number of Attention Heads: 32
    *   Intermediate Size: 14336
    *   Vocabulary Size: 128256
    (Source: config.json)
*   **Total Model Size:** The total size of the model weights is 34.15 GB (Source: model.safetensors.index.json).
*   **Context Length:** The model supports a maximum position embedding of 8192 (Source: config.json).

### Training details:
The model's training process consists of three main phases (Source: arXiv_paper.pdf, Section 4, page 6):

1.  **Pre-training:** This phase aligns the visual modules with the LLM's input space using large-scale image-text pairs. It is divided into three stages:
    *   **Stage 1:** Warms up the compression layer by training only this module with a 224x224 image resolution.
    *   **Stage 2:** Extends the visual encoder's input resolution to 448x448 and trains the entire visual encoder.
    *   **Stage 3:** Trains both the compression layer and visual encoder using an adaptive visual encoding strategy to handle high-resolution inputs of any aspect ratio, incorporating OCR data to enhance this capability. The LLM is kept frozen during this phase.
    Techniques like **Caption Rewriting** (using GPT-4 to refine low-quality web captions) and **Data Packing** (combining multiple samples into a fixed-length sequence) were used to improve data quality and training efficiency (Source: arXiv_paper.pdf, Section 4.1, page 7).

2.  **Supervised Fine-Tuning (SFT):** After pre-training, all model parameters are unlocked and fine-tuned on high-quality visual question-answering datasets. The data is split into two parts: Part 1 focuses on basic recognition capabilities with short-response datasets, and Part 2 enhances capabilities for generating detailed responses and following complex instructions (Source: arXiv_paper.pdf, Section 4.2, page 8).

3.  **RLAIF-V (Reinforcement Learning from AI Feedback for Vision):** To address hallucination issues, the model is further aligned using Direct Preference Optimization (DPO). This involves generating multiple responses for an instruction, using open-source models to evaluate the correctness of atomic claims within each response, and constructing a preference dataset to train the model to generate more trustworthy outputs (Source: arXiv_paper.pdf, Section 4.3, page 9).

### Paper or other resource for more information:
An academic paper describing the model series is available:
*   **Title:** MiniCPM-V: A GPT-4V Level MLLM on Your Phone
*   **Authors:** Yuan Yao, Tianyu Yu, Ao Zhang, et al.
*   **Link:** The paper is included in the repository as `arXiv_paper.pdf`.
The paper provides a detailed overview of the model's architecture, training process, and performance, and also links to the official GitHub repository: https://github.com/OpenBMB/MiniCPM-V (Source: arXiv_paper.pdf, page 1).

### Citation details:
Insufficient information.

### License:
The model is licensed under the Apache License, Version 2.0 (Source: configuration_minicpm.py).

### Contact:
For questions or feedback, the corresponding author can be contacted at `yaoyuanthu@gmail.com` (Source: arXiv_paper.pdf, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed as an efficient, high-performance Multimodal Large Language Model (MLLM) capable of being deployed on end-side devices like mobile phones (Source: arXiv_paper.pdf, Abstract, page 1). Its primary use is for multimodal dialogue, where it can process both image and text inputs to generate relevant text-based responses (Source: merlin_metadata.json).

Key capabilities include:
*   **General Visual Understanding:** Answering questions about images, describing scenes, and performing complex reasoning (Source: arXiv_paper.pdf, Figure 2, page 4).
*   **Strong OCR Capability:** Accurately reading and transcribing text from images, including converting tables in images to Markdown format (Source: arXiv_paper.pdf, Abstract, page 1; Figure 2, page 4).
*   **Trustworthy Behavior:** The model is optimized to have low hallucination rates (Source: arXiv_paper.pdf, Abstract, page 1).
*   **Multilingual Support:** The model supports multimodal interactions in over 30 languages (Source: arXiv_paper.pdf, Abstract, page 1).

The model takes images and a sequence of conversational messages as input and generates a text response (Source: modeling_minicpmv.py, `chat` method).

### Primary intended users:
The primary users include:
*   **Developers:** Who can integrate the model into applications, especially on mobile and other end-side devices.
*   **Researchers:** Exploring efficient and powerful MLLMs.
*   **General Users:** Interacting with the model for various multimodal tasks on personal devices.
(Source: Inferred from the paper's focus on "end-side devices" and "real-world applications" in `arXiv_paper.pdf`, Section 1, page 2).

### Out-of-scope uses:
The model is not designed for the following:
*   **Generation of non-text modalities:** The model's output is limited to text. It cannot generate images, audio, or video (Source: arXiv_paper.pdf, Section 7, page 17).
*   **High-stakes applications requiring perfect factuality:** Although optimized for trustworthiness, as with all language models, it may still produce hallucinations or incorrect information. Its use in critical decision-making contexts should be carefully considered (Source: arXiv_paper.pdf, Section 4.3, page 9).
*   **Real-time video or audio processing:** The model's architecture is designed for static image inputs (Source: arXiv_paper.pdf, Section 7, page 17).

---

## How to Use
This section outlines how to use the model.

The model can be used for multimodal chat by providing an image and a sequence of messages. The processor handles the combination of image and text inputs, and the model generates a text response. The following is a conceptual example of how to use the model for inference (Source: modeling_minicpmv.py, `chat` method; processing_minicpmv.py).

```python
from PIL import Image
import torch
from transformers import AutoProcessor, AutoModel

# Load the model and processor
model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

processor = AutoProcessor.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

# Prepare inputs
image = Image.open('path_to_your_image.jpg').convert('RGB')
msgs = [{'role': 'user', 'content': 'What is in this image?'}]

# Set sampling parameters for generation
# For greedy decoding, set do_sample=False
generation_config = {
    "top_p": 0.8,
    "top_k": 100,
    "temperature": 0.7,
    "do_sample": True,
    "repetition_penalty": 1.05
}

# Generate a response
# The `chat` method is a helper function provided in the modeling code
# It processes the inputs and calls the model's generate method
with torch.inference_mode():
    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=processor.tokenizer,
        max_new_tokens=1024,
        **generation_config
    )

# Print the output
print(res)

# For streaming output
# res = model.chat(..., stream=True)
# for chunk in res:
#     print(chunk, end='')
```

**Input/Output Structure:**
*   **Input:**
    *   `image`: A PIL Image object.
    *   `msgs`: A list of dictionaries, where each dictionary represents a turn in the conversation with a `role` ('user' or 'assistant') and `content` (a string). The image is typically associated with the first user message.
*   **Output:** A string containing the generated response from the model.

The chat template follows a specific format with special tokens to delineate roles and turns (Source: tokenizer_config.json, `chat_template`).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Image Quality and Resolution:** The model is designed to handle high-resolution images (up to 1.8M pixels, e.g., 1344x1344) with varying aspect ratios, thanks to its adaptive visual encoding mechanism. Performance on very low-resolution or blurry images may be degraded (Source: arXiv_paper.pdf, Section 3.2, page 6).
*   **Language:** The model has multilingual capabilities covering over 30 languages. Performance may vary across languages, potentially influenced by the base LLM's proficiency in a given language and the amount of multilingual SFT data (Source: arXiv_paper.pdf, Section 4.2, page 8; Section 6.5, page 15).
*   **Data Quality:** The quality of the training data, particularly captions and instructions, is crucial. The developers employed caption rewriting to mitigate issues with noisy web data (Source: arXiv_paper.pdf, Section 4.1, page 7).

### Evaluation factors:
The model was evaluated across a variety of factors and capabilities, including:
*   **General Multimodal Capabilities:** Assessed using the OpenCompass benchmark suite (Source: arXiv_paper.pdf, Table 4, page 13).
*   **OCR Performance:** Evaluated on benchmarks like OCRBench, TextVQA, and DocVQA (Source: arXiv_paper.pdf, Table 5, page 14).
*   **Hallucination Rates:** Measured using Object HalBench (Source: arXiv_paper.pdf, Table 4, page 13).
*   **Multilingual Performance:** Assessed by translating the LLaVA Bench into 15+ languages and evaluating the model's responses (Source: arXiv_paper.pdf, Figure 8, page 14).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a comprehensive set of benchmarks, each with its own scoring methodology:
*   **OpenCompass:** A collection of 11 popular multimodal benchmarks used as a general evaluation indicator. The specific metrics within each sub-benchmark vary (Source: arXiv_paper.pdf, Section 6.2, page 13).
*   **MME, MM-Bench, MMMU, MathVista, LLaVA Bench:** These are components of OpenCompass, each targeting different aspects like perception, reasoning, and instruction following (Source: arXiv_paper.pdf, Section 6.2, page 13).
*   **OCRBench, TextVQA, DocVQA:** Standard benchmarks for evaluating OCR and text-rich image understanding capabilities (Source: arXiv_paper.pdf, Section 6.2, page 13).
*   **Object HalBench:** Measures hallucination rates at both the response level and mention level to evaluate the model's trustworthiness (Source: arXiv_paper.pdf, Table 4, page 13).

### Decision thresholds:
Insufficient information.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its capabilities comprehensively (Source: arXiv_paper.pdf, Section 6.2, page 13):
*   **General Benchmarks:**
    *   **OpenCompass:** A suite that includes MME, MM-Bench, MMMU, MathVista, and LLaVA Bench.
    *   **RealWorldQA:** For real-world spatial understanding.
*   **OCR Benchmarks:**
    *   **OCR-Bench**
    *   **TextVQA**
    *   **DocVQA**
*   **Hallucination Benchmark:**
    *   **Object HalBench**
*   **Multilingual Benchmark:**
    *   **LLaVA Bench:** The reference responses were translated into over 15 languages to evaluate multilingual performance.

### Motivation:
These datasets were chosen because they are popular and cover a wide spectrum of multimodal tasks, including visual question answering, conversation, knowledge and reasoning, OCR, and hallucination detection. This allows for a comprehensive and robust evaluation of the model's performance against other state-of-the-art models (Source: arXiv_paper.pdf, Section 6.2, page 13).

### Preprocessing:
For the multilingual evaluation, the LLaVA Bench reference responses were translated into different languages, and GPT-4-Turbo was used for evaluation (Source: arXiv_paper.pdf, Figure 8, page 14). Other specific preprocessing steps for evaluation data are not detailed.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is composed of large-scale datasets for pre-training and high-quality datasets for supervised fine-tuning (SFT).

**Pre-training Data (Source: arXiv_paper.pdf, Table 1, page 7):**
*   **Image Captioning:**
    *   English (410M pairs): COCO, Visual Genome (VG), CC3M, CC12M, LAION-COCO, COYO, LAION-2B.
    *   Chinese (110M pairs): AIC, LAION-2B-Chinese, WuKong, Zero-Chinese.
*   **OCR & Knowledge:**
    *   English (39M): WIT, IDL, SynthText, SynthDoG-en, ArxivCap.
    *   Chinese (11M): WIT, LAION-2B-OCR.

**Supervised Fine-Tuning (SFT) Data (Source: arXiv_paper.pdf, Table 2, page 8):**
*   **Part 1 (Basic Recognition):** A collection of datasets for VQA (e.g., VQAv2, GQA), knowledge (e.g., OKVQA), grounding (RefCOCO), reasoning, math, OCR (e.g., DocVQA, TextVQA), and chat, totaling over 4.8M samples.
*   **Part 2 (Advanced Capabilities):** Includes instruct-tuning datasets like LLaVA-Instruct-150K, UniMM-Chat, and ShareGPT4V, as well as text-only instruction datasets like Ultra-Chat and Alpaca. It also includes 90K multilingual data points covering 36 languages.

### Motivation:
*   **Pre-training Data:** Used to align the visual encoder and compression layer with the LLM's embedding space and to learn foundational multimodal knowledge (Source: arXiv_paper.pdf, Section 4.1, page 7).
*   **SFT Data:** Used to teach the model knowledge and interaction capabilities from high-quality human annotations, shaping its response style and ability to follow complex instructions (Source: arXiv_paper.pdf, Section 4.2, page 8).

### Preprocessing:
*   **Image Preprocessing:** The model uses an adaptive visual encoding strategy. Images are partitioned into multiple slices to handle high resolutions and preserve aspect ratios. Each slice is resized, and the visual encoder's position embeddings are interpolated to match the slice's dimensions. The original image is also included as an additional slice (Source: arXiv_paper.pdf, Section 3.2, page 6; image_processing_minicpmv.py).
*   **Text Preprocessing:**
    *   **Data Cleaning:** Image-text pairs with poor correlation or ill-formatted text were removed from the pre-training data (Source: arXiv_paper.pdf, Section 4.1, page 7).
    *   **Caption Rewriting:** An auxiliary LLM was used to convert low-quality web captions into a higher-quality question-answer format (Source: arXiv_paper.pdf, Section 4.1, page 7).
    *   **Data Packing:** To improve efficiency, multiple training samples were packed into a single fixed-length sequence, with position IDs and attention masks adjusted to prevent interference between samples (Source: arXiv_paper.pdf, Section 4.1, page 7).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was analyzed across different languages. Table 7 in the paper shows the LLaVA Bench score for 9 languages (French, German, Portuguese, Spanish, Czech, Hungarian, Japanese, Korean, Thai) with and without multilingual fine-tuning. For example, with multilingual training, the score for German improved from 22.8 to 76.5, and for Japanese, it improved from 13.8 to 67.9 (Source: arXiv_paper.pdf, Table 7, page 15). Figure 8 and Figure 13 further visualize these results across more languages, comparing the model to Yi-VL 34B and Phi-3-vision-128k-instruct (Source: arXiv_paper.pdf, page 14, 26).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **FP16 Precision:** The model in its standard fp16 version requires 16-17 GB of memory to load (Source: arXiv_paper.pdf, Section 5.2, page 10).
*   **4-bit Quantized:** Using a 4-bit quantization strategy (Q4_K_M mode in GGML), the memory requirement is reduced to approximately 5 GB, making it suitable for mobile phone usage (Source: arXiv_paper.pdf, Section 5.2, page 10).

### Deploying Requirements:
The model is designed for deployment on end-side devices. Performance benchmarks were conducted on the following hardware (Source: arXiv_paper.pdf, Section 5.4, page 12):
*   **Xiaomi 14 Pro (Snapdragon 8 Gen 3):** With full optimizations including NPU acceleration, achieves an encoding latency of 9.4s and a decoding throughput of 8.2 tokens/s.
*   **vivo X100 Pro (Mediatek Dimensity 9300):** Achieves an encoding latency of 13.9s and a decoding throughput of 4.9 tokens/s.
*   **Macbook Pro (M1):** Achieves an encoding latency of 10.4s and a decoding throughput of 16.9 tokens/s.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Risk of Hallucination:** MLLMs are prone to generating content that is not factually grounded in the input image. To mitigate this, the developers employed RLAIF-V (Reinforcement Learning from AI Feedback for Vision), a technique specifically designed to reduce hallucination rates and improve the model's trustworthiness by aligning it with feedback from other AI models (Source: arXiv_paper.pdf, Section 4.3, page 9).
*   **Privacy:** A key motivation for developing an on-device model is to enhance user privacy. By performing computations locally, the need to send potentially sensitive data to cloud servers is reduced (Source: arXiv_paper.pdf, Section 1, page 2).
*   **Sensitive Data:** The repository does not contain information about whether sensitive data was used during training. The training data consists of publicly available and web-crawled datasets (Source: arXiv_paper.pdf, Tables 1 & 2, pages 7-8).
*   **Potential for Misuse:** As with any generative model, there is a risk of misuse for creating misleading or harmful content. The developers focused on improving trustworthiness, but users should remain aware of these risks. The paper does not detail specific misuse cases or affected groups.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge several limitations of the current model (Source: arXiv_paper.pdf, Section 7, page 17):
*   **Capability Depth:** There is still room for improvement in the model's multimodal understanding and inference efficiency.
*   **Capability Width:** The model is limited to the image modality. It does not support other modalities like video or audio.
*   **Deployment Performance:** While deployable on mobile devices, the inference speed and latency are not yet optimal for a seamless user experience. Performance can also be limited by the device's battery capacity.
*   **Hardware Optimization:** Existing deployment frameworks and mobile chips are often not fully optimized for MLLM architectures, which can limit performance.

### Recommendations:
Based on the model's limitations and the research findings, the following recommendations are suggested:
*   **Use on Optimized Hardware:** For the best performance on mobile devices, use hardware with a dedicated NPU (like the Qualcomm Snapdragon 8 Gen 3) and appropriate deployment frameworks (Source: arXiv_paper.pdf, Section 5.4, page 12).
*   **Be Mindful of Hallucinations:** While the model has been optimized to reduce hallucinations, users should critically evaluate its outputs, especially in sensitive contexts.
*   **Future Research:** The paper suggests that promising future work includes developing more efficient visual encoding methods and better leveraging GPU/NPU acceleration for the LLM component to achieve real-time interaction on end-side devices (Source: arXiv_paper.pdf, Section 5.4, page 12; Section 7, page 17).