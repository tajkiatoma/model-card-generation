## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh (paper.pdf, p. 1). The developers are affiliated with Hugging Face and Sorbonne Université (paper.pdf, p. 1).

### Model date:
The associated academic paper is dated May 3, 2024 (paper.pdf, p. 1).

### Model version:
The model is named Idefics2 (paper.pdf, p. 1). The repository is based on `transformers` version 4.39.0.dev0 (`config.json`, `generation_config.json`). The paper discusses three versions of the model: a base version, an instruction-tuned version, and a chat-optimized version (paper.pdf, p. 1).

### Model type:
Idefics2 is an 8 billion parameter open-source vision-language model (VLM) (paper.pdf, p. 1).

**Architecture:**
The model uses a fully autoregressive architecture (`Idefics2ForConditionalGeneration`) that processes sequences of images and texts to generate text outputs (paper.pdf, p. 3; `config.json`). It is composed of three main components (paper.pdf, p. 3; `architecture.png`):
1.  **Vision Encoder:** A vision transformer that processes input images. It is based on the SigLIP-SO400M model (paper.pdf, p. 6). The vision encoder has 27 hidden layers, a hidden size of 1152, and 16 attention heads. It processes images up to a resolution of 980x980 with a patch size of 14 (`config.json`).
2.  **Vision-Language Connector:** This module maps the visual features to the language model's input space. It uses a Perceiver resampler to pool the visual features into a fixed number of tokens (64 by default), followed by a modality projection layer (paper.pdf, p. 3, 5; `config.json`).
3.  **Language Model:** A text decoder that generates the output. It is based on the Mistral-7B-v0.1 model (paper.pdf, p. 6). The text model has a vocabulary size of 32,003 and supports a maximum context length of 32,768 tokens (`config.json`).

**Model Size:**
*   **Parameters:** 8 billion (paper.pdf, p. 1).
*   **Total Size on Disk:** Approximately 33.6 GB (`model.safetensors.index.json`).

### Training details:
The model was trained in a multi-stage process:

1.  **Pre-training:** This phase was decomposed into two stages to maximize compute efficiency (paper.pdf, p. 7).
    *   **Stage 1:** The model was trained with a maximum image resolution of 384 pixels on a mix of interleaved image-text documents (OBELICS dataset) and image-text pairs (PMD, LAION COCO) (paper.pdf, p. 7).
    *   **Stage 2:** The maximum image resolution was increased to 980 pixels, and PDF documents (OCR-IDL, PDFA, RenderedText) were introduced to the training mixture to improve OCR capabilities (paper.pdf, p. 7).
    *   During pre-training, the entire model was trained, using Low-Rank Adaptation (LoRA) for the parameters of the pre-trained backbones to ensure training stability (paper.pdf, p. 4, 7). The learning rate was set to 10⁻⁴ (paper.pdf, p. 7).

2.  **Instruction Fine-tuning:** The base model was instruction-tuned on "The Cauldron," a large collection of 50 vision-language datasets and several text-only instruction datasets (paper.pdf, p. 8). This stage used DoRA (a variant of LoRA) and employed techniques like NEFTune (adding noise to embeddings) and random scaling of image resolution to prevent overfitting (paper.pdf, p. 8).

3.  **Chat Optimization:** The instruction-tuned model was further trained for a few hundred steps on dialogue data (LLaVA-Conv, ShareGPT4V) to improve its performance in conversational scenarios (paper.pdf, p. 9).

### Paper or other resource for more information:
The model is described in the academic paper: "What matters when building vision-language models?" (paper.pdf, p. 1).
*   **Authors:** Hugo Laurençon, Léo Tronchon, Matthieu Cord, Victor Sanh.
*   **arXiv ID:** arXiv:2405.02246v1 [cs.CV] (paper.pdf, p. 1).
The paper provides an in-depth analysis of the design choices, training procedures, and performance of Idefics2.

