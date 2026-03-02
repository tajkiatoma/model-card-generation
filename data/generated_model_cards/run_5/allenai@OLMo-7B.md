## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from the Allen Institute for Artificial Intelligence, University of Washington, Yale University, New York University, and Carnegie Mellon University (OLMo: Accelerating the Science of Language Models, p. 1). The primary affiliation is the Allen Institute for Artificial Intelligence (OLMo: Accelerating the Science of Language Models, p. 1).

### Model date:
The associated academic paper was last updated on June 7, 2024 (OLMo: Accelerating the Science of Language Models, p. 1). The model was trained in a series of checkpoints, with over 557,000 steps recorded, corresponding to over 2.46 trillion tokens of training data (step_token_index, OLMo: Accelerating the Science of Language Models, p. 3, Table 1).

### Model version:
This model is the OLMo-7B variant. The OLMo framework also includes a 1B parameter model and other 7B variants, such as OLMo-7B-twin-2T (OLMo: Accelerating the Science of Language Models, p. 2, 8). The goal of the OLMo project is to provide a "truly Open Language Model" to enable the scientific study of language models, releasing not just model weights but also training data, and training and evaluation code (OLMo: Accelerating the Science of Language Models, p. 1).

### Model type:
OLMo is a decoder-only transformer language model designed for causal language modeling (`config.json`, OLMo: Accelerating the Science of Language Models, p. 2).

**Architecture Details:**
*   **Model Type:** `hf_olmo` (`config.json`)
*   **Architecture:** `OLMoForCausalLM` (`config.json`)
*   **Layers:** 32 (`config.json`)
*   **Hidden Size (`d_model`):** 4096 (`config.json`)
*   **Attention Heads:** 32 (`config.json`)
*   **MLP Hidden Size:** 22016 (`config.json`)
*   **Activation Function:** SwiGLU (`config.json`, OLMo: Accelerating the Science of Language Models, p. 2)
*   **Positional Embeddings:** Rotary Positional Embeddings (RoPE) (`config.json`, OLMo: Accelerating the Science of Language Models, p. 3)
*   **Layer Normalization:** Non-parametric, with no adaptive gain or bias (`config.json`, OLMo: Accelerating the Science of Language Models, p. 2)
*   **Biases:** All bias terms are excluded from the architecture to improve training stability (`config.json`, OLMo: Accelerating the Science of Language Models, p. 2)
*   **Vocabulary Size:** 50,280, expanded to an embedding matrix size of 50,304 for throughput (`config.json`, OLMo: Accelerating the Science of Language Models, p. 3)
*   **Context Length:** 2048 tokens (`config.json`)

### Training details:
The model was trained using the ZeRO optimizer strategy via PyTorch's FSDP framework to reduce memory consumption (OLMo: Accelerating the Science of Language Models, p. 4).

