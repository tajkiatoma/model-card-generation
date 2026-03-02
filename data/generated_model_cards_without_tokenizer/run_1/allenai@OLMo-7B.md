## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a large team of researchers primarily from the Allen Institute for Artificial Intelligence (AI2), with collaborators from the University of Washington, Yale University, New York University, and Carnegie Mellon University (2402.00838.pdf, p. 1). The project, named OLMo (Open Language Model), aims to provide a powerful, truly open language model to the research community to enable the scientific study of language models (2402.00838.pdf, p. 1).

### Model date:
The academic paper describing the model was submitted to arXiv, with the latest version (v4) dated June 7, 2024 (2402.00838.pdf, p. 1). The project involves the release of not just the final model, but also hundreds of intermediate checkpoints at intervals of 1000 training steps (2402.00838.pdf, p. 8; revisions.txt).

### Model version:
The repository contains multiple model variants, primarily OLMo-1B and OLMo-7B (2402.00838.pdf, p. 2). The main OLMo-7B model was trained for 2.46 trillion tokens (2402.00838.pdf, p. 3, Table 1). A key feature of the OLMo project is the release of over 500 intermediate checkpoints for its models, available as revisions, allowing for detailed analysis of the model's state throughout the training process (2402.00838.pdf, p. 8; revisions.txt). The repository also includes adapted versions of the model, such as OLMo+SFT and OLMo+SFT+DPO, which are fine-tuned for instruction following and safety (2402.00838.pdf, p. 8).

### Model type:
OLMo is a decoder-only transformer-based language model designed for causal language modeling (2402.00838.pdf, p. 2; modeling_olmo.py). The model architecture is specified in the `config.json.txt` file and the associated paper.

**OLMo-7B Architecture Details:**
*   **Parameters:** 7 billion (2402.00838.pdf, p. 2).
*   **Layers (`n_layers`):** 32 (config.json.txt; 2402.00838.pdf, p. 3, Table 1).
*   **Hidden Size (`d_model`):** 4096 (config.json.txt; 2402.00838.pdf, p. 3, Table 1).
*   **Attention Heads (`n_heads`):** 32 (config.json.txt; 2402.00838.pdf, p. 3, Table 1).
*   **MLP Hidden Size (`mlp_hidden_size`):** 22016 (config.json.txt).
*   **Vocabulary Size (`vocab_size`):** 50280 (config.json.txt). The embedding matrix size is increased to 50304 to be a multiple of 128 for better throughput (2402.00838.pdf, p. 3).
*   **Context Length (`max_sequence_length`):** 2048 tokens (config.json.txt; 2402.00838.pdf, p. 4).

**Architectural Features:**
*   **No Biases:** All bias terms are excluded from the architecture to improve training stability (2402.00838.pdf, p. 2).
*   **Non-parametric Layer Norm:** Uses a layer norm formulation without adaptive gain or bias (2402.00838.pdf, p. 2).
*   **SwiGLU Activation:** Employs the SwiGLU activation function instead of ReLU (config.json.txt; 2402.00838.pdf, p. 2).
*   **Rotary Positional Embeddings (RoPE):** Uses RoPE instead of absolute positional embeddings (2402.00838.pdf, p. 3).
*   **Tokenizer:** A modified BPE-based tokenizer from GPT-NeoX-20B with additional tokens for masking personally identifiable information (PII) (2402.00838.pdf, p. 3).

