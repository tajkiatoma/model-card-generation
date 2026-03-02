## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, BLOOM (BigScience Large Open-science Open-access Multilingual Language Model), was developed by the BigScience Workshop (Paper, p. 1). BigScience is an open research collaboration that was coordinated by over 1,200 registered participants with the goal of the public release of a large language model (LLM) (Paper, p. 6).

The project was initiated by a compute grant from GENCI on the Jean Zay supercomputer at IDRIS/CNRS. It began with a concerted effort from Hugging Face and the French NLP community and expanded into a broad international collaboration to support linguistic, geographical, and scientific diversity. The participants came from various fields, including machine learning, computer science, linguistics, statistics, socio-cultural anthropology, philosophy, and law, representing 38 countries (Paper, p. 6). The project was organized into 30 working groups, each focusing on a specific aspect of the model's development, such as data, modeling, evaluation, and ethical considerations (Paper, p. 6-7).

A list of major contributors and participants in various roles (Dataset, Tokenization, Architecture, etc.) is provided in the accompanying paper (Paper, pp. 1-3).

### Model date:
The development of BLOOM was a collaborative effort that took place over an extended period. The project started after a compute grant was awarded by GENCI (Paper, p. 6). The final training of the 176B parameter model took approximately 3.5 months to complete (Paper, p. 18, 43). The associated research paper is dated June 27, 2023 (Paper, p. 1).

### Model version:
The primary model is BLOOM, a 176-billion parameter model (Paper, p. 3). The repository also details five smaller pretrained variants with the same architecture: BLOOM-560M, BLOOM-1.1B, BLOOM-1.7B, BLOOM-3B, and BLOOM-7.1B (Paper, p. 21, Table 3).

Additionally, the paper describes finetuned versions of these models:
*   **BLOOMZ**: Models that underwent multitask prompted finetuning to improve zero-shot task generalization abilities across multiple languages (Paper, p. 14, 22).
*   **SGPT-BLOOM**: Models that underwent contrastive finetuning to produce high-quality text embeddings for tasks like multilingual information retrieval and semantic textual similarity (Paper, p. 22).

The model was developed using `transformers` version 4.21.0 (config.json).

### Model type:
BLOOM is a large language model (LLM) for text generation, specifically a decoder-only Transformer architecture trained for causal language modeling (Paper, p. 3, 15).

**Architecture Details:**
*   **Model Type:** `bloom` (config.json).
*   **Architecture Class:** `BloomForCausalLM` (config.json).
*   **Parameters:** 176 billion (Paper, p. 3).
*   **Layers:** 70 transformer layers (`n_layer`, config.json).
*   **Hidden Size:** 14336 (`n_embed`, config.json).
*   **Attention Heads:** 112 (`num_attention_heads`, config.json).
*   **Vocabulary Size:** 250,880 (`vocab_size`, config.json).
*   **Sequence Length:** 2048 (Paper, p. 21, Table 3).
*   **Positional Embeddings:** It uses ALiBi (Attention with Linear Biases) positional embeddings, which directly attenuate attention scores based on the distance between keys and queries, instead of adding positional information to the embeddings. This was found to lead to smoother training and better downstream performance (Paper, p. 16).
*   **Layer Normalization:** An additional LayerNorm is applied immediately after the embedding layer to improve training stability (Paper, p. 16).

### Training details:
The model was pretrained using an autoregressive language modeling objective (Paper, p. 4). The training was performed using the Megatron-DeepSpeed framework, which enables large-scale distributed training through a combination of data parallelism, tensor parallelism, and pipeline parallelism (3D parallelism) (Paper, p. 19).

**Key Parameters and Hyperparameters (for 176B model):**
*   **Precision:** `bfloat16` mixed precision (Paper, p. 21, Table 3).
*   **Optimizer:** ZeRO (Zero Redundancy Optimizer) stage 1 (Paper, p. 20) with Adam parameters β1=0.9 and β2=0.95 (Paper, p. 21, Table 3).
*   **Global Batch Size:** 2048 (Paper, p. 21, Table 3).
*   **Learning Rate:** A cosine decay schedule was used with a peak learning rate of 6e-5, warming up for 375 million tokens and decaying to a minimum of 6e-6 (Paper, p. 21, Table 3).
*   **Total Tokens Trained:** 366 billion tokens (Paper, p. 21, Table 3).
*   **Regularization:** Weight decay of 0.1 and gradient clipping at 1.0 were used. No dropout was applied (`hidden_dropout`: 0.0, `attention_dropout`: 0.0, config.json; Paper, p. 22).

