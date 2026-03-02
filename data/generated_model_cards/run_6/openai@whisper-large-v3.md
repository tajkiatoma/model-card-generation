## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers at OpenAI: Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever (2212.04356.pdf, p. 1).

### Model date:
The associated research paper was submitted on December 6, 2022 (2212.04356.pdf, p. 1). The paper mentions training an improved "V2" model after the original release (2212.04356.pdf, p. 4). This repository is for the "v3" version of the model (config.json.txt).

### Model version:
This is the `large-v3` version of the Whisper model (config.json.txt). The associated paper describes the initial Whisper models and a "Large model (denoted V2)" which was trained for 2.5 times more epochs with additional regularization techniques like SpecAugment, Stochastic Depth, and BPE Dropout (2212.04356.pdf, p. 4). This v3 model is an advancement on the previous versions.

### Model type:
The model is a Transformer-based encoder-decoder model for automatic speech recognition (ASR) (2212.04356.pdf, p. 3). It is named "Whisper" (config.json.txt).

**Architecture Details:**
*   **Encoder:** The encoder processes an 80-channel log-Mel spectrogram input. It uses a stem of two 1D convolutional layers (with GELU activation) followed by sinusoidal position embeddings and Transformer blocks. The Transformer blocks are pre-activation residual blocks (2212.04356.pdf, p. 3).
*   **Decoder:** The decoder is a standard Transformer that uses learned position embeddings and tied input-output token representations (2212.04356.pdf, p. 3).
*   **Tokenizer:** The model uses a byte-level Byte-Pair Encoding (BPE) text tokenizer (2212.04356.pdf, p. 3; tokenizer_summary.json.txt).

**Model Size and Parameters:**
*   **Model Name:** `large-v3`
*   **Layers:** 32 encoder layers and 32 decoder layers (config.json.txt).
*   **Model Dimensions (d_model):** 1280 (config.json.txt).
*   **Heads:** 20 attention heads for both encoder and decoder (config.json.txt).
*   **Feed Forward Dimension:** 5120 for both encoder and decoder (config.json.txt).
*   **Parameters:** The "Large" model family has 1550M (1.55 billion) parameters (2212.04356.pdf, Table 1, p. 5).
*   **Vocabulary Size:** 51,866 (config.json.txt).
*   **Context Length:** The decoder supports a maximum of 448 target positions (config.json.txt). The encoder processes audio in 30-second chunks (2212.04356.pdf, p. 2).

### Training details:
The model was trained on a large-scale, weakly supervised dataset to perform multiple tasks jointly (2212.04356.pdf, p. 1, 4).

*   **Algorithm:** The model is trained using a sequence-to-sequence approach on a multitask format. Special tokens are used in the decoder to specify tasks such as language identification, transcription, and translation (2212.04356.pdf, p. 3, Figure 1).
*   **Training Setup:** The models were trained with data parallelism using FP16 precision and dynamic loss scaling (2212.04356.pdf, p. 4).
*   **Optimizer:** AdamW optimizer was used (2212.04356.pdf, p. 4).
*   **Hyperparameters:**
    *   **Batch Size:** 256 segments (2212.04356.pdf, p. 4).
    *   **Learning Rate:** A linear learning rate decay schedule was used after a warmup over the first 2048 updates (2212.04356.pdf, p. 4).
    *   **Regularization:** The initial models did not use data augmentation or regularization, relying on the dataset's diversity. The v2 model added SpecAugment, Stochastic Depth, and BPE Dropout (2212.04356.pdf, p. 4).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). "Robust Speech Recognition via Large-Scale Weak Supervision." arXiv preprint arXiv:2212.04356. This paper details the model architecture, training data, methodology, and evaluation results (2212.04356.pdf).

The paper also provides a link to the official repository for inference code and models:
*   https://github.com/openai/whisper (2212.04356.pdf, p. 2).

### Citation details:
The following BibTeX entry can be used for citation:
```bibtex
@article{radford2022robust,
  title={Robust Speech Recognition via Large-Scale Weak Supervision},
  author={Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2212.04356},
  year={2022}
}
```
(2212.04356.pdf)

### License:
Insufficient information

### Contact:
For correspondence, the paper lists the following contacts at OpenAI:
*   Alec Radford: `alec@openai.com` (2212.04356.pdf, p. 1)
*   Jong Wook Kim: `jongwook@openai.com` (2212.04356.pdf, p. 1)

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed as a single, robust system for various speech processing tasks, intended to work reliably "out of the box" without task-specific fine-tuning (2212.04356.pdf, p. 1). Its primary uses are:
*   **Multilingual Speech Recognition:** Transcribing speech from 97 different languages into their original language (2212.04356.pdf, p. 2, 3).
*   **Speech Translation:** Translating speech from various languages into English (2212.04356.pdf, p. 2, 3).
*   **Spoken Language Identification:** Identifying the language being spoken in an audio clip (2212.04356.pdf, p. 3).
*   **Voice Activity Detection (VAD):** Detecting the presence or absence of speech in an audio segment (2212.04356.pdf, p. 3).

