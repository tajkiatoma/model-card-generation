## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by researchers from FAIR at Meta, INRIA, and UC Berkeley (2312.05187-1-100.pdf, p. 1).

### Model date:
The paper describing the model is dated November 30, 2023 (2312.05187-1-100.pdf, p. 1).

### Model version:
This model is **SeamlessM4T v2**. It is an improved version of the SeamlessM4T model (2312.05187-1-100.pdf, p. 1). Key improvements include:
*   **Upgraded Architecture**: It uses an updated multitask-UNITY2 framework with a non-autoregressive text-to-unit (T2U) decoder, which improves S2ST inference speed by 3x (2312.05187-1-100.pdf, p. 12).
*   **Enhanced Speech Encoder**: It incorporates a new w2v-BERT 2.0 speech encoder pre-trained on 4.5 million hours of unlabeled audio, a 4.5x increase from the previous version (2312.05187-1-100.pdf, p. 3, 12).
*   **Expanded Training Data**: The model was fine-tuned with more supervision from automatically aligned data (SeamlessAlign) to improve performance on low-resource languages (2312.05187-1-100.pdf, p. 3). The expanded SeamlessAlign adds 114,800 hours of data (2312.05187-1-100.pdf, p. 1, 14).

### Model type:
SeamlessM4T v2 is a foundational multilingual and multimodal model for speech and text translation (2312.05187-1-100.pdf, p. 3, 12). It is part of a family of models designed for end-to-end expressive and streaming translation (2312.05187-1-100.pdf, p. 1).

*   **Architecture**: The model uses a multitask-UNITY2 architecture. Its key components are (2312.05187-1-100.pdf, p. 12):
    *   A **Conformer speech encoder** pre-trained with the w2v-BERT 2.0 algorithm.
    *   A **text-to-text (T2TT) model** pre-trained on NLLB data.
    *   A novel **non-autoregressive text-to-unit (T2U) decoder** (UnitY2) with hierarchical modeling of subword, character, and discrete units.
    *   A multilingual **HiFi-GAN unit vocoder** to convert discrete units to waveform (2312.05187-1-100.pdf, p. 20).
*   **Category**: The model performs multiple tasks, including Automatic Speech Recognition (ASR), Speech-to-Text Translation (S2TT), Text-to-Text Translation (T2TT), Speech-to-Speech Translation (S2ST), and Text-to-Speech Translation (T2ST) (2312.05187-1-100.pdf, p. 12, Table 2).
*   **Model Size**: The large version of the model has 2.3 billion parameters (2312.05187-1-100.pdf, p. 13). The total size of the model weights is 9.24 GB (model.safetensors.index.json.txt).
*   **Context Length**: The `model_max_length` is set to a very large number in the configuration, suggesting no practical limit is specified (tokenizer_config.json.txt).

### Training details:
The model was developed using a multi-stage process involving pre-training separate components and then fine-tuning them jointly (2312.05187-1-100.pdf, p. 12).

*   **Self-Supervised Pre-training**: The w2v-BERT 2.0 speech encoder was pre-trained on approximately 4.5 million hours of unlabeled speech data from 143+ languages (2312.05187-1-100.pdf, p. 13, 16, Table 5).
*   **Component Pre-training**:
    *   A text-to-text (T2TT) model was pre-trained on NLLB data (2312.05187-1-100.pdf, p. 12).
    *   An X2T (speech/text to text) model was trained using knowledge distillation from the T2TT model on a combination of human-labeled, pseudo-labeled, and automatically aligned S2TT data (2312.05187-1-100.pdf, p. 12, 16).
    *   The UnitY2 text-to-unit (T2U) decoder was pre-trained using a teacher T2U model (2312.05187-1-100.pdf, p. 12, 20).
