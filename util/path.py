from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


DATA_DIRECTORY = get_project_root() / 'data'
REPOS_DIRECTORY = DATA_DIRECTORY / 'repos'
MODEL_PAPER_DIRECTORY = DATA_DIRECTORY / 'papers'
GRAPHS_DIRECTORY = DATA_DIRECTORY / 'graphs'

REORGANIZED_ORIGINAL_MODEL_CARD_DIRECTORY = DATA_DIRECTORY / 'reorganized_original_model_cards'

MODEL_CARD_GENERATOR_DIRECTORY = get_project_root() / 'model_card_generator'

SELECTED_REPOS_FILE = DATA_DIRECTORY / 'selected_repos.csv'
REPO_FILES = DATA_DIRECTORY / 'repo_files.json'
CITED_REPO_FILES = DATA_DIRECTORY / 'cited_repo_files.json'
REPO_FILES_TO_JURY = DATA_DIRECTORY / 'repo_files_to_jury.json'
REPO_FILES_WITHOUT_CONFIG_FILES = DATA_DIRECTORY / 'repo_files_without_configuration_files.json'
REPO_FILES_WITHOUT_TOKENIZER_FILES = DATA_DIRECTORY / 'repo_files_without_tokenizer_files.json'
CONFLICT_REPOS_LIST_FILE = DATA_DIRECTORY / 'conflict_repos.json'
AGREED_INCORRECT_SECTIONS_FILE = DATA_DIRECTORY / 'agreed_incorrect_sections.json'
GENERATED_MODEL_CARDS_DIRECTORY = DATA_DIRECTORY / 'generated_model_cards' / 'run_1'
GENERATED_MODEL_CARDS_WITHOUT_PAPER_DIRECTORY = DATA_DIRECTORY / 'generated_model_cards_without_paper' / 'run_1'
GENERATED_MODEL_CARDS_WITHOUT_CONFIG_DIRECTORY = DATA_DIRECTORY / 'generated_model_cards_without_config' / 'run_1'
GENERATED_MODEL_CARDS_WITHOUT_TOKENIZER_DIRECTORY = DATA_DIRECTORY / 'generated_model_cards_without_tokenizer' / 'run_1'
GENERATED_MODEL_CARD_CHECKLISTS_DIRECTORY = DATA_DIRECTORY / 'generated_model_card_checklists'

LLM_JURY_RESULT_DIRECTORY = DATA_DIRECTORY / 'llm_jury_results'

SECTION_NAMES_FILE = DATA_DIRECTORY.parent / 'util' / 'section_names.json'