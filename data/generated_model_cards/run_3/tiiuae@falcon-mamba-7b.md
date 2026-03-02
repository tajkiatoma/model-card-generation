## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers at the Technology Innovation Institute (TII) in Abu Dhabi, United Arab Emirates (technical_report.pdf, page 1). The authors of the technical report are Jingwei Zuo, Maksim Velikanov, Dhia Eddine Rhaiem, Ilyas Chahed, Younes Belkada, Guillaume Kunsch, and Hakim Hacid (technical_report.pdf, page 1).

### Model date:
The technical report describing the model was submitted to arXiv on October 7, 2024 (technical_report.pdf, page 1).

### Model version:
The model is named Falcon Mamba 7B (technical_report.pdf, page 1). A "pre-decay checkpoint" of the model is also released to support further research and continual training. This checkpoint is from before the final learning rate decay stage of training, and the final model shows a "notable performance boost" compared to this checkpoint (technical_report.pdf, pages 4, 6).

As a pure Mamba-based model, Falcon Mamba 7B is presented as a competitive attention-free alternative to Transformer-based models like Mistral 7B and Llama3.1 8B, as well as hybrid models like Zamba 7B (technical_report.pdf, page 1).

### Model type:
Falcon Mamba 7B is a base large language model for causal language modeling, built on a pure Mamba architecture, making it a State Space Language Model (SSLM) (technical_report.pdf, pages 1, 2). It is described as the "first competitive attention-free 7B language model" (technical_report.pdf, page 1).

**Architecture:**
The model's architecture is `FalconMambaForCausalLM` (`config.json`) and is based on the Mamba architecture (Gu & Dao, 2023), which uses Selective State Space Models (SSMs) (technical_report.pdf, page 2). The core idea of SSMs is to map an input sequence to an output through a higher-dimensional latent state, using a selection mechanism to introduce input-dependent dynamics efficiently (image-1.png). Unlike Transformers, sequence length is not a fixed part of the Mamba architecture, allowing for variable sequence lengths during inference (technical_report.pdf, page 2).

**Key Parameters:**
*   **Parameters:** 7.27 Billion (technical_report.pdf, page 2, Table 1)
*   **Total Size:** 14.55 GB (`model.safetensors.index.json`)
*   **Layers:** 64 (`config.json`; technical_report.pdf, page 2, Table 1)
*   **Hidden Size (`d_model`):** 4096 (`config.json`; technical_report.pdf, page 2, Table 1)
*   **Intermediate Size:** 8192 (`config.json`)
*   **Expansion Factor (E):** 2 (technical_report.pdf, page 2, Table 1)
*   **State Dimension (N):** 16 (`config.json`; technical_report.pdf, page 2, Table 1)
*   **Convolution Kernel Size (`d_conv`):** 4 (`config.json`; technical_report.pdf, page 2, Table 1)
*   **Vocabulary Size:** 65024 (`config.json`; technical_report.pdf, page 2, Table 1)
*   **Precision:** bfloat16 (`config.json`)

### Training details:
The model was pre-trained on 5.8 trillion tokens (technical_report.pdf, page 1).

*   **Hardware:** The training was conducted on 256 H100 80GB GPUs (technical_report.pdf, page 3).
*   **Parallelism:** The training utilized Data Parallelism (DP=256) combined with ZeRO optimization (technical_report.pdf, page 3).
*   **Optimizer:** The AdamW optimizer was used with the following parameters: β₁ = 0.9, β₂ = 0.95, ε = 10⁻⁸, and a weight decay of 0.1 (technical_report.pdf, page 3).
*   **Learning Rate Schedule:** A warmup-stable-decay (WSD) schedule was applied. It included a fixed warmup duration of 1 trillion tokens, a stable stage with a learning rate of 6.4 × 10⁻⁴, and a final decay stage for approximately 10% of the total training tokens, where the learning rate was reduced exponentially (technical_report.pdf, page 3).
*   **Batching:** A batch size ramp-up was used, linearly increasing from 128 to 2048 over the first 50 trillion tokens. Batch scaling was applied to the learning rate to maintain a constant gradient noise temperature (technical_report.pdf, page 3).
*   **Stabilization:** To stabilize training, RMSNorm layers were added after the B, C, and Δ parameters in each block. The developers noted that the Mamba architecture was more sensitive to learning rates than Transformers, leading to occasional loss spikes (technical_report.pdf, pages 2-3).

