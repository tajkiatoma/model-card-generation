## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, Falcon Mamba 7B, was developed by researchers Jingwei Zuo, Maksim Velikanov, Dhia Eddine Rhaiem, Ilyas Chahed, Younes Belkada, Guillaume Kunsch, and Hakim Hacid from the Technology Innovation Institute (TII) in Abu Dhabi, United Arab Emirates (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1). This model is part of the FalconLLM series (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).

### Model date:
The technical report describing the model is dated October 7, 2024 (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1). The model was developed using `transformers` version `4.43.0.dev0`, indicating recent development (config.json; generation_config.json).

### Model version:
The model is named Falcon Mamba 7B (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1). A separate "pre-decay checkpoint" is also available, which represents the model's state before the final learning rate decay stage of training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4, 8).

### Model type:
Falcon Mamba 7B is a decoder-only, causal language model based on a pure Mamba architecture, making it a State Space Language Model (SSLM) that is attention-free (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1-2). The architecture is specified as `FalconMambaForCausalLM` (config.json).

The Mamba architecture is a type of Selective State Space Model which processes sequential data by mapping an input `x` to an output `y` through a higher-dimensional latent state `h`. It uses input-dependent dynamics and a hardware-aware algorithm to efficiently manage memory (image-figure-1.png).

Key architectural parameters include:
*   **Parameters:** 7.27 billion (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Total Size:** 14.55 GB (model.safetensors.index.json).
*   **Layers:** 64 hidden layers (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Hidden Size (`d_model`):** 4096 (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Intermediate Size:** 8192 (config.json).
*   **Expansion Factor (E):** 2 (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **State Size (`state_size`):** 16 (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Convolution Kernel (`d_conv`):** 4 (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Vocabulary Size:** 65,024 (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, Table 1).
*   **Context Length:** The Mamba architecture does not have a fixed sequence length limit; any sequence length can be used during inference, with practical limits determined by the training data context length (up to 8192 tokens) and available memory (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2, 4).

### Training details:
The model was pre-trained on 5.8 trillion tokens using the following configuration (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 3):
*   **Algorithm:** The model was trained using the AdamW optimizer (β₁=0.9, β₂=0.95, ε=10⁻⁸, weight decay=0.1) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was used with a max learning rate of 6.4 × 10⁻⁴. The decay stage, which used an exponential schedule, constituted 10% of the total training tokens (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Batch Size:** A batch size ramp-up was employed, linearly increasing from 128 to 2048. Batch scaling was used to maintain a constant noise temperature for the optimizer (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Hardware and Parallelism:** Training was conducted on 256 H100 80GB GPUs, using Data Parallelism (DP=256) and ZeRO optimization (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Precision:** The model was trained with `bfloat16` precision (config.json).
*   **Stabilization:** To counter training instability and loss spikes observed with the Mamba architecture, RMSNorm layers were added after the B, C, and Δ parameters in each block (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2-3).
*   **Embeddings:** The model's input embeddings were untied from the output weights (`tie_word_embeddings: false`) to improve flexibility and performance (config.json; Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).

### Paper or other resource for more information:
The primary resource is the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., et al. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355. (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

The model weights and associated files are publicly available on Hugging Face:
*   **Main Model:** `https://huggingface.co/tiiuae/falcon-mamba-7b` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).
*   **Pre-decay Checkpoint:** `https://huggingface.co/tiiuae/falcon-mamba-7b-pre-decay` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

### Citation details:
To cite the model, please use the following BibTeX entry:
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
The model is released under the Falcon Mamba 7B TII License. This is a permissive, Apache 2.0-based license that includes an acceptable use policy to promote the responsible use of AI (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). The full license text can be found at: `https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 8).

### Contact:
For questions or feedback, the development team can be contacted at: `Falcon-LLM [at] tii[dot]ae` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a foundational, general-purpose language model intended for text generation (causal language modeling) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 8; config.json). Its Mamba architecture makes it particularly well-suited for tasks involving long sequences, as it maintains constant memory usage and throughput during generation. This makes it a strong candidate for applications requiring low-latency, large-scale generation, such as processing audio or video data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). The model has demonstrated competitive performance on various benchmarks, including few-shot learning (MMLU, ARC-25) and long-context reasoning (MuSR) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 6).

### Primary intended users:
The model is intended for AI researchers and developers. This is supported by its public release under a permissive license, its integration into the Hugging Face ecosystem, and the release of a pre-decay checkpoint to encourage further research and continual training on the model (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4, 8).

### Out-of-scope uses:
*   **Multilingual Applications:** The model was trained primarily on English data, as multilingual corpora were intentionally excluded. It is not designed for multilingual tasks without further fine-tuning or continual pre-training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Prohibited Uses:** Any use that violates the terms of the acceptable use policy is out-of-scope. The policy promotes the responsible use of AI (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **High-Stakes In-Context Learning:** The paper notes that the model may have limitations in in-context learning compared to Transformer-based models, so it may be less suitable for applications that heavily rely on this capability without specialized prompting techniques (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

---

## How to Use
This section outlines how to use the model.

The model is integrated into the Hugging Face ecosystem and can be used with the `transformers` library for tasks like inference, quantization, and fine-tuning (via the TRL library) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). It is also supported by the `llama.cpp` package for CPU-based deployment (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

When batching inputs of varying lengths, left-side padding should be used (`padding_side: "left"`) (tokenizer_config.json). The model is designed to handle this by zeroing out the hidden states corresponding to padding tokens to ensure they do not affect the generation output (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

The tokenizer includes several special tokens that can be used to structure prompts, such as `>>TITLE<<`, `>>ABSTRACT<<`, `>>QUESTION<<`, and `>>ANSWER<<`. The end-of-sequence token is `<|endoftext|>` (special_tokens_map.json; tokenizer.json).

No code snippets for usage are available in the provided repository data.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Model Architecture:** The model's performance is heavily influenced by its attention-free Mamba (SSM) architecture, which provides efficiency in long-context scenarios but may have different characteristics compared to Transformers in tasks like in-context learning (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, 8).
*   **Sequence Length:** The model's key advantage is its constant memory and throughput cost regardless of sequence length during generation, making this a critical factor for performance and efficiency (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 6-7).
*   **Data Quality and Training Strategy:** The developers suggest that the quality of pre-training data and the training strategies employed are crucial factors that can mitigate architectural disadvantages and significantly impact final performance (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 6).

### Evaluation factors:
The model's evaluation was analyzed across different factors:
*   **Architectural Category:** Performance was compared against models from three distinct architectural groups: pure State Space Models (like itself), Transformers, and Hybrid SSM-attention models (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Model Size:** The 7B model was benchmarked against other models of similar size (7B-9B) as well as larger models (11B, 12B, 14B) to situate its performance within the broader landscape (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, Tables 2 & 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's effectiveness was assessed using accuracy and task-specific scores on a wide range of public benchmarks, including (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, Tables 2 & 3):
*   **Reasoning and Knowledge:** MMLU, MMLU-Pro, ARC-25, HellaSwag-10, Winogrande-5, TruthfulQA-0, BIG-Bench Hard (BBH).
*   **Math and Problem-Solving:** GSM8K, MATH-Lvl5, GPQA, MuSR.
*   **Instruction Following:** IFEval.

Efficiency was measured using:
*   **Throughput:** Measured in tokens per second (tok/s) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).
*   **Memory Consumption:** Measured as peak GPU memory usage (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).

### Decision thresholds:
Insufficient information.

### Variation approaches:
To ensure robust and unbiased comparisons, performance metrics were sourced from independent evaluations on the public Hugging Face Leaderboards where possible. For models or benchmarks not on the leaderboards, results were taken from their respective technical reports or from internal evaluations conducted using standardized frameworks like `lm-evaluation-harness` and `lighteval` (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5). The number of few-shot examples (e.g., 0-shot, 5-shot) was kept consistent with standard benchmark practices (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a broad set of publicly available academic benchmarks to assess its capabilities in various domains (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5). These include:
*   **IFEval:** For instruction following.
*   **GSM8K, MATH-Lvl5, ARC Challenge, GPQA, MuSR:** For math, reasoning, and problem-solving.
*   **MMLU, MMLU-Pro, BIG-Bench Hard (BBH), HellaSwag-10, Winogrande-5, TruthfulQA-0:** For aggregate knowledge and reasoning abilities.

### Motivation:
These datasets were chosen because they are part of the public Hugging Face Leaderboards, which provides a source of independent and standardized evaluations. The collection of benchmarks was selected to "span a broad range of top-level categories to assess the model's versatility and performance across various tasks" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5).

### Preprocessing:
Insufficient information. The paper does not describe any specific preprocessing steps applied to the evaluation datasets.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a 5.8 trillion token dataset composed of a mixture of English-language web data, curated corpora, code, and math data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 1, 3). The data sources include:
*   **Web Data:** Primarily the **RefinedWeb** dataset, which is filtered and deduplicated from Common Crawl. Parts of **Fineweb-Edu** were also used in the final training stage (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3-4).
*   **Curated Data:** A collection of books, scientific publications (from arXiv and PubMed), patents (USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Code Data:** Sourced from **The Stack** dataset (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Math Data:** Sourced from **Proof-Pile-2** and additional math-related text filtered from web data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Synthetic and Instruction Data:** In the final decay stage, data from **Cosmopedia** and a small amount of multitask instruction data were introduced (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

The mixture of these datasets was varied across four training stages and a final decay stage, as detailed in Figure 1 of the technical report (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

### Motivation:
The training data was selected and staged according to a curriculum learning strategy. The goal was to progressively increase data complexity and introduce high-quality scientific data in later stages (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4). The final decay stage introduced even more diverse and high-quality data to "refine or shapen the knowledge learned," while a small portion of instruction data was added to improve zero-shot and few-shot capabilities (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

### Preprocessing:
*   **Filtering and Deduplication:** The RefinedWeb dataset was created by applying language identification, quality filtering, and both fuzzy and exact deduplication to Common Crawl data (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3). Code data from The Stack underwent the same pipeline (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Causal Temporality:** Conversation data was processed to enforce causal ordering, ensuring that each conversation was used only once during training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).
*   **Tokenization:** The model uses the same BPE tokenizer as the Falcon series of models (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3). The pre-tokenization process involves splitting by punctuation, applying byte-level encoding, handling digits, and splitting on specific regex patterns (tokenizer.json).
*   **Packing:** Sequences were packed together during pre-training. The proportions of short and long samples were managed at each stage to avoid distribution shifts (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Performance results on individual benchmarks are presented in Tables 2 and 3 of the technical report. These tables disaggregate performance by model, allowing for direct comparison. For example (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, Tables 2 & 3):
*   **GSM8K-5:** FalconMamba-7B scores 52.54, outperforming Mistral-7B-v0.1 (37.83) and Llama-3.1-8B (47.92).
*   **MMLU-PRO-5:** FalconMamba-7B scores 14.47, compared to Gemma-7B (21.64) and Mistral-Nemo-Base-2407 (12B) (27.46).
*   **Throughput:** At 131,072 generated tokens, FalconMamba-7B maintains a throughput of 13.53 tok/s, while Mistral-7B's throughput drops to 4.27 tok/s (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).

### Intersectional results:
The provided tables allow for intersectional analysis across model architecture and benchmark category. For instance, one can compare the performance of pure SSM models (like Falcon Mamba) against Transformer models on reasoning tasks (e.g., GSM8K) versus aggregate knowledge tasks (e.g., MMLU) (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 5, Tables 2 & 3). However, the paper does not explicitly present results for intersections of more than two factors.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights have a total size of 14.55 GB (model.safetensors.index.json). Loading the model in its training precision (`bfloat16`) would require approximately 14.55 GB of RAM or VRAM, plus overhead (config.json).

### Deploying Requirements:
*   **GPU:** On a single 24 GB A10 GPU with float32 precision, the model can process a maximum context length of 16,000 tokens using parallel prefill. With sequential prefill, it can handle arbitrarily long prompts (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 2).
*   **Memory Efficiency:** During generation, the model's peak memory usage remains constant regardless of the number of tokens generated, unlike Transformer models where memory usage scales linearly with context length (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 7, Figure 3).
*   **CPU:** The model is supported in the `llama.cpp` package, enabling deployment on standard CPU hardware (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).

### Training or Fine-tuning Requirements:
The model was pre-trained on a cluster of 256 NVIDIA H100 80GB GPUs (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers have released the model with an acceptable use policy to guide its application toward responsible and ethical purposes (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8). The training data includes content from public web sources and conversation platforms like Reddit, which may contain sensitive personal information or reflect societal biases (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 4). The provided documents do not detail specific steps taken to anonymize this data or mitigate biases, beyond the general filtering and deduplication applied to the web corpus. The potential risks associated with the model's use are not explicitly enumerated, but are governed by the linked acceptable use policy.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **In-Context Learning Limitations:** The paper acknowledges that pure Mamba models like this one may show "some limitations in in-context learning compared to Transformers" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Untested Long-Context Proficiency:** While the architecture is highly efficient for long sequences, the model was trained with a "medium 8k context length." Its actual performance on extra-large context tasks remains an "underexplored area" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Language Limitation:** The model is intended for English-language use only. Multilingual data was deliberately excluded from training, so it will not perform well in other languages without additional training (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 3).
*   **Training Instability:** The Mamba architecture is noted to be more sensitive to hyperparameters like learning rate than Transformers, which can lead to training instabilities (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 2).

### Recommendations:
*   **Use Specialized Prompting:** To mitigate potential weaknesses in in-context learning, users are encouraged to use "high-quality data, especially Chain-of-Thought (CoT) instruction data or tailored prompting techniques" (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).
*   **Use Sequential Prefill for Long Prompts:** For applications with very long input prompts, users should leverage sequential prefill to avoid the memory scaling issues associated with parallel prefill, thereby unlocking the model's ability to process arbitrarily long sequences (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 6).
*   **Further Research:** The developers recommend further community research into scaling Mamba models, optimizing their training for very long contexts, and exploring optimal ways to create hybrid SSM-attention architectures (Falcon Mamba: The First Competitive Attention-free 7B Language Model, p. 8).