*   **Optimizer:** AdamW with betas of 0.9 and 0.95, and an epsilon of 1.0E-5 (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
*   **Learning Rate Schedule:**
    *   **Peak LR:** 3.0E-4 (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   **Warmup:** 5000 steps (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   **Decay:** Linear decay to a tenth of the peak learning rate (3.0E-05) over the remainder of training (`config.json`, OLMo: Accelerating the Science of Language Models, p. 5).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens (2048 instances of 2048 tokens each) (OLMo: Accelerating the Science of Language Models, p. 3, 4).
*   **Precision:** Mixed-precision training with `amp_bf16` (`config.json`, OLMo: Accelerating the Science of Language Models, p. 5).
*   **Gradient Clipping:** Gradients are clipped such that the total L2-norm does not exceed 1.0 (OLMo: Accelerating the Science of Language Models, p. 5).
*   **Total Training Tokens:** The evaluated checkpoint was trained on 2.46 trillion tokens (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Groeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., ... & Hajishirzi, H. (2024). *OLMo: Accelerating the Science of Language Models*. arXiv preprint arXiv:2402.00838. (OLMo: Accelerating the Science of Language Models, p. 1).

The paper describes the model architecture, training data (Dolma), training process, and evaluation framework. The full OLMo framework release includes training and evaluation code, training data, and intermediate model checkpoints (OLMo: Accelerating the Science of Language Models, p. 1-2).

### Citation details:
```bibtex
@article{Groeneveld2024OLMo,
  title={{OLMo: Accelerating the Science of Language Models}},
  author={Dirk Groeneveld and Iz Beltagy and Pete Walsh and Akshita Bhagia and Rodney Kinney and Oyvind Tafjord and Ananya Harsh Jha and Hamish Ivison and Ian Magnusson and Yizhong Wang and Shane Arora and David Atkinson and Russell Authur and Khyathi Raghavi Chandu and Arman Cohan and Jennifer Dumas and Yanai Elazar and Yuling Gu and Jack Hessel and Tushar Khot and William Merrill and Jacob Morrison and Niklas Muennighoff and Aakanksha Naik and Crystal Nam and Matthew E. Peters and Valentina Pyatkin and Abhilasha Ravichander and Dustin Schwenk and Saurabh Shah and Will Smith and Emma Strubell and Nishant Subramani and Mitchell Wortsman and Pradeep Dasigi and Nathan Lambert and Kyle Richardson and Luke Zettlemoyer and Jesse Dodge and Kyle Lo and Luca Soldaini and Noah A. Smith and Hannaneh Hajishirzi},
  journal={ArXiv},
  year={2024},
  volume={abs/2402.00838v4},
  url={https://api.semanticscholar.org/CorpusID:267386491}
}
```
(Derived from OLMo: Accelerating the Science of Language Models, p. 1)

### License:
All code and weights are released under the Apache 2.0 License (OLMo: Accelerating the Science of Language Models, p. 2).

### Contact:
For questions, issues, or feedback, contact the development team at `olmo@allenai.org` (OLMo: Accelerating the Science of Language Models, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to enable the scientific study of language models by providing the research community with a powerful, truly open model (OLMo: Accelerating the Science of Language Models, p. 1). It is intended to be used as a base model for research into topics such as the relationship between pretraining data and model capabilities, the impact of design and hyperparameter choices, and optimization methods (OLMo: Accelerating the Science of Language Models, p. 2). It can also be used as a foundation for further fine-tuning for downstream applications, such as creating a general chat assistant (OLMo: Accelerating the Science of Language Models, p. 3).

### Primary intended users:
The primary intended users are members of the open research community, including academics and practitioners, who study and build upon large language models (OLMo: Accelerating the Science of Language Models, p. 1).

### Out-of-scope uses:
The model is not intended for deployment in high-stakes scenarios without significant further evaluation and adaptation. The training data is primarily in English, so its performance in other languages is out-of-scope (OLMo: Accelerating the Science of Language Models, p. 9). The model may generate problematic content, including biased, toxic, or factually incorrect information (hallucinations), and should not be used in ways that could cause harm (OLMo: Accelerating the Science of Language Models, p. 9-10).

---

## How to Use
This section outlines how to use the model.

To use the model and its tokenizer, you need to have the `ai2-olmo` library installed, with a version of at least `0.2.2` (`requirements.txt`). You can then use the Hugging Face `transformers` library to load the model and tokenizer.

```python
# Make sure to install the required packages:
# pip install transformers torch ai2-olmo>=0.2.2

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model from the Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")
model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")

# Example prompt
prompt = "The science of language models is"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
# The model can be run on a GPU if available
# inputs = inputs.to("cuda")
# model.to("cuda")
response = model.generate(**inputs, max_length=50, do_sample=True, top_k=50, top_p=0.95)

# Decode and print the output
print(tokenizer.decode(response[0], skip_special_tokens=True))

# Expected output might be something like:
# The science of language models is a rapidly developing field. The ability to train models on massive amounts of text data has led to a revolution in natural language processing. These models are now able to perform a wide range of tasks, from translation to summarization to question answering.
```
(Derived from `config.json`, `tokenizer_config.json`, `requirements.txt`)

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Language:** The model's pretraining data is focused on English, which is a significant factor in its performance and capabilities (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Text Domain:** The model's performance varies across different domains of text, such as scraped web text (Common Crawl) versus curated sources (Wikipedia, academic papers) (OLMo: Accelerating the Science of Language Models, p. 7).
*   **Dialect:** The model's performance may vary across different dialects of English. The evaluation data includes datasets for targeted analysis of performance disparities between dialects (OLMo: Accelerating the Science of Language Models, p. 16).

### Evaluation factors:
The model was evaluated on the following factors:
*   **Downstream Task Performance:** Zero-shot performance on a suite of 8 core commonsense reasoning tasks (OLMo: Accelerating the Science of Language Models, p. 4-5).
*   **Intrinsic Language Modeling:** Perplexity across a wide range of text domains using the Paloma benchmark (OLMo: Accelerating the Science of Language Models, p. 4, 6).
*   **Chat and Safety Capabilities:** Performance of the instruction-tuned model on chat capabilities (AlpacaEval), safety (ToxiGen), and truthfulness (TruthfulQA) (OLMo: Accelerating the Science of Language Models, p. 4, 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Downstream Tasks:** Zero-shot accuracy is reported. This is determined using a rank classification approach where candidate text completions are ranked by their likelihood (OLMo: Accelerating the Science of Language Models, p. 6).
*   **Intrinsic Language Modeling:** Performance is measured by perplexity, reported as bits per byte (bpb) to allow for fair comparison between models with different vocabularies (OLMo: Accelerating the Science of Language Models, p. 6).
*   **Adaptation Evaluation:**
    *   **MMLU:** 0-shot accuracy (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **AlpacaEval:** Win rate (%) against a baseline model (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **ToxiGen:** Percentage of generated text classified as toxic (lower is better) (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **TruthfulQA:** Percentage of responses that are both informative and truthful (% Info+True) (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For downstream task evaluation, different likelihood normalization strategies were selected for each dataset to calculate the ranking of candidate answers. For example, unconditional likelihood normalization was used for `arc` and `openbookqa`, while per-token normalization was used for `hellaswag`, `piqa`, and `winogrande` (OLMo: Accelerating the Science of Language Models, p. 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Downstream Evaluation Suite:** A set of 8 core tasks were used: `arc` (easy and challenge), `boolq`, `openbookqa`, `sciq`, `hellaswag`, `piqa`, and `winogrande` (OLMo: Accelerating the Science of Language Models, p. 5). An additional 6 tasks were also evaluated: `headqa_en`, `logiqa`, `mrpc`, `qnli`, `wic`, and `wnli` (OLMo: Accelerating the Science of Language Models, p. 17, Table 7).
*   **Intrinsic Evaluation Benchmark (Paloma):** A perplexity benchmark that includes 585 different domains of text from 18 separate data sources. The primary reported results are on an aggregate of 11 publicly available sources, including C4, Wikitext-103, RedPajama, and Dolma (OLMo: Accelerating the Science of Language Models, p. 4, 6).
*   **Adaptation Evaluation Suite (TÜLU):** This suite includes evaluations for chat capabilities and safety, using datasets such as MMLU, AlpacaEval, ToxiGen, and TruthfulQA (OLMo: Accelerating the Science of Language Models, p. 4, 8).

### Motivation:
*   The downstream tasks were selected at the beginning of model development due to their "naturalness (e.g., all can be formulated as text completion scoring tasks) and ability to provide meaningful signals throughout training" (OLMo: Accelerating the Science of Language Models, p. 4).
*   The Paloma benchmark was used to "measure how OLMo fits distributions of language beyond held-out training data" (OLMo: Accelerating the Science of Language Models, p. 4).
*   The adaptation evaluation suite was used to "showcase the efficacy of using OLMo as a base for further fine-tuning" (OLMo: Accelerating the Science of Language Models, p. 4).

### Preprocessing:
For the Paloma perplexity evaluation, the training data was explicitly decontaminated. Any pretraining document containing paragraphs that leaked from the Paloma evaluation data was removed to ensure a fair out-of-sample fit measurement (OLMo: Accelerating the Science of Language Models, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on **Dolma**, a "diverse, multi-source corpus containing trillions of tokens" (OLMo: Accelerating the Science of Language Models, p. 3). The OLMo-7B model was trained on a 2.46 trillion token sample from this corpus (OLMo: Accelerating the Science of Language Models, p. 3, Table 1). The composition of the full Dolma dataset is as follows:

| Source             | Type          | UTF-8 bytes (GB) | Docs (millions) | Tokens (billions) |
|--------------------|---------------|------------------|-----------------|-------------------|
| Common Crawl       | web pages     | 9,812            | 3,734           | 2,180             |
| GitHub             | code          | 1,043            | 210             | 342               |
| Reddit             | social media  | 339              | 377             | 80                |
| Semantic Scholar   | papers        | 268              | 38.8            | 57                |
| Project Gutenberg  | books         | 20.4             | 0.056           | 5.2               |
| Wikipedia          | encyclopedic  | 16.2             | 6.2             | 3.7               |
| **Total**          |               | **11,519**       | **4,367**       | **2,668**         |

(OLMo: Accelerating the Science of Language Models, p. 3, Table 2)

The full Dolma corpus is openly available (OLMo: Accelerating the Science of Language Models, p. 2).

### Motivation:
The Dolma dataset was created to "facilitate open research on language model pretraining" (OLMo: Accelerating the Science of Language Models, p. 3). The data sources were chosen because they are (1) commonly used in large-scale language model pretraining and (2) accessible to the general public (OLMo: Accelerating the Science of Language Models, p. 3).

### Preprocessing:
The Dolma dataset was built using a pipeline that includes: (1) language filtering, (2) quality filtering, (3) content filtering, (4) deduplication, (5) multi-source mixing, and (6) tokenization (OLMo: Accelerating the Science of Language Models, p. 3).

*   **Tokenization:** A modified version of the BPE-based tokenizer from GPT-NeoX-20B was used, with additional special tokens for masking personally identifiable information (PII) (`tokenizer.json`, OLMo: Accelerating the Science of Language Models, p. 3). The tokenizer uses NFC normalization and a ByteLevel pre-tokenizer (`tokenizer.json`).
*   **Training Instance Creation:** Tokens from every document are concatenated, with a special EOS token (`<|endoftext|>`) appended to the end of each document. This stream of tokens is then grouped into consecutive chunks of 2048 tokens to form training instances (OLMo: Accelerating the Science of Language Models, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
**Downstream Task Evaluation (Zero-shot Accuracy):**

| Model    | arc_challenge | arc_easy | boolq | hellaswag | openbookqa | piqa | sciq | winogrande | avg.  |
|----------|---------------|----------|-------|-----------|------------|------|------|------------|-------|
| OLMo-7B  | 48.5          | 65.4     | 73.4  | 76.4      | 50.4       | 78.4 | 93.8 | 67.9       | 69.3  |

(OLMo: Accelerating the Science of Language Models, p. 6, Table 3)

**Intrinsic Evaluation (Bits per Byte on select Paloma sources):**
OLMo-7B's performance was evaluated on 11 sources from the Paloma benchmark. For example, it performs well on C4, which is highly represented in its training data, and is less sample efficient on sources like WikiText-103 (OLMo: Accelerating the Science of Language Models, p. 7-8, Figure 2).

**Adaptation Evaluation (Instruction-Tuned Model):**

| Metric              | OLMo+SFT | OLMo+SFT+DPO |
|---------------------|----------|--------------|
| MMLU (0-shot)       | 47.3     | 46.1         |
| AlpacaEval (% win)  | 57.0     | 69.3         |
| ToxiGen (% Toxic)   | 14.4     | 1.7          |
| TruthfulQA (% I+T)  | 41.2     | 52.0         |

(OLMo: Accelerating the Science of Language Models, p. 8, Table 4; p. 21, Table 8)

### Intersectional results:
The average (`avg.`) score across the 8 core downstream tasks for OLMo-7B is 69.3 (OLMo: Accelerating the Science of Language Models, p. 6, Table 3). The "Sources Combined" plot in the paper shows the aggregate bits per byte performance across 11 data sources from the Paloma benchmark, where OLMo-7B shows a competitive fit compared to other models (OLMo: Accelerating the Science of Language Models, p. 7-8, Figure 2).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on two different high-performance computing clusters:
*   **LUMI Supercomputer:** Utilized up to 256 nodes, where each node consists of 4x AMD MI250X GPUs with 128GB of memory each (OLMo: Accelerating the Science of Language Models, p. 5).
*   **MosaicML (Databricks) Cluster:** Utilized 27 nodes, where each node consists of 8x NVIDIA A100 GPUs with 40GB of memory each (OLMo: Accelerating the Science of Language Models, p. 5).

At the 7B scale, this hardware setup enabled training with a micro-batch size of 4096 tokens per GPU (OLMo: Accelerating the Science of Language Models, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers take the position that "increased openness of language models is essential for scientific understanding of their abilities and limitations" and that this openness will accelerate research to mitigate potential harms (OLMo: Accelerating the Science of Language Models, p. 10).

*   **Sensitive Data:** The training data likely contains sensitive content such as "toxic language, personal information, and copyrighted text" (OLMo: Accelerating the Science of Language Models, p. 9). To mitigate this, the tokenizer includes special tokens for masking personally identifiable information (PII), though the developers acknowledge that no approach can completely remove such content (OLMo: Accelerating the Science of Language Models, p. 3, 9).
*   **Risks and Mitigation:**
    *   **Misuse:** There is a risk that the model could be "used in unintended ways that cause harm." The developers opted for a permissive license (Apache 2.0) because they believe a stricter license would not remove the overall risk in the field, and that openness is the best option for enabling diverse approaches to understanding and mitigating harms (OLMo: Accelerating the Science of Language Models, p. 10).
    *   **Bias, Toxicity, and Hallucinations:** The pretrained model faces the same issues as other LLMs, including bias, toxicity, and hallucinations. The adapted (instruction-tuned) versions of the model are "better at avoiding these generations, but they are not perfect" (OLMo: Accelerating the Science of Language Models, p. 9). The evaluation framework includes metrics for toxicity (ToxiGen) to measure these risks (OLMo: Accelerating the Science of Language Models, p. 8).
    *   **Environmental Impact:** The developers estimate that pretraining the 7B model on NVIDIA A100 GPUs produced 70 tCO2eq, and on AMD MI250X GPUs (powered by carbon-neutral hydroelectricity) produced 0 tCO2eq (OLMo: Accelerating the Science of Language Models, p. 18, Table 6). They hope that by openly releasing the model, they can reduce future emissions by allowing others to build on their work instead of training from scratch (OLMo: Accelerating the Science of Language Models, p. 10, 16).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Data Limitations:** The model's training data is primarily in English, and its capabilities in other languages are limited (OLMo: Accelerating the Science of Language Models, p. 9). The training data may contain toxic, biased, or copyrighted content despite mitigation efforts (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Evaluation Gaps:** Many of the downstream evaluation tasks are not representative of how users typically interact with language models (e.g., as a chatbot). Furthermore, language model evaluations are described as "very noisy," and comparisons should be taken with a grain of salt (OLMo: Accelerating the Science of Language Models, p. 9-10). Some evaluation tasks were found to have unstable performance trends during development and provide limited signal (OLMo: Accelerating the Science of Language Models, p. 17).
*   **Adaptation Imperfections:** The instruction-tuned versions of the model are improved but not perfect; they can still exhibit bias, toxicity, and hallucinations. The data mixture used for adaptation (TÜLU) was originally designed for a different model family (Llama) and relies on data distilled from other models (OLMo: Accelerating the Science of Language Models, p. 9).

### Recommendations:
*   Users should be aware of the model's limitations and potential to generate harmful or incorrect content. It should not be used for high-stakes applications without rigorous testing and adaptation for the specific use case.
*   The developers recommend using the full open framework (data, code, weights) to conduct further research into the science of language models (OLMo: Accelerating the Science of Language Models, p. 1).
*   Users should be cautious when relying on certain downstream evaluation tasks (e.g., `mrpc`, `wic`) for measuring model performance, as they can be unstable or tied to random chance (OLMo: Accelerating the Science of Language Models, p. 17).