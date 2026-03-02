## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by FAIR at Meta (2312.05187.pdf, p. 1, Appendix B, p. 102). The development involved a large team of researchers and engineers from Seamless Communication, with collaborators from INRIA and UC Berkeley (2312.05187.pdf, p. 1).

### Model date:
The model was described in a paper dated November 30, 2023 (2312.05187.pdf, p. 1).

### Model version:
This is SeamlessM4T v2 (Large version) (2312.05187.pdf, p. 1, Appendix B, p. 102). It is an improved version of the original SeamlessM4T model. Key improvements include:
*   An updated **UnitY2 framework** with a non-autoregressive text-to-unit (T2U) decoder, which improves S2ST inference speed by 3x compared to the v1 model (2312.05187.pdf, p. 1, 12).
*   A new **w2v-BERT 2.0 speech encoder** pre-trained on 4.5 million hours of unlabeled audio, a 4.5x increase in data from the previous version (2312.05187.pdf, p. 3, 12).
*   Finetuning with more supervision from automatically aligned data to boost performance on low-resource languages (2312.05187.pdf, p. 3).

### Model type:
SeamlessM4T v2 is a massively multilingual and multimodal translation model with an encoder-decoder architecture (config.json.txt; 2312.05187.pdf, p. 1). It is designed for speech and text translation tasks.

*   **Architecture:** The model is a `SeamlessM4Tv2Model` (config.json.txt). It is a multitask model that integrates several pre-trained components (2312.05187.pdf, p. 12):
    1.  A **Conformer speech encoder** (w2v-BERT 2.0) for processing audio input.
    2.  A **Transformer text encoder-decoder** (from NLLB) for text-to-text tasks.
    3.  A **non-autoregressive text-to-unit (T2U) decoder** (UnitY2) for generating discrete acoustic units from text.
*   **Category:** The model performs multiple tasks including Automatic Speech Recognition (ASR), Speech-to-Text Translation (S2TT), Speech-to-Speech Translation (S2ST), Text-to-Text Translation (T2TT), and Text-to-Speech Translation (T2ST) (2312.05187.pdf, p. 12, Table 2).
*   **Size and Parameters:**
    *   **Parameters:** The model has 2.3 billion parameters (2312.05187.pdf, p. 13, Table 60, p. 110).
    *   **Size:** The total size of the model weights is 9,236,998,676 bytes (~9.24 GB) (model.safetensors.index.json.txt).
    *   **Configuration:** It has a hidden size of 1024, with 24 encoder layers and 24 decoder layers, and 16 attention heads in each (config.json.txt).
*   **Context Length:** The model supports a maximum position embedding of 4096 tokens (config.json.txt).

### Training details:
The model was developed by pre-training individual components and then finetuning them jointly in a multitask setup (2312.05187.pdf, p. 12).

*   **Pre-training:**
    *   The **w2v-BERT 2.0 speech encoder** was pre-trained on 4.5 million hours of unlabeled audio from public data repositories (2312.05187.pdf, p. 12, 13).
    *   The **text-to-text (T2TT) model** was pre-trained on NLLB data (2312.05187.pdf, p. 12).
    *   The **text-to-unit (T2U) model** was pre-trained on 34.5K hours of ASR data (2312.05187.pdf, p. 13, Figure 2).
*   **Finetuning:** The model was finetuned in multiple stages. The X2T (speech/text to text) model was trained to support T2TT, ASR, and S2TT by combining the pre-trained speech and text encoders. This stage used knowledge distillation from the strong T2TT model (2312.05187.pdf, p. 12, 16). The final loss function is a weighted sum of six individual losses: `LS2TT`, `LT2TT`, `LKD`, `LASR`, `LAE`, and `LKD-ASR` (2312.05187.pdf, p. 17, Eq. 8). The multitask-UnitY2 model was then finetuned on 145K hours of pseudo-labeled and automatically aligned speech-to-unit data (2312.05187.pdf, p. 12, 13, 20).

