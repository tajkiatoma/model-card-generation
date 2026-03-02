## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by the Technology Innovation Institute (TII) in Abu Dhabi, United Arab Emirates (2410.05355.pdf, p. 1).

### Model date:
The technical report presenting the model was submitted to arXiv on October 7, 2024 (2410.05355.pdf, p. 1).

### Model version:
The primary model is **Falcon Mamba 7B**. A **pre-decay checkpoint** is also released to support community research and continual training (2410.05355.pdf, p. 4).

As a pure Mamba-based model, Falcon Mamba 7B is presented as the first competitive attention-free model at the 7B scale. It surpasses other leading open-weight models based on Transformers (like Mistral 7B and Llama3.1 8B), other State Space Models (like RWKV-v6), and hybrid Mamba-Transformer models (like Zamba 7B) on various benchmarks (2410.05355.pdf, p. 1, 5).

### Model type:
Falcon Mamba 7B is a decoder-only, causal language model based on the pure Mamba architecture, making it a State Space Language Model (SSLM) (2410.05355.pdf, p. 1-2). It is an attention-free model designed for efficient processing of long sequences (2410.05355.pdf, p. 1). The Mamba architecture uses a selection mechanism with structured state space models (SSMs) to handle input-dependent dynamics efficiently, as illustrated in the architecture diagram (mamba-paper.png).

Key architectural details include:
*   **Model Type:** `falcon_mamba` (config.json.txt).
*   **Architecture Class:** `FalconMambaForCausalLM` (config.json.txt).
*   **Parameters:** 7.27 billion (2410.05355.pdf, p. 2).
*   **Total Size:** ~14.55 GB (model.safetensors.index.json.txt).
*   **Layers:** 64 hidden layers (config.json.txt; 2410.05355.pdf, p. 2).
*   **Hidden Size (`d_model`):** 4096 (config.json.txt; 2410.05355.pdf, p. 2).
*   **Intermediate Size:** 8192 (config.json.txt).
*   **State Size (`state_size`):** 16 (config.json.txt; 2410.05355.pdf, p. 2).
*   **Convolution Kernel (`conv_kernel`):** 4 (config.json.txt; 2410.05355.pdf, p. 2).
*   **Vocabulary Size:** 65,024 (config.json.txt; 2410.05355.pdf, p. 2).
*   **Precision:** `bfloat16` (config.json.txt).
*   **Embeddings:** Input embeddings are untied from the output weights to increase model flexibility (2410.05355.pdf, p. 2).

The model uses a Byte-Pair Encoding (BPE) tokenizer (tokenizer_summary.json.txt).

### Training details:
The model was pre-trained on 5.8 trillion tokens (2410.05355.pdf, p. 1). The training process included the following:

