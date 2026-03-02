## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, BLOOM (BigScience Large Open-science Open-access Multilingual Language Model), was developed by the BigScience Workshop, an open research collaboration of hundreds of researchers (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3). The project was coordinated by BigScience and began after receiving a compute grant from GENCI on the Jean Zay supercomputer at IDRIS/CNRS (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 6). The collaboration grew to include over 1200 registered participants from 38 countries with backgrounds in machine learning, computer science, linguistics, statistics, philosophy, law, and other fields (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 6). A list of major contributors and participants across different working groups like Dataset, Tokenization, Architecture, and Engineering is provided in the accompanying paper (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 1-3). Correspondence can be directed to bigscience-contact@googlegroups.com (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 1).

### Model date:
The development of BLOOM was a year-long initiative (May 2021 - May 2022) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 6). The final training of the 176B parameter model took approximately 3.5 months on the Jean Zay supercomputer (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 18). The model was released with a detailed model card and a Responsible AI License (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24). The associated research paper is dated June 27, 2023 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 1).

### Model version:
The primary model is BLOOM, a 176-billion parameter model (config.json; BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21). The project also trained and released five smaller versions with the same architecture and training data for research and accessibility (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 22, Table 3):
*   BLOOM-560M
*   BLOOM-1.1B
*   BLOOM-1.7B
*   BLOOM-3B
*   BLOOM-7.1B

Additionally, multitask finetuned versions of these models, referred to as BLOOMZ, were created to improve zero-shot task generalization abilities (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 14, 22). The model was developed using version 4.21.0 of the `transformers` library (config.json).

### Model type:
BLOOM is a large language model of the "bloom" model type, specifically a decoder-only Transformer designed for causal language modeling (`BloomForCausalLM`) (config.json; BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3, 15).

**Architecture Details:**
*   **Parameters:** 176,247 million (176B) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21).
*   **Layers:** 70 Transformer layers (`n_layer`: 70) (config.json).
*   **Hidden Size:** 14,336 (`n_embed`: 14336) (config.json).
*   **Attention Heads:** 112 (`num_attention_heads`: 112) (config.json).
*   **Vocabulary Size:** 250,880 (`vocab_size`: 250880) (config.json).
*   **Sequence Length:** 2048 tokens (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21).
*   **Positional Embeddings:** It uses ALiBi (Attention with Linear Biases) positional embeddings, which directly attenuate attention scores based on the distance between keys and queries, leading to smoother training and better downstream performance (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 16).
*   **Layer Normalization:** An additional layer normalization is applied immediately after the embedding layer to improve training stability (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 16).
*   **Activation Function:** GELU (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21).
*   **Model Size:** The total size of the model weights is approximately 352.5 GB (model.safetensors.index.json; pytorch_model.bin.index.json).

### Training details:
BLOOM was trained using the Megatron-DeepSpeed framework, which enables large-scale distributed training through a combination of 3D parallelism: Data Parallelism (DP=8), Pipeline Parallelism (PP=12), and Tensor Parallelism (TP=4) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 19, Figure 6). The training also utilized the ZeRO (Zero Redundancy Optimizer) stage 1 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 20).

**Key Hyperparameters and Methodologies:**
*   **Precision:** The model was trained using `bfloat16` mixed precision, which has the same dynamic range as `float32` but lower precision, providing a balance of high performance and training stability (config.json; BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 20).
*   **Total Tokens:** Trained on 366 billion tokens from the ROOTS corpus (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21).
*   **Batch Size:** Global batch size of 2048 sequences (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21).
*   **Learning Rate:** 6.0e-5, with a cosine decay schedule and a minimum learning rate of 6.0e-6 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21, Table 3).
*   **Warmup:** 375 million tokens (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21, Table 3).
*   **Optimizer:** Adam with β1=0.9 and β2=0.95 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 21, Table 3).
*   **Regularization:** Weight decay of 0.1 and gradient clipping at 1.0. No dropout was used (`hidden_dropout`: 0.0, `attention_dropout`: 0.0) (config.json; BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 22).
*   **Fused Kernels:** Custom fused CUDA kernels were used for operations like LayerNorm, scaling, masking, and softmax to optimize GPU utilization and minimize data transfers (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 20).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   **BLOOM: A 176B-Parameter Open-Access Multilingual Language Model**. This paper details the entire development process, including dataset creation, architecture design, engineering challenges, and evaluation results (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 1-73).

