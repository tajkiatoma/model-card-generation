import shutil
from pathlib import Path

from google import genai
from google.genai import types

from util import helper, path, constants


def delete_generated_files():
    model_ids_file_paths = helper.get_model_file_paths()

    for model_id, file_paths in model_ids_file_paths.items():
        for file_path in file_paths:
            txt_file = file_path.with_name(file_path.name + ".txt")
            if txt_file.exists():
                txt_file.unlink()

            pdf_file = file_path.with_name(file_path.name + '.pdf')
            if pdf_file.exists():
                pdf_file.unlink()

        repo_directory = path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id)
        summary_file_path = repo_directory / "tokenizer_summary.json"

        if summary_file_path.exists():
            summary_file_path.unlink()


def copy_original_model_cards():
    selected_repos = helper.get_selected_repos()
    model_ids = selected_repos['model_id'].values

    for model_id in model_ids:
        source_path = path.DATA_DIRECTORY.parent.parent / 'auto-model-card-generation' / 'data' / 'publish' / f'{helper.get_repo_dir_name(model_id)}' / '8_manually_added_missing_information.md'
        destination_path = path.REORGANIZED_ORIGINAL_MODEL_CARD_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}.md'

        if destination_path.exists():
            continue

        shutil.copy(source_path, destination_path)


def upload_file(file_path: Path):
    client = genai.Client(api_key=constants.GEMINI_API_KEY)
    uploaded_file = client.files.upload(file=file_path, config=types.UploadFileConfig(mime_type='text/x-rst'))
    print(uploaded_file)


if __name__ == '__main__':
    # file = path.REPOS_DIRECTORY / 'ctheodoris@Geneformer' / 'docs'/ 'source'/ 'about.rst'
    # upload_file(file)

    id_paths = helper.get_models_with_paper_file_paths_without_paper()
    print(len(id_paths))