**Hardware and Duration:**
*   **Hardware:** Trained on the Jean Zay supercomputer, using 48 nodes, each with 8 NVIDIA A100 80GB GPUs (a total of 384 GPUs) (Paper, p. 18).
*   **Duration:** Training took approximately 3.5 months and consumed 1,082,990 compute hours (Paper, p. 18).

### Paper or other resource for more information:
The primary resource is the academic paper describing the model's development and evaluation:
*   **Paper:** BigScience Workshop. (2023). *BLOOM: A 176B-Parameter Open-Access Multilingual Language Model*. arXiv:2211.05100v4 [cs.CL].
*   **Model Hub:** The model and its variants are publicly released on the Hugging Face Hub: [https://hf.co/bigscience/bloom](https://hf.co/bigscience/bloom) (Paper, p. 3, footnote 1).

### Citation details:
Insufficient information. A BibTeX entry is not provided in the repository.

### License:
The BLOOM model is released under a custom **Responsible AI License (RAIL)**. This license aims to balance open access with responsible use by including behavioral-use clauses that restrict potentially harmful applications of the model. The license distinguishes between the "source code" and the "model" (trained parameters) (Paper, p. 24).
*   **Model:** The model is offered at no charge, and users are free to use it as long as they comply with the terms, which include 13 behavioral-use restrictions based on the model's intended uses and the BigScience ethical charter (Paper, p. 24).
*   **Source Code:** The source code for BLOOM is available under an Apache 2.0 open-source license (Paper, p. 24).

More information on RAIL licenses can be found at licenses.ai (Paper, p. 24, footnote 27).

### Contact:
For correspondence, questions, or feedback, contact the BigScience Workshop at: **bigscience-contact@googlegroups.com** (Paper, p. 1, footnote *).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BLOOM is a general-purpose, open-access, multilingual language model designed to perform a variety of natural language tasks. Its primary function is to generate text from a prompt (causal language modeling) (Paper, p. 3, 15). It was created to "democratize" access to powerful large language models for the research community and facilitate future research and applications (Paper, p. 3).

The model is capable of performing new tasks based on a few demonstrations (few-shot) or natural language instructions (zero-shot) (Paper, p. 3). It is inherently multilingual, having been trained on text from 46 natural languages and 13 programming languages (Paper, p. 3).

Examples of demonstrated capabilities include:
*   **Text Classification:** Tasks like natural language inference and sentiment analysis (e.g., on the SuperGLUE benchmark) (Paper, p. 26).
*   **Machine Translation:** Translating between various languages, including those in the training data and related languages (Paper, p. 26, 32).
*   **Summarization:** Performing abstractive summarization in multiple languages (e.g., on the WikiLingua dataset) (Paper, p. 26).
*   **Code Generation:** Generating code snippets (e.g., evaluated on the HumanEval benchmark) (Paper, p. 32).

The model takes text as input and generates text as output.

### Primary intended users:
The primary intended users are researchers and developers in the machine learning and natural language processing communities (Paper, p. 3, 4). The project's goal was to make a powerful LLM publicly available to a community that was previously excluded from their development due to high computational costs (Paper, p. 4).

### Out-of-scope uses:
The model is not intended for any use that violates the terms of its Responsible AI License (RAIL). The license includes 13 behavioral-use restrictions designed to prevent "potentially harmful use-cases" (Paper, p. 24). While the specific restrictions are not enumerated in the provided paper, they are based on the limitations described in the model card and the BigScience ethical charter. Any application that aims to generate harmful, unethical, or illegal content is out-of-scope.

---

## How to Use
Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** As a multilingual model, language is a primary factor. The model was trained on 46 natural and 13 programming languages, and its performance varies significantly across them, particularly between high-resource and low-resource languages (Paper, p. 3, 32).
*   **Linguistic Properties:** The model's ability to capture morphosyntactic features varies by language family and script (e.g., Latin vs. Devanagari, Tamil, Arabic) (Paper, p. 38, 40).
*   **Demographic and Social Factors:** The model's behavior may be influenced by social biases present in the training data. The paper evaluates for biases related to ethnicity, color, gender, socioeconomic status, nationality, religion, age, sexual orientation, physical appearance, and disability (Paper, p. 42, Table 14).

### Evaluation factors:
The model's performance was evaluated across the following factors:
*   **Language:** Performance was disaggregated by language for tasks like machine translation, summarization, and linguistic probing (Paper, p. 31, 33, 39).
*   **Bias Type:** Performance was analyzed across nine distinct categories of social bias for English and French using the CrowS-Pairs dataset (Paper, p. 42, Table 14).
*   **Language Family and Script:** Statistical tests were conducted to analyze correlations between probing performance and language family/script (Paper, p. 38, 40).
*   **Model Size:** Performance was compared across the six different sizes of BLOOM models (560M to 176B) to analyze scaling properties (Paper, p. 29, Figure 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics were used to assess the model's performance on various tasks:
*   **Classification (SuperGLUE):** Accuracy (Paper, p. 28, Figure 7).
*   **Machine Translation (WMT, Flores-101, DiaBLa):** BLEU and COMET (Paper, p. 26, 30). spBLEU was used for Flores-101 (Paper, p. 31, Table 8).
*   **Summarization (WikiLingua):** ROUGE-2, ROUGE-L, and Levenshtein distance. ROUGE-2 F-measure scores are reported (Paper, p. 26, 33).
*   **Code Generation (HumanEval):** pass@k (Paper, p. 34, Table 9).
*   **Bias (CrowS-Pairs):** Accuracy, representing the model's preference for stereotyped vs. non-stereotyped statements (Paper, p. 41).
*   **Linguistic Probing:** Weighted F1 score, used due to target class imbalance (Paper, p. 38).
*   **Sentence Embeddings (MTEB):** Accuracy for classification tasks and Spearman correlation for semantic textual similarity (STS) tasks (Paper, p. 37, Table 10).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robustness of measurements:
*   For prompt-based evaluations, a random sample of five prompts was used for each task, and performance was evaluated across this set (Paper, p. 26).
*   For bias evaluation on CrowS-Pairs, results were averaged over eight runs (Paper, p. 42, Table 14).
*   For linguistic probing experiments, results were averaged across three runs with different random seeds (Paper, p. 38).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
A wide range of datasets were used for evaluation, detailed in Section 4.1.3 of the paper (Paper, p. 26):
*   **SuperGLUE:** A subset of the English-only benchmark, including Ax-b, Ax-g, BoolQ, CB, WiC, WSC, and RTE (Paper, p. 26).
*   **WMT14:** For machine translation between English↔French and English↔Hindi (Paper, p. 26).
*   **Flores-101:** A multilingual benchmark for low-resource and multilingual machine translation (Paper, p. 26).
*   **DiaBLa:** A corpus of bilingual (English-French) spontaneous written dialogues for machine translation (Paper, p. 26).
*   **WikiLingua:** A multilingual summarization dataset with article-summary pairs in 9 languages (Arabic, English, Spanish, French, Hindi, Indonesian, Portuguese, Vietnamese, Chinese) (Paper, p. 26).
*   **HumanEval:** A benchmark for evaluating code generation capabilities (Paper, p. 32).
*   **Multilingual CrowS-Pairs:** A dataset for measuring social biases in English and French, adapted from the original CrowS-Pairs and extended with French examples (Paper, p. 41).
*   **Universal Dependencies (UD):** Treebanks for 17 languages were used for multilingual linguistic probing (Paper, p. 37).
*   **Massive Text Embedding Benchmark (MTEB):** Includes datasets like MASSIVE (multilingual NLU) and STS22 (semantic textual similarity) for evaluating sentence embeddings (Paper, p. 35, 37).

### Motivation:
The evaluation datasets were chosen to provide an accurate and realistic picture of BLOOM's capabilities in zero-shot and few-shot settings, which reflect common practical use cases for models of this scale (Paper, p. 24). English-only datasets like SuperGLUE were included to facilitate comparison with prior work. Multilingual datasets like WikiLingua and Flores-101 were chosen specifically to test the model's inherent multilingual abilities, a core design goal of the project (Paper, p. 26).

### Preprocessing:
*   **Generation Tasks (MT, Summarization):** Greedy decoding was used. The maximum generation length was set per dataset (64 for WMT14, 512 for Flores-101) (Paper, p. 26).
*   **MT Tokenization:** The `sacrebleu` library's default tokenization was used for WMT and DiaBLa, while `spm-flores-101` was used for Flores-101 (Paper, p. 26).
*   **Summarization Tokenization:** For calculating ROUGE, a SentencePiece tokenizer built from the Flores-101 dataset was used to better measure the fidelity of multilingual generations (Paper, p. 26).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
BLOOM was trained on the **ROOTS corpus**, a composite collection of 498 datasets amounting to 1.61 TB of text (Paper, p. 7).
*   **Languages:** The corpus spans 46 natural languages and 13 programming languages (Paper, p. 7). A full list of languages and their respective sizes in the corpus is available in Table 1 of the paper (Paper, p. 8).
*   **Composition:** The corpus was compiled from several sources (Paper, p. 11):
    *   **OSCAR:** Version 21.09 (from the February 2021 Common Crawl snapshot), constituting 38% of the corpus.
    *   **BigScience Catalogue:** A large list of processed and non-processed sources curated by workshop participants and research collectives.
    *   **GitHub Code:** A dataset of programming languages collected from Google's BigQuery.
*   **Public Availability:** The ROOTS corpus is hosted on the Hugging Face Hub under the "BigScience Data" organization. While 223 of the 498 source components are available for direct access, full access to the entire corpus is gated and requires an application from researchers with a relevant project (Paper, p. 10).

### Motivation:
The choice of training data was motivated by the BigScience Ethical Charter, which prioritizes "human involvement, local expertise, and language expertise" (Paper, p. 9). This was a deliberate move away from common heuristic-based filtering of large web-crawled corpora, which can compound biases and lead to negative outcomes for marginalized populations. The goal was to create a diverse, multilingual dataset with better documentation and governance standards (Paper, p. 9).

### Preprocessing:
The data processing pipeline for the ROOTS corpus involved several steps (Paper, p. 11-13; Figure 2):
*   **Source Aggregation:** Data was obtained from various sources, including downloading NLP datasets, scraping PDF archives, and extracting text from web crawls (Paper, p. 11).
*   **"Quality" Filtering:** A set of quality indicators were defined to filter out non-natural language (e.g., SEO pages, spam). The filtering process was guided by fluent speakers for each language, who adjusted parameters and selected appropriate indicators for each source (Paper, p. 12). The definition of quality was "written by humans for humans," without judgment of content or grammaticality (Paper, p. 12).
*   **Deduplication:** Near-duplicate documents were removed in two steps (Paper, p. 13). Duplicated lines were also removed from the data used to train the tokenizer (Paper, p. 17).
*   **Privacy Redaction:** Personal Identifiable Information (PII) was redacted from the OSCAR portion of the corpus using regex-based methods (Paper, p. 13).
*   **Normalization:** No unicode normalization was applied to the text to ensure the model remained as general as possible (Paper, p. 18).
*   **Pre-tokenization:** A custom regex was used to split text by whitespaces and punctuation while preserving all characters, including sequences of spaces and line breaks, which are important for programming languages (Paper, p. 18).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results disaggregated by several individual factors:
*   **By Language:**
    *   Machine translation performance (spBLEU) on the Flores-101 devtest set is broken down by low-resource, Romance, high-resource, and high-to-mid-resource language pairs (Paper, p. 31, Table 8).
    *   One-shot summarization performance (ROUGE-2 F-measure) is shown for 9 different languages (Paper, p. 33, Figure 9).
    *   Linguistic probing performance (F1 score) is presented for 17 different languages (Paper, p. 39, Figure 12).
*   **By Bias Type:**
    *   Accuracy on the CrowS-Pairs dataset is disaggregated into 9 bias categories (e.g., gender, religion, age) for both English and French (Paper, p. 42, Table 14).
*   **By Model Size:**
    *   Performance on SuperGLUE tasks is plotted against model size (from 350M to 176B parameters) for both BLOOM and OPT model families (Paper, p. 29, Figure 8).
    *   Code generation performance (pass@k) on HumanEval is reported for all six BLOOM model sizes (Paper, p. 34, Table 9).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model's weights is approximately 352.5 GB (`total_size` in model.safetensors.index.json and pytorch_model.bin.index.json). Loading this model requires substantial hardware, likely multiple high-VRAM GPUs or a large amount of CPU RAM, though specific minimum requirements are not provided.

### Deploying Requirements:
The paper provides an example of a real-time API deployment for carbon footprint analysis. This deployment uses a Google Cloud Platform (GCP) instance with 16 GPUs (Paper, p. 23). The specific type of GPU is not mentioned for deployment.

### Training or Fine-tuning Requirements:
*   **Training:** The 176B parameter BLOOM model was trained on a cluster of 48 nodes, for a total of **384 NVIDIA A100 80GB GPUs**. Each node was also equipped with 2x AMD EPYC 7543 32-Core CPUs and **512 GB of RAM** (Paper, p. 18).
*   **Fine-tuning:** Hyperparameters for multitask finetuning are provided (Paper, p. 21, Table 3), but the specific hardware used for this process is not detailed. It was likely performed on a similar, possibly smaller, configuration of the Jean Zay supercomputer.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

Ethical considerations were a central part of the BigScience project, guided by a collaboratively designed **Ethical Charter** that emphasizes values of inclusivity, diversity, openness, reproducibility, and responsibility (Paper, p. 7).

*   **Sensitive Data:** The training data was sourced from public datasets and the web, which contained Personal Identifiable Information (PII). A risk mitigation strategy involved redacting PII (such as social security numbers) from the OSCAR portion of the corpus, which was identified as the highest-risk source (Paper, p. 13).

*   **Risks and Mitigation Strategies:**
    *   **Harmful Use-Cases:** The developers acknowledged the risk of the model being used for potentially harmful purposes. To mitigate this, BLOOM was released under a **Responsible AI License (RAIL)**, which includes 13 behavioral-use restrictions to limit such applications (Paper, p. 24).
    *   **Bias:** The risk of the model perpetuating social biases from its training data was acknowledged. A preliminary bias evaluation was conducted using the multilingual CrowS-Pairs dataset for English and French across nine bias categories (e.g., gender, religion, nationality) (Paper, p. 41-42). While results suggested a "limited presence of bias," the paper acknowledges the limitations of this evaluation and the lack of multilingual bias assessment tools (Paper, p. 43).
    *   **Environmental Impact:** The carbon footprint of the model's entire lifecycle was a key consideration. A Life Cycle Assessment (LCA) approach was used to estimate emissions from equipment manufacturing, training, and deployment (Paper, p. 22-23). The training emissions were estimated at 25 tons of CO2eq, which is significantly lower than comparable models like GPT-3, largely due to the use of France's low-carbon, nuclear-powered energy grid (Paper, p. 23).
    *   **Exclusion:** The project was motivated by the goal of democratizing access to LLMs, as the high computational cost of their development has historically excluded the majority of the research community (Paper, p. 4, 6).

*   **Known Fraught Use Cases:** The behavioral-use restrictions in the RAIL license are designed to prevent fraught use cases, though these are not explicitly listed in the paper. The bias evaluation highlights sensitivities around gender, socioeconomic status, religion, and nationality, where model performance showed statistically significant (though small) deviations from neutral (Paper, p. 42, Table 14).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Under-Represented Languages:** The model's performance is poor for languages that were under-represented in the training data. For example, translation quality for Swahili and Yoruba (<50k tokens each in the training data) is very low (Paper, p. 32).
*   **Limitations of Bias Evaluation:** The bias analysis is preliminary. It only covers English and French and is limited to the constructs measured by the CrowS-Pairs dataset. The paper explicitly states that "very little material (corpora, measures) is available for multilingual bias assessment" and that the evaluation cannot cover all possible usage scenarios (Paper, p. 43).
*   **Prompt Sensitivity:** The model's performance, particularly in zero-shot settings on classification tasks, can be highly dependent on the specific prompt used. Average performance across multiple prompts can be close to random chance, even when individual prompts perform well (Paper, p. 27-28).
*   **Extrapolation of Ablation Studies:** Architectural decisions were guided by ablation studies on smaller models (e.g., 1.3B parameters). The paper cautions that these findings may not fully extrapolate to the 176B scale due to "phase transitions" in model behavior observed in models larger than 6.7B (Paper, p. 15).
*   **Overgeneration in Translation:** In machine translation tasks, especially in zero-shot settings, the model is prone to over-generation (producing text longer than the reference) and sometimes fails to produce text in the correct target language (Paper, p. 29-30).

### Recommendations:
*   **Adherence to License:** All users must use the model in accordance with the usage restrictions outlined in the Responsible AI License (RAIL) (Paper, p. 24).
*   **Use Few-Shot Prompting:** Performance is significantly improved when using few-shot examples compared to zero-shot. For instance, in machine translation, few-shot prompting greatly reduces issues of overgeneration and improves translation quality (Paper, p. 30).
*   **Prompt Engineering:** For tasks like machine translation, more verbose prompts tend to yield better results (Paper, p. 29). Users should be aware that performance can be sensitive to the prompt design.
*   **Caution with Low-Resource Languages:** Users should exercise caution when applying the model to low-resource languages, especially those that were not well-represented in the ROOTS training corpus, as performance may be poor (Paper, p. 32).