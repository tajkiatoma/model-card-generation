import json
import os
from pathlib import Path
from pprint import pprint

from util import helper, path


def is_pointer_file(file_path: Path) -> bool:
    try:
        # Skip obviously large files — pointer files are usually < 200 bytes
        if file_path.stat().st_size > 300:
            return False

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            first_kb = file.read(1024)

            if "version https://git-lfs.github.com/spec/v1" in first_kb:
                return True
    except Exception as e:
        print(f'Error reading file {file_path}: {e}')
    return False


if __name__ == '__main__':
    repos_files = {}
    selected_repos = helper.get_selected_repos()
    model_ids = selected_repos['model_id'].values
    excluding_file_names = ['.gitattributes', '.gitignore', 'README.md', 'README_zh.md', '.DS_Store']
    excluding_file_extensions = ['.pt', '.pth', '.bin', '.safetensors', '.model', '.ckpt', '.h5', '.gguf', # model parameters or entire model files
                                 '.pkl', '.msgpack', '.ot', '.onnx', '.onnx_data', # serialized model or metadata files
                                 '.0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.v2', # sharded model files
                                 '.cff', '.css', # style files
                                 '.svg', '.gif' # gemini unsupported files
                                 ]

    file_extensions = set()

    for model_id in model_ids:
        model_dir = path.REPOS_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}'

        repo_files = []
        for file in model_dir.rglob('*'):
            if '.git' in file.parts:
                continue
            if file.is_file():
                if is_pointer_file(file):
                    continue
                if file.name in excluding_file_names:
                    continue
                if file.suffix in excluding_file_extensions:
                    continue

                repo_files.append(str(file.relative_to(model_dir)))
                file_extensions.add(file.suffix)

                # file_size_in_kb = file.stat().st_size / 1024
                # if file_size_in_kb > 2048:
                #     print(f'{model_id}: {file.relative_to(model_dir)}, {file_size_in_kb:.2f} KB')

        repos_files[model_id] = repo_files

    pprint(file_extensions)
    with open(path.REPO_FILES, 'w', encoding='utf-8') as file:
        json.dump(repos_files, file)
