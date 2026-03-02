## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, named Whisper, was developed by researchers at OpenAI (2212.04356.pdf, p. 1). The authors of the accompanying paper are Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever (2212.04356.pdf, p. 1).

### Model date:
The associated research paper was submitted to arXiv on December 6, 2022 (2212.04356.pdf, p. 1). The paper describes the initial model and an improved "Large V2" model (2212.04356.pdf, p. 4, footnote 3). The model in this repository is identified as `openai/whisper-large-v3` (config.json.txt).

### Model version:
This repository contains the `large-v3` version of the Whisper model (config.json.txt). The accompanying paper primarily details the original and "V2" versions. The V2 model was trained for 2.5 times more epochs than the original and included regularization techniques like SpecAugment, Stochastic Depth, and BPE Dropout (2212.04356.pdf, p. 4, footnote 3). Differences for v3 are not specified in the provided documents.

### Model type:
The Whisper model is an encoder-decoder Transformer designed for speech processing tasks (2212.04356.pdf, p. 3). It is a sequence-to-sequence model that processes audio input and generates text output (2212.04356.pdf, p. 4).

**Architecture Details:**
*   **Model Type:** `whisper` (config.json.txt).
*   **Structure:** It is an encoder-decoder architecture (`is_encoder_decoder: true`) for conditional generation (`architectures: ["WhisperForConditionalGeneration"]`) (config.json.txt).
*   **Input:** The model takes an 80-channel log-magnitude Mel spectrogram as input, computed from audio resampled to 16,000 Hz (2212.04356.pdf, p. 3). The feature extractor uses a 30-second chunk length (`chunk_length: 30`), a sampling rate of 16,000 Hz (`sampling_rate: 16000`), and 128 Mel bins (`num_mel_bins: 128`) (preprocessor_config.json.txt, config.json.txt).
*   **Encoder:** The encoder uses 32 transformer layers (`encoder_layers: 32`) with a model dimension of 1280 (`d_model: 1280`), 20 attention heads (`encoder_attention_heads: 20`), and a feed-forward network dimension of 5120 (`encoder_ffn_dim: 5120`) (config.json.txt). It is preceded by a stem of two convolutional layers (2212.04356.pdf, p. 3).
*   **Decoder:** The decoder also has 32 transformer layers (`decoder_layers: 32`) with a model dimension of 1280 (`d_model: 1280`), 20 attention heads (`decoder_attention_heads: 20`), and a feed-forward network dimension of 5120 (`decoder_ffn_dim: 5120`) (config.json.txt).
*   **Parameters:** The "Large" model has 1550 million (1.55B) parameters (2212.04356.pdf, p. 5, Table 1).
*   **Size:** The total size of the model weights on disk is 6,173,962,240 bytes (approximately 6.17 GB) (pytorch_model.bin.index.fp32.json.txt, model.safetensors.index.fp32.json.txt).
*   **Context Length:** The model processes audio in 30-second segments (2212.04356.pdf, p. 2). The maximum source position length is 1500, and the maximum target (text) position length is 448 tokens (config.json.txt).

### Training details:
The model was trained using a large-scale weak supervision approach on a massive dataset of audio and corresponding transcripts (2212.04356.pdf, p. 1).

*   **Algorithm:** The model is trained as an audio-conditional language model in a multitask format to predict sequences of text tokens (2212.04356.pdf, p. 3).
*   **Multitask Format:** A single model is trained to perform multiple tasks by conditioning the decoder with special tokens. These tasks include speech transcription (`<|transcribe|>`), translation to English (`<|translate|>`), language identification (e.g., `<|en|>`, `<|fr|>`), and voice activity detection (`<|nospeech|>`) (2212.04356.pdf, p. 3; generation_config.json.txt).
*   **Hyperparameters (Original/V1):**
    *   **Optimizer:** AdamW (2212.04356.pdf, p. 4, 28).
    *   **Batch Size:** 256 segments (2212.04356.pdf, p. 4, 28).
    *   **Learning Rate:** A linear decay schedule with a warmup over the first 2048 updates. The max learning rate for the "Large" model was 1.75 x 10⁻⁴ (2212.04356.pdf, p. 4, 28).
    *   **Precision:** FP16 with dynamic loss scaling (2212.04356.pdf, p. 4).
    *   **Epochs:** Trained for 2-3 passes over the dataset (2212.04356.pdf, p. 4).
