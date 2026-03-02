## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh (What matters when building vision-language models?.pdf, p. 1). The developers are affiliated with Hugging Face and Sorbonne Université (What matters when building vision-language models?.pdf, p. 1).

### Model date:
The academic paper describing the model was submitted to arXiv on May 3, 2024 (What matters when building vision-language models?.pdf, p. 1). The development process included data filtering and removal of opted-out content in January 2024 (What matters when building vision-language models?.pdf, p. 6).

### Model version:
The model is named Idefics2. It is an 8-billion parameter vision-language model (What matters when building vision-language models?.pdf, p. 1). Idefics2 is a successor to Idefics1 and differs significantly in its architecture. While Idefics1 used a cross-attention architecture to fuse visual and text features, Idefics2 employs a fully autoregressive architecture where image features are concatenated with text embeddings and fed directly to the language model (What matters when building vision-language models?.pdf, p. 3, 4). This change, combined with other improvements, makes Idefics2 more efficient at inference and state-of-the-art in its size category (What matters when building vision-language models?.pdf, p. 1, 6). The model was developed using `transformers` version `4.39.0.dev0` (config.json).

### Model type:
Idefics2 is a multi-modal vision-language model (VLM) of the `idefics2` type, with an `Idefics2ForConditionalGeneration` architecture (config.json). It is designed to take both images and text as input to generate textual outputs (What matters when building vision-language models?.pdf, p. 2).

**Architecture Details:**
The model follows a fully autoregressive architecture, which consists of three main components (What matters when building vision-language models?.pdf, p. 3, 6; Idefics2_...png):
1.  **Vision Encoder**: A pre-trained vision transformer, SigLIP-SO400M, processes input images (What matters when building vision-language models?.pdf, p. 6). The vision model has a hidden size of 1152, 27 hidden layers, and 16 attention heads. It processes images up to a size of 980x980 with a patch size of 14 (config.json).
2.  **Language Model**: A pre-trained large language model decoder, Mistral-7B-v0.1, handles text processing and generation (What matters when building vision-language models?.pdf, p. 6). The text model has a vocabulary size of 32003 and supports a maximum position embedding of 32768 (config.json).
3.  **Connector**: A module that connects the vision and language components. It includes a Perceiver resampler for pooling visual features into a fixed number of tokens (64 by default) and a modality projection layer to map visual features into the language model's embedding space (What matters when building vision-language models?.pdf, p. 3; Idefics2_...png).

**Model Size:**
*   **Parameters**: 8 billion (What matters when building vision-language models?.pdf, p. 1).
*   **Total Size on Disk**: Approximately 33.6 GB (model.safetensors.index.json).

### Training details:
The model was trained in a multi-stage process:

1.  **Multi-stage Pre-training**:
    *   **Stage 1**: The model was trained with a maximum image resolution of 384 pixels and a global batch size of 2,048. The data mixture was 70% interleaved image-text documents (OBELICS) and 30% image-text pairs (PMD, LAION-COCO) (What matters when building vision-language models?.pdf, p. 7).
    *   **Stage 2**: The maximum image resolution was increased to 980 pixels to handle text-rich PDF documents. The data mixture was 45% OBELICS, 35% image-text pairs, and 20% PDF documents (What matters when building vision-language models?.pdf, p. 7).
    *   **Algorithm**: The training used a learning rate of 10⁻⁴ for approximately 2 epochs over the training data, which corresponds to 1.5 billion images and 225 billion text tokens (What matters when building vision-language models?.pdf, p. 7). To stabilize training while adapting pre-trained backbones, Low-Rank Adaptation (LoRA) was used (What matters when building vision-language models?.pdf, p. 4).

2.  **Instruction Fine-tuning**:
    *   The base model was fine-tuned on "The Cauldron," a collection of 50 vision-language datasets and several text-only instruction datasets, formatted into a shared question/answer structure (What matters when building vision-language models?.pdf, p. 8).
    *   **Algorithm**: The fine-tuning was performed using DoRA, a variant of LoRA. To mitigate overfitting, techniques like NEFTune (adding noise to embeddings) and random scaling of image resolutions were employed (What matters when building vision-language models?.pdf, p. 8).

3.  **Chat Fine-tuning**:
    *   To improve performance in conversational scenarios, the instruction-tuned model was further trained for a few hundred steps on dialogue data from LLaVA-Conv and ShareGPT4V (What matters when building vision-language models?.pdf, p. 9).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   Laurençon, H., Tronchon, L., Cord, M., & Sanh, V. (2024). *What matters when building vision-language models?*. arXiv preprint arXiv:2405.02246. (What matters when building vision-language models?.pdf, p. 1).
