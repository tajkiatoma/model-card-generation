## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, BLOOM, was developed by the BigScience Workshop, a collaborative open research initiative (2211.05100.pdf, p. 1, 6). The project was initiated by Hugging Face and the French NLP community and grew into a broad international collaboration involving over 1,200 registered participants from various fields, including machine learning, linguistics, law, and philosophy (2211.05100.pdf, p. 6). Hundreds of these participants, representing 38 countries, directly contributed to the project's artifacts (2211.05100.pdf, p. 6). The paper lists the major contributors and various working groups that focused on different aspects of the project such as dataset creation, architecture, and evaluation (2211.05100.pdf, p. 1-3).

### Model date:
The development of BLOOM was a year-long project (2211.05100.pdf, p. 6). The final training of the 176B parameter model took approximately 3.5 months on the Jean Zay supercomputer (2211.05100.pdf, p. 18, 43). The associated research paper was first submitted to arXiv in November 2022, with the version provided in the repository dated June 27, 2023 (2211.05100.pdf, p. 1).

### Model version:
The primary model is BLOOM, with 176 billion parameters (2211.05100.pdf, p. 1). The repository also details several smaller versions of the model that were trained:
*   BLOOM-560M
*   BLOOM-1.1B
*   BLOOM-1.7B
*   BLOOM-3B
*   BLOOM-7.1B
(2211.05100.pdf, p. 21, Table 3)

Additionally, finetuned versions of these models were created:
*   **BLOOMZ**: Models that underwent multitask prompted finetuning to improve zero-shot generalization abilities (2211.05100.pdf, p. 14, 33).
*   **SGPT-BLOOM**: Models that underwent contrastive finetuning to produce high-quality text embeddings for tasks like information retrieval and semantic textual similarity (2211.05100.pdf, p. 22).

### Model type:
BLOOM is a large language model (LLM) in the category of text generation (2211.05100.pdf, p. 3).

**Architecture:**
*   It is a decoder-only Transformer language model, trained with a causal language modeling objective (predicting the next token) (2211.05100.pdf, p. 3, 15).
*   It incorporates two main architectural deviations from a standard Transformer:
    1.  **ALiBi (Attention with Linear Biases) Positional Embeddings:** Instead of adding positional embeddings to the word embeddings, ALiBi directly penalizes attention scores based on the distance between keys and queries. This was found to lead to smoother training and better downstream performance (2211.05100.pdf, p. 16).
    2.  **Embedding LayerNorm:** An additional layer normalization is applied immediately after the embedding layer to improve training stability (2211.05100.pdf, p. 16).

**Size and Parameters:**
*   **Parameters:** 176 billion (176,247M) (2211.05100.pdf, p. 21, Table 3).
*   **Layers:** 70 Transformer layers (2211.05100.pdf, p. 21, Table 3).
*   **Hidden Dimension:** 14,336 (2211.05100.pdf, p. 21, Table 3).
*   **Attention Heads:** 112 (2211.05100.pdf, p. 21, Table 3).
*   **Vocabulary Size:** 250,680 (2211.05100.pdf, p. 18, 21).
*   **Context Length:** 2048 tokens (2211.05100.pdf, p. 21, Table 3).
*   **Total Size on Disk:** Approximately 352.5 GB (model.safetensors.index.json.txt, pytorch_model.bin.index.json.txt).

### Training details:
BLOOM was trained using the Megatron-DeepSpeed framework, which enables large-scale distributed training using a combination of data, tensor, and pipeline parallelism (3D parallelism) (2211.05100.pdf, p. 19).

