## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by FAIR at Meta (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1, 102). The development involved a large team of researchers and engineers from the Seamless Communication project (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1).

### Model date:
The model and associated paper are dated November 30, 2023 (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1, 102).

### Model version:
This model is **SeamlessM4T v2** (specifically, the Large version) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1, 102).

It is an improved version of the original SeamlessM4T model. Key improvements include (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 3, 12):
*   **Architecture:** Upgraded from a multitask-UnitY to a multitask-UnitY2 architecture, which features a stronger non-autoregressive Text-to-Unit (T2U) model. This change improves S2ST inference speed by 3x.
*   **Pre-training:** The w2v-BERT 2.0 speech encoder was pre-trained on a significantly larger dataset of 4.5 million hours of unlabeled audio, compared to 1 million hours for the previous version.
*   **Data:** The model was finetuned with more supervision from an expanded version of the SeamlessAlign dataset, which now includes 114,800 hours of automatically aligned data for 76 languages, improving performance on low-resource languages.

The model was developed with `transformers_version: "4.36.0.dev0"` (config.json).

### Model type:
SeamlessM4T v2 is a massively multilingual and multimodal translation model designed for speech and text translation tasks (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1).

**Architecture:**
The model is a `SeamlessM4Tv2Model` with an encoder-decoder architecture (`is_encoder_decoder: true`) (config.json). It is described as a **Multitask-UnitY2** model composed of three main components (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102):
1.  A **Conformer speech encoder** based on w2v-BERT 2.0.
2.  A **Transformer text encoder-decoder** for text-to-text tasks.
3.  A **Transformer encoder with a non-autoregressive decoder** for Text-to-Unit (T2U) generation.

**Key Architectural Details** (config.json):
*   **Model Type:** `seamless_m4t_v2`
*   **Hidden Size:** 1024
*   **Encoder Layers:** 24 text encoder layers, 24 speech encoder layers
*   **Decoder Layers:** 24 text decoder layers, 6 T2U encoder layers, 6 T2U decoder layers
*   **Attention Heads:** 16 for all major components (encoder, decoder, speech encoder, T2U).
*   **Activation Function:** `relu` for the main transformer blocks and `swish` for the speech encoder.

**Size and Context Length:**
*   **Size:** The model has 2.3 billion parameters (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 13, Table 60). The total size on disk is approximately 9.24 GB (model.safetensors.index.json).
*   **Context Length:** The model supports a maximum position embedding of 4096 tokens (config.json).

### Training details:
The model was developed using a multi-stage training process (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 12-17):

1.  **Component Pre-training:**
    *   **Speech Encoder:** A Conformer-based w2v-BERT 2.0 model was pre-trained on 4.5 million hours of unlabeled audio data using a self-supervised learning approach (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 12, 16).
    *   **Text-to-Text Model:** A Transformer model was pre-trained on the NLLB dataset for text-to-text translation (T2TT) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 12).

2.  **Multitask Finetuning (X2T):** The pre-trained components were fused into an end-to-end model and finetuned to support speech-to-text (S2TT), automatic speech recognition (ASR), and text-to-text (T2TT) tasks. This stage used knowledge distillation from the strong T2TT model to the S2TT task (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 12, 16). The finetuning was performed in two stages: first on English-centric data, then on multilingual data, for a total of 200K updates (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 17).

3.  **Speech-to-Speech Finetuning (S2ST):** The model was further finetuned on speech-to-unit (S2U) data using the UnitY2 architecture. This architecture uses a non-autoregressive (NAR) decoder to predict discrete acoustic units from text, which are then converted to audio by a vocoder. This stage used a combination of pseudo-labeled and automatically aligned S2ST data totaling 145K hours (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 16, 20).

### Paper or other resource for more information:
The primary resource for the model is the academic paper that introduces it:
*   **Paper:** Seamless Communication, et al. (2023). *Seamless: Multilingual Expressive and Streaming Speech Translation*. This paper provides a comprehensive overview of the Seamless model family, including SeamlessM4T v2, its architecture, training data, and evaluation results (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf).
*   **Code Repository:** The official code, models, and related tools are publicly released at: `https://github.com/facebookresearch/seamless_communication` (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1).

### Citation details:
To cite the model, please use the following reference to the main paper (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1):
```bibtex
@article{seamless2023,
  title={Seamless: Multilingual Expressive and Streaming Speech Translation},
  author={Seamless Communication et al.},
  journal={ArXiv},
  year={2023},
  eprint={2311.00000},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```

