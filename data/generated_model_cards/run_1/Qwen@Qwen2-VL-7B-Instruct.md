## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The Qwen2-VL model series was developed by the Qwen Team at Alibaba Group (Wang et al., 2024, p. 1).

### Model date:
The research paper presenting the model was submitted to arXiv on October 3, 2024. The knowledge cutoff for the data used to train the model is June 2023 (Wang et al., 2024, p. 1, 5).

### Model version:
This model card describes the Qwen2-VL series, which is an advanced upgrade of the previous Qwen-VL models. The series includes three open-weight models with different parameter counts (Wang et al., 2024, p. 1, 3):
*   **Qwen2-VL-2B:** The most efficient model, with 2 billion parameters (1.5B for the LLM and 675M for the vision encoder), designed for on-device execution. It provides adequate performance for scenarios with limited resources (Wang et al., 2024, p. 3).
*   **Qwen2-VL-7B:** A performance-optimized model with 8 billion parameters (7.6B for the LLM and 675M for the vision encoder). It features significant upgrades for text recognition and video understanding and delivers strong performance across a broad range of visual tasks (Wang et al., 2024, p. 3).
*   **Qwen2-VL-72B:** The most capable model, with 72 billion parameters. It offers further improvements in visual reasoning, instruction-following, decision-making, and agent capabilities, delivering optimal performance on complex tasks (Wang et al., 2024, p. 3).

This series introduces key architectural upgrades over the original Qwen-VL, including Naive Dynamic Resolution and Multimodal Rotary Position Embedding (M-RoPE) (Wang et al., 2024, p. 1).

### Model type:
Qwen2-VL is a series of Large Vision-Language Models (LVLMs) designed for multimodal understanding, processing text, images, and videos (Wang et al., 2024, p. 1).

*   **Architecture:** The model follows a common LVLM framework of a visual encoder connected to a Large Language Model (LLM). It uses a Vision Transformer (ViT) with approximately 675 million parameters as the vision encoder and the Qwen2 series for the language model component (Wang et al., 2024, p. 3-4). The specific architecture is `Qwen2VLForConditionalGeneration` (`config.json`).
*   **Key Components:**
    *   **Naive Dynamic Resolution:** Allows the model to process images of any resolution by dynamically converting them into a variable number of visual tokens, which more closely aligns with human perception (Wang et al., 2024, p. 1, 4).
    *   **Multimodal Rotary Position Embedding (M-RoPE):** An enhancement that deconstructs rotary embeddings into temporal, height, and width components. This facilitates the effective fusion of positional information across text, images, and videos, improving comprehension of dynamic content like videos (Wang et al., 2024, p. 1, 4-5).
*   **Model Size and Parameters:** The series is available in 2B, 8B, and 72B parameter versions (Wang et al., 2024, p. 3). The specific model described by the provided repository files has a total size of approximately 16.58 GB (`model.safetensors.index.json`). Key parameters from the configuration file include (`config.json`):
    *   `hidden_size`: 3584
    *   `intermediate_size`: 18944
    *   `num_hidden_layers`: 28
    *   `num_attention_heads`: 28
    *   `num_key_value_heads`: 4
    *   `vocab_size`: 152064
*   **Context Length:** The model supports a maximum context length of 32,768 tokens (`config.json`, `tokenizer_config.json`).

### Training details:
The Qwen2-VL models were trained using a three-stage methodology on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service (Wang et al., 2024, p. 5, 8).

*   **Training Stages (Wang et al., 2024, p. 5):**
    1.  **Stage 1 (ViT Pre-training):** The Vision Transformer (ViT) component is trained on a large corpus of image-text pairs to learn core visual-textual correlations. The LLM component is initialized from pre-trained Qwen2 weights.
    2.  **Stage 2 (Full-parameter Pre-training):** All model parameters are unfrozen and trained on a cumulative total of 1.4 trillion tokens, including mixed image-text content, OCR data, and visual question-answering datasets. This stage enhances nuanced understanding and multitasking capabilities.
    3.  **Stage 3 (Instruction Fine-tuning):** The ViT parameters are locked, and the LLM is exclusively fine-tuned on a diverse set of instruction-following datasets constructed in the ChatML format. This includes multimodal conversations, document parsing, and agent-based interactions.
*   **Training Infrastructure (Wang et al., 2024, p. 8):**
    *   **Hardware:** Alibaba Cloud's PAI-Lingjun Intelligent Computing Service.
    *   **Software:** PyTorch version 2.1.2 with CUDA 11.8.
    *   **Optimization Techniques:** Training was scaled using 3D parallelism (Data, Tensor, and Pipeline Parallelism). It also leveraged DeepSpeed's ZeRO-1 optimizer, sequence parallelism, selective checkpointing, and FlashAttention for memory and computational efficiency.
