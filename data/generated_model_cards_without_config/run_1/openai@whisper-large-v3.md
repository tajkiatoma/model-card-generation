## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model, named Whisper, was developed by researchers at OpenAI (2212.04356.pdf, p. 1). The listed authors are Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and Ilya Sutskever (2212.04356.pdf, p. 1).

### Model date:
The associated academic paper was submitted to arXiv on December 6, 2022 (2212.04356.pdf, p. 1). The commercial ASR services used for comparison were queried on September 1, 2022 (2212.04356.pdf, p. 10).

### Model version:
The paper describes a suite of models of varying sizes. It also specifically mentions a "Large V2" model, which was trained for 2.5 times more epochs than the original "Large" model and included regularization techniques such as SpecAugment, Stochastic Depth, and BPE Dropout (2212.04356.pdf, p. 4, Table 18, p. 28). The results reported in the paper were updated to reflect this improved V2 model unless otherwise specified (2212.04356.pdf, p. 4).

### Model type:
Whisper is an encoder-decoder Transformer model designed for speech processing tasks (2212.04356.pdf, p. 3).

*   **Architecture:** The model uses a standard Transformer architecture. The encoder processes an 80-channel log-magnitude Mel spectrogram computed from 25-millisecond windows of audio with a 10-millisecond stride. The encoder stem consists of two convolution layers. Sinusoidal position embeddings are added before the Transformer blocks. The decoder uses learned position embeddings and tied input-output token representations (2212.04356.pdf, p. 3).
*   **Category:** It is a multitask and multilingual model for automatic speech recognition (ASR), speech translation, spoken language identification, and voice activity detection (2212.04356.pdf, p. 3).
*   **Size:** The model comes in several sizes, from Tiny to Large. The "Large" version has 1550M (1.55 billion) parameters, with 32 layers, a model width of 1280, and 20 attention heads (2212.04356.pdf, Table 1, p. 5). The total size of the FP32 version of the large model is 6,173,962,240 bytes (approx. 6.17 GB) (pytorch_model.bin.index.fp32.json.txt; model.safetensors.index.fp32.json.txt).
*   **Tokenizer:** A byte-level Byte-Pair Encoding (BPE) tokenizer is used, with a vocabulary size of 50,257 (merges.txt; tokenizer_summary.json.txt). For multilingual models, the vocabulary was refit from the GPT-2 vocabulary to better handle non-English languages (2212.04356.pdf, p. 3).
*   **Context Length:** The model processes audio in 30-second chunks (2212.04356.pdf, p. 2, 9). The tokenizer configuration specifies a `model_max_length` of 1000000000000000019884624838656 (tokenizer_config.json.txt).

### Training details:
*   **Algorithm:** The model was trained using weakly supervised learning on a large-scale dataset (2212.04356.pdf, p. 1).
*   **Parameters and Hyperparameters:**
    *   The models were trained with data parallelism in FP16 precision with dynamic loss scaling (2212.04356.pdf, p. 4).
    *   **Optimizer:** AdamW (2212.04356.pdf, Table 17, p. 28).
    *   **Learning Rate Schedule:** Linear decay with a warmup over the first 2048 updates (2212.04356.pdf, p. 4, Table 17, p. 28). Maximum learning rates varied by model size, e.g., 2.0 x 10\⁻⁴ for the Large V2 model (2212.04356.pdf, Table 19, p. 28).
    *   **Batch Size:** 256 segments (2212.04356.pdf, p. 4, Table 17, p. 28). For the Large V2 model, the batch size was 1024 (2212.04356.pdf, Table 18, p. 28).
    *   **Epochs:** The models were trained for 2-3 passes over the dataset (2212.04356.pdf, p. 4). The Large V2 model was trained for 2.5 times more epochs than the original (2212.04356.pdf, p. 4).
*   **Regularization:** The initial models did not use data augmentation. The Large V2 model added SpecAugment, Stochastic Depth (0.1), and BPE Dropout (0.1) for regularization (2212.04356.pdf, p. 4, Table 18, p. 28).

### Paper or other resource for more information:
The primary resource is the academic paper:
*   Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). *Robust Speech Recognition via Large-Scale Weak Supervision*. arXiv preprint arXiv:2212.04356. (2212.04356.pdf)