### Citation details:
```bibtex
@misc{laurençon2024matters,
      title={What matters when building vision-language models?}, 
      author={Hugo Laurençon and Léo Tronchon and Matthieu Cord and Victor Sanh},
      year={2024},
      eprint={2405.02246},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
(paper.pdf, p. 1)

### License:
Insufficient information.

### Contact:
Insufficient information.

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Idefics2 is a foundational vision-language model designed for a wide range of multimodal tasks (paper.pdf, p. 1). Its primary intended uses include:
*   **Visual Question Answering (VQA):** Answering questions based on the content of an image, including those requiring OCR, external knowledge, or reasoning about charts and diagrams (paper.pdf, p. 2, 3).
*   **Text Transcription (OCR):** Extracting and transcribing text from images, scanned documents, and screenshots (paper.pdf, p. 2, 7).
*   **Image Captioning:** Generating descriptive text for images (paper.pdf, p. 3).
*   **Document Understanding:** Analyzing and extracting information from complex documents like PDFs and resumes (paper.pdf, p. 2, 7, 24).
*   **Code Generation from Screenshots:** Converting screenshots of webpages into functional code (paper.pdf, p. 2).

The model takes a sequence of images and text as input and generates a text sequence as output (paper.pdf, p. 2).

### Primary intended users:
The model and its associated training data are released as resources for the VLM community, indicating that the primary intended users are researchers and developers in the field of artificial intelligence (paper.pdf, p. 2).

### Out-of-scope uses:
The model is not designed for and should not be used for applications that can cause harm. The developers identified several potential misuse cases and harmful capabilities during red-teaming exercises (paper.pdf, p. 25):
*   Perpetuating harmful stereotypes or making judgments about individuals based on visual cues (e.g., age, gender, attire).
*   Generating content for online harassment or creating offensive memes.
*   Assuming emotional states or mental conditions from images.
*   Solving CAPTCHAs to bypass security measures.
*   Developing phishing schemes from screenshots of legitimate websites.
*   Generating instructions for creating dangerous items like explosives or for modifying firearms.

---

## How to Use
This section outlines how to use the model.

The model can be used through the Hugging Face `transformers` library. It uses the `Idefics2Processor` for preparing inputs (images and text) and `Idefics2ForConditionalGeneration` for inference (`config.json`, `processor_config.json`).

**Input Format:**
The input is a list of messages, where each message has a `role` (`'User'` or `'Assistant'`) and `content`, which is a list of dictionaries. Each dictionary in the content list can be of type `'text'` or `'image'` (`processor_config.json`).

**Chat Template:**
For conversational use, the inputs should be formatted according to the following Jinja template (`processor_config.json`):
```jinja
{% for message in messages %}{{message['role'].capitalize()}}{% if message['content'][0]['type'] == 'image' %}{{':'}}{% else %}{{': '}}{% endif %}{% for line in message['content'] %}{% if line['type'] == 'text' %}{{line['text']}}{% elif line['type'] == 'image' %}{{ '<image>' }}{% endif %}{% endfor %}<end_of_utterance>
{% endfor %}{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}
```

**Example Usage (Python Pseudocode):**
```python
from transformers import Idefics2ForConditionalGeneration, Idefics2Processor
from PIL import Image
import requests

# Load the model and processor
model = Idefics2ForConditionalGeneration.from_pretrained("HuggingFaceM4/idefics2-8b-chatty")
processor = Idefics2Processor.from_pretrained("HuggingFaceM4/idefics2-8b-chatty")

# Prepare inputs
url = "https://www.ilankelman.org/stopsigns/australia.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
text = "What is written on the sign?"

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": text}
        ]
    }
]

# Process inputs
prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(text=prompt, images=[image], return_tensors="pt")