*   **Hyperparameters (Large V2):**
    *   **Batch Size:** 1024 (2212.04356.pdf, p. 28, Table 18).
    *   **Regularization:** BPE Dropout (0.1), Stochastic Depth (0.1), and SpecAugment were added (2212.04356.pdf, p. 4, 28).
    *   **Learning Rate:** Max learning rate was 2.0 x 10⁻⁴ (2212.04356.pdf, p. 28, Table 19).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Radford, A., et al. (2022). "Robust Speech Recognition via Large-Scale Weak Supervision." arXiv:2212.04356. This paper details the model's architecture, training data, methodology, and extensive evaluation results (2212.04356.pdf).

The authors also released inference code at the following URL:
*   `https://github.com/openai/whisper` (2212.04356.pdf, p. 2).

### Citation details:
A BibTeX citation for the model can be formatted as follows, based on the provided paper:
```bibtex
@misc{radford2022robust,
      title={Robust Speech Recognition via Large-Scale Weak Supervision}, 
      author={Alec Radford and Jong Wook Kim and Tao Xu and Greg Brockman and Christine McLeavey and Ilya Sutskever},
      year={2022},
      eprint={2212.04356},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```
(2212.04356.pdf, p. 1)

### License:
Insufficient information.

### Contact:
Correspondence for the project can be directed to Alec Radford (`alec@openai.com`) or Jong Wook Kim (`jongwook@openai.com`) (2212.04356.pdf, p. 1, footnote).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is designed as a single, robust system for various speech processing tasks, intended to work reliably "out of the box" in a zero-shot setting without task-specific fine-tuning (2212.04356.pdf, p. 1, 5). Its primary capabilities include:

*   **Automatic Speech Recognition (ASR):** Transcribing speech from audio. The model is multilingual and can transcribe speech in 97 languages (2212.04356.pdf, p. 3, 7).
*   **Speech Translation:** Translating speech from any of the supported languages into English (2212.04356.pdf, p. 3).
*   **Language Identification:** Identifying the language being spoken in an audio clip from a set of 99 languages (2212.04356.pdf, p. 3; generation_config.json.txt).
*   **Voice Activity Detection (VAD):** Detecting whether there is speech in an audio segment (2212.04356.pdf, p. 3).

The model takes a 30-second audio segment as input and generates a sequence of text tokens as output. For long-form audio, a specific buffering strategy is required (2212.04356.pdf, p. 9).

### Primary intended users:
The model and its code were released to "serve as a foundation for further work on robust speech processing," indicating that the primary intended users are researchers and developers in the speech and machine learning communities (2212.04356.pdf, p. 1).

### Out-of-scope uses:
Insufficient information. The provided documents do not explicitly list out-of-scope uses.

---

## How to Use
This section outlines how to use the model.

The model performs tasks based on a sequence of special tokens provided to the decoder. The input audio is processed as a 30-second log-Mel spectrogram (2212.04356.pdf, p. 3).

A typical workflow is as follows:
1.  **Start Token:** The decoder sequence begins with a start-of-transcript token (`<|startoftranscript|>`, ID 50258) (2212.04356.pdf, p. 3; generation_config.json.txt).
2.  **Language Token:** The next token specifies the language of the audio. For example, `<|en|>` (ID 50259) for English or `<|fr|>` (ID 50265) for French. If the language is unknown, the model will predict it first (2212.04356.pdf, p. 3; generation_config.json.txt).
3.  **Task Token:** The next token specifies the task. This is either `<|transcribe|>` (ID 50360) for speech recognition in the specified language or `<|translate|>` (ID 50359) for translation into English (2212.04356.pdf, p. 3; generation_config.json.txt).
4.  **Timestamp Control:** The model can optionally predict timestamps. To disable timestamps, the `<|notimestamps|>` token (ID 50364) is provided (2212.04356.pdf, p. 3; generation_config.json.txt).
5.  **Generation:** After these control tokens, the model generates the text transcript, which concludes with an end-of-transcript token (`<|endoftext|>`, ID 50257) (2212.04356.pdf, p. 3).