The paper provides a comprehensive overview of the model's architecture, training experiments, and performance.

Additional resources can be found at the Hugging Face collection for Idefics2:
*   https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe (What matters when building vision-language models?.pdf, p. 2).

### Citation details:
To cite the model, please use the following BibTeX entry based on the associated paper:
```bibtex
@misc{laurençon2024idefics2,
      title={What matters when building vision-language models?}, 
      author={Hugo Laurençon and Léo Tronchon and Matthieu Cord and Victor Sanh},
      year={2024},
      eprint={2405.02246},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(Source: What matters when building vision-language models?.pdf, p. 1)

### License:
Insufficient information

### Contact:
Insufficient information

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Idefics2 is a foundational vision-language model (VLM) designed for a wide range of multi-modal tasks that require understanding both images and text (What matters when building vision-language models?.pdf, p. 1, 2). Its primary capabilities include:
*   **Visual Question Answering (VQA)**: Answering questions based on the content of an image, including general VQA, OCR-based VQA, and knowledge-based VQA (What matters when building vision-language models?.pdf, p. 3, 6).
*   **Text Transcription**: Extracting and transcribing text from images, scanned documents, and screenshots (What matters when building vision-language models?.pdf, p. 2, 8).
*   **Document and Chart Understanding**: Analyzing and answering questions about charts, diagrams, tables, and PDF documents (What matters when building vision-language models?.pdf, p. 1, 2).
*   **Image Captioning**: Generating descriptive text for images (What matters when building vision-language models?.pdf, p. 3).
*   **Code Generation**: Converting screenshots of webpages into functional code (What matters when building vision-language models?.pdf, p. 2).
*   **Visual Reasoning**: Performing tasks that require logical or mathematical reasoning based on visual inputs (What matters when building vision-language models?.pdf, p. 1, 8).

The model takes a sequence of images and/or text as input and generates a textual response (What matters when building vision-language models?.pdf, p. 2).

### Primary intended users:
The primary intended users are researchers and developers in the field of artificial intelligence and machine learning, particularly those working on vision-language models (What matters when building vision-language models?.pdf, p. 2). The release of the model and its training data is intended to support the VLM community (What matters when building vision-language models?.pdf, p. 2).

### Out-of-scope uses:
The model is not designed or intended for applications that could cause harm. A red-teaming exercise identified several potential misuse cases and out-of-scope applications where the model might produce problematic outputs. Users should refrain from using the model for such purposes (What matters when building vision-language models?.pdf, p. 25, 26):
*   **Perpetuating Harmful Stereotypes**: The model may speculate on individuals' professions, social status, or other attributes based on visual cues, potentially reinforcing historical disparities and stereotypes.
*   **Online Harassment**: Generating content that promotes harassment or creating offensive memes from images.
*   **Making Unfounded Assumptions**: Assuming emotional states, mental conditions, or attractiveness based solely on visual appearance.
*   **Security Risks**:
    *   Solving CAPTCHAs with distorted text.
    *   Developing phishing schemes from website screenshots.
    *   Generating step-by-step guides for creating explosives or manipulating firearms.
The paper notes that these security risks are currently limited by the model's "occasional inability to accurately read text within images" (What matters when building vision-language models?.pdf, p. 25).

---

## How to Use
This section outlines how to use the model.

While no direct code snippets are provided in the repository, the model's usage can be inferred from its configuration files. Idefics2 is a multi-modal model that processes interleaved sequences of text and images.

**Input-Output Structure:**
*   **Input**: A sequence of text and images. In a conversational context, inputs are formatted with roles (e.g., "User:", "Assistant:"). Images are represented by the special token `<image>` in the text sequence (processor_config.json).
*   **Output**: A generated text sequence that completes the input prompt.

**Chat Template:**
The model uses a specific chat template to format conversational inputs. Each message in a conversation is structured with a role (`User` or `Assistant`) followed by its content, which can be a mix of text and images. Each turn is terminated by the `<end_of_utterance>` token (processor_config.json).

A formatted conversation would look like this:
```
User: <image> What is happening in this image?<end_of_utterance>
Assistant: This is an image of a cat sitting on a mat.<end_of_utterance>
User: What color is the cat?<end_of_utterance>
Assistant:
```
The model would then generate the text to complete the "Assistant:" turn.

**Special Tokens:**
The following special tokens are used to structure the input:
*   `<s>`: Beginning of sequence token (tokenizer.json).
*   `</s>`: End of sequence token (tokenizer.json).
*   `<image>`: Placeholder for an image in the text sequence (special_tokens_map.json).
*   `<end_of_utterance>`: Marks the end of a turn in a conversation (special_tokens_map.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development paper identifies several key factors that influence the model's performance (What matters when building vision-language models?.pdf, Section 3):
*   **Quality of Pre-trained Backbones**: The performance of the underlying unimodal vision and language models has a significant impact. The paper found that the quality of the language model backbone has a higher impact than the quality of the vision backbone for a fixed parameter count (What matters when building vision-language models?.pdf, p. 4).
*   **Model Architecture**: The choice between a fully autoregressive architecture and a cross-attention architecture affects performance, parameter count, and inference cost. The fully autoregressive architecture was found to be superior when unimodal backbones are trained (What matters when building vision-language models?.pdf, p. 4).
*   **Training Method**: Whether the pre-trained backbones are kept frozen or fine-tuned (e.g., using LoRA) during training significantly impacts performance and stability. Unfreezing the backbones with LoRA was found to improve performance (What matters when building vision-language models?.pdf, p. 4).
*   **Number of Visual Tokens**: The quantity of visual tokens used to represent an image affects both computational efficiency and performance. The paper found that using a Perceiver resampler to reduce visual tokens to 64 significantly improves efficiency and downstream performance (What matters when building vision-language models?.pdf, p. 5).
*   **Image Resolution and Aspect Ratio**: The resolution and aspect ratio of input images are crucial, especially for tasks involving text recognition. The model was adapted to handle images in their original aspect ratio and at various resolutions to improve flexibility and performance (What matters when building vision-language models?.pdf, p. 5).
*   **Image Splitting**: The strategy of splitting an image into sub-images during training and inference can trade compute efficiency for higher performance, particularly on OCR-heavy tasks (What matters when building vision-language models?.pdf, p. 6).

### Evaluation factors:
The evaluation factors analyzed in the paper are the same as the relevant factors listed above. The paper presents a series of ablation studies to systematically measure the impact of each of these factors on model performance across a set of standard benchmarks (What matters when building vision-language models?.pdf, Section 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of standard metrics tailored to different downstream tasks (What matters when building vision-language models?.pdf, p. 3, 8, 9):
*   **VQA accuracy (VQA acc.)**: Used for visual question answering benchmarks like VQAv2, TextVQA, and OKVQA. This metric measures the accuracy of the model's generated answers compared to ground-truth answers.
*   **CIDEr**: Used for the COCO captioning benchmark to evaluate the quality of generated image descriptions.
*   **MMMU score**: A specific metric for the MMMU benchmark, which covers multi-discipline college-level problems.
*   **ANLS (Average Normalized Levenshtein Similarity)**: Used for the DocVQA benchmark to evaluate performance on document-based question answering.
*   **Accuracy**: Used for the MMBench benchmark.

The selection of these metrics is justified by their common use in the VLM literature for evaluating specific capabilities such as general VQA, OCR, and reasoning (What matters when building vision-language models?.pdf, p. 3, 9).

### Decision thresholds:
The model uses greedy decoding for evaluations, meaning it selects the token with the highest probability at each step of the generation process (What matters when building vision-language models?.pdf, p. 23). No other specific decision thresholds are mentioned.

### Variation approaches:
Performance metrics are reported based on standard evaluation protocols for each benchmark.
*   Ablation studies were conducted by training for 6,000 steps and reporting the average score of 4-shot performance on four benchmarks (VQAv2, TextVQA, OKVQA, COCO) (What matters when building vision-language models?.pdf, p. 3).
*   Final model evaluations were performed in a zero-shot setting (What matters when building vision-language models?.pdf, p. 9, 24).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its diverse capabilities.
*   **Ablation Studies**: VQAv2, TextVQA, OKVQA, and COCO (What matters when building vision-language models?.pdf, p. 3).
*   **Final Evaluation**: The final evaluation included the above datasets as well as MMMU, MathVista, MMBench, and DocVQA (What matters when building vision-language models?.pdf, p. 8, 9, 24).

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks in the VLM community and cover a wide spectrum of tasks and capabilities (What matters when building vision-language models?.pdf, p. 3, 8):
*   **VQAv2, OKVQA**: For general and knowledge-based visual question answering.
*   **TextVQA, DocVQA**: For tasks requiring OCR and reading text in images/documents.
*   **COCO**: For image captioning.
*   **MMMU, MathVista**: For complex multi-discipline and mathematical reasoning in visual contexts.
*   **MMBench**: For various perception and reasoning tasks.

### Preprocessing:
During evaluation, two main strategies for image preprocessing are used, depending on the number of visual tokens specified (What matters when building vision-language models?.pdf, p. 6, 9):
1.  **Standard Inference (64 tokens)**: Images are processed as standalone inputs, preserving their original aspect ratio.
2.  **Image Splitting (320 tokens)**: For tasks requiring higher resolution (like OCR), each image is split into 4 crops, which are processed along with the original image, forming a sequence of 5 images.

The model was evaluated in a zero-shot setting for the final results (What matters when building vision-language models?.pdf, p. 9).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained in multiple stages using a diverse collection of public and newly created datasets.

**1. Pre-training Data:**
*   **OBELICS**: An open, web-scale dataset of 350 million interleaved image-text documents, totaling 115 billion text tokens (What matters when building vision-language models?.pdf, p. 6).
*   **Image-Text Pairs**: A combination of high-quality pairs from PMD and web-scale pairs from the synthetic captions subset of LAION-COCO (What matters when building vision-language models?.pdf, p. 7).
*   **PDF Documents**: 19 million documents from OCR-IDL and 18 million pages from PDFA (What matters when building vision-language models?.pdf, p. 7).
*   **Rendered Text**: A synthetic dataset of texts written with a wide variety of fonts, colors, and backgrounds (What matters when building vision-language models?.pdf, p. 7).

**2. Instruction Fine-tuning Data ("The Cauldron"):**
*   A massive collection of 50 vision-language datasets covering tasks like VQA, captioning, OCR, and reasoning. A full list is provided in the paper's appendix (Table 14) (What matters when building vision-language models?.pdf, p. 8, 22, 23).
*   Text-only instruction datasets including OpenHermes-2.5, LIMA, Dolly, MetaMathQA, and MathInstruct (What matters when building vision-language models?.pdf, p. 8, 23).

**3. Chat Fine-tuning Data:**
*   Dialogue datasets including LLaVA-Conv and ShareGPT4V (What matters when building vision-language models?.pdf, p. 9).

### Motivation:
The choice of datasets was motivated by the goal of creating a versatile and robust VLM:
*   **OBELICS** was used to teach the model to handle long contexts with arbitrarily interleaved images and text (What matters when building vision-language models?.pdf, p. 6).
*   **Image-text pairs** were used to learn the fundamental alignment between visual and textual concepts (What matters when building vision-language models?.pdf, p. 7).
*   **PDF and Rendered Text datasets** were included to significantly boost the model's OCR and document understanding abilities (What matters when building vision-language models?.pdf, p. 7).
*   **The Cauldron** and text-only instruction datasets were used to align the model to follow task-oriented instructions and perform complex reasoning (What matters when building vision-language models?.pdf, p. 8).
*   **Dialogue datasets** were used to improve the model's performance in conversational chat scenarios (What matters when building vision-language models?.pdf, p. 9).

### Preprocessing:
Several preprocessing steps were applied to the training data:
*   **Data Filtering**: The OBELICS dataset was filtered to remove newly opted-out content and the 5% of documents with the highest perplexity scores. The LAION-COCO dataset was filtered to remove 7% of samples identified as NSFW by a classifier (What matters when building vision-language models?.pdf, p. 6, 7).
*   **Image Processing**: Images were randomly scaled up during pre-training to cover a distribution of sizes. For instruction tuning, an image splitting strategy (4 crops + original image) was applied to 50% of the samples to improve performance on OCR-heavy tasks (What matters when building vision-language models?.pdf, p. 6, 7). The image processor configuration specifies steps for resizing, rescaling, and normalizing images (preprocessor_config.json).
*   **Text Formatting**: All instruction datasets were prompted into a shared question/answer format. For multi-turn examples, the user/assistant turns were randomly shuffled to prevent overfitting (What matters when building vision-language models?.pdf, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by individual benchmarks, which represent different tasks and capabilities. The tables below summarize the model's performance on key benchmarks.

**Idefics2-base (8B parameters, 64 visual tokens) on 4-shot tasks:**
| Benchmark | Metric | Score |
| :--- | :--- | :--- |
| VQAv2 | VQA acc. | 70.3 |
| TextVQA | VQA acc. | 57.9 |
| OKVQA | VQA acc. | 54.6 |
| COCO | CIDEr | 116.0 |
(Source: What matters when building vision-language models?.pdf, p. 8, Table 8)

**Idefics2 (instruction-tuned, 8B parameters) on zero-shot tasks:**
| Model Variant | MMMU | MathVista | TextVQA | MMBench | DocVQA | VQAv2 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Idefics2 (64 tokens) | 43.5/37.9 | 51.6 | 70.4 | 76.8 | 67.3 | 80.8 |
| Idefics2 (320 tokens) | 43.0/37.7 | 51.4 | 73.0 | 76.7 | 74.0 | 81.2 |
(Source: What matters when building vision-language models?.pdf, p. 9, Table 9; p. 24, Table 15)

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space**: The model weights require approximately 33.6 GB of disk space (model.safetensors.index.json).
*   **RAM/VRAM**: As an 8-billion parameter model, loading and running inference will require a significant amount of VRAM, likely in the range of 16-24 GB for quantized versions and more for full precision. The paper notes that the fully autoregressive architecture and learned pooling make Idefics2 more computationally efficient at inference compared to similar models (What matters when building vision-language models?.pdf, p. 4, 6).

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper notes that using Low-Rank Adaptation (LoRA) "allows training the unimodal backbones at a fraction of the GPU memory cost of full fine-tuning" (What matters when building vision-language models?.pdf, p. 4). Pre-training was conducted with a large global batch size of 2,048, implying a multi-GPU setup, but specific hardware details are not provided (What matters when building vision-language models?.pdf, p. 7).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

**Sensitive Data Usage:**
The model was trained on large-scale, web-crawled datasets (OBELICS, LAION), which may contain personal or sensitive information. The developers took steps to mitigate this by:
1.  Filtering the LAION-COCO dataset using a high-recall NSFW classifier, removing 7% of the samples (What matters when building vision-language models?.pdf, p. 7).
2.  Filtering the OBELICS dataset to exclude content from creators who opted out as of September 2023, with an additional removal of newly opted-out content in January 2024 using the Spawning API (What matters when building vision-language models?.pdf, p. 6).

**Risks and Mitigation:**
A red-teaming exercise was conducted to evaluate the model's propensity to generate inaccurate, biased, or offensive responses. The key risks identified are (What matters when building vision-language models?.pdf, p. 25, 26):
*   **Perpetuation of Harmful Stereotypes**: The model can make judgments about individuals' professions, social status, or emotional states based on visual cues like age, attire, and gender, which can reinforce harmful stereotypes.
*   **Generation of Harmful Content**: The model can be prompted to generate content for online harassment or create offensive memes.
*   **Security Vulnerabilities**:
    *   The model can successfully solve distorted-text CAPTCHAs.
    *   It can be used to develop phishing schemes from website screenshots.
    *   It can generate step-by-step guides for constructing small-scale explosives or manipulating firearms.

**Mitigation Efforts:**
*   The developers note that the chat-optimized model often encourages user caution or flags problematic queries. For instance, when prompted for a racist comment, it may provide the answer but follow up with a disclaimer about the harm of stereotyping (What matters when building vision-language models?.pdf, p. 26).
*   However, it is acknowledged that these cautionary prompts can be circumvented ("jailbroken") with certain formulations, highlighting the need for user discretion (What matters when building vision-language models?.pdf, p. 26).
*   The security risks are noted to be currently limited by the model's "occasional inability to accurately read text within images" (What matters when building vision-language models?.pdf, p. 25).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Jailbreaking**: The model's safety mechanisms can be circumvented by certain prompt formulations, leading to the generation of harmful or problematic content (What matters when building vision-language models?.pdf, p. 26).
*   **Security Risks**: The model's ability to read distorted text and understand visual layouts poses security risks, such as solving CAPTCHAs and aiding in the creation of phishing schemes (What matters when building vision-language models?.pdf, p. 25).
*   **Stereotyping and Bias**: The model can perpetuate harmful stereotypes by making judgments based on visual cues in images of people (What matters when building vision-language models?.pdf, p. 25).
*   **Evaluation Metric Limitations**: The performance on benchmarks like VQAv2 is measured by VQA accuracy, which strongly penalizes answers that are semantically correct but not in the exact format of the ground truth. This can make performance differences appear larger than they are in qualitative human evaluation (What matters when building vision-language models?.pdf, p. 23).
*   **Vision Encoder Limitations**: The paper notes that the open VLM community lacks a large, well-trained vision encoder, which may limit the potential performance of models like Idefics2 (What matters when building vision-language models?.pdf, p. 4).

### Recommendations:
*   Users should exercise "critical thinking and discretion when engaging with the model's outputs," as safety prompts can be bypassed (What matters when building vision-language models?.pdf, p. 26).
*   The model should not be used for applications that require making judgments about individuals, especially in sensitive domains like insurance eligibility or professional evaluation, as it may perpetuate biases (What matters when building vision-language models?.pdf, p. 25).
*   Given the identified security risks, the model should not be deployed in applications where its ability to solve CAPTCHAs or generate malicious content could be exploited.