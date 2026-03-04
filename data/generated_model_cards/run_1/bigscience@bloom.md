## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the BigScience Workshop, an open research collaboration involving over 1,200 registered participants from diverse backgrounds, including machine learning, computer science, linguistics, and law (2211.05100.pdf, p. 6). The project was initiated by a concerted effort from Hugging Face and the French NLP community and grew into a broad international collaboration (2211.05100.pdf, p. 6). Hundreds of individuals from 38 countries directly contributed to the project's artifacts (2211.05100.pdf, p. 6). A full list of contributors is available in the associated paper (2211.05100.pdf, p. 1-3).

### Model date:
The training of the final BLOOM model took approximately 3.5 months (2211.05100.pdf, p. 18, 43). The associated research paper was submitted to arXiv and the latest version (v4) is dated June 27, 2023 (2211.05100.pdf, p. 1).

### Model version:
The primary model is BLOOM, a 176 billion parameter model (config.json.txt; 2211.05100.pdf, p. 3). The project also trained five smaller size variants: BLOOM-560M, BLOOM-1.1B, BLOOM-1.7B, BLOOM-3B, and BLOOM-7.1B (2211.05100.pdf, p. 21, Table 3). Additionally, multitask finetuned versions, referred to as BLOOMZ, were created (2211.05100.pdf, p. 14). The model was developed using version 4.21.0 of the Transformers library (config.json.txt).

### Model type:
BLOOM is a large language model for causal language modeling (config.json.txt). It is a decoder-only Transformer model (2211.05100.pdf, p. 3).

**Architecture Details:**
*   **Parameters:** 176 billion (176,247M) (2211.05100.pdf, p. 21, Table 3).
*   **Layers:** 70 Transformer layers (config.json.txt; 2211.05100.pdf, p. 21, Table 3).
*   **Attention Heads:** 112 (config.json.txt; 2211.05100.pdf, p. 21, Table 3).
*   **Hidden Dimension:** 14336 (config.json.txt; 2211.05100.pdf, p. 21, Table 3).
*   **Vocabulary Size:** 250,880 (config.json.txt; 2211.05100.pdf, p. 21, Table 3).
*   **Sequence Length:** 2048 tokens (2211.05100.pdf, p. 21, Table 3).
*   **Positional Embeddings:** It uses ALiBi (Attention with Linear Biases) positional embeddings, which directly attenuate attention scores based on the distance between keys and queries, instead of adding positional information to the embedding layer. This was found to lead to smoother training and better downstream performance (2211.05100.pdf, p. 16).
*   **Layer Normalization:** An additional layer normalization is applied immediately after the embedding layer to improve training stability (2211.05100.pdf, p. 16).
*   **Activation Function:** GELU (2211.05100.pdf, p. 21, Table 3).

**Model Size:**
*   The total size of the model weights on disk is 352,494,542,848 bytes (approximately 352.5 GB) (model.safetensors.index.json.txt; pytorch_model.bin.index.json.txt).

### Training details:
The model was trained using a causal, autoregressive language modeling objective (2211.05100.pdf, p. 4, 15). The training was performed using the Megatron-DeepSpeed framework, which enables large-scale distributed training through a combination of data parallelism, tensor parallelism, and pipeline parallelism (3D parallelism) (2211.05100.pdf, p. 19).

**Key Parameters and Hyperparameters:**
*   **Precision:** `bfloat16` mixed precision (2211.05100.pdf, p. 20, 21).
*   **Optimizer:** Adam with β1=0.9 and β2=0.95 (2211.05100.pdf, p. 21, Table 3).
*   **Learning Rate:** 6e-5, with a cosine decay schedule and warmup for 375 million tokens (2211.05100.pdf, p. 21, Table 3).
*   **Global Batch Size:** 2048 (2211.05100.pdf, p. 21, Table 3).
*   **Total Tokens Trained:** 366 billion tokens (2211.05100.pdf, p. 21, Table 3).
*   **Dropout:** No dropout was used (hidden_dropout: 0.0, attention_dropout: 0.0) (config.json.txt; 2211.05100.pdf, p. 22).
*   **Gradient Clipping:** 1.0 (2211.05100.pdf, p. 21, Table 3).
*   **Weight Decay:** 0.1 (2211.05100.pdf, p. 21, Table 3).