### License:
The model is released under the **CC-BY-NC 4.0 license** (Creative Commons Attribution-NonCommercial 4.0 International) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102). This license allows for non-commercial use, sharing, and adaptation of the model, provided appropriate credit is given.

### Contact:
*   For questions or comments about the model, users can open an issue on the official GitHub repository: `https://github.com/facebookresearch/seamless_communication/issues` (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102).
*   The corresponding author for the research paper is Xutai Ma at `xutaima@meta.com` (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
SeamlessM4T-Large v2 is a multilingual and multimodal translation model intended primarily for research in speech and text translation. It supports a wide range of tasks (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102):

*   **Automatic Speech Recognition (ASR):** Transcribing speech into text for 96 languages.
*   **Speech-to-Text Translation (S2TT):** Translating speech from 100 source languages into text in 96 target languages.
*   **Speech-to-Speech Translation (S2ST):** Translating speech from 100 source languages into speech in 36 target languages.
*   **Text-to-Text Translation (T2TT):** Translating text from 96 source languages into text in 96 target languages.
*   **Text-to-Speech Translation (T2ST):** Translating text from 96 source languages into speech in 36 target languages.

The model is designed to be a foundational component for building systems that enable more naturalistic cross-lingual communication, with potential applications in real-time calling, AR/VR environments, online streaming, and assistive wearable devices (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 84).

### Primary intended users:
The primary intended users are researchers and developers in the machine translation, speech processing, and broader AI research communities (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102).

### Out-of-scope uses:
The model is released for research purposes and is not intended for production deployment. Specific out-of-scope uses include (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102):
*   **Domain-specific applications:** The model is trained on general domain data and is not intended for use with specialized inputs, such as in the medical or legal domains.
*   **Long-form translation:** The model was trained on short speech and text segments. Translating longer sequences may result in quality degradation.
*   **Certified translations:** Outputs from this model cannot be used as certified translations.

---

## How to Use
This section outlines how to use the model.

Information on how to use the model, including scripts for evaluation and fine-tuning, can be found in the official GitHub repository at `https://github.com/facebookresearch/seamless_communication` (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102).

The model accepts either speech (as an audio waveform) or text as input and can generate either speech or text as output, depending on the specified task (e.g., S2TT, S2ST). Users need to specify the source language and target language for translation tasks. The model supports a wide range of languages, which are specified using special language tokens (e.g., `__eng__`, `__fra__`) (tokenizer_config.json, special_tokens_map.json).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors identified and analyzed in the research paper:
*   **Language Resource Level:** Performance varies significantly depending on whether a language is high-resource, medium-resource, low-resource, or zero-shot in the training data (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 51).
*   **Language Family:** The linguistic distance between source and target languages affects performance. For example, translation quality is generally better between closely related languages (e.g., within the Italic or Germanic families) compared to distant pairs (e.g., English to Sinitic languages) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 51).
*   **Demographics and Speaker Traits:** The model's performance can be affected by speaker characteristics such as gender, pitch, and accent (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 68).
*   **Acoustic Conditions:** Background noise and variations in vocal style can impact the robustness of speech-input tasks (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 58).

### Evaluation factors:
The model was evaluated across the following factors:
*   **Language Resource Level:** Performance was disaggregated for high, medium, and low-resource languages to assess the impact of data availability (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 23, Table 9).
*   **Language Family:** The quality and latency of streaming translation were analyzed across different language families to understand the effect of linguistic divergence (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 51).
*   **Gender:** Gender bias was systematically evaluated by comparing model outputs for masculine and feminine grammatical forms (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 78).
*   **Acoustic Conditions:** Robustness was tested by evaluating the model on speech with simulated background noise (from the MUSAN dataset) and on speech with diverse vocal styles (from the FLEURS dataset) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 58).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A comprehensive set of automatic and human evaluation metrics were used to assess the model's performance across different tasks and dimensions (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 109, Table 59):

**Quality & Semantics:**
*   **ASR:** Word Error Rate (WER) on normalized transcriptions.
*   **S2TT:** SacreBLEU (with language-specific tokenizers) and BLASER 2.0.
*   **T2TT:** chrF2++.
*   **S2ST & T2ST:** ASR-BLEU, which measures the BLEU score between the ASR transcription of the generated speech and the reference text.

**Robustness:**
*   **chrFMS / CoefVarMS:** Metrics to evaluate robustness against vocal style variations.

**Toxicity:**
*   **ETOX / ASR-ETOX:** A text-based metric to measure added toxicity.
*   **MuTox / ASR-MuTox:** A multimodal metric to measure added toxicity in speech and text.

