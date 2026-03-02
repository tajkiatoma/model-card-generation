## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh from Hugging Face and Sorbonne Université (Paper, p. 1).

### Model date:
The research paper describing the model was submitted to arXiv on May 3, 2024 (Paper, p. 1). The training data was filtered to remove opted-out content as of January 2024 (Paper, p. 6).

### Model version:
The model is named Idefics2. It is an 8 billion parameter model that builds upon the insights from developing its predecessor, Idefics1 (Paper, p. 1, 8). The developers have released three versions: a base pre-trained model, an instruction-tuned version, and a chat-optimized version (Paper, p. 1). The model was developed using `transformers` version `4.39.0.dev0` (config.json).

### Model type:
Idefics2 is a multi-modal vision-language model (VLM) that accepts images and text as input and generates text as output (Paper, p. 2).

**Architecture:**
*   It employs a **fully autoregressive architecture**, where visual and text features are concatenated and fed into the language model (Paper, p. 3).
*   **Vision Backbone:** The model uses a pre-trained vision transformer, specifically **SigLIP-SO400M** (Paper, p. 6). The vision encoder has 27 hidden layers, a hidden size of 1152, and 16 attention heads. It processes images with a patch size of 14x14 (config.json).
*   **Language Backbone:** The text decoder is based on the **Mistral-7B-v0.1** model (Paper, p. 6). It has a vocabulary size of 32,003 and supports a maximum position embedding of 32,768 (config.json).
*   **Connector Module:** To bridge the vision and text modalities, Idefics2 uses a **perceiver resampler** to pool the visual features into a fixed number of tokens (64 by default), followed by a modality projection layer (Paper, p. 3, 5).

**Size and Context:**
*   **Parameters:** 8 billion parameters (Paper, p. 1).
*   **Total Size:** The model weights have a total size of approximately 33.6 GB (model.safetensors.index.json).
*   **Image Resolution:** The model can handle images with a resolution up to 980x980 pixels (Paper, p. 7; config.json).
*   **Context Length:** The language model supports a context length of up to 32,768 tokens (config.json).

### Training details:
The model was trained in a multi-stage process:

**1. Pre-training:**
The base model was pre-trained starting from SigLIP-SO400M and Mistral-7B-v0.1 backbones (Paper, p. 6). The pre-trained backbones were adapted using **Low-Rank Adaptation (LoRA)** to ensure training stability (Paper, p. 4). The pre-training was divided into two stages:
*   **Stage 1:** The model was trained with a maximum image resolution of 384 pixels and a global batch size of 2048. The data mixture consisted of 70% interleaved image-text documents (OBELICS) and 30% image-text pairs (Paper, p. 7).
*   **Stage 2:** PDF documents were introduced into the training mix, and the maximum image resolution was increased to 980 pixels. The data mixture was 45% OBELICS, 35% image-text pairs, and 20% PDF documents (Paper, p. 7).
The pre-training used a learning rate of 1e-4 and covered approximately 1.5 billion images and 225 billion text tokens over 2 epochs (Paper, p. 7).

**2. Instruction Fine-tuning:**
Following pre-training, the model was instruction-tuned using **Decomposed Low-Rank Adaptation (DoRA)**, a variant of LoRA (Paper, p. 8). The training data was a massive collection of 50 vision-language datasets, named **The Cauldron**, supplemented with text-only instruction datasets to improve reasoning and instruction-following capabilities (Paper, p. 8). To prevent overfitting, the training process incorporated NEFTune (adding noise to embeddings), random scaling of image resolutions, and shuffling of conversational turns (Paper, p. 8).

**3. Chat Fine-tuning:**
To create the chat version, the instruction-tuned model was further fine-tuned for a few hundred steps on dialogue data from LLaVA-Conv and ShareGPT4V datasets (Paper, p. 9).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Laurençon, H., Tronchon, L., Cord, M., & Sanh, V. (2024). *What matters when building vision-language models?* arXiv preprint arXiv:2405.02246. (Paper, p. 1).

A collection of related resources, including the model, is available on the Hugging Face Hub:
*   `https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe` (Paper, p. 2).