*   **Algorithm:** Autoregressive language modeling on a large multilingual text corpus (2211.05100.pdf, p. 4).
*   **Precision:** The model was trained using `bfloat16` mixed precision to ensure training stability while maintaining high performance (2211.05100.pdf, p. 20).
*   **Optimizer:** Adam optimizer with β1=0.9 and β2=0.95 (2211.05100.pdf, p. 21, Table 3).
*   **Learning Rate:** A cosine learning rate decay schedule was used, with a peak learning rate of 6.0e-5 and a minimum of 6.0e-6 (2211.05100.pdf, p. 21-22, Table 3).
*   **Batch Size:** Global batch size of 2048 sequences (2211.05100.pdf, p. 21, Table 3).
*   **Training Tokens:** The model was trained on 366 billion tokens from the ROOTS corpus (2211.05100.pdf, p. 21, Table 3). This consisted of one epoch over ~341 billion tokens, plus an additional 25 billion tokens of repeated data (2211.05100.pdf, p. 22).
*   **Tokenizer:** A Byte-Pair Encoding (BPE) tokenizer was trained on a subset of the ROOTS corpus. It is a byte-level tokenizer, which prevents unknown tokens and maximizes vocabulary sharing across languages (2211.05100.pdf, p. 18).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   **Title:** BLOOM: A 176B-Parameter Open-Access Multilingual Language Model (2211.05100.pdf).
*   **Summary:** The paper details the entire process of creating BLOOM, from the collaborative BigScience workshop organization, the creation of the ROOTS training dataset, the model's architecture and training, to its evaluation on a wide range of tasks.

