## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh (2405.02246.pdf, page 1). The developers are affiliated with Hugging Face and Sorbonne Université (2405.02246.pdf, page 1).

### Model date:
The paper describing the model was submitted to arXiv on May 3, 2024 (2405.02246.pdf, page 1).

### Model version:
The model is named Idefics2. The paper and associated resources release three versions of the model: a base pre-trained model, an instruction-tuned model, and a chat model (2405.02246.pdf, Abstract, page 1). This model is an evolution of Idefics1, improving upon it by using a fully autoregressive architecture instead of a cross-attention one, among other changes (2405.02246.pdf, pages 3-4).

### Model type:
Idefics2 is an open-source foundational Vision-Language Model (VLM) with 8 billion parameters (2405.02246.pdf, Abstract, page 1).

*   **Architecture:** It has a fully autoregressive architecture that processes sequences of images and texts to generate text outputs (2405.02246.pdf, page 3; assets/Idefics2_flowchart.png). The core components are:
    *   **Vision Encoder:** A pre-trained vision backbone, SigLIP-SO400M, processes images (2405.02246.pdf, page 6).
    *   **Language Model:** A pre-trained large language model, Mistral-7B-v0.1, serves as the text decoder (2405.02246.pdf, page 6).
    *   **Vision-Language Connector:** This connects the vision and language modalities. It includes a modality projection layer and a perceiver resampler to pool visual features into a fixed number of visual tokens (64 in the standard configuration) before they are concatenated with text embeddings and fed to the language model (2405.02246.pdf, page 3, Figure 2).
*   **Model Size:** The model has 8 billion parameters (2405.02246.pdf, Abstract, page 1). The total size of the model weights is approximately 33.6 GB (model.safetensors.index.json.txt).
*   **Context Length:** The tokenizer configuration specifies a `model_max_length` of 1000000000000000019884624838656, but practical context length is determined by the training data, which used sequences up to 2,048 tokens (2405.02246.pdf, page 7; tokenizer_config.json.txt).

### Training details:
The model was trained in multiple stages:

*   **Multi-stage Pre-training:**
    1.  **Stage 1:** The model was trained on a mix of interleaved image-text documents (OBELICS) and image-text pairs (PMD, LAION-COCO). The max image resolution was limited to 384 pixels with a global batch size of 2,048 (2405.02246.pdf, page 7).
    2.  **Stage 2:** PDF documents (OCR-IDL, PDFA, Rendered Text) were introduced, and the max image resolution was increased to 980 pixels. The same global batch size was used, but with gradient accumulation to manage memory costs (2405.02246.pdf, page 7).
*   **Training Algorithm:** The training uses a learning rate of 1e-4 for approximately 2 epochs over the training data (2405.02246.pdf, page 7). To stabilize training and improve performance when unfreezing the pre-trained backbones, Low-Rank Adaptation (LoRA) was used to adapt the parameters of the vision and language models (2405.02246.pdf, page 4).
*   **Instruction Fine-tuning:** After pre-training, the base model was instruction-tuned on a large collection of 50 vision-language datasets and several text-only datasets, collectively named "The Cauldron" (2405.02246.pdf, page 8). This stage used DoRA (a variant of LoRA) and NEFTune (adding noise to embeddings) to lower the risk of overfitting. Images were also randomly scaled up in resolution during this phase (2405.02246.pdf, page 8).
*   **Chat Model Fine-tuning:** To optimize for chat scenarios, the instruction-tuned model was further trained for a few hundred steps on dialogue data from LLaVA-Conv and ShareGPT4V (2405.02246.pdf, page 9).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Paper:** Laurençon, H., Tronchon, L., Cord, M., & Sanh, V. (2024). *What matters when building vision-language models?* arXiv preprint arXiv:2405.02246. The paper details the experiments, architectural choices, data, and training methods that led to the development of Idefics2 (2405.02246.pdf).
*   **Model Repository:** A collection of Idefics2 models and resources is available at Hugging Face: https://huggingface.co/collections/HuggingFaceM4/idefics2-661d1971b7c50831dd3ce0fe (2405.02246.pdf, page 2).

### Citation details:
Insufficient information. The paper does not provide a BibTeX citation. A citation can be constructed as:
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

### License:
Insufficient information.

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Idefics2 is a foundational vision-language model intended for a wide range of multimodal tasks. It takes images and text as input and outputs text (2405.02246.pdf, page 2). Its capabilities include:
*   Answering questions about images, charts, and diagrams (2405.02246.pdf, page 2, Figure 1).
*   Transcribing text from images and scanned documents (2405.02246.pdf, page 2, Figure 3).
*   Describing visual content in detail (2405.02246.pdf, Figure 6, page 25).
*   Performing visual reasoning based on document understanding (2405.02246.pdf, Figure 5, page 24).
*   Counting objects in a picture (2405.02246.pdf, page 2).
*   Converting screenshots of webpages into code (2405.02246.pdf, page 2).

