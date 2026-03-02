## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a large team of researchers primarily from the Allen Institute for Artificial Intelligence (AI2), with collaborators from the University of Washington, Yale University, New York University, and Carnegie Mellon University (Paper, Page 1). The full list of authors includes Dirk Groeneveld, Iz Beltagy, Pete Walsh, and many others, with contact available at `olmo@allenai.org` (Paper, Page 1).

### Model date:
The associated academic paper is dated June 7, 2024 (Paper, Page 1). The paper describes this as the "first release of OLMo" and mentions that since the original release, the data and training setup have been improved (Paper, Page 9). The model includes over 500 intermediate checkpoints released at intervals of 1000 training steps (Paper, Page 8; checkpoints.txt).

### Model version:
This model card describes the OLMo-7B model. The OLMo framework also includes other variants, such as a 1B model and a 7B-twin-2T model (Paper, Page 2, 8). The model was developed using Transformers version 4.36.2 (config.json). The OLMo project is a "truly Open Language Model" framework, which, unlike many prior efforts, releases not only model weights and inference code but also the training data, training logs, evaluation code, and numerous intermediate checkpoints to enable scientific study (Paper, Page 1).

### Model type:
OLMo-7B is a decoder-only transformer-based language model designed for causal language modeling (Paper, Page 2; config.json).

**Architecture Details:**
*   **Model Architecture:** `OLMoForCausalLM` (config.json).
*   **Parameters:** 7 billion (Paper, Page 2).
*   **Layers:** 32 (`n_layers`) (config.json; Paper, Page 3).
*   **Attention Heads:** 32 (`n_heads`) (config.json; Paper, Page 3).
*   **Hidden Dimension:** 4096 (`d_model`) (config.json; Paper, Page 3).
*   **MLP Hidden Size:** 22016 (`mlp_hidden_size`) (config.json).
*   **Activation Function:** SwiGLU (`activation_type`) (config.json; Paper, Page 2).
*   **Layer Normalization:** Non-parametric layer norm with no adaptive gain or bias (`layer_norm_type: "default"`, `layer_norm_with_affine: false`) (config.json; Paper, Page 2).
*   **Biases:** All bias terms are excluded from the architecture to improve training stability (`include_bias: false`) (config.json; Paper, Page 2).
*   **Positional Embeddings:** Rotary Positional Embeddings (RoPE) are used instead of absolute positional embeddings (`rope: true`) (config.json; Paper, Page 3).
*   **Vocabulary Size:** 50,280, with the embedding matrix size increased to 50,304 (a multiple of 128) to maximize training throughput (config.json; Paper, Page 3).
*   **Context Length:** 2048 tokens (`max_sequence_length`) (config.json).

### Training details:
The model was pretrained on 2.46 trillion tokens from the Dolma dataset (Paper, Page 3).

*   **Optimizer:** AdamW with betas of 0.9 and 0.95, and an epsilon of 1.0E-5 (Paper, Page 3, 5).
*   **Learning Rate Schedule:** The learning rate was warmed up over 5000 steps to a peak of 3.0E-4. After the warmup, it was decayed linearly to one-tenth of the peak learning rate (3.0E-5) over the remainder of training (Paper, Page 3, 5; Paper, Page 17, Table 5).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens was used (Paper, Page 4).
*   **Precision:** Mixed-precision training (`amp_bf16`) was employed, with most operations running in `bfloat16` and certain operations like softmax running in full precision for stability (config.json; Paper, Page 4-5).
*   **Gradient Clipping:** Gradients were clipped such that the total L2-norm of the parameter gradients does not exceed 1.0 (Paper, Page 5).
*   **Distributed Training:** The model was trained using PyTorch's Fully Sharded Data Parallel (FSDP) framework with the ZeRO optimizer strategy (Paper, Page 4).

### Paper or other resource for more information:
The primary resource is the academic paper: "OLMo: Accelerating the Science of Language Models" by Dirk Groeneveld, Iz Beltagy, Pete Walsh, et al. (Paper, Page 1).

The paper also refers to several other key resources that are part of the OLMo framework release:
*   **Dolma Dataset:** The open pretraining dataset and its accompanying report (Soldaini et al., 2024) (Paper, Page 2).
*   **Catwalk:** The framework used for downstream and intrinsic evaluation (Groeneveld et al., 2023) (Paper, Page 2).
*   **Paloma:** The perplexity-based evaluation benchmark (Magnusson et al., 2023) (Paper, Page 2).
*   **Open Instruct:** The framework used for instruction tuning and adaptation (Ivison et al., 2023) (Paper, Page 2).

