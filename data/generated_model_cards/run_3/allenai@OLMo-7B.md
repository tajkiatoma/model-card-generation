## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a multi-institutional collaboration led by the Allen Institute for Artificial Intelligence (AI2). Other contributing institutions include the University of Washington, Yale University, New York University, and Carnegie Mellon University (OLMo: Accelerating the Science of Language Models, p. 1).

### Model date:
The associated research paper was last updated on June 7, 2024. The model repository includes numerous intermediate checkpoints released throughout the training process, starting from `step0-tokens0B` up to `step557000-tokens2464B`, indicating an ongoing development timeline (OLMo: Accelerating the Science of Language Models, p. 1; revisions.txt).

### Model version:
This model card describes the OLMo-7B model. The OLMo framework also includes other variants, such as a 1B parameter model and a 7B-twin-2T model (OLMo: Accelerating the Science of Language Models, p. 2, 8). Unlike many other models that only release final weights, the OLMo release includes over 500 intermediate checkpoints at intervals of 1000 training steps, allowing for detailed analysis of the model's learning trajectory (OLMo: Accelerating the Science of Language Models, p. 8; revisions.txt). The goal of OLMo is to be a "truly Open Language Model" to enable scientific study, releasing not just model weights but also training data, and training and evaluation code (OLMo: Accelerating the Science of Language Models, p. 1).

### Model type:
OLMo is a decoder-only transformer-based language model designed for causal language modeling (OLMo: Accelerating the Science of Language Models, p. 2; config.json).

**Architecture Details:**
*   **Parameters:** 7 Billion (OLMo: Accelerating the Science of Language Models, p. 2).
*   **Layers:** 32 (`n_layers`) (config.json).
*   **Hidden Size:** 4096 (`d_model`) (config.json).
*   **Attention Heads:** 32 (`n_heads`) (config.json).
*   **MLP Hidden Size:** 22016 (`mlp_hidden_size`) (config.json).
*   **Activation Function:** SwiGLU (`activation_type`) (config.json; OLMo: Accelerating the Science of Language Models, p. 2).
*   **Positional Embeddings:** Rotary Positional Embeddings (RoPE) (`rope: true`) (config.json; OLMo: Accelerating the Science of Language Models, p. 3).
*   **Layer Normalization:** Non-parametric formulation with no affine transformation (`layer_norm_type: "default"`, `layer_norm_with_affine: false`) (config.json; OLMo: Accelerating the Science of Language Models, p. 2).
*   **Biases:** All bias terms are excluded from the architecture to improve training stability (`include_bias: false`) (config.json; OLMo: Accelerating the Science of Language Models, p. 2).
*   **Vocabulary Size:** 50,280 (`vocab_size`) (config.json). The embedding matrix size is increased to 50,304 to be a multiple of 128 for improved throughput (OLMo: Accelerating the Science of Language Models, p. 3).

**Context Length:**
*   The model supports a maximum sequence length of 2048 tokens (`max_sequence_length`) (config.json).

### Training details:
The model was pretrained using a standard next-token prediction objective.

