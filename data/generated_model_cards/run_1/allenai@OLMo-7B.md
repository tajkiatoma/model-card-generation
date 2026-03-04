## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a large team of researchers primarily from the Allen Institute for Artificial Intelligence (AI2), with collaborators from the University of Washington, Yale University, New York University, and Carnegie Mellon University (2402.00838.pdf, p. 1). The full list of authors includes Dirk Groeneveld, Iz Beltagy, Pete Walsh, and many others listed in the associated paper (2402.00838.pdf, p. 1).

### Model date:
The associated academic paper was submitted to arXiv and the first version of this model was released in early 2024. The paper has a revision date of June 7, 2024 (2402.00838.pdf, p. 1).

### Model version:
The OLMo framework includes models of different sizes, primarily a 1B and a 7B parameter version (2402.00838.pdf, p. 2). The repository provides over 500 intermediate checkpoints for the models, released at intervals of 1000 training steps, allowing for detailed analysis of the training process over time (2402.00838.pdf, p. 8; revisions.txt). For example, checkpoints are available from `step0-tokens0B` up to `step557000-tokens2464B` and beyond (revisions.txt). The evaluated 7B model checkpoint was trained for 2.46 trillion tokens (2402.00838.pdf, p. 3, 5).

### Model type:
OLMo is a decoder-only transformer-based language model, specifically an `OLMoForCausalLM` (2402.00838.pdf, p. 2; config.json.txt). It is designed as a competitive, "truly Open Language Model" for text generation and scientific study (2402.00838.pdf, p. 1).

**Architecture Details:**
The architecture incorporates several modern improvements over the vanilla transformer (2402.00838.pdf, p. 2):
*   **No Biases:** All bias terms are excluded from the architecture to improve training stability (2402.00838.pdf, p. 2).
*   **Layer Normalization:** A non-parametric layer norm without affine transformation is used (2402.00838.pdf, p. 2; config.json.txt).
*   **Activation Function:** SwiGLU activation function is used instead of ReLU (2402.00838.pdf, p. 2; config.json.txt).
*   **Positional Embeddings:** Rotary Positional Embeddings (RoPE) are used instead of absolute positional embeddings (2402.00838.pdf, p. 3; config.json.txt).
*   **Vocabulary:** It uses a modified BPE-based tokenizer from GPT-NeoX-20B with a vocabulary size of 50,280, plus additional tokens for masking personally identifiable information (PII) (2402.00838.pdf, p. 3; tokenizer_summary.json.txt). The model's embedding matrix size is increased to 50,304 to be a multiple of 128 for throughput optimization (2402.00838.pdf, p. 3; config.json.txt).

**Model Size (7B version):**
*   **Parameters:** ~7 billion
*   **Layers (`n_layers`):** 32 (config.json.txt)
*   **Hidden Size (`d_model`):** 4096 (config.json.txt)
*   **Attention Heads (`n_heads`):** 32 (config.json.txt)
*   **MLP Hidden Size:** 22016 (config.json.txt)
*   **Max Sequence Length:** 2048 (config.json.txt)

### Training details:
The model was pretrained using a supervised learning approach on a next-token prediction task (2402.00838.pdf, p. 3).

*   **Optimizer:** AdamW optimizer was used (2402.00838.pdf, p. 3).
    *   Betas: (0.9, 0.95) (2402.00838.pdf, p. 3, Table 1).
    *   Epsilon: 1.0e-5 (2402.00838.pdf, p. 3, Table 1).
    *   Weight Decay: 0.1 for the 7B model (2402.00838.pdf, p. 17, Table 5).
*   **Learning Rate Schedule:** The learning rate was warmed up over the first 5000 steps (~21B tokens) to a peak of 3.0e-4, then linearly decayed to one-tenth of the peak rate over the remainder of training (2402.00838.pdf, p. 3, 5).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens was used (2048 instances of 2048 tokens each) (2402.00838.pdf, p. 4).
*   **Precision:** Mixed-precision training with `amp_bf16` was employed to improve throughput (2402.00838.pdf, p. 4; config.json.txt).
*   **Gradient Clipping:** Gradients were clipped such that the total L2-norm of the parameter gradients does not exceed 1.0 (2402.00838.pdf, p. 5).
*   **Framework:** The model was trained using the ZeRO optimizer strategy via PyTorch's FSDP framework to reduce memory consumption (2402.00838.pdf, p. 4).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   **Title:** OLMo: Accelerating the Science of Language Models
*   **Authors:** Dirk Groeneveld, Iz Beltagy, Pete Walsh, et al.
*   **Summary:** The paper introduces OLMo, a truly open language model, and its surrounding framework. It details the model architecture, the open training dataset Dolma, the training process, and evaluation results. The authors emphasize the release of the entire framework—including data, training code, evaluation code, and intermediate checkpoints—to empower the research community (2402.00838.pdf).