The training process utilized fused CUDA kernels to optimize GPU computations by minimizing data transfers between VRAM and registers (2211.05100.pdf, p. 20).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   **Title:** BLOOM: A 176B-Parameter Open-Access Multilingual Language Model
*   **Authors:** BigScience Workshop
*   **Source:** 2211.05100.pdf
This paper provides a comprehensive overview of the model's development, including the creation of its training dataset, the design of its architecture and tokenizer, evaluation results, and ethical considerations (2211.05100.pdf, p. 43).

### Citation details:
```bibtex
@article{bigscience2022bloom,
  title={BLOOM: A 176B-Parameter Open-Access Multilingual Language Model},
  author={BigScience Workshop},
  journal={arXiv preprint arXiv:2211.05100},
  year={2022}
}
```
(Source: Derived from 2211.05100.pdf)

### License:
The BLOOM model is released under a custom "Responsible AI License (RAIL)". This license separates the "source code" from the "model" and includes behavioral-use clauses to limit the model's application in potentially harmful use-cases. The license contains 13 behavioral-use restrictions based on the model's intended uses and the BigScience ethical charter. The model is offered at no charge, and users are free to use it as long as they comply with the usage restrictions (2211.05100.pdf, p. 24). The source code for BLOOM is available under an Apache 2.0 open source license (2211.05100.pdf, p. 24).

