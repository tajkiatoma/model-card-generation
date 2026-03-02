import re

import requests

from util import path, helper


def create_paper_directory(model_id: str, paper_id: str):
    print(model_id, paper_id)
    if paper_id != "":
        model_dir = path.MODEL_PAPER_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}'

        if model_dir.exists():
            print('Paper directory exists...')
            return

        model_dir.mkdir(parents=True)
        paper_id = paper_id.strip("'")
        if bool(re.match(r"^\d{4}\.\d{5}$", paper_id)):
            paper_url = f'https://arxiv.org/pdf/{paper_id}.pdf'
            print(f'...Downloading paper from {paper_url}')
            output_path = model_dir / f'{paper_id}.pdf'

            with requests.get(paper_url, stream=True) as r:
                r.raise_for_status()

                with open(output_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)


if __name__ == '__main__':
    selected_repos = helper.get_selected_repos()
    selected_repos['paper_id'] = selected_repos['paper_id'].fillna("")
    selected_repos.apply(lambda model: create_paper_directory(model['model_id'], model['paper_id']), axis=1)