*   **Multitask Fine-tuning**: The final multitask-UNITY2 model was fine-tuned on 145K hours of pseudo-labeled and automatically aligned speech-to-unit data. During this stage, the X2T model components were frozen, and only the T2U model weights were updated (2312.05187-1-100.pdf, p. 20). The training process used a weighted sum of six loss functions, including losses for S2TT, T2TT, ASR, and knowledge distillation (2312.05187-1-100.pdf, p. 17).

### Paper or other resource for more information:
*   **Paper**: Seamless: Multilingual Expressive and Streaming Speech Translation. This paper introduces the Seamless model family, including SeamlessM4T v2, SeamlessExpressive, and SeamlessStreaming, detailing their architecture, training, and evaluation (2312.05187-1-100.pdf).
*   **Code Repository**: The models, code, and a watermark detector are publicly released at `https://github.com/facebookresearch/seamless_communication` (2312.05187-1-100.pdf, p. 1, 4).

### Citation details:
```bibtex
@article{seamless2023,
  title={Seamless: Multilingual Expressive and Streaming Speech Translation},
  author={Seamless Communication et al.},
  journal={arXiv preprint arXiv:2312.05187},
  year={2023}
}
```
(2312.05187-1-100.pdf)

### License:
Insufficient information

### Contact:
For correspondence, contact Xutai Ma at `xutaima@meta.com` (2312.05187-1-100.pdf, p. 1).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
SeamlessM4T v2 is a foundational model designed to support a wide range of multilingual and multimodal translation tasks. Its primary purpose is to provide state-of-the-art semantic accuracy across these tasks (2312.05187-1-100.pdf, p. 12).

*   **Tasks Supported**:
    *   **Speech-to-Text Translation (S2TT)**: Translates speech in one language to text in another. Supports 101 source languages into 96 target languages (2312.05187-1-100.pdf, p. 12, Table 2).
    *   **Speech-to-Speech Translation (S2ST)**: Translates speech in one language to speech in another. Supports 101 source languages into 36 target languages (2312.05187-1-100.pdf, p. 12, Table 2).
    *   **Text-to-Text Translation (T2TT)**: Translates text in one language to text in another. Supports 96 source and target languages (2312.05187-1-100.pdf, p. 12, Table 2).
    *   **Automatic Speech Recognition (ASR)**: Transcribes speech into text in the same language. Supports 96 languages (2312.05187-1-100.pdf, p. 12, Table 2).
    *   **Text-to-Speech Translation (T2ST)**: A zero-shot task that translates text in one language to speech in another (2312.05187-1-100.pdf, p. 21).
*   **Language Coverage**: The model supports nearly 100 languages for input (speech or text) and output (speech or text) (2312.05187-1-100.pdf, p. 3). A detailed list of supported languages and modalities is available in Table 1 of the paper (2312.05187-1-100.pdf, p. 10-11).
*   **Real-world Scenarios**: The model is intended to be a foundational component for systems that unlock cross-lingual communication in real-time, such as in audio/video calling, AR/VR environments, online streaming, and wearable devices (2312.05187-1-100.pdf, p. 83-84).

### Primary intended users:
The model is intended for a broad audience, including:
*   **Researchers and Developers**: To "spur further research into related domains" and build technologies that bridge multilingual connections (2312.05187-1-100.pdf, p. 4, 84).
*   **End-Users with Language Barriers**: Individuals, such as immigrants, who depend on translation technologies for "essential information gathering and communication" in their daily lives (2312.05187-1-100.pdf, p. 5).

### Out-of-scope uses:
The paper highlights several applications and behaviors that are out-of-scope or constitute misuse:
*   **Malicious Use**: The model should not be used for malicious purposes such as "voice phishing" or creating "deepfakes" (2312.05187-1-100.pdf, p. 85). The repository includes a watermarking mechanism to help mitigate this risk (2312.05187-1-100.pdf, p. 1).
*   **Localization**: The model is designed for translation, not localization. For example, it will translate units of measurement (e.g., "miles") but not convert them to a different system (e.g., "kilometers") even if that is the local standard (2312.05187-1-100.pdf, p. 68).
*   **Generating Harmful Content**: The model should not be used to produce outputs that could cause physical harm (e.g., loud saturated noises) or convey dangerously incorrect high-stakes information (e.g., health, legal) (2312.05187-1-100.pdf, p. 67-68).
*   **Adding Toxicity**: The model should not add toxicity to the output when none is present in the input (2312.05187-1-100.pdf, p. 68).