*   **Algorithm:** The model was trained using the AdamW optimizer with the following parameters: β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸, and a weight decay of 0.1 (2410.05355.pdf, p. 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was used. It included a warmup phase of 1 trillion tokens, a stable phase with a maximum learning rate of 6.4 × 10⁻⁴, and an exponential decay phase for the final 10% of training tokens (2410.05355.pdf, p. 3).
*   **Batch Size:** The batch size was linearly increased from 128 to 2048 over the first 50 trillion tokens. Batch scaling was applied to keep the Adam noise temperature constant (2410.05355.pdf, p. 3).
*   **Sequence Length:** Training followed a curriculum learning approach, progressively increasing the sequence length from 2048 up to 8192 across four stages (2410.05355.pdf, p. 4).
*   **Stabilization:** To improve training stability, RMSNorm layers were added after the B, C, and Δ projections within each Mamba block (2410.05355.pdf, p. 3).
*   **Hardware and Parallelism:** Training was conducted on 256 NVIDIA H100 80GB GPUs using Data Parallelism (DP=256) and ZeRO optimization (2410.05355.pdf, p. 3).

### Paper or other resource for more information:
The primary resource is the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., Chahed, I., Belkada, Y., Kunsch, G., & Hacid, H. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355. (2410.05355.pdf).

The paper provides a detailed overview of the model architecture, training process, data mixtures, and evaluation results. The model weights are publicly available on Hugging Face (2410.05355.pdf, p. 1).

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
(Citation derived from 2410.05355.pdf)

### License:
The Falcon Mamba 7B models are available under the "Falcon Mamba 7B TII License," which is described as a permissive Apache 2.0-based software license. It includes an acceptable use policy to promote the responsible use of AI (2410.05355.pdf, p. 8). The full terms and conditions are available at `https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html` (2410.05355.pdf, p. 1, 8).

### Contact:
For questions or feedback, the development team can be contacted at: `Falcon-LLM [at] tii[dot]ae` (2410.05355.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a pre-trained, base large language model intended for general-purpose use (2410.05355.pdf, p. 1, 8). Its core capabilities are text generation and understanding. Due to its Mamba architecture, it is particularly well-suited for tasks requiring the processing of long sequences, as it offers significantly faster inference and lower memory consumption for long context generation compared to Transformer-based models (2410.05355.pdf, p. 1, 6).

The model has demonstrated strong performance on a variety of tasks, including:
*   Few-shot learning and reasoning (e.g., MMLU, ARC-25) (2410.05355.pdf, p. 6).
*   Math and problem-solving (e.g., GSM8K) (2410.05355.pdf, p. 6).
*   Long-context reasoning (e.g., MuSR) (2410.05355.pdf, p. 6).

It is a causal language model, meaning it takes a sequence of text as input and predicts the next token (config.json.txt).

### Primary intended users:
The paper does not explicitly define the primary intended users. However, by making the model publicly available on Hugging Face under a permissive license and providing details for fine-tuning and deployment, the intended users are likely AI/ML researchers, developers, and practitioners who wish to build upon, study, or deploy advanced language models (2410.05355.pdf, p. 1, 8).

### Out-of-scope uses:
The model is a base model and has not been fine-tuned for specific safety protocols, so it may generate problematic content without further alignment. The model is released with an acceptable use policy that outlines prohibited uses (2410.05355.pdf, p. 8). The paper also notes that pure Mamba designs may show limitations in in-context learning tasks compared to Transformers, suggesting it may be less suitable for applications that heavily rely on this capability without specific prompting techniques or fine-tuning (2410.05355.pdf, p. 8).

---

## How to Use
This section outlines how to use the model.

The model is integrated into the Hugging Face ecosystem and can be used with the `transformers` library (2410.05355.pdf, p. 8). Below is a code snippet demonstrating how to load the model and tokenizer to generate text.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Specify the model repository ID
model_id = "tiiuae/falcon-mamba-7b"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load the model
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16, # As specified in config.json.txt
    device_map="auto"
)

# Define the input prompt
prompt = "The capital of the United Arab Emirates is"

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate text
# generation_config.json specifies eos_token_id=11
outputs = model.generate(**inputs, max_new_tokens=20, eos_token_id=11)

# Decode and print the output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

The model supports quantization and can be fine-tuned using the TRL library. It is also available in GGUF format for CPU-based inference with tools like `llama.cpp` (2410.05355.pdf, p. 8).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors identified during its development:
*   **Data Quality and Mixture:** The selection and mixture of data across different training stages were crucial. The training curriculum was designed to introduce higher-quality and more complex data (e.g., scientific, code, math) in later stages to improve performance (2410.05355.pdf, p. 4).
*   **Sequence Length:** The Mamba architecture is designed to handle long sequences efficiently. While the model was trained with a context length up to 8192 tokens, its ability to process even longer sequences during inference is a key architectural advantage (2410.05355.pdf, p. 2, 4, 8).
*   **Training Strategy:** Hyperparameters such as learning rate and batch size, as well as techniques like batch scaling, were found to significantly affect training stability and final model performance (2410.05355.pdf, p. 2-3).

### Evaluation factors:
The model was evaluated based on its performance across different architectural categories: pure State Space Models (SSMs), Transformers, and Hybrid models. This allows for a direct comparison of the pure Mamba design against other state-of-the-art approaches (2410.05355.pdf, p. 4).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a wide range of standard academic benchmarks, with results reported as accuracy or other task-specific scores. The benchmarks cover instruction following, math, reasoning, problem-solving, and aggregate knowledge. Key benchmarks include:
*   **ARC-25, HellaSwag-10, MMLU-5, Winogrande-5, TruthfulQA-0, GSM8K-5** (from HF Leaderboard v1) (2410.05355.pdf, p. 5, Table 2).
*   **IFEval-0, BBH-3, Math-Lvl5-4, GPQA-0, MuSR-0, MMLU-PRO-5** (from HF Leaderboard v2) (2410.05355.pdf, p. 5, Table 3).

### Decision thresholds:
Insufficient information. This is not applicable for a generative base model.

### Variation approaches:
Performance results were primarily extracted from the public Hugging Face Open LLM Leaderboards (v1 and v2) to ensure unbiased comparison. For models or benchmarks where leaderboard results were unavailable, internal evaluations were performed using the `lm-evaluation-harness` and `lighteval` packages. The evaluations were conducted in few-shot settings (e.g., 0-shot, 3-shot, 5-shot, 25-shot) as specified for each benchmark (2410.05355.pdf, p. 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a collection of publicly available academic benchmarks spanning various capabilities (2410.05355.pdf, p. 5):
*   **Instruction Following:** IFEval
*   **Math & Reasoning:** GSM8K, MATH-Lvl5, ARC Challenge
*   **Problem Solving & Knowledge:** GPQA, MuSR
*   **Aggregate Benchmarks:** MMLU, MMLU-Pro, BIG-Bench Hard (BBH)

### Motivation:
These benchmarks were selected because their results are publicly available and independently conducted by Hugging Face. They cover a "broad range of top-level categories to assess the model's versatility and performance across various tasks" (2410.05355.pdf, p. 5).

### Preprocessing:
The paper does not describe any specific preprocessing steps for the evaluation data beyond the standard formatting required for the few-shot evaluation settings of each benchmark (2410.05355.pdf, p. 5).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a diverse mixture of 5.8 trillion tokens, primarily in English (2410.05355.pdf, p. 1, 3). The training corpus was composed of:
*   **Web Data:** The majority of the data comes from RefinedWeb, a high-quality, filtered, and deduplicated web dataset derived from Common Crawl (2410.05355.pdf, p. 3). In the final decay stage, parts of Fineweb-Edu were also used (2410.05355.pdf, p. 4).
*   **Curated Data:** This includes books, scientific publications (arXiv, PubMed), patents (USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (2410.05355.pdf, p. 4).
*   **Code Data:** Samples were taken from The Stack dataset (2410.05355.pdf, p. 4).
*   **Math Data:** Data from Proof-Pile-2 was used, along with math data filtered from the web (2410.05355.pdf, p. 4).
*   **Synthetic & Instruction Data:** In the final decay stage, synthetic data from Cosmopedia and a small portion of multitask instruction data were introduced (2410.05355.pdf, p. 4).

The data mixture varied across five training stages, following a curriculum learning approach (2410.05355.pdf, p. 4, Figure 1).

### Motivation:
The dataset was chosen to create a "high-quality English pre-training dataset" (2410.05355.pdf, p. 3). The curriculum learning strategy, which gradually increased the proportion of high-quality scientific, code, and math data, was designed to improve model capabilities over the course of training (2410.05355.pdf, p. 4). The inclusion of a small amount of instruction data in the final stage was intended to enhance the model's zero-shot and few-shot learning abilities (2410.05355.pdf, p. 4).

### Preprocessing:
The following preprocessing steps were applied to the training data:
*   **Web Data:** Raw Common Crawl data was filtered using language identification, line-wise and document-wise filtering, and both fuzzy and exact deduplication to create the RefinedWeb dataset (2410.05355.pdf, p. 3).
*   **Conversational Data:** Conversation trees were processed to enforce "causal temporality," ensuring that each conversation was used only once during training (2410.05355.pdf, p. 4).
*   **Tokenization:** The same tokenizer as the Falcon series was used (2410.05355.pdf, p. 3). It is a BPE tokenizer with a vocabulary of 65,024 tokens (tokenizer_summary.json.txt).
*   **Packing:** Packing was used during pretraining, and the proportions of short and long samples were carefully selected at each stage to avoid distribution shifts (2410.05355.pdf, p. 4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The model's performance was benchmarked against other models, grouped by architecture type. Falcon Mamba 7B consistently outperforms or matches other 7B-scale models.

**HF Leaderboard v1 Tasks (Average Score):**
*   **FalconMamba-7B:** 64.09
*   Falcon2-11B (Transformer): 64.28
*   Gemma-7B (Transformer): 63.75
*   Meta-llama-3.1-8B (Transformer): 62.28
*   Zyphra/Zamba-7B-v1 (Hybrid): 60.00
*   RWKV-v6-Finch-14B (RWKV): 55.57
(2410.05355.pdf, p. 5, Table 2)

**HF Leaderboard v2 Tasks (Average Score):**
*   **FalconMamba-7B:** 15.04
*   Gemma-7B (Transformer): 15.28
*   Mistral-Nemo-Base-2407 (12B, Transformer): 15.08
*   Mistral-7B-v0.1 (Transformer): 14.50
*   RecurrentGemma-9b (Hybrid): 13.20
*   RWKV-v6-Finch-14B (RWKV): 10.55
(2410.05355.pdf, p. 5, Table 3)

The results demonstrate that Falcon Mamba 7B is the first attention-free model to achieve performance competitive with top-tier Transformer models of a similar scale (2410.05355.pdf, p. 1, 6).

### Intersectional results:
Insufficient information. The paper does not provide performance results disaggregated by demographic or other intersectional factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights have a total size of approximately 14.55 GB (model.safetensors.index.json.txt). As the model was trained and is typically used with `bfloat16` precision (config.json.txt), it requires at least 15 GB of GPU VRAM to be loaded.

### Deploying Requirements:
*   **GPU:** On a single 24GB A10 GPU, the model can process a maximum context length of 16k tokens with parallel prefill. With sequential prefill, it can process arbitrarily long prompts (2410.05355.pdf, p. 7, Figure 2).
*   **Inference Performance:** During long sequence generation (up to 130k tokens) on an 80GB H100 GPU, Falcon Mamba 7B maintains a constant throughput and peak memory usage, unlike Transformer models where memory usage grows linearly and throughput decreases (2410.05355.pdf, p. 7, Figure 3).
*   **CPU:** The model is supported by the `llama.cpp` package, enabling deployment on local machines using CPU hardware (2410.05355.pdf, p. 8).

### Training or Fine-tuning Requirements:
The model was pre-trained on 256 NVIDIA H100 80GB GPUs (2410.05355.pdf, p. 3). Fine-tuning would require a similar class of hardware, though potentially with fewer devices depending on the scale of the task.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The model is released with an "acceptable use policy that promotes the responsible use of AI" (2410.05355.pdf, p. 8). This policy is part of the model's license. The provided documents do not contain the policy itself but link to it. As a base model, it has not undergone specific safety alignment or fine-tuning, which means it could potentially generate harmful, biased, or inaccurate content. Users should implement their own safety measures and guardrails before deploying the model in any application. The paper does not provide details on the use of sensitive data or specific risk mitigation strategies beyond the acceptable use policy.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers acknowledge the following limitations:
*   **In-Context Learning:** The model may have "potentially some limitations in in-context learning compared to Transformers" (2410.05355.pdf, p. 8).
*   **Long-Context Training:** Although the architecture is well-suited for long contexts, the pre-training strategy used a "rather medium 8k context length." The model's proficiency on extra-large contexts was not a primary focus of the training and remains an "unexplored area for future research" (2410.05355.pdf, p. 8).
*   **Architecture Scaling:** The effects of data scaling and model scaling for the Mamba architecture are less explored in the literature compared to Transformers, leaving potential optimizations as an open research area (2410.05355.pdf, p. 8).

### Recommendations:
Based on the model's characteristics and limitations, the developers suggest:
*   **Prompting:** To mitigate potential weaknesses in in-context learning, users can employ high-quality data, Chain-of-Thought (CoT) instruction data, or tailored prompting techniques (2410.05355.pdf, p. 8).
*   **Future Research:** The developers encourage further research into tailoring training procedures for extra-large contexts to fully leverage the Mamba architecture's capabilities (2410.05355.pdf, p. 8).
*   **Hybrid Models:** The paper notes that exploring hybrid models that combine the complementary features of SSMs and attention remains a promising direction for future work (2410.05355.pdf, p. 8).
*   **Continual Training:** The released pre-decay checkpoint can be used by the community for further research or to continue training on more high-quality data (2410.05355.pdf, p. 4).