### Contact:
For correspondence, questions, or feedback, contact the BigScience Workshop at: `bigscience-contact@googlegroups.com` (2211.05100.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BLOOM is a general-purpose, open-access, multilingual language model designed to perform new tasks based on a few demonstrations (few-shot) or natural language instructions (zero-shot) (2211.05100.pdf, p. 3). It is a causal language model that generates text by predicting the next token in a sequence (2211.05100.pdf, p. 4, 15). Its capabilities span 46 natural languages and 13 programming languages (2211.05100.pdf, p. 3). It can be used for a range of tasks, including text generation, summarization, machine translation, and code generation, without requiring task-specific finetuning (2211.05100.pdf, p. 24). The model takes a text prompt as input and outputs a generated text continuation.

### Primary intended users:
The model was created to "democratize this powerful technology" and make it publicly available, particularly for the research community that has often been excluded from the development of large language models (2211.05100.pdf, p. 3, 4). The intended users are researchers, developers, and the general public who wish to build applications or conduct research using a large-scale multilingual language model (2211.05100.pdf, p. 3).

### Out-of-scope uses:
The model is not intended for any use that violates the 13 behavioral-use restrictions outlined in its Responsible AI License (RAIL). These restrictions are designed to prevent "potentially harmful use-cases" (2211.05100.pdf, p. 24). The specific restrictions are detailed in the license itself, which is linked from the model's documentation (2211.05100.pdf, p. 24).

---

## How to Use
Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model is multilingual, trained on 46 natural and 13 programming languages. Its performance varies significantly across these languages, particularly between high-resource and low-resource languages present in the training data (2211.05100.pdf, p. 7, 32).
*   **Prompting:** As a model intended for few-shot and zero-shot use, its performance is highly dependent on the natural language prompt provided to it. The paper shows that different prompts for the same task can lead to significant performance variations (2211.05100.pdf, p. 25, 28).
*   **Task Domain:** The model's performance is evaluated across various domains, including general language understanding (SuperGLUE), machine translation (WMT, Flores-101), summarization (WikiLingua), and code generation (HumanEval) (2211.05100.pdf, p. 24).

### Evaluation factors:
The model evaluation systematically analyzes performance based on the following factors:
*   **Language:** Performance is disaggregated by language in tasks like machine translation and summarization (2211.05100.pdf, p. 31, 33).
*   **Prompt Variation:** For each task, performance is evaluated across a set of different prompts to simulate realistic use and measure robustness (2211.05100.pdf, p. 25).
*   **Few-shot vs. Zero-shot:** Performance is compared between zero-shot (no examples in the prompt) and one-shot (one example in the prompt) settings (2211.05100.pdf, p. 28).
*   **Model Scale:** Performance is compared across the different size variants of BLOOM (e.g., 560M to 176B parameters) (2211.05100.pdf, p. 28).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The selection of metrics is task-dependent:
*   **Classification (SuperGLUE):** Accuracy, measured by choosing the candidate label with the maximum log-likelihood (2211.05100.pdf, p. 26).
*   **Machine Translation (WMT, Flores-101, DiaBLa):** BLEU and COMET scores (2211.05100.pdf, p. 26, 30).
*   **Summarization (WikiLingua):** ROUGE-2, ROUGE-L, and Levenshtein distance (2211.05100.pdf, p. 26).
*   **Code Generation (HumanEval):** pass@k (2211.05100.pdf, p. 32, 34).
*   **Social Bias (CrowS-Pairs):** Prompt accuracy, where a score of 50% suggests an absence of bias in preferring stereotyped statements (2211.05100.pdf, p. 41).

### Decision thresholds:
For classification tasks, the model's prediction is determined by the maximum log-likelihood among a set of pre-defined candidate label strings associated with the prompt (2211.05100.pdf, p. 26). No specific numerical thresholds are mentioned.

### Variation approaches:
To ensure robust measurements and account for prompt sensitivity, evaluations are conducted using a random sample of five different prompts for each task. The paper reports performance across these prompts to show variability (2211.05100.pdf, p. 26, 28). For bias evaluation, results are averaged over eight runs (2211.05100.pdf, p. 42).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of datasets to test its capabilities in different settings:
*   **SuperGLUE (subset):** For English-only classification tasks, including Ax-b, Ax-g, BoolQ, CB, WiC, WSC, and RTE (2211.05100.pdf, p. 26).
*   **WMT14:** For machine translation between English-French and English-Hindi (2211.05100.pdf, p. 26).
*   **Flores-101:** A multilingual machine translation benchmark used to test many language directions, including low-resource and high-resource pairs (2211.05100.pdf, p. 26, 31).
*   **DiaBLa:** A parallel dataset of informal bilingual dialogues (English-French) used to test translation in a conversational context (2211.05100.pdf, p. 26, 30).
*   **WikiLingua:** A multilingual summarization dataset used to test abstractive summarization in nine languages (2211.05100.pdf, p. 26).
*   **HumanEval:** A benchmark for evaluating code generation capabilities from docstrings (2211.05100.pdf, p. 32).
*   **Multilingual CrowS-Pairs:** A dataset used to measure social biases in English and French by comparing model preferences for stereotyped vs. non-stereotyped sentences (2211.05100.pdf, p. 41).

### Motivation:
The datasets were chosen to provide an accurate picture of how BLOOM compares to other large language models in realistic zero-shot and few-shot settings (2211.05100.pdf, p. 24). The selection covers a diverse range of tasks (classification, translation, summarization, code generation), languages, and evaluation goals (e.g., bias assessment) to comprehensively benchmark the model's abilities (2211.05100.pdf, p. 24).

### Preprocessing:
For evaluation, prompts were generated using the `promptsource` library (2211.05100.pdf, p. 25). These prompts were developed by human contributors prior to the model's release to simulate realistic user interaction without *a priori* refinement (2211.05100.pdf, p. 25). For generation tasks like machine translation and summarization, greedy decoding was used. The maximum generation length was set per dataset (e.g., 64 tokens for WMT14, 512 for Flores-101) to align with standard practices (2211.05100.pdf, p. 26).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
BLOOM was trained on the **ROOTS corpus**, a composite collection of 498 datasets amounting to 1.61 terabytes of text (2211.05100.pdf, p. 7). The corpus is multilingual, spanning 46 natural languages and 13 programming languages (2211.05100.pdf, p. 7).

**Composition of ROOTS:**
*   **OSCAR:** 38% of the corpus is from OSCAR version 21.09, which is derived from Common Crawl web data (2211.05100.pdf, p. 11).
*   **Crowdsourced Datasets:** A large portion was curated by workshop participants who compiled the "BigScience Catalogue," a list of sources covering a wide range of languages. This included 252 sources identified through a bottom-up approach (2211.05100.pdf, p. 11).
*   **GitHub Code:** A dataset of programming languages was collected from GitHub via Google's BigQuery (2211.05100.pdf, p. 11).
The full linguistic makeup of the corpus is detailed in Table 1 of the paper (2211.05100.pdf, p. 8).

### Motivation:
The ROOTS corpus was created to address the disconnect between model developers and data subjects often seen in large-scale data curation. The project prioritized human involvement, local expertise, and language-specific knowledge over purely heuristic-based filtering of web data. This was done to better account for the needs and rights of data subjects and to create a more transparent and well-documented training corpus (2211.05100.pdf, p. 9).

### Preprocessing:
The data processing pipeline for the ROOTS corpus involved several key steps (2211.05100.pdf, p. 11-13):
1.  **Data Sourcing:** Data was obtained from various sources, including web crawls, NLP datasets, and code repositories (2211.05100.pdf, p. 11).
2.  **"Quality" Filtering:** A set of quality indicators were used to filter for text "written by humans for humans." These indicators and their thresholds were selected individually for each language by fluent speakers to filter out non-natural language like SEO spam or preprocessing errors (2211.05100.pdf, p. 12).
3.  **Deduplication:** Near-duplicate documents were removed using two deduplication steps (2211.05100.pdf, p. 13).
4.  **Privacy Redaction:** Personal Identifiable Information (PII), such as social security numbers, was redacted from the OSCAR portion of the corpus using regex-based methods (2211.05100.pdf, p. 13).
5.  **Tokenization:** A custom Byte-Pair Encoding (BPE) tokenizer with a vocabulary of 250,680 was trained on a subset of the ROOTS data. No text normalization (like NFKC) was performed to keep the model as general as possible (2211.05100.pdf, p. 17-18).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results disaggregated by several individual factors:
*   **By Language:** Machine translation results on the Flores-101 dataset are broken down by language pairs, including low-resource, Romance, and high-resource categories (2211.05100.pdf, p. 31, Table 8). Summarization results on WikiLingua are also shown per language (2211.05100.pdf, p. 33, Figure 9).
*   **By Bias Type:** Results on the CrowS-Pairs dataset are disaggregated by bias categories such as gender, religion, socioeconomic status, and nationality for both English and French (2211.05100.pdf, p. 42, Table 14).
*   **By Model Size:** Performance on SuperGLUE tasks is shown for BLOOM models of different sizes (from 560M to 176B parameters) and compared against OPT models of similar scales (2211.05100.pdf, p. 29, Figure 8).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** The model weights require approximately 352.5 GB of disk storage (model.safetensors.index.json.txt; pytorch_model.bin.index.json.txt).
*   **RAM/VRAM:** To load the model, a minimum of ~353 GB of RAM or VRAM is required if using `bfloat16` precision. If using `float32` precision, this requirement doubles to ~705 GB.

### Deploying Requirements:
For real-time deployment, the paper mentions an API instance running on a Google Cloud Platform (GCP) instance with 16 GPUs (2211.05100.pdf, p. 23). The exact GPU specifications for this deployment are not detailed, but this suggests that a multi-GPU setup is necessary for practical inference.

### Training or Fine-tuning Requirements:
The model was trained on the Jean Zay supercomputer using the following hardware configuration (2211.05100.pdf, p. 18):
*   **Nodes:** 48 nodes (plus 4 spare nodes).
*   **GPUs:** Each node contained 8 NVIDIA A100 80GB GPUs, for a total of 384 GPUs used for training.
*   **CPU:** Each node was equipped with 2x AMD EPYC 7543 32-Core CPUs.
*   **System RAM:** 512 GB of RAM per node.
*   **Interconnect:** 4 NVLink GPU-to-GPU interconnects per node and 4 Omni-Path 100 Gbps links per node for inter-node communication.
The total training process consumed 1,082,990 compute hours over 3.5 months (2211.05100.pdf, p. 18).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The BigScience workshop established an Ethical Charter to guide the project, emphasizing values of inclusivity, diversity, openness, reproducibility, and responsibility (2211.05100.pdf, p. 7).

**Sensitive Data:** The training data was sourced from public web crawls and other datasets, which may contain personal or sensitive information. To mitigate this, Personal Identifiable Information (PII) was redacted from the OSCAR portion of the corpus, which was identified as having the highest privacy risk (2211.05100.pdf, p. 13).

**Risks and Mitigation:**
*   **Harmful Use-Cases:** The developers acknowledge the risk of the model being used for potentially harmful applications. To mitigate this, the model is released under a Responsible AI License (RAIL) which includes 13 behavioral-use restrictions to limit such applications (2211.05100.pdf, p. 24).
*   **Social Bias:** The model was evaluated for social biases using the multilingual CrowS-Pairs dataset for English and French. The results suggest an overall absence of bias in the tested scenarios, with performance close to the 50% neutral baseline. However, some bias categories showed statistically significant (though small) deviations from this baseline (2211.05100.pdf, p. 41-42). The paper acknowledges that this evaluation is limited and cannot cover all possible scenarios or languages (2211.05100.pdf, p. 43).
*   **Environmental Impact:** The carbon footprint of training was a key consideration. The training was conducted on the Jean Zay supercomputer, which is powered by France's low-carbon nuclear energy grid. The total emissions from training were estimated to be 25 tons of CO2eq, significantly less than comparable models like GPT-3 (502 tons) and Gopher (352 tons) (2211.05100.pdf, p. 23, Table 4).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Low-Resource Languages:** The model's performance is poor on some under-represented languages in the training data. For example, translation quality for Swahili and Yoruba, which had very few tokens in the ROOTS corpus, is significantly lower than for high-resource languages (2211.05100.pdf, p. 32).
*   **Limitations of Bias Evaluation:** The bias assessment is limited to the scenarios, languages (English and French), and language variations covered by the CrowS-Pairs dataset. The authors note that very little material is available for comprehensive multilingual bias assessment, and the findings may not generalize to wider model use or other languages (2211.05100.pdf, p. 43).
*   **Prompt Sensitivity:** The model's performance in zero-shot and few-shot settings is sensitive to the phrasing of the prompt. While average performance may be modest on some tasks, specific prompts can elicit much stronger results (2211.05100.pdf, p. 28).
*   **Over-generation in Translation:** In zero-shot machine translation, the model is prone to over-generation (producing text beyond the correct translation) and sometimes fails to produce output in the correct target language. These issues are significantly improved in a one-shot setting (2211.05100.pdf, p. 29-30).

### Recommendations:
*   **Responsible Use:** Users must adhere to the terms of the Responsible AI License (RAIL), which prohibits use in 13 specified harmful application areas (2211.05100.pdf, p. 24).
*   **Use Few-Shot Prompting:** For many tasks, particularly machine translation, providing one or more examples in the prompt (one-shot or few-shot learning) significantly improves performance and reliability compared to zero-shot prompting (2211.05100.pdf, p. 28, 30).
*   **Further Testing:** The paper notes that further research is needed to evaluate the model's multilingual abilities on languages not included in the pretraining corpus and to conduct a deeper analysis of its performance on under-resourced languages (2211.05100.pdf, p. 41). Users working with languages that were under-represented in the training data should perform extensive testing before deployment.