---

## How to Use
Insufficient information

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
The paper identifies and analyzes several factors that influence the model's performance:
*   **Data Resource Level**: The volume of available training data for a language (categorized as high, medium, or low) significantly impacts performance (2312.05187-1-100.pdf, p. 9, 23).
*   **Language Family**: Linguistic distance from English affects performance, with better results for closer language families like Italic and Germanic compared to more distant ones like Sinitic or Indo-Aryan (2312.05187-1-100.pdf, p. 51).
*   **Background Noise**: The presence of background noise (e.g., "music" or "noise") in the input speech can degrade performance (2312.05187-1-100.pdf, p. 58).
*   **Vocal Style Variations**: Variations in the speaker's vocal style can affect the model's robustness (2312.05187-1-100.pdf, p. 58).
*   **Gender**: The model's performance can vary based on grammatical gender, with analysis focusing on robustness to gender inflections and overgeneralization towards a specific gender (2312.05187-1-100.pdf, p. 78).
*   **Pitch and Accent**: The model's sensitivity to different pitch ranges and speaker accents is considered a potential source of bias (2312.05187-1-100.pdf, p. 68).

### Evaluation factors:
The model evaluation reports results disaggregated by the following factors:
*   **Resource Level**: Performance is analyzed for high, medium, and low-resource languages (2312.05187-1-100.pdf, p. 23, Table 9).
*   **Language Family**: Quality and latency are evaluated across different language subgroups (2312.05187-1-100.pdf, p. 51-52, Figures 13 & 14).
*   **Background Noise**: Robustness is evaluated by adding simulated noise from the MUSAN dataset to the input audio (2312.05187-1-100.pdf, p. 58).
*   **Vocal Style**: Robustness is evaluated using the FLEURS dataset, which contains vocal style variations (2312.05187-1-100.pdf, p. 58).
*   **Gender**: Gender bias is evaluated using the MULTILINGUAL HOLISTICBIAS dataset, analyzing robustness and overgeneralization (2312.05187-1-100.pdf, p. 78).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
A combination of automatic metrics is used to assess different aspects of the model's performance:
*   **Translation Quality**:
    *   **SacreBLEU**: Used for S2TT tasks (2312.05187-1-100.pdf, p. 21).
    *   **chrF2++**: Used for T2TT tasks (2312.05187-1-100.pdf, p. 21).
    *   **ASR-BLEU**: Used to evaluate the accuracy of S2ST and T2ST outputs by transcribing the generated speech with an ASR model (Whisper-Large) and comparing it to a reference translation (2312.05187-1-100.pdf, p. 21).
*   **Speech Recognition Quality**:
    *   **Word Error Rate (WER)**: Used for ASR tasks on normalized transcriptions (2312.05187-1-100.pdf, p. 21).
*   **Expressivity Preservation**:
    *   **AUTOPCP**: A neural model trained to predict human judgments of sentence-level prosody similarity (2312.05187-1-100.pdf, p. 37, 56).
    *   **Vocal Style Similarity (VSim)**: Cosine similarity of embeddings from a pretrained WavLM-based encoder on source and generated speech (2312.05187-1-100.pdf, p. 37).
    *   **Rhythm Metrics**: Spearman correlation of speech rate (**Rate**) and a joint pause alignment score (**Pause**) between source and generated speech (2312.05187-1-100.pdf, p. 37).