**Bias:**
*   **ASR-chrF & BLASER 2.0:** Used to evaluate gender bias.

**Human Evaluation:**
*   **XSTS (Cross-lingual Semantic Textual Similarity):** To measure semantic accuracy.
*   **MOS (Mean Opinion Score):** To evaluate speech quality on naturalness, sound quality, and clarity.

### Decision thresholds:
Insufficient information.

### Variation approaches:
*   **Robustness Evaluation:** Performance was measured across various signal-to-noise ratio (SNR) levels to assess robustness against background noise (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 58).
*   **Human Evaluation Statistics:** For human evaluation results, bootstrap re-sampling (with n=500) was used to estimate mean values and standard errors, ensuring robust statistical analysis (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 61).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a wide range of public benchmark datasets to assess its performance across multiple tasks and languages (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102):
*   **FLEURS:** An n-way parallel speech and text dataset covering 102 languages, used for evaluating ASR, S2TT, and S2ST tasks.
*   **FLORES-200:** A text dataset used for evaluating T2TT.
*   **CoVoST 2:** A multilingual speech-to-text translation dataset used for S2TT evaluation.
*   **CVSS:** A massively multilingual speech-to-speech translation corpus used for S2ST evaluation.
*   **HolisticBias & Multilingual HolisticBias:** Datasets designed to evaluate gender bias in text and speech translation.

### Motivation:
These datasets were chosen for their comprehensive language coverage, diversity of tasks, and suitability for evaluating specific aspects of the model. For instance, FLEURS was used for its broad n-way parallel data, which allows for extensive evaluation of multiple translation tasks and directions (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102). The HolisticBias datasets were specifically chosen to enable a systematic evaluation of gender bias (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 78).

### Preprocessing:
For evaluation, specific preprocessing steps were applied to the data to ensure fair and consistent measurement (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 21):
*   **Text Normalization:** For ASR evaluation (WER), both reference and hypothesis texts were normalized using the standard Whisper normalization procedure.
*   **Tokenization:** For BLEU score calculation in S2TT, the `13a` tokenizer was used for most languages, while a character-level tokenizer was used for Mandarin Chinese, Japanese, Thai, Lao, and Burmese.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a combination of unlabeled, pseudo-labeled, and automatically aligned data from various sources (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 12-14):
*   **Unlabeled Speech Data:** 4.5 million hours of diverse raw audio from publicly available repositories were used to pre-train the w2v-BERT 2.0 speech encoder (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 13, Figure 2).
*   **Parallel Text Data:** The NLLB dataset, containing 5 billion bitexts across 98 language pairs, was used to pre-train the text-to-text translation component (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 13, Figure 2).
*   **Aligned Speech-Text/Speech-Speech Data:**
    *   **SeamlessAlign:** An automatically aligned dataset created by mining parallel sentences from 3.9 million hours of raw web audio. The v2 version of this dataset covers 76 languages and contains 114,800 hours of data (45,300 hours for S2T eng-X, 60,200 hours for S2T X-eng, and 9,300 hours for S2S) (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 14).
    *   **Pseudo-labeled Data:** Existing ASR data was translated using the NLLB model to create pseudo-labeled S2TT data. This data was then used to generate pseudo-labeled S2ST data with a text-to-unit model (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 15).
*   **Total Supervised Data:** After filtering, the final training data amounted to 351,000 hours for S2TT tasks and 145,000 hours for S2ST tasks (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 15-16, Table 4).

### Motivation:
The data strategy was designed to overcome the scarcity of high-quality, human-labeled data for speech translation, especially for low-resource languages. Large-scale unlabeled data was used for powerful self-supervised pre-training, while automatic alignment and pseudo-labeling techniques were employed to create massive-scale supervised datasets for finetuning (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 13).