The model can handle an arbitrary sequence of interleaved images and texts (2405.02246.pdf, page 6).

### Primary intended users:
The primary intended users are researchers and developers in the VLM community who can build upon this open-source model for various applications (2405.02246.pdf, page 2).

### Out-of-scope uses:
The model is not intended for applications where high-stakes decisions are made without human oversight, especially given its identified limitations and potential for bias. Red-teaming exercises revealed the model could be prompted to:
*   Perpetuate harmful stereotypes and pass judgments on individuals' professions, social status, or attractiveness based on visual cues (2405.02246.pdf, page 25).
*   Generate content that could promote online harassment or offensive memes (2405.02246.pdf, page 25).
*   Successfully solve CAPTCHAs, which could be misused to bypass security measures (2405.02246.pdf, page 25).
*   Develop phishing schemes from screenshots of websites (2405.02246.pdf, page 25).
*   Provide instructions for creating small-scale explosives or manipulating firearms, posing a significant security risk (2405.02246.pdf, page 25).

---

## How to Use
This section outlines how to use the model. 

The model processes interleaved image and text inputs. The input is formatted as a sequence where images are represented by a special `<image>` token.

**Example 1: Text Transcription** (2405.02246.pdf, Figure 3, page 8)
*   **Input:** An image of a handwritten letter is provided to the model.
*   **Prompt:** `<image>The content of the letter is:\n`
*   **Output:**
    ```
    Dear Craig,
    Actually, I've never been big on letter writing, though it is nice to receive a hand written note from someone. I am afraid that the art of drawing, and the related ability to sketch an idea, are also being lost. But perhaps, as the cliche goes, what goes around comes around.
    Good luck with your project.
    Tom Cianfichi
    ```

**Example 2: Document Information Extraction in JSON format** (2405.02246.pdf, Figure 5, page 24)
*   **Input:** An image of a resume.
*   **Prompt:** `Extract the name, email, current job, and education. Output a JSON format.`
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

**Example 3: Answering questions about a scientific diagram** (2405.02246.pdf, Figure 7, page 25)
*   **Input:** An image of an aquatic food chain diagram.
*   **Prompt:** `What happens to fish if pelicans increase?`
*   **Output:**
    ```
    If pelicans increase, they may consume more fish, which could lead to a decrease in the fish population or an imbalance in the ecosystem. This could potentially affect other species that rely on fish for food, such as seals, dolphins, and humans who fish for consumption.
    ```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper identifies several factors that influence the model's performance:
*   **Backbone Quality:** The quality of the pre-trained unimodal backbones (both language and vision) has a significant impact. Better language models (e.g., Mistral-7B over LLaMA-1-7B) and vision encoders (e.g., SigLIP over CLIP-ViT) lead to better VLM performance (2405.02246.pdf, pages 3-4).
*   **Architecture:** The choice between a fully autoregressive and a cross-attention architecture affects performance, parameter count, and inference cost (2405.02246.pdf, page 4).
*   **Number of Visual Tokens:** The number of visual tokens used to represent an image after pooling affects both computational efficiency and performance. The model's performance does not improve with more than 64 visual tokens (2405.02246.pdf, page 5).
*   **Image Resolution and Aspect Ratio:** Training on fixed-size square images versus preserving the original aspect ratio and resolution can impact performance on tasks requiring detailed visual information, as well as affect GPU memory usage (2405.02246.pdf, page 5).
*   **Training Data:** The type and quality of training data, such as using synthetic captions or including OCR-focused documents, directly influence the model's capabilities (2405.02246.pdf, page 7).

### Evaluation factors:
The evaluation factors analyzed are the same as the relevant factors listed above. The paper presents a series of ablation studies to quantify the impact of each of these factors on downstream benchmark performance (2405.02246.pdf, pages 3-7).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is assessed using a variety of standard metrics depending on the task:
*   **VQA accuracy (VQA acc.):** Used for visual question answering benchmarks like VQAv2, TextVQA, and OKVQA (2405.02246.pdf, Table 8, page 8).
*   **CIDEr:** Used for evaluating image captioning performance on the COCO dataset (2405.02246.pdf, Table 8, page 8).
*   **MMMU score:** A comprehensive score for the MMMU benchmark, which covers multi-discipline college-level problems (2405.02246.pdf, Table 9, page 9).
*   **Accuracy:** Used for the MMBench benchmark (2405.02246.pdf, Table 9, page 9).
*   **Average Normed Levenshtein Similarity (ANLS):** Used for the DocVQA benchmark, which measures OCR performance in documents (2405.02246.pdf, Table 15, page 24).