The model is designed to handle a wide distribution of audio from different environments, recording setups, and speakers (2212.04356.pdf, p. 2).

### Primary intended users:
The primary intended users are researchers and developers in the field of speech processing. The release of models and inference code is intended to "serve as a foundation for further work on robust speech processing" (2212.04356.pdf, p. 1).

### Out-of-scope uses:
The model is not designed for tasks outside of speech-to-text processing. The paper notes that the model can sometimes produce plausible but incorrect guesses for speaker names, and it was fine-tuned to remove this behavior, indicating that speaker identification is not a reliable use case (2212.04356.pdf, p. 5). The model is trained on 30-second audio chunks and requires specific strategies for long-form transcription, so direct transcription of audio longer than 30 seconds without these strategies is out-of-scope (2212.04356.pdf, p. 9).

---

## How to Use
This section outlines how to use the model.

The model uses a multitask format where the desired task is specified by providing a sequence of special tokens to the decoder as a prompt (2212.04356.pdf, p. 3).

**Input-Output Structure:**
*   **Input:** The model takes a 30-second audio clip, which is converted into an 80-channel log-Mel spectrogram (2212.04356.pdf, p. 3).
*   **Output:** The model generates a sequence of text tokens, including the transcribed/translated text and potentially timestamps.

**Task Specification:**
A task is specified by formatting the initial tokens fed to the decoder. The general format is as follows (2212.04356.pdf, Figure 1, p. 4):
1.  **Start Token:** The sequence begins with the `<|startoftranscript|>` token.
2.  **Language Token:** The next token specifies the language of the audio (e.g., `<|en|>`, `<|fr|>`). This is used for both transcription and as the source language for translation.
3.  **Task Token:** The task is specified with either `<|transcribe|>` for speech-to-text in the specified language or `<|translate|>` to translate the audio into English.
4.  **Timestamp Control:** The model can be instructed to predict timestamps by including timestamp tokens in the prompt. If timestamps are not desired, the `<|notimestamps|>` token is included.

**Example Prompt for English Transcription:**
`<|startoftranscript|><|en|><|transcribe|><|notimestamps|>` (2212.04356.pdf, p. 3; generation_config.json.txt).

**Example Prompt for Translation to English:**
`<|startoftranscript|><|es|><|translate|><|notimestamps|>` (This would translate Spanish audio to English text) (2212.04356.pdf, p. 3).

For long-form transcription (audio > 30 seconds), a specific decoding strategy is required, which involves transcribing in 30-second windows and using predicted timestamps to shift the window forward (2212.04356.pdf, p. 9, Section 4.5).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors due to the diverse nature of its training data. These include:
*   **Audio Quality:** The model is trained on a wide distribution of audio from various environments and recording setups, making it robust to noise (2212.04356.pdf, p. 2, 9).
*   **Language:** Performance varies significantly across the 97 languages it was trained on. The amount of training data for a given language is a strong predictor of its performance (2212.04356.pdf, p. 7).
*   **Task:** The model performs multiple tasks (transcription, translation), and its effectiveness can differ between them (2212.04356.pdf, p. 11).
*   **Domain:** The model is evaluated across various domains, including read speech (LibriSpeech), podcasts (Rev16), public talks (TED-LIUM), and earnings calls (Earnings-21), showing that performance can vary by domain (2212.04356.pdf, p. 9).