*   **Generation Parameters (`generation_config.json`):**
    *   `do_sample`: true
    *   `temperature`: 0.01
    *   `top_p`: 0.001
    *   `top_k`: 1
    *   `repetition_penalty`: 1.0

### Paper or other resource for more information:
*   **Primary Paper:** Wang, P., Bai, S., Tan, S., Wang, S., Fan, Z., Bai, J., ... & Lin, J. (2024). *Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution*. arXiv preprint arXiv:2409.12191. This paper provides a comprehensive overview of the model's architecture, training process, and performance evaluations.
*   **Code Repository:** The official code is available on GitHub at [https://github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL) (Wang et al., 2024, p. 1).

### Citation details:
To cite the model and its accompanying paper, please use the following BibTeX format (Wang et al., 2024):
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

### License:
The model is licensed under the Apache License, Version 2.0 (`LICENSE.txt`). This is a permissive open-source license that allows users to:
*   **Use:** Freely use the software for commercial and private purposes.
*   **Modify:** Create and distribute derivative works.
*   **Distribute:** Reproduce and distribute copies of the work or derivative works.

Key conditions include retaining copyright and license notices. The license also includes a disclaimer of warranty and a limitation of liability (`LICENSE.txt`). The full license text is available at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).

### Contact:
No direct contact email is provided. For questions, issues, or feedback, users are encouraged to engage with the development team through the official GitHub repository: [https://github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL) (Wang et al., 2024, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The Qwen2-VL series is designed as a versatile, general-purpose Large Vision-Language Model with a wide range of capabilities for processing and understanding multimodal inputs (text, images, and videos).

*   **Core Capabilities (Wang et al., 2024, p. 2-3):**
    *   **General Visual Question Answering:** Engaging in general chat about visual content, identifying objects, and describing complex scenes (Wang et al., 2024, p. 25-26).
    *   **Document and Diagram Understanding:** Reading and interpreting text within documents, charts, and high-resolution infographics (Wang et al., 2024, p. 11, 27).
    *   **Multilingual OCR:** Understanding and transcribing text in multiple languages from images, including English, Chinese, most European languages, Japanese, Korean, Arabic, and Vietnamese (Wang et al., 2024, p. 3, 11, 28-31).
    *   **Video Understanding:** Comprehending and answering questions about video content, including extended-duration videos over 20 minutes in length (Wang et al., 2024, p. 3, 41-42).
    *   **Visual Grounding and Referring Comprehension:** Localizing and identifying specific objects or regions in an image based on textual descriptions (Wang et al., 2024, p. 6, 11, 43).
    *   **Mathematical and Code Reasoning:** Solving mathematical problems presented in visual formats and understanding algorithmic problems from screenshots (Wang et al., 2024, p. 11, 32-35).
    *   **Visual Agent and Function Calling:** Acting as a visual agent to perform tasks like UI operations on mobile devices, interacting with tools through function calls based on visual and text inputs (Wang et al., 2024, p. 3, 7, 12, 44-45).
*   **Input-Output Structure:** The model accepts a combination of text, images, and videos as input. The output is generated text, which can be a direct answer, a description, a piece of code, or a function call depending on the task (`chat_template.json`, Wang et al., 2024, p. 6-7).

### Primary intended users:
The primary intended users are researchers and developers in the field of artificial intelligence. The open-weight release of the models is intended to enable these users to "harness the full potential in a variety of applications and research projects" and to "advance AI technologies" (Wang et al., 2024, p. 16).

### Out-of-scope uses:
Insufficient information.

---

## How to Use
This section outlines how to use the model.

The model uses a specific chat template with special tokens to handle multimodal inputs. A conversation consists of turns from a `system`, `user`, and `assistant`.

*   **Chat Template (`chat_template.json`):**
    Each message is enclosed by `<|im_start|>{role}\n{content}<|im_end|>\n`.
    *   A system prompt is automatically added if the first message is not from the system: `<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n`.
    *   Visual inputs (images or videos) are embedded within the user's text prompt using special tokens. For example, an image is represented as `<|vision_start|><|image_pad|><|vision_end|>`.

*   **Example: Dialogue with Images (Wang et al., 2024, p. 6):**
    ```
    <|im_start|>user
    <|vision_start|>Picture1.jpg<|vision_end|><|vision_start|>Picture2.jpg<|vision_end|>What do the two pictures have in common?<|im_end|>
    <|im_start|>assistant
    Both pictures are of SpongeBob SquarePants.<|im_end|>
    ```

*   **Example: Visual Grounding (Referring Comprehension) (Wang et al., 2024, p. 7):**
    The model can generate bounding box coordinates for objects referenced in text.
    *   **Input:**
        ```
        <|im_start|>user
        <|vision_start|>Picture1.jpg<|vision_end|>Detect the bounding box of 'the red car'<|im_end|>
        ```
    *   **Sample Output:**
        ```
        <|im_start|>assistant
        <|object_ref_start|>the red car<|object_ref_end|><|box_start|>(701,531),(869,675)<|box_end|>
        <|im_end|>
        ```

*   **Example: Visual Agent for UI Operations (Wang et al., 2024, p. 7):**
    The model can be prompted with a system message defining a set of actions (e.g., `Tap`, `Home`) and then perform multi-step reasoning to complete a task on a device.
    *   **Input:**
        ```
        <|im_start|>system
        You are a helpful assistant.
        # Actions
        ## You have the following actions.
        ### Tap
        ...
        *FUNCTION*: The action to take...<|im_end|>
        <|im_start|>user
        Find a pizza restaurant nearby in Map.<|vision_start|>Screenshot_1.jpg<|vision_end|><|im_end|>
        ```
    *   **Sample Output:**
        ```
        <|im_start|>assistant
        Several e-mails are displaying on the phone screen. To open Map, I need go back to the home screen and find the corresponding app icon.
        *FUNCTION*: Home *ARGS*: {}
        *RESULT*: <|vision_start|>Screenshot_2.jpg<|vision_end|>
        *RETURN*: I return to the home screen. Next, I need to find the icon of Map and tap on it.
        ...
        <|im_end|>
        ```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
Based on the model's design and evaluation, the following are key factors that influence its performance:
*   **Image Resolution and Aspect Ratio:** The model is specifically designed with a "Naive Dynamic Resolution" mechanism to handle images of varying resolutions and aspect ratios effectively. The ablation studies confirm that performance on perceptual tasks like OCR and VQA is sensitive to image size, with dynamic resolution providing a robust and efficient approach compared to fixed-size strategies (Wang et al., 2024, p. 1, 14).
*   **Language:** The model has multilingual capabilities, and its performance on tasks like OCR varies across different languages. It was evaluated on English, Chinese, Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (Wang et al., 2024, p. 3, 9).
*   **Modality:** The model's performance is dependent on the input modality (text, image, video). Its M-RoPE architecture was specifically developed to better handle temporal information in videos (Wang et al., 2024, p. 5).
*   **Task Complexity:** Performance varies significantly based on the complexity of the task, from simple object recognition to multi-step agent-based reasoning or advanced multi-disciplinary problems (Wang et al., 2024, p. 9).

### Evaluation factors:
The model was evaluated across the relevant factors identified above:
*   **Task Type:** Performance was disaggregated across a wide array of benchmarks, each representing a different capability, such as general visual question answering, document understanding, mathematical reasoning, video comprehension, and agent abilities (Wang et al., 2024, p. 9-12).
*   **Language:** Multilingual OCR performance was explicitly reported for Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (Wang et al., 2024, p. 9, Table 3).
*   **Model Scale:** Results were reported separately for the 2B, 7B, and 72B model versions to analyze scaling laws (Wang et al., 2024, p. 9, 15).
*   **Image Resolution:** An ablation study was conducted to analyze the impact of different image resolutions (both fixed and dynamic) on performance across several benchmarks (Wang et al., 2024, p. 14).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of metrics specific to each evaluation benchmark (Wang et al., 2024, p. 9-10):
*   **Accuracy:** Used for benchmarks like MMMU, DocVQA, InfoVQA, AI2D, ChartQA, and MathVista.
*   **Score:** Used for composite benchmarks like OCRBench and MME.
*   **Success Rate (SR):** Used for agent tasks like Number Line, BlackJack, ALFRED, R2R, and REVERIE to measure if the agent successfully completed the task.
*   **Goal-Condition Success (GC):** A metric for the ALFRED benchmark that measures the completion of sub-goals.
*   **Type Match (TM) and Exact Match (EM):** Used for function calling benchmarks (FnCall, AITZ) to measure the accuracy of the selected function and its arguments, respectively.

The selection of these metrics is justified by their common usage as standard evaluation measures for their respective well-established benchmarks.

### Decision thresholds:
For text generation, the model uses the following decision thresholds (`generation_config.json`):
*   **`temperature`:** 0.01
*   **`top_p`:** 0.001
*   **`top_k`:** 1

These parameters result in highly deterministic output, favoring the most likely token at each step of the generation process.

### Variation approaches:
Insufficient information.

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive set of public, state-of-the-art benchmarks to assess its capabilities across various domains. These datasets are publicly available and widely used for evaluating LVLMs.

*   **General VQA:** RealWorldQA, MMStar, MMVet, MMT-Bench, MMBench, MME, HallusionBench (Wang et al., 2024, p. 9).
*   **Document & Diagram Reading:** DocVQA, ChartQA, InfoVQA, TextVQA, AI2D, OCRBench (Wang et al., 2024, p. 9, 11).
*   **Multilingual OCR:** MTVQA and an internal benchmark covering Korean, Japanese, French, German, Italian, Russian, Vietnamese, and Arabic (Wang et al., 2024, p. 9, 11).
*   **Mathematical Reasoning:** MathVista, MathVision (Wang et al., 2024, p. 9, 11).
*   **Referring Expression Comprehension:** RefCOCO, RefCOCO+, RefCOCOg (Wang et al., 2024, p. 11-12).
*   **Video Understanding:** MVBench, PerceptionTest, EgoSchema, Video-MME (Wang et al., 2024, p. 10, 11).
*   **Agent & Function Calling:** AITZ, Number Line, BlackJack, EZPoint, Point24, ALFRED, R2R, REVERIE, and an internal FnCall dataset (Wang et al., 2024, p. 10, 12).

### Motivation:
These datasets were chosen to provide an extensive and rigorous evaluation of the Qwen2-VL series. The selection covers a wide spectrum of visual perception and high-level cognition tasks, allowing for a comprehensive comparison against previous state-of-the-art and closed-source models like GPT-4o. The benchmarks were selected to demonstrate the model's specific advantages in areas like document understanding, multilingual capabilities, and agent abilities (Wang et al., 2024, p. 8-9).

### Preprocessing:
*   **Image Preprocessing:** Input images are normalized using a mean of `[0.48145466, 0.4578275, 0.40821073]` and a standard deviation of `[0.26862954, 0.26130258, 0.27577711]` (`preprocessor_config.json`). For the dynamic resolution approach, small images are upscaled to surpass a minimum pixel threshold (`min_pixels`) before being fed into the model (Wang et al., 2024, p. 14).
*   **Video Preprocessing:** For the Video-MME benchmark, which includes videos up to one hour long, the maximum number of frames extracted per video was limited to 768 during evaluation (Wang et al., 2024, p. 12).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale, diverse corpus of multimodal data totaling 1.4 trillion tokens (Wang et al., 2024, p. 6).
*   **Pre-training Data:** The pre-training dataset is a diverse mix that includes (Wang et al., 2024, p. 5):
    *   Image-text pairs
    *   Optical Character Recognition (OCR) data
    *   Interleaved image-text articles
    *   Visual Question Answering (VQA) datasets
    *   Video dialogues
    *   Image knowledge datasets
    The data sources primarily consist of cleaned web pages, open-source datasets, and synthetic data (Wang et al., 2024, p. 5).
*   **Instruction Fine-tuning Data:** For the final stage of training, a dataset of instruction-following data was constructed using the ChatML format. This included pure text-based dialogues as well as multimodal conversational data covering image question-answering, document parsing, multi-image comparison, video comprehension, and agent-based interactions (Wang et al., 2024, p. 6).

### Motivation:
The choice of a diverse, large-scale dataset was motivated by the goal of developing a robust and versatile multimodal understanding capability. The mix of image-text pairs, OCR data, and VQA datasets in pre-training was instrumental for building a strong foundation of core visual-textual correlations. The inclusion of multimodal instruction data in the fine-tuning stage was aimed at enhancing the model's ability to understand and execute a wide range of instructions across various modalities (Wang et al., 2024, p. 5-6).

### Preprocessing:
*   **Video Data:** To preserve information, videos in the training set were sampled at two frames per second. To balance computational demands with comprehension, the resolution of each video frame was dynamically adjusted to limit the total number of tokens per video to 16,384 (Wang et al., 2024, p. 5).
*   **Data Formatting:** Vision and text inputs are demarcated using special tokens. `<|vision_start|>` and `<|vision_end|>` are inserted at the start and end of the image feature sequence. For dialogue data, each turn is marked with `<|im_start|>` and `<|im_end|>` tokens to follow the ChatML format (Wang et al., 2024, p. 6).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative results disaggregated by model size, task, and language.

*   **Performance by Model Size and Benchmark:** Table 2 compares the performance of Qwen2-VL-2B, Qwen2-VL-7B, and Qwen2-VL-72B against previous state-of-the-art models across 20 benchmarks, showing strong scaling with model size (Wang et al., 2024, p. 9). For example, on DocVQA, the scores are 90.1, 94.5, and 96.5 for the 2B, 7B, and 72B models, respectively.
*   **Performance by Language:** Table 3 shows the multilingual OCR performance of Qwen2-VL-72B compared to GPT-4o across 8 languages. Qwen2-VL-72B achieves higher scores in most languages, such as 94.5 vs. 87.8 in Korean and 94.1 vs. 89.7 in French (Wang et al., 2024, p. 9).
*   **Performance by Capability:** Figure 6(a) illustrates how performance scales with model size across five capability dimensions: OCR, Video, General VQA, MMMU (college-level problems), and Math. Performance improves consistently with model size, especially for mathematical abilities (Wang et al., 2024, p. 16).
*   **Performance by Training Data Volume:** Figure 6(b) shows the performance of Qwen2-VL-7B on several benchmarks as the number of training tokens increases during the second pre-training stage. Performance on tasks like AI2D and InfoVQA shows steady improvement as more data is used (Wang et al., 2024, p. 16).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is approximately 16.58 GB (`model.safetensors.index.json`). The model uses `bfloat16` precision (`config.json`). Therefore, loading and running the model for inference requires a GPU or system with at least 17 GB of VRAM/RAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Training the Qwen2-VL models requires a large-scale, distributed computing environment.
*   **Platform:** The models were trained on Alibaba Cloud's PAI-Lingjun Intelligent Computing Service (Wang et al., 2024, p. 8).
*   **Software:** The training stack used PyTorch 2.1.2 and CUDA 11.8 (Wang et al., 2024, p. 8).
*   **Hardware:** While specific GPU counts are not provided, the use of 3D parallelism (Data, Tensor, and Pipeline) for the 72B model implies a multi-node cluster of high-end accelerator cards (e.g., NVIDIA A100 or H100 GPUs) is necessary for training from scratch or full fine-tuning (Wang et al., 2024, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The training data for Qwen2-VL includes "cleaned web pages, open-source datasets, and synthetic data" (Wang et al., 2024, p. 5). While the term "cleaned" is used, the provided documents do not specify the exact filtering methods or what types of data (e.g., personal information, protected attributes) were removed or retained.

*   **Risks:** As a general-purpose large vision-language model, Qwen2-VL is susceptible to the same risks inherent in similar technologies. These include, but are not limited to:
    *   Generating biased, harmful, or toxic content.
    *   Creating or perpetuating misinformation.
    *   Potential for misuse in applications like surveillance or generating non-consensual content.
    *   Reinforcing societal biases present in the training data.
*   **Risk Mitigation:** The provided paper and repository files do not detail specific risk mitigation strategies, such as bias evaluations, red-teaming efforts, or safety-specific fine-tuning. The Apache 2.0 license includes a disclaimer of warranty and limitation of liability, placing the responsibility on the user to determine the appropriateness of using the model and to assume any associated risks (`LICENSE.txt`).
*   **Sensitive Data:** It is not specified whether sensitive data was used during training. Given that a portion of the data comes from web pages, it is possible that personal or sensitive information was present in the raw data corpus.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers have identified several areas where the model has limitations:
*   **Complex Reasoning:** On the MMMU benchmark, which evaluates massive multi-discipline understanding, the model's performance lags behind top-tier closed-source models like GPT-4o. This indicates "room for improvement when handling more complex and challenging problem sets" (Wang et al., 2024, p. 9).
*   **Long Video Understanding:** During evaluation on the Video-MME benchmark, the number of frames extracted per video was limited to 768. This may have negatively impacted performance on very long videos (over 20 minutes). Future work is planned to extend the model's capabilities for longer sequences (Wang et al., 2024, p. 12).
*   **Vision-Language Navigation (VLN):** The model's performance on VLN tasks (R2R, REVERIE) is "significantly behind current specialized VLN models." This gap is attributed to the model's difficulty in generating complete and structured map information from a series of visual inputs, which remains a major challenge for general-purpose multimodal models (Wang et al., 2024, p. 13).

### Recommendations:
Based on the identified caveats, users should consider the following:
*   For tasks requiring expert-level, multi-disciplinary reasoning, the model's outputs should be carefully verified.
*   When using the model for understanding very long videos, performance may degrade. For critical applications, users should be aware of this limitation.
*   For specialized tasks like autonomous navigation in 3D environments, dedicated models may provide better performance than Qwen2-VL in its current state.
*   Users should be aware of the general ethical risks associated with large language models and use the model responsibly.