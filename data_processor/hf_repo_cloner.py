import pandas as pd
from huggingface_hub import Repository
from huggingface_hub.utils import GatedRepoError, RepositoryNotFoundError
from tqdm import tqdm

from util import constants, helper


def clone_repo(model_id: str, sha: str):
    print(f'Cloning {model_id}...')
    clone_to = helper.get_repo_path(model_id)
    if clone_to.exists():
        print(f'Repository already exists: {model_id}')
        return
    try:
        Repository(local_dir=clone_to, clone_from=model_id, token=constants.HF_ACCESS_TOKEN, revision=sha, skip_lfs_files=True)
    except GatedRepoError:
        print(f'GatedRepoError: {model_id}')
    except RepositoryNotFoundError:
        print(f'RepositoryNotFoundError: {model_id}')


if __name__ == '__main__':
    selected_repos = helper.get_selected_repos()
    model_id_sha = selected_repos[['model_id', 'sha']]
    # model_ids = pd.Series(['BAAI/bge-m3', 'CompVis/stable-diffusion-v1-4', 'FacebookAI/roberta-large-mnli', 'MahmoodLab/UNI', 'Qwen/Qwen2-VL-7B-Instruct'])
    tqdm.pandas()
    model_id_sha.progress_apply(lambda row: clone_repo(row['model_id'], row['sha']), axis=1)
