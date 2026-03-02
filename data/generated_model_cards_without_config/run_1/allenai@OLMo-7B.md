## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers primarily from the Allen Institute for Artificial Intelligence (AI2), with collaborators from the University of Washington, Yale University, New York University, and Carnegie Mellon University (2402.00838.pdf, p. 1). The project aims to provide a "truly Open Language Model" to the research community to enable the scientific study of language models (2402.00838.pdf, p. 1).

### Model date:
The associated academic paper was last revised on June 7, 2024 (2402.00838.pdf, p. 1). The project releases numerous intermediate model checkpoints at intervals of 1000 training steps, with the final 7B model checkpoint being trained on 2.46 trillion tokens (2402.00838.pdf, p. 3, 8; revisions.txt).

### Model version:
The OLMo framework includes several model variants. The primary models released are a 1 billion parameter model (OLMo-1B) and a 7 billion parameter model (OLMo-7B) (2402.00838.pdf, p. 2). The paper also mentions a `7B-twin-2T` model (2402.00838.pdf, p. 8). The models are released with over 500 intermediate checkpoints to allow for detailed analysis of the training process (2402.00838.pdf, p. 8). The project's goal is to provide a more open alternative to other models like LLaMA or Falcon by releasing not just model weights but also the training data, training code, evaluation code, and training logs (2402.00838.pdf, p. 1).

### Model type:
OLMo is a decoder-only transformer-based language model (2402.00838.pdf, p. 2).

*   **Architecture:** The architecture includes several modifications to the vanilla transformer to improve training stability and throughput (2402.00838.pdf, p. 2):
    *   **No biases:** All bias terms are excluded from the architecture.
    *   **Non-parametric Layer Normalization:** Uses layer normalization without the affine transformation (adaptive gain and bias).
    *   **SwiGLU Activation Function:** Replaces the standard ReLU activation function.
    *   **Rotary Positional Embeddings (RoPE):** Replaces absolute positional embeddings.
*   **Size:** The released models have 1B and 7B parameters (2402.00838.pdf, p. 2).
    *   **OLMo-1B:** 16 layers, 16 attention heads, hidden dimension of 2048.
    *   **OLMo-7B:** 32 layers, 32 attention heads, hidden dimension of 4096.
*   **Context Length:** The model was trained with a sequence length of 2048 tokens (2402.00838.pdf, p. 4, 17).
*   **Vocabulary:** It uses a modified BPE-based tokenizer from GPT-NeoX with a vocabulary size of 50,280 (2402.00838.pdf, p. 3; tokenizer_summary.json.txt). The embedding matrix is sized to 50,304 to be a multiple of 128 for improved throughput (2402.00838.pdf, p. 3).

### Training details:
The model was pretrained using a supervised learning approach on a next-token prediction task (2402.00838.pdf, p. 1).

*   **Algorithm:** The model was trained using the ZeRO optimizer strategy via PyTorch's FSDP framework for distributed training (2402.00838.pdf, p. 4).
*   **Optimizer:** AdamW optimizer was used with the following hyperparameters (2402.00838.pdf, p. 3, 17):
    *   Betas: (0.9, 0.95)
    *   Epsilon: 1.0e-5
    *   Weight Decay: 0.1
*   **Learning Rate Schedule:** A linear warmup was used for the first 5000 steps (~21B tokens), reaching a peak learning rate of 3.0e-4 for the 7B model. Afterward, the learning rate was decayed linearly to 10% of its peak value over the rest of the training (2402.00838.pdf, p. 3, 5).
*   **Batch Size:** A constant global batch size of approximately 4 million tokens was used (2048 instances of 2048 tokens each) (2402.00838.pdf, p. 4).
*   **Other Details:**
    *   **Precision:** Mixed-precision training with `bfloat16` was employed to improve throughput (2402.00838.pdf, p. 4).
    *   **Gradient Clipping:** Gradients were clipped such that the total L2-norm of the parameter gradients did not exceed 1.0 (2402.00838.pdf, p. 5).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Groeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., ... & Hajishirzi, H. (2024). *OLMo: Accelerating the Science of Language Models*. arXiv preprint arXiv:2402.00838. (2402.00838.pdf).