The paper also highlights the release of the full framework artifacts, including the Dolma dataset, data curation tools, and the Catwalk evaluation framework (2402.00838.pdf, p. 8-9).

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
(Citation constructed from 2402.00838.pdf, p. 1)

### License:
All code and model weights are released under the Apache 2.0 License (2402.00838.pdf, p. 2).

### Contact:
For questions, issues, or feedback, contact the development team at `olmo@allenai.org` (2402.00838.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to "enable the scientific study of language models" by providing a powerful, truly open model and its complete development framework (2402.00838.pdf, p. 1). It is intended to be a general-purpose tool for researchers to study aspects like the relationship between pretraining data and model capabilities, the impact of design choices, and optimization methods (2402.00838.pdf, p. 2).

The model can be used as a base for further fine-tuning on specific tasks. For example, it has been successfully fine-tuned to function as a general chat assistant (2402.00838.pdf, p. 3). The model takes text as input and generates text as output (causal language modeling) (config.json.txt).

### Primary intended users:
The primary intended users are the "research community" and "academics and practitioners" (2402.00838.pdf, p. 1, 8). The release aims to empower open research and reduce duplicated efforts in training large models from scratch (2402.00838.pdf, p. 1, 8).

### Out-of-scope uses:
The model is not intended for applications that cause harm. The developers acknowledge the "possibility remains that these models will be used in unintended ways that cause harm" (2402.00838.pdf, p. 10). As the model was pretrained primarily on English data, its performance in other languages is out-of-scope (2402.00838.pdf, p. 9). The pretrained model, without fine-tuning, is not designed to be a safe or helpful assistant and may exhibit biases, toxicity, or generate factual inaccuracies (2402.00838.pdf, p. 9).

---

## How to Use
This section outlines how to use the model.

The model is compatible with the Hugging Face Transformers library (config.json.txt, `auto_map` section). Users can load the model and tokenizer using the `AutoModelForCausalLM` and `AutoTokenizerFast` classes. The required library version is `ai2-olmo>=0.2.2` (requirements.txt).

Here is a sample code snippet for using the model:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model from the Hugging Face Hub or a local directory
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")
model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")

# Prepare the input text
prompt = "The science of language models is"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
outputs = model.generate(**inputs, max_length=50)

# Decode and print the output
generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
print(generated_text)
```
**Sample Output:**
```
The science of language models is a rapidly developing field, with new models and techniques being developed all the time. In this article, we will provide an overview of the current state of the art in language modeling, and discuss some of the key challenges and opportunities in this
```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Text Domain:** The model's performance is influenced by the domain of the text. The evaluation framework used, Paloma, includes 585 different domains from 18 sources (e.g., news, Reddit, scientific papers) to measure this variation (2402.00838.pdf, p. 4).
*   **Language:** The model was pretrained primarily on English text, so performance on other languages is a relevant, though unevaluated, factor (2402.00838.pdf, p. 9).
*   **Dialect and Community-Specific Language:** The evaluation includes datasets for targeted analysis of performance disparities across different dialects (e.g., TwitterAAE) and language from fringe online communities (e.g., Manosphere, Gab) (2402.00838.pdf, p. 16).

### Evaluation factors:
The model was evaluated on the following factors:
*   **Downstream Task Performance:** Performance was measured on a suite of 8 core commonsense reasoning tasks (2402.00838.pdf, p. 4).
*   **Intrinsic Language Modeling:** Perplexity was measured across a combination of 11 diverse text sources from the Paloma benchmark to assess how well the model fits different distributions of language (2402.00838.pdf, p. 6).
*   **Adaptation Performance:** After fine-tuning, the model was evaluated on chat capabilities and safety (2402.00838.pdf, p. 4).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Accuracy:** Zero-shot accuracy is used for downstream commonsense reasoning tasks (2402.00838.pdf, p. 6).
*   **Bits Per Byte (Bpb):** This metric, a form of perplexity, is used for intrinsic language modeling evaluation to allow for fair comparison between models with different vocabularies (2402.00838.pdf, p. 6).
*   **Adapted Model Metrics:** For instruction-tuned versions, a suite of metrics is used, including MMLU (0-shot accuracy), AlpacaEval (% win rate against a baseline), ToxiGen (% of generations deemed toxic), and TruthfulQA (% of responses that are both informative and truthful) (2402.00838.pdf, p. 8, Table 4).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For zero-shot downstream task evaluation, a "rank classification approach" is used. Candidate text completions are ranked by their likelihood. This likelihood is calculated using several normalization strategies depending on the dataset, such as per-token normalization, per-character normalization, or incorporating the answer's unconditional likelihood (2402.00838.pdf, p. 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
A wide range of publicly available datasets were used for evaluation:
*   **Core Downstream Tasks:** A suite of 8 commonsense reasoning tasks: arc (easy and challenge), boolq, openbookqa, sciq, hellaswag, piqa, and winogrande (2402.00838.pdf, p. 5).
*   **Intrinsic Language Modeling (Perplexity):** The Paloma benchmark, which contains 585 text domains. A subset of 11 publicly available sources was used for the main comparison, including C4, mC4-en, Wikitext-103, Penn Treebank, RedPajama, Falcon-RefinedWeb, and Dolma (2402.00838.pdf, p. 6).
*   **Adaptation Evaluation:** The TULU evaluation suite was used for instruction-tuned models, which includes benchmarks like MMLU, GSM8k, BBH, ToxiGen, and TruthfulQA (2402.00838.pdf, p. 4, 21).

### Motivation:
The core downstream tasks were selected at the beginning of development due to their "naturalness" (they can be formulated as text completion) and their "ability to provide meaningful signals throughout training" (2402.00838.pdf, p. 4). The Paloma benchmark was chosen to measure how the model fits language distributions beyond its training data and to allow for more equal inclusion of under-represented text domains (2402.00838.pdf, p. 4).

### Preprocessing:
For the perplexity evaluation on Paloma, the training data was explicitly decontaminated. Any pretraining document containing paragraphs that were also present in the Paloma evaluation data was removed to ensure a fair out-of-sample evaluation (2402.00838.pdf, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on **Dolma**, a diverse, multi-source corpus of three trillion tokens created specifically for this project. The full dataset is publicly available (2402.00838.pdf, p. 3, 9). The 7B model was trained on a 2.46T token sample of Dolma (2402.00838.pdf, p. 5).

The composition of the full Dolma dataset is as follows:
*   **Common Crawl (web pages):** 2,180 billion tokens
*   **GitHub (code):** 342 billion tokens
*   **Reddit (social media):** 80 billion tokens
*   **Semantic Scholar (papers):** 57 billion tokens
*   **Project Gutenberg (books):** 5.2 billion tokens
*   **Wikipedia (encyclopedic):** 3.7 billion tokens
*   **Total:** 2,668 billion tokens
(2402.00838.pdf, p. 3, Table 2)

### Motivation:
The Dolma dataset was created to "facilitate open research on language model pretraining," as high-quality, large-scale pretraining datasets are often not publicly released. The data sources were chosen because they are (1) commonly used in large-scale pretraining and (2) accessible to the general public (2402.00838.pdf, p. 3).

### Preprocessing:
The Dolma dataset was built using a six-step pipeline: (1) language filtering, (2) quality filtering, (3) content filtering, (4) deduplication, (5) multi-source mixing, and (6) tokenization (2402.00838.pdf, p. 3). For model training, tokens from each document are concatenated with a special end-of-sentence (EOS) token. This stream of tokens is then grouped into consecutive chunks of 2048 tokens to form training instances, which are then shuffled (2402.00838.pdf, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
*   **Downstream Tasks:** Table 3 presents the zero-shot accuracy for OLMo-7B on 8 individual core tasks. For example, it scored 48.5 on `arc_challenge`, 73.4 on `boolq`, and 76.4 on `hellaswag` (2402.00838.pdf, p. 6).
*   **Perplexity:** Figure 2 shows the bits-per-byte score for OLMo-7B on 11 individual data sources from the Paloma benchmark, such as C4, RedPajama, and WikiText-103, comparing its performance trend against other models as training progresses (2402.00838.pdf, p. 8).
*   **Adaptation Tasks:** Table 8 shows the performance of the base and fine-tuned OLMo-7B on individual tasks from the TULU suite. For example, after SFT+DPO fine-tuning, the model scored 46.1 on MMLU, 1.7% toxic on ToxiGen, and 52.0% on TruthfulQA (2402.00838.pdf, p. 21).

### Intersectional results:
The paper presents aggregated results across tasks and data sources. For instance, Table 3 includes an `avg.` column showing the average accuracy across the 8 core downstream tasks (69.3 for OLMo-7B) (2402.00838.pdf, p. 6). The "Sources Combined" subplot in Figure 2 shows the aggregate bits-per-byte performance across 11 Paloma data sources (2402.00838.pdf, p. 8). No intersectional results across demographic or other fine-grained societal factors are presented.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was trained on two different high-performance computing clusters, demonstrating its compatibility with both AMD and NVIDIA hardware (2402.00838.pdf, p. 5):
*   **LUMI Supercomputer:** Utilized up to 256 nodes, where each node consists of 4x AMD MI250X GPUs with 128GB of memory each.
*   **MosaicML (Databricks) Cluster:** Utilized 27 nodes, where each node consists of 8x NVIDIA A100 GPUs with 40GB of memory each.

The training framework (PyTorch FSDP) enabled training the 7B model with a micro-batch size of 4096 tokens per GPU (2402.00838.pdf, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers' core ethical position is that "increased openness of language models is essential for scientific understanding of their abilities and limitations" and for mitigating potential harms (2402.00838.pdf, p. 10).

*   **Sensitive Data:** The training data likely contains "problematic content like toxic language, personal information, and copyrighted text." This was mitigated "to the best of our ability," but the developers acknowledge that "no perfect approaches today can completely remove such content" (2402.00838.pdf, p. 9). The tokenizer includes special tokens for masking personally identifiable information (PII) (2402.00838.pdf, p. 3).
*   **Risks and Mitigation:**
    *   **Misuse:** There is a risk that the models "will be used in unintended ways that cause harm." The developers argue that releasing the model under a permissive license (Apache 2.0) does not increase the overall risk in the field, as many comparable models already exist. They believe that openness accelerates research and development efforts to understand and mitigate these harms by allowing a "diversity of approaches and analyses" (2402.00838.pdf, p. 10).
    *   **Bias, Toxicity, and Hallucinations:** The pretrained models are acknowledged to face these issues. The adapted (fine-tuned) models are "better at avoiding these generations, but they are not perfect" (2402.00838.pdf, p. 9).
    *   **Environmental Impact:** By releasing the models and training framework, the developers hope to reduce future emissions by allowing others to "build on them instead of having to train their own from scratch" (2402.00838.pdf, p. 10). The carbon footprint of the training is documented in the paper's appendix (2402.00838.pdf, p. 18, Table 6).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers list several limitations in the paper (2402.00838.pdf, p. 9):
*   **Language Coverage:** The model is primarily focused on English, and its capabilities in other languages are limited.
*   **Data Content:** The training data may contain toxic, biased, or copyrighted content despite mitigation efforts.
*   **Model Behavior:** The pretrained model can exhibit bias, toxicity, and hallucinations. Fine-tuned versions are improved but not perfect.
*   **Evaluation Gaps:** Many standard downstream evaluation tasks are not representative of how users interact with models (e.g., as a chatbot). Furthermore, language model evaluations are described as "very noisy," and comparisons should be "taken with a grain of salt."
*   **Adaptation Data:** The data mixture used for fine-tuning the chat model (TULU) was originally designed for a different model family (Llama) and relies on data distilled from other models.

### Recommendations:
The paper does not provide explicit recommendations for downstream users. However, the overarching recommendation is for the research community to use the open artifacts (model weights, checkpoints, data, code) to conduct scientific studies on language models (2402.00838.pdf, p. 1). Users should be aware of the model's limitations, especially regarding potential for harmful generations, and should consider further fine-tuning and safety measures before deployment in sensitive applications. Building upon the provided models and checkpoints is recommended over training from scratch to reduce environmental impact (2402.00838.pdf, p. 10).