### Decision thresholds:
The model uses greedy decoding for generating outputs during evaluation, meaning it selects the token with the highest probability at each step (2405.02246.pdf, page 23). No other specific decision thresholds are mentioned.

### Variation approaches:
Performance is evaluated in zero-shot and few-shot settings:
*   **Few-shot:** Ablation studies were conducted using 4-shot performance on a set of 4 benchmarks (VQAv2, TextVQA, OKVQA, COCO) (2405.02246.pdf, page 3).
*   **Zero-shot:** Final evaluations against state-of-the-art models were performed in a zero-shot setting (2405.02246.pdf, page 9).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its diverse capabilities:
*   **General VQA:** VQAv2, OKVQA (2405.02246.pdf, page 3).
*   **OCR-based VQA:** TextVQA, DocVQA (2405.02246.pdf, pages 3, 9).
*   **Image Captioning:** COCO captions (2405.02246.pdf, page 3).
*   **Multi-discipline Reasoning:** MMMU (2405.02246.pdf, page 8).
*   **Mathematical Reasoning:** MathVista (2405.02246.pdf, page 8).
*   **General Perception and Reasoning:** MMBench (2405.02246.pdf, page 9).

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks that measure a wide range of different capabilities, including general visual understanding, OCR, external knowledge, captioning, mathematical reasoning, and multi-discipline college-level problems (2405.02246.pdf, pages 3, 8).

### Preprocessing:
The training data was deduplicated against the evaluation sets to ensure minimal contamination and fair evaluation (2405.02246.pdf, page 8). For some evaluations, an image splitting strategy was used where an image is decomposed into 4 crops plus the original, resulting in 5 total images being fed to the model to boost performance on high-resolution tasks (2405.02246.pdf, page 6).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model underwent a two-phase training process with different data mixtures.

**1. Pre-training Data:**
*   **Interleaved Image-Text Documents:** OBELICS, a web-scale dataset with 115 billion text tokens and 350 million images (2405.02246.pdf, page 6).
*   **Image-Text Pairs:** A combination of high-quality pairs from PMD and web-scale pairs from a filtered version of LAION-COCO (2405.02246.pdf, page 7).
*   **PDF Documents:** 19 million documents from OCR-IDL, 18 million pages from PDFA, and the RenderedText dataset, which contains texts with diverse fonts and colors (2405.02246.pdf, page 7).

**2. Instruction Fine-tuning Data:**
*   **The Cauldron:** A collection of 50 vision-language datasets and several text-only instruction datasets created by the authors. This includes datasets for general VQA, captioning, OCR, document understanding, reasoning, and more. A full list is provided in the paper's appendix (2405.02246.pdf, page 8, Table 14, pages 21-22).
*   **Dialogue Data:** For the chat version, the model was further fine-tuned on LLaVA-Conv and ShareGPT4V (2405.02246.pdf, page 9).

### Motivation:
*   **OBELICS** was chosen to preserve the language model's performance while teaching it to handle long contexts with interleaved images and text (2405.02246.pdf, page 6).
*   **Image-text pairs** were used to learn the fundamental alignment between visual and textual concepts (2405.02246.pdf, page 7).
*   **PDF and Rendered Text datasets** were included specifically to improve the model's OCR and document understanding abilities (2405.02246.pdf, page 7).
*   **The Cauldron** was created to teach the model to follow instructions and perform specific, task-oriented operations (2405.02246.pdf, page 8).
*   **Dialogue datasets** were used to optimize the model for conversational, "chatty" interactions (2405.02246.pdf, page 9).