### Paper or other resource for more information:
A detailed overview of the model is available in the technical report:
*   Zuo, J., Velikanov, M., Rhaiem, D. E., Chahed, I., Belkada, Y., Kunsch, G., & Hacid, H. (2024). *Falcon Mamba: The First Competitive Attention-free 7B Language Model*. arXiv preprint arXiv:2410.05355. (technical_report.pdf)

The model weights are publicly available on Hugging Face at: `https://huggingface.co/tiiuae/falcon-mamba-7b` (technical_report.pdf, page 1).

### Citation details:
Insufficient information.

### License:
The model is available under the "Falcon Mamba 7B TII License," which is described as a permissive Apache 2.0-based software license. It includes an acceptable use policy to promote the responsible use of AI (technical_report.pdf, page 8).
*   **License Terms:** `https://falconllm.tii.ae/falcon-mamba-7b-terms-and-conditions.html` (technical_report.pdf, page 8)
*   **Acceptable Use Policy:** `https://falconllm.tii.ae/falcon-mamba-7b-acceptable-use-policy.html` (technical_report.pdf, page 8)

### Contact:
For questions or feedback, the development team can be contacted at: `Falcon-LLM [at] tii[dot]ae` (technical_report.pdf, page 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Falcon Mamba 7B is a pre-trained, general-purpose base language model (technical_report.pdf, pages 1, 8). Its primary intended use is as a foundation for further fine-tuning on specific downstream tasks.

Due to the linear-time complexity and constant memory usage of the Mamba architecture during inference, the model is particularly well-suited for applications requiring long sequence generation and reasoning. It is significantly faster and requires substantially less memory for long sequences compared to Transformer-based models (technical_report.pdf, page 1). The model has shown strong performance on long-context reasoning tasks like MuSR (technical_report.pdf, page 6). The model takes `input_ids` and an `attention_mask` as input and generates a sequence of tokens as output (`tokenizer_config.json`).

### Primary intended users:
The paper does not explicitly define the primary users, but by making the model publicly available on Hugging Face under a permissive license, the intended users are likely AI researchers, developers, and practitioners who wish to build upon or experiment with a powerful, non-Transformer-based language model (technical_report.pdf, pages 1, 8).

### Out-of-scope uses:
The model is released with an acceptable use policy that outlines restrictions and promotes responsible use. Any use that violates this policy is out-of-scope (technical_report.pdf, page 8). The paper also notes that the model may have limitations in in-context learning compared to Transformers, suggesting it might be less suitable for tasks that heavily rely on this capability without specific fine-tuning or prompting strategies (technical_report.pdf, page 8).

---

## How to Use
This section outlines how to use the model.

The model is fully integrated into the Hugging Face ecosystem and can be used with the `transformers` library for tasks like inference, quantization, and fine-tuning (via the TRL library) (technical_report.pdf, page 8). It is also supported by the `llama.cpp` package for deployment on local CPUs (technical_report.pdf, page 8).

The model expects input to be tokenized into `input_ids` and an `attention_mask` (`tokenizer_config.json`). The tokenizer includes several special tokens such as `>>TITLE<<`, `>>ABSTRACT<<`, and `>>QUESTION<<` that can be used to structure prompts (`special_tokens_map.json`, `tokenizer.json`).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The technical report highlights the following factors as relevant to the model's performance:
*   **Architecture:** The model's pure Mamba (attention-free) architecture is a key factor, influencing its efficiency with long sequences and its performance characteristics compared to Transformer and hybrid Mamba-Transformer models (technical_report.pdf, pages 1, 6).
*   **Training Data:** The quality, diversity, and mixture of the training data are identified as crucial factors. The model's performance was shaped by a curriculum learning strategy where data mixtures were adjusted across training stages (technical_report.pdf, pages 4, 6).
*   **Training Strategy:** The learning rate schedule, batch size, and stabilization techniques were important for achieving stable training and optimal performance (technical_report.pdf, page 3).

### Evaluation factors:
The model's evaluation focused on comparing its performance against other models based on their architecture type:
*   Pure State Space Models (SSMs)
*   Transformer models
*   Hybrid SSM-attention models
(technical_report.pdf, page 4)

Additionally, the evaluation disaggregates results between the final model and its "pre-decay" checkpoint to show the impact of the final training stage (technical_report.pdf, page 5, Tables 2 & 3).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The model's performance was assessed using a broad range of academic benchmarks, primarily sourced from the Hugging Face Open LLM Leaderboard (v1 and v2) (technical_report.pdf, page 5).

*   **Reasoning and Problem-Solving:**
    *   **GSM8K (5-shot):** Math word problems.
    *   **MATH-Lvl5 (4-shot):** Mathematical problem solving.
    *   **ARC Challenge (25-shot):** Grade-school science questions.
    *   **GPQA (0-shot):** Graduate-level Google-proof Q&A.
    *   **MuSR (0-shot):** Multi-step soft reasoning.
*   **Aggregate and Multitask Understanding:**
    *   **MMLU (5-shot):** Massive multitask language understanding.
    *   **MMLU-Pro (5-shot):** A more robust version of MMLU.
    *   **BIG-Bench Hard (BBH) (3-shot):** A suite of challenging tasks.
*   **Instruction Following:**
    *   **IFEval (0-shot):** Instruction following evaluation.
*   **Other Common Benchmarks:**
    *   **HellaSwag (10-shot), Winogrande (5-shot), TruthfulQA (0-shot).**
*   **Efficiency Metrics:**
    *   **Throughput (tok/s):** Generation speed.
    *   **Maximum GPU memory occupied:** Memory consumption during inference.
(All metrics sourced from technical_report.pdf, pages 5, 7)

### Decision thresholds:
Insufficient information. This is not applicable for a generative base model.

### Variation approaches:
To ensure unbiased comparisons, results were taken directly from public leaderboards where possible. For models or benchmarks not on the leaderboards, internal evaluations were conducted using standard frameworks like `lm-evaluation-harness` and `lighteval` (technical_report.pdf, page 5). The number of few-shot examples (e.g., 0-shot, 5-shot, 25-shot) was varied depending on the standard evaluation protocol for each benchmark (technical_report.pdf, page 5).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of publicly available benchmark datasets to assess its capabilities in different domains (technical_report.pdf, page 5). These include:
*   **IFEval**
*   **GSM8K**
*   **MATH-Lvl5**
*   **ARC Challenge**
*   **GPQA**
*   **MuSR**
*   **MMLU**
*   **MMLU-Pro**
*   **BIG-Bench Hard (BBH)**
*   **HellaSwag**
*   **Winogrande**
*   **TruthfulQA**

### Motivation:
These benchmarks were selected because they are part of the Hugging Face Open LLM Leaderboard, which provides independent and public results. The collection was chosen to "span a broad range of top-level categories to assess the model's versatility and performance across various tasks," including instruction following, reasoning, and general knowledge (technical_report.pdf, page 5).

### Preprocessing:
The technical report does not detail specific preprocessing steps for the evaluation data, but it does specify the number of few-shot examples used for each task, implying that the data was formatted into prompts according to each benchmark's standard (technical_report.pdf, page 5).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a 5.8 trillion token dataset composed of a diverse mixture of web data, curated text, code, and math (technical_report.pdf, pages 1, 3). The data sources include:
*   **Web Data:** Primarily from **RefinedWeb**, a high-quality, five-trillion-token English dataset derived from Common Crawl. Parts of **Fineweb-Edu** were also used in the final training stage (technical_report.pdf, pages 3-4).
*   **Curated Data:** A collection of books, scientific publications (from arXiv and PubMed), patents (USPTO), and conversations from platforms like Reddit, StackExchange, and Hackernews (technical_report.pdf, page 4).
*   **Code Data:** Sourced from **The Stack** dataset (technical_report.pdf, page 4).
*   **Math Data:** Sourced from **Proof-Pile-2** and math-related web data filtered with a classifier (technical_report.pdf, page 4).
*   **Synthetic and Instruction Data:** Data from **Cosmopedia** and a small amount of multitask instruction data were introduced in the final decay stage of training (technical_report.pdf, page 4).

The proportions of these data sources were varied across four training stages, as detailed in Figure 1 of the technical report (technical_report.pdf, page 4).

### Motivation:
The datasets were "carefully selected" to create a high-quality and diverse training corpus (technical_report.pdf, page 1). A curriculum learning approach was adopted, where data complexity and the proportion of high-quality scientific data were increased in later stages. This was done to "increase high quality and scientific data at late stages" and "refine or shapen the knowledge learned during earlier stages" (technical_report.pdf, page 4).

### Preprocessing:
The preprocessing steps varied by data source:
*   **Web Data (RefinedWeb):** Underwent language identification, line-wise and document-wise filtering, and both fuzzy and exact deduplication (technical_report.pdf, page 3).
*   **Conversational Data:** Processed to "enforce causal temporality," ensuring that each conversation was used only once during training (technical_report.pdf, page 4).
*   **Code Data:** Passed through the same processing pipeline as the web data (technical_report.pdf, page 4).
*   **Tokenization:** The same tokenizer as the Falcon series of models was used. It includes 11 additional special tokens like `>>TITLE<<` and `>>ANSWER<<` (`special_tokens_map.json`, `tokenizer.json`; technical_report.pdf, page 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The technical report provides performance results disaggregated by benchmark and model architecture. Table 2 and Table 3 show the scores of Falcon Mamba 7B on individual tasks (e.g., MMLU, GSM8K, ARC-25) and compare them against other Transformer, RWKV, and hybrid models. The tables also present separate results for the final Falcon Mamba 7B model and its "pre-decay" checkpoint, allowing for analysis of the impact of the final training stage (technical_report.pdf, page 5).

### Intersectional results:
Insufficient information. The provided repository does not contain performance results across combinations of factors like demographics or environmental conditions.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
The model's inference requirements were evaluated on two types of GPUs:
*   **On a single 24 GB A10 GPU (batch size 1, float32):** The model can process a maximum sequence length of 16,000 tokens using parallel prefill. With sequential prefill, it can process "arbitrarily long prompts" (technical_report.pdf, pages 6-7, Figure 2).
*   **On a single 80 GB H100 GPU (batch size 1):** When generating up to 130,000 tokens from a short prompt, the model maintains a constant throughput of ~13.5 tokens/second and constant peak CUDA memory usage (technical_report.pdf, page 7, Figure 3).

### Training or Fine-tuning Requirements:
The model was pre-trained on a cluster of **256 H100 80GB GPUs** (technical_report.pdf, page 3).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The developers promote the responsible use of AI by releasing the model under a license that includes an **acceptable use policy** (technical_report.pdf, page 8). Users are expected to adhere to this policy.

The training data includes large web scrapes from Common Crawl and user-generated content from platforms like Reddit (technical_report.pdf, pages 3-4). These sources may contain sensitive, personal, or biased information. The report does not detail specific mitigation strategies for these data-related risks beyond filtering and deduplication. Potential risks associated with the model's application are not explicitly enumerated in the report; users are directed to the acceptable use policy for guidance on responsible deployment (technical_report.pdf, page 8).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **In-Context Learning Limitations:** The model may have "some limitations in in-context learning compared to Transformers." While this can be mitigated with high-quality data and specific prompting techniques, a performance gap may remain (technical_report.pdf, page 8).
*   **Training Instability:** During pre-training, the model exhibited "consistent loss spikes that occurred randomly and unpredictably," indicating that the Mamba architecture is more sensitive to learning rates than Transformers (technical_report.pdf, page 2).
*   **Untested Long-Context Proficiency:** Although the architecture is well-suited for long contexts, the training strategy used a "rather medium 8k context length." Therefore, the model's actual proficiency on extra-large contexts remains an "unexplored area for future research" (technical_report.pdf, page 8).
*   **Unexplored Scaling Laws:** The paper notes that data and model scaling for the Mamba architecture are less explored than for Transformers, leaving its limitations and optimization potential as an open research question (technical_report.pdf, page 8).

### Recommendations:
*   **Consult the Acceptable Use Policy:** All users should review and adhere to the model's acceptable use policy to ensure responsible application (technical_report.pdf, page 8).
*   **Use Left-Side Padding for Batching:** For batched inference with inputs of varying lengths, left-side padding should be used. The model is designed to handle this by zeroing out the hidden states for padding tokens to prevent them from influencing predictions (technical_report.pdf, page 8).
*   **Continual Training:** The developers have released a "pre-decay checkpoint" to "support the community in further research or continual training on the model" (technical_report.pdf, page 4).
*   **Prompting for In-Context Learning:** To mitigate limitations in in-context learning, users should consider using "Chain-of-Thought (CoT) instruction data or tailored prompting techniques" (technical_report.pdf, page 8).