**Long-Form Transcription:**
For audio longer than 30 seconds, a special strategy is required:
*   The audio is processed in consecutive 30-second windows.
*   The model's predicted timestamps are used to determine the shift for the next window.
*   A set of heuristics, including beam search, temperature scheduling, and conditioning on the previous transcript, is used to prevent repetition and improve reliability (2212.04356.pdf, p. 9, 12).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper identifies several factors that influence the model's performance:
*   **Amount of Training Data:** Performance on a given language is strongly correlated with the amount of training data available for that language (squared correlation of 0.83) (2212.04356.pdf, p. 7).
*   **Language and Script:** Languages with unique scripts or that are linguistically distant from the Indo-European majority of the training data tend to have worse performance than expected (e.g., Hebrew, Telugu, Chinese, Korean) (2212.04356.pdf, p. 7).
*   **Audio Quality and Noise:** Performance degrades with increased additive noise. The model's robustness varies depending on the type of noise (e.g., white noise vs. more natural pub noise) and the signal-to-noise ratio (SNR) (2212.04356.pdf, p. 8).
*   **Domain and Content:** The model's performance varies across different domains, such as read audiobooks (LibriSpeech), phone calls (CallHome), and jargon-heavy segments (Meanwhile, Earnings-21) (2212.04356.pdf, p. 6, 9).