This paper details the entire OLMo framework, including the model architecture, the Dolma pretraining dataset, training procedures, evaluation results, and the project's philosophy of openness.

The official project website is also available: https://allenai.org/olmo (2402.00838.pdf, p. 2).

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
(2402.00838.pdf)

### License:
All code and model weights are released under the Apache 2.0 License (2402.00838.pdf, p. 2).

### Contact:
For questions or feedback, contact the development team at `olmo@allenai.org` (2402.00838.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary purpose of OLMo is to serve as a foundational, "truly open language model" to "enable the scientific study of language models" (2402.00838.pdf, p. 1). It is intended for research on topics such as the relationship between pretraining data and model capabilities, the impact of design and hyperparameter choices, and optimization methods (2402.00838.pdf, p. 2).

The model can be used as a base for fine-tuning on various downstream tasks. The paper demonstrates its efficacy for adaptation into a general chat assistant (2402.00838.pdf, p. 3). The model is a text-to-text, autoregressive model; it takes a string of text as input and generates text as output (modeling_olmo.py).

### Primary intended users:
The primary intended users are members of the open research community, including academics and practitioners who need full access to a powerful language model, its training data, and its development process for scientific study (2402.00838.pdf, p. 1).

### Out-of-scope uses:
The model is not intended for use in any way that causes harm (2402.00838.pdf, p. 10). As the model was pretrained primarily on English text, its performance in other languages is not guaranteed and is considered out-of-scope (2402.00838.pdf, p. 9). The pretrained model is not tuned for safety and may generate biased, toxic, or hallucinatory content; using the base model directly in user-facing applications without safety fine-tuning is an out-of-scope use (2402.00838.pdf, p. 9).

---

## How to Use
This section outlines how to use the model.

The model can be loaded and used with the Hugging Face `transformers` library. First, ensure the necessary packages are installed (requirements.txt):
```bash
pip install torch
pip install transformers
pip install ai2-olmo>=0.2.2
```

Below is a Python code snippet demonstrating how to load the OLMo-7B model and tokenizer to generate text:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the tokenizer and model from the Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B")
model = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B")

# Prepare the input text
prompt = "The science of language models is"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
# The model can be run on a GPU if available
# inputs = {k: v.to('cuda') for k, v in inputs.items()}
# model.to('cuda')
response = model.generate(**inputs, max_new_tokens=50, do_sample=True, top_k=50, top_p=0.95)

# Decode and print the output
generated_text = tokenizer.batch_decode(response, skip_special_tokens=True)[0]
print(generated_text)
```
(Based on requirements.txt, modeling_olmo.py, and standard Hugging Face usage)

**Sample Output:**
```
The science of language models is a rapidly developing field. The ability to generate human-like text has been a long-standing goal of artificial intelligence research. In recent years, there has been a surge of interest in large-scale language models, which have achieved remarkable success on a wide range of natural language processing tasks.
```

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Text Domain:** The model's performance varies significantly across different domains of text. It performs best on in-distribution data (e.g., web text from Common Crawl) and is less sample efficient on sources less related to scraped web text, such as Wikipedia or academic papers (2402.00838.pdf, p. 7).
*   **Problematic Content:** The training data contains problematic content such as toxic language, personal information, and copyrighted text. While mitigation efforts were made, this can still affect the model's outputs (2402.00838.pdf, p. 9).
*   **Language:** The model is trained primarily on English text, and its performance on other languages is not evaluated (2402.00838.pdf, p. 9).

### Evaluation factors:
The model was evaluated across a wide range of factors:
*   **Downstream Task Performance:** Performance was measured on a suite of 8 core commonsense reasoning tasks (e.g., `arc`, `boolq`, `hellaswag`) and 6 additional tasks (e.g., `headqa_en`, `logiqa`) (2402.00838.pdf, p. 5, 17).
*   **Text Domain Fit:** Intrinsic language modeling performance (perplexity) was evaluated across 11 different text sources from the Paloma benchmark, including C4, Wikipedia, RedPajama, and Dolma (2402.00838.pdf, p. 6, 8).
*   **Adaptation Performance:** After instruction tuning, the model was evaluated on chat capabilities (AlpacaEval), safety (ToxiGen), and truthfulness (TruthfulQA) (2402.00838.pdf, p. 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Downstream Task Evaluation:** For classification-style tasks, the model's performance is measured by **zero-shot accuracy** using a rank classification approach, where candidate completions are ranked by their likelihood (2402.00838.pdf, p. 6).
*   **Intrinsic Language Modeling Evaluation:** The primary metric is **perplexity**, reported as **bits per byte (BPB)** to allow for fair comparison between models with different vocabularies (2402.00838.pdf, p. 6).
*   **Adaptation Evaluation:**
    *   **ToxiGen:** The percentage of generations deemed toxic by a classifier (% Toxic, lower is better) (2402.00838.pdf, p. 8, 20).
    *   **TruthfulQA:** The percentage of responses that are both informative and truthful (% Info+True, higher is better) (2402.00838.pdf, p. 8, 21).
    *   **AlpacaEval:** The win rate (% win) against a baseline model (Davinci-003) as judged by GPT-4 (2402.00838.pdf, p. 8, 21).
    *   **MMLU:** Zero-shot accuracy on the Massive Multitask Language Understanding benchmark (2402.00838.pdf, p. 8).

### Decision thresholds:
Insufficient information.

### Variation approaches:
For downstream task evaluation, different likelihood normalization strategies were selected for each dataset to achieve the best performance. For example, unconditional likelihood normalization was used for `arc` and `openbookqa`, while per-token normalization was used for `hellaswag` and `piqa` (2402.00838.pdf, p. 6).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on three main suites of data:

1.  **Core Downstream Tasks:** A suite of 8 commonsense reasoning tasks (2402.00838.pdf, p. 5):
    *   `arc` (easy and challenge)
    *   `boolq`
    *   `openbookqa`
    *   `sciq`
    *   `hellaswag`
    *   `piqa`
    *   `winogrande`
2.  **Intrinsic Language Modeling (Paloma Benchmark):** A perplexity benchmark including 585 different domains of text drawn from 18 separate data sources. The paper reports aggregate results on 11 publicly available sources, including C4, mC4-en, Wikitext-103, Penn Treebank, RedPajama, Falcon-RefinedWeb, and Dolma (2402.00838.pdf, p. 4, 6).
3.  **Adaptation Evaluation (TÜLU Suite):** An evaluation suite focused on chat capabilities and safety, including benchmarks like MMLU, AlpacaEval, ToxiGen, and TruthfulQA (2402.00838.pdf, p. 4, 8).

### Motivation:
*   The core downstream tasks were selected at the beginning of model development due to their "naturalness" (all can be formulated as text completion scoring tasks) and their ability to "provide meaningful signals throughout training" (2402.00838.pdf, p. 4).
*   The Paloma benchmark was used to measure how well the model fits language distributions beyond its held-out training data, across a wide and diverse set of text domains (2402.00838.pdf, p. 4).
*   The TÜLU suite was used to showcase the efficacy of using OLMo as a base model for fine-tuning into a helpful and safe chat assistant (2402.00838.pdf, p. 4).

### Preprocessing:
For the Paloma perplexity evaluation, explicit decontamination was performed. Any pretraining document that contained paragraphs that had "leaked" from the Paloma evaluation data was removed from the training set. This was done to prevent underestimating perplexity (i.e., overestimating the model's out-of-sample fit) (2402.00838.pdf, p. 4).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on **Dolma**, a diverse, multi-source corpus of three trillion tokens created for this project. The dataset is publicly available. The composition of the full Dolma dataset is as follows (2402.00838.pdf, p. 3):

| Source              | Type           | Size (GB) | Documents (millions) | Tokens (billions) |
| ------------------- | -------------- | --------- | -------------------- | ----------------- |
| Common Crawl      | web pages      | 9,812     | 3,734                | 2,180             |
| GitHub              | code           | 1,043     | 210                  | 342               |
| Reddit              | social media   | 339       | 377                  | 80                |
| Semantic Scholar    | papers         | 268       | 38.8                 | 57                |
| Project Gutenberg   | books          | 20.4      | 0.056                | 5.2               |
| Wikipedia           | encyclopedic   | 16.2      | 6.2                  | 3.7               |
| **Total**           |                | **11,519**  | **4,367**              | **2,668**           |

The released models were trained on a 2 trillion token sample from Dolma (2402.00838.pdf, p. 5).

### Motivation:
The Dolma dataset was created and released to "facilitate open research on language model pretraining," addressing the common issue where pretraining data for large models is not made public. This openness allows researchers to better understand how training data impacts model capabilities and limitations (2402.00838.pdf, p. 3). The sources were chosen because they are commonly seen in large-scale pretraining and are accessible to the general public (2402.00838.pdf, p. 3).

### Preprocessing:
The Dolma dataset was built using a pipeline with the following steps (2402.00838.pdf, p. 3):
1.  Language filtering
2.  Quality filtering
3.  Content filtering
4.  Deduplication
5.  Multi-source mixing
6.  Tokenization

For model training, the tokens from every document are concatenated, with a special `eos_token` appended to the end of each document. This continuous stream of tokens is then grouped into consecutive chunks of 2048 tokens to form training instances. These instances are shuffled in a reproducible way for each training run (2402.00838.pdf, p. 5).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results are presented for individual tasks and data sources.

*   **Core Downstream Tasks (Zero-shot Accuracy):**
    *   **OLMo-7B:** 69.3% average accuracy across 8 core tasks. Individual scores include 48.5% on `arc_challenge`, 73.4% on `boolq`, and 76.4% on `hellaswag` (2402.00838.pdf, Table 3, p. 6).
    *   **OLMo-1B:** 60.4% average accuracy across 8 core tasks (2402.00838.pdf, Table 3, p. 6).
*   **Intrinsic Evaluation (Bits Per Byte):**
    *   OLMo-7B's performance is shown for 11 individual data sources from the Paloma benchmark. For example, it achieves a competitive fit on C4 and Falcon RefinedWeb, which are closer to its pretraining distribution, and is less sample efficient on sources like WikiText-103 and M2D2 S2ORC (2402.00838.pdf, Figure 2, p. 8).
*   **Adaptation Evaluation (OLMo-7B+SFT+DPO):**
    *   **MMLU (0-shot):** 46.1% (2402.00838.pdf, Table 8, p. 21)
    *   **ToxiGen (% Toxic):** 1.7% (2402.00838.pdf, Table 8, p. 21)
    *   **TruthfulQA (% Info+True):** 52.0% (2402.00838.pdf, Table 8, p. 21)
    *   **AlpacaEval (% win):** 69.3% (2402.00838.pdf, Table 8, p. 21)

### Intersectional results:
*   The "Sources Combined" subplot in Figure 2 shows the aggregate bits per byte performance of OLMo-7B and other models across the 11 data sources from the Paloma benchmark, demonstrating its competitive overall fit (2402.00838.pdf, p. 8).
*   Table 7 presents the average zero-shot accuracy for OLMo-7B (47.5%) across 6 additional end-tasks, where it outperforms other comparable models on aggregate (2402.00838.pdf, p. 18).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The model was pretrained on two different GPU clusters to ensure the codebase works on both NVIDIA and AMD hardware (2402.00838.pdf, p. 5).
*   **LUMI Supercomputer:** Utilized up to 256 nodes, where each node consists of 4x AMD MI250X GPUs, each with 128GB of memory.
*   **MosaicML (Databricks) Cluster:** Utilized 27 nodes, where each node consists of 8x NVIDIA A100 GPUs, each with 40GB of memory.

The use of the FSDP framework at the 7B scale enabled training with a micro-batch size of 4096 tokens per GPU (2402.00838.pdf, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Sensitive Data:** The developers acknowledge that the pretraining data, due to its scale, "likely contains problematic content like toxic language, personal information, and copyrighted text" (2402.00838.pdf, p. 9). Mitigation efforts included content filtering during data curation and adding special tokens to the tokenizer for masking personally identifiable information (PII) (2402.00838.pdf, p. 3, 9).
*   **Risks and Mitigation:**
    *   **Misuse:** The "Ethics Statement" acknowledges the risk that "models will be used in unintended ways that cause harm" (2402.00838.pdf, p. 10).
    *   **Bias and Toxicity:** The pretrained models are noted to "face the same issues as existing pretrained LLMs, such as bias, toxicity and, hallucinations" (2402.00838.pdf, p. 9).
    *   **Mitigation through Openness:** The core ethical position of the project is that "increased openness of language models is essential for scientific understanding of their abilities and limitations" (2402.00838.pdf, p. 10). By releasing the model, data, and code, the developers aim to accelerate research and development efforts to understand and mitigate potential harms, allowing for a diversity of approaches and analyses (2402.00838.pdf, p. 10). The release of adapted models with improved safety scores (e.g., on ToxiGen) demonstrates a path for mitigating these risks (2402.00838.pdf, p. 8).
*   **Environmental Impact:** The developers estimate the carbon emissions for pretraining the 7B models to be between 0 and 70 tCO2eq, depending on the hardware used (2402.00838.pdf, Table 6, p. 18). They argue that releasing open models can reduce future emissions by allowing others to build upon their work instead of training from scratch (2402.00838.pdf, p. 10, 16).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Data Limitations:** The model is pretrained primarily on English data, and its capabilities in other languages are unknown (2402.00838.pdf, p. 9). The training data may contain toxic, biased, or copyrighted content despite filtering efforts (2402.00838.pdf, p. 9).
*   **Model Limitations:** The base pretrained models are not instruction-tuned for safety and can produce harmful or inaccurate content. The adapted (fine-tuned) models are better at avoiding these generations but are "not perfect" (2402.00838.pdf, p. 9).
*   **Evaluation Gaps:** Many downstream evaluation tasks are not representative of how users interact with language models in real-world scenarios (e.g., as a chatbot). Furthermore, language model evaluations can be noisy, and comparisons should be "taken with a grain of salt" (2402.00838.pdf, p. 9-10). Some evaluation tasks were found to have unstable performance during training, providing a limited signal for model development (2402.00838.pdf, p. 17).
*   **Adaptation Data:** The instruction-tuning data mix used for adaptation (TÜLU) was designed for a different model family (Llama) and relies on data distilled from other models, which is a limitation the authors hope to reduce in the future (2402.00838.pdf, p. 9).

### Recommendations:
*   Users should fine-tune the base model for safety before deploying it in any user-facing application.
*   The open release is intended to enable practitioners to build on the existing models rather than training new ones from scratch, which is more resource-efficient and has a lower environmental impact (2402.00838.pdf, p. 10).
*   Researchers should be cautious about relying too heavily on evaluation tasks with unstable performance trends (such as `qnli` or `wnli`) when measuring model progress (2402.00838.pdf, p. 17, 19).
*   The developers advocate for a "trade-off on the side of being more open" as the best option for advancing the science and safety of language models (2402.00838.pdf, p. 10).