### Training details:
The model was trained using a supervised, next-token prediction objective (2402.00838.pdf, p. 2).
*   **Optimizer:** AdamW with β1=0.9, β2=0.95, and ε=1.0e-5 (2402.00838.pdf, p. 3, Table 1; 2402.00838.pdf, p. 17, Table 5).
*   **Learning Rate Schedule:** For the 7B model, the peak learning rate is 3.0e-4, with a warmup over 5000 steps. After warmup, the learning rate decays linearly to one-tenth of the peak rate (3.0e-5) over the remainder of training (2402.00838.pdf, p. 3, Table 1; 2402.00838.pdf, p. 5).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens was used (2048 instances of 2048 tokens each) (2402.00838.pdf, p. 4).
*   **Precision:** Mixed-precision training with `bfloat16` was employed to improve throughput, with certain operations like softmax kept in full precision for stability (config.json.txt; 2402.00838.pdf, p. 5).
*   **Gradient Clipping:** Gradients are clipped such that the total L2-norm of the parameter gradients does not exceed 1.0 (2402.00838.pdf, p. 5; 2402.00838.pdf, p. 17, Table 5).
*   **Framework:** The model was trained using PyTorch's Fully Sharded Data Parallel (FSDP) framework with the ZeRO optimizer strategy to manage memory consumption (2402.00838.pdf, p. 4).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Groeneveld, D., Beltagy, I., Walsh, P., et al. (2024). *OLMo: Accelerating the Science of Language Models*. arXiv preprint arXiv:2402.00838. This paper details the entire OLMo framework, including the model architecture, training data, evaluation, and ethical considerations (2402.00838.pdf).

The official project website is also available:
*   `https://allenai.org/olmo` (2402.00838.pdf, p. 2).