*   **Optimizer:** AdamW optimizer (OLMo: Accelerating the Science of Language Models, p. 3, 5).
    *   Betas: (0.9, 0.95) (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   Epsilon: 1.0e-5 (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   Weight Decay: 0.1 (OLMo: Accelerating the Science of Language Models, p. 17, Table 5).
*   **Learning Rate Schedule:**
    *   Peak Learning Rate: 3.0e-4 (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   Warmup: 5000 steps (OLMo: Accelerating the Science of Language Models, p. 3, Table 1).
    *   Decay: After warmup, the learning rate decays linearly to one-tenth of the peak value (3.0e-5) over the remainder of training (OLMo: Accelerating the Science of Language Models, p. 5, 17).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens (2048 instances of 2048 tokens each) (OLMo: Accelerating the Science of Language Models, p. 3, 4).
*   **Precision:** Mixed-precision training using `amp_bf16` (config.json; OLMo: Accelerating the Science of Language Models, p. 4-5).
*   **Gradient Clipping:** Gradients are clipped such that the total L2-norm of the parameter gradients does not exceed 1.0 (OLMo: Accelerating the Science of Language Models, p. 5).
*   **Framework:** The model was trained using PyTorch's Fully Sharded Data Parallel (FSDP) framework with the ZeRO optimizer strategy to manage memory consumption across GPUs (OLMo: Accelerating the Science of Language Models, p. 4).

### Paper or other resource for more information:
The primary resource for the model is the academic paper:
*   Groeneveld, D., Beltagy, I., Walsh, P., et al. (2024). *OLMo: Accelerating the Science of Language Models*. arXiv:2402.00838v4.

The paper provides a comprehensive overview of the model's architecture, training data, evaluation, and the open-source framework surrounding it. Additional resources, including the official project website, can be found at `https://allenai.org/olmo` (OLMo: Accelerating the Science of Language Models, p. 2).

### Citation details:
```bibtex
@article{OLMo,
  title={{OLMo: Accelerating the Science of Language Models}},
  author={Dirk Groeneveld and Iz Beltagy and Pete Walsh and Akshita Bhagia and Rodney Kinney and Oyvind Tafjord and Ananya Harsh Jha and Hamish Ivison and Ian Magnusson and Yizhong Wang and Shane Arora and David Atkinson and Russell Authur and Khyathi Raghavi Chandu and Arman Cohan and Jennifer Dumas and Yanai Elazar and Yuling Gu and Jack Hessel and Tushar Khot and William Merrill and Jacob Morrison and Niklas Muennighoff and Aakanksha Naik and Crystal Nam and Matthew E. Peters and Valentina Pyatkin and Abhilasha Ravichander and Dustin Schwenk and Saurabh Shah and Will Smith and Emma Strubell and Nishant Subramani and Mitchell Wortsman and Pradeep Dasigi and Nathan Lambert and Kyle Richardson and Luke Zettlemoyer and Jesse Dodge and Kyle Lo and Luca Soldaini and Noah A. Smith and Hannaneh Hajishirzi},
  journal={arXiv preprint arXiv:2402.00838},
  year={2024}
}
```
(OLMo: Accelerating the Science of Language Models, p. 1)

### License:
All model weights and source code are released under the Apache 2.0 License (OLMo: Accelerating the Science of Language Models, p. 2).

### Contact:
For questions, feedback, or issues, contact the development team at `olmo@allenai.org` (OLMo: Accelerating the Science of Language Models, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to serve as a foundational, "truly open language model" to "enable the scientific study of language models" (OLMo: Accelerating the Science of Language Models, p. 1). It is a base model for causal language modeling (next-token prediction) and is intended to be used for:
*   **Research:** To study the behaviors, biases, and capabilities of large language models with full transparency into the training data and process.
*   **Finetuning:** To serve as a base model for adaptation to specific downstream tasks, including the creation of chat assistants and other instruction-following models (OLMo: Accelerating the Science of Language Models, p. 3).

The model takes a sequence of text as input and generates subsequent text.

### Primary intended users:
The primary intended users are members of the open research community, including academics and practitioners in the field of NLP and machine learning (OLMo: Accelerating the Science of Language Models, p. 1, 8).

### Out-of-scope uses:
The model is not intended for deployment in production systems without careful evaluation and finetuning. Specific out-of-scope uses include:
*   **Multilingual Applications:** The model was pretrained primarily on English data and is not designed for use in other languages (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Critical Decision-Making:** As a pretrained model, it is prone to generating biased, toxic, or factually incorrect content (hallucinations) and should not be used for high-stakes applications where this could cause harm (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Malicious Uses:** The model should not be used for applications intended to cause harm, spread misinformation, or engage in other malicious activities (OLMo: Accelerating the Science of Language Models, p. 10).

---

## How to Use
This section outlines how to use the model.

The model can be loaded and used with the `ai2-olmo` library, which is built to integrate with the Hugging Face `transformers` ecosystem (requirements.txt).

Below is a Python code snippet demonstrating how to use the OLMo-7B model for text generation:
```python
# First, install the necessary library
# pip install ai2-olmo

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model from the Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("allenai/olmo-7b")
model = AutoModelForCausalLM.from_pretrained("allenai/olmo-7b")

# Define the input prompt
prompt = "The science of language models is"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
# The model can generate text up to its max sequence length of 2048 tokens.
response = model.generate(**inputs, max_length=100, do_sample=True, top_k=50, top_p=0.95)

# Decode and print the output
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])
```
*(Code example based on standard Hugging Face usage patterns and information from `config.json`, `tokenizer_config.json`, and `requirements.txt`)*

**Sample Output:**
```
The science of language models is a rapidly developing field. The ability to generate human-like text has been a long-standing goal of artificial intelligence research. In recent years, there has been a surge of interest in language models, which are statistical models that can be used to generate text. These models are trained on large amounts of text data and can be used to generate text that is similar to the text that they were trained on.
```
*(Output is a hypothetical example of what the model might generate.)*

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data Distribution:** The model's performance is highly dependent on the similarity between the evaluation data and its training data. The composition of the training data (e.g., the proportion of web text, code, and academic papers) significantly influences its capabilities on different domains (OLMo: Accelerating the Science of Language Models, p. 7).
*   **Language:** The model is primarily trained on English text, and its performance on other languages is not evaluated and expected to be poor (OLMo: Accelerating the Science of Language Models, p. 9).

### Evaluation factors:
The model's performance was evaluated across different text domains and data sources. The primary evaluation factor reported is the source of the text, using benchmarks like Paloma which is composed of 18 distinct data sources (e.g., C4, Wikipedia, Reddit, GitHub) (OLMo: Accelerating the Science of Language Models, p. 6, 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a variety of metrics:
*   **Downstream Task Performance:** Zero-shot accuracy on a suite of commonsense reasoning and question-answering tasks. The evaluation uses a rank classification approach where the model ranks multiple-choice options by their likelihood (OLMo: Accelerating the Science of Language Models, p. 6).
*   **Intrinsic Language Modeling:** Perplexity, reported in bits per byte (BPB), on the Paloma benchmark to measure how well the model fits various text distributions (OLMo: Accelerating the Science of Language Models, p. 6).
*   **Instruction Following and Safety (for adapted models):**
    *   **MMLU:** 0-shot accuracy for multitask understanding (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **AlpacaEval:** Win-rate against a baseline model, judged by GPT-4 (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **ToxiGen:** The percentage of generated responses classified as toxic, used to measure model safety (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).
    *   **TruthfulQA:** The percentage of responses that are both informative and truthful (OLMo: Accelerating the Science of Language Models, p. 8, Table 4).

### Decision thresholds:
For most downstream evaluations, which are formulated as multiple-choice questions, decisions are based on ranking the likelihood of candidate answers rather than using a fixed threshold (OLMo: Accelerating the Science of Language Models, p. 6). For the ToxiGen evaluation, a separate RoBERTa-based classifier is used to identify toxic content, which implies an internal decision threshold, but the specific value is not reported (OLMo: Accelerating the Science of Language Models, p. 20).

### Variation approaches:
Model performance was measured at regular intervals throughout training. Evaluations were run every 1000 training steps on intermediate checkpoints to provide a continuous signal on model quality and to analyze performance trends as a function of tokens seen (OLMo: Accelerating the Science of Language Models, p. 4, 7).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of publicly available datasets:
*   **Core Downstream Tasks:** A suite of 8 tasks including `arc` (easy and challenge), `boolq`, `openbookqa`, `sciq`, `hellaswag`, `piqa`, and `winogrande` (OLMo: Accelerating the Science of Language Models, p. 5).
*   **Auxiliary Downstream Tasks:** 6 additional tasks including `headqa_en`, `logiqa`, `mrpc`, `qnli`, `wic`, and `wnli` (OLMo: Accelerating the Science of Language Models, p. 17).
*   **Perplexity Benchmark (Paloma):** This benchmark includes 585 text domains from 18 sources. The paper reports detailed results on 11 publicly available sources: C4, mC4-en, Wikitext-103, Penn Treebank, RedPajama, Falcon-RefinedWeb, Dolma, M2D2 S2ORC, M2D2 Wikipedia, C4 100 domains, and Dolma 100 Subreddits (OLMo: Accelerating the Science of Language Models, p. 6).
*   **Adaptation Evaluation Suite (TÜLU):** This includes datasets like `MMLU`, `AlpacaEval`, `ToxiGen`, and `TruthfulQA` to assess the performance of instruction-tuned models (OLMo: Accelerating the Science of Language Models, p. 4, 8).

### Motivation:
*   The core downstream tasks were selected at the beginning of development due to their "naturalness" (all can be formulated as text completion) and their "ability to provide meaningful signals throughout training" (OLMo: Accelerating the Science of Language Models, p. 4).
*   The Paloma benchmark was chosen to measure the model's fit on out-of-distribution data and because it supports explicit decontamination, allowing for a more controlled scientific evaluation (OLMo: Accelerating the Science of Language Models, p. 4).
*   The TÜLU suite was used to "showcase the efficacy of using OLMo as a base for further fine-tuning" on chat capabilities and safety (OLMo: Accelerating the Science of Language Models, p. 4).

### Preprocessing:
A key preprocessing step for the evaluation was decontamination. For the Paloma perplexity benchmark, any document in the pretraining data that contained paragraphs from the Paloma evaluation set was removed. This was done to prevent data leakage and ensure that the evaluation accurately reflects the model's out-of-sample generalization performance (OLMo: Accelerating the Science of Language Models, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was pretrained on **Dolma**, a large-scale, open, and diverse multi-source corpus created for this project. The full corpus contains approximately 3 trillion tokens, and the OLMo-7B model was trained on a 2.46 trillion token sample from it (OLMo: Accelerating the Science of Language Models, p. 3, 5). The full Dolma dataset is publicly available (OLMo: Accelerating the Science of Language Models, p. 9).

The composition of the full Dolma corpus is as follows:
| Source | Type | Tokens (billions) |
| :--- | :--- | :--- |
| Common Crawl | Web pages | 2,180 |
| GitHub | Code | 342 |
| Reddit | Social media | 80 |
| Semantic Scholar | Papers | 57 |
| Project Gutenberg | Books | 5.2 |
| Wikipedia | Encyclopedic | 3.7 |
| **Total** | | **2,668** |
(OLMo: Accelerating the Science of Language Models, p. 3, Table 2)

### Motivation:
The Dolma dataset was created to "facilitate open research on language model pretraining" (OLMo: Accelerating the Science of Language Models, p. 3). The data sources were chosen because they are commonly used in large-scale pretraining and are accessible to the general public, enabling reproducibility and further study on how training data impacts model capabilities (OLMo: Accelerating the Science of Language Models, p. 3).

### Preprocessing:
The Dolma corpus was constructed using a comprehensive pipeline that included:
1.  **Language filtering**
2.  **Quality filtering**
3.  **Content filtering**
4.  **Deduplication**
5.  **Multi-source mixing**
6.  **Tokenization**

(OLMo: Accelerating the Science of Language Models, p. 3)

The tokenizer is a modified version of the BPE-based tokenizer from GPT-NeoX-20B, with additional special tokens added for masking personally identifiable information (PII) such as `|||IP_ADDRESS|||`, `|||EMAIL_ADDRESS|||`, and `|||PHONE_NUMBER|||` (OLMo: Accelerating the Science of Language Models, p. 3; tokenizer_config.json). For training, documents were concatenated with a special `<|endoftext|>` token appended to each, and then grouped into consecutive chunks of 2048 tokens to form training instances (OLMo: Accelerating the Science of Language Models, p. 5; special_tokens_map.json).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of OLMo-7B is reported for individual tasks and data domains.
*   **Downstream Tasks:** Zero-shot accuracy on 8 core tasks is presented in Table 3. For example, OLMo-7B achieves 48.5 on `arc_challenge`, 73.4 on `boolq`, and 76.4 on `hellaswag` (OLMo: Accelerating the Science of Language Models, p. 6, Table 3). Results for 6 additional tasks are in Table 7 (OLMo: Accelerating the Science of Language Models, p. 18).
*   **Perplexity:** Bits per byte (BPB) scores for 11 individual data sources from the Paloma benchmark are shown in Figure 2. The model performs particularly well on C4, which is closely related to its Common Crawl training data (OLMo: Accelerating the Science of Language Models, p. 8, Figure 2).
*   **Adapted Model Performance:** Performance on individual metrics for the finetuned models is available. For example, after SFT and DPO, OLMo-7B achieves a 46.1 on MMLU, a 1.7% toxic generation rate on ToxiGen, and a 52.0% score on TruthfulQA (OLMo: Accelerating the Science of Language Models, p. 21, Table 8).

### Intersectional results:
The paper provides an aggregated performance metric for the Paloma benchmark, combining results across 11 different data sources. This gives a broad measure of the model's generalization capability (OLMo: Accelerating the Science of Language Models, p. 8, Figure 2, "Sources Combined" subplot). No other intersectional results (e.g., across demographic factors) are provided.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on two different large-scale GPU clusters:
*   **LUMI Supercomputer:** Utilized up to 256 nodes, where each node consists of 4x AMD MI250X GPUs, each with 128GB of memory (OLMo: Accelerating the Science of Language Models, p. 5).
*   **MosaicML (Databricks) Cluster:** Utilized 27 nodes, where each node consists of 8x NVIDIA A100 GPUs, each with 40GB of memory (OLMo: Accelerating the Science of Language Models, p. 5).

Training at the 7B scale required a micro-batch size of 4096 tokens per GPU (OLMo: Accelerating the Science of Language Models, p. 4). The total power consumption for pretraining was estimated to be between 104 MWh (on A100s) and 135 MWh (on MI250Xs) (OLMo: Accelerating the Science of Language Models, p. 18, Table 6).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Sensitive Data:** The training data, sourced from public web crawls and other large corpora, "likely contains problematic content like toxic language, personal information, and copyrighted text" (OLMo: Accelerating the Science of Language Models, p. 9). Mitigation efforts included adding special tokens to the tokenizer to mask PII, though the developers acknowledge that "no perfect approaches today... can completely remove such content" (OLMo: Accelerating the Science of Language Models, p. 3, 9).
*   **Risks and Mitigation:**
    *   **Risks:** The pretrained model is subject to common LLM risks such as "bias, toxicity and, hallucinations" (OLMo: Accelerating the Science of Language Models, p. 9). There is also a risk that the model could be "used in unintended ways that cause harm" (OLMo: Accelerating the Science of Language Models, p. 10).
    *   **Mitigation Strategy:** The primary mitigation strategy is the model's openness. The developers argue that providing full access to the model, data, and code will "accelerate research and development efforts to understand and mitigate those potential harms" by enabling a diversity of analyses from the broader community (OLMo: Accelerating the Science of Language Models, p. 10). Additionally, the release of finetuned "adapted models" demonstrates that safety can be improved (e.g., toxicity is reduced from 81.4% to 1.7% in the base vs. DPO-tuned model) (OLMo: Accelerating the Science of Language Models, p. 21, Table 8).
*   **Fraught Use Cases:** The paper does not specify particular use cases that are especially fraught but warns generally against misuse. The evaluation includes performance on data from fringe online communities known for hate speech (e.g., Manosphere, Gab, 4chan), acknowledging the need to understand model behavior on such text (OLMo: Accelerating the Science of Language Models, p. 16).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Data Limitations:** The model is pretrained on English-language data and is not suitable for multilingual contexts. The training data may still contain toxic, biased, or private information despite mitigation efforts (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Model Limitations:** The pretrained model can generate harmful, biased, or factually incorrect content. While finetuning improves performance and safety, the resulting adapted models are "not perfect" (OLMo: Accelerating the Science of Language Models, p. 9).
*   **Evaluation Gaps:** Many of the downstream evaluation tasks are not representative of real-world user interactions (e.g., chatbot conversations). Furthermore, language model evaluations are described as "very noisy," and some auxiliary evaluation tasks were found to have unstable performance during training, providing a limited signal for development (OLMo: Accelerating the Science of Language Models, p. 9, 17).

### Recommendations:
*   Users should not deploy the base model in user-facing applications without significant finetuning and safety evaluations.
*   Researchers are encouraged to use the full suite of released artifacts (model checkpoints, training data, code) to conduct studies on the science of language models (OLMo: Accelerating the Science of Language Models, p. 1).
*   Users should be cautious when interpreting performance on certain auxiliary evaluation tasks (e.g., `mrpc`, `wic`, `wnli`), as they were found to be less stable and reliable during model development (OLMo: Accelerating the Science of Language Models, p. 17).
*   When adapting OLMo for instruction-following tasks, users should consider that it may require different data mixtures for finetuning compared to other models like Llama, for which many existing datasets were designed (OLMo: Accelerating the Science of Language Models, p. 9).