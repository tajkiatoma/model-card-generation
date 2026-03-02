import json

from util import helper, path

def list_cited_files():
    with open(path.REPO_FILES, 'r', encoding='utf-8') as file:
        repos_files = json.load(file)

    repos_cited_files = {}

    selected_repos = helper.get_selected_repos()
    model_ids = selected_repos['model_id'].tolist()

    for model_id in model_ids:
        print(f'---------------------------------------------------{model_id}')

        model_paper = helper.get_repo_paper_file(model_id)
        repo_files = ([model_paper.name] + repos_files[model_id]) if model_paper else repos_files[model_id]

        generated_model_card_path = path.GENERATED_MODEL_CARDS_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}.md'
        with open(generated_model_card_path, 'r', encoding='utf-8') as f:
            generated_model_card = f.read().strip()

        repos_cited_files[model_id] = []
        for file_name in repo_files:
            display_name = file_name.replace('\\', '/')
            if display_name in generated_model_card:
                print(f'----- CITED {display_name}')

                start = 0
                while True:
                    name_index = generated_model_card.find(display_name, start)
                    if name_index == -1:
                        break

                    last_opening_parenthesis_index = generated_model_card.rfind('(', 0, name_index)
                    next_closing_parenthesis_index = generated_model_card.find(')', name_index)

                    if last_opening_parenthesis_index != -1 and next_closing_parenthesis_index != -1:
                        citation_text = generated_model_card[last_opening_parenthesis_index:next_closing_parenthesis_index+1]
                        print(citation_text)
                    start = name_index + len(display_name)

                repos_cited_files[model_id].append(display_name)


        print(f'Total files in repo: {len(repo_files)}')
        print(f'Cited files count: {len(repos_cited_files[model_id])}')

    with open(path.CITED_REPO_FILES, 'w', encoding='utf-8') as file:
        json.dump(repos_cited_files, file, indent=4)


def get_cited_file_extensions():
    with open(path.CITED_REPO_FILES, 'r', encoding='utf-8') as file:
        cited_repo_files = json.load(file)

    file_extensions = set()
    for model_id, cited_files in cited_repo_files.items():
        for file_name in cited_files:
            if '.' in file_name:
                extension = file_name.split('.')[-1]
                file_extensions.add(extension)

    print('Cited file extensions:')
    for ext in sorted(file_extensions):
        print(ext)

    return file_extensions


if __name__ == '__main__':
    get_cited_file_extensions()