## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers at the Technology Innovation Institute in Abu Dhabi, United Arab Emirates. The developers are Jingwei Zuo, Maksim Velikanov, Dhia Eddine Rhaiem, Ilyas Chahed, Younes Belkada, Guillaume Kunsch, and Hakim Hacid (2410.05355.pdf, p. 1).

### Model date:
The technical report describing the model was submitted to arXiv on October 7, 2024 (2410.05355.pdf, p. 1).

### Model version:
The model is named Falcon Mamba 7B. A "pre-decay checkpoint" of the model is also available, which represents the model's state before the final learning rate decay stage of training (2410.05355.pdf, p. 4). This model is the first State Space Language Model (SSLM) in the FalconLLM series and is a pure Mamba-based model, distinguishing it from hybrid Mamba-Transformer models and traditional Transformer-based models (2410.05355.pdf, p. 1-2).

### Model type:
Falcon Mamba 7B is a decoder-only, attention-free, pre-trained large language model based on the Mamba architecture, also known as a State Space Language Model (SSLM) (2410.05355.pdf, p. 1-2).

**Architecture:**
*   The model uses a pure Mamba architecture, which is a type of Structured State Space Model (SSM) that processes sequences linearly, offering significant efficiency gains over the quadratic complexity of Transformer attention mechanisms, especially for long sequences (2410.05355.pdf, p. 1, 6; mamba-paper.png).
*   The architecture is specified as `FalconMambaForCausalLM` (config.json.txt).
*   To improve training stability, RMSNorm layers are added after the B, C, and Δ projections within each block (2410.05355.pdf, p. 3).

**Model Size and Parameters:**
*   **Parameters:** 7.27 billion (2410.05355.pdf, Table 1, p. 2).
*   **Total Size on Disk:** 14.54 GB (model.safetensors.index.json.txt).
*   **Layers:** 64 hidden layers (config.json.txt; 2410.05355.pdf, Table 1, p. 2).
*   **Hidden Size (`d_model`):** 4096 (config.json.txt; 2410.05355.pdf, Table 1, p. 2).
*   **Intermediate Size:** 8192 (config.json.txt).
*   **State Size (`N`):** 16 (config.json.txt; 2410.05355.pdf, Table 1, p. 2).
*   **Convolution Kernel:** 4 (config.json.txt; 2410.05355.pdf, Table 1, p. 2).
*   **Expansion Factor (`E`):** The technical report states an expansion factor of 2 (2410.05355.pdf, Table 1, p. 2), while the model's configuration file specifies an expansion factor of 16 (config.json.txt).
*   **Vocabulary Size:** 65,024 (config.json.txt; 2410.05355.pdf, Table 1, p. 2).
*   **Precision:** The model was trained and is stored in `bfloat16` format (config.json.txt).

**Context Length:**
*   The Mamba architecture does not have a fixed sequence length limit during inference. The model was trained on sequences up to 8,192 tokens (2410.05355.pdf, p. 2, 4).

### Training details:
The model was pre-trained on 5.8 trillion tokens (2410.05355.pdf, p. 1).

