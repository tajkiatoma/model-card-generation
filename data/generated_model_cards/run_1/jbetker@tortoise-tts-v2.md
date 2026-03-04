## Model Details
This section provides fundamental information about the model, helping stakeholders understand its context and key characteristics.

### Person or organization developing model:
The model was developed by James Betker, an independent researcher (2305.07243v2.pdf, p. 1, 12). The author's email is james@adamant.ai (setup.py).

The project is described as a product of the open-source community. Special thanks are given to Kim Betker for support, as well as to several contributors for their instrumental work: Phil Wang (author of x-transformers), Kim Seonghyeon (author of the VQVAE implementation), FAIR (for open-sourcing tooling and technology), and Prafulla Dhariwal and Alex Nichol (for their work on improved diffusion models) (2305.07243v2.pdf, p. 12).

### Model date:
The associated research paper is dated May 23, 2023 (2305.07243v2.pdf, p. 1). The development and training of the models took place over a period of one year (2305.07243v2.pdf, p. 4).

### Model version:
The model version is 2.1.3 (setup.py). The associated paper and model weights are referred to as "v2" (2305.07243v2.pdf, p. 3; api.py). Insufficient information is available in the repository to describe how this version differs from previous ones.

### Model type:
TorToise is a text-to-speech (TTS) system that combines several neural network models to generate high-quality, multi-voice speech from text and reference audio clips (2305.07243v2.pdf, p. 1, 3). The architecture consists of four main components:

1.  **Autoregressive (AR) Model**: This model uses a GPT-2 architecture to convert text tokens into a sequence of discrete speech codes or continuous latents. It is a Transformer stack with 30 layers, a model dimension of 1024, and 16 attention heads. It supports a maximum sequence length of 402 text tokens and 604 MEL tokens (2305.07243v2.pdf, p. 8, 9; tortoise/models/autoregressive.py; api.py).

2.  **Contrastive Language-Voice Pretrained Transformer (CLVP)**: Similar to CLIP, this model is used to score and re-rank the outputs from the autoregressive model, selecting the best candidates. It consists of two parallel Transformer encoders, one for text and one for speech. The implementation uses x-transformers with 12 encoder layers, 8 attention heads, and a model dimension of 512 for both text and speech encoders. The maximum sequence length is 350 for text and 430 for speech tokens (2305.07243v2.pdf, p. 4; tortoise/models/clvp.py; api.py).

3.  **Diffusion Decoder (DDPM)**: A Denoising Diffusion Probabilistic Model that converts the speech codes or AR latents into a MEL spectrogram. It is a U-Net-like architecture combining residual convolutions and dense self-attention. It has 10 layers, a model dimension of 1024, and 16 attention heads (2305.07243v2.pdf, p. 3, 11, 12; tortoise/models/diffusion_decoder.py; api.py).

4.  **Vocoder**: A pre-trained UnivNet model is used as a MEL inverter to convert the final MEL spectrogram into a raw audio waveform (2305.07243v2.pdf, p. 1; api.py; tortoise/models/vocoder.py).

The overall process involves the AR model generating multiple speech candidates, which are then ranked by the CLVP model. The top-ranked candidates are then processed by the diffusion decoder and finally the vocoder to produce the output audio (2305.07243v2.pdf, p. 3, 4).

### Training details:
The models were trained on a cluster of 8 NVIDIA RTX-3090 GPUs over one year (2305.07243v2.pdf, p. 4).

*   **Autoregressive Model**: Trained with a causal masking objective to predict the next token. The training prompt combines speech conditioning, text tokens, and MEL tokens. It was trained for 119M samples with a batch size of 1024. The optimizer used an AdamW-like setup with a learning rate of 1e-4, betas of (0.9, 0.96), and weight decay of 0.01, with a 500-step warmup (2305.07243v2.pdf, p. 8, 9).
*   **CLVP Model**: Trained with a contrastive loss objective on 80M samples of text and speech token pairs. The batch size was 1024. The optimizer used a learning rate of 3e-4, betas of (0.9, 0.96), weight decay of 0.001, and a 500-step warmup (2305.07243v2.pdf, p. 10).
*   **Diffusion Decoder**: Initially trained to convert discrete speech codes from a VQVAE into MEL spectrograms. It was then fine-tuned on the latent space from the autoregressive model's outputs (a technique named "The Tortoise Trick"). It was trained for 65M samples with a batch size of 512. The loss function was a combination of Mean Squared Error (MSE) and Variational Lower Bound (VLB). The optimizer used a learning rate of 1e-5, betas of (0.9, 0.999), weight decay of 0.001, and a 1000-step warmup. Classifier-free guidance was implemented by dropping conditioning signals 15% of the time during training (2305.07243v2.pdf, p. 4, 11, 12).