The paper also provides a link to the official repository for models and inference code:
*   <https://github.com/openai/whisper> (2212.04356.pdf, p. 2)

### Citation details:
The following BibTeX entry can be used for citation (2212.04356.pdf, p. 1):
```bibtex
@article{radford2022robust,
  title={Robust Speech Recognition via Large-Scale Weak Supervision},
  author={Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  journal={arXiv preprint arXiv:2212.04356},
  year={2022}
}
```

### License:
Insufficient information.

### Contact:
Correspondence can be directed to Alec Radford (<alec@openai.com>) or Jong Wook Kim (<jongwook@openai.com>) (2212.04356.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
Whisper is a general-purpose speech processing model designed to work reliably "out of the box" in a broad range of environments without requiring dataset-specific fine-tuning (2212.04356.pdf, p. 2, 5). Its primary uses are:

*   **Multilingual Speech Recognition:** Transcribing speech from 97 languages (2212.04356.pdf, p. 2).
*   **Speech Translation:** Translating speech from any of the supported languages into English (2212.04356.pdf, p. 2, 3).
*   **Spoken Language Identification:** Identifying the language being spoken in an audio clip (2212.04356.pdf, p. 3).
*   **Voice Activity Detection (VAD):** Detecting the presence or absence of speech in audio (2212.04356.pdf, p. 3).

The model is designed to handle a wide diversity of audio from different environments, recording setups, and speakers (2212.04356.pdf, p. 2). It can also perform long-form transcription on audio files that are minutes or hours long (2212.04356.pdf, p. 9).

### Primary intended users:
The model and code were released to "serve as a foundation for further work on robust speech processing," indicating that the primary intended users are AI researchers and developers in the field of speech processing (2212.04356.pdf, p. 1).

### Out-of-scope uses:
The paper does not explicitly list out-of-scope uses. However, based on its design, the model is not intended for:
*   Processing modalities other than audio.
*   Real-time transcription, as the current implementation processes audio in 30-second chunks (2212.04356.pdf, p. 9).
*   Speaker diarization (identifying who is speaking), as the model was specifically fine-tuned to remove the behavior of guessing speaker names (2212.04356.pdf, p. 5).

---

## How to Use
This section outlines how to use the model.

The model processes 30-second segments of audio and predicts a sequence of tokens. The task is specified by providing a sequence of special tokens to the decoder (2212.04356.pdf, p. 3).

The input to the model is an 80-channel log-magnitude Mel spectrogram representation of 16,000 Hz audio (2212.04356.pdf, p. 3).

The decoding process is controlled by a sequence of special tokens (2212.04356.pdf, p. 3; added_tokens.json.txt):
1.  **`<|startoftranscript|>`:** This token signals the beginning of a prediction task.
2.  **Language Token:** A token specifying the language of the audio (e.g., `<|en|>`, `<|de|>`). This is used for both transcription and as a target for language identification.
3.  **Task Token:** Either `<|transcribe|>` for speech-to-text in the identified language or `<|translate|>` for speech-to-English translation.
4.  **Timestamp Control Token:** `<|notimestamps|>` is used to specify that no timestamps should be predicted. If this token is omitted, the model will interleave timestamp tokens (e.g., `<|0.00|>`, `<|5.24|>`) with the text tokens.
5.  **Output Text:** The model generates the transcribed or translated text.
6.  **`<|endoftext|>`:** This token marks the end of the transcription.

For long-form transcription of audio longer than 30 seconds, a buffered approach is used, where the model processes consecutive 30-second windows, using predicted timestamps to align the segments (2212.04356.pdf, p. 9, 12).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The model's performance is influenced by several factors due to the diverse nature of its training data:
*   **Language:** The model's performance varies significantly across the 97 languages it supports, strongly correlating with the amount of training data available for each language (2212.04356.pdf, p. 7, Figure 3).
*   **Audio Quality and Environment:** The model was trained on a wide distribution of audio, including different recording setups and environments (e.g., ambient noise, chatter) (2212.04356.pdf, p. 2). Its robustness to additive white noise and "pub noise" was explicitly evaluated (2212.04356.pdf, p. 9).
*   **Task:** Performance varies by task (e.g., transcription vs. translation) (2212.04356.pdf, p. 11, Figure 8).
*   **Domain and Speaker Style:** The model was evaluated across many academic datasets covering different domains, such as audiobooks (LibriSpeech), phone calls (CallHome, Switchboard), and talks (TED-LIUM) (2212.04356.pdf, p. 6, Table 2).

### Evaluation factors:
The model evaluation reported in the paper analyzes performance across:
*   **Multiple Datasets:** A suite of 12+ English datasets and several multilingual datasets (Fleurs, MLS, VoxPopuli) were used to measure robustness and generalization (2212.04356.pdf, p. 6, 19).
*   **Languages:** Performance is reported on a per-language basis for multilingual benchmarks (2212.04356.pdf, p. 23-26).
*   **Noise Conditions:** Performance is measured across different signal-to-noise ratios (SNR) for both white noise and pub noise (2212.04356.pdf, p. 8, Figure 5).
*   **Model Size:** The effect of model size (Tiny, Base, Small, Medium, Large) on performance is analyzed across all tasks (2212.04356.pdf, p. 11, Figure 8).
*   **Dataset Size:** The effect of training dataset size on performance is analyzed by training on subsets of the full data (2212.04356.pdf, p. 11, Table 6).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Word Error Rate (WER):** The primary metric for speech recognition. The paper uses an extensive text normalization process to minimize penalties for non-semantic differences like formatting and punctuation before calculating WER (2212.04356.pdf, p. 5, Appendix C, p. 21).
*   **Relative Error Reduction (RER):** Used to compare the robustness of Whisper to other models (2212.04356.pdf, p. 6, Table 2).
*   **BLEU Score:** Used to evaluate the performance of speech-to-English translation (X→en) (2212.04356.pdf, p. 8).
*   **Accuracy:** Used to measure performance on language identification (2212.04356.pdf, p. 8).

### Decision thresholds:
For long-form transcription, several heuristics and thresholds are used to improve reliability:
*   A **no-speech probability threshold of 0.6** is combined with an **average log-probability threshold of -1.0** to improve voice activity detection (2212.04356.pdf, p. 12).
*   The initial timestamp token is constrained to be between **0.0 and 1.0 seconds** to prevent the model from ignoring the beginning of an audio segment (2212.04356.pdf, p. 12).
*   Decoding temperature is increased from 0.0 to 1.0 if the average log probability is lower than -1.0 or the gzip compression rate of the text is higher than 2.4, to handle repetitive loops (2212.04356.pdf, p. 12).

### Variation approaches:
The paper uses a 95% bootstrap estimate for confidence intervals when analyzing the scaling properties of the models (2212.04356.pdf, p. 12, Figure 9).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated in a zero-shot setting on a wide range of existing academic datasets without using their training splits (2212.04356.pdf, p. 5). A full list is provided in Appendix A of the paper (2212.04356.pdf, p. 19-20).

**Short-form English Datasets:**
*   LibriSpeech (test-clean and test-other)
*   TED-LIUM 3 (test split)
*   Common Voice 5.1 (English subset)
*   Artie bias corpus
*   CallHome and Switchboard
*   WSJ
*   CORAAL
*   CHiME-6
*   AMI-IHM and AMI-SDM1

**Long-form English Datasets:**
*   TED-LIUM 3 (11 full-length talks)
*   Meanwhile (64 segments from The Late Show with Stephen Colbert)
*   Rev16 (a subset of 16 podcast episodes)
*   Kincaid46 (46 audio files from a blog post benchmark)
*   Earnings-21 and Earnings-22
*   CORAAL (231 full-length interviews)

**Multilingual Datasets:**
*   Multilingual LibriSpeech (MLS)
*   Fleurs (used for transcription, translation, and language ID)
*   VoxPopuli (ASR data in 16 languages)
*   Common Voice 9
*   CoVoST 2 (X into English translation)

### Motivation:
The datasets were chosen to measure the model's broad generalization and robustness across a wide variety of domains, tasks, languages, recording conditions, and speaker styles (2212.04356.pdf, p. 5, 9). Using many datasets for evaluation helps to avoid overstating model capabilities based on performance on a single, narrow benchmark (2212.04356.pdf, p. 6).

### Preprocessing:
Before calculating WER, the reference transcripts from the evaluation datasets undergo an extensive text standardization process. This is a best-effort attempt to penalize only genuine mistranscriptions, not differences in formatting or punctuation (2212.04356.pdf, p. 5).

**For English text, the steps include:**
1.  Removing text within brackets `[]` and parentheses `()`.
2.  Removing filler words like `hmm`, `uh`, `um`.
3.  Normalizing contracted forms (e.g., "you're" to "you are").
4.  Removing commas between digits and periods not followed by numbers.
5.  Normalizing numeric and currency expressions (e.g., "Ten thousand dollars" to "$10000").
6.  Converting British spellings to American spellings.
7.  Removing most symbols and diacritics.
8.  Collapsing successive whitespace characters.
(2212.04356.pdf, Appendix C, p. 21)

**For non-English text, a simpler process is used:**
1.  Removing text within brackets and parentheses.
2.  Replacing punctuation and symbols with a space.
3.  Making the text lowercase.
4.  Collapsing successive whitespace characters.
(2212.04356.pdf, Appendix C, p. 21)

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a new dataset of 680,000 hours of audio-transcript pairs collected from the internet (2212.04356.pdf, p. 2).
*   **Size and Structure:** The dataset is composed of 30-second audio segments paired with text transcripts (2212.04356.pdf, p. 2).
*   **Diversity:** The dataset is multilingual and multitask.
    *   **65%** of the data (438,218 hours) is English-language speech recognition.
    *   **17%** (117,113 hours) is non-English speech recognition, covering 96 other languages.
    *   **18%** (125,739 hours) is translation from another language into English.
    (2212.04356.pdf, p. 2, Figure 11, p. 27).
*   The data covers a broad distribution of audio from many different environments, recording setups, and speakers (2212.04356.pdf, p. 2).

### Motivation:
The dataset was created to scale up weakly supervised pre-training for speech recognition to a level comparable with large-scale unsupervised methods. The goal was to create a large and diverse supervised dataset to train a single robust model that generalizes well across many tasks and domains without needing fine-tuning (2212.04356.pdf, p. 2).

### Preprocessing:
The data processing pipeline was designed to be minimalist (2212.04356.pdf, p. 2).
*   **Filtering:** Several automated filtering methods were developed to improve transcript quality. This included heuristics to detect and remove machine-generated transcripts (e.g., by checking for all-lowercase text or lack of punctuation) (2212.04356.pdf, p. 2).
*   **Language Verification:** An audio language detector was used to ensure the spoken language in the audio matched the language of the transcript. Mismatched pairs where the transcript was English were repurposed as speech-to-English translation data (2212.04356.pdf, p. 2).
*   **De-duplication:** Fuzzy de-duping of transcript texts was used to reduce duplication (2212.04356.pdf, p. 2).
*   **Segmentation:** Audio files were broken into 30-second segments and paired with the corresponding subset of the transcript (2212.04356.pdf, p. 2).
*   **Feature Extraction:** All audio was re-sampled to 16,000 Hz, and an 80-channel log-magnitude Mel spectrogram was computed and scaled to be between -1 and 1 (2212.04356.pdf, p. 3).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper provides extensive quantitative analyses broken down by various factors:

*   **Performance by Dataset:** Table 2 shows the Word Error Rate (WER) for the Large V2 model on 15 different English speech recognition datasets, ranging from 2.7% on LibriSpeech Clean to 36.4% on AMI SDM1 (2212.04356.pdf, p. 6).
*   **Performance by Language:**
    *   For multilingual speech recognition on the Fleurs dataset, WERs for the Large V2 model range from 4.2% (Spanish) to 140.3% (Javanese) (2212.04356.pdf, p. 24-25).
    *   For speech translation to English on the CoVoST2 dataset, BLEU scores for the Large V2 model range from 15.0 (Indonesian) to 48.1 (Spanish) (2212.04356.pdf, p. 26).
*   **Performance by Noise Level:** Figure 5 shows that the Large V2 model's WER on LibriSpeech test-clean increases as the Signal-to-Noise Ratio (SNR) decreases. For "pub noise," the WER is below 5% at 20 dB SNR but rises to over 50% at -5 dB SNR (2212.04356.pdf, p. 8).
*   **Performance by Model Size:** Figure 8 shows that as model size increases from Tiny (39M params) to Large (1550M params), average WER on English datasets drops from ~17% to ~10%, and average multilingual WER on Fleurs drops from ~60% to ~29% (2212.04356.pdf, p. 11).
*   **Performance by Training Data Size:** Table 6 shows that as training data increases from 3,405 hours to 681,070 hours, the Medium model's average English WER drops from 30.5% to 9.9% (2212.04356.pdf, p. 11).

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information.

### Deploying Requirements:
Insufficient information.

### Training or Fine-tuning Requirements:
The models were trained with data parallelism across accelerators using FP16 precision with dynamic loss scaling (2212.04356.pdf, p. 4). The specific number and type of accelerators (e.g., GPUs/TPUs) are not specified.

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Data Source:** The model was trained on 680,000 hours of audio and transcripts from the internet (2212.04356.pdf, p. 2). This data may contain personal or sensitive information. The dataset is also acknowledged to be "English-heavy" due to biases in the data collection pipeline (2212.04356.pdf, p. 14).
*   **Potential Risks:**
    *   **Misuse:** Like any speech recognition technology, this model could be used for surveillance purposes.
    *   **Performance Disparities:** The model's performance is significantly worse on low-resource languages for which there was little training data (2212.04356.pdf, p. 7, 14). This could lead to inequitable performance for speakers of those languages.
    *   **Hallucination:** The model can "complete hallucination where the model will output a transcript entirely unrelated to the actual audio," which could lead to the generation of misinformation (2212.04356.pdf, p. 14).
*   **Risk Mitigation:**
    *   **Transparency:** The developers released the models and inference code to serve as a foundation for further work and to allow for scrutiny (2212.04356.pdf, p. 1).
    *   **Policy Consultation:** The paper acknowledges a policy advisor for advising the project, suggesting that policy and ethical considerations were part of the development process (2212.04356.pdf, p. 14).
    *   **Data Filtering:** Automated methods were used to filter the training data, including removing machine-generated transcripts to avoid learning "transcript-ese" (2212.04356.pdf, p. 2).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance on Low-Resource Languages:** The model's performance is still "quite poor on many languages" due to the English-heavy nature of the training data (2212.04356.pdf, p. 14).
*   **Long-Form Transcription Errors:** The model can exhibit failure modes during long-form transcription, such as getting stuck in repetitive loops, failing to transcribe the beginning or end of an audio segment, or hallucinating text completely unrelated to the audio (2212.04356.pdf, p. 14). The heuristics used to mitigate this are a "workaround for the noisy predictions of the model" (2212.04356.pdf, p. 12).
*   **Text Normalizer Overfitting:** The text normalizer used for evaluation was developed alongside the model, creating a risk that it is overfitted to Whisper's specific transcription style and may not be a neutral benchmark when comparing to other models (2212.04356.pdf, p. 12).
*   **Speaker Identification:** The model has a tendency to transcribe plausible but incorrect guesses for speaker names, a behavior that was mitigated by fine-tuning the model on a subset of transcripts without speaker annotations (2212.04356.pdf, p. 5).

### Recommendations:
*   **Use for Robustness Research:** The released models and code are intended to "serve as a foundation for further work on robust speech processing" (2212.04356.pdf, p. 1).
*   **Emphasize Zero-Shot Evaluation:** The authors suggest that "emphasizing zero-shot and out-of-distribution evaluations of models, particularly when attempting to compare to human performance," is important to avoid overstating model capabilities (2212.04356.pdf, p. 6).
*   **Future Improvements:** The paper suggests several avenues for future work, including:
    *   Targeted data collection to improve performance on low-resource languages (2212.04356.pdf, p. 14).
    *   Fine-tuning on high-quality supervised datasets or using reinforcement learning to improve decoding strategies and reduce errors (2212.04356.pdf, p. 14).
    *   Further study into the benefits of fine-tuning for specific domains where high-quality data is available (2212.04356.pdf, p. 14).