The model and its smaller versions are publicly released on the Hugging Face Hub:
*   **Link:** [https://hf.co/bigscience/bloom](https://hf.co/bigscience/bloom) (2211.05100.pdf, p. 3, 24).

### Citation details:
The paper can be cited using the following BibTeX entry:
```bibtex
@article{bigscience2022bloom,
  title={BLOOM: A 176B-Parameter Open-Access Multilingual Language Model},
  author={BigScience Workshop},
  journal={arXiv preprint arXiv:2211.05100},
  year={2022}
}
```
(2211.05100.pdf)

### License:
The BLOOM model is released under a custom **Responsible AI License (RAIL)**. This license is designed to balance open access with responsible use (2211.05100.pdf, p. 24).
*   The license is offered at no charge.
*   It includes 13 behavioral-use restrictions to limit the model's application in potentially harmful use-cases, such as generating misinformation, violating laws, or creating malicious code. These restrictions were based on the BLOOM Model Card and the BigScience ethical charter (2211.05100.pdf, p. 24).
*   The license distinguishes between the "model" (the trained parameters) and the "source code". The source code for BLOOM is available under an Apache 2.0 open source license (2211.05100.pdf, p. 24).

### Contact:
For correspondence and inquiries, the BigScience Workshop can be contacted via email: `bigscience-contact@googlegroups.com` (2211.05100.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BLOOM is a foundational large language model designed for general-purpose text generation and understanding across multiple languages (2211.05100.pdf, p. 3). Its primary intended use is as a base model for researchers and practitioners to explore and build upon for various downstream NLP tasks (2211.05100.pdf, p. 3, 43).

The model is capable of performing tasks based on natural language instructions or a few examples (few-shot/zero-shot learning) (2211.05100.pdf, p. 3). Evaluated capabilities include:
*   **Text Classification:** Tasks like natural language inference and sentiment analysis (e.g., on the SuperGLUE benchmark) (2211.05100.pdf, p. 26).
*   **Machine Translation:** Translating between many of the 46 languages it was trained on (2211.05100.pdf, p. 26, 29).
*   **Text Summarization:** Generating abstractive summaries of text in multiple languages (2211.05100.pdf, p. 26).
*   **Code Generation:** Generating code in several of the 13 programming languages in its training data (2211.05100.pdf, p. 32).

The model takes a text string as input and outputs a text string as a continuation or answer (2211.05100.pdf, p. 4).

### Primary intended users:
The primary intended users are members of the research community, particularly those who were previously excluded from the development of large-scale language models due to resource constraints (2211.05100.pdf, p. 3-4). The project's goal was to "democratize" this technology, making it publicly available for future research and applications (2211.05100.pdf, p. 3).

### Out-of-scope uses:
Any use of the model that violates the 13 behavioral-use restrictions outlined in its Responsible AI License (RAIL) is considered out-of-scope (2211.05100.pdf, p. 24). These restrictions were put in place to prevent "potentially harmful use-cases" (2211.05100.pdf, p. 24). While the full list is in the license, such uses generally include generating malicious content, spreading disinformation, engaging in illegal activities, or infringing on human rights.

---

## How to Use
The paper does not provide direct code snippets for using the model. However, it states that the model is released on the Hugging Face Hub, implying it can be used with the `transformers` library (2211.05100.pdf, p. 3, 24).

The primary way to interact with the model for specific tasks is through **prompting**, where a natural language instruction or example is provided as input to guide the model's output (2211.05100.pdf, p. 5, 25). The paper's appendix provides numerous examples of prompts used for evaluation.

**Example Input-Output Structure (for a classification task):**

A prompt is constructed by filling a template with data. For the WSC (Winograd Schema Challenge) task, a prompt template might be:
`{{ text }} In the previous sentence, can the pronoun "{{ span2_text }}" be replaced with "{{ span1_text }}"? Yes or no?` (2211.05100.pdf, p. 66)

**Sample Input:**
`Passage: I tried to paint a picture of an orchard, with lemons in the lemon trees, but they came out looking more like light bulbs. In the previous sentence, can the pronoun "they" be replaced with "lemon trees"? Yes or no?` (based on 2211.05100.pdf, p. 66)

**Sample Output:**
`No` (based on 2211.05100.pdf, p. 66)

The model's output is generated autoregressively, token by token, continuing from the provided input prompt.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** As a multilingual model, language is the most significant factor. The model was trained on 46 natural and 13 programming languages, and its performance varies across them. Performance is notably weaker on low-resource languages that were under-represented in the training data (e.g., Swahili, Yoruba) (2211.05100.pdf, p. 32).
*   **Prompt Formulation:** The model's performance is highly sensitive to how a task is framed in the input prompt. The evaluation showed that different prompts for the same task can yield significant performance variations (2211.05100.pdf, p. 28-29).
*   **Social Biases:** The model may reflect social biases present in its training data. The paper evaluates for biases related to ethnicity, gender, socioeconomic status, nationality, religion, age, sexual orientation, physical appearance, and disability (2211.05100.pdf, p. 42, Table 14).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Language:** Performance was disaggregated by language for tasks like machine translation, summarization, and probing analysis (2211.05100.pdf, p. 31, 33, 39).
*   **Task:** Performance was measured across a wide variety of NLP tasks, including classification, generation, and code (2211.05100.pdf, Section 4).
*   **Model Size:** Performance was compared across different model sizes (from 560M to 176B parameters) to analyze scaling properties (2211.05100.pdf, p. 28, Figure 8).
*   **Bias Type:** The bias evaluation was disaggregated by nine different categories of social bias (2211.05100.pdf, p. 42, Table 14).
*   **Linguistic Features:** Probing analysis evaluated the model's encoding of 38 different morphosyntactic features (e.g., Tense, Gender, Number) (2211.05100.pdf, p. 37, 39).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The selection of metrics was task-dependent:
*   **Classification (SuperGLUE):** Accuracy (2211.05100.pdf, p. 28).
*   **Machine Translation (WMT, Flores-101, DiaBLa):** BLEU and COMET (2211.05100.pdf, p. 26, 30).
*   **Summarization (WikiLingua):** ROUGE-2, ROUGE-L, and Levenshtein distance (2211.05100.pdf, p. 26).
*   **Code Generation (HumanEval):** pass@k (2211.05100.pdf, p. 32, Table 9).
*   **Bias (CrowS-Pairs):** Prompt accuracy, where a score of 50% indicates no preference for stereotyped statements (2211.05100.pdf, p. 41).
*   **Linguistic Probing:** Weighted F1 score (2211.05100.pdf, p. 38).
*   **Tokenizer Quality:** Fertility (number of subwords created per word) (2211.05100.pdf, p. 17).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robust measurements and account for variability:
*   For classification tasks, performance was evaluated across a random sample of five different prompts for each task to measure sensitivity to prompt wording (2211.05100.pdf, p. 26).
*   For bias evaluation, results were averaged over eight runs (2211.05100.pdf, p. 42, Table 14).
*   For linguistic probing, results were averaged across three runs with different random seeds to account for randomness in classifier initialization (2211.05100.pdf, p. 38).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
A wide range of public datasets were used for evaluation:
*   **SuperGLUE (subset):** English-only classification tasks including Ax-b, Ax-g, BoolQ, CB, WiC, WSC, and RTE (2211.05100.pdf, p. 26).
*   **WMT14:** Machine translation for English-French and English-Hindi (2211.05100.pdf, p. 26).
*   **Flores-101:** A many-to-many multilingual translation dataset covering 101 languages (2211.05100.pdf, p. 26).
*   **DiaBLa:** A bilingual (English-French) dataset of spontaneous written dialogues for contextual machine translation (2211.05100.pdf, p. 26).
*   **WikiLingua:** A multilingual summarization dataset with article-summary pairs in 9 languages (Arabic, English, Spanish, French, Hindi, Indonesian, Portuguese, Vietnamese, Chinese) (2211.05100.pdf, p. 26).
*   **HumanEval:** A benchmark for evaluating code generation from docstrings (2211.05100.pdf, p. 32).
*   **Multilingual CrowS-Pairs:** A dataset for measuring social bias in English and French, consisting of minimal pairs of stereotyped and non-stereotyped sentences (2211.05100.pdf, p. 41).
*   **Universal Dependencies (UD):** A collection of treebanks for 17 languages used for linguistic probing analysis (2211.05100.pdf, p. 37).

### Motivation:
The datasets were chosen to facilitate a comprehensive evaluation of the model's capabilities. English-only datasets like SuperGLUE were included for comparison with prior work (2211.05100.pdf, p. 26). Multilingual datasets like Flores-101, WikiLingua, and the multilingual CrowS-Pairs were specifically chosen to assess BLOOM's core strength as a multilingual model (2211.05100.pdf, p. 26, 41). Datasets like HumanEval and Universal Dependencies were used to test specific capabilities in code and linguistic representation, respectively (2211.05100.pdf, p. 32, 37).

### Preprocessing:
Preprocessing was specific to each evaluation task:
*   **Prompting:** For most tasks, data was formatted into natural language prompts using the `promptsource` library. For classification, the model's prediction was determined by the maximum log-likelihood assigned to a set of candidate label strings (2211.05100.pdf, p. 26).
*   **Tokenization for Generation Metrics:** For machine translation, `sacrebleu`'s default tokenization was used for WMT14 and DiaBLa, while a specific SentencePiece model (`spm-flores-101`) was used for Flores-101 (2211.05100.pdf, p. 26). For summarization, the ROUGE metric was calculated using the SentencePiece tokenizer from the Flores-101 dataset to better handle multilingual text (2211.05100.pdf, p. 26).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
BLOOM was trained on the **ROOTS corpus**, a large, composite multilingual dataset created specifically for this project (2211.05100.pdf, p. 7).
*   **Size:** 1.61 terabytes of text (2211.05100.pdf, p. 7).
*   **Diversity:** The corpus contains text in 46 natural languages and 13 programming languages (2211.05100.pdf, p. 7). A full breakdown of languages and their proportions is available in the paper (2211.05100.pdf, p. 8, Table 1).
*   **Sources:** ROOTS is a composite of 498 datasets from various sources (2211.05100.pdf, p. 7). The main components are:
    1.  **OSCAR:** A web-crawled corpus derived from Common Crawl, making up 38% of ROOTS (2211.05100.pdf, p. 11).
    2.  **Crowdsourced Datasets:** A large collection of new and existing datasets identified and curated by workshop participants and research collectives (e.g., Masader for Arabic) (2211.05100.pdf, p. 11).
    3.  **GitHub Code:** A dataset of code from GitHub, collected via Google's BigQuery (2211.05100.pdf, p. 11).
*   **Availability:** While the full corpus cannot be released due to licensing and privacy constraints, 223 of the 498 components are available for direct access. Resources to visualize and access the data are on the Hugging Face Hub under the "BigScience Data" organization (2211.05100.pdf, p. 10).

### Motivation:
The ROOTS corpus was created to address a key issue in LLM development: the lack of accountability and transparency in dataset curation (2211.05100.pdf, p. 9). The project aimed to move away from purely heuristic-based filtering of web data and instead prioritize human involvement, local language expertise, and thorough documentation. This approach was designed to better account for the needs and rights of data subjects and rights-holders (2211.05100.pdf, p. 9).

### Preprocessing:
The data processing pipeline for ROOTS involved several key steps (2211.05100.pdf, p. 11-13, Figure 2):
1.  **Sourcing:** Data was obtained from all identified sources, which involved downloading, extracting text from various formats (including PDFs), and scraping websites (2211.05100.pdf, p. 11).
2.  **"Quality" Filtering:** A series of filters were applied to remove non-natural language text (e.g., SEO spam, boilerplate). The goal was to retain text "written by humans for humans," with filter parameters and term lists selected by fluent speakers for each language (2211.05100.pdf, p. 12).
3.  **Deduplication:** Near-duplicate documents were removed to improve data diversity (2211.05100.pdf, p. 13).
4.  **Privacy Redaction:** Personal Identifiable Information (PII), such as social security numbers, was redacted from the OSCAR portion of the corpus using regex-based methods (2211.05100.pdf, p. 13).
5.  **No Normalization:** No unicode normalization (e.g., NFKC) was applied to the text in order to create the most general model possible, preserving distinctions like the difference between `2²` and `22` (2211.05100.pdf, p. 18).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides numerous results disaggregated by individual factors:
*   **By Language:**
    *   Machine translation performance (spBLEU) is reported for low-resource, Romance, high-resource, and mid-resource language pairs on the Flores-101 dataset (2211.05100.pdf, p. 31, Table 8).
    *   Summarization performance (ROUGE-2) is shown for 9 different languages on the WikiLingua dataset (2211.05100.pdf, p. 33, Figure 9).
    *   Linguistic probing performance (F1 score) is broken down by 17 languages (2211.05100.pdf, p. 39, Table 12).
*   **By Bias Type:**
    *   Bias evaluation results on CrowS-Pairs are disaggregated into 9 categories: ethnicity/color, gender, socioeconomic status, nationality, religion, age, sexual orientation, physical appearance, and disability for both English and French (2211.05100.pdf, p. 42, Table 14).
*   **By Model Size:**
    *   Performance on SuperGLUE tasks is shown for BLOOM and OPT models of varying sizes, from ~500M to 176B parameters, to illustrate scaling trends (2211.05100.pdf, p. 29, Figure 8).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is approximately 352.5 GB (model.safetensors.index.json.txt). Loading the full 176B parameter model in `bfloat16` would require at least 352 GB of GPU VRAM or CPU RAM.

### Deploying Requirements:
The paper mentions an ongoing exploration of a real-time deployment of the BLOOM API on a Google Cloud Platform (GCP) instance with **16 GPUs** (2211.05100.pdf, p. 23). This suggests that a multi-GPU setup is required for practical deployment.

### Training or Fine-tuning Requirements:
The full BLOOM model was trained on the Jean Zay supercomputer using the following hardware configuration (2211.05100.pdf, p. 18):
*   **Number of Nodes:** 48 nodes (plus 4 spare nodes).
*   **GPUs:** Each node was equipped with 8 NVIDIA A100 80GB GPUs, for a **total of 384 GPUs**.
*   **Interconnect:** Nodes used 4 NVLink interconnects for intra-node communication and 4 Omni-Path 100 Gbps links for inter-node communication.
*   **CPU and RAM:** Each node had 2x AMD EPYC 7543 32-Core CPUs and 512 GB of RAM.
*   **Total Training Time:** The training process took approximately 3.5 months and consumed 1,082,990 compute hours (2211.05100.pdf, p. 18).

---

## Ethical Considerations
The BigScience workshop placed a strong emphasis on ethical considerations throughout the model's development, guided by a collaboratively designed **Ethical Charter** that values inclusivity, diversity, openness, reproducibility, and responsibility (2211.05100.pdf, p. 7).

*   **Sensitive Data:** The training data was sourced from public web data (Common Crawl via OSCAR) and other public datasets. The developers acknowledged the privacy risks associated with web-crawled data and implemented a PII redaction step on the OSCAR portion of the corpus to remove identifiable information like social security numbers (2211.05100.pdf, p. 13).
*   **Risks and Mitigation:**
    *   **Harmful Use:** The developers acknowledged the risk of the model being used for harmful purposes. To mitigate this, the model was released with a **Responsible AI License (RAIL)** that includes 13 behavioral-use restrictions, explicitly forbidding applications such as generating malicious code, promoting hate speech, or creating disinformation (2211.05100.pdf, p. 24).
    *   **Social Bias:** The model was evaluated for social biases across nine categories using the multilingual CrowS-Pairs dataset. While the results suggest a limited overall presence of bias compared to masked language models, statistically significant biases were detected in several categories, including gender, religion, and socioeconomic status (2211.05100.pdf, p. 41-42).
    *   **Environmental Impact:** The carbon footprint of the model's training was estimated using a Life Cycle Assessment approach. The training process emitted an estimated 25 tons of CO2eq, which is significantly less than comparable models like GPT-3 (502 tons) due to the use of more efficient hardware and a low-carbon energy grid (nuclear power in France) (2211.05100.pdf, p. 23, Table 4).
    *   **Resource Concentration:** The project itself was an attempt to mitigate the concentration of power in a few resource-rich organizations by creating a large-scale, open-access model through a broad, international collaboration (2211.05100.pdf, p. 3-4).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Low-Resource Languages:** The model's performance on languages that were under-represented in the training data (e.g., Swahili, Yoruba, with <50k tokens) is very poor. This questions the model's utility on these specific languages despite their inclusion in the training set (2211.05100.pdf, p. 32).
*   **Limitations of Bias Evaluation:** The bias evaluation, while extensive, has limitations. The CrowS-Pairs metric was originally designed for masked language models, not autoregressive models like BLOOM. Furthermore, there is a lack of comprehensive corpora and measures for assessing bias in a multilingual context. The findings are limited to the specific situations, languages (English and French), and biases covered in the dataset (2211.05100.pdf, p. 43).
*   **Prompt Sensitivity:** The model's performance can vary significantly based on the phrasing of the input prompt. The reported evaluation scores are averages over several prompts and may not reflect performance on any single user-designed prompt (2211.05100.pdf, p. 28).
*   **Over-generation in Translation:** In zero-shot machine translation tasks, the model is prone to over-generation (producing excessively long or repetitive text) and sometimes fails to generate text in the correct target language (2211.05100.pdf, p. 29-30).

### Recommendations:
*   Users must adhere to the use restrictions outlined in the **Responsible AI License (RAIL)** to prevent misuse of the model (2211.05100.pdf, p. 24).
*   For better performance on specific tasks, **multitask finetuning** (as demonstrated with BLOOMZ) is highly effective and can significantly improve zero-shot generalization (2211.05100.pdf, p. 33).
*   When using the model for few-shot machine translation, providing an in-context example greatly improves translation quality and reduces issues like over-generation (2211.05100.pdf, p. 30).
*   Further research is needed to evaluate the model's abilities on languages not included in the pretraining corpus, to conduct deeper analysis of its linguistic knowledge, and to develop better methods for multilingual bias assessment (2211.05100.pdf, p. 41).