### Paper or other resource for more information:
The model and its development are described in the paper "Better speech synthesis through scaling" by James Betker (2305.07243v2.pdf).

The official open-source repository containing the model code and trained weights is available at: https://github.com/neonbjb/tortoise-tts (2305.07243v2.pdf, p. 1; setup.py).

### Citation details:
To cite this model, please use the following BibTeX entry:
```bibtex
@misc{betker2023better,
      title={Better speech synthesis through scaling},
      author={James Betker},
      year={2023},
      eprint={2305.07243},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```
(Source: 2305.07243v2.pdf)

### License:
The model is released under the Apache License, Version 2.0. The license permits reproduction, preparation of derivative works, public display, performance, sublicensing, and distribution of the work, subject to certain conditions. It includes a disclaimer of warranty and limitation of liability (LICENSE.txt; setup.py).

### Contact:
For questions, issues, or feedback, contact James Betker at james@adamant.ai (setup.py).

---

## Intended Use
This section outlines the intended applications of the model.

### Primary intended uses:
The primary intended use of Tortoise-TTS is as an expressive, multi-voice text-to-speech (TTS) system (2305.07243v2.pdf, p. 1). Its key capabilities include:

*   **High-Quality Speech Generation**: Generating realistic and natural-sounding speech from input text (2305.07243v2.pdf, p. 1).
*   **Voice Cloning**: Mimicking a specific voice by providing one or more reference audio clips (approximately 10 seconds each) of the target speaker. This allows the model to infer and replicate vocal characteristics like tone and prosody (2305.07243v2.pdf, p. 3, 4; api.py).
*   **Voice Combination**: Creating novel voices by combining conditioning latents from multiple speakers (tortoise_tts.ipynb.txt).
*   **Long-Form Narration**: Reading long text files by splitting them into smaller segments and synthesizing them sequentially (read.py).

The model takes a string of text and a list of voice samples (or pre-computed conditioning latents) as input. It outputs a PyTorch tensor containing the generated audio waveform at a 24kHz sampling rate (api.py).

### Primary intended users:
The model is intended for researchers, developers, and hobbyists in the field of speech synthesis. The provision of an accessible API, command-line scripts, and a Colab notebook suggests a broad audience with varying levels of technical expertise (api.py; do_tts.py; tortoise_tts.ipynb.txt).

### Out-of-scope uses:
The repository does not explicitly list out-of-scope uses. However, the voice cloning capability presents a significant risk of misuse. Potential out-of-scope and misuse cases include:

*   Creating synthetic speech to impersonate individuals without their consent.
*   Generating misinformation or "deepfakes" for malicious purposes.
*   Violating the personal rights of individuals whose voices are used for training or cloning.

Users are responsible for determining the appropriateness of using the model and assume any risks associated with its application (LICENSE.txt).

---

## How to Use
This section outlines how to use the model.

To use the model, first clone the repository and install the required dependencies:
```bash
git clone https://github.com/neonbjb/tortoise-tts.git
cd tortoise-tts
pip3 install -r requirements.txt
python3 setup.py install
```
(Source: tortoise_tts.ipynb.txt)

The primary way to use the model is through the `TextToSpeech` API. The following Python snippet demonstrates how to generate speech for a given text using a pre-packaged voice:

```python
import torchaudio
import IPython
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

# This will download all the models used by Tortoise from the HF hub.
tts = TextToSpeech()

# The text to be spoken.
text = "The expressiveness of autoregressive transformers is literally nuts! I absolutely adore them."

# Pick a voice from the 'tortoise/voices' directory.
voice = 'tom'
voice_samples, conditioning_latents = load_voice(voice)

# Select a preset for quality/speed trade-off.
# Options: {"ultra_fast", "fast", "standard", "high_quality"}
preset = "fast"

# Generate speech.
gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                          preset=preset)

# Save the generated audio.
torchaudio.save('generated.wav', gen.squeeze(0).cpu(), 24000)
IPython.display.Audio('generated.wav')
```
(Source: tortoise_tts.ipynb.txt, do_tts.py, api.py)

The model can also generate speech with a random voice or a combination of voices:
```python
# Generate with a random voice
gen = tts.tts_with_preset(text, voice_samples=None, conditioning_latents=None, preset=preset)

# Combine voices
from tortoise.utils.audio import load_voices
voice_samples, conditioning_latents = load_voices(['pat', 'william'])
gen = tts.tts_with_preset("They used to say that if man was meant to fly, he’d have wings. But he did fly. He discovered he had to.",
                          voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset)
```
(Source: tortoise_tts.ipynb.txt)

For command-line usage, you can use `do_tts.py` for single sentences or `read.py` for entire text files:
```bash
# Generate a single sentence
python3 tortoise/do_tts.py --text "I am a language model that has learned to speak." --voice pat --preset standard

# Read a text file
python3 tortoise/read.py --textfile tortoise/data/riding_hood.txt --voice train_atkins --preset ultra_fast
```
(Source: do_tts.py, read.py)