### Citation details:
```bibtex
@misc{laurencon2024matters,
      title={What matters when building vision-language models?}, 
      author={Hugo Laurençon and Léo Tronchon and Matthieu Cord and Victor Sanh},
      year={2024},
      eprint={2405.02246},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(Paper, p. 1)

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Idefics2 is a foundational vision-language model designed for a wide range of tasks that require understanding both images and text. Its primary capabilities include:
*   **Document Understanding:** Retrieving information from scanned PDFs and documents (Paper, p. 2, 7).
*   **Visual Question Answering (VQA):** Answering questions about charts, diagrams, and general images (Paper, p. 2).
*   **Optical Character Recognition (OCR):** Transcribing text from images (Paper, p. 2).
*   **Image Captioning and Description:** Describing the content of an image (Paper, p. 3).
*   **Code Generation:** Converting screenshots of webpages into functional code (Paper, p. 2).
*   **Multi-modal Reasoning:** Handling an arbitrary number of interleaved images and text within a long context (Paper, p. 6).

The model takes a sequence of images and/or text as input and generates a text string as output. The input format for conversational use is specified by a chat template (processor_config.json).

### Primary intended users:
The model is intended for researchers and developers in the vision-language and broader AI community. It is released as a resource to facilitate progress and experimentation in the field (Paper, p. 2).

### Out-of-scope uses:
The model is not designed for and should not be used for applications that could cause harm. Based on red-teaming analysis, the following uses are explicitly out-of-scope:
*   **Perpetuating Stereotypes:** Making judgments or perpetuating historical disparities about individuals' professions, social status, or other attributes based on visual cues like age, attire, or gender (Paper, p. 25).
*   **Harassment and Harmful Content:** Generating content that promotes online harassment or creating offensive memes that reinforce harmful associations (Paper, p. 25).
*   **Making Assumptions about Individuals:** Assuming emotional states, mental conditions, or attractiveness based on visual appearance (Paper, p. 25).
*   **Security-Risk Applications:**
    *   Systematically solving CAPTCHAs with distorted text (Paper, p. 25).
    *   Developing phishing schemes from screenshots of legitimate websites (Paper, p. 25).
    *   Generating step-by-step instructions for creating dangerous items like explosives or for modifying firearms (Paper, p. 25).

---

## How to Use
This section outlines how to use the model.

The model can be used for multi-modal chat by formatting the input as a conversation. The input should be a list of messages, where each message has a `role` (`User` or `Assistant`) and `content`, which is a list of dictionaries specifying the `type` (`text` or `image`) and the data. The special token `<image>` is used as a placeholder for images in the text.

The chat template is defined as:
`{% for message in messages %}{{message['role'].capitalize()}}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}<end_of_utterance>\n{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}` (processor_config.json).

**Example 1: Chart Analysis** (Paper, Figure 1, p. 1)
*   **Input:**
    *   Image: A table of financial data for 2014 and 2015.
    *   Prompt: "For 2024, the interest expense is twice what it was in 2014, and the long-term debt is 10% higher than its 2015 level. Can you calculate the combined total of the interest and long-term debt for 2024?"
*   **Output:** "Yes, I can help you calculate that. First, let's find out the interest expense for 2024: Interest Expense (2024) = 2 * Interest Expense (2014) = 2 * 630 = 1260. Next, let's find the long-term debt for 2024: Long-Term Debt (2024) = Long-Term Debt (2015) + 10% of Long-Term Debt (2015) = 19,260 + 0.1 * 19,260 = 19,260 + 1,926 = 21,186. Now, we can add these two amounts together to get the combined total of the interest and long-term debt for 2024: Combined Total (2024) = Interest Expense (2024) + Long-Term Debt (2024) = 1260 + 21,186 = 22,446. So, the combined total of the interest and long-term debt for 2024 is $22,446."

**Example 2: Text Transcription** (Paper, Figure 3, p. 8)
*   **Input:**
    *   Image: A handwritten letter.
    *   Prompt: `<image>The content of the letter is:\n`
*   **Output:** "Dear Craig, Actually, I've never been big on letter writing, though it is nice to receive a hand written note from someone. I am afraid that the art of drawing, and the related ability to sketch an idea, are also being lost. But perhaps, as the cliche goes, what goes around comes around. Good luck with your project. Tom Cianfichi"

**Example 3: Resume Parsing** (Paper, Figure 5, p. 24)
*   **Input:**
    *   Image: A resume.
    *   Prompt: "Extract the name, email, current job, and education. Output a JSON format."
*   **Output:**
```json
{
  "name": "Yann Karpathy",
  "email": "yann.karpathy@gmail.com",
  "current_job": "Machine Learning Engineer, Hugging Face",
  "education": [
    {
      "year": "2012 - 2018",
      "degree": "Ph.D. in Computer Science",
      "university": "Stanford University"
    },
    {
      "year": "2010 - 2012",
      "degree": "Master of Science in Artificial Intelligence",
      "university": "Massachusetts Institute of Technology"
    },
    {
      "year": "2006 - 2010",
      "degree": "Bachelor of Science in Computer Science",
      "university": "University of Toronto"
    }
  ]
}
```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development paper identifies several key factors that significantly influence the performance of vision-language models:
*   **Quality of Pre-trained Backbones:** The performance of the final VLM is highly dependent on the quality of the initial unimodal vision and language models. The paper found that the quality of the language model backbone has a higher impact than the vision backbone for a fixed parameter count (Paper, p. 3-4).
*   **Model Architecture:** The choice between a fully autoregressive and a cross-attention architecture impacts performance, parameter count, and inference cost. The fully autoregressive architecture was found to outperform the cross-attention one when the backbones are trained (Paper, p. 4).
*   **Number of Visual Tokens:** The number of tokens used to represent an image affects both computational cost and performance. The model uses a perceiver resampler to reduce the number of visual tokens from 729 to 64, which was found to improve performance while increasing efficiency (Paper, p. 5).
*   **Image Resolution and Aspect Ratio:** Handling images at their native resolution and aspect ratio, rather than resizing to a fixed square, preserves visual details crucial for tasks like OCR and improves efficiency (Paper, p. 5).
*   **Image Splitting:** For tasks requiring very high resolution, splitting an image into multiple sub-images (e.g., 4 crops + original) can boost performance at the cost of increased computation (Paper, p. 6).
*   **Training Data Composition:** The mixture of data types used during pre-training (interleaved documents, image-text pairs, PDFs) and instruction-tuning is critical for achieving a broad set of capabilities (Paper, p. 6-7).

### Evaluation factors:
The factors listed above were systematically analyzed and reported during the model's evaluation through a series of ablation studies (Paper, p. 3-6). The final model's performance is reported under different conditions, such as using a standard number of visual tokens (64) versus an increased number via image splitting (320), to demonstrate the trade-off between performance and computational cost (Paper, Table 9, p. 9).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard benchmarks and metrics tailored to different capabilities:
*   **Visual Question Answering (VQA):** VQA accuracy (VQA-acc) on datasets like VQAv2, TextVQA, and OKVQA (Paper, p. 8).
*   **Document Question Answering:** Average Normalized Levenshtein Similarity (ANLS) on DocVQA (Paper, p. 24).
*   **Image Captioning:** CIDEr score on the COCO dataset (Paper, p. 8).
*   **General Multi-modal Reasoning:**
    *   MMMU score for multi-discipline college-level problems on the MMMU benchmark (Paper, p. 9).
    *   Accuracy for various perception and reasoning tasks on the MMBench benchmark (Paper, p. 9).
*   **Mathematical Reasoning:** MMMU score on the MathVista benchmark (Paper, p. 9).

### Decision thresholds:
All evaluations were performed using greedy decoding with a batch size of 1 (Paper, p. 23). For open-ended generation tasks, specific stop words (`Question`, `User`, `<end_of_utterance>`, `<eos>`) were used to terminate the generation (Paper, p. 23).

### Variation approaches:
Performance was measured under different settings to ensure robustness:
*   **Few-shot Evaluation:** The base model was evaluated using 8 random in-context examples (Paper, p. 8).
*   **Zero-shot Evaluation:** The instruction-tuned and chat models were evaluated in a zero-shot setting (Paper, p. 9, 24).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a comprehensive suite of public benchmarks to assess its diverse capabilities:
*   **VQAv2:** For general visual question answering (Paper, p. 3).
*   **TextVQA:** For VQA requiring reading text in images (Paper, p. 3).
*   **OKVQA:** For VQA requiring external knowledge (Paper, p. 3).
*   **COCO Captioning:** For image captioning (Paper, p. 3).
*   **MMMU:** A benchmark for massive multi-discipline multi-modal understanding and reasoning (Paper, p. 8).
*   **MathVista:** For mathematical reasoning in visual contexts (Paper, p. 8).
*   **MMBench:** For evaluating various perception and reasoning abilities (Paper, p. 9).
*   **DocVQA:** For question answering on document images (Paper, p. 24).

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks in the VLM community and collectively cover a wide range of essential multi-modal tasks, from basic perception to complex, college-level reasoning (Paper, p. 3, 8).

### Preprocessing:
The evaluation data undergoes the same preprocessing as the training data. This includes:
*   **Resizing:** Images are resized to have their longest edge be 980 pixels (image_processor_config.json).
*   **Normalization:** Image pixel values are rescaled and normalized with a mean and standard deviation of 0.5 (image_processor_config.json).
*   **Image Splitting:** For certain evaluations, an "image splitting" strategy is applied to enhance performance on high-resolution tasks. A single image is decomposed into the original image plus four crops, which are then fed to the model as a sequence of five images. This increases the number of visual tokens per original image from 64 to 320 (Paper, p. 6, 9).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a diverse mix of publicly available and specially created datasets across three stages.

**1. Pre-training Data:**
*   **OBELICS:** A large-scale, open web dataset of 350 million interleaved image-text documents, containing 115 billion text tokens (Paper, p. 6).
*   **Image-Text Pairs:** A combination of high-quality human-annotated pairs from PMD and web-scale pairs from a filtered version of LAION-COCO with synthetic captions (Paper, p. 7).
*   **Document Data:** 19 million industry documents from OCR-IDL and 18 million pages from PDFA (Paper, p. 7).
*   **Rendered Text:** A dataset of text rendered with various fonts, colors, and backgrounds (Paper, p. 7).

**2. Instruction Fine-tuning Data:**
*   **The Cauldron:** A collection of 50 vision-language datasets created and released by the authors, covering tasks like VQA, captioning, document understanding, chart reasoning, and code generation. A full list is available in the paper's appendix (Paper, p. 8, 21-22).
*   **Text-Only Instructions:** Datasets such as OpenHermes-2.5, LIMA, Dolly, and MetaMathQA were included to improve instruction following and mathematical reasoning (Paper, p. 8, 22).

**3. Chat Fine-tuning Data:**
*   **LLaVA-Conv** and **ShareGPT4V:** Dialogue datasets used to optimize the model for conversational interactions (Paper, p. 9).

### Motivation:
The datasets were chosen to imbue the model with a comprehensive set of skills:
*   **OBELICS** was used to teach the model to handle long, interleaved sequences of images and text, which is crucial for VQA performance (Paper, p. 6).
*   **Image-text pairs** were used to learn the fundamental alignment between visual and textual concepts (Paper, p. 7).
*   **Document and rendered text data** were included specifically to build strong OCR and document understanding capabilities (Paper, p. 7).
*   **The Cauldron** and **text-only instruction data** were used to align the model to follow human instructions across a wide variety of tasks (Paper, p. 8).
*   **Dialogue data** was used to make the model's interactions more natural and "chatty" (Paper, p. 9).

### Preprocessing:
Significant preprocessing and filtering were applied to the training data to ensure quality:
*   **Filtering:** The OBELICS dataset was filtered to remove the 5% of documents with the highest perplexity scores and to exclude content from creators who opted out of data collection (Paper, p. 6). The LAION-COCO dataset was filtered using a NSFW classifier, removing 7% of the samples (Paper, p. 7).
*   **Deduplication:** The instruction-tuning data was deduplicated against the evaluation sets to prevent data contamination and ensure fair evaluation (Paper, p. 8).
*   **Image Augmentation:** During pre-training, images were randomly scaled up to cover a wide distribution of potential image sizes (Paper, p. 7). During instruction-tuning, image resolutions were also randomly scaled up to reduce overfitting (Paper, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative analysis across various factors.
*   **Performance by LM Backbone:** With a cross-attention architecture, switching the language model from LLaMA-1-7B to Mistral-7B improved the average score on 4 benchmarks from 62.5 to 67.6 (Paper, Table 1, p. 3).
*   **Performance by Vision Backbone:** Switching the vision encoder from CLIP-ViT-H to SigLIP-SO400M improved the average score from 57.4 to 60.7 (Paper, Table 2, p. 4).
*   **Performance by Architecture:** With frozen backbones, the cross-attention architecture scored 66.7, while the fully autoregressive architecture scored 60.3. However, when backbones were trained with LoRA, the fully autoregressive architecture scored 69.5, outperforming the cross-attention architecture's 67.3 (Paper, Table 3, p. 4).
*   **Performance by Pooling Strategy:** Using a Perceiver resampler for pooling achieved an average score of 71.7 (with 64 tokens), significantly outperforming a simple linear projection (44.5) (Paper, Table 4, p. 5; Table 11, p. 21).
*   **Performance by Image Splitting:** On the TextVQA benchmark, the model's score increased from 70.4 to 73.0 when using image splitting (320 tokens vs. 64 tokens). On MMBench, the score was stable (76.8 vs. 76.7) (Paper, Table 9, p. 9).

### Intersectional results:
*   **Architecture and Training Method:** The relative performance of the fully autoregressive and cross-attention architectures depends on the training method. Cross-attention is better when backbones are frozen, but fully autoregressive is superior when backbones are fine-tuned with LoRA (Paper, Table 3, p. 4).
*   **OCR Data and Image Resolution:** The benefit of training on OCR data is most apparent at higher image resolutions. On DocVQA, the model trained without OCR data scored 42.9 at 768 resolution. When trained with OCR data at the same resolution, the score increased to 49.9 (Paper, Table 7, p. 7).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model's weights is approximately 33.6 GB (model.safetensors.index.json). Specific RAM/VRAM requirements for loading the model are not provided.

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
Specific hardware details (e.g., GPU type, number of GPUs) are not provided. However, the paper notes that certain methodological choices were made to improve efficiency:
*   Using **LoRA** for fine-tuning reduces the GPU memory cost compared to full fine-tuning (Paper, p. 4).
*   The **aspect-ratio-preserving** image processing strategy saves GPU memory compared to resizing all images to a fixed high resolution (Paper, p. 6).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

A red-teaming exercise was conducted to evaluate the model's propensity to generate inaccurate, biased, or offensive responses (Paper, p. 10, 23).

**Risks and Mitigation:**
*   **Harmful Stereotypes and Bias:** The model may perpetuate harmful stereotypes based on visual cues (e.g., speculating on a person's profession or social status based on their appearance). The developers note that the model would often encourage the user to exercise caution, but that these safeguards can be circumvented through "jailbreak" prompts (Paper, p. 25-26).
*   **Harmful Content Generation:** The model can be prompted to generate content for online harassment or create offensive memes. It can also be used to generate step-by-step guides for harmful activities, such as constructing small-scale explosives or manipulating firearms (Paper, p. 25).
*   **Security Risks:** The model demonstrated the ability to solve distorted-text CAPTCHAs and to develop phishing schemes from screenshots of websites. The paper notes that these security risks are currently limited by the model's occasional inability to read text accurately, but this may change as OCR capabilities improve (Paper, p. 25).
*   **Sensitive Data:** The model was trained on large, web-crawled datasets (OBELICS, LAION), which may contain personal or sensitive information. Mitigation efforts included filtering the data to remove opted-out content and NSFW material (Paper, p. 6-7).

**Affected Groups:**
The potential for perpetuating stereotypes and generating harmful content could negatively impact individuals based on their age, attire, gender, facial expressions, and other visual characteristics (Paper, p. 25).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Evaluation Metric Limitations:** The VQAv2 benchmark metric strongly penalizes answers that are semantically correct but not in the exact format of the ground truth. This means that reported accuracy scores may not fully reflect the model's true capabilities, and score differences between models can be misleading (Paper, p. 23).
*   **Vulnerability to "Jailbreaking":** While the model has safety mechanisms to avoid generating harmful content, these can be bypassed with carefully crafted prompts. The vision modality introduces new avenues for injecting malicious prompts (Paper, p. 26).
*   **Dependence on Backbone Models:** The paper notes that the open-source community currently lacks a large, well-trained vision encoder, which may limit the performance of models like Idefics2 (Paper, p. 4).
*   **Improving OCR Increases Risk:** The security risks associated with the model (e.g., phishing, solving CAPTCHAs) are currently limited by its imperfect OCR capabilities. As these capabilities improve, the risks may become more severe (Paper, p. 25).

### Recommendations:
*   **Exercise Critical Thinking:** Users should apply critical thinking and discretion when engaging with the model's outputs, as it can generate inaccurate or biased content, and its safety features are not foolproof (Paper, p. 26).
*   **Tune Compute for Performance:** Users can make a trade-off between computational cost and performance based on their specific task. For tasks requiring high-resolution detail (like reading text in a document), using the "image splitting" technique (processing an image as 5 sub-images) is recommended for higher accuracy. For less demanding tasks, the standard processing (64 tokens per image) is more efficient (Paper, p. 6, 9).
*   **Use Native Image Resolution:** The model is designed to handle images at various resolutions and aspect ratios. Users should leverage this flexibility to process images as needed, which can save compute and memory compared to resizing everything to a fixed high resolution (Paper, p. 5).