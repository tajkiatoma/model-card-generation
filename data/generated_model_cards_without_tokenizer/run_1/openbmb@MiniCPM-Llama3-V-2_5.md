## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the MiniCPM-V Team from OpenBMB (2408.01800.pdf, p. 1). The core team members and project leads listed are Yuan Yao, Tianyu Yu, Ao Zhang, Chongyi Wang, Junbo Cui, Hongji Zhu, Tianchi Cai, Haoyu Li, Weilin Zhao, Zhihui He, Qianyu Chen, Huarong Zhou, Zhensheng Zou, Haoye Zhang, Shengding Hu, Zhi Zheng, Jie Zhou, Jie Cai, Xu Han, Guoyang Zeng, Dahai Li, Zhiyuan Liu, and Maosong Sun (2408.01800.pdf, p. 1).

### Model date:
The MiniCPM-V series includes several models released in 2024 (2408.01800.pdf, p. 2):
*   **MiniCPM-V 1.0:** Launched in February 2024.
*   **MiniCPM-V 2.0:** Introduced in April 2024.
*   **MiniCPM-Llama3-V 2.5:** Released in May 2024.

The associated research paper was submitted to arXiv on August 3, 2024 (2408.01800.pdf, p. 1).

### Model version:
This model card describes version **2.5** of the MiniCPM-V series (config.json.txt; preprocessor_config.json.txt). This version is part of a series of efficient Multimodal Large Language Models (MLLMs) designed for on-device deployment (2408.01800.pdf, p. 2).

Key differences between the versions are (2408.01800.pdf, p. 12, Table 3):
*   **MiniCPM-V 1.0 (2.8B):** Trained with pre-training stages 1 & 2 and SFT. It used a fixed resolution of 448x448.
*   **MiniCPM-V 2.0 (2.8B):** Included all three pre-training stages, SFT, and an adaptive visual encoding strategy for handling various image aspect ratios and resolutions up to 1.8M pixels. It also incorporated RLHF-V for alignment.
*   **MiniCPM-Llama3-V 2.5 (8.5B):** Builds upon version 2.0 by adopting Llama3-Instruct 8B as the base Large Language Model (LLM) and using RLAIF-V for alignment to reduce hallucinations.

### Model type:
MiniCPM-V is a Multimodal Large Language Model (MLLM) for multimodal dialogue tasks (configuration.json.txt). Its architecture comprises three main modules (2408.01800.pdf, p. 5):
1.  **Visual Encoder:** A SigLIP SoViT-400m/14 model is used to encode input images (2408.01800.pdf, p. 5). The vision model has 27 hidden layers, a hidden size of 1152, and 16 attention heads (config.json.txt). The last layer of the vision encoder is kept (i.e., `drop_vision_last_layer` is false) (config.json.txt).
2.  **Compression Layer:** A perceiver resampler with a single cross-attention layer compresses the visual tokens from the encoder into a fixed number of queries (96 for this version) (2408.01800.pdf, p. 6; config.json.txt). This resampler is adaptive and uses 2D sincos positional embeddings (resampler.py).
3.  **Large Language Model (LLM):** A `LlamaForCausalLM` model is used for conditional text generation based on the compressed visual tokens and text input (modeling_minicpmv.py). For version 2.5, the base LLM is Llama3-Instruct 8B (2408.01800.pdf, p. 12). The LLM has 32 hidden layers, a hidden size of 4096, 32 attention heads, and a vocabulary size of 128,256 (config.json.txt).

The model supports high-resolution images (e.g., 1344 × 1344) with any aspect ratio through an adaptive visual encoding technique that partitions the image into slices (2408.01800.pdf, p. 6).

**Model Size:**
*   **Parameters:** 8.5 billion (2408.01800.pdf, p. 13, Table 4).
*   **Total Size on Disk:** Approximately 34.15 GB (model.safetensors.index.json.txt).

### Training details:
The model's training process consists of three main phases (2408.01800.pdf, p. 6-9):

1.  **Pre-training:** This phase aims to align the visual modules with the LLM's input space. It is divided into three stages:
    *   **Stage 1:** The compression layer is warmed up using 200M image-text pairs at a 224x224 resolution, while the visual encoder and LLM remain frozen.
    *   **Stage 2:** The visual encoder is unfrozen and trained to handle a higher resolution of 448x448 using another 200M image-text pairs.
    *   **Stage 3:** Both the visual encoder and compression layer are trained using an adaptive visual encoding strategy for high-resolution inputs. OCR data is introduced in this stage to enhance OCR capabilities. The LLM remains frozen.
    *   Techniques like **Caption Rewriting** (using GPT-4 to refine web captions) and **Data Packing** (combining multiple samples into a fixed-length sequence) are used to improve data quality and training efficiency.