### Evaluation factors:
The model evaluation in the paper analyzes performance across these relevant factors:
*   **Datasets:** Performance is reported on a wide range of standard benchmarks, each representing a different domain or recording condition (e.g., LibriSpeech, Common Voice, WSJ, CORAAL) (2212.04356.pdf, p. 6, Table 2).
*   **Languages:** Multilingual performance is evaluated on datasets like Fleurs and MLS, with results broken down by language (2212.04356.pdf, p. 7, 23-25).
*   **Noise Levels:** Robustness is explicitly tested by adding white noise and pub noise at various signal-to-noise ratios (SNRs) (2212.04356.pdf, p. 9, Figure 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
The following metrics are used to assess the model's performance:
*   **Word Error Rate (WER):** The primary metric for speech recognition tasks. The paper uses an extensive text normalization process to minimize penalties for non-semantic differences (like punctuation or formatting) before calculating WER (2212.04356.pdf, p. 5, Appendix C).
*   **BLEU Score:** Used to evaluate the quality of speech translation (2212.04356.pdf, p. 8).
*   **Accuracy:** Used for language identification tasks (2212.04356.pdf, p. 8).

### Decision thresholds:
For long-form transcription, several heuristics and thresholds are used to improve reliability:
*   **No-speech Threshold:** A segment is considered silent if the probability of the `<|nospeech|>` token is above 0.6 **and** the average log-probability of the generated text is below -1 (2212.04356.pdf, p. 12).
*   **Temperature Fallback:** Decoding starts at a temperature of 0. The temperature is increased by 0.2 (up to 1.0) if the average log-probability is below -1 or if the gzip compression rate of the generated text is higher than 2.4, which helps mitigate repetition (2212.04356.pdf, p. 12).

### Variation approaches:
The paper mentions using 95% bootstrap estimate confidence intervals to analyze the scaling properties of the model (2212.04356.pdf, p. 12, Figure 9).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated in a zero-shot setting on a wide range of existing public datasets to measure its generalization capabilities. The datasets are detailed in Appendix A of the research paper (2212.04356.pdf, p. 19-20).

**Short-form English Datasets:**
*   LibriSpeech (test-clean and test-other)
*   TED-LIUM 3 (test split)
*   Common Voice 5.1 (English subset)
*   Artie bias corpus
*   CallHome and Switchboard
*   WSJ
*   CORAAL
*   CHiME-6
*   AMI (IHM and SDM1 splits)

**Long-form English Datasets:**
*   TED-LIUM 3 (full-length talks)
*   Meanwhile (segments from The Late Show with Stephen Colbert)
*   Rev16 (a subset of 16 podcast episodes)
*   Kincaid46 (46 audio files from a blog benchmark)
*   Earnings-21 and Earnings-22
*   CORAAL (full-length interviews)

**Multilingual Datasets:**
*   Multilingual LibriSpeech (MLS)
*   Fleurs
*   VoxPopuli
*   Common Voice 9
*   CoVoST 2 (for X→English translation)

### Motivation:
The datasets were chosen to cover a wide variety of domains, tasks, languages, and recording conditions. This allows for a comprehensive evaluation of the model's robustness and its ability to generalize to new distributions without any dataset-specific fine-tuning (2212.04356.pdf, p. 5).

### Preprocessing:
For evaluation, a comprehensive text standardization process is applied to both the model's output and the reference transcripts before calculating the Word Error Rate (WER). This is done to ensure that the metric reflects actual transcription errors rather than stylistic differences in formatting, punctuation, or spelling (e.g., converting British to American spellings, normalizing numeric expressions). The specific rules for English and non-English text are detailed in Appendix C of the paper (2212.04356.pdf, p. 21).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale dataset of 680,000 hours of weakly supervised audio and text data collected from the internet (2212.04356.pdf, p. 2).

*   **Size and Structure:** The dataset contains 680,000 hours of audio, which is broken into 30-second segments paired with corresponding transcript subsets (2212.04356.pdf, p. 2).
*   **Diversity:**
    *   **Multilingual:** 65% of the data is English speech recognition. 18% is X-to-English translation data (125,000 hours). The remaining 17% is non-English speech recognition covering 96 other languages (117,000 hours) (2212.04356.pdf, p. 2, 27).
    *   **Multitask:** The data is formatted to support multiple tasks, including transcription, translation, and voice activity detection (2212.04356.pdf, p. 3).

### Motivation:
The goal was to create a large and diverse supervised dataset to improve the robustness and zero-shot generalization of speech recognition models, closing the gap between the scale of unsupervised datasets and smaller, high-quality supervised ones (2212.04356.pdf, p. 1-2).

### Preprocessing:
A minimalist approach was taken to preprocessing, with the model trained to predict the raw text of transcripts. The following automated filtering and processing steps were applied (2212.04356.pdf, p. 2):
*   **Audio Resampling:** All audio is resampled to 16,000 Hz (2212.04356.pdf, p. 3).
*   **Feature Extraction:** An 80-channel log-magnitude Mel spectrogram is computed from 25ms windows with a 10ms stride (2212.04356.pdf, p. 3).
*   **Filtering Machine-Generated Transcripts:** Heuristics were used to detect and remove transcripts likely generated by other ASR systems to avoid learning "transcript-ese." For example, all-lowercase or all-uppercase transcripts were filtered out (2212.04356.pdf, p. 2).
*   **Language Filtering:** An audio language detector was used to ensure the spoken language matched the transcript language. Mismatched pairs where the transcript was English were used as X→English translation data (2212.04356.pdf, p. 2).
*   **De-duplication:** Fuzzy de-duping of transcripts was used to reduce duplication (2212.04356.pdf, p. 2).
*   **Segmentation:** Audio files were broken into 30-second segments and paired with the corresponding text (2212.04356.pdf, p. 2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The research paper provides detailed performance results broken down by individual factors:

*   **By Dataset (English):** The WER for the `large-v2` model on various English datasets includes: LibriSpeech test-clean (2.5%), LibriSpeech test-other (4.9%), TED-LIUM3 (3.7%), Common Voice 5.1 (8.2%), and WSJ (6.2%) (2212.04356.pdf, Table 9, p. 22).
*   **By Language:**
    *   On Multilingual LibriSpeech (MLS), the `large-v2` model achieves a WER of 9.3% (2212.04356.pdf, Table 10, p. 23).
    *   On Fleurs, performance varies widely by language, from a WER of 4.2% on English to 124.7% on Amharic for the `medium` model (2212.04356.pdf, p. 24).
*   **By Noise Level:** On LibriSpeech test-clean with additive pub noise, the `large` model's WER degrades from ~3% at 40 dB SNR to ~20% at 0 dB SNR and ~60% at -10 dB SNR (2212.04356.pdf, Figure 5, p. 8).
*   **By Task (Translation):** On the CoVoST2 dataset for X→English translation, the `large-v2` model achieves a BLEU score of 39.7 on high-resource languages, 31.8 on medium-resource, and 21.5 on low-resource languages (2212.04356.pdf, Table 15, p. 26).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
*   **Disk Space:** The model weights have a total size of approximately 6.17 GB (model.safetensors.index.fp32.json.txt).
*   **RAM/VRAM:** The model is intended to be run in `float16` precision (config.json.txt). Loading the model in `float16` would require approximately 3.1 GB of VRAM, while loading in `float32` would require approximately 6.2 GB.

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper mentions that models were trained using data parallelism with FP16 precision (2212.04356.pdf, p. 4), but does not specify the exact hardware configuration (e.g., number or type of GPUs) used for training.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Sourcing:** The model was trained on a large dataset of audio from the internet. The developers acknowledge that this data collection pipeline has biases, such as being "very English-heavy" (2212.04356.pdf, p. 14). This can lead to performance disparities, with the model performing poorly on many lower-resource languages (2212.04356.pdf, p. 7).
*   **Model Hallucinations:** The paper notes that a failure mode of sequence-to-sequence models like Whisper is "complete hallucination where the model will output a transcript entirely unrelated to the actual audio" (2212.04356.pdf, p. 14). This poses a risk of generating misinformation.
*   **Potential for Misuse:** As a powerful speech recognition tool, the model could be used for surveillance or other applications that infringe on privacy. The developers have released the model and code to "serve as a foundation for further work on robust speech processing," encouraging research and understanding of its capabilities and limitations (2212.04356.pdf, p. 1).
*   **Risk Mitigation:** To mitigate the risk of the model generating incorrect speaker names, it was briefly fine-tuned on a subset of transcripts that do not include speaker annotations (2212.04356.pdf, p. 5). For long-form transcription, specific decoding heuristics were developed to reduce errors like repetition loops (2212.04356.pdf, p. 12).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
The developers highlight several limitations in the paper (2212.04356.pdf, Section 6, p. 13-14):
*   **Long-Form Transcription Errors:** The model can still produce errors in long-form transcription, such as getting stuck in repetition loops, failing to transcribe the beginning or end of an audio segment, or hallucinating text unrelated to the audio.
*   **Performance on Low-Resource Languages:** The model's performance is "quite poor on many languages" due to the English-centric nature of the training data. Performance is strongly correlated with the amount of training data available for a language.
*   **Overfitting to Whisper's Transcription Style:** The text normalizer used for evaluation was developed alongside the model, which may result in it being overfitted to Whisper's specific output style. This could lead to an underestimation of the WER compared to other normalization methods (2212.04356.pdf, p. 5, 12).
*   **Lack of Speaker Diarization:** The model does not separate speakers in its output.

### Recommendations:
*   **Use Heuristics for Long-Form Transcription:** For transcribing audio longer than 30 seconds, it is crucial to use the recommended decoding strategies, including beam search, temperature fallback for repetitive content, and voice activity detection thresholds, to ensure reliable output (2212.04356.pdf, p. 12, Section 4.5).
*   **Further Research and Fine-Tuning:** The paper suggests that performance could be improved by:
    *   Fine-tuning the model on high-quality supervised datasets for specific domains (2212.04356.pdf, p. 14).
    *   Using reinforcement learning to more directly optimize decoding performance (2212.04356.pdf, p. 14).
    *   Targeted data collection efforts to increase the amount of training data for lower-resource languages (2212.04356.pdf, p. 14).

---