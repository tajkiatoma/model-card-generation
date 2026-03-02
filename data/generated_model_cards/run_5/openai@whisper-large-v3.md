## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers at OpenAI: Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1). OpenAI is an AI research and deployment company based in San Francisco, CA (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1).

### Model date:
The associated research paper was submitted on December 6, 2022 (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1).

### Model version:
This is the `large-v3` version of the Whisper model (`config.json`). The associated paper primarily discusses the training and performance of the initial "Large" and an improved "Large V2" model, which was trained for 2.5 times more epochs with additional regularization techniques like SpecAugment, Stochastic Depth, and BPE Dropout (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4). This v3 model is an iteration on that work.

### Model type:
The model is a "Whisper" type, specifically an encoder-decoder Transformer designed for conditional generation (`config.json`). It processes audio data and generates text transcripts (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).

**Architecture Details:**
*   **Overall Structure:** It is an encoder-decoder Transformer model (`config.json`; Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Encoder:** The encoder processes an 80-channel log-magnitude Mel spectrogram representation of the audio. It has a stem of two convolution layers (the second with a stride of two) with a GELU activation function. Sinusoidal position embeddings are added before the Transformer blocks are applied (`config.json`; Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Decoder:** The decoder is an audio-conditional language model that uses learned position embeddings and tied input-output token representations (`config.json`; Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Size and Layers:** The "Large" model has 1550M parameters (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Table 1, p. 5).
    *   Model dimensions (`d_model`): 1280 (`config.json`).
    *   Encoder layers: 32 (`config.json`).
    *   Decoder layers: 32 (`config.json`).
    *   Encoder attention heads: 20 (`config.json`).
    *   Decoder attention heads: 20 (`config.json`).
    *   Encoder FFN dimension: 5120 (`config.json`).
    *   Decoder FFN dimension: 5120 (`config.json`).
*   **Vocabulary:** The model uses a vocabulary of 51,866 tokens, which includes a byte-level BPE text tokenizer and special tokens for tasks and languages (`config.json`, `vocab.json`).
*   **Context Length:** The model is trained on 30-second audio chunks (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2). The maximum source position length is 1500, and the maximum target position length is 448 (`config.json`).

### Training details:
The model was trained using large-scale weak supervision on a diverse dataset.
*   **Algorithm:** The model is trained to predict audio transcripts in a supervised fashion (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1). It is a multitask model trained jointly for speech recognition, language identification, and speech translation (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4).
*   **Training Setup:**
    *   The models were trained with data parallelism across accelerators using FP16 precision with dynamic loss scaling (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4).
    *   **Optimizer:** AdamW (`Robust Speech Recognition via Large-Scale Weak Supervision.pdf`, p. 4).
    *   **Learning Rate Schedule:** Linear learning rate decay to zero after a warmup over the first 2048 updates (`Robust Speech Recognition via Large-Scale Weak Supervision.pdf`, p. 4).
    *   **Batch Size:** A batch size of 256 segments was used for the initial models (`Robust Speech Recognition via Large-Scale Weak Supervision.pdf`, p. 4).
*   **Regularization:** The "Large V2" model, an iteration before v3, incorporated SpecAugment, Stochastic Depth, and BPE Dropout for regularization (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4). The base models relied primarily on the diversity of the large dataset for generalization (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4).

### Paper or other resource for more information:
*   **Primary Paper:** "Robust Speech Recognition via Large-Scale Weak Supervision" by Radford et al. (2022). This paper details the motivation, data collection, training methodology, and extensive evaluation of the Whisper models (Robust Speech Recognition via Large-Scale Weak Supervision.pdf).
*   **Code Repository:** The authors released inference code and models at `https://github.com/openai/whisper` (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).

### Citation details:
```bibtex
@article{radford2022robust,
  title={Robust Speech Recognition via Large-Scale Weak Supervision},
  author={Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2212.04356},
  year={2022}
}
```
(Citation derived from Robust Speech Recognition via Large-Scale Weak Supervision.pdf)

### License:
Insufficient information.

### Contact:
For correspondence, the paper lists Alec Radford (`alec@openai.com`) and Jong Wook Kim (`jongwook@openai.com`) (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The model is intended for robust speech processing. It is a single, unified model designed to perform multiple tasks without the need for dataset-specific fine-tuning (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1, 5).

**Capabilities and Tasks:**
*   **Multilingual Speech Recognition:** Transcribing speech from 97 languages (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
*   **Speech Translation:** Translating speech from other languages into English (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
*   **Language Identification:** Identifying the language being spoken in an audio clip (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Voice Activity Detection (VAD):** Detecting segments of audio that contain no speech (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4).

**Input-Output Structure:**
*   **Input:** The model takes a 30-second chunk of audio, represented as an 80-channel log-Mel spectrogram (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Output:** The model generates a sequence of text tokens representing the transcript, translation, or task classification (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3). Special tokens are used to specify the task (e.g., `<|transcribe|>`, `<|translate|>`) and language (e.g., `<|en|>`, `<|fr|>`) (`generation_config.json`, `vocab.json`).

### Primary intended users:
The model and its code were released to "serve as a foundation for further work on robust speech processing," indicating that the primary intended users are AI researchers and developers in the field of speech processing (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 1).

### Out-of-scope uses:
The paper does not explicitly list out-of-scope uses. However, based on the model's design, some uses are implicitly out-of-scope for the base model:
*   **Direct Long-Form Transcription:** The model is trained on 30-second audio chunks and cannot process longer inputs at once. A specific buffered transcription strategy is required to handle longer audio files, which is not an inherent capability of the model itself (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 9).
*   **Speaker Diarization:** While the model can transcribe speech, it is not designed to distinguish between or identify different speakers in an audio recording (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).

---

## How to Use
Insufficient information.

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper identifies several factors that influence the model's performance:
*   **Language:** Performance varies significantly across different languages, strongly correlating with the amount of training data available for that language (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 7).
*   **Audio Quality and Noise:** The model's robustness is tested against additive noise (white noise and "pub noise"), with performance degrading as the signal-to-noise ratio (SNR) decreases (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 9).
*   **Domain and Recording Conditions:** The model is evaluated across a wide range of domains, including read speech (LibriSpeech), podcasts (Rev16), phone calls (CallHome), meetings (AMI), and earnings calls (Earnings-21), showing performance variation across these different conditions (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 6, 9).
*   **Speaker Accents and Dialects:** The model is evaluated on datasets like CORAAL (Corpus of Regional African American Language) to assess performance on different dialects (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 9).

### Evaluation factors:
The model evaluation reports performance disaggregated by:
*   **Dataset/Domain:** Performance is reported separately for each of the 12+ academic datasets used for evaluation (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Table 2, p. 6).
*   **Language:** For multilingual tasks, performance is broken down by language (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 7).
*   **Noise Level:** Robustness is evaluated across a range of signal-to-noise ratios (SNRs) (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Figure 5, p. 8).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Word Error Rate (WER):** This is the primary metric for speech recognition tasks. The paper notes that a custom text normalizer is used before calculating WER to minimize penalties from formatting or punctuation differences that do not affect semantic meaning (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 5).
*   **BLEU Score:** This metric is used to evaluate the performance of speech translation tasks (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 8).
*   **Accuracy:** This metric is used for language identification tasks (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 8).

### Decision thresholds:
For long-form transcription, a set of heuristics with specific thresholds are used to improve reliability:
*   A **no-speech probability threshold of 0.6** is combined with an **average log-probability threshold of -1.0** to improve voice activity detection (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 13).
*   The initial timestamp token is constrained to be between **0.0 and 1.0 seconds** to prevent the model from ignoring the beginning of an audio segment (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 13).

### Variation approaches:
The paper uses **95% bootstrap estimate confidence intervals** to show the statistical variance in performance when comparing English-only and multilingual/multitask models across different model sizes (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Figure 9, p. 12).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated in a zero-shot setting on a wide range of existing academic datasets.

**Short-form English-only datasets:**
*   LibriSpeech (test-clean and test-other splits)
*   TED-LIUM 3 (test split)
*   Common Voice 5.1 (English subset)
*   Artie bias corpus (a subset of Common Voice)
*   CallHome and Switchboard
*   WSJ
*   CORAAL
*   CHiME-6
*   AMI-IHM and AMI-SDM1
(Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Appendix A.1, p. 19)

**Long-form English-only datasets:**
*   TED-LIUM 3 (full-length talks from the test split)
*   Meanwhile (64 segments from The Late Show with Stephen Colbert)
*   Rev16 (a subset of 16 podcast episodes)
*   Kincaid46 (46 audio files from a blog article benchmark)
*   Earnings-21 and Earnings-22
*   CORAAL (full-length interviews)
(Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Appendix A.2, p. 19)

**Multilingual datasets:**
*   Multilingual LibriSpeech (MLS)
*   Fleurs
*   VoxPopuli
*   Common Voice 9
*   CoVoST 2 (for X-to-English translation)
(Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Appendix A.3, p. 20)

### Motivation:
The datasets were chosen to cover a wide variety of domains, tasks, languages, and recording conditions. This allows for a comprehensive study of the model's ability to generalize in a zero-shot setting, which is a measure of its broad robustness (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 5).

### Preprocessing:
An extensive text standardization process is applied to both the model's output and the reference transcripts before calculating the Word Error Rate (WER). This is done to "better distinguish between innocuous differences in wording and genuine mistranscriptions" (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 21).

**For English text, the steps include:**
1.  Removing phrases in brackets `[]` and parentheses `()`.
2.  Removing filler words like `hmm`, `uh`, `um`.
3.  Normalizing contractions (e.g., "you're" to "you are").
4.  Removing commas between digits and periods not followed by numbers.
5.  Removing symbols and diacritics.
6.  Normalizing numeric expressions to a standard form (e.g., "Ten thousand dollars" to "$10000").
7.  Converting British spellings to American spellings.
8.  Replacing successive whitespace characters with a single space.
(Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Appendix C, p. 21)

**For non-English text, a simpler standardization is used:**
1.  Removing phrases in brackets and parentheses.
2.  Replacing markers, symbols, and punctuation with a space.
3.  Converting the text to lowercase.
4.  Replacing successive whitespace characters with a single space.
(Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Appendix C, p. 21)

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a large-scale, weakly supervised dataset collected from the internet.
*   **Size:** 680,000 hours of audio data (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
*   **Content:** The dataset is multilingual and multitask.
    *   **English Speech Recognition:** 65% of the data (438,218 hours) is for English speech recognition (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Figure 11, p. 27).
    *   **Multilingual Speech Recognition:** 17% of the data (117,113 hours) covers 96 other languages (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2, Figure 11, p. 27).
    *   **Translation to English:** 18% of the data (125,739 hours) is for speech translation into English (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2, Figure 11, p. 27).
*   **Source:** The data consists of audio-transcript pairs scraped from the internet, resulting in a very diverse dataset covering a broad distribution of environments, recording setups, and speakers (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).

### Motivation:
The goal was to scale up weakly supervised pre-training by an order of magnitude to improve the robustness and generalization of speech recognition models, removing the need for dataset-specific fine-tuning to achieve high-quality results (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).

### Preprocessing:
The raw data from the internet underwent several automated and manual filtering steps to improve its quality.
*   **Audio Preprocessing:** All audio is re-sampled to 16,000 Hz. An 80-channel log-magnitude Mel spectrogram is computed on 25-millisecond windows with a 10-millisecond stride. The input is globally scaled to be between -1 and 1 (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).
*   **Transcript Filtering:**
    *   Heuristics were used to detect and remove machine-generated transcripts (e.g., all-lowercase or all-uppercase text) (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
    *   An audio language detector was used to ensure the spoken language matched the transcript language. Mismatched pairs where the transcript was English were used for speech translation training (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
    *   Fuzzy de-duping was applied to transcript texts to reduce duplication (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
*   **Segmentation:** Audio files are broken into 30-second segments, paired with the corresponding transcript text (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 2).
*   **Final Filtering:** An initial model was trained and used to identify data sources with high error rates, which were then manually inspected and removed (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
*   **Performance by Dataset:** The WER for the `large-v2` model on various English datasets includes: LibriSpeech Clean (2.7%), Common Voice (9.0%), TED-LIUM (4.0%), Switchboard (13.8%), and WSJ (3.9%) (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Table 2, p. 6).
*   **Performance by Language:** On the Fleurs dataset, zero-shot WER for the `large-v2` model varies widely, from 4.2% on Spanish to over 100% on languages like Amharic and Javanese (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Figure 3, p. 7; Table 13, p. 24).
*   **Performance by Noise Level:** On LibriSpeech test-clean with additive pub noise, the `large-v2` model's WER is below 10% at an SNR of 10 dB and around 20% at 0 dB (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Figure 5, p. 8).
*   **Translation Performance:** On the CoVoST2 X→En translation task, the `large-v2` model achieves a BLEU score of 36.3 on high-resource languages, 31.5 on medium-resource, and 21.5 on low-resource languages (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, Table 15, p. 26).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
The total size of the model weights is approximately 6.17 GB (`model.safetensors.index.json`). The model weights are stored in `float16` precision (`config.json`).

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The models were trained using data parallelism across multiple accelerators with FP16 precision (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 4). Specific hardware details (e.g., number or type of GPUs, memory requirements) are not provided.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Bias:** The pre-training dataset is acknowledged to be "very English-heavy due to biases of our data collection pipeline, which sourced primarily from English-centric parts of the internet." This results in significantly poorer performance on low-resource languages (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Potential for Misuse:** As a general-purpose speech recognition tool, the model could be used for surveillance or to transcribe private conversations without consent. The paper does not discuss mitigation strategies for this risk.
*   **Hallucination:** The paper notes a failure mode where the model "will output a transcript entirely unrelated to the actual audio." This could lead to the generation of false or misleading information (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Sensitive Data:** The training data was collected from the internet and was not filtered for personal or sensitive information. The model may have been trained on such data and could potentially reproduce it in its outputs.

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Long-Form Transcription Reliability:** The model is trained on 30-second segments. While a strategy for transcribing longer audio is proposed, it relies on heuristics to work around the model's "noisy predictions." Failure modes like repetition loops and hallucination are still present (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 13-14).
*   **Performance on Low-Resource Languages:** The model's performance is "still quite poor on many languages." Its effectiveness is strongly correlated with the amount of training data available for a given language (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Overfitting to Normalizer:** The text normalizer used for evaluation was developed alongside the model. While it generalizes to other models, it reduces WER more significantly for Whisper on certain datasets (e.g., WSJ, CallHome), potentially inflating its relative performance (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 12).
*   **Speaker Guessing:** The model has a tendency to guess speaker names, which are often incorrect. This behavior is mitigated by fine-tuning the model on a subset of transcripts that do not include speaker annotations (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 5).

### Recommendations:
The paper suggests several areas for future work to improve upon the model:
*   **Improved Decoding Strategies:** Fine-tuning on high-quality supervised datasets or using reinforcement learning could help reduce decoding errors like repetition and hallucination (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Targeted Data Collection:** A targeted effort to increase the amount of training data for low-resource languages could lead to large performance improvements (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Study of Fine-Tuning:** The paper focuses on zero-shot performance. Further study is needed to understand how fine-tuning affects the model's capabilities and to allow for direct comparison with other common evaluation paradigms (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).
*   **Incorporate Auxiliary Objectives:** While not found to be necessary for good performance, incorporating unsupervised pre-training or self-teaching methods could potentially improve results further (Robust Speech Recognition via Large-Scale Weak Supervision.pdf, p. 14).