import base64
import json
import os
import re
from pathlib import Path

import pandas as pd
from pandas import DataFrame
from fpdf import FPDF

from util import path

# https://platform.openai.com/docs/assistants/tools/file-search
supported_document_suffixes = ['.c', '.cpp', '.css', '.csv', '.docx', '.html', '.java', '.js', '.json', '.md', '.pdf',
                               '.php', '.pptx', '.py', '.rb', '.tex', '.ts', '.txt', '.xlsx', '.xml']
# https://platform.openai.com/docs/assistants/deep-dive/creating-image-input-content
supported_image_suffixes = ['.png', '.jpg', '.jpeg', '.gif', '.webp']

gemini_unsupported_text_type_suffixes = ['.json', '.yaml', '.yml', '.in', '.ipynb', '.md', '', '.rst', '.ini']
sonnet_unsupported_text_type_suffixes = ['.json', '.yaml', '.yml', '.in', '.ini', '', '.md', '.rst', '.py', '.ipynb']

section_subsection_headers = {
    '## Model Details': [
        '### Person or organization developing model:',
        '### Model date:',
        '### Model version:',
        '### Model type:',
        '### Training details:',
        '### Paper or other resource for more information:',
        '### Citation details:',
        '### License:',
        '### Contact:'
    ],
    '## Intended Use': [
        '### Primary intended uses:',
        '### Primary intended users:',
        '### Out-of-scope uses:'
    ],
    '## How to Use': [],
    '## Factors': [
        '### Relevant factors:',
        '### Evaluation factors:'
    ],
    '## Metrics': [
        '### Model performance measures:',
        '### Decision thresholds:',
        '### Variation approaches:'
    ],
    '## Evaluation Data': [
        '### Datasets:',
        '### Motivation:',
        '### Preprocessing:'
    ],
    '## Training Data': [
        '### Datasets:',
        '### Motivation:',
        '### Preprocessing:'
    ],
    '## Quantitative Analyses': [
        '### Unitary results:',
        '### Intersectional results:'
    ],
    '## Memory or Hardware Requirements': [
        '### Loading Requirements:',
        '### Deploying Requirements:',
        '### Training or Fine-tuning Requirements:'
    ],
    '## Ethical Considerations': [],
    '## Caveats and Recommendations': [
        '### Caveats:',
        '### Recommendations:'
    ]
}


def get_repo_dir_name(model_id: str) -> str:
    return model_id.replace("/", "@")


def get_model_id(repo_dir_name: str) -> str:
    return repo_dir_name.replace("@", "/")


def get_repo_path(model_id: str) -> Path:
    return path.REPOS_DIRECTORY / get_repo_dir_name(model_id)


def get_next_iteration_no(base_dir: Path, prefix="run_") -> int:
    if not base_dir.exists():
        return 1
    pattern = re.compile(rf'^{prefix}(\d+)$')

    existing_iterations = [
        int(pattern.match(d).group(1))
        for d in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, d)) and pattern.match(d)
    ]

    next_iteration_no = max(existing_iterations, default=0) + 1
    return next_iteration_no


def get_selected_repos() -> DataFrame:
    return pd.read_csv(path.SELECTED_REPOS_FILE, dtype={"paper_id": str})


def is_image_file(file_path: Path) -> bool:
    """Return True if the file has a common image extension."""
    return file_path.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def is_json_file(file_path: Path) -> bool:
    """Return True if the file has a .json extension."""
    return file_path.suffix.lower() == ".json"


def is_txt_file(file_path: Path) -> bool:
    """Return True if the file has a .txt extension."""
    return file_path.suffix.lower() == ".txt"


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"
        "\U0001F780-\U0001F7FF"
        "\U0001F800-\U0001F8FF"
        "\U0001F900-\U0001F9FF"
        "\U0001FA00-\U0001FA6F"
        "\U0001FA70-\U0001FAFF"
        "\u2600-\u26FF"  # miscellaneous symbols
        "\u2700-\u27BF"  # dingbats
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub("", text)