2.  **Supervised Fine-Tuning (SFT):** All model parameters are unfrozen to learn from high-quality, human-annotated visual question-answering datasets. The SFT data is divided into two parts: Part 1 focuses on basic recognition with short responses, and Part 2 enhances capabilities for generating detailed responses and following complex instructions.

3.  **RLAIF-V (Reinforcement Learning from AI Feedback for Vision):** To address hallucinations, the model is further aligned using Direct Preference Optimization (DPO). This involves:
    *   **Response Generation:** Sampling multiple responses from the policy model for a given instruction.
    *   **Feedback Collection:** Using an open-source MLLM (LLaVA-NeXT-Yi-34B) to evaluate the correctness of atomic claims extracted from each response.
    *   **DPO:** Constructing a preference dataset from the scored responses and optimizing the model.

### Paper or other resource for more information:
The primary resource is the academic paper describing the model series:
*   **Paper:** Yao, Y., Yu, T., Zhang, A., et al. (2024). *MiniCPM-V: A GPT-4V Level MLLM on Your Phone*. arXiv:2408.01800. Available at: https://arxiv.org/abs/2408.01800 (2408.01800.pdf).
*   **Repository:** https://github.com/OpenBMB/MiniCPM-V (2408.01800.pdf, p. 1).

The paper provides a comprehensive overview of the model's architecture, training techniques, performance benchmarks, and deployment strategies.

### Citation details:
To cite the model, please use the information from the associated research paper (2408.01800.pdf). A potential BibTeX entry is:
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

### License:
The model's code is licensed under the **Apache License, Version 2.0**. This license allows for commercial and private use, modification, and distribution, provided that the original copyright and license notices are retained. It does not grant trademark rights (configuration_minicpm.py; modeling_minicpmv.py; processing_minicpmv.py).

