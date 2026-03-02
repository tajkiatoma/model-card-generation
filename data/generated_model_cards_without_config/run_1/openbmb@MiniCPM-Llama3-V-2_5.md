## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the MiniCPM-V Team and OpenBMB (2408.01800.pdf, p. 1).

### Model date:
The MiniCPM-V series includes several models released in 2024 (2408.01800.pdf, p. 2):
*   **MiniCPM-V 1.0:** Launched in February 2024.
*   **MiniCPM-V 2.0:** Introduced in April 2024.
*   **MiniCPM-Llama3-V 2.5:** Released in May 2024.

The associated research paper was submitted on August 3, 2024 (2408.01800.pdf, p. 1).

### Model version:
This model card describes the MiniCPM-V series, with a focus on the latest version, **MiniCPM-Llama3-V 2.5**. The series demonstrates a progression in capabilities and efficiency (2408.01800.pdf, p. 2, 12, Table 3, p. 13):

*   **MiniCPM-V 1.0 (2.8B):** Based on the MiniCPM 2B language model, it was one of the first Multimodal Large Language Models (MLLMs) designed for mobile phones. It was trained with a fixed image resolution of 448x448.
*   **MiniCPM-V 2.0 (2.8B):** Also based on the MiniCPM 2B LLM, this version introduced support for high-resolution images (up to 1.8M pixels) with any aspect ratio using an adaptive visual encoding strategy. It also incorporated RLHF-V for alignment to improve trustworthiness.
*   **MiniCPM-Llama3-V 2.5 (8.5B):** This version uses Llama3-Instruct 8B as its base LLM, leading to significantly improved performance. It retains the adaptive visual encoding for high-resolution images and uses RLAIF-V for alignment to reduce hallucinations.

### Model type:
MiniCPM-V is a series of Multimodal Large Language Models (MLLMs) designed for efficient deployment on end-side devices like mobile phones (2408.01800.pdf, p. 1).

**Architecture:**
The model's architecture consists of three main components (2408.01800.pdf, p. 5, Figure 3; modeling_minicpmv.py):
1.  **Visual Encoder (VPM):** A SigLIP SoViT-400m/14 vision transformer is used to encode input images. It employs an adaptive visual encoding approach to handle high-resolution images of various aspect ratios by partitioning them into slices (2408.01800.pdf, p. 5-6; modeling_minicpmv.py).
2.  **Compression Layer (Resampler):** A perceiver resampler with a single cross-attention layer compresses the visual tokens from the encoder into a fixed number of queries (96 tokens for MiniCPM-Llama3-V 2.5) (2408.01800.pdf, p. 5-6; resampler.py).
3.  **Large Language Model (LLM):** The compressed visual tokens are fed along with text input into a large language model for conditional text generation. The LLM used for MiniCPM-Llama3-V 2.5 is Llama3-Instruct 8B (2408.01800.pdf, p. 12, Table 3, p. 13; modeling_minicpmv.py).

**Model Size:**
*   **MiniCPM-V 1.0 & 2.0:** 2.8 billion parameters (2408.01800.pdf, Table 4, p. 13).
*   **MiniCPM-Llama3-V 2.5:** 8.5 billion parameters (2408.01800.pdf, Table 4, p. 13).
The total size of the model weights is approximately 34.15 GB (model.safetensors.index.json.txt).

### Training details:
The model's training process consists of three main phases (2408.01800.pdf, p. 6):

1.  **Pre-training:** This phase aims to align the visual modules with the LLM's input space and is divided into three stages (2408.01800.pdf, p. 7):
    *   **Stage 1:** The compression layer is warmed up using 200M image-text pairs with a fixed visual resolution of 224x224. Only the compression layer is trained.
    *   **Stage 2:** The visual encoder's input resolution is extended to 448x448. The entire visual encoder is trained using another 200M image-text pairs.
    *   **Stage 3:** Both the visual encoder and compression layer are trained using the adaptive visual encoding strategy to handle high-resolution inputs. OCR data is introduced in this stage to enhance OCR capabilities. The LLM remains frozen throughout pre-training.