### Citation details:
To cite the model and its framework, please use the following information from the research paper:
*   **Title:** OLMo: Accelerating the Science of Language Models
*   **Authors:** Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, and others.
*   **arXiv ID:** arXiv:2402.00838v4 [cs.CL] (Paper, Page 1).

### License:
All code and weights for the OLMo model are released under the Apache 2.0 License (Paper, Page 2).

### Contact:
For questions, feedback, or to report issues, contact the development team at `olmo@allenai.org` (Paper, Page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to enable the scientific study of language models by providing a truly open model and framework (Paper, Page 1). It is a foundational, pretrained causal language model intended to serve as a base for further research and fine-tuning (Paper, Page 3). It can be adapted for specific downstream applications, such as being trained into a general chat assistant (Paper, Page 3). The model's core capability is to predict the next token in a sequence of text.

### Primary intended users:
The primary intended users are the open research community, including academics and practitioners in the field of NLP and AI (Paper, Page 1, 8). The release is designed to empower this community to study model behaviors, capabilities, biases, and risks with full access to training data, code, and intermediate checkpoints (Paper, Page 1).

### Out-of-scope uses:
The model is not intended for deployment in production systems without significant further fine-tuning and safety evaluations. The developers acknowledge that the pretrained model faces issues such as bias, toxicity, and hallucinations (Paper, Page 9). The training data is primarily in English, making the model unsuitable for use in other languages (Paper, Page 9). The developers also state that "openness is not without risk; the possibility remains that these models will be used in unintended ways that cause harm" (Paper, Page 10).

---

## How to Use
This section outlines how to use the model.

To use the OLMo-7B model, you need to have the `ai2-olmo>=0.2.2` library installed, along with its dependencies like `transformers` (requirements.txt). The model can be loaded using the Hugging Face `transformers` library.

Here is a code snippet demonstrating how to load the model and tokenizer and generate text:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model from the Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")
model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")

# Input text for generation
prompt = "The discovery of the Higgs boson was a significant milestone in"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
# The model can be used with various generation strategies like greedy decoding, sampling, etc.
# Here's a simple example using the generate method.
outputs = model.generate(**inputs, max_length=50)

# Decode and print the output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
(Derived from code_snippets.txt, config.json, and standard Hugging Face usage patterns)

The model uses special tokens for padding (`<|padding|>`) and end-of-text (`<|endoftext|>`) (special_tokens_map.json; tokenizer.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Pretraining Data Composition:** The model's performance is influenced by the composition of its pretraining data (Dolma) and its similarity to the target evaluation domains. For example, the model performs well on evaluations predominated by Common Crawl data, which makes up a large portion of its training set (Paper, Page 7, 8).
*   **Language:** The model was pretrained almost exclusively on English text, so its performance will be poor or non-existent for other languages (Paper, Page 9).
*   **Data Preprocessing:** Preprocessing decisions, such as how code data is cleaned or how semantic deduplication is applied, can impact model performance on specific domains (Paper, Page 7).

### Evaluation factors:
The model was evaluated across a variety of factors:
*   **Task Domain:** Performance was measured on commonsense reasoning tasks (e.g., `arc`, `piqa`), intrinsic language modeling across diverse text domains (e.g., web pages, academic papers, social media via the Paloma benchmark), and chat/instruction-following capabilities after adaptation (Paper, Page 4, 6, 8).
*   **Safety and Truthfulness:** After fine-tuning, the model was evaluated for toxicity generation (ToxiGen) and its ability to produce informative and truthful responses (TruthfulQA) (Paper, Page 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Downstream Task Evaluation:** Zero-shot accuracy is the primary metric. This is measured using a rank classification approach where the model ranks candidate text completions by their likelihood (Paper, Page 6).
*   **Intrinsic Language Modeling:** Bits per byte (BPB) is used to measure perplexity on the Paloma benchmark. This allows for fair comparison between models with different vocabularies (Paper, Page 6).
*   **Adaptation Evaluation:** A suite of metrics is used for the instruction-tuned models, including:
    *   **MMLU:** 0-shot accuracy for massive multitask language understanding (Paper, Page 8, Table 4).
    *   **AlpacaEval:** Win rate (%) against a baseline model, as judged by GPT-4 (Paper, Page 8, 21).
    *   **ToxiGen:** The percentage of generated responses deemed toxic by a classifier (% Toxic, lower is better) (Paper, Page 8, 20).
    *   **TruthfulQA:** The percentage of responses that are both informative and truthful (% Info+True) (Paper, Page 8, 21).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For downstream task evaluation, different likelihood normalization strategies were selected for each dataset to ensure robust measurements. For example, unconditional likelihood normalization was used for `arc` and `openbookqa`, while per-token normalization was used for `hellaswag`, `piqa`, and `winogrande` (Paper, Page 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public datasets:
*   **Core Downstream Tasks:** A suite of 8 commonsense reasoning tasks: `arc` (easy and challenge), `boolq`, `openbookqa`, `sciq`, `hellaswag`, `piqa`, and `winogrande` (Paper, Page 5).
*   **Additional Downstream Tasks:** 6 additional tasks were also used: `headqa_en`, `logiqa`, `mrpc`, `qnli`, `wic`, and `wnli` (Paper, Page 17).
*   **Intrinsic Evaluation (Perplexity):** The Paloma benchmark, which contains 585 text domains from 18 sources. The reported aggregate results use a subset of 11 publicly available sources, including C4, mC4-en, Wikitext 103, RedPajama, and Dolma (Paper, Page 4, 6).
*   **Adaptation Evaluation:** The TÜLU evaluation suite was used, which includes benchmarks like MMLU, GSM8k, BBH, TydiQA, Codex-Eval, AlpacaEval, ToxiGen, and TruthfulQA (Paper, Page 4, 21).

### Motivation:
The core downstream tasks were chosen at the beginning of development due to their "naturalness" (they can be formulated as text completion) and their "ability to provide meaningful signals throughout training" (Paper, Page 4). The Paloma benchmark was chosen to measure how the model fits language distributions beyond its training data, across a wide and stratified set of domains (Paper, Page 4). The adaptation evaluation suite was chosen to assess the model's chat capabilities and safety after fine-tuning (Paper, Page 4).

### Preprocessing:
For the Paloma perplexity evaluation, the evaluation data was explicitly decontaminated from the model's pretraining data. Any pretraining document containing paragraphs that also appeared in the Paloma evaluation set was removed to ensure a fair out-of-sample fit measurement (Paper, Page 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on **Dolma**, a diverse, multi-source corpus of three trillion tokens that is publicly available (Paper, Page 3, 9). The OLMo-7B model was trained on a 2.46 trillion token sample from this dataset (Paper, Page 3).

The composition of the full Dolma dataset is as follows:
*   **Common Crawl (web pages):** 2,180 billion tokens
*   **GitHub (code):** 342 billion tokens
*   **Reddit (social media):** 80 billion tokens
*   **Semantic Scholar (papers):** 57 billion tokens
*   **Project Gutenberg (books):** 5.2 billion tokens
*   **Wikipedia (encyclopedic):** 3.7 billion tokens
(Paper, Page 3, Table 2)

### Motivation:
The Dolma dataset was created "to facilitate open research on language model pretraining." The data sources were chosen because they are (1) commonly used in large-scale language model pretraining and (2) accessible to the general public (Paper, Page 3).

### Preprocessing:
The Dolma dataset was constructed using a six-stage pipeline: (1) language filtering, (2) quality filtering, (3) content filtering, (4) deduplication, (5) multi-source mixing, and (6) tokenization (Paper, Page 3).

For model training, the data was prepared as follows:
*   A special end-of-sentence (EOS) token (`<|endoftext|>`) was appended to each document (Paper, Page 5).
*   The documents were concatenated together.
*   The concatenated text was grouped into consecutive chunks of 2048 tokens to form training instances (Paper, Page 5).
*   The training instances were shuffled in a reproducible manner for each training run (Paper, Page 5).
*   The text was tokenized using a modified BPE-based tokenizer from GPT-NeoX-20B, which includes special tokens for masking personally identifiable information (PII) (Paper, Page 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
*   **Core Downstream Tasks:** Zero-shot accuracy for OLMo-7B on 8 core tasks is presented in Table 3. For example, it achieves 48.5 on `arc_challenge`, 73.4 on `boolq`, 76.4 on `hellaswag`, and an average of 69.3 (Paper, Page 6).
*   **Intrinsic Evaluation:** Figure 2 shows the bits per byte performance on 11 individual data sources from the Paloma benchmark. The model performs particularly well on C4, where it overtakes other models, likely due to the high percentage of Common Crawl data in its training set (Paper, Page 8).
*   **Adaptation Evaluation:** Table 4 and Table 8 show performance on various instruction-tuning benchmarks. The base OLMo-7B model scores 28.3 on MMLU (0-shot). After supervised fine-tuning (SFT), this increases to 47.3. After DPO, it is 46.1 (Paper, Page 8, 21). On ToxiGen, the toxicity rate drops from 81.4% for the base model to 1.7% for the SFT+DPO model (Paper, Page 21).

### Intersectional results:
The "Sources Combined" subplot in Figure 2 presents the aggregate performance (bits per byte) across 11 data sources from the Paloma benchmark, comparing OLMo-7B's scaling trend against other 7B-scale models. The results show that OLMo has a competitive fit, especially given its training data was explicitly decontaminated against the benchmark (Paper, Page 7, 8).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on two different GPU clusters to ensure the codebase could be used on both NVIDIA and AMD hardware (Paper, Page 5).

*   **Hardware:**
    *   **LUMI Supercomputer:** Up to 256 nodes, each with 4x AMD MI250X GPUs (128GB of memory per GPU module) and 800Gbps interconnect (Paper, Page 5).
    *   **MosaicML (Databricks) Cluster:** 27 nodes, each with 8x NVIDIA A100 GPUs (40GB of memory per GPU) and 800Gbps interconnect (Paper, Page 5).
*   **Framework:** Training used PyTorch's FSDP framework, which enables training at the 7B scale with a micro-batch size of 4096 tokens per GPU (Paper, Page 4).
*   **Energy Consumption:** Pretraining the 7B model on the AMD MI250X cluster consumed an estimated 135 MWh of energy. On the NVIDIA A100 cluster, it consumed an estimated 104 MWh (Paper, Page 18, Table 6).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Sensitive Data:** The developers acknowledge that the large-scale training data "likely contains problematic content like toxic language, personal information, and copyrighted text." They state that this was mitigated to the best of their ability, but "there are no perfect approaches today that can completely remove such content" (Paper, Page 9). The tokenizer was specifically modified with additional tokens to mask PII (e.g., IP addresses, email addresses, phone numbers) (Paper, Page 3; tokenizer_config.json).
*   **Risks and Harms:** The pretrained model is subject to known risks of large language models, including "bias, toxicity and, hallucinations" (Paper, Page 9). The developers also acknowledge the risk that the open-source models could be "used in unintended ways that cause harm" (Paper, Page 10).
*   **Risk Mitigation Strategy:** The primary mitigation strategy is openness. The developers argue that releasing the entire framework (data, code, weights, checkpoints) is "essential for scientific understanding of their abilities and limitations" and accelerates research efforts to "understand and mitigate those potential harms" by allowing a diversity of approaches and analyses (Paper, Page 10). They also release adapted (instruction-tuned) models which are "better at avoiding these generations, but they are not perfect" (Paper, Page 9).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Language Limitation:** The model is trained primarily on English data and is not suitable for use in other languages (Paper, Page 9).
*   **Evaluation Gaps:** The developers note that many standard downstream evaluations are "not actually representative of how users interact with language models (i.e., as a chatbot)" (Paper, Page 9). Furthermore, language model evaluations are "currently very noisy," and comparisons should be taken with a grain of salt (Paper, Page 9-10). Some evaluation tasks were found to be unstable during training, providing limited signal (Paper, Page 17).
*   **Adaptation Limitations:** The instruction-tuning data mixture used (TÜLU) was originally designed for the Llama model family, and OLMo may require a different data mix to better suit its unique characteristics. The mixture also relies on data distilled from other models (Paper, Page 9).
*   **Known Issues:** The base model can generate biased, toxic, or factually incorrect (hallucinated) content. While the adapted models are better, they are not perfect (Paper, Page 9).

### Recommendations:
*   Users should not deploy the base model in user-facing applications without extensive fine-tuning and safety testing.
*   The model and its associated artifacts are intended for research purposes to advance the scientific understanding of language models (Paper, Page 1).
*   Researchers are encouraged to use the provided intermediate checkpoints and training data to study model behavior throughout the training process (Paper, Page 1).
*   Users should be aware of the model's limitations and potential for generating harmful content, and implement appropriate safeguards for any application.