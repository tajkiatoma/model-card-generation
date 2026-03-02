## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by Jingwei Zuo, Maksim Velikanov, Dhia Eddine Rhaiem, Ilyas Chahed, Younes Belkada, Guillaume Kunsch, and Hakim Hacid from the Technology Innovation Institute (TII) in Abu Dhabi, United Arab Emirates (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

### Model date:
The technical report presenting the model is dated October 7, 2024 (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

### Model version:
The model is named Falcon Mamba 7B (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1). A "pre-decay checkpoint" of the model is also released, which represents the model's state before the final learning rate decay stage of training. This pre-decay version shows slightly lower performance on benchmarks but is provided to support further research and continual training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4, 5).

### Model type:
Falcon Mamba 7B is a decoder-only, causal language model based on the Mamba architecture, making it a pure State Space Model (SSM) without any attention mechanism (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1; config.json).

**Architecture:**
*   The model's architecture is `FalconMambaForCausalLM` (config.json). It is a Selective State Space Model that uses a hardware-aware algorithm to efficiently manage the expanded state in the GPU memory hierarchy (ssm_overview.png).
*   It is based on the Mamba architecture (Gu & Dao, 2023) and is described as the first State Space Language Model (SSLM) in the FalconLLM series (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).

**Size and Key Parameters:**
*   **Parameters:** 7.27 Billion (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Total Size:** 14.5 GB (model.safetensors.index.json).
*   **Layers:** 64 hidden layers (`num_hidden_layers`) (config.json).
*   **Hidden Size:** 4096 (`hidden_size`) (config.json).
*   **Intermediate Size:** 8192 (`intermediate_size`) (config.json).
*   **Vocabulary Size:** 65,024 (`vocab_size`) (config.json).
*   **State Size (N):** 16 (`state_size`) (config.json).
*   **Convolution Kernel Size:** 4 (`conv_kernel`) (config.json).
*   **Context Length:** The Mamba architecture does not have a fixed sequence length limit like Transformers. Any sequence length can be used during inference, though the model's ability to process long sequences is influenced by the context lengths used during training (up to 8192 tokens) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, 4).

### Training details:
The model was pre-trained using the following configuration:
*   **Optimizer:** AdamW with β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸, and a weight decay of 0.1 (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was used. It included a 1 trillion token warmup, followed by a stable phase with a maximum learning rate of 6.4 × 10⁻⁴. The final 10% of training tokens were used for an exponential decay phase, reducing the learning rate to η_max / 25 (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Batch Size:** The training started with a batch size of 128 and linearly ramped up to 2048 over the first 50 trillion tokens (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Stability Techniques:** To improve training stability, RMSNorm layers were added after the B, C, and Δ projections within each Mamba block (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Embeddings:** The input embeddings were untied from the output weights to increase model flexibility and performance (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).
*   **Data Type:** The model was trained with `bfloat16` precision (config.json).

### Paper or other resource for more information:
A detailed overview of the model's architecture, training, and evaluation is available in the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., Chahed, I., Belkada, Y., Kunsch, G., & Hacid, H. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355.

The model weights are publicly available on Hugging Face:
*   `https://huggingface.co/tiiuae/falcon-mamba-7b` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

### Citation details:
```bibtex
@misc{zuo2024falcon,
      title={Falcon Mamba: The First Competitive Attention-free 7B Language Model}, 
      author={Jingwei Zuo and Maksim Velikanov and Dhia Eddine Rhaiem and Ilyas Chahed and Younes Belkada and Guillaume Kunsch and Hakim Hacid},
      year={2024},
      eprint={2410.05355},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
(Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1)

### License:
The model is available under the Falcon Mamba 7B TII License, which is described as a "permissive Apache 2.0-based software license which includes an acceptable use policy that promotes the responsible use of AI" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **License Terms:** `https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Acceptable Use Policy:** `https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

### Contact:
For questions or feedback, contact the development team at: `Falcon-LLM[at]tii[dot]ae` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a foundational, pre-trained, general-purpose language model intended for text generation tasks (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 8). Its primary capability is to take a text prompt as input and generate a coherent text continuation. Due to its Mamba architecture, it is particularly well-suited for tasks requiring long sequence generation, as it maintains constant memory cost and high throughput regardless of the context length (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 8). It is designed to be a competitive alternative to Transformer-based models of a similar scale (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

### Primary intended users:
The model is intended for AI researchers, developers, and practitioners in the machine learning community. The public release of the model and its pre-decay checkpoint is meant to "support the community in further research or continual training on the model" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

### Out-of-scope uses:
The provided documents do not explicitly list out-of-scope uses. However, the model is governed by an acceptable use policy, which should be consulted for a detailed list of prohibited applications (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). The paper notes that the model may have "some limitations in in-context learning compared to Transformers," suggesting it might be less suitable for tasks that heavily rely on this capability without specific fine-tuning or prompting strategies (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

---

## How to Use
This section outlines how to use the model.

The model is integrated into the Hugging Face ecosystem and can be used with the `transformers` library for inference, quantization, and fine-tuning (via the TRL library) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). It is also supported in the `llama.cpp` package for deployment on CPUs (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

The model expects `input_ids` and `attention_mask` as inputs (tokenizer_config.json).

No concrete code snippets for usage are provided in the repository.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data Quality and Mixture:** The paper suggests that the quality of training data and the training strategy play a more crucial role in performance than the model architecture itself. The model's training involved a curriculum learning approach with changing data mixtures across four stages to progressively increase complexity and quality (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4, 6).
*   **Training Sequence Length:** While the model can handle any sequence length at inference, its proficiency with long contexts is determined by the sequence lengths used during training (up to 8192 tokens) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, 4).
*   **Prompting Techniques:** The model's performance, particularly on in-context learning tasks, can be influenced by the use of tailored prompting techniques like Chain-of-Thought (CoT) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

### Evaluation factors:
The model was evaluated on a range of factors to assess its versatility (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5):
*   **Instruction Following**
*   **Math, Reasoning, and Problem-Solving**
*   **Aggregate Knowledge** (via MMLU and BIG-Bench Hard)
*   **Throughput and Memory Consumption** for long sequence generation.

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was measured using scores from a wide range of standard academic benchmarks, primarily sourced from the Open LLM Leaderboard (v1 and v2). These include (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, Tables 2 & 3):
*   **ARC-25:** AI2 Reasoning Challenge
*   **HellaSwag-10:** Commonsense NLI
*   **MMLU-5 / MMLU-PRO-5:** Massive Multitask Language Understanding
*   **Winogrande-5:** Commonsense Reasoning
*   **TruthfulQA-0:** Truthfulness
*   **GSM8K-5:** Grade School Math
*   **IFEval-0:** Instruction Following
*   **BBH-3:** BIG-Bench Hard
*   **Math-Lvl5-4:** Mathematical Problem Solving
*   **GPQA-0:** Graduate-Level Google-Proof Q&A
*   **MuSR-0:** Multistep Soft Reasoning

Efficiency was measured using **generation throughput (tokens/second)** and **peak GPU memory usage** (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure an unbiased comparison, performance results for competitor models were primarily extracted from the public Hugging Face Leaderboards (v1 and v2). For models not on the leaderboards, results were taken from their respective papers or from internal evaluations. These internal evaluations were conducted using the `lm-evaluation-harness` and `lighteval` packages (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a suite of publicly available benchmarks (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5):
*   **IFEval (0-shot):** For instruction following.
*   **GSM8K (5-shots), MATH-Lvl5 (4-shots), ARC Challenge (25-shots), GPQA (0-shot), MuSR (0-shot):** For math, reasoning, and problem-solving.
*   **MMLU (5-shots), MMLU-Pro (5-shots), BIG-Bench Hard (BBH) (3-shots):** For aggregate knowledge and complex reasoning.

### Motivation:
These benchmarks were chosen because they are publicly available, independently conducted by Hugging Face, and "span a broad range of top-level categories to assess the model's versatility and performance across various tasks" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

### Preprocessing:
Insufficient information is available regarding specific preprocessing steps for the evaluation data, other than the number of few-shot examples used for each benchmark (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on 5.8 trillion tokens from a diverse data mixture, largely based on the data used for Falcon2-11B but excluding multilingual data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 3). The data sources include:
*   **Web Data:** Primarily from the RefinedWeb dataset, which is derived from Common Crawl. Parts of the Fineweb-Edu dataset were also used in the final training stage (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3, 4).
*   **Curated Data:** A collection of books, scientific publications (arXiv, PubMed), patents (USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Code Data:** Samples from The Stack dataset (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Math Data:** Data from the Proof-Pile-2 dataset and math-related content filtered from web data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Synthetic and Instruction Data:** In the final decay stage, synthetic data from Cosmopedia and a small amount of multitask instruction data were introduced (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

The proportions of these data sources were varied across five distinct training stages as part of a curriculum learning strategy (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4, Figure 1).

### Motivation:
The dataset was chosen to be diverse and high-quality. A curriculum learning approach was followed, where the data mixture was adjusted across stages to "increase high quality and scientific data at late stages." Data introduced in the final decay stage was intended to "refine or shapen the knowledge learned" and "enhance the model's zero-shot and few-shot learning capabilities" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

### Preprocessing:
*   **Web Data (RefinedWeb):** Raw Common Crawl data was processed through language identification, line-wise and document-wise filtering, and both fuzzy and exact deduplication (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Conversational Data:** Causal temporality was enforced to ensure each conversation was used only once during training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Code Data:** Processed using the same pipelines as the web data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Tokenization:** The model uses the same BPE tokenizer as the Falcon series models. The pre-tokenization process involves splitting by punctuation, byte-level encoding, handling digits, and splitting on specific regex patterns (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3; tokenizer.json).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results on individual benchmarks are presented in Tables 2 and 3 of the technical report. Falcon Mamba 7B achieves an average score of 64.09 on the HF Leaderboard v1 tasks and 15.04 on the v2 tasks (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

**Selected Benchmark Scores (Falcon Mamba 7B):**
*   **ARC-25:** 62.03
*   **MMLU-5:** 62.11
*   **GSM8K-5:** 52.54
*   **IFEval-0:** 33.36
*   **Gemma-7B:** 15.28

**Efficiency Analysis:**
*   **Memory:** On a 24GB A10 GPU, the model can process a maximum context length of 16k tokens with parallel prefill and a virtually unlimited length with sequential prefill (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 2).
*   **Throughput:** When generating up to 130k tokens on an 80GB H100 GPU, the model maintains a constant throughput and memory footprint, unlike Transformer models where both degrade linearly with sequence length (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).

### Intersectional results:
Insufficient information. The results are not disaggregated by demographic or other intersectional factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
*   **GPU:** The model's memory usage was evaluated on a single 24 GB A10 GPU and an 80GB H100 GPU. On a 24GB GPU, it can handle sequences up to 16k tokens long (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 6, 7).
*   **CPU:** The model is supported by the `llama.cpp` package, enabling deployment on local machines using CPU hardware (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

### Training or Fine-tuning Requirements:
The pre-training was conducted on a cluster of **256 H100 80GB GPUs** using Data Parallelism (DP=256) and ZeRO optimization (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model is released with an "acceptable use policy that promotes the responsible use of AI" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). Users are expected to adhere to this policy.

The training data includes content from public web sources like Common Crawl, Reddit, and StackExchange, which may contain sensitive or personal information (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3, 4). While the RefinedWeb portion of the data underwent filtering and deduplication, the extent of personal data removal is not specified.

The provided documents do not detail specific risks, mitigation strategies beyond the acceptable use policy, or analysis of potential harms.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **In-Context Learning:** The model may show "some limitations in in-context learning compared to Transformers" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Training Instability:** During pre-training, the model exhibited "consistent loss spikes that occurred randomly and unpredictably," indicating that the Mamba architecture is more sensitive to learning rates than Transformers (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).
*   **Long-Context Proficiency:** The training strategy used a "rather medium 8k context length," so the model's full potential on extra-long sequence understanding and generation remains an "underexplored area" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Scaling Laws:** The effects of data and model scaling for the Mamba architecture are less understood than for Transformers, leaving its potential limitations and optimizations as an open research question (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

### Recommendations:
*   **Prompting:** To mitigate limitations in in-context learning, users can employ "high-quality data, especially Chain-of-Thought (CoT) instruction data or tailored prompting techniques" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Batched Inference:** When performing batched generation with sequences of varying lengths, left-side padding should be used. To prevent padding tokens from affecting the output, users should zero out the hidden states corresponding to the padding tokens before and after the causal convolution step (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Future Research:** The paper recommends further research into training Mamba-based models on extra-large contexts and exploring optimal ways to combine SSM and attention mechanisms in hybrid architectures (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).