### Contact:
For questions or feedback, contact Yuan Yao at `yaoyuanthu@gmail.com` (2408.01800.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
MiniCPM-Llama3-V 2.5 is an efficient, multimodal large language model designed for deployment on end-side devices like mobile phones and personal computers (2408.01800.pdf, p. 2). Its primary intended use is for multimodal dialogue and question-answering tasks involving both text and images.

Key capabilities include:
*   **General Multimodal Understanding:** Answering questions about images, describing scenes, and performing complex reasoning (2408.01800.pdf, p. 4, Fig. 2).
*   **Strong OCR Capability:** Accurately transcribing text from images, including screenshots, documents, and tables, and converting structured data like tables into markdown format (2408.01800.pdf, p. 3, 15).
*   **High-Resolution Image Perception:** Handling images up to 1.8M pixels (e.g., 1344x1344) with any aspect ratio, allowing for recognition of fine-grained details (2408.01800.pdf, p. 3, 15).
*   **Multilingual Support:** Generalizing its multimodal capabilities to over 30 languages (2408.01800.pdf, p. 3, 14).
*   **Trustworthy Behavior:** The model is optimized to have lower hallucination rates compared to other leading models (2408.01800.pdf, p. 3).

The model takes a text prompt and one or more images as input and generates a text-based response (modeling_minicpmv.py).

### Primary intended users:
The primary users are developers and researchers building applications that require multimodal understanding on resource-constrained devices. This includes mobile app developers, AI researchers exploring efficient MLLMs, and businesses looking to integrate on-device AI for privacy-sensitive or offline scenarios (2408.01800.pdf, p. 2).

### Out-of-scope uses:
The model has several limitations and is not intended for the following uses:
*   **Processing other modalities:** The model is designed for image and text inputs only. It does not support video or audio (2408.01800.pdf, p. 17).
*   **High-stakes, safety-critical applications:** Despite efforts to reduce hallucinations, the model can still generate factually incorrect or nonsensical information. It should not be used in applications where errors could lead to harm, such as medical diagnosis or autonomous driving, without human oversight (2408.01800.pdf, p. 9).
*   **Real-time inference on current mobile hardware:** While optimized for on-device use, the model's latency may not be suitable for applications requiring real-time responses without further specialized hardware (NPU) acceleration and optimization (2408.01800.pdf, p. 17).
*   **Generating harmful or biased content:** The model was trained on large-scale web data and may reflect biases present in that data. It should not be used to generate offensive, discriminatory, or otherwise harmful content.

---

## How to Use
This section outlines how to use the model.

The model can be used for chat-based interaction involving images and text. The following Python code snippet demonstrates how to use the model with the `transformers` library (based on `modeling_minicpmv.py`).

**Input Structure:** The model accepts a list of messages, where each message has a `role` (`user` or `assistant`) and `content`. The content can be a string or a list containing strings and `PIL.Image.Image` objects.

**Output Structure:** The model generates a text string as a response. It can also be used in streaming mode to generate text token by token.

```python
import torch
from PIL import Image
import requests
from transformers import AutoModel, AutoProcessor

# Load the model and processor
model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

processor = AutoProcessor.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

# Prepare image and text prompt
image_url = 'https://i.imgur.com/294a22a.jpeg' # Example image of a cat on a laptop
image = Image.open(requests.get(image_url, stream=True).raw).convert('RGB')
question = 'What is in the image?'
msgs = [{'role': 'user', 'content': question}]

# The chat function handles the conversation history and image processing
# For a single-turn conversation, you can pass the image and messages directly
# The image is automatically placed at the beginning of the first user message
answer = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=processor.tokenizer,
    sampling=True, # Use sampling for generation
    temperature=0.7,
    max_new_tokens=1024
)
print(answer)

# Example Output:
# The image shows a cat sitting on a person's lap, looking at a laptop screen. The cat is a tabby with brown and black stripes, and it appears to be focused on the screen. The person's hands are visible on the laptop's keyboard, and the laptop is open, displaying a screen with some text or images. The setting seems to be indoors, possibly in a home or office environment.

# For multi-turn conversation, manage the `msgs` list
msgs.append({'role': 'assistant', 'content': answer})
msgs.append({'role': 'user', 'content': 'What color is the cat?'})

# In subsequent turns, the image is not needed if it's already part of the context
answer_2 = model.chat(
    image=None,
    msgs=msgs,
    tokenizer=processor.tokenizer,
    sampling=True,
    temperature=0.7
)
print(answer_2)

# Example Output:
# The cat is a tabby, which means it has a coat with stripes, dots, or swirling patterns. In this image, the cat has brown and black stripes.
```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Based on the model's design and evaluation, the following are key factors that influence its performance:
*   **Language:** The model is designed to be multilingual, and its performance varies across different languages. It was pre-trained on English and Chinese data and then fine-tuned with multilingual data to generalize to over 30 languages (2408.01800.pdf, p. 8, 14).
*   **Image Resolution and Aspect Ratio:** The model's performance on tasks requiring fine-grained detail (like OCR) is highly dependent on image resolution. The adaptive visual encoding mechanism was specifically designed to handle high-resolution images (up to 1.8M pixels) and variable aspect ratios effectively (2408.01800.pdf, p. 6).
*   **Task Complexity:** Performance varies by task, from basic recognition (e.g., short captions) to advanced reasoning (e.g., complex VQA, math problems) (2408.01800.pdf, p. 8, Table 2).

### Evaluation factors:
The model was evaluated across these factors:
*   **Language:** The model's multilingual performance was explicitly evaluated by translating the LLaVA Bench benchmark into 15+ languages and using GPT-4-Turbo for scoring (2408.01800.pdf, p. 14, Fig. 8).
*   **Task Type:** The model was evaluated on a wide range of tasks using a comprehensive set of benchmarks, including general VQA (MME, MMBench), reasoning (MMMU, MathVista), OCR (OCRBench, TextVQA), and hallucination detection (Object HalBench) (2408.01800.pdf, p. 13).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard benchmarks, each with its own scoring metric (2408.01800.pdf, p. 13):
*   **OpenCompass:** A comprehensive collection of 11 multimodal benchmarks. The specific metrics depend on the sub-task (e.g., accuracy for VQA). The paper reports an overall score.
*   **MME:** Measures both perception and cognition capabilities. The score is calculated as 100 * (accuracy_perception + accuracy_cognition).
*   **MMBench, MMMU, MathVista, LLaVA Bench:** These benchmarks typically use accuracy as the primary metric for evaluating question-answering capabilities.
*   **OCRBench, TextVQA, DocVQA:** These benchmarks evaluate OCR and text-understanding capabilities, often using accuracy or other task-specific metrics.
*   **Object HalBench:** Measures the rate of hallucination at both the response level and the mention level. Lower rates indicate better, more trustworthy performance.

### Decision thresholds:
Insufficient information.

### Variation approaches:
The performance metrics are reported as scores on the established test sets of the public benchmarks mentioned above. The paper presents these scores directly without discussing statistical variations like confidence intervals or cross-validation results (2408.01800.pdf, p. 13-15, Tables 4, 5, 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its capabilities comprehensively (2408.01800.pdf, p. 13):
*   **General Benchmarks:**
    *   **OpenCompass:** A collection including MME, MM-Bench, MMMU, MathVista, LLaVA Bench, etc.
    *   **RealWorldQA:** For real-world spatial understanding.
*   **OCR Benchmarks:**
    *   **OCRBench**
    *   **TextVQA**
    *   **DocVQA**
*   **Hallucination Benchmarks:**
    *   **Object HalBench**
*   **Multilingual Benchmarks:**
    *   **LLaVA Bench:** The reference responses were translated into over 15 languages to evaluate multilingual performance.

### Motivation:
These datasets were chosen because they are popular, widely used benchmarks that cover a diverse set of multimodal tasks. This allows for a comprehensive evaluation and a robust comparison against other state-of-the-art open-source and proprietary models (2408.01800.pdf, p. 13). The inclusion of OCR and hallucination benchmarks specifically targets key areas of improvement for the MiniCPM-V series.

### Preprocessing:
The paper does not detail specific preprocessing steps for the evaluation data, but it is assumed that the standard procedures for each benchmark were followed. The model's internal preprocessing for images involves the adaptive visual encoding strategy, which includes partitioning the image into slices, resizing, and applying 2D positional embedding interpolation (2408.01800.pdf, p. 6; image_processing_minicpmv.py).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The training data is composed of three main types, used across different training phases (2408.01800.pdf, p. 7-9):

1.  **Pre-training Data (Table 1):**
    *   **Image Captioning:** A total of 520 million image-text pairs.
        *   English (410M): COCO, VG, CC3M, CC12M, LAION-COCO, COYO, LAION-2B.
        *   Chinese (110M): AIC, LAION-2B-Chinese, WuKong, Zero-Chinese.
    *   **OCR+Knowledge:** A total of 50 million pairs.
        *   English (39M): WIT, IDL, SynthText, SynthDoG-en, ArxivCap.
        *   Chinese (11M): WIT, LAION-2B-OCR.

2.  **Supervised Fine-Tuning (SFT) Data (Table 2):**
    *   A collection of high-quality datasets divided into two parts:
        *   **Part 1 (Basic Recognition):** ~4.7M samples from datasets like Flickr-30K, COCO, VQAv2, RefCOCO, DocVQA, TextVQA, etc., focusing on short-form QA and captioning.
        *   **Part 2 (Advanced Capabilities):** ~3.8M samples from datasets like LLaVA-Instruct-150K, UniMM-Chat, ShareGPT4V, Ultra-Chat, Alpaca, etc., featuring long, detailed responses and complex instructions.
    *   Includes 90K multilingual data points covering 36 languages for multilingual conversation capability.

3.  **RLAIF-V Data:**
    *   A preference dataset consisting of 6,000 preference pairs derived from 3,000 unique images, created by scoring model-generated responses with an AI feedback model.

### Motivation:
The large-scale pre-training data was chosen to effectively align the visual encoder and compression layer with the LLM and to build a foundation of multimodal knowledge (2408.01800.pdf, p. 7). The SFT data was selected to instill more complex reasoning and instruction-following abilities from high-quality human annotations (2408.01800.pdf, p. 8). The RLAIF-V data was specifically constructed to mitigate the critical issue of hallucination (2408.01800.pdf, p. 9).

### Preprocessing:
Several preprocessing steps were applied to the training data to improve quality and efficiency (2408.01800.pdf, p. 7):
*   **Data Cleaning:** Image-text pairs with poor correlation and ill-formatted text were removed from the pre-training data.
*   **Caption Rewriting:** An auxiliary LLM, fine-tuned on a seed set annotated by GPT-4, was used to rewrite low-quality web captions into a more structured question-answer format.
*   **Data Packing:** To improve memory usage and computational efficiency, multiple samples of varying lengths were packed into a single fixed-length sequence. Position IDs and attention masks were modified to prevent interference between packed samples.
*   **Image Preprocessing:** During Stage 3 of pre-training, the adaptive visual encoding strategy was used for high-resolution images. For image inputs, normalization is applied with a mean of `[0.5, 0.5, 0.5]` and a standard deviation of `[0.5, 0.5, 0.5]` (image_processing_minicpmv.py).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results across several factors:

*   **Overall Performance (Table 4):** MiniCPM-Llama3-V 2.5 achieves a score of 65.1 on OpenCompass, 2024.6 on MME, 77.2 on MMBench (en), 86.7 on LLaVA Bench, and a hallucination rate of 10.3%/5.0% on Object HalBench (2408.01800.pdf, p. 13).
*   **OCR Performance (Table 5):** The model scores 725 on OCRBench, 76.6 on TextVQA val, and 84.8 on DocVQA test (2408.01800.pdf, p. 14).
*   **Effect of RLAIF-V (Table 6):** With RLAIF-V, the OpenCompass score improves from 64.5 to 65.1, and Object HalBench hallucination rates improve from 86.9%/93.6% correct to 89.7%/95.0% correct (equivalent to a reduction in hallucination) (2408.01800.pdf, p. 15).
*   **Effect of Multilingual Training (Table 7):** Adding multilingual SFT data significantly improves performance on the LLaVA Bench across various languages. For example, performance in German improves from 22.8 to 76.5, and in Japanese from 13.8 to 67.9 (2408.01800.pdf, p. 15).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   The full fp16 version of the model requires **16-17 GB** of memory (2408.01800.pdf, p. 10).
*   Using Q4_K_M 4-bit quantization (within the GGML framework), the memory requirement is reduced to approximately **5 GB**, making it suitable for mobile phone deployment (2408.01800.pdf, p. 10).

### Deploying Requirements:
The model is designed for deployment on end-side devices. Performance tests were conducted on (2408.01800.pdf, p. 12):
*   **Xiaomi 14 Pro** (Snapdragon 8 Gen 3)
*   **vivo X100 Pro** (Mediatek Dimensity 9300)
*   **Macbook Pro** (M1)

On a Xiaomi 14 Pro with NPU acceleration for the vision encoder, the model achieves a visual encoding time of 1.3s and a decoding throughput of 8.2 tokens/s (2408.01800.pdf, p. 11-12).

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Hallucination and Trustworthiness:** A primary ethical challenge for MLLMs is generating content that is not factually grounded in the image (hallucination). This poses risks, especially in high-stakes scenarios. The developers explicitly addressed this by incorporating the RLAIF-V training phase, which uses AI feedback to reduce hallucination rates and improve the model's trustworthiness. Performance on the Object HalBench was used to measure this improvement (2408.01800.pdf, p. 9, 15).
*   **Data Privacy:** The model is designed for on-device deployment, which is presented as a solution for privacy-protective scenarios, as user data does not need to be sent to cloud servers (2408.01800.pdf, p. 2).
*   **Bias in Training Data:** The model was pre-trained on large-scale web-crawled datasets like LAION-2B (2408.01800.pdf, p. 7). Such datasets are known to contain societal biases, which the model may learn and perpetuate. The paper mentions data cleaning to remove pairs with poor correlation but does not detail specific steps taken to mitigate societal biases.
*   **Potential for Misuse:** As a capable generative model, MiniCPM-V could be misused to create misleading or harmful content. Making the model efficient and accessible on end-devices could lower the barrier for such misuse. The developers do not specify any built-in safeguards against misuse beyond the general alignment for helpfulness and truthfulness.
*   **Sensitive Data:** The training data includes large web-crawled datasets which may inadvertently contain personal or sensitive information. The paper does not discuss methods for identifying or removing such data.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge several limitations in the current version of the model (2408.01800.pdf, p. 17):
*   **Capability Depth and Efficiency:** There is still significant room for improvement in the model's multimodal understanding and inference efficiency.
*   **Limited Modalities:** The model only supports image and text inputs and does not handle other modalities like video or audio.
*   **On-Device Performance:** Despite optimizations, the inference speed and latency on mobile devices are "still far from good enough" for many real-world applications. Performance can also be limited by the device's battery capacity.
*   **Potential for Hallucination:** While reduced, the model can still produce hallucinations. Users should be critical of the model's outputs and verify important information, especially in sensitive contexts.

### Recommendations:
*   **Use Quantization for Deployment:** For on-device deployment, users are recommended to use a 4-bit quantized version of the model to meet the memory constraints of mobile devices (2408.01800.pdf, p. 10).
*   **Leverage Hardware Acceleration:** To achieve acceptable performance, users should leverage hardware acceleration where available, such as the NPU on Qualcomm chips for visual encoding (2408.01800.pdf, p. 12).
*   **Human-in-the-Loop:** Due to the risk of hallucination, it is recommended to use the model in applications where a human can oversee or verify its output, rather than in fully autonomous, safety-critical systems.
*   **Awareness of Bias:** Users should be aware that the model may generate content that reflects societal biases present in its training data.