The model and its smaller versions are publicly available on the Hugging Face Hub, which includes documentation and usage examples:
*   **Model Page:** `hf.co/bigscience/bloom` (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3, 24).

### Citation details:
```bibtex
@article{BigScienceWorkshop2022BLOOM,
  title={{BLOOM: A 176B-Parameter Open-Access Multilingual Language Model}},
  author={BigScience Workshop},
  journal={ArXiv},
  year={2022},
  volume={abs/2211.05100}
}
```
(BLOOM: A 176B-Parameter Open-Access Multilingual Language Model)

### License:
The BLOOM model is released under a custom **Responsible AI License (RAIL)**. This license is designed to balance open access with responsible use by including behavioral-use clauses that restrict the model's application in potentially harmful scenarios, such as generating misinformation or for malicious purposes. The license contains 13 such restrictions based on the model's intended uses and limitations. The model is offered at no charge, and users are free to use it as long as they comply with the license terms. The source code associated with BLOOM is available under an Apache 2.0 open-source license (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24).

### Contact:
For questions, feedback, or to report issues, you can contact the BigScience Workshop at: **bigscience-contact@googlegroups.com** (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
BLOOM is a general-purpose, open-access, multilingual language model designed to perform a wide variety of natural language processing tasks based on natural language instructions or few-shot demonstrations (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3). As a causal decoder-only model, its primary function is text generation. It can be prompted to perform tasks such as:
*   Text summarization (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26)
*   Machine translation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26)
*   Text classification (e.g., entailment, sentiment analysis) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26)
*   Code generation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 32)

The model is multilingual and can perform these tasks across the 46 natural and 13 programming languages it was trained on (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3). The input-output structure involves providing a text prompt, which the model then completes. For example, a prompt for translation could be `English: We appear to have stopped moving. = French:` and the model would be expected to generate the French translation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 72).

### Primary intended users:
The primary intended users are researchers and developers in the machine learning and natural language processing communities (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3). The model was created to "democratize this powerful technology" and "facilitate future research and applications using LLMs" by providing an open-access alternative to proprietary models (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 3).

### Out-of-scope uses:
The model is not intended for any use that violates the terms of its Responsible AI License (RAIL). The license includes 13 behavioral-use restrictions to limit potentially harmful applications. These restrictions define the out-of-scope uses and were identified based on the model's limitations and the BigScience ethical charter (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24). Users must consult the full license text to understand all restrictions.

---

## How to Use
The model is available on the Hugging Face Hub and can be used with the `transformers` library (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24). The tokenizer is a `BloomTokenizerFast` (tokenizer_config.json).

Below is a generic code snippet illustrating how to load and use the model for text generation. Note that running the full 176B parameter model requires substantial hardware.

```python
from transformers import BloomForCausalLM, BloomTokenizerFast
import torch

# Load the tokenizer and model
# For the full 176B model, you'll need multiple high-VRAM GPUs and device_map="auto"
# For demonstration, a smaller version can be used, e.g., "bigscience/bloom-560m"
model_name = "bigscience/bloom-1b7"
tokenizer = BloomTokenizerFast.from_pretrained(model_name)
model = BloomForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto", # Use bfloat16 if available
    device_map="auto"
)

# Example prompt for translation (based on paper's examples)
prompt = "English: It is a beautiful day. = French:"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate text
# The model will continue the text from the prompt
output_sequences = model.generate(
    input_ids=inputs["input_ids"],
    max_length=50, # Set a max length for the generation
    num_return_sequences=1
)

# Decode and print the output
generated_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
print(generated_text)

# Expected-style output:
# English: It is a beautiful day. = French: C'est une belle journée.
```
The model's input is a string of text, and its output is the continuation of that text. The format of the prompt is crucial for guiding the model to perform the desired task (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 25). Appendix A of the research paper provides extensive examples of prompts used for various evaluation tasks like question answering, summarization, and translation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 65-73).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** As a multilingual model trained on 46 natural and 13 programming languages, language is a primary factor. Performance varies significantly across languages, particularly between high-resource and low-resource languages present in the training data (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 32).
*   **Demographic and Social Factors:** The model's behavior can be influenced by demographic factors. The paper evaluates potential biases related to ethnicity, color, gender, socioeconomic status, nationality, religion, age, sexual orientation, physical appearance, and disability (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 42, Table 14).
*   **Prompt Formulation:** The performance of the model is highly sensitive to the way a task is framed in the input prompt. The evaluation shows that different prompts for the same task can lead to significant performance variations (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 25, 29).