The output is a PyTorch tensor containing the audio waveform at a 24kHz sample rate (api.py).

---

## Factors
This section addresses variables that may impact the model's performance.

### Relevant factors:
*   **Reference Audio Quality**: The quality, tone, and prosody of the `voice_samples` significantly influence the generated speech, as the model uses them to infer vocal characteristics (2305.07243v2.pdf, p. 4).
*   **Generation Preset**: The choice of preset (`'ultra_fast'`, `'fast'`, `'standard'`, `'high_quality'`) directly impacts the trade-off between inference speed and output quality by controlling the number of autoregressive samples and diffusion iterations (api.py).
*   **Intelligibility vs. Diversity Slider**: The `clvp_cvvp_slider` (or `voice_diversity_intelligibility_slider`) parameter balances how closely the output follows the text versus how closely it mimics the reference voice. A value closer to 1 prioritizes text intelligibility, while a value closer to 0 prioritizes voice similarity (api.py; do_tts.py).
*   **Autoregressive and Diffusion Parameters**: Advanced users can tune various parameters like `temperature`, `top_p`, `repetition_penalty`, and `diffusion_iterations` to control the generation process (api.py).

### Evaluation factors:
*   **Hyperparameters**: The `sweep.py` script indicates that hyperparameters such as `top_p`, `temperature`, `diffusion_temperature`, and `cond_free_k` were factors considered during evaluation and tuning (sweep.py).
*   **Intelligibility**: A wav2vec model was used to characterize the "intelligibility" of speech segments (2305.07243v2.pdf, p. 5).
*   **Sample Similarity**: A CLVP-based distance metric, similar to FID for images, was used to compare the similarity between real and generated audio samples (2305.07243v2.pdf, p. 5).

---

## Metrics
This section describes how the model's performance is evaluated.

### Model performance measures:
*   **Training Loss**: The models were optimized using standard loss functions for their respective architectures. The autoregressive model used Cross-Entropy loss, the diffusion decoder used Mean Squared Error (MSE) and a Variational Lower Bound (VLB) term, and the CLVP model used a contrastive loss (2305.07243v2.pdf, p. 7, 9, 10, 12).
*   **Qualitative Evaluation**: The paper directs readers to a webpage for qualitative comparisons between samples generated by Tortoise and other TTS systems (2305.07243v2.pdf, p. 5). The `tortoise_v2_examples.html` file provides numerous audio samples for subjective evaluation.
*   **Intelligibility Score**: An open-source wav2vec model was used to measure the intelligibility of the generated speech (2305.07243v2.pdf, p. 5).
*   **Similarity Metric**: A CLVP-based distance metric was used to measure the perceptual distance between real and generated audio samples (2305.07243v2.pdf, p. 5).

### Decision thresholds:
*   During inference, the autoregressive model uses nucleus sampling with a probability (P) threshold of 0.8 (2305.07243v2.pdf, p. 4). This is implemented as `top_p=.8` in the API (api.py).

### Variation approaches:
The model employs a re-ranking process to improve output quality. It generates a large number of candidate speech clips (`num_autoregressive_samples`) from the autoregressive model. These candidates are then scored by the CLVP and CVVP models based on their correlation with the input text and reference voice. The top `k` candidates with the highest scores are selected for the final diffusion and vocoding steps (2305.07243v2.pdf, p. 4; api.py).

---

## Evaluation Data
This section provides details about the datasets used to evaluate the model.

### Datasets:
The official test split of the LibriTTS dataset was used for validation purposes during development (2305.07243v2.pdf, p. 5). A custom evaluation suite was also built to compare Tortoise against other state-of-the-art systems (2305.07243v2.pdf, p. 5). The `eval_multiple.py` script references a local dataset path that is not included in the repository, so further details are unavailable (eval_multiple.py).

### Motivation:
LibriTTS is a widely used benchmark in the TTS community, making it suitable for standardized validation (2305.07243v2.pdf, p. 5). The custom evaluation suite was created because many other high-performance TTS systems are closed-source, making direct comparison difficult (2305.07243v2.pdf, p. 5).

### Preprocessing:
Insufficient information.

---

## Training Data
This section provides details about the datasets used to train the model.

### Datasets:
The model was trained on a combination of publicly available and custom-scraped datasets:
1.  **LibriTTS**: A large corpus of English speech derived from the LibriSpeech project, containing approximately 585 hours of audio (2305.07243v2.pdf, p. 5).
2.  **HiFiTTS**: A multi-speaker English TTS dataset containing approximately 311 hours of high-quality audio (2305.07243v2.pdf, p. 5).
3.  **Extended Dataset**: A custom dataset of 49,000 hours of speech audio scraped from audiobooks and podcasts on the internet (2305.07243v2.pdf, p. 5, 6).