*   **Optimizer:** AdamW with the following hyperparameters: β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸, and a weight decay of 0.1 (2410.05355.pdf, p. 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was used. It included a warmup phase of 1 trillion tokens, a stable phase with a maximum learning rate of 6.4 × 10⁻⁴, and a final exponential decay phase over the last 10% of training tokens (2410.05355.pdf, p. 3).
*   **Batch Size:** The training used a batch size ramp-up, linearly increasing from 128 to 2048 over the first 50 trillion tokens. A "batch scaling" technique was applied to keep the Adam optimizer's noise temperature constant when the batch size changed (2410.05355.pdf, p. 3).
*   **Hardware and Parallelism:** The model was trained on 256 NVIDIA H100 80GB GPUs using Data Parallelism (DP=256) and ZeRO optimization (2410.05355.pdf, p. 3).
*   **Training Stages:** The pre-training was conducted in five stages: four stages with a constant learning rate and progressively increasing sequence length (from 2k to 8k), followed by a final learning rate decay stage. The data mixture was adjusted at each stage to follow a curriculum learning approach, introducing higher-quality data later in training (2410.05355.pdf, p. 4, Figure 1).

### Paper or other resource for more information:
The primary resource is the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., Chahed, I., Belkada, Y., Kunsch, G., & Hacid, H. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355. (2410.05355.pdf).

The model weights are available on Hugging Face:
*   `https://huggingface.co/tiiuae/falcon-mamba-7b` (2410.05355.pdf, p. 1).

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
(2410.05355.pdf, p. 1)

### License:
The model is available under the "Falcon Mamba 7B TII License," which is described as a permissive, Apache 2.0-based software license. The license includes an acceptable use policy to promote the responsible use of AI (2410.05355.pdf, p. 8).
*   Terms and Conditions: `https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html` (2410.05355.pdf, p. 1, 8).
*   Acceptable Use Policy: `https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html` (2410.05355.pdf, p. 8).

### Contact:
For questions or feedback, contact the development team at: `Falcon-LLM [at] tii[dot]ae` (2410.05355.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a pre-trained, base language model intended for general-purpose use (2410.05355.pdf, p. 1, 8). Its primary use is as a foundation for further fine-tuning on specific downstream tasks. Due to its Mamba architecture, it is particularly well-suited for applications requiring efficient processing of long sequences, such as long-context reasoning and large-scale text generation (2410.05355.pdf, p. 1, 6, 8). The model has demonstrated strong performance on a variety of benchmarks, including reasoning, problem-solving, and instruction-following tasks (2410.05355.pdf, p. 5-6).

### Primary intended users:
The model is released publicly with a permissive license, indicating that the primary intended users are AI researchers, developers, and practitioners who wish to build upon a strong, attention-free foundation model (2410.05355.pdf, p. 1, 8).

### Out-of-scope uses:
*   **Multilingual Applications:** The model was intentionally trained almost exclusively on English data. The developers note that a 7B model may not be sufficient for strong multilingual performance without harming its English capabilities. Therefore, it is not intended for out-of-the-box use on multilingual tasks (2410.05355.pdf, p. 3).
*   **Prohibited Uses:** Any use that violates the model's Acceptable Use Policy is out-of-scope. The policy can be found at `https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html` (2410.05355.pdf, p. 8).

---

## How to Use
This section outlines how to use the model.

The model is integrated into the Hugging Face ecosystem and can be used with the `transformers` library (2410.05355.pdf, p. 8). The model's configuration files (`config.json.txt`, `generation_config.json.txt`) are set up for this purpose. While no explicit code snippets are provided in the repository, a user would typically load the model and tokenizer from Hugging Face and use them for text generation. The model is also supported by the `llama.cpp` library for CPU-based deployment (2410.05355.pdf, p. 8).

The model uses the following special token IDs:
*   `bos_token_id`: 0 (beginning of sequence) (config.json.txt; generation_config.json.txt).
*   `eos_token_id`: 11 (end of sequence) (config.json.txt; generation_config.json.txt).
*   `pad_token_id`: 11 (padding) (config.json.txt; generation_config.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Data Quality and Mixture:** The paper emphasizes that the quality of pre-training data and the training strategy (e.g., curriculum learning with varying data mixtures) are crucial factors that can mitigate architectural disadvantages and significantly impact performance (2410.05355.pdf, p. 4, 6).
*   **Sequence Length:** The model's Mamba architecture is designed to be highly efficient with long sequences, maintaining constant memory and throughput during generation. Its performance advantage over Transformers grows as sequence length increases (2410.05355.pdf, p. 6-7).
*   **Learning Rate Sensitivity:** The Mamba architecture was found to be more sensitive to learning rates than Transformers, making careful tuning of the learning rate schedule a critical factor for stable and effective training (2410.05355.pdf, p. 2).
*   **Prompting Techniques:** Performance on certain tasks, like in-context learning, can be influenced by the use of tailored prompting techniques such as Chain-of-Thought (CoT) (2410.05355.pdf, p. 8).

### Evaluation factors:
The model was evaluated across a broad range of tasks to assess its versatility. These factors include:
*   **Instruction Following:** (IFEval) (2410.05355.pdf, p. 5).
*   **Reasoning and Problem-Solving:** (GSM8K, MATH-Lvl5, ARC Challenge, GPQA, MuSR) (2410.05355.pdf, p. 5).
*   **General Knowledge and Multitask Understanding:** (MMLU, MMLU-Pro, BIG-Bench Hard, HellaSwag, Winogrande, TruthfulQA) (2410.05355.pdf, p. 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance is measured using the standard evaluation metrics for a variety of academic benchmarks. These are primarily accuracy-based scores. The results are presented in comparison to other state-of-the-art models (2410.05355.pdf, Tables 2 & 3, p. 5).

For efficiency, the model is evaluated on:
*   **Throughput:** Measured in tokens per second (tok/s) during generation (2410.05355.pdf, Figure 3, p. 7).
*   **Memory Consumption:** Measured as the maximum GPU memory occupied by tensors (2410.05355.pdf, Figure 3, p. 7).

### Decision thresholds:
Insufficient information. This is not applicable for a generative base model.

### Variation approaches:
The evaluation was conducted using established frameworks like `lm-evaluation-harness` and `lighteval` (2410.05355.pdf, p. 5). Performance is reported for different few-shot settings (e.g., 0-shot, 3-shot, 5-shot, 25-shot) depending on the benchmark, which represents a variation in the evaluation approach (2410.05355.pdf, p. 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of publicly available benchmarks (2410.05355.pdf, p. 5):
*   **IFEval:** For instruction following.
*   **GSM8K, MATH-Lvl5, ARC Challenge, GPQA, MuSR:** For math, reasoning, and problem-solving.
*   **MMLU, MMLU-Pro, BIG-Bench Hard (BBH):** Aggregate benchmarks for multitask understanding.
*   **HellaSwag, Winogrande, TruthfulQA:** For commonsense reasoning and truthfulness.

### Motivation:
These benchmarks were selected because they "span a broad range of top-level categories to assess the model's versatility and performance across various tasks" (2410.05355.pdf, p. 5). The selection allows for a comprehensive comparison against other leading models with different architectures.

### Preprocessing:
The paper does not detail specific preprocessing steps for the evaluation data. However, it specifies the number of few-shot examples provided to the model for each benchmark, which is a key part of the evaluation setup (e.g., "MMLU (5-shots)") (2410.05355.pdf, p. 5).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a 5.8 trillion token dataset composed of a diverse mixture of English-language data (2410.05355.pdf, p. 1, 3). The data sources include:
*   **Web Data:** Primarily from RefinedWeb, a large, filtered dataset derived from Common Crawl. Parts of Fineweb-Edu were also used in the final training stage (2410.05355.pdf, p. 3-4).
*   **Curated Data:** A collection of books, scientific publications (arXiv, PubMed), patents (USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (2410.05355.pdf, p. 4).
*   **Code Data:** Sourced from The Stack dataset (2410.05355.pdf, p. 4).
*   **Math Data:** Sourced from the Proof-Pile-2 dataset and math-related web data (2410.05355.pdf, p. 4).
*   **Synthetic and Instruction Data:** In the final training stage, synthetic data from Cosmopedia and a small amount of multitask instruction data were introduced (2410.05355.pdf, p. 4).

The proportions of these data sources were varied across five distinct training stages, as detailed in Figure 1 of the technical report (2410.05355.pdf, p. 4).

### Motivation:
The training data was selected to build a strong, general-purpose language model. A curriculum learning approach was adopted, where the data mixture was adjusted to increase complexity and quality over time, with more scientific and high-quality data introduced in later stages (2410.05355.pdf, p. 4). Multilingual data was deliberately excluded to maximize performance in English for a model of this size (2410.05355.pdf, p. 3).

### Preprocessing:
*   **Tokenizer:** The same tokenizer as the Falcon series of models was used without modification (2410.05355.pdf, p. 3).
*   **Web Data Filtering:** The RefinedWeb data underwent extensive preprocessing, including language identification, line-wise and document-wise filtering, and both fuzzy and exact deduplication (2410.05355.pdf, p. 3).
*   **Conversation Data:** To handle conversational trees, a method was applied to enforce causal temporality, ensuring each conversation was used only once during training (2410.05355.pdf, p. 4).
*   **Packing:** To improve training efficiency, sequences were packed together. The proportions of short and long samples were carefully managed at each stage to avoid distribution shifts (2410.05355.pdf, p. 4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The technical report provides performance scores for the model on individual benchmarks. The results are presented for both the final model and the pre-decay checkpoint (2410.05355.pdf, Tables 2 & 3, p. 5).

**Selected Results for FalconMamba-7B (Final):**
*   **ARC-25:** 62.03
*   **MMLU-5:** 62.11
*   **GSM8K-5:** 52.54
*   **IFEval-0:** 33.36
*   **BBH-3:** 19.88
*   **MMLU-PRO-5:** 14.47
*   **GPQA-0:** 8.05
*   **MuSR-0:** 10.86

### Intersectional results:
Insufficient information. The provided documents do not contain performance results across combinations of factors (e.g., performance on a specific task for a specific demographic group).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** Approximately 14.55 GB to store the model weights (model.safetensors.index.json.txt).
*   **VRAM/RAM:** At least 14.5 GB of VRAM/RAM is required to load the model in `bfloat16` precision (config.json.txt).

### Deploying Requirements:
*   **GPU:** The model can fit sequences up to 16k tokens on a single 24 GB GPU (like an NVIDIA A10) using parallel prefill. With sequential prefill, it can process arbitrarily long prompts on the same hardware (2410.05355.pdf, Figure 2, p. 7). On an 80GB H100 GPU, it can generate up to 130k tokens with constant throughput and memory usage (2410.05355.pdf, Figure 3, p. 7).
*   **CPU:** The model is supported by the `llama.cpp` package, enabling deployment on local machines using CPU hardware (2410.05355.pdf, p. 8).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The model was pre-trained on a cluster of 256 NVIDIA H100 80GB GPUs (2410.05355.pdf, p. 3).
*   **Fine-tuning:** Fine-tuning is supported via the Hugging Face TRL (Transformer Reinforcement Learning) library, though specific hardware requirements are not provided (2410.05355.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers promote the responsible use of AI by releasing the model under a license that includes an Acceptable Use Policy (2410.05355.pdf, p. 8). The policy itself is not included in the repository but is available via a link.

The training data includes large-scale web data (Common Crawl) and user-generated content (Reddit, StackExchange), which may contain sensitive personal information, biases, or toxic content (2410.05355.pdf, p. 3-4). While the web data underwent filtering and deduplication, the extent to which these processes mitigate ethical risks is not detailed. The paper does not provide a broader discussion of potential risks, harms, or biases associated with the model's use.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **In-Context Learning:** The model may have "some limitations in in-context learning compared to Transformers" (2410.05355.pdf, p. 8).
*   **Limited Long-Context Training:** Although the architecture excels at long sequences, the pre-training strategy used a "rather medium 8k context length." Therefore, the model's proficiency on extra-long context tasks was not a primary focus of its training and remains an "underexplored area" (2410.05355.pdf, p. 8).
*   **Unexplored Scaling:** The effects of data scaling and model scaling for the Mamba architecture are less understood than for Transformers, leaving potential optimizations as an open area for research (2410.05355.pdf, p. 8).
*   **Multilingual Performance:** The model is not intended for multilingual applications, as it was trained primarily on English data (2410.05355.pdf, p. 3).

### Recommendations:
*   **Prompting:** To mitigate limitations in in-context learning, users can employ "high-quality data, especially Chain-of-Thought (CoT) instruction data or tailored prompting techniques" (2410.05355.pdf, p. 8).
*   **Continual Training:** The developers have released a "pre-decay checkpoint" to "support the community in further research or continual training on the model," particularly for those interested in exploring different data mixtures or training strategies (2410.05355.pdf, p. 4).
*   **Future Research:** The paper recommends future work on tailoring the training procedure for extra-large contexts to fully leverage the Mamba architecture's strengths for applications like audio and video generation (2410.05355.pdf, p. 8).