### Evaluation factors:
The model evaluations reported in the paper analyze performance across the following factors:
*   **Language:** Performance is disaggregated by language for tasks like machine translation (across Romance, low-resource, and high-resource pairs) and summarization (across 9 languages) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 31, 33).
*   **Bias Categories:** Bias is evaluated and reported across nine different social and demographic categories for English and French (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 42, Table 14).
*   **Model Scale:** Performance is compared across the six different sizes of BLOOM models to analyze scaling properties (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 28, Figure 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of task-specific metrics:
*   **Classification (SuperGLUE):** Accuracy (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 28).
*   **Machine Translation (WMT, Flores-101, DiaBLa):** BLEU and COMET scores (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26, 30).
*   **Summarization (WikiLingua):** ROUGE-2, ROUGE-L, and Levenshtein distance (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **Code Generation (HumanEval):** pass@k, which measures the percentage of problems solved if the model generates k samples (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 34, Table 9).
*   **Bias (CrowS-Pairs):** Prompt accuracy, where a score close to 50% indicates an absence of systematic preference for stereotyped statements (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 41).
*   **Linguistic Probing (Universal Dependencies):** Weighted F1 score, used to evaluate the performance of a logistic regression classifier trained on the model's embeddings to predict morphosyntactic features (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 38).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robust measurements and account for variability, the following approaches were used:
*   **Prompt Variation:** For prompt-based tasks, a random sample of five different prompts was used for each task to evaluate performance and variability across prompt formulations (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **Multiple Runs:** Bias evaluation results on CrowS-Pairs were averaged over eight runs. Probing task results were averaged across three runs with different random seeds to account for randomness in classifier initialization (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 38, 42).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public datasets covering multiple tasks and languages:
*   **SuperGLUE:** A subset of the English benchmark including Ax-b, Ax-g, BoolQ, CB, WiC, WSC, and RTE tasks (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **WMT14:** For machine translation between English-French and English-Hindi (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **Flores-101:** A multilingual benchmark for low-resource and multilingual machine translation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **DiaBLa:** A corpus of bilingual (English-French) spontaneous written dialogues for contextual machine translation (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **WikiLingua:** A multilingual summarization dataset with article-summary pairs in 9 languages (Arabic, English, Spanish, French, Hindi, Indonesian, Portuguese, Vietnamese, Chinese) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   **HumanEval:** A benchmark for evaluating code generation capabilities in Python (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 32).
*   **multilingual CrowS-Pairs:** A dataset for measuring social biases in English and French, adapted from the original CrowS-Pairs (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 41).
*   **Universal Dependencies (UD):** Treebanks for 17 languages were used for probing the model's internal representations of linguistic information (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 37).

### Motivation:
The datasets were chosen to provide a comprehensive evaluation of the model's capabilities. English-only datasets like SuperGLUE were included to facilitate comparison with prior work (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26). The multilingual datasets (WMT, Flores-101, WikiLingua) were chosen to specifically test BLOOM's core design goal: multilingual performance (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26). Datasets like HumanEval, CrowS-Pairs, and Universal Dependencies were used to evaluate more specific capabilities and characteristics, such as code generation, social bias, and learned linguistic knowledge (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 32, 37, 41).

### Preprocessing:
Preprocessing steps were specific to each evaluation task:
*   For machine translation, default tokenization was used for WMT14 and DiaBLa, while the `spm-flores-101` tokenizer was used for Flores-101 to calculate BLEU scores (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   For summarization, the SentencePiece tokenizer from the Flores-101 dataset was used for calculating ROUGE scores to better handle multilingual text (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 26).
*   For probing tasks, the original training, validation, and test splits from the Universal Dependencies treebanks were used (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 38).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
BLOOM was trained on the **ROOTS corpus**, a composite collection of 498 datasets amounting to 1.61 terabytes of text. The corpus is multilingual, spanning 46 natural languages and 13 programming languages (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 7).

The data sources for ROOTS include (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 11):
1.  **Crowdsourced Datasets (BigScience Catalogue):** A large list of processed and non-processed sources covering a wide range of languages, compiled by workshop participants and research collectives.
2.  **GitHub Code:** A dataset of programming languages collected from the GitHub data collection on Google's BigQuery.
3.  **OSCAR:** Data sourced from the OSCAR corpus (version 21.09), which is derived from a Common Crawl web snapshot. This source constitutes 38% of the final corpus.

A detailed breakdown of the 46 natural languages, their families, and their size in bytes is provided in Table 1 of the paper (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 8). The distribution of the 13 programming languages is shown in Figure 3 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 13).

### Motivation:
The creation of the ROOTS corpus was motivated by a desire to move beyond purely automated, heuristic-based data collection from web crawls. The project aimed to prioritize human involvement, local expertise, and language expertise in the data curation process. This was done to create a high-quality, diverse multilingual dataset while improving standards of documentation and respect for data rights-holders (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 9).

### Preprocessing:
The data processing pipeline for creating the ROOTS corpus involved several steps (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 11-13, Figure 2):
*   **Source Data Acquisition:** Text was extracted from a variety of formats, including NLP datasets, PDF files from scientific archives, and HTML from web crawls.
*   **"Quality" Filtering:** A set of quality indicators were used to filter for text "written by humans for humans." These indicators and their thresholds were selected individually for each language by fluent speakers to remove non-natural language like SEO pages and spam.
*   **Deduplication:** Near-duplicate documents were removed in two deduplication steps.
*   **Privacy Redaction:** Personal Identifiable Information (PII), such as social security numbers, was redacted from the OSCAR portion of the corpus using regular expressions.
*   **Tokenization:** The model uses a custom Byte-Pair Encoding (BPE) tokenizer trained on a deduplicated subset of the ROOTS corpus. It is a byte-level tokenizer, which prevents unknown tokens. No text normalization (e.g., Unicode normalization) was performed on the training data to keep the model as general as possible (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 18).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by individual factors:
*   **By Language:**
    *   **Machine Translation (Flores-101):** Table 8 presents spBLEU scores for 1-shot translation across various language pairs, grouped into low-resource, Romance, high-resource, and high-to-mid-resource categories. For example, in low-resource pairs, BLOOM achieves a score of 24.6 for English to Bengali, compared to M2M's 23.0. For Romance languages, BLOOM scores 37.2 for French to English, compared to M2M's 28.7 (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 31).
    *   **Summarization (WikiLingua):** Figure 9 shows ROUGE-2 F-measure scores for one-shot summarization in 9 languages, demonstrating performance increases with model scale (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 33).
*   **By Bias Type:**
    *   **CrowS-Pairs:** Table 14 shows the model's accuracy on bias categories for English and French. For example, on the "gender" category, the model scores 51.17% for English and 51.24% for French, indicating a slight preference for stereotyped statements. For "religion," the scores are 53.82% (English) and 53.01% (French) (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 42).
*   **By Morphosyntactic Feature:**
    *   **Probing:** Figure 12 shows heatmaps of probing performance (F1 score) for different linguistic features (e.g., Aspect, Case, Gender, Tense) across 17 languages for both BLOOM-1.7B and BLOOM-176B (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 39).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The full 176B parameter model has a total size of approximately 352.5 GB (model.safetensors.index.json; pytorch_model.bin.index.json). Loading this model in `bfloat16` or `float16` precision would require approximately 352 GB of GPU VRAM. The training setup used nodes with 8 x 80GB A100 GPUs (640 GB total VRAM per node), suggesting that multiple high-VRAM GPUs are necessary to load the model (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 18).

### Deploying Requirements:
The paper mentions an ongoing exploration of deploying the model via an API on a Google Cloud Platform instance with 16 GPUs. This suggests that a multi-GPU server is required for real-time deployment (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 23).

### Training or Fine-tuning Requirements:
The pre-training of the 176B BLOOM model was a large-scale computational task with the following hardware requirements (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 18):
*   **Hardware:** 48 nodes of the Jean Zay supercomputer, with 4 spare nodes maintained for redundancy.
*   **GPUs:** Each node contained 8 NVIDIA A100 80GB GPUs, for a total of 384 GPUs used for training.
*   **CPU:** Each node was equipped with 2x AMD EPYC 7543 32-Core CPUs.
*   **System RAM:** 512 GB of RAM per node.
*   **Interconnect:** 4 NVLink GPU-to-GPU interconnects per node and 4 Omni-Path 100 Gbps links per node for inter-node communication.
*   **Total Compute:** The training process took 3.5 months and consumed 1,082,990 compute hours.

---

## Ethical Considerations
The BigScience workshop established an Ethical Charter to guide the project, emphasizing values of inclusivity, diversity, openness, reproducibility, and responsibility (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 7).

*   **Sensitive Data:** The training data, ROOTS, was sourced from publicly available data, including web crawls (OSCAR). Recognizing the privacy risks, the developers redacted Personal Identifiable Information (PII) from the OSCAR portion of the corpus using regex-based methods (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 13).
*   **Risks and Mitigation:** The developers acknowledge the risk of "potentially harmful use-cases" (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24). To mitigate this, BLOOM was released with a **Responsible AI License (RAIL)**. This license includes 13 behavioral-use clauses that explicitly restrict the use of the model for malicious purposes, thereby striking a balance between open access and responsible use (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24).
*   **Bias:** The model was evaluated for social biases using the multilingual CrowS-Pairs dataset for English and French. The results suggest an "overall absence of bias" as scores were close to the 50% baseline, but also show statistically significant (though small) preferences for stereotypes in certain categories like gender, socioeconomic status, and religion (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, pp. 41-42). The paper acknowledges that this evaluation is limited and does not cover all possible languages or bias types (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 43).
*   **Environmental Impact:** The carbon footprint of the model's training was estimated using a Life Cycle Assessment approach. The training process consumed 433 MWh and resulted in an estimated 25 tons of CO2eq emissions, which is significantly lower than comparable models like GPT-3 due to the use of a low-carbon energy grid (nuclear-powered) in France (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 23, Table 4).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Low-Resource Languages:** The model's performance is very poor for under-represented languages in the training data. For example, translation quality for Swahili and Yoruba (<50k tokens in training data) is significantly worse than for other languages, questioning the model's utility for these specific languages despite their inclusion in training (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 32).
*   **Limited Bias Evaluation:** The bias analysis is confined to English and French using the CrowS-Pairs dataset. The authors explicitly state that this does not cover the breadth of possible usage scenarios or the full range of languages the model supports. Little material is available for comprehensive multilingual bias assessment (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 43).
*   **Extrapolation of Ablation Studies:** Architectural decisions were partly based on ablation studies conducted on smaller models (e.g., 1.3B parameters). The authors caution that these findings may not fully extrapolate to the final 176B model, as emergent properties and phase transitions have been observed in models larger than 6.7B (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 15).
*   **Architectural Artifacts:** The use of an additional LayerNorm after the embedding layer, which was added to improve stability, might have been a necessary fix for instabilities encountered when using `float16` precision in early experiments. The final training used `bfloat16`, which may have alleviated the need for this architectural change (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 16).

### Recommendations:
*   **Adherence to License:** All users must use the model in accordance with the behavioral-use restrictions outlined in the Responsible AI License (RAIL) to prevent harmful applications (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 24).
*   **Careful Prompting:** The model's output is highly dependent on the input prompt. Users should expect to experiment with prompt engineering to achieve desired results.
*   **Caution with Low-Resource Languages:** Users should be cautious when applying the model to tasks involving languages that were under-represented in the ROOTS training corpus, as performance may be poor.
*   **Further Research:** The paper suggests several areas for future research, including:
    *   Probing the model's abilities on languages not included in the pretraining corpus.
    *   Conducting a more in-depth evaluation of performance on under-resourced languages.
    *   Analyzing how morpho-syntactic representations are built across different layers and during the course of training (BLOOM: A 176B-Parameter Open-Access Multilingual Language Model, p. 41).