### Preprocessing:
*   **Filtering:** The OBELICS dataset was filtered to remove newly opted-out content and the 5% of documents with the highest perplexity scores (2405.02246.pdf, page 6). The LAION-COCO dataset was filtered using a NSFW classifier, removing 7% of the samples (2405.02246.pdf, page 7).
*   **Formatting:** All instruction-tuning datasets were formatted into a shared question/answer format. Multiple Q/A pairs for a single image were concatenated into multi-turn conversations (2405.02246.pdf, page 8).
*   **Augmentation/Regularization:** During fine-tuning, noise was added to embeddings (NEFTune), image resolutions were randomly scaled, and multi-turn conversations were shuffled to reduce overfitting (2405.02246.pdf, page 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides several quantitative analyses based on model configuration and training choices:
*   **Language Model Backbone:** Replacing LLaMA-1-7B with Mistral-7B improved the average score on 4 benchmarks from 62.5 to 67.6 (2405.02246.pdf, Table 1, page 3).
*   **Vision Encoder Backbone:** Switching from CLIP-ViT-H to SigLIP-SO400M improved the average score from 57.4 to 60.7 (2405.02246.pdf, Table 2, page 4).
*   **Architecture:** With frozen backbones, the cross-attention architecture scored 66.7, while the fully autoregressive architecture scored 60.3. With LoRA-trained backbones, the fully autoregressive architecture scored 69.5, outperforming the cross-attention architecture's 67.3 (2405.02246.pdf, Table 3, page 4).
*   **Pooling Strategy:** Using a perceiver resampler with 64 visual tokens achieved a score of 71.7, significantly better than a simple linear projection (44.5) or a mapping network (51.8) (2405.02246.pdf, Tables 4 & 11, pages 5, 21).
*   **OCR Data:** Adding OCR documents to the training mix improved DocVQA performance from 42.9 to 49.9 ANLS (2405.02246.pdf, Table 7, page 7).

### Intersectional results:
Insufficient information. The paper does not provide performance results disaggregated across demographic or other intersectional factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information. However, the paper notes that adapting the vision encoder to preserve the original aspect ratio of images allows for saving GPU memory at inference time by not having to resize all images to a fixed high resolution (2405.02246.pdf, page 5).

### Training or Fine-tuning Requirements:
Insufficient information. However, the paper notes that using LoRA for training the unimodal backbones allows for training at "a fraction of the GPU memory cost of full fine-tuning" (2405.02246.pdf, page 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

*   **Sensitive Data:** The developers took steps to filter the training data. A NSFW classifier was used on the LAION-COCO dataset to remove inappropriate content (2405.02246.pdf, page 7). The OBELICS dataset was filtered to exclude content from creators who opted out as of January 2024 (2405.02246.pdf, page 6).
*   **Risks and Mitigation:** A red-teaming exercise was conducted on the chat-optimized model to evaluate its propensity to generate inaccurate, biased, or offensive responses (2405.02246.pdf, page 23). The model was found to be capable of being "jailbroken" to circumvent its safety measures (2405.02246.pdf, page 26).
*   **Potential Harms:** The model may perpetuate harmful stereotypes by making judgments about people's professions, social status, or attractiveness based on visual cues. It can also be prompted to generate content for online harassment or assume emotional states based on appearance (2405.02246.pdf, page 25).
*   **Security Risks:** The model was found to have capabilities that pose security risks, including:
    *   Solving CAPTCHAs with distorted text.
    *   Developing phishing schemes from website screenshots.
    *   Crafting step-by-step guides for constructing small-scale explosives or manipulating firearms (2405.02246.pdf, page 25).
*   **Risk Acknowledgment:** The developers note that while the model often encourages user caution, certain prompts can bypass these safeguards. They highlight that the addition of a vision modality introduces new avenues for malicious prompts and vulnerabilities in language models (2405.02246.pdf, page 26).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Evaluation Metric Sensitivity:** The VQA accuracy metric is noted to be sensitive to the output format. Models that produce more verbose or slightly different phrasing (e.g., "large" instead of "big") are penalized, even if semantically correct. A manual analysis suggests that a 5-point difference on VQAv2 may be barely noticeable in terms of generation quality (2405.02246.pdf, page 23).
*   **Limited Vision Encoders:** The authors acknowledge that the open VLM community lacks a large, well-trained vision encoder, which may limit the potential performance of models like Idefics2 (2405.02246.pdf, page 4).
*   **Security Risk Limitation:** The identified security risks, such as generating guides for explosives, are currently limited by the model's "occasional inability to accurately read text within images." As OCR capabilities improve, these risks may become more severe (2405.02246.pdf, page 25).
*   **Jailbreaking:** The model's safety mechanisms can be circumvented with certain formulations of prompts, a challenge that is becoming more prominent for vision-language models (2405.02246.pdf, page 26).

### Recommendations:
*   Users should exercise "critical thinking and discretion when engaging with the model's outputs," as certain prompts can bypass its cautionary measures and lead to harmful or inaccurate generations (2405.02246.pdf, page 26).
*   The model should not be used for high-stakes decisions without human oversight, given its potential for bias and factual inaccuracies.
*   Users should be aware of the model's capabilities for misuse, such as solving CAPTCHAs or generating phishing content, and implement appropriate safeguards in their applications.