### Preprocessing:
The collected training data underwent an extensive filtering pipeline to ensure quality and safety (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 15):
*   **Toxicity Filtering:** Pairs with a toxicity imbalance between source and target were removed.
*   **Length Filtering:** Utterances shorter than 0.1 seconds or longer than 50 seconds were removed.
*   **Special Character Filtering:** Sentences with a high percentage of emojis, punctuation, or digits were filtered out.
*   **Repetition Filtering:** Sentences with excessive character or n-gram repetition were removed.
*   **Deduplication:** Duplicate target sentences were removed to prevent the model from overfitting.
*   **Language ID Filtering:** A language identification model was used to discard pairs where the target sentence was not in the expected language.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides performance results disaggregated by several individual factors:
*   **By Language Resource Level:** Table 9 shows the performance improvement of SeamlessM4T v2 over its predecessor, broken down by low, medium, and high resource levels. For example, for S2TT X-eng, the BLEU score improved by +2.8 for low-resource, +3.0 for medium-resource, and +1.7 for high-resource languages (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 23).
*   **By Language Family:** Figures 13 and 14 show the quality-latency trade-off for streaming translation, grouped by language families (e.g., Italic, Germanic, Sinitic). Performance is generally better for families closer to English (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 52).
*   **By Gender:** Table 56 presents gender bias results, showing the model's performance on masculine vs. feminine source sentences for both robustness (X-eng) and overgeneralization (eng-X) tasks (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 79).
*   **By Noise Condition:** Figure 16 shows the model's robustness to background noise, plotting BLEU/WER against different Signal-to-Noise Ratios (SNR) for "music" and "noise" categories (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 58).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** The model requires approximately 9.24 GB of disk space (model.safetensors.index.json).
*   **Memory:** To load the model with its default `float32` precision, approximately 9.2 GB of RAM or VRAM is required (config.json, Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 13).

### Deploying Requirements:
Inference time experiments for the S2ST task were conducted on a single A100 GPU with 96 CPUs, suggesting that a high-end GPU is recommended for deployment (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 110).

### Training or Fine-tuning Requirements:
Insufficient information.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The development of SeamlessM4T v2 included a comprehensive approach to responsible AI, with a focus on safety, fairness, and transparency (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 66-85).

*   **Sensitive Data:** The model was trained on large-scale web data, and while filtering was applied, the presence of sensitive data such as personal information or protected attributes cannot be entirely ruled out. The project included evaluations for gender bias and PII hallucination (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 68, 78).

*   **Risks and Mitigation Strategies:**
    *   **Toxicity:** The model may generate toxic content, either by hallucinating it (added toxicity) or failing to translate existing toxicity (deleted toxicity). A red-teaming effort found that toxicity was the most prevalent critical error category (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 69).
        *   **Mitigation:** Training data was filtered for toxicity imbalance. For inference, a mitigation technique named **MinTox** is used, which can re-run translation with constraints if toxicity is detected in the output but not the input. This reduces added toxicity by up to 80% in S2TT (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 73-74).
    *   **Gender Bias:** The model can exhibit gender bias, such as overgeneralizing to masculine forms when translating from a neutral language (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 78).
        *   **Mitigation:** This bias was quantified using the HolisticBias dataset. While v2 shows improved robustness to gender inflections, overgeneralization remains a challenge that requires specific mitigation techniques (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 79).
    *   **Misinformation and Harmful Content:** Mistranslations in high-stakes domains (e.g., health, legal) or of instructions could lead to physical or material harm.
        *   **Mitigation:** A dedicated red-teaming effort was conducted to identify and quantify these types of critical errors (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 67).
    *   **Deepfakes and Voice Phishing:** The model's speech generation capabilities could be misused for malicious purposes.
        *   **Mitigation:** The system includes an inaudible, localized **watermarking** mechanism (SeamlessWM) that allows for the detection and tracing of AI-generated audio at the frame level. The detector is also publicly released (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 79).

*   **Affected Groups:** The paper acknowledges that performance gaps may persist for low-resource languages and for users from diverse demographic backgrounds (race, accent, gender). It also notes that while the technology can improve information access, it could also make digitally less literate communities more vulnerable to online scams or misinformation (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 84, 102).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Long-Form Content:** The model was trained on short utterances (up to 50 seconds). Its performance on long-form audio or text translation may be degraded (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 15, 102).
*   **Domain Generalization:** The model is trained on general-domain data. Its performance on specialized domains (e.g., medical, legal) has not been investigated and is likely to be suboptimal (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102).
*   **Bias and Fairness:** Despite evaluations, the model may still produce biased (e.g., gendered) or false outputs. Performance can vary for users with different accents, races, or genders (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 84, 102).
*   **Toxicity:** The added toxicity mitigation (MinTox) reduces but does not eliminate the risk of the model generating toxic content (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 74).

### Recommendations:
*   **Use Case:** The model is intended for research applications. It should not be used in production or for high-stakes applications where errors could have adverse impacts on health, safety, or legal standing (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 102).
*   **Toxicity Mitigation:** Researchers using the model should consider implementing additional integrity mitigations for "added toxicity," especially in user-facing applications (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 103).
*   **Future Research:** The paper recommends that future work should focus on improving coverage for low-resource languages, closing performance gaps for diverse user groups, and expanding to other modalities like sign language to create more inclusive and robust systems (Seamless - Multilingual Expressive and Streaming Speech Translation.pdf, p. 85).

---