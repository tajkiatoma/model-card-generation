## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by a team of researchers from the Technology Innovation Institute (TII) in Abu Dhabi, United Arab Emirates. The authors listed are Jingwei Zuo, Maksim Velikanov, Dhia Eddine Rhaiem, Ilyas Chahed, Younes Belkada, Guillaume Kunsch, and Hakim Hacid (Source: 2410.05355.pdf, p. 1).

### Model date:
The technical report describing the model was submitted to arXiv on October 7, 2024 (Source: 2410.05355.pdf, p. 1).

### Model version:
The model is named Falcon Mamba 7B. A "pre-decay checkpoint" of the model is also released, which represents the model's state before the final learning rate decay stage of training. This pre-decay version shows a notable performance difference from the final model, and is released to support community research into training dynamics (Source: 2410.05355.pdf, p. 4, 5).

Falcon Mamba 7B is the first State Space Language Model (SSLM) in the FalconLLM series (Source: 2410.05355.pdf, p. 2). It is a pure Mamba-based model, distinguishing it from hybrid Mamba-Transformer models like Zamba 7B and Transformer-based models like Llama 3.1 and Mistral 7B (Source: 2410.05355.pdf, p. 1, 2).

### Model type:
Falcon Mamba 7B is a base large language model of the State Space Model (SSM) category, specifically using the Mamba architecture (Source: 2410.05355.pdf, p. 1, 2). It is an attention-free model designed for text generation (Source: 2410.05355.pdf, p. 1).

**Architecture Details:**
*   The model is based on the Mamba architecture (Gu & Dao, 2023), which uses a selective state space mechanism instead of attention (Source: 2410.05355.pdf, p. 2; mamba-paper.png).
*   It adds RMSNorm layers after the B, C, and Δ projections within each block to stabilize training (Source: 2410.05355.pdf, p. 3).
*   The input embeddings are untied from the output weights to increase model flexibility (Source: 2410.05355.pdf, p. 2).

**Model Size and Parameters:**
*   **Parameters:** 7.27 billion (Source: 2410.05355.pdf, p. 2, Table 1).
*   **Total Size:** 14.5 GB (Source: model.safetensors.index.json.txt).
*   **Layers:** 64 (Source: 2410.05355.pdf, p. 2, Table 1).
*   **Model Dimension (d_model):** 4096 (Source: 2410.05355.pdf, p. 2, Table 1).
*   **Vocabulary Size:** 65,024 (Source: 2410.05355.pdf, p. 2, Table 1; tokenizer_summary.json.txt).
*   **Context Length:** Unlike transformers, sequence length is not a fixed part of the Mamba architecture. The model can theoretically handle any sequence length during inference, though its practical ability is determined by the sequence lengths used during training (up to 8,192 tokens) (Source: 2410.05355.pdf, p. 2, 4).

### Training details:
The model was trained on 5.8 trillion tokens (Source: 2410.05355.pdf, p. 1).