# Generate output
generated_ids = model.generate(**inputs, max_new_tokens=50)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)
```

**Special Tokens:**
*   `<s>` (id: 1): Beginning of sequence token (`tokenizer.json`).
*   `</s>` (id: 2): End of sequence token (`tokenizer.json`).
*   `<image>` (id: 32001): Placeholder for an image in the text sequence (`special_tokens_map.json`).
*   `<end_of_utterance>` (id: 32002): Token to mark the end of a turn in a conversation (`special_tokens_map.json`).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The development paper identifies several key factors that influence the performance, efficiency, and stability of vision-language models (paper.pdf, p. 2-6):
*   **Backbone Model Quality:** The performance of the underlying pre-trained vision encoder and language model significantly impacts the final VLM's capabilities. Better language models were found to have a higher impact than better vision backbones for a fixed parameter count (paper.pdf, p. 4).
*   **Architecture Choice:** The method used to fuse vision and text modalities (e.g., fully autoregressive vs. cross-attention) has a major effect on performance and the effectiveness of training the backbones (paper.pdf, p. 4).
*   **Number of Visual Tokens:** The quantity of tokens used to represent an image affects computational cost and performance. Using a learned pooling mechanism (Perceiver resampler) to reduce the number of tokens was found to improve both efficiency and downstream task performance (paper.pdf, p. 5).
*   **Image Resolution and Aspect Ratio:** Training on fixed-size square images can be problematic for tasks involving non-square images or requiring high detail. Adapting the model to handle images in their original aspect ratio and at various resolutions is a crucial factor for flexibility and performance (paper.pdf, p. 5).
*   **Image Splitting Strategy:** Decomposing an image into multiple sub-images at inference time can trade higher computational cost for improved performance, especially on tasks requiring high-resolution detail like OCR (paper.pdf, p. 6).

### Evaluation factors:
The model's evaluation reports performance across several of the relevant factors mentioned above:
*   The final model is evaluated with and without the image splitting strategy, corresponding to using 320 or 64 visual tokens per image, respectively. This allows for analyzing the trade-off between compute and performance (paper.pdf, p. 9, Table 9).
*   Ablation studies were conducted to explicitly measure the impact of backbone choice, architecture, pooling strategy, and aspect ratio preservation on a set of downstream benchmarks (paper.pdf, p. 4-5, Tables 2-5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of standard benchmarks and metrics tailored to different capabilities (paper.pdf, p. 8, 9, 24):
*   **VQAv2:** VQA accuracy (VQA acc.) for general visual question answering.
*   **TextVQA:** VQA accuracy (VQA acc.) for visual question answering requiring reading text in images.
*   **OKVQA:** VQA accuracy (VQA acc.) for visual question answering requiring external knowledge.
*   **DocVQA:** Average Normalized Levenshtein Similarity (ANLS) for question answering on document images.
*   **COCO:** CIDEr score for image captioning quality.
*   **MMMU:** MMMU score for massive multi-discipline multimodal understanding and reasoning.
*   **MathVista:** A score derived from MMMU for mathematical reasoning in visual contexts.
*   **MMBench:** Accuracy for comprehensive evaluation of perception and reasoning abilities.
*   **Human Evaluation:** Blind human evaluations were used to compare the chattiness and user preference of the chat-optimized model (paper.pdf, p. 9).

### Decision thresholds:
Insufficient information.

### Variation approaches:
*   For the base model, evaluations on VQA tasks were conducted using 8 random in-context examples in an open-ended setting (paper.pdf, p. 8).
*   For the instruction-tuned and chat models, evaluations were performed in a zero-shot setting (paper.pdf, p. 9).
*   All evaluations were performed with a batch size of 1 and greedy decoding (`paper.pdf`, p. 23).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmarks to assess its capabilities (paper.pdf, p. 3, 8, 9, 24):
*   **General VQA:** VQAv2 (Goyal et al., 2017)
*   **OCR & Text-based VQA:** TextVQA (Singh et al., 2019), DocVQA (Mathew et al., 2021)
*   **Knowledge-based VQA:** OKVQA (Marino et al., 2019)
*   **Image Captioning:** COCO (Lin et al., 2014)
*   **Multidisciplinary Reasoning:** MMMU (Yue et al., 2024)
*   **Mathematical Reasoning:** MathVista (Lu et al., 2024)
*   **General Perception & Reasoning:** MMBench (Liu et al., 2023)

### Motivation:
These datasets were chosen because they are commonly adopted benchmarks in the VLM community (paper.pdf, p. 8). They collectively cover a diverse set of essential multimodal abilities, including general perception, reading comprehension, reasoning, and knowledge integration, providing a comprehensive assessment of the model's performance (paper.pdf, p. 3, 8, 9).

### Preprocessing:
For evaluation, specific prompting strategies were used depending on the task format. For multi-choice questions (MMMU, MathVista, MMBench), a template providing the question and choices was used. For open-ended questions (TextVQA, DocVQA, VQAv2), a simpler prompt asking for a brief answer was used (`paper.pdf`, p. 23). Additionally, an "image splitting" technique was evaluated, where a single image is processed as a sequence of 5 images (the original plus four crops) to provide higher detail at the cost of more computation (paper.pdf, p. 6).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a diverse mix of public and newly created datasets across its different training stages.

*   **Pre-training Data** (paper.pdf, p. 6-7):
    *   **OBELICS:** An open, web-scale dataset of 350 million images and 115 billion text tokens from interleaved image-text documents (Laurençon et al., 2023).
    *   **PMD:** A dataset of high-quality, human-annotated image-text pairs (Singh et al., 2022).
    *   **LAION COCO:** A dataset with synthetic captions generated for images from the LAION dataset (Schuhmann et al., 2022).
    *   **PDF Documents:** A collection including 19 million industry documents from OCR-IDL (Biten et al., 2022), 18 million pages from PDFA, and the RenderedText dataset.

*   **Instruction Fine-tuning Data** (paper.pdf, p. 8):
    *   **The Cauldron:** A massive collection of 50 vision-language datasets covering tasks like VQA, captioning, document understanding, chart reasoning, and code generation. This dataset was created and released alongside the model.
    *   **Text-only Datasets:** Instruction-following datasets like OpenHermes-2.5, LIMA, Dolly, MetaMathQA, and MathInstruct were included to improve reasoning and instruction-following capabilities.
    *   A full list of datasets in The Cauldron is available in Table 14 of the paper (`paper.pdf`, p. 22-23).

*   **Chat Fine-tuning Data** (paper.pdf, p. 9):
    *   **LLaVA-Conv** (Liu et al., 2023) and **ShareGPT4V** (Chen et al., 2023) were used to optimize the model for conversational interactions.

### Motivation:
The choice of datasets was motivated by the goal of creating a robust and general-purpose VLM.
*   Interleaved documents (OBELICS) were used to teach the model to handle long contexts with an arbitrary mix of images and text (paper.pdf, p. 6).
*   Image-text pairs (PMD, LAION) were used to learn the fundamental alignment between visual and textual concepts (paper.pdf, p. 7).
*   PDF and rendered text data were included specifically to build strong OCR and document understanding abilities (paper.pdf, p. 7).
*   The diverse instruction-tuning mixture (The Cauldron) was designed to teach the model to follow complex instructions across a wide variety of multimodal tasks (paper.pdf, p. 8).

### Preprocessing:
*   **Data Filtering:** The training data underwent significant filtering. OBELICS was filtered to remove opted-out content and documents with high perplexity scores (paper.pdf, p. 6). LAION COCO was filtered using a NSFW classifier to remove 7% of the samples (paper.pdf, p. 7).
*   **Image Preprocessing:** During training, images were randomly scaled up to cover a distribution of potential sizes (paper.pdf, p. 7). The image processor resizes images to have a longest edge of 980, rescales pixel values, and normalizes them (`image_processor_config.json`). The model was also adapted to preserve the original aspect ratio of images (paper.pdf, p. 5).
*   **Text Preprocessing:** Text was tokenized using a Llama-style BPE tokenizer (`tokenizer_config.json`, `tokenizer.json`). For instruction tuning, datasets were prompted into a shared question/answer format (paper.pdf, p. 8).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance is reported across numerous individual benchmarks.

**Idefics2-base (8B) Performance** (paper.pdf, p. 8, Table 8):
*   **VQAv2:** 70.3
*   **TextVQA:** 57.9
*   **OKVQA:** 54.6
*   **COCO (CIDEr):** 116.0

**Idefics2 (8B, instruction-tuned) Performance** (paper.pdf, p. 9, Table 9; `paper.pdf`, p. 24, Table 15):
*   **MMMU (val/test):** 43.5 / 37.9
*   **MathVista (testmini):** 51.6
*   **MMBench (test):** 76.8
*   **DocVQA (test, ANLS):** 67.3
*   **VQAv2 (testdev):** 80.8

### Intersectional results:
The paper provides results that analyze performance across the factor of image processing strategy (standard vs. image splitting), which corresponds to the number of visual tokens used per image (64 vs. 320).

**Idefics2 (8B, instruction-tuned) Performance with 64 vs. 320 tokens per image** (paper.pdf, p. 9, Table 9; `paper.pdf`, p. 24, Table 15):
| Metric | 64 tokens/image | 320 tokens/image |
| :--- | :--- | :--- |
| **TextVQA (val)** | 70.4 | 73.0 |
| **MMBench (test)** | 76.8 | 76.7 |
| **DocVQA (test, ANLS)** | 67.3 | 74.0 |
| **VQAv2 (testdev)** | 80.8 | 81.2 |
| **MMMU (val/test)** | 43.5 / 37.9 | 43.0 / 37.7 |
| **MathVista (testmini)** | 51.6 | 51.4 |

These results show that using more tokens via image splitting provides a significant performance boost on tasks that require reading fine-grained text from images (TextVQA, DocVQA), while having a mixed or minor effect on other benchmarks.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights have a total size of approximately 33.6 GB (`model.safetensors.index.json`). The default data type is `float32` (`config.json`), so loading the model in full precision would require at least 34 GB of RAM or VRAM.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

A red-teaming exercise was conducted to evaluate the model's propensity to generate inaccurate, biased, or offensive responses (`paper.pdf`, p. 23).

**Sensitive Data:** The developers took steps to mitigate risks from training data by using a NSFW classifier to filter the LAION COCO dataset and removing newly opted-out content from the OBELICS web dataset (paper.pdf, p. 6, 7).

**Risks and Mitigation:**
The red-teaming analysis identified several potential risks (`paper.pdf`, p. 25):
*   **Perpetuation of Harmful Stereotypes:** The model may make judgments or perpetuate historical disparities regarding individuals' professions, social status, or other characteristics based on visual cues like age, attire, and gender.
*   **Generation of Harmful Content:** The model could be prompted to generate content that promotes online harassment or creates offensive memes from benign images.
*   **Inappropriate Inferences:** The model might assume emotional states or mental conditions based on a person's outward appearance.
*   **Security Vulnerabilities:** The model demonstrated capabilities that pose security risks, including:
    *   Successfully solving distorted text CAPTCHAs.
    *   Assisting in the creation of phishing schemes from screenshots.
    *   Crafting step-by-step guides for constructing small-scale explosives or manipulating firearms. It is noted that this risk is currently limited by the model's occasional inability to read text accurately.

**Mitigation Strategies and Model Behavior:**
The model often attempts to mitigate harm by encouraging user caution or flagging a problematic query. For instance, when insistently prompted to write a racist comment, the model might provide the response but follow it with a statement explaining why the stereotype is harmful and contributes to social injustice (`paper.pdf`, p. 26). However, it is also acknowledged that these safeguards can be circumvented with "jailbreak" prompts, which is an ongoing challenge for vision-language models (`paper.pdf`, p. 26).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Jailbreaking Vulnerability:** The model's safety mechanisms can be bypassed by certain adversarial prompts ("jailbreaks"). The addition of the vision modality introduces new and complex avenues for such attacks that are an active area of research (`paper.pdf`, p. 26).
*   **Evaluation Metric Limitations:** Standard metrics for open-ended VQA (like VQAv2 accuracy) are very strict and penalize answers that are semantically correct but not an exact match to the ground truth (e.g., "large" vs. "big"). This can make it difficult to interpret small differences in scores between models (`paper.pdf`, p. 23).
*   **Chattiness vs. Accuracy Trade-off:** There is a tension between generating conversational, "chatty" responses that humans prefer and producing the short, precise answers required to achieve high scores on academic benchmarks. The chat-optimized version of the model is designed for the former (paper.pdf, p. 9).
*   **Inaccurate Text Reading:** While the model has strong OCR capabilities, it can still occasionally fail to read text within images accurately, which limits some of its harmful capabilities but can also affect performance on benign tasks (`paper.pdf`, p. 25).

### Recommendations:
*   **Exercise Critical Thinking:** Users should use critical thinking and discretion when engaging with the model's outputs, as its safety guardrails are not foolproof (`paper.pdf`, p. 26).
*   **Use Image Splitting for OCR-heavy Tasks:** For tasks that require reading fine-grained text from images (e.g., TextVQA, DocVQA), users should consider using the image splitting strategy (processing an image as 5 separate crops). This increases computational cost but can significantly improve performance (paper.pdf, p. 6, 9).
*   **Choose the Right Model Version:** Users should select the appropriate model version for their needs. The `base` model is suitable for further fine-tuning, while the `chat` model is optimized for direct interaction and conversational tasks (paper.pdf, p. 1).