### Evaluation factors:
The model was evaluated across a wide range of factors to measure its robustness and generalization:
*   **Multiple Datasets:** Performance was measured across 13 short-form English datasets and 7 long-form English datasets to assess generalization across different domains, accents, and recording conditions (2212.04356.pdf, p. 6, 9, 19).
*   **Multiple Languages:** The model was evaluated on multilingual datasets including Multilingual LibriSpeech (MLS), Fleurs, and VoxPopuli (2212.04356.pdf, p. 6, 20).
*   **Task:** Performance was measured for transcription, translation, and language identification (2212.04356.pdf, p. 6-8).
*   **Noise:** Robustness was evaluated by adding white noise and pub noise at various signal-to-noise ratios (SNRs) (2212.04356.pdf, p. 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Word Error Rate (WER):** The primary metric used for evaluating speech recognition performance. The authors note that standard WER penalizes innocuous formatting differences, so they developed an extensive text normalizer to apply to both reference and hypothesis texts before calculation (2212.04356.pdf, p. 5).
*   **BLEU Score:** Used to evaluate the performance of speech translation (2212.04356.pdf, p. 8).
*   **Accuracy:** Used to evaluate language identification performance (2212.04356.pdf, p. 8).

### Decision thresholds:
For long-form transcription, several heuristics with specific thresholds are used to improve reliability:
*   **Voice Activity Detection:** A segment is considered to have no speech if the probability of the `<|nospeech|>` token is greater than 0.6 AND the average log-probability of the generated tokens is less than -1 (2212.04356.pdf, p. 13).
*   **Temperature Fallback:** The decoding temperature is increased from 0.0 by 0.2 (up to 1.0) if the average log probability of tokens is lower than -1 OR the gzip compression rate of the generated text is higher than 2.4, which helps prevent repetitive loops (2212.04356.pdf, p. 12).
*   **Initial Timestamp Constraint:** The initial timestamp token is constrained to be between 0.0 and 1.0 seconds to prevent the model from ignoring the beginning of an audio segment (2212.04356.pdf, p. 13).

### Variation approaches:
When analyzing the scaling properties of the model, 95% bootstrap estimate confidence intervals were used to show the statistical significance of performance differences (2212.04356.pdf, p. 12, Figure 9 caption).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated in a zero-shot setting on a wide variety of publicly available datasets. A full list is provided in Appendix A of the paper (2212.04356.pdf, p. 19-20).

*   **Short-form English ASR:** LibriSpeech, TED-LIUM 3, Common Voice 5.1, Artie bias corpus, CallHome, Switchboard, WSJ, CORAAL, CHiME-6, AMI-IHM, and AMI-SDM1.
*   **Long-form English ASR:** Full-length talks from TED-LIUM 3, "Meanwhile" (segments from The Late Show), Rev16 (podcasts), Kincaid46 (various audio), Earnings-21/22 (earnings calls), and full interviews from CORAAL.
*   **Multilingual ASR:** Multilingual LibriSpeech (MLS), Fleurs, VoxPopuli, and Common Voice 9.
*   **Speech Translation (X→en):** CoVoST 2.

### Motivation:
The datasets were chosen to be diverse in their domains, tasks, and languages to rigorously test the model's zero-shot generalization and robustness (2212.04356.pdf, p. 5). The long-form datasets were specifically chosen to cover a wide distribution of lengths and recording conditions found in real-world applications (2212.04356.pdf, p. 9).

### Preprocessing:
Before calculating Word Error Rate (WER), a comprehensive text standardization procedure was applied to both the model's output and the ground truth transcripts to minimize penalties for non-semantic differences like punctuation or formatting (2212.04356.pdf, p. 5).

For English text, this process includes (2212.04356.pdf, p. 21):
1.  Removing content in brackets and parentheses.
2.  Removing filler words like "hmm" and "uh".
3.  Standardizing contractions (e.g., "you're" becomes "you are").
4.  Removing punctuation and symbols, except those relevant for numeric expressions.
5.  Standardizing numeric and currency expressions (e.g., "Ten thousand dollars" becomes "$10000").
6.  Converting British spellings to American spellings using a provided dictionary (normalizer.json.txt).

For non-English text, a simpler normalization is applied: lowercasing and removing all markers, symbols, and punctuation (2212.04356.pdf, p. 21).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale, weakly supervised dataset collected from the internet (2212.04356.pdf, p. 1).

*   **Size:** 680,000 hours of audio supervision (2212.04356.pdf, p. 1).
*   **Structure:** The data consists of audio-transcript pairs. The audio is segmented into 30-second chunks for training (2212.04356.pdf, p. 2).
*   **Diversity:**
    *   **Multilingual:** 65% of the data (438,218 hours) is English speech recognition. 17% (117,113 hours) is multilingual speech recognition covering 96 languages other than English. (2212.04356.pdf, p. 2, 27).
    *   **Multitask:** 18% of the data (125,739 hours) is for any-to-English speech translation (2212.04356.pdf, p. 2, 27).
*   **Source:** The data was collected from various sources on the internet (2212.04356.pdf, p. 2). The dataset is not publicly available.

### Motivation:
The motivation was to close the gap between the scale of unsupervised pre-training datasets (up to 1M hours) and existing supervised datasets (typically a few thousand hours). By creating a very large and diverse weakly supervised dataset, the goal was to improve the robustness and zero-shot generalization of speech recognition models (2212.04356.pdf, p. 1-2).

### Preprocessing:
A multi-stage filtering and processing pipeline was applied to the raw web data to improve its quality (2212.04356.pdf, p. 2-3):

1.  **Audio Processing:** All audio was resampled to 16,000 Hz and converted into an 80-channel log-Mel spectrogram (2212.04356.pdf, p. 3).
2.  **Transcript Filtering:**
    *   Heuristics were used to detect and remove transcripts that were likely machine-generated (e.g., all-lowercase or lacking punctuation) (2212.04356.pdf, p. 2).
    *   An audio language detector was used to ensure the spoken language matched the transcript language. Mismatched pairs where the transcript was English were used as speech translation data (2212.04356.pdf, p. 2).
    *   Fuzzy deduplication was applied to reduce redundant content (2212.04356.pdf, p. 2).
3.  **Model-Based Filtering:** An initial model was trained, and its error rate on different data sources was used to manually inspect and remove low-quality sources (2212.04356.pdf, p. 3).
4.  **Text Standardization:** Unlike the evaluation step, the training transcripts were used in their raw form without significant standardization, relying on the model to learn to handle diverse text formats (2212.04356.pdf, p. 2).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive results disaggregated by various factors.

*   **By Dataset (English ASR):** The Large V2 model achieves a WER of 2.7% on LibriSpeech Clean, 5.2% on LibriSpeech Other, 4.0% on TED-LIUM, 9.0% on Common Voice, and 25.5% on CHiME6 (2212.04356.pdf, p. 6, Table 2).
*   **By Language (Multilingual ASR):** Performance varies significantly by language, strongly correlating with the amount of training data. On the Fleurs dataset, WER ranges from low single digits for high-resource languages like Spanish (ES) and Italian (IT) to over 80% for very low-resource languages like Mongolian (MN) and Yoruba (YO) (2212.04356.pdf, p. 7, Figure 3).
*   **By Noise Level (English ASR):** On LibriSpeech test-clean with additive pub noise, the model's WER is ~5% at 20 dB SNR, ~10% at 10 dB SNR, and ~25% at 0 dB SNR (2212.04356.pdf, p. 8, Figure 5).
*   **By Resource Level (Speech Translation):** On the CoVoST2 dataset, the zero-shot model achieves a BLEU score of 36.2 on high-resource languages, 32.6 on medium-resource languages, and 25.2 on low-resource languages (2212.04356.pdf, p. 8, Table 4).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The model weights require approximately 6.17 GB of disk space. Loading the model into memory would require at least this much RAM or VRAM (pytorch_model.bin.index.fp32.json.txt, model.safetensors.index.fp32.json.txt).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The paper states that models were trained "with data parallelism across accelerators using FP16," which implies a multi-GPU setup is necessary for training from scratch (2212.04356.pdf, p. 4). Specific hardware details or memory requirements for training are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The provided documents do not contain a dedicated section on ethical considerations. The following points are inferred from the description of the model and its training data:

*   **Data Provenance and Privacy:** The model was trained on 680,000 hours of audio from the internet (2212.04356.pdf, p. 1). This data may contain personally identifiable information, sensitive content, or copyrighted material. The paper does not specify what steps, if any, were taken to anonymize data or respect privacy.
*   **Bias:** The training data is heavily skewed towards English (65% of the data) and Indo-European languages (2212.04356.pdf, p. 7, 27). As a result, the model's performance is significantly worse on low-resource languages, potentially widening the digital divide (2212.04356.pdf, p. 7, 14). The paper acknowledges this performance gap but does not analyze other potential demographic or social biases in detail.
*   **Potential for Misuse:** A powerful speech recognition tool could be used for mass surveillance or other applications that infringe on privacy. These risks are not discussed in the paper.
*   **Model Errors (Hallucinations):** The model can sometimes "hallucinate," producing a transcript that is entirely unrelated to the actual audio. This is a failure mode of the sequence-to-sequence architecture (2212.04356.pdf, p. 14). Such errors could have serious consequences if the model is used in critical applications.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Long-Form Transcription Reliability:** The model processes audio in 30-second chunks. Transcribing longer audio requires a specific set of heuristics which are not foolproof and can be unreliable. Failure modes include getting stuck in repetitive loops, hallucinating text, or failing to transcribe the beginning or end of a segment (2212.04356.pdf, p. 9, 14).
*   **Performance on Low-Resource Languages:** The model's performance is poor on many languages for which there was little training data. Performance is strongly predicted by the amount of training data for a given language (2212.04356.pdf, p. 7, 14).
*   **Text Normalizer Overfitting:** The custom text normalizer used for evaluation was developed alongside the model. While tests show it performs similarly to other normalizers on most datasets, it provides a significantly larger WER reduction for Whisper on a few specific datasets (WSJ, CallHome, Switchboard), suggesting it may be partially tuned to Whisper's specific output style (2212.04356.pdf, p. 12).
*   **Zero-Shot Focus:** This model was evaluated primarily in a zero-shot setting. Its performance after fine-tuning on specific datasets was not studied in the paper (2212.04356.pdf, p. 14).

### Recommendations:
*   **Use Heuristics for Long-Form Audio:** When transcribing audio longer than 30 seconds, users should employ the recommended decoding strategy, which includes beam search, temperature fallback, and conditioning on previous text, to mitigate common failure modes (2212.04356.pdf, p. 12-13).
*   **Be Cautious with Low-Resource Languages:** Users should expect high error rates when using the model on languages that are not well-represented in the training data (see Figure 11 on page 27 of the paper for a breakdown) (2212.04356.pdf, p. 7).
*   **Consider Model Size:** For English-only tasks, smaller models trained with limited compute may perform better if trained only on English data, as joint multilingual/multitask training can act as negative transfer. However, at a large scale, the joint training outperforms English-only training (2212.04356.pdf, p. 11-12).
*   **Future Improvements:** The paper suggests that performance could be improved by targeted data collection for low-resource languages, fine-tuning on high-quality supervised datasets, and developing more robust decoding strategies (2212.04356.pdf, p. 14).

---