def save_as_pdf(source_path, pdf_path):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=8)

    with open(source_path, "rb") as f:
        content = f.read().decode('utf-8', errors='ignore')

    content = remove_emojis(content)
    content = content.expandtabs(4)

    pdf.write(5, content)
    pdf.output(pdf_path)


def get_error_repository_ids() -> list:
    return [
        'CAMB-AI/MARS5-TTS',
        'DeepFloyd/IF-I-XL-v1.0',
        'Tencent-Hunyuan/HunyuanDiT',
        'ctheodoris/Geneformer',
        'facebook/seamless-m4t-v2-large',
        'CompVis/stable-diffusion-v1-4',
        'Crosstyan/BPModel',
        'EleutherAI/gpt-j-6b',
        'FacebookAI/roberta-large-mnli',
        'HuggingFaceM4/idefics2-8b',
        'JosephusCheung/Guanaco',
        'NousResearch/Llama-2-7b-chat-hf',
        'Qwen/Qwen2-VL-7B-Instruct',
        'SamLowe/roberta-base-go_emotions',
        'WizardLMTeam/WizardCoder-15B-V1.0',
        'amazon/MistralLite',
        'bigscience/bloom',
        'cerebras/Cerebras-GPT-13B',
        'dalle-mini/dalle-mini',
        'databricks/dolly-v2-12b',
        'distil-whisper/distil-large-v2',
        'llm-blender/PairRM',
        'microsoft/Phi-3-mini-128k-instruct',
        'openai-community/gpt2-xl',
        'stabilityai/stable-diffusion-2-1',
        'stanford-crfm/BioMedLM',
        'openai/whisper-large-v3',
        'openchat/openchat_3.5'
    ]


def get_model_file_paths() -> dict[str, list[Path]]:
    with open(path.REPO_FILES, 'r', encoding='utf-8') as file:
        repo_files = json.load(file)

    # error_repos = get_error_repository_ids()

    model_ids_file_paths = {}

    for model_id, file_paths in repo_files.items():
        # if model_id in error_repos:
        #     continue
        model_ids_file_paths[model_id] = [path.REPOS_DIRECTORY / get_repo_dir_name(model_id) / file_path for file_path
                                          in file_paths]

        paper_file_path = get_repo_paper_file(model_id)
        if paper_file_path:
            model_ids_file_paths[model_id].append(paper_file_path)

    return model_ids_file_paths


def get_repo_paper_file(model_id: str) -> Path | None:
    paper_directory = path.MODEL_PAPER_DIRECTORY / f'{get_repo_dir_name(model_id)}'
    if paper_directory.exists():
        return next(paper_directory.iterdir(), None)
    return None


def get_models_with_paper_file_paths_without_paper() -> dict[str, list[Path]]:
    model_ids_with_paper = []
    for model_paper_directory in path.MODEL_PAPER_DIRECTORY.iterdir():
        model_paper = next(model_paper_directory.iterdir(), None)

        if model_paper:
            model_id = get_model_id(model_paper_directory.name)
            print(f'Found paper for {model_id}')
            model_ids_with_paper.append(model_id)

    with open(path.REPO_FILES, 'r', encoding='utf-8') as file:
        repo_files = json.load(file)

    model_ids_file_paths = {}
    for model_id in model_ids_with_paper:
        model_repo_file_paths = repo_files[model_id]
        model_ids_file_paths[model_id] = [path.REPOS_DIRECTORY / get_repo_dir_name(model_id) / file_path for file_path
                                          in model_repo_file_paths]

    return model_ids_file_paths