### Motivation:
The goal of training a large-scale generative model necessitated a very large amount of data to learn the complex distributions of speech and text (2305.07243v2.pdf, p. 5).

### Preprocessing:
The custom "Extended Dataset" underwent significant preprocessing:
*   Audio was split into clips of 5-20 seconds based on 500ms silences.
*   A pipeline of custom-trained classifiers filtered out clips containing background noise, music, poor quality (e.g., phone calls), multiple speakers, or reverb.
*   The cleaned audio was transcribed using a wav2vec2-large model that was fine-tuned to predict punctuation, which is important for generating natural-sounding speech (2305.07243v2.pdf, p. 6).

---

## Quantitative Analyses
This section presents disaggregated evaluation results.

### Unitary results:
Insufficient information.

### Intersectional results:
Insufficient information.

---

## Memory or Hardware Requirements
This section outlines the memory or hardware requirements for loading, deploying, and training the model.

### Loading Requirements:
A GPU is strongly recommended for running the model. The documentation notes that inference on a CPU can take hours for a single sentence. The `autoregressive_batch_size` parameter can be lowered to mitigate GPU Out-Of-Memory (OOM) errors, indicating significant VRAM usage (tortoise_tts.ipynb.txt; api.py). Specific memory requirements are not provided.

### Deploying Requirements:
Similar to loading requirements, a GPU is strongly recommended for deployment to achieve reasonable inference speeds (tortoise_tts.ipynb.txt).

### Training or Fine-tuning Requirements:
The models were trained from scratch on a cluster of 8 NVIDIA RTX-3090 GPUs over a period of one year (2305.07243v2.pdf, p. 4).

---

## Ethical Considerations
This section discusses the ethical considerations in model development, including challenges, risks, and solutions.

*   **Voice Cloning and Misuse**: The model's ability to clone voices from short audio clips presents a significant risk of misuse. This includes creating unauthorized voice duplicates for impersonation, fraud, or generating misinformation (deepfakes). The repository does not explicitly state these risks, but they are inherent to the technology.
*   **Data Provenance and Copyright**: The training data includes 49,000 hours of audio scraped from audiobooks and podcasts on the web (2305.07243v2.pdf, p. 5). This data may contain copyrighted material and voices of individuals who did not consent to their use in training a generative model.
*   **Detection of Synthetic Audio**: As a mitigation strategy, the repository includes a classifier model (`is_this_from_tortoise.py`) designed to detect whether an audio clip was generated by Tortoise. This tool can help identify synthetic media but may not be foolproof (is_this_from_tortoise.py).
*   **Responsibility**: The Apache 2.0 license places the responsibility for the use of the model on the end-user, disclaiming warranty and limiting liability for any damages that may arise from its use (LICENSE.txt).

---

## Caveats and Recommendations
This section lists unresolved issues and provides guidance for users.

### Caveats:
*   **Limited Sequence Length**: The autoregressive model uses fixed positional encodings, which limits the maximum length of speech it can generate in a single pass (2305.07243v2.pdf, p. 12). For long texts, the output quality may degrade or fail, and users are advised to break up their input (api.py).
*   **Re-ranking on Long Samples**: The CLVP model, used for re-ranking, was trained on audio clips of up to 13 seconds. Its performance may suffer when ranking longer speech samples (2305.07243v2.pdf, p. 12).
*   **Random Voice Quality**: Generating speech with a "random" voice can sometimes produce "strange utterances" (tortoise_tts.ipynb.txt).
*   **Architectural Limitations**: The author notes that the diffusion decoder's architecture, which omits feed-forward blocks, was a "poor design decision" that could be improved (2305.07243v2.pdf, p. 12).
*   **Mixed Sampling Rates**: The model stack operates at mixed sampling rates (22kHz for the AR model, 24kHz for the vocoder), which is suboptimal (2305.07243v2.pdf, p. 12).

### Recommendations:
*   **Use High-Quality Voice Samples**: For best results in voice cloning, use high-quality, clean audio clips of the target speaker.
*   **Segment Long Texts**: When synthesizing long passages of text, split the text into smaller chunks (e.g., by sentence or paragraph) to avoid degradation in quality. The `read.py` script provides a utility function for this (read.py).
*   **Tune Generation Parameters**: Use the provided presets for a good balance of quality and speed. For more control, experiment with the detailed parameters in the `tts()` function, such as `temperature`, `top_p`, and `diffusion_iterations` (api.py).
*   **Future Research**: The paper suggests several avenues for future work, including using relative positional encodings, training on longer audio sequences and larger batches, improving the diffusion decoder architecture, and training the entire stack at a consistent sampling rate (2305.07243v2.pdf, p. 12).

---