from pathlib import Path
from statistics import median

from model_card_evaluator.result_viewer import plot_one_violin
from model_card_evaluator.similarity_calculator.semantic_similarity_calculator import calculate_similarity
from util import helper, path


def get_file_similarity_score(file_1: Path, file_2: Path) -> float:
    if not file_1.exists() or not file_2.exists():
        raise FileNotFoundError()

    with open(file_1, 'r', encoding='utf-8') as f:
        content1 = f.read()

    with open(file_2, 'r', encoding='utf-8') as f:
        content2 = f.read()

    return calculate_similarity(content1, content2)


def get_model_card_similarity_scores(model_ids: list[str], source_dir_1: Path, source_dir_2: Path) -> list[float]:
    similarity_scores = []
    for model_id in model_ids:
        model_card_filename = helper.get_repo_dir_name(model_id)
        model_card_1_filepath = source_dir_1 / f'{model_card_filename}.md'
        model_card_2_filepath = source_dir_2 / f'{model_card_filename}.md'

        try:
            similarity_score = get_file_similarity_score(model_card_1_filepath, model_card_2_filepath)
            print(model_id, similarity_score)

            similarity_scores.append(similarity_score)
        except FileNotFoundError as e:
            print(f'Model card not found for {model_id}')
            continue

    return  similarity_scores

def print_similarity_stats(similarity_scores: list[float]):
    average_similarity_score = sum(similarity_scores) / len(similarity_scores)
    print(f'avg: {average_similarity_score:.2f}')

    median_similarity_score = median(similarity_scores)
    print(f'med: {median_similarity_score:.2f}')

    min_similarity_score = min(similarity_scores)
    print(f'min: {min_similarity_score:.2f}')

    max_similarity_score = max(similarity_scores)
    print(f'max: {max_similarity_score:.2f}')


if __name__ == '__main__':
    selected_models = helper.get_selected_repos()
    model_ids = selected_models['model_id'].tolist()

    original_model_card_dir = path.REORGANIZED_ORIGINAL_MODEL_CARD_DIRECTORY
    generated_model_card_dir = path.GENERATED_MODEL_CARDS_DIRECTORY
    generated_model_card_without_paper_dir = path.GENERATED_MODEL_CARDS_WITHOUT_PAPER_DIRECTORY
    generated_model_card_without_config_dir = path.GENERATED_MODEL_CARDS_WITHOUT_CONFIG_DIRECTORY
    generated_model_card_without_tokenizer_dir = path.GENERATED_MODEL_CARDS_WITHOUT_TOKENIZER_DIRECTORY

    similarity_scores = get_model_card_similarity_scores(model_ids, original_model_card_dir, generated_model_card_dir)
    print_similarity_stats(similarity_scores)

    plot_one_violin(similarity_scores, 0.0, 1.0,
                    path.GRAPHS_DIRECTORY / 'distribution_of_model_card_similarity_scores.pdf')