def get_file_paths_for_jury() -> dict[str, list[Path]]:
    with open(path.REPO_FILES_TO_JURY, 'r', encoding='utf-8') as file:
        repos_files = json.load(file)

    model_ids_file_paths = {}

    for model_id, file_paths in repos_files.items():
        repo_file_paths = []
        repo_directory = path.REPOS_DIRECTORY / get_repo_dir_name(model_id)
        for file_path in file_paths:
            full_file_path = repo_directory / file_path
            if full_file_path.exists():
                repo_file_paths.append(full_file_path)
            else:
                paper_path = path.MODEL_PAPER_DIRECTORY / f'{get_repo_dir_name(model_id)}' / file_path
                if paper_path.exists():
                    repo_file_paths.append(paper_path)
                else:
                    print(f'File {file_path} for model {model_id} not found in repo or paper directory.')

        model_ids_file_paths[model_id] = repo_file_paths

    return model_ids_file_paths


def get_repo_files_without_config_files() -> dict[str, list[Path]]:
    with open(path.REPO_FILES, 'r', encoding='utf-8') as file:
        repo_files = json.load(file)

    with open(path.REPO_FILES_WITHOUT_CONFIG_FILES, 'r', encoding='utf-8') as file:
        repo_files_without_config_files = json.load(file)

    with open(path.CITED_REPO_FILES, 'r', encoding='utf-8') as file:
        cited_repo_files = json.load(file)

    model_ids_file_paths = {}
    repos_containing_configuration_file = []
    for model_id, cited_files in cited_repo_files.items():
        all_repo_files = set(repo_files.get(model_id, []))
        files_without_config_files = set(repo_files_without_config_files.get(model_id, []))

        config_files = all_repo_files - files_without_config_files
        if len(config_files) > 0:
            repos_containing_configuration_file.append(model_id)
        cited_config_files = [file for file in config_files if file.replace('\\', '/') in cited_files]

        if len(cited_config_files) == 0:
            print(f'No config files have been cited. ({model_id})')
        else:
            model_ids_file_paths[model_id] = [path.REPOS_DIRECTORY / get_repo_dir_name(model_id) / file_path for file_path
                                          in files_without_config_files]
            paper_file = get_repo_paper_file(model_id)
            if paper_file:
                model_ids_file_paths[model_id].append(paper_file)

    print(f'{len(repos_containing_configuration_file)} repos contain a configuration file. {len(model_ids_file_paths)} repos cite them.')
    return model_ids_file_paths


def get_repo_files_without_tokenizer_files():
    with open(path.REPO_FILES, 'r', encoding='utf-8') as file:
        repo_files = json.load(file)

    with open(path.REPO_FILES_WITHOUT_TOKENIZER_FILES, 'r', encoding='utf-8') as file:
        repo_files_without_tokenizer_files = json.load(file)

    with open(path.CITED_REPO_FILES, 'r', encoding='utf-8') as file:
        cited_repo_files = json.load(file)

    model_ids_file_paths = {}
    repos_containing_tokenizer_file = []
    for model_id, cited_files in cited_repo_files.items():
        all_repo_files = set(repo_files.get(model_id, []))
        files_without_tokenizer_files = set(repo_files_without_tokenizer_files.get(model_id, []))

        tokenizer_files = all_repo_files - files_without_tokenizer_files
        if len(tokenizer_files) > 0:
            repos_containing_tokenizer_file.append(model_id)
        cited_tokenizer_files = [file for file in tokenizer_files if file.replace('\\', '/') in cited_files]

        if len(cited_tokenizer_files) == 0:
            print(f'No tokenizer files have been cited. ({model_id})')
        else:
            model_ids_file_paths[model_id] = [path.REPOS_DIRECTORY / get_repo_dir_name(model_id) / file_path for file_path
                                          in files_without_tokenizer_files]
            paper_file = get_repo_paper_file(model_id)
            if paper_file:
                model_ids_file_paths[model_id].append(paper_file)

    print(f'{len(repos_containing_tokenizer_file)} repos contain a tokenizer file. {len(model_ids_file_paths)} repos cite them.')

    return model_ids_file_paths


if __name__ == '__main__':
    get_repo_files_without_tokenizer_files()