*   **Streaming Latency**:
    *   **Average Lagging (AL) and Length-Adaptive Average Lagging (LAAL)**: Used for text output to quantify the delay (2312.05187-1-100.pdf, p. 48).
    *   **Ending Offset**: The time difference between the end of the source speech and the end of the translated speech, used for speech output (2312.05187-1-100.pdf, p. 48).

### Decision thresholds:
*   **Streaming Policy**: The streaming models use a decision threshold `tEMMA` for the Efficient Monotonic Multihead Attention (EMMA) policy, which controls the latency-quality trade-off. Evaluations are reported for `tEMMA` values of 0.4, 0.5, 0.6, and 0.7 (2312.05187-1-100.pdf, p. 49, 50).
*   **Data Alignment**: A margin score threshold of 1.15 was used to filter automatically aligned data pairs for training (2312.05187-1-100.pdf, p. 14).

### Variation approaches:
For human evaluation results, the paper reports bootstrap re-sampled mean and standard error estimates, re-sampling 500 times at the item level to ensure robust measurements (2312.05187-1-100.pdf, p. 61).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The model was evaluated on a variety of public benchmarks:
*   **FLEURS**: A many-to-many speech translation benchmark used for S2TT, S2ST, ASR, and T2ST tasks. It covers 102 languages (2312.05187-1-100.pdf, p. 14, 21).
*   **CVSS**: A multilingual speech-to-speech translation corpus used for S2ST evaluation (2312.05187-1-100.pdf, p. 21).
*   **CoVOST 2**: A multilingual speech-to-text translation benchmark used for S2TT evaluation (2312.05187-1-100.pdf, p. 23).
*   **mExpresso**: A multilingual expressive speech dataset with acted speech in six styles across six languages, used for evaluating expressivity preservation (2312.05187-1-100.pdf, p. 25, 38).
*   **mDRAL**: A multilingual corpus of spontaneous conversations and re-enactments in six languages, used for evaluating expressivity in a more naturalistic setting (2312.05187-1-100.pdf, p. 25, 38).
*   **MULTILINGUAL HOLISTICBIAS**: A dataset used to evaluate gender bias in translation (2312.05187-1-100.pdf, p. 78).

### Motivation:
These datasets were chosen to comprehensively evaluate the model's capabilities across its various tasks and dimensions:
*   FLEURS, CVSS, and CoVOST 2 are standard benchmarks for assessing multilingual translation and ASR quality (2312.05187-1-100.pdf, p. 21).
*   mExpresso and mDRAL were specifically chosen for expressivity evaluation because they contain rich prosodic variations. mExpresso provides acted, stylized speech, while mDRAL contains more natural, spontaneous speech (2312.05187-1-100.pdf, p. 38, 60).
*   HOLISTICBIAS was used to specifically probe for gender bias, a key ethical consideration (2312.05187-1-100.pdf, p. 78).

### Preprocessing:
For ASR and ASR-BLEU evaluations, the transcribed hypotheses and reference texts are normalized before scoring. This follows the procedure from Radford et al. (2022) (2312.05187-1-100.pdf, p. 21). For streaming evaluation, starting and ending silences in the source audio were removed to better reflect real-life settings (2312.05187-1-100.pdf, p. 49).

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
SeamlessM4T v2 was trained on a massive and diverse collection of data from multiple sources, leveraging techniques to overcome the scarcity of labeled speech data (2312.05187-1-100.pdf, p. 13). The main data types are summarized in Figure 2 (p. 13) and Table 4 (p. 16):
*   **Unlabeled Speech**: 4.5 million hours of audio from 143+ languages from publicly available data repositories, used for self-supervised pre-training of the speech encoder (2312.05187-1-100.pdf, p. 13, 16).
*   **Paired Text Data**: 5 billion bitexts across 98 languages from sources like NLLB-SEED, PUBLICBITEXT, and mined data (MMTBT, SMTBT), used for pre-training the T2TT model (2312.05187-1-100.pdf, p. 13).
*   **Speech-to-Text Data**: A total of 351K hours for S2TT tasks, comprising:
    *   Human-labeled ASR and S2TT data.
    *   Pseudo-labeled ASR data, created by transcribing audio with an ASR model and translating the text with an NLLB model.
    *   Automatically aligned S2TT pairs from the **SeamlessAlign** dataset, which was expanded to cover 76 languages (2312.05187-1-100.pdf, p. 13, 15-16).