### Paper or other resource for more information:
*   **Paper:** The model is detailed in the academic paper "Seamless: Multilingual Expressive and Streaming Speech Translation" (2312.05187.pdf). The paper provides a comprehensive overview of the model's architecture, training data, evaluation, and ethical considerations.
*   **Repository:** The code is publicly available at `https://github.com/facebookresearch/seamless_communication` (2312.05187.pdf, p. 1).

### Citation details:
A BibTeX citation for the associated paper can be formatted as follows, based on the provided paper (2312.05187.pdf):
```bibtex
@article{seamless2023,
  title={Seamless: Multilingual Expressive and Streaming Speech Translation},
  author={Seamless Communication et al.},
  journal={arXiv preprint arXiv:2312.05187},
  year={2023}
}
```

### License:
The model is licensed under the CC-BY-NC 4.0 license (2312.05187.pdf, Appendix B, p. 102).

### Contact:
*   For questions or comments about the model, users can open an issue in the official GitHub repository: `https://github.com/facebookresearch/seamless_communication/issues` (2312.05187.pdf, Appendix B, p. 102).
*   The corresponding author for the research paper is Xutai Ma at `xutaima@meta.com` (2312.05187.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
SeamlessM4T-Large v2 is a multilingual and multimodal translation model intended for research in speech and text translation. It supports the following tasks (2312.05187.pdf, Appendix B, p. 102; Table 2, p. 12):
*   **S2ST (Speech-to-Speech Translation):** Translates speech from 101 source languages into 36 target languages.
*   **S2TT (Speech-to-Text Translation):** Transcribes and translates speech from 101 source languages into 96 target languages.
*   **T2ST (Text-to-Speech Translation):** Synthesizes speech in 36 target languages from text in 96 source languages (evaluated zero-shot).
*   **T2TT (Text-to-Text Translation):** Translates text from 96 source languages into 96 target languages.
*   **ASR (Automatic Speech Recognition):** Transcribes speech for 96 languages.
*   **TTS (Text-to-Speech):** Synthesizes speech for 36 languages.

The model accepts either speech or text as input and can generate either speech or text as output (2312.05187.pdf, p. 9).

### Primary intended users:
The primary users are researchers and the machine translation (speech and text) research community (2312.05187.pdf, Appendix B, p. 102).

### Out-of-scope uses:
The model has the following out-of-scope uses (2312.05187.pdf, Appendix B, p. 102):
*   **Production Deployment:** It is a research model and is not released for production deployment.
*   **Domain-Specific Applications:** The model is trained on general domain data and is not intended for use with domain-specific inputs, such as medical or legal text.
*   **Long-Form Translation:** The model was trained on short text and speech inputs, and translating longer sequences may result in quality degradation.
*   **Certified Translations:** Translations generated by SeamlessM4T-Large v2 cannot be used as certified translations.

---

## How to Use
This section outlines how to use the model. 

Insufficient information. The provided repository files do not include code snippets for model usage. Information on how to use the model, along with scripts for evaluation and finetuning, can be found in the official GitHub repository at `https://github.com/facebookresearch/seamless_communication` (2312.05187.pdf, Appendix B, p. 102).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors identified and evaluated in the research paper:
*   **Language Resource Level:** Performance varies depending on whether a language is high, medium, or low-resource, which is categorized based on the volume of available training data (2312.05187.pdf, p. 9, 23).
*   **Background Noise:** The presence and type of background noise (e.g., ambient noise, music) in the source audio can affect performance (2312.05187.pdf, p. 58).
*   **Vocal Style Variations:** Different vocal styles in the input speech can impact the model's robustness (2312.05187.pdf, p. 58).
*   **Gender:** The model's output can be affected by gendered language in the input, leading to potential biases (2312.05187.pdf, p. 77).
*   **Language Family:** The linguistic distance between source and target languages can affect translation quality and latency, particularly for streaming applications (2312.05187.pdf, p. 51).

### Evaluation factors:
The model was evaluated against the following factors:
*   **Language Resource Level:** Performance was analyzed for high, medium, and low-resource languages (2312.05187.pdf, Table 9, p. 23).
*   **Background Noise:** Robustness was tested against simulated "noise" and "music" categories from the MUSAN dataset at various signal-to-noise ratios (2312.05187.pdf, Figure 16, p. 58).
*   **Vocal Style Variations:** Robustness was evaluated using metrics like chrFMS and CoefVarMS on the Fleurs dataset (2312.05187.pdf, Table 40, p. 59).
*   **Gender Bias:** The model was evaluated for robustness to gender variations and overgeneralization using the Multilingual HolisticBias dataset (2312.05187.pdf, p. 78).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A combination of automatic and human evaluation metrics were used to assess the model's performance across its various tasks. A detailed list is available in the paper's "Metric Card" (2312.05187.pdf, Appendix H, p. 109).

**Automatic Metrics:**
*   **S2TT (Speech-to-Text Translation):** SacreBLEU (with specific tokenizers for certain languages) (2312.05187.pdf, p. 21).
*   **T2TT (Text-to-Text Translation):** chrF2++ (2312.05187.pdf, p. 21).
*   **ASR (Automatic Speech Recognition):** Word Error Rate (WER) on normalized transcriptions (2312.05187.pdf, p. 21).
*   **S2ST (Speech-to-Speech Translation) & T2ST (Text-to-Speech Translation):** ASR-BLEU, which measures the BLEU score between the ASR-transcribed model output and the reference text (2312.05187.pdf, p. 21).
*   **Robustness:** chrFMS (mean chrF by group) and CoefVarMS (coefficient of variation of chrF by group) for vocal style variations (2312.05187.pdf, p. 59).
*   **Toxicity:** ETOX and MuTox for detecting added toxicity (2312.05187.pdf, p. 70).
*   **Gender Bias:** chrF, ASR-chrF, and BLASER 2.0 (2312.05187.pdf, p. 78).

**Human Evaluation Metrics:**
*   **Semantic Meaning:** Cross-Lingual Semantic Textual Similarity (XSTS) (2312.05187.pdf, p. 4).
*   **Speech Quality:** Mean Opinion Score (MOS) for naturalness, sound quality, and speech clarity (2312.05187.pdf, p. 59).

### Decision thresholds:
Several thresholds were used during data processing and evaluation:
*   **Data Alignment:** A margin score threshold of 1.15 was used to filter automatically aligned data pairs (2312.05187.pdf, p. 14).
*   **Toxicity Filtering:** An imbalance threshold of 1 was used to remove training pairs where the difference in toxic items between source and target was greater than one (2312.05187.pdf, p. 15).
*   **Language Identification (LID) Filtering:** A confidence threshold of 0.9 was used for specific languages (Dutch, English, French, German, Italian, Polish, Portuguese, Russian, and Spanish) to discard pairs where the target language was incorrect (2312.05187.pdf, p. 15).

### Variation approaches:
For human evaluation results, bootstrap re-sampled mean and standard error estimates were reported to ensure statistical robustness, with a resampling rate of `nb = 500` times at the item level (2312.05187.pdf, p. 61).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a range of public benchmark datasets (2312.05187.pdf, Appendix B, p. 102):
*   **Fleurs:** An n-way parallel speech and text dataset covering 102 languages.
*   **Flores:** A text-to-text translation benchmark.
*   **CoVoST 2:** A multilingual speech-to-text translation dataset.
*   **CVSS:** A massively multilingual speech-to-speech translation corpus.
*   **HolisticBias and Multilingual HolisticBias:** Datasets designed for evaluating gender bias.
*   **mExpresso and mDRAL:** Expressive speech datasets used for evaluating the expressive capabilities of the broader Seamless model family (2312.05187.pdf, p. 38).

### Motivation:
Fleurs was chosen as a primary evaluation dataset because it provides n-way parallel speech and text data across 102 languages, enabling comprehensive evaluation of the model's multiple tasks and language capabilities (2312.05187.pdf, Appendix B, p. 102). The other datasets were chosen as they are standard benchmarks for specific tasks like speech translation (CoVoST 2, CVSS) and bias evaluation (HolisticBias).

### Preprocessing:
The evaluation data underwent specific preprocessing steps depending on the metric:
*   For **ASR evaluation (WER)**, transcriptions and references were normalized following the procedure used for the Whisper model (2312.05187.pdf, p. 21).
*   For **S2TT evaluation (SacreBLEU)**, the default `13a` tokenizer was used, except for Mandarin Chinese, Japanese, Thai, Lao, and Burmese, for which character-level tokenization was applied (2312.05187.pdf, p. 21).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a massive collection of data from various sources, including unlabeled, human-labeled, pseudo-labeled, and automatically aligned data (2312.05187.pdf, p. 12, Figure 2).
*   **Unlabeled Speech:** 4.5 million hours from publicly available data repositories, used for self-supervised pre-training of the w2v-BERT 2.0 speech encoder (2312.05187.pdf, p. 13).
*   **Parallel Text (T2TT):** 5 billion bitexts across 98 languages from sources like NLLB-SEED and PUBLICBITEXT, used for the text-to-text component (2312.05187.pdf, p. 13, Figure 2).
*   **ASR Data:** 34.5K hours of speech with transcriptions across 36 languages, used for pre-training the text-to-unit model (2312.05187.pdf, p. 13, Figure 2).
*   **Automatically Aligned Data (SeamlessAlign):** A new version of this dataset was created, adding 114,800 hours of automatically aligned speech-to-text and speech-to-speech data, expanding language coverage to 76 languages (2312.05187.pdf, p. 1, 14).
*   **Total Finetuning Data:** After filtering, the data used for finetuning amounted to 351K hours for S2TT tasks and 145K hours for S2ST tasks (2312.05187.pdf, p. 15, Table 4).

### Motivation:
The primary motivation for the data collection strategy was to overcome the scarcity of human-labeled speech translation data. This was achieved by leveraging large amounts of unlabeled audio and text data through self-supervision and pre-training, and then creating large-scale supervised datasets through automatic alignment and pseudo-labeling (2312.05187.pdf, p. 13).

### Preprocessing:
The combined training data was subjected to a series of filtering steps to improve quality (2312.05187.pdf, p. 15):
*   **Toxicity filtering:** Removed pairs with a significant difference in toxicity between source and target.
*   **Length filtering:** Removed utterances that were too short (<0.1s) or too long (>50s), or text longer than 250 sub-words.
*   **Special characters filtering:** Removed text with high percentages of emojis, punctuation, digits, or spaces.
*   **Repetition filtering:** Removed sentences with excessive contiguous character repetitions or low n-gram diversity.
*   **Deduplication:** Removed data points with identical target text to prevent redundancy.
*   **LID filtering:** A language identification model was used to discard pairs where the target text was not in the expected language.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results disaggregated by several factors:
*   **By Language Resource Level:** Table 9 shows that SeamlessM4T v2 improves over v1 most significantly for low-resource languages in S2TT (+2.8 BLEU), S2ST (+4.3 ASR-BLEU), and ASR (-7.5 WER) (2312.05187.pdf, p. 23).
*   **By Language Family:** For the streaming version of the model, performance is better for "Italic" and "Germanic" languages, which are closer to the English-centric training data, while more distant language families like "Sinitic" and "Japanesic" show a larger drop in quality and higher latency (2312.05187.pdf, p. 51, Figures 13 & 14).
*   **By Gender:** In robustness tests (X-eng), the model shows a 3.3% to 3.4% relative performance drop when translating masculine vs. feminine forms. In overgeneralization tests (eng-X), the gap is larger, at 11.1% for S2TT (chrF) and 10.5% for S2ST (ASR-chrF), indicating a tendency to overgeneralize towards the masculine gender (2312.05187.pdf, Table 56, p. 79).
*   **By Noise Condition:** The model's performance degrades as the signal-to-noise ratio (SNR) decreases. However, it consistently outperforms Whisper-Large-v2 and the previous SeamlessM4T-Large across all noise levels for both S2TT (BLEU) and ASR (WER) (2312.05187.pdf, Figure 16, p. 58).

### Intersectional results:
Insufficient information. The provided repository does not contain performance results across combinations of factors (e.g., accuracy for a specific gender within a particular noise condition).

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model has 2.3 billion parameters and a total size of approximately 9.24 GB (2312.05187.pdf, p. 13; model.safetensors.index.json.txt). Loading this model would require at least this amount of disk space and a comparable amount of RAM or VRAM, depending on the precision used (e.g., float32, float16).

### Deploying Requirements:
Inference time for S2ST tasks was evaluated on a single A100 GPU with 96 CPUs (2312.05187.pdf, p. 110). The non-autoregressive decoder in v2 makes inference speed significantly faster and less dependent on output length compared to v1, improving its suitability for deployment (2312.05187.pdf, p. 12, Figure 30, p. 110).

### Training or Fine-tuning Requirements:
Insufficient information. The paper mentions specific hardware used for training components of the broader Seamless family (e.g., 16 V100 GPUs for PRETSSEL) (2312.05187.pdf, p. 36), but does not specify the full hardware requirements for finetuning the core SeamlessM4T v2 model.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions. 

The developers took a comprehensive approach to responsible AI, detailed in Section 8 of the paper (2312.05187.pdf, p. 66).

*   **Sensitive Data:** The model was evaluated for gender bias and toxicity, and red-teaming included checks for hallucinated Personally Identifiable Information (PII), indicating that the training data may contain such sensitive attributes or content (2312.05187.pdf, p. 68, 77).
*   **Risks and Mitigation Strategies:**
    *   **Toxicity:** The model can produce or add toxicity to translations. This risk was mitigated through **toxicity filtering** of training data and implementing **MinTox**, an inference-time technique to prevent the model from adding toxic content (2312.05187.pdf, p. 15, 69).
    *   **Gender Bias:** The model exhibits a tendency to overgeneralize towards the masculine gender. This was quantified through extensive evaluation on the HolisticBias dataset. The paper notes that specific techniques are needed to counteract this (2312.05187.pdf, p. 78-79).
    *   **Misuse (Deepfakes, Voice Phishing):** The paper acknowledges the risk of the model being used for malicious purposes like voice phishing. To mitigate this, an **inaudible, localized watermarking mechanism (SeamlessWM)** was developed to trace the provenance of AI-generated audio. The detector for this watermark was also released (2312.05187.pdf, p. 79, 85).
    *   **Critical Errors:** A **red-teaming effort** was conducted to identify various critical errors, including safety concerns (e.g., deviation in legal/health information), opposite sentiment, and errors in instructions, numbers, or named entities (2312.05187.pdf, p. 67-68).
*   **Potentially Harmed Groups:**
    *   The paper notes that performance gaps in ASR for users with different accents or from different racial backgrounds could lead to poorer downstream translation quality for these groups (2312.05187.pdf, p. 84).
    *   While providing translation for low-resource languages can improve information access, it could also make communities with lower digital literacy more vulnerable to misinformation and online scams if the technology is misused (2312.05187.pdf, p. 84, 102).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Added Toxicity:** Even with mitigation, the risk of "added toxicity" remains. Researchers using the model should consider implementing additional integrity mitigations (2312.05187.pdf, Appendix B, p. 103).
*   **Long-Form Content:** The model was trained on short utterances and may exhibit degraded performance on long-form speech or text translation (2312.05187.pdf, Appendix B, p. 102).
*   **Performance Disparities:** Model performance can vary based on user demographics such as race or accent, potentially leading to performance gaps for certain user groups (2312.05187.pdf, p. 84).
*   **Domain Generalization:** The model was trained on general domain data and its performance on other domains (e.g., medical, legal) has not been thoroughly investigated (2312.05187.pdf, Appendix B, p. 102).
*   **False or Biased Outputs:** Despite efforts to optimize for quality, the model may still produce toxic, biased, or false outputs, which could have an adverse impact on users who rely on the translations for important decisions (2312.05187.pdf, Appendix B, p. 102).

### Recommendations:
*   **Research Use Only:** The model is intended for research applications and is not released for production deployment (2312.05187.pdf, Appendix B, p. 102).
*   **Awareness of Limitations:** Users should be aware of the model's limitations, particularly regarding potential biases, toxicity, and performance on out-of-domain or long-form content.
*   **Future Work:** The paper recommends that future research should focus on improving language coverage (especially for low-resource languages), closing performance gaps for diverse user groups, and exploring other modalities like sign language (2312.05187.pdf, p. 85).