*   **Hardware:** Training was conducted on 256 NVIDIA H100 80GB GPUs (Source: 2410.05355.pdf, p. 3).
*   **Framework:** The training utilized Data Parallelism (DP=256) combined with ZeRO optimization (Source: 2410.05355.pdf, p. 3).
*   **Optimizer:** AdamW optimizer was used with the following hyperparameters:
    *   β₁ = 0.9
    *   β₂ = 0.95
    *   ε = 10⁻⁸
    *   Weight decay = 0.1
    (Source: 2410.05355.pdf, p. 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was applied.
    *   Warmup duration: 1 trillion tokens.
    *   Stable learning rate (η_max): 6.4 × 10⁻⁴.
    *   Decay stage: The learning rate was reduced exponentially to η_max / 25 over the final 10% of training tokens (Source: 2410.05355.pdf, p. 3).
*   **Batching:** Batch size was linearly ramped up from 128 to 2048 over the first 50 trillion tokens. A "batch scaling" technique was used to keep the Adam optimizer's noise temperature constant by adjusting the learning rate when the batch size changed (Source: 2410.05355.pdf, p. 3).

### Paper or other resource for more information:
The primary resource is the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., Chahed, I., Belkada, Y., Kunsch, G., & Hacid, H. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355. (Source: 2410.05355.pdf).

The model weights are publicly available on Hugging Face:
*   https://huggingface.co/tiiuae/falcon-mamba-7b (Source: 2410.05355.pdf, p. 1).

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
(Source: 2410.05355.pdf).

### License:
The model is released under the Falcon Mamba 7B TII License, which is described as a permissive, Apache 2.0-based software license. It includes an acceptable use policy to promote the responsible use of AI (Source: 2410.05355.pdf, p. 8).
*   License Terms: https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html (Source: 2410.05355.pdf, p. 1, 8).
*   Acceptable Use Policy: https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html (Source: 2410.05355.pdf, p. 8).

### Contact:
For questions or feedback, the developers can be contacted at: `Falcon-LLM[at]tii[dot]ae` (Source: 2410.05355.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a pretrained, general-purpose base language model intended for text generation and understanding tasks (Source: 2410.05355.pdf, p. 1, 8). Due to its Mamba architecture, it is particularly well-suited for:
*   **Long-context generation:** The model maintains constant memory and throughput usage regardless of the sequence length, making it highly efficient for generating very long sequences (Source: 2410.05355.pdf, p. 8).
*   **Long-context reasoning tasks:** The model has shown strong performance on benchmarks that require long-context reasoning, such as MuSR (Source: 2410.05355.pdf, p. 6).
*   **Low-latency applications:** Its architectural efficiency makes it a candidate for real-world applications requiring large-scale, low-latency generation, such as for audio and video modalities (Source: 2410.05355.pdf, p. 8).

The model takes text as input and generates text as output.

### Primary intended users:
The paper does not explicitly define the primary users, but by making the model publicly available on Hugging Face under a permissive license, the intended users are likely AI researchers, developers, and practitioners who wish to build upon, fine-tune, or study state-of-the-art language models, particularly those with non-Transformer architectures (Source: 2410.05355.pdf, p. 1, 8).

### Out-of-scope uses:
*   **Multilingual tasks:** The model was trained primarily on English data, with multilingual data explicitly excluded from the pre-training corpus. Therefore, it is not intended for promising performance on multilingual tasks without further continual pre-training (Source: 2410.05355.pdf, p. 3).
*   Any use that violates the acceptable use policy is out-of-scope. This policy is available at https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html (Source: 2410.05355.pdf, p. 8).

---

## How to Use
This section outlines how to use the model.

The model is integrated into the Hugging Face ecosystem and can be used with the `transformers` library. It is also supported by `llama.cpp` for CPU-based deployment (Source: 2410.05355.pdf, p. 8).

For batched generation with sequences of varying lengths, left-side padding should be used. The model is designed to handle this by zeroing out the hidden states for padding tokens to ensure they do not influence predictions (Source: 2410.05355.pdf, p. 8; tokenizer_config.json.txt).

Below is a sample code snippet for using the model with the `transformers` library:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "tiiuae/falcon-mamba-7b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

inputs = tokenizer("The capital of the United Arab Emirates is", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```
*(Note: This code snippet is a standard usage example inferred from the model's availability in the Hugging Face Transformers library, as stated in the paper (Source: 2410.05355.pdf, p. 8).)*

The tokenizer includes several special tokens such as `>>TITLE<<`, `>>ABSTRACT<<`, and `>>QUESTION<<`, which may be used for specific prompting formats, though the paper does not provide examples (Source: tokenizer_config.json.txt; special_tokens_map.json.txt).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The technical report focuses on the following factors as relevant to model performance:
*   **Model Architecture:** The primary factor explored is the difference between pure SSM (Mamba), pure Transformer, and hybrid SSM-Transformer architectures (Source: 2410.05355.pdf, p. 4).
*   **Training Data Quality and Mixture:** The paper suggests that the quality of data and training strategies play a more crucial role than architecture in mitigating some of its inherent disadvantages (Source: 2410.05355.pdf, p. 6). The data mixture was varied across training stages (Source: 2410.05355.pdf, p. 4, Figure 1).
*   **Sequence Length:** Sequence length is a critical factor for memory consumption and throughput, especially when comparing the model to Transformers (Source: 2410.05355.pdf, p. 6).

### Evaluation factors:
The evaluation focuses on comparing Falcon Mamba 7B against other models based on their architectural category: State Space Models (SSMs), Transformers, and Hybrid models (Source: 2410.05355.pdf, p. 4).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a broad range of standard academic benchmarks, primarily from the Hugging Face Open LLM Leaderboard (v1 and v2). The average score across these benchmarks was used as a top-level metric (Source: 2410.05355.pdf, p. 5, Table 2 & 3).

Specific benchmarks include:
*   **Reasoning and Knowledge:** ARC-25, HellaSwag-10, MMLU-5, Winogrande-5, TruthfulQA-0, MMLU-Pro-5, BIG-Bench Hard (BBH)-3 (Source: 2410.05355.pdf, p. 5, Table 2 & 3).
*   **Math and Problem-Solving:** GSM8K-5, MATH-Lvl5-4 (Source: 2410.05355.pdf, p. 5, Table 2 & 3).
*   **Instruction Following:** IFEval-0 (Source: 2410.05355.pdf, p. 5, Table 3).
*   **Specialized Q&A:** GPQA-0, MuSR-0 (Source: 2410.05355.pdf, p. 5, Table 3).

In addition to correctness-based metrics, the model was also evaluated on:
*   **Throughput:** Measured in tokens per second (tok/s) (Source: 2410.05355.pdf, p. 7, Figure 3).
*   **Memory Consumption:** Peak GPU memory usage (Source: 2410.05355.pdf, p. 7, Figure 3).

### Decision thresholds:
Insufficient information. This is not applicable for a base generative model.

### Variation approaches:
Performance results for competitor models were extracted from the public Hugging Face Leaderboards (v1 and v2) to ensure unbiased comparison. When leaderboard results were not available, the best results from either the original papers or internal evaluations were used. Internal evaluations were performed using the `lm-evaluation-harness` and `lighteval` packages (Source: 2410.05355.pdf, p. 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a collection of publicly available academic benchmark datasets, selected from the Hugging Face Open LLM Leaderboard. These include:
*   ARC (AI2 Reasoning Challenge) (Source: 2410.05355.pdf, p. 5)
*   HellaSwag (Source: 2410.05355.pdf, p. 5)
*   MMLU (Massive Multitask Language Understanding) (Source: 2410.05355.pdf, p. 5)
*   Winogrande (Source: 2410.05355.pdf, p. 5)
*   TruthfulQA (Source: 2410.05355.pdf, p. 5)
*   GSM8K (Grade School Math 8K) (Source: 2410.05355.pdf, p. 5)
*   IFEval (Instruction Following Evaluation) (Source: 2410.05355.pdf, p. 5)
*   BIG-Bench Hard (BBH) (Source: 2410.05355.pdf, p. 5)
*   MATH (Mathematical Problem Solving) (Source: 2410.05355.pdf, p. 5)
*   GPQA (Graduate-Level Google-Proof Q&A) (Source: 2410.05355.pdf, p. 5)
*   MuSR (Multi-step Soft Reasoning) (Source: 2410.05355.pdf, p. 5)
*   MMLU-Pro (Source: 2410.05355.pdf, p. 5)

### Motivation:
These benchmarks were chosen because they are publicly available, independently conducted by HuggingFace, and collectively "span a broad range of top-level categories to assess the model's versatility and performance across various tasks" (Source: 2410.05355.pdf, p. 5).

### Preprocessing:
The evaluation was conducted in few-shot settings, with the number of shots specified for each benchmark (e.g., 0-shot for IFEval, 5-shots for MMLU, 25-shots for ARC) (Source: 2410.05355.pdf, p. 5). No other specific preprocessing steps for the evaluation data are described.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a dataset of 5.8 trillion tokens, consisting of a diverse mixture of English-language web data, curated documents, code, and math (Source: 2410.05355.pdf, p. 1, 3). The data sources include:
*   **Web Data:** Primarily from RefinedWeb, a high-quality filtered and deduplicated web dataset derived from Common Crawl. Parts of Fineweb-Edu were also used in the final training stage (Source: 2410.05355.pdf, p. 3, 4).
*   **Curated Data:** A collection of books, scientific publications (from arXiv and PubMed), patents (from USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (Source: 2410.05355.pdf, p. 4).
*   **Code Data:** Samples from The Stack dataset (Source: 2410.05355.pdf, p. 4).
*   **Math Data:** Data from the Proof-Pile-2 dataset and math data filtered from the web (Source: 2410.05355.pdf, p. 4).
*   **Instruction/Synthetic Data:** In the final decay stage, synthetic data from Cosmopedia and a small amount of multitask instruction data were introduced (Source: 2410.05355.pdf, p. 4).

The data mixture was adjusted across four training stages, progressively increasing the proportion of high-quality scientific data (Source: 2410.05355.pdf, p. 4, Figure 1).

### Motivation:
The training data was selected to create a strong, general-purpose language model. A curriculum learning approach was followed, where data diversity and complexity were increased in later training stages to enhance model capabilities (Source: 2410.05355.pdf, p. 4). The inclusion of instruction data in the final stage was motivated by the goal of enhancing the model's zero-shot and few-shot learning abilities (Source: 2410.05355.pdf, p. 4).

### Preprocessing:
*   **Web Data:** Raw Common Crawl data was processed to create RefinedWeb through language identification, line-wise and document-wise filtering, and both fuzzy and exact deduplication (Source: 2410.05355.pdf, p. 3).
*   **Conversation Data:** Conversation trees were processed to enforce causal temporality, ensuring each conversation was used only once during training (Source: 2410.05355.pdf, p. 4).
*   **Tokenization:** The same tokenizer as the Falcon series of models was used with no changes. It is a Byte-Pair Encoding (BPE) tokenizer (Source: 2410.05355.pdf, p. 3; tokenizer_summary.json.txt).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The performance of Falcon Mamba 7B on individual benchmarks is presented in Tables 2 and 3 of the technical report. Key results include:
*   **ARC-25:** 62.03 (Source: 2410.05355.pdf, p. 5, Table 2)
*   **MMLU-5:** 62.11 (Source: 2410.05355.pdf, p. 5, Table 2)
*   **GSM8K-5:** 52.54 (Source: 2410.05355.pdf, p. 5, Table 2)
*   **IFEval-0:** 33.36 (Source: 2410.05355.pdf, p. 5, Table 3)
*   **BBH-3:** 19.88 (Source: 2410.05355.pdf, p. 5, Table 3)
*   **MMLU-PRO-5:** 14.47 (Source: 2410.05355.pdf, p. 5, Table 3)

Throughput and memory analysis shows that Falcon Mamba 7B maintains a constant throughput (~13.5 tok/s) and constant peak memory usage on an H100 GPU when generating sequences up to 130k tokens, unlike Transformer models where performance degrades and memory usage increases linearly (Source: 2410.05355.pdf, p. 7, Figure 3).

### Intersectional results:
Insufficient information. The paper does not provide performance results across combinations of factors (e.g., by demographic group or domain).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
*   **GPU:** The model can process sequences up to 16,000 tokens long on a single 24 GB A10 GPU using parallel prefill. With sequential prefill, it can process arbitrarily long prompts on the same hardware (Source: 2410.05355.pdf, p. 7, Figure 2). On an 80GB H100 GPU, it maintains constant memory usage regardless of the number of generated tokens (Source: 2410.05355.pdf, p. 7, Figure 3).
*   **CPU:** The model is supported in the `llama.cpp` package, enabling deployment on local machines using CPU hardware (Source: 2410.05355.pdf, p. 8).

### Training or Fine-tuning Requirements:
*   **Pre-training:** The model was trained on a cluster of 256 NVIDIA H100 80GB GPUs (Source: 2410.05355.pdf, p. 3).
*   **Fine-tuning:** Fine-tuning is supported via the Hugging Face TRL (Transformer Reinforcement Learning) library (Source: 2410.05355.pdf, p. 8).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers promote the responsible use of the model through a licensing structure that includes a mandatory acceptable use policy (Source: 2410.05355.pdf, p. 8). The training data is sourced from large-scale web corpora (Common Crawl) and platforms with user-generated content (Reddit, StackExchange), which may contain biases, offensive content, or personal information (Source: 2410.05355.pdf, p. 3, 4). While the web data underwent filtering and deduplication, the extent of PII removal or bias mitigation is not detailed (Source: 2410.05355.pdf, p. 3). Potential risks are those common to large language models, such as generating harmful, biased, or inaccurate information. The primary mitigation strategy provided by the developers is the enforcement of the acceptable use policy, which users must adhere to.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers highlight several limitations:
*   **Limited In-Context Learning:** The model may show limitations in in-context learning tasks compared to state-of-the-art Transformers (Source: 2410.05355.pdf, p. 8).
*   **Medium-Length Context Training:** The training strategy focused on creating a strong general-purpose model and used a context length of up to 8k tokens. The model's full potential on extra-long context tasks was not the primary focus of the training procedure and remains an area for future exploration (Source: 2410.05355.pdf, p. 8).
*   **Unexplored Scaling Laws:** The effects of data and model scaling for the Mamba architecture are less understood than for Transformers, leaving potential optimizations as an open research area (Source: 2410.05355.pdf, p. 8).

### Recommendations:
*   **Usage for Batched Inference:** When performing batched generation with inputs of different lengths, users should use left-side padding (Source: 2410.05355.pdf, p. 8).
*   **Improving In-Context Learning:** The paper suggests that the model's limitations in in-context learning can be mitigated by using high-quality data, Chain-of-Thought (CoT) instruction data during fine-tuning, or applying tailored prompting techniques (Source: 2410.05355.pdf, p. 8).
*   **Future Research:** The developers recommend further research into tailoring the training procedure for extra-large contexts to fully leverage the Mamba architecture's strengths (Source: 2410.05355.pdf, p. 8).