2.  **Supervised Fine-Tuning (SFT):** After pre-training, all model parameters are unfrozen and fine-tuned on high-quality visual question-answering datasets. The SFT data is split into two parts: Part 1 focuses on basic recognition capabilities with shorter responses, and Part 2 enhances capabilities for generating detailed responses and following complex instructions (2408.01800.pdf, p. 8).

3.  **Alignment (RLAIF-V):** To reduce hallucinations and improve trustworthiness, the model is aligned using RLAIF-V (Reinforcement Learning from AI Feedback for Vision). This involves generating multiple responses, using open-source models to provide feedback on their correctness, and then performing Direct Preference Optimization (DPO) on preference pairs derived from this feedback (2408.01800.pdf, p. 9).

### Paper or other resource for more information:
*   **Research Paper:** "MiniCPM-V: A GPT-4V Level MLLM on Your Phone" provides a detailed overview of the model series, its architecture, training, and evaluation (2408.01800.pdf).
*   **GitHub Repository:** The official code and resources are available at: `https://github.com/OpenBMB/MiniCPM-V` (2408.01800.pdf, p. 1).

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
(2408.01800.pdf)

### License:
The paper describes the model as "open-source" (2408.01800.pdf, p. 3). However, no specific license file is provided in the repository.

### Contact:
For questions or feedback, contact Yuan Yao at `yaoyuanthu@gmail.com` (2408.01800.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
MiniCPM-V is designed as an efficient, high-performance Multimodal Large Language Model (MLLM) for deployment on end-side devices such as mobile phones, personal computers, and vehicles (2408.01800.pdf, p. 2). Its primary uses include:

*   **General Visual Question Answering:** Answering questions based on the content of an image (2408.01800.pdf, p. 4).
*   **High-Resolution Image Understanding:** Perceiving and analyzing images up to 1.8M pixels (e.g., 1344x1344) at any aspect ratio, which is crucial for fine-grained details (2408.01800.pdf, p. 3).
*   **Optical Character Recognition (OCR):** Accurately transcribing text from images, including screenshots, documents, and tables (2408.01800.pdf, p. 3, 15).
*   **Multilingual Interaction:** Engaging in multimodal conversations in over 30 languages (2408.01800.pdf, p. 3, 15).
*   **Trustworthy Assistance:** Providing factually grounded responses with low hallucination rates, making it suitable for high-stakes scenarios (2408.01800.pdf, p. 3, 9).

The model takes a text prompt and one or more images as input and generates a text-based response (modeling_minicpmv.py).

### Primary intended users:
The primary users are developers and researchers building AI applications for on-device deployment, where efficiency, privacy, and offline capability are important. This includes mobile app developers, AI researchers working on efficient models, and industries requiring on-premise multimodal AI (2408.01800.pdf, p. 2).

### Out-of-scope uses:
The model has several limitations and is not intended for the following uses (2408.01800.pdf, p. 17):
*   **Video or Audio Processing:** The model is designed exclusively for image and text modalities and cannot process video or audio inputs.
*   **High-Throughput Server Deployment:** While efficient for its performance level, the model is optimized for on-device use, not for large-scale, high-latency server applications where larger models might be more suitable.
*   **Mission-Critical Applications without Human Oversight:** Despite efforts to reduce hallucinations, the model can still make errors. It should not be used in critical applications where a mistake could lead to harm without a human in the loop.
*   **Generating Harmful or Biased Content:** The model should not be used to create offensive, discriminatory, or malicious content.

---

## How to Use
This section outlines how to use the model.

The model can be used for chat-based interaction involving images and text. The `MiniCPMV` class provides a `chat` method that orchestrates the processing of inputs and generation of responses (modeling_minicpmv.py).

Below is a conceptual code snippet demonstrating how to use the model for inference:

```python
from PIL import Image
from transformers import AutoProcessor
from modeling_minicpmv import MiniCPMV # Assuming the model class is in this file

# Load the model and processor
model_path = "OpenBMB/MiniCPM-Llama3-V-2_5"
model = MiniCPMV.from_pretrained(model_path, trust_remote_code=True).to(device='cuda', dtype=torch.float16)
processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
tokenizer = processor.tokenizer

# Prepare inputs
image = Image.open("path_to_your_image.jpg").convert("RGB")
question = "What is in this image?"
msgs = [{"role": "user", "content": question}]

# Set generation parameters
generation_config = {
    "top_p": 0.8,
    "top_k": 100,
    "temperature": 0.7,
    "do_sample": True,
    "repetition_penalty": 1.05,
    "max_new_tokens": 1024
}

# Generate a response
# The chat function handles tokenization and image processing internally
with torch.inference_mode():
    response = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        processor=processor,
        **generation_config
    )

print(response)
```
*(Source: Based on the `chat` function definition in `modeling_minicpmv.py`)*

The `chat` function can also handle streaming output by setting `stream=True`. It will return a generator that yields text chunks as they are generated (modeling_minicpmv.py).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Image Resolution and Aspect Ratio:** The model is designed to handle high-resolution images with varying aspect ratios through its adaptive visual encoding mechanism. Performance on fine-grained tasks like OCR is dependent on sufficient image resolution (2408.01800.pdf, p. 6).
*   **Language:** The model supports over 30 languages, but performance may vary across them. The model was pre-trained on English and Chinese multimodal data, with multilingual capabilities extended through supervised fine-tuning (2408.01800.pdf, p. 8, 15).
*   **Hardware:** As an on-device model, performance (latency and throughput) is highly dependent on the hardware, including the CPU, memory, and availability of accelerators like NPUs (2408.01800.pdf, p. 10-12).

### Evaluation factors:
The model was evaluated on a wide range of factors, including (2408.01800.pdf, p. 13):
*   **General Multimodal Capabilities:** Assessed using the OpenCompass benchmark, which covers 11 popular benchmarks like MME, MM-Bench, and LLaVA Bench.
*   **OCR Capability:** Evaluated on OCR-Bench, TextVQA, and DocVQA.
*   **Trustworthiness (Hallucination):** Measured using Object HalBench.
*   **Multilingual Performance:** Assessed using a translated version of LLaVA Bench across numerous languages.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of standard metrics from established benchmarks (2408.01800.pdf, p. 13-14):
*   **OpenCompass Score:** An aggregate score from a collection of 11 multimodal benchmarks.
*   **Accuracy:** Used in benchmarks like MME, MM-Bench, MMMU, and MathVista.
*   **OCR-Bench Score:** A specific metric for evaluating OCR capabilities.
*   **Hallucination Rate:** Measured on Object HalBench at both the response level and mention level to quantify trustworthiness.
*   **GPT-4 Score:** For benchmarks like LLaVA Bench, responses are often scored by GPT-4 to assess quality.

### Decision thresholds:
Insufficient information.

### Variation approaches:
Performance is reported as scores on standard, public benchmarks. For multilingual evaluation on LLaVA Bench, reference responses were translated, and GPT-4-Turbo was used for evaluation (2408.01800.pdf, p. 14, Figure 8 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public benchmarks to assess various capabilities (2408.01800.pdf, p. 13):

*   **General Benchmarks (via OpenCompass):**
    *   MME, MM-Bench, MMMU, MathVista, LLaVA Bench, RealWorldQA, and others.
*   **OCR Benchmarks:**
    *   **OCR-Bench:** For general OCR capabilities.
    *   **TextVQA:** For reading text to answer questions.
    *   **DocVQA:** For question answering on document images.
*   **Hallucination Benchmarks:**
    *   **Object HalBench:** To evaluate the model's tendency to hallucinate objects.
*   **Multilingual Benchmarks:**
    *   A translated version of **LLaVA Bench** was used to evaluate performance in over 30 languages.

### Motivation:
These datasets were chosen because they are popular, comprehensive benchmarks that cover a wide range of essential MLLM capabilities, including visual question answering, reasoning, OCR, and trustworthiness. This allows for a thorough comparison against other state-of-the-art open-source and proprietary models (2408.01800.pdf, p. 13).

### Preprocessing:
Insufficient information is available regarding specific preprocessing steps for the evaluation data, but it is assumed to follow the standard preprocessing pipeline defined by the model's processor, which includes adaptive image slicing and normalization (image_processing_minicpmv.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is composed of three main types: pre-training data, supervised fine-tuning (SFT) data, and preference data for alignment.

*   **Pre-training Data:** A large-scale collection of image-text pairs from various sources, totaling over 500 million samples. The data is in English and Chinese (2408.01800.pdf, Table 1, p. 7).
    *   **Image Captioning (English):** 410M pairs from COCO, VG, CC3M, CC12M, LAION-COCO, COYO, LAION-2B.
    *   **Image Captioning (Chinese):** 110M pairs from AIC, LAION-2B-Chinese, WuKong, Zero-Chinese.
    *   **OCR+Knowledge (English):** 39M pairs from WIT, IDL, SynthText, SynthDoG-en, ArxivCap.
    *   **OCR+Knowledge (Chinese):** 11M pairs from WIT, LAION-2B-OCR.

*   **Supervised Fine-Tuning (SFT) Data:** A curated collection of high-quality datasets divided into two parts (2408.01800.pdf, Table 2, p. 8).
    *   **Part 1 (Basic Recognition):** Includes datasets like Flickr-30K, VQAv2, RefCOCO, DocVQA, TextVQA, and ChartQA, totaling over 4.7M samples.
    *   **Part 2 (Advanced Instruction Following):** Includes datasets like SVIT, LLaVA-Instruct-150K, UniMM-Chat, ShareGPT4V, Ultra-Chat, and Alpaca, totaling over 2.6M samples.

*   **Alignment Data (RLAIF-V):** A preference dataset consisting of 6,000 preference pairs generated from 3,000 unique images, used for Direct Preference Optimization (DPO) (2408.01800.pdf, p. 9).

### Motivation:
*   **Pre-training Data:** Used to align the visual encoder and compression layer with the LLM and to learn foundational multimodal knowledge from a vast and diverse set of images and text (2408.01800.pdf, p. 7).
*   **SFT Data:** Used to teach the model to follow human instructions, learn rich knowledge, and improve its interaction capabilities using high-quality, human-annotated data (2408.01800.pdf, p. 8).
*   **Alignment Data:** Specifically created to reduce the model's hallucination rate and improve its trustworthiness (2408.01800.pdf, p. 9).

### Preprocessing:
Several preprocessing techniques were applied to the training data to improve quality and efficiency (2408.01800.pdf, p. 7):
*   **Data Cleaning:** Image-text pairs with poor correlation or ill-formatted text were removed from the pre-training data.
*   **Caption Rewriting:** An auxiliary LLM, fine-tuned on GPT-4 annotations, was used to rewrite low-quality web captions into a cleaner question-answer format.
*   **Data Packing:** To improve memory usage and computational efficiency, multiple samples were packed into a single sequence of a fixed length, with position IDs and attention masks adjusted to prevent interference between samples.
*   **Image Preprocessing:** Images are processed using the adaptive visual encoding scheme, which involves partitioning the image into slices, resizing, and applying normalization (mean: [0.5, 0.5, 0.5], std: [0.5, 0.5, 0.5]) (2408.01800.pdf, p. 6; image_processing_minicpmv.py).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of the MiniCPM-V series has been extensively benchmarked. Below are key results for **MiniCPM-Llama3-V 2.5 (8.5B)**:

*   **General Performance:** Achieved a score of **65.1** on the OpenCompass benchmark, outperforming other open-source models of similar and larger sizes, including Idefics2-8B (57.2), LLaVA-NeXT-Yi-34B (62.7), and Cambrian-34B (64.9) (2408.01800.pdf, Table 4, p. 13).
*   **OCR Performance:** Achieved a score of **725** on OCRBench, **76.6** on TextVQA val, and **84.8** on DocVQA test, performing comparably to or better than proprietary models like Gemini Pro and GPT-4V (2408.01800.pdf, Table 5, p. 14).
*   **Hallucination:** Exhibited low hallucination rates of **10.3% (response-level)** and **5.0% (mention-level)** on Object HalBench, which is better than GPT-4V (13.6%/7.3%) (2408.01800.pdf, Table 4, p. 13).
*   **Multilingual Performance:** Showed strong performance across more than 15 languages on the LLaVA Bench, outperforming Yi-VL 34B and Phi-3-vision-128k-instruct in most tested languages, including German, French, Japanese, and Korean (2408.01800.pdf, Figure 8, p. 14).
*   **Ablation Studies:**
    *   **RLAIF-V:** Applying RLAIF-V improved the OpenCompass score from 64.5 to 65.1 and significantly reduced hallucination rates (2408.01800.pdf, Table 6, p. 15).
    *   **Multilingual Training:** Adding a small amount of multilingual SFT data (<0.5%) dramatically improved performance in non-English languages, e.g., increasing the German score on LLaVA Bench from 22.8 to 76.5 (2408.01800.pdf, Table 7, p. 15).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Unquantized (FP16):** The MiniCPM-Llama3-V 2.5 model requires 16-17 GB of memory (2408.01800.pdf, p. 10).
*   **Quantized (4-bit):** Using a 4-bit quantization strategy (Q4_K_M mode in GGML), the memory requirement is reduced to approximately **5 GB**, making it suitable for mobile phone deployment (2408.01800.pdf, p. 10).

### Deploying Requirements:
The model is designed for on-device deployment. Performance has been benchmarked on the following hardware (2408.01800.pdf, p. 11-12):
*   **Xiaomi 14 Pro:** (CPU: Snapdragon 8 Gen 3, with NPU acceleration)
    *   Encoding Latency: 9.4s (with optimizations)
    *   Decoding Throughput: 8.2 tokens/s
*   **vivo X100 Pro:** (CPU: Mediatek Dimensity 9300)
    *   Encoding Latency: 13.9s
    *   Decoding Throughput: 4.9 tokens/s
*   **Macbook Pro (M1):**
    *   Encoding Latency: 10.4s
    *   Decoding Throughput: 16.9 tokens/s

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Hallucination Risk:** MLLMs are prone to generating content that is not factually grounded in the input image (hallucination). This poses a significant risk, especially in high-stakes applications. To mitigate this, the developers employed **RLAIF-V**, a technique specifically designed to align the model's behavior and reduce hallucination rates, making the model more trustworthy (2408.01800.pdf, p. 9). Quantitative analysis shows that MiniCPM-Llama3-V 2.5 has lower hallucination rates than GPT-4V on the Object HalBench benchmark (2408.01800.pdf, Table 4, p. 13).
*   **Data Provenance and Bias:** The model was pre-trained on large-scale, web-crawled datasets such as LAION-2B (2408.01800.pdf, Table 1, p. 7). Such datasets may contain societal biases, copyrighted material, or personal information. The paper mentions data cleaning was performed to remove pairs with poor correlation and ill-formatted text, but does not detail further steps taken to address potential biases or harmful content within the training data (2408.01800.pdf, p. 7).
*   **Misuse:** As a capable multimodal model, there is a risk of misuse for generating misinformation, harmful content, or for surveillance purposes. The intended use is for beneficial on-device applications.
*   **Multilingual Fairness:** By incorporating multilingual generalization techniques, the model aims to provide useful capabilities to users across more than 30 languages, reducing the reliance on extensive data collection in low-resource languages and promoting broader accessibility (2408.01800.pdf, p. 8).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge several limitations of the current MiniCPM-V models (2408.01800.pdf, p. 17):
*   **Capability Depth:** There is still room for improvement in the model's deep multimodal understanding and reasoning capabilities.
*   **Capability Width:** The model is currently limited to the image and text modalities. It does not support other modalities like video or audio.
*   **On-Device Performance:** While optimized for mobile devices, the inference speed and latency are "still far from good enough" for a seamless real-time user experience. Performance can also be limited by the device's battery capacity.
*   **Framework Optimization:** Existing deployment frameworks are often tailored for older architectures (CNNs, LSTMs) and may be sub-optimal for Transformer-based MLLMs.

### Recommendations:
*   **Use with Human Oversight:** Due to the risk of hallucination, it is recommended to use the model in applications where a human can verify the output, especially for critical tasks.
*   **Hardware-Specific Optimization:** Users deploying the model should consider hardware-specific optimizations. The paper shows that leveraging NPUs can significantly reduce visual encoding latency (2408.01800.pdf, p. 12).
*   **Future Research:** The paper suggests promising research directions include developing more efficient visual encoding methods and better leveraging GPU/NPU acceleration for the LLM component to achieve real-time interaction on end-side devices (2408.01800.pdf, p. 17).