### Citation details:
```bibtex
@misc{groeneveld2024olmo,
      title={OLMo: Accelerating the Science of Language Models}, 
      author={Dirk Groeneveld and Iz Beltagy and Pete Walsh and Akshita Bhagia and Rodney Kinney and Oyvind Tafjord and Ananya Harsh Jha and Hamish Ivison and Ian Magnusson and Yizhong Wang and Shane Arora and David Atkinson and Russell Authur and Khyathi Raghavi Chandu and Arman Cohan and Jennifer Dumas and Yanai Elazar and Yuling Gu and Jack Hessel and Tushar Khot and William Merrill and Jacob Morrison and Niklas Muennighoff and Aakanksha Naik and Crystal Nam and Matthew E. Peters and Valentina Pyatkin and Abhilasha Ravichander and Dustin Schwenk and Saurabh Shah and Will Smith and Emma Strubell and Nishant Subramani and Mitchell Wortsman and Pradeep Dasigi and Nathan Lambert and Kyle Richardson and Luke Zettlemoyer and Jesse Dodge and Kyle Lo and Luca Soldaini and Noah A. Smith and Hannaneh Hajishirzi},
      year={2024},
      eprint={2402.00838},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(2402.00838.pdf, p. 1)

### License:
All code and model weights are released under the Apache 2.0 License (2402.00838.pdf, p. 2).

### Contact:
For questions, issues, or feedback, contact the development team at `olmo@allenai.org` (2402.00838.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to serve as a "powerful, truly open language model" to enable and accelerate the scientific study of language models by the research community (2402.00838.pdf, p. 1). It is a foundational, pretrained model intended to be a base for further research and fine-tuning. For example, it can be fine-tuned to become a general chat assistant or adapted for other downstream applications (2402.00838.pdf, p. 3). As a causal language model, its core capability is next-token prediction, which can be used for text generation.

### Primary intended users:
The primary intended users are the open research community, including academics and practitioners, who require full access to model weights, training data, and development tools to study the strengths, weaknesses, biases, and risks of large language models (2402.00838.pdf, p. 1, 8).

### Out-of-scope uses:
The model is not intended for deployment in high-stakes scenarios without significant further fine-tuning and safety testing. The pretrained base model is known to have issues such as bias, toxicity, and hallucinations (2402.00838.pdf, p. 9). The developers acknowledge the risk that the model could be used in "unintended ways that cause harm" (2402.00838.pdf, p. 10). As the model was pretrained primarily on English data, its use for other languages is out-of-scope (2402.00838.pdf, p. 9).

---

## How to Use
This section outlines how to use the model.

The model is designed to be used with the Hugging Face Transformers library (config.json.txt). The required Python packages are listed in `requirements.txt`, including `ai2-olmo>=0.2.2`.

Below is a sample code snippet for using the OLMo-7B model for text generation:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model from the Hugging Face Hub
# Replace "allenai/OLMo-7B" with the specific model version you want to use.
# You can also specify a revision for an intermediate checkpoint, e.g., revision="step1000-tokens4B"
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")
model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")

# Input text
prompt = "The science of language models is"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
# The model can be used with various generation strategies.
# Here is a simple example with max_length.
outputs = model.generate(**inputs, max_length=50)

# Decode and print the output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
*(This code is constructed based on the model architecture (`OLMoForCausalLM`), auto_map configuration in `config.json.txt`, and standard Hugging Face Transformers usage patterns.)*

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Text Domain:** The model's performance varies significantly across different text domains. It performs best on in-distribution data (like Common Crawl) and is less sample efficient on sources less related to scraped web text, such as curated sources like Wikipedia or academic papers (2402.00838.pdf, p. 7).
*   **Linguistic Dialect:** The paper mentions specific datasets for targeted analyses of performance disparities between different dialects of English, such as TwitterAAE (African-American English) and ICE (International Corpus of English), suggesting dialect is a relevant factor (2402.00838.pdf, p. 16).
*   **Data Curation:** Pretraining data composition, quality filtering, and deduplication strategies are identified as key factors that influence model capabilities (2402.00838.pdf, p. 3, 7).

### Evaluation factors:
The model evaluation reports performance disaggregated by:
*   **Downstream Task:** Performance is reported across a suite of 8 core commonsense reasoning tasks (e.g., `arc`, `boolq`, `hellaswag`) (2402.00838.pdf, p. 5-6).
*   **Text Domain:** Intrinsic performance (perplexity) is reported for 11 different data sources from the Paloma benchmark, such as C4, Wikitext-103, and RedPajama (2402.00838.pdf, p. 6, 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Downstream Task Evaluation:** Zero-shot **accuracy** is the primary metric. This is calculated using a rank classification approach where the model ranks candidate text completions by likelihood (2402.00838.pdf, p. 6).
*   **Intrinsic Language Modeling Evaluation:** **Perplexity**, reported in **bits per byte (BPB)**, is used to measure how well the model fits various text distributions. This allows for fair comparison between models with different vocabularies (2402.00838.pdf, p. 6).
*   **Adapted Model Evaluation:** A suite of metrics is used, including **MMLU accuracy**, **AlpacaEval win rate**, **ToxiGen toxicity percentage**, and **TruthfulQA percentage of informative and truthful answers** (2402.00838.pdf, p. 8, Table 4).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For downstream task evaluation, several likelihood normalization strategies are used depending on the dataset to calculate the final prediction. These include:
*   **Unconditional normalization:** Used for `arc` and `openbookqa`.
*   **Per-token normalization:** Used for `hellaswag`, `piqa`, and `winogrande`.
*   **No normalization:** Used for `boolq` and `sciq`, which are formulated as single-token prediction tasks (2402.00838.pdf, p. 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
*   **Downstream Evaluation:** The core evaluation suite consists of 8 commonsense reasoning tasks: `arc` (easy and challenge), `boolq`, `openbookqa`, `sciq`, `hellaswag`, `piqa`, and `winogrande` (2402.00838.pdf, p. 5).
*   **Intrinsic (Perplexity) Evaluation:** The **Paloma benchmark** is used. It contains 585 different domains of text from 18 separate data sources. The paper reports results on a subset of 11 publicly available sources, including C4, mC4-en, Wikitext 103, Penn Treebank, RedPajama, Falcon-RefinedWeb, and Dolma (2402.00838.pdf, p. 4, 6).
*   **Adaptation Evaluation:** The **TÜLU evaluation suite** is used to evaluate instruction-tuned models on chat capabilities and safety (2402.00838.pdf, p. 4). This includes benchmarks like MMLU, AlpacaEval, ToxiGen, and TruthfulQA (2402.00838.pdf, p. 8, Table 4).

### Motivation:
*   The downstream tasks were chosen at the beginning of model development due to their "naturalness" (all can be formulated as text completion scoring tasks) and their "ability to provide meaningful signals throughout training" (2402.00838.pdf, p. 4).
*   The Paloma benchmark was chosen to measure how the model fits distributions of language beyond its held-out training data, allowing for evaluation across a wide and diverse range of text domains (2402.00838.pdf, p. 4).

### Preprocessing:
For the perplexity evaluation on Paloma, the training data was explicitly decontaminated. Any document from the pretraining data that contained paragraphs that also appeared in the Paloma evaluation data was removed to prevent data leakage and ensure a fair assessment of the model's out-of-sample fit (2402.00838.pdf, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on **Dolma**, a large-scale, open pretraining corpus created for this project. Dolma is a diverse, multi-source corpus containing over 3 trillion tokens from billions of documents (2402.00838.pdf, p. 3). The full dataset is publicly available (2402.00838.pdf, p. 2).

The composition of the Dolma dataset is as follows:
| Source             | Type           | Size (GB) | Documents (millions) | Tokens (billions) |
|--------------------|----------------|-----------|----------------------|-------------------|
| Common Crawl       | web pages      | 9,812     | 3,734                | 2,180             |
| GitHub             | code           | 1,043     | 210                  | 342               |
| Reddit             | social media   | 339       | 377                  | 80                |
| Semantic Scholar   | papers         | 268       | 38.8                 | 57                |
| Project Gutenberg  | books          | 20.4      | 0.056                | 5.2               |
| Wikipedia          | encyclopedic   | 16.2      | 6.2                  | 3.7               |
| **Total**          |                | **11,519**| **4,367**            | **2,668**         |
(2402.00838.pdf, p. 3, Table 2)

The OLMo-7B model was trained on a 2.46 trillion token sample from this dataset (2402.00838.pdf, p. 3, Table 1).

### Motivation:
The Dolma dataset was created to facilitate open research on language model pretraining, which has been hindered by the lack of open access to large-scale pretraining data (2402.00838.pdf, p. 3). The data sources were chosen because they are (1) commonly used in large-scale language model pretraining and (2) accessible to the general public (2402.00838.pdf, p. 3).

### Preprocessing:
The Dolma corpus was constructed using a comprehensive pipeline that included:
1.  Language filtering
2.  Quality filtering
3.  Content filtering (e.g., for adult content)
4.  Deduplication
5.  Multi-source mixing
6.  Tokenization
(2402.00838.pdf, p. 3)

For model training, the tokens from every document are concatenated, with a special `[EOS]` token appended to the end of each document. This continuous stream of tokens is then grouped into consecutive chunks of 2048 tokens to form training instances (2402.00838.pdf, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results are presented for individual factors.
*   **Downstream Task Performance (OLMo-7B):**
    *   arc_challenge: 48.5
    *   arc_easy: 65.4
    *   boolq: 73.4
    *   hellaswag: 76.4
    *   openbookqa: 50.4
    *   piqa: 78.4
    *   sciq: 93.8
    *   winogrande: 67.9
    (2402.00838.pdf, p. 6, Table 3)
*   **Intrinsic Performance (Perplexity):** Figure 2 in the paper shows the bits-per-byte score for OLMo-7B and other models on 11 separate data sources from the Paloma benchmark, including C4, RedPajama, and WikiText-103 (2402.00838.pdf, p. 8).
*   **Adapted Model Performance (OLMo-7B+SFT+DPO):**
    *   MMLU (0-shot): 46.1
    *   AlpacaEval (% win): 69.3
    *   ToxiGen (% Toxic): 1.7
    *   TruthfulQA (% Info + True): 52.0
    (2402.00838.pdf, p. 8, Table 4; 2402.00838.pdf, p. 21, Table 8)

### Intersectional results:
The "Sources Combined" subplot in Figure 2 of the paper presents an aggregated bits-per-byte score across 11 data sources from the Paloma benchmark, comparing OLMo-7B's performance against other models throughout training (2402.00838.pdf, p. 8). No other intersectional results (e.g., across demographic and environmental factors) are provided.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on two different high-performance computing clusters, demonstrating its compatibility with both AMD and NVIDIA hardware (2402.00838.pdf, p. 5).
*   **LUMI Supercomputer:** Utilized up to 256 nodes, where each node consists of 4x AMD MI250X GPUs with 128GB of memory each.
*   **MosaicML (Databricks) Cluster:** Utilized 27 nodes, where each node consists of 8x NVIDIA A100 GPUs with 40GB of memory each.

The total energy consumed for pretraining the 7B models was estimated to be **239 MWh** (2402.00838.pdf, p. 16).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers take the position that "increased openness of language models is essential for scientific understanding of their abilities and limitations" (2402.00838.pdf, p. 10).

*   **Sensitive Data:** The developers acknowledge that the large-scale training data (Dolma) "likely contains problematic content like toxic language, personal information, and copyrighted text." They state that this content was mitigated "to the best of our ability," but recognize that no perfect approach exists to completely remove such content (2402.00838.pdf, p. 9). The tokenizer was specifically modified to include tokens for masking personally identifiable information (PII) (2402.00838.pdf, p. 3).
*   **Risks and Mitigation:**
    *   **Harmful Use:** A primary risk is that the model could be "used in unintended ways that cause harm." The developers believe that the open release of the model and its artifacts will accelerate research efforts to understand and mitigate these potential harms by allowing a diversity of approaches and analyses (2402.00838.pdf, p. 10).
    *   **Bias, Toxicity, and Hallucinations:** The pretrained models are acknowledged to face the same issues as other LLMs, including bias, toxicity, and hallucinations. To mitigate this, adapted (instruction-tuned) versions of the model are also released, which are "better at avoiding these generations, but they are not perfect" (2402.00838.pdf, p. 9).
    *   **Environmental Impact:** The paper provides a detailed analysis of the power consumption and carbon footprint of training, estimating that pretraining the 7B model on NVIDIA A100 GPUs in Australia produced 70 tCO2eq. They hope that by releasing the model, they can reduce future emissions by allowing others to build upon their work instead of retraining from scratch (2402.00838.pdf, p. 10, 16).
*   **Licensing:** The choice of a permissive Apache 2.0 license is justified by the observation that many comparable models have already been released with similar licenses. Therefore, using a more restrictive license would not remove the overall risk in the field, and the developers believe the "trade-off on the side of being more open is the best option" (2402.00838.pdf, p. 10).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers explicitly list several limitations of the model and the framework (2402.00838.pdf, p. 9):
*   **Data:** The pretraining data is primarily in **English**, which limits the model's applicability to other languages.
*   **Adaptation:** The adapted models are not perfect and still exhibit issues like bias and toxicity. The data mixture used for adaptation (TÜLU) was originally designed for a different model family (Llama) and relies on data distilled from other proprietary models.
*   **Evaluation:** Many of the downstream evaluation tasks are not representative of common user interactions (e.g., as a chatbot). Furthermore, language model evaluations are described as "very noisy," and there is no single perfect automatic evaluation.
*   **Training:** The paper does not provide extensive logs of training runs that may have diverged or failed, which is a challenging aspect of training large models.

### Recommendations:
*   Users should be aware of the model's limitations, particularly the potential for generating biased, toxic, or factually incorrect content, especially in the base pretrained version (2402.00838.pdf, p. 9).
*   For applications requiring safer and more helpful interactions, using the adapted (instruction-tuned) versions of the model is recommended over the base model (2402.00838.pdf, p. 8).
*   The developers caution that results from automatic evaluations "should be taken with a grain of salt" (2402.00838.pdf, p. 10).
*   The developers encourage the research community to use the full suite of released artifacts (models, data, code) to conduct further studies on the science of language models (2402.00838.pdf, p. 1).