*   **Speech-to-Speech Data**: A total of 145K hours for S2ST tasks, comprising pseudo-labeled S2TT data (converted to units with a teacher T2U model) and automatically aligned S2S pairs (2312.05187-1-100.pdf, p. 13, 15-16).

### Motivation:
The choice of datasets was motivated by the need to build a high-quality, wide-coverage multilingual model despite the scarcity of human-labeled speech translation data. The strategy was to (2312.05187-1-100.pdf, p. 13):
1.  Leverage large amounts of unlabeled audio and text for powerful pre-trained components (w2v-BERT 2.0, NLLB).
2.  Use automatic alignment (SeamlessAlign) and pseudo-labeling to create large-scale, albeit noisy, supervised data for speech tasks.
3.  Combine these diverse data sources in a multitask learning framework to improve performance, especially for low-resource languages.

### Preprocessing:
The combined training data was subjected to a series of filtering steps to improve its quality (2312.05187-1-100.pdf, p. 15):
*   **Toxicity filtering**: Removed pairs with an imbalance in toxicity between source and target.
*   **Length filtering**: Removed utterances that were too short (<0.1s) or too long (>50s), or text longer than 250 sub-words.
*   **Special characters filtering**: Removed text with high proportions of emojis, punctuation, digits, or spaces.
*   **Repetition filtering**: Removed sentences with excessive character or n-gram repetition.
*   **Deduplication**: Removed data points with identical target text to prevent over-representation.
*   **Language ID (LID) filtering**: Discarded pairs where the target sentence language did not match the expected language, using an LID model.

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
The paper presents performance results broken down by several individual factors:
*   **Resource Level**: Table 9 shows the performance improvement of SeamlessM4T v2 over v1, broken down by low, medium, and high resource levels. For low-resource languages, S2TT BLEU improved by +2.8, S2ST ASR-BLEU by +4.3, and ASR WER by -7.5 (2312.05187-1-100.pdf, p. 23).
*   **Language Family**: Figures 13 and 14 show the quality-latency trade-off for streaming S2TT and S2ST across different language families. Performance is generally better for language families closer to English (Italic, Germanic) than for more distant ones (Sinitic, Japanesic) (2312.05187-1-100.pdf, p. 52).
*   **Gender**: Table 56 presents results for robustness (X-eng) and overgeneralization (eng-X) on inputs with masculine vs. feminine gender. For X-eng S2TT, the model achieves a chrF score of 54.2 for feminine source and 56.0 for masculine source (2312.05187-1-100.pdf, p. 79).
*   **Background Noise**: Figure 16 shows that as Signal-to-Noise Ratio (SNR) decreases, S2TT BLEU scores drop and ASR WER increases. At 0 dB SNR with music, SeamlessM4T v2 achieves a BLEU score of around 20, outperforming Whisper-Large-v2 (around 15) (2312.05187-1-100.pdf, p. 58).

### Intersectional results:
Insufficient information

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
Insufficient information

### Deploying Requirements:
Insufficient information

### Training or Fine-tuning Requirements:
The paper provides some details on the hardware used for training components, giving an indication of the required resources:
*   The PRETSSEL component was trained for 500k iterations using 16 V100 GPUs (2312.05187-1-100.pdf, p. 36).
*   The HiFi-GAN vocoder was trained for one million iterations on 8 V100 GPUs (2312.05187-1-100.pdf, p. 36).
*   The main X2T model was fine-tuned for a total of 200K updates (2312.05187-1-100.pdf, p. 17).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

The paper dedicates Section 8 to "Responsible AI," outlining a four-pronged approach to building the models safely and ethically (2312.05187-1-100.pdf, p. 4, 66).

*   **Risk Identification and Mitigation**:
    *   **Red Teaming**: The developers conducted one of the first known red-teaming efforts for multimodal machine translation to identify critical errors. Categories of errors tested include safety concerns (e.g., deviation in health/legal info), opposite sentiment, deviation in toxicity, named entity errors, gender bias, and hallucination of PII (2312.05187-1-100.pdf, p. 67-68).
    *   **Toxicity**: The model was evaluated for "added toxicity" (introducing toxic content not present in the source). A novel textless speech toxicity detector (MuTox) was developed, and a mitigation technique (MinTox) was implemented at inference time to reduce added toxicity by up to 80-90% in some cases (2312.05187-1-100.pdf, p. 70, 74).
    *   **Gender Bias**: The model was systematically evaluated for gender bias using the MULTILINGUAL HOLISTICBIAS dataset. Results show the model consistently improves robustness in handling gender variations compared to previous versions, but can still exhibit overgeneralization towards the masculine gender in some cases (2312.05187-1-100.pdf, p. 78).
    *   **Potential for Misuse**: The paper acknowledges the risk of misuse for "voice phishing" or "deepfakes" (2312.05187-1-100.pdf, p. 85). To mitigate this, an inaudible, localized watermarking mechanism (SeamlessWM) was developed and its detector was publicly released to help trace the provenance of AI-generated audio (2312.05187-1-100.pdf, p. 1, 79).
*   **Use of Sensitive Data**: The model was trained on large-scale public data, and specific filtering steps were applied to remove pairs with toxicity imbalance (2312.05187-1-100.pdf, p. 15). The red-teaming effort explicitly checked for hallucinations of personally identifiable information (PII) (2312.05187-1-100.pdf, p. 68).
*   **Known Fraught Use Cases**: The paper highlights that performance gaps may exist for different user groups based on race, accent, or gender, which could lead to subsequent performance degradation in expressive and streaming tasks (2312.05187-1-100.pdf, p. 84).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Performance Disparities**: Model performance may vary for different user populations. The paper acknowledges that performance gaps at the ASR stage for users of different races, accents, or genders can lead to downstream degradation in translation quality (2312.05187-1-100.pdf, p. 84).
*   **Potential for Misuse**: Despite mitigation efforts like watermarking, the models are "not impervious to unintended use" by bad actors for applications like voice phishing (2312.05187-1-100.pdf, p. 85).
*   **Critical Errors**: The red-teaming analysis identified several types of critical errors the model can still produce, including opposite sentiment, deviation in toxicity, and gender bias (2312.05187-1-100.pdf, p. 69-70, Tables 49 & 50).
*   **Toxicity Mitigation Limitations**: While the MinTox mitigation technique reduces added toxicity, it is less effective for S2ST tasks compared to S2TT tasks (2312.05187-1-100.pdf, p. 74).

### Recommendations:
*   **Responsible Use**: Users should be aware of the model's potential for misuse. The paper advocates for a "multifaceted approach" to safety, including individual-level AI literacy, scam prevention tactics, and increased public awareness (2312.05187-1-100.pdf, p. 85).
*   **Future Research**: The paper recommends that future work should focus on:
    *   Improving language coverage and closing performance gaps between high- and low-resource languages (2312.05187-1-100.pdf, p. 85).
    *   Ensuring systems work well for diverse user groups that have been historically underprioritized in AI development (2312.05187-1-100.pdf, p. 85).
    *   Integrating the visual modality to support sign languages, gestures, and other visual signals for more inclusive and robust communication (2312.05187-1-100.pdf, p. 85).

---