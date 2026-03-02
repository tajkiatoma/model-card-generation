import statistics
from pathlib import Path

from model_card_evaluator.similarity_calculator.section_reader import get_section_content, get_subsection_content
from model_card_evaluator.similarity_calculator.semantic_similarity_calculator import calculate_similarity, \
    print_similarity_stats
from util import helper, path
from util.helper import section_subsection_headers


def get_section_similarity_scores(model_ids: list[str], source_dir_1: Path, source_dir_2: Path) -> dict:
    similarity_scores = {}
    for model_id in model_ids:
        print(f'----------------------------------------------------- {model_id}')

        model_card_filename = helper.get_repo_dir_name(model_id)
        model_card_1_filepath = source_dir_1 / f'{model_card_filename}.md'
        model_card_2_filepath = source_dir_2 / f'{model_card_filename}.md'

        if not model_card_1_filepath.exists() or not model_card_2_filepath.exists():
            print(f'File not found for {model_id}')
            continue

        with open(model_card_1_filepath, 'r', encoding='utf-8') as file:
            original_model_card = file.read()

        with open(model_card_2_filepath, 'r', encoding='utf-8') as file:
            generated_model_card = file.read()

        for i, (section_header, subsection_headers) in enumerate(section_subsection_headers.items()):
            if len(subsection_headers) == 0:
                original_section = get_section_content(original_model_card, i)
                generated_section = get_section_content(generated_model_card, i)

                similarity_score = calculate_similarity(original_section, generated_section)

                if section_header not in similarity_scores:
                    similarity_scores[section_header] = []

                similarity_scores[section_header].append(similarity_score)
                # print(f'Section: {section_header} - Similarity: {similarity_score}')
            else:
                for j, subsection_header in enumerate(subsection_headers):
                    original_subsection = get_subsection_content(original_model_card, i, j)
                    generated_subsection = get_subsection_content(generated_model_card, i, j)

                    similarity_score = calculate_similarity(original_subsection, generated_subsection)

                    if f'{section_header} / {subsection_header}' not in similarity_scores:
                        similarity_scores[f'{section_header} / {subsection_header}'] = []

                    similarity_scores[f'{section_header} / {subsection_header}'].append(similarity_score)
                    # print(f'Subsection: {section_header} / {subsection_header} - Similarity: {similarity_score}')

    return similarity_scores


def print_section_similarity_stats(section_similarity_scores: dict):
    section_stats = []
    for section_header, similarity_scores in section_similarity_scores.items():
        # print(section_header)
        # print(similarity_scores)
        # print_similarity_stats(similarity_scores)
        section_stats.append({
            'section_header': section_header,
            'average': sum(similarity_scores) / len(similarity_scores),
            'median': statistics.median(similarity_scores),
            'min': min(similarity_scores),
            'max': max(similarity_scores)
        })

    sorted_section_stats = sorted(section_stats, key=lambda x: x['average'])
    for stats in sorted_section_stats:
        print(
            f"{stats['section_header']}\t{stats['average']:.2f}\t{stats['median']:.2f}\t{stats['min']:.2f}\t{stats['max']:.2f}")


def print_overall_section_similarity_stats_as_latex(section_similarity_scores_for_types: list[dict], type_headers: list[str]):
    print('\\begin{tabular}{@{}l' + ('rr' * len(type_headers)) + '@{}}')
    print('\t\\toprule')
    type_headers_for_latex = [f'\\multicolumn{{2}}{{c}}{{\\textbf{{{header}}}}}' for header in type_headers]
    print(f'\t\\multirow{{2}}{{*}}{{\\textbf{{(Sub)sections}}}} & ' + ' & '.join(header for header in type_headers_for_latex) + r' \\')
    print('\t\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}')
    print(f'\t & ' + ' & '.join('\\textbf{{Avg}} & \\textbf{{Med}}' for _ in type_headers) + r' \\')
    print('\t\midrule')

    for section_header in section_similarity_scores_for_types[0].keys():
        display_section_name = section_header.replace("### ", "").replace("## ", "").replace(":", "").strip()
        stat_for_section = f'\t\t{display_section_name}'
        for section_scores_for_type in section_similarity_scores_for_types:
            avg_score = sum(section_scores_for_type[section_header]) / len(section_scores_for_type[section_header])
            median_score = statistics.median(section_scores_for_type[section_header])
            stat_for_section += f' & \cellcolor{{softc0!{avg_score*100:.2f}!white}}{avg_score:.2f} & \cellcolor{{softc0!{median_score*100:.2f}!white}}{median_score:.2f}'
        stat_for_section += r' \\'
        print(stat_for_section)

    print('\t\\bottomrule')
    print('\end{tabular}')


if __name__ == '__main__':
    # print_overall_section_similarity_stats_as_latex(None, ['Without Paper', 'Without Config', 'Without Tokenizer'])

    selected_models = helper.get_selected_repos()
    model_ids = selected_models['model_id'].tolist()

    # model_ids = ['BAAI/bge-m3', 'CompVis/stable-diffusion-v1-4', 'FacebookAI/roberta-large-mnli', 'MahmoodLab/UNI', 'Qwen/Qwen2-VL-7B-Instruct']

    generated_model_card_dir = path.GENERATED_MODEL_CARDS_DIRECTORY
    generated_model_card_without_paper_dir = path.GENERATED_MODEL_CARDS_WITHOUT_PAPER_DIRECTORY
    generated_model_card_without_config_dir = path.GENERATED_MODEL_CARDS_WITHOUT_CONFIG_DIRECTORY
    generated_model_card_without_tokenizer_dir = path.GENERATED_MODEL_CARDS_WITHOUT_TOKENIZER_DIRECTORY

    section_similarity_scores_for_papers = get_section_similarity_scores(model_ids, generated_model_card_dir, generated_model_card_without_paper_dir)
    section_similarity_scores_for_config = get_section_similarity_scores(model_ids, generated_model_card_dir, generated_model_card_without_config_dir)
    section_similarity_scores_for_tokenizer = get_section_similarity_scores(model_ids, generated_model_card_dir, generated_model_card_without_tokenizer_dir)
    # print_overall_section_similarity_stats_as_latex([section_similarity_scores_for_papers, section_similarity_scores_for_config, section_similarity_scores_for_tokenizer], ['w/o Paper', 'w/o Config', 'w/o Tokenizer'])

    avg_scores_paper = []
    median_scores_paper = []
    for section, section_similarity_score in section_similarity_scores_for_papers.items():
        avg_score = sum(section_similarity_score) / len(section_similarity_score)
        avg_scores_paper.append(avg_score)

        median_score = statistics.median(section_similarity_score)
        median_scores_paper.append(median_score)

        # print(section, avg_score, median_score)

    # print(avg_scores_paper)
    # print(f'Avg: {sum(avg_scores_paper)/len(avg_scores_paper):.2f}')
    # print(f'Med: {statistics.median(avg_scores_paper):.2f}')
    #
    # print(median_scores_paper)
    # print(f'Avg: {sum(median_scores_paper)/len(median_scores_paper):.2f}')
    # print(f'Med: {statistics.median(median_scores_paper):.2f}')

    avg_scores_config = []
    median_scores_config = []
    for section, section_similarity_score in section_similarity_scores_for_config.items():
        avg_scores_config.append(sum(section_similarity_score) / len(section_similarity_score))
        median_scores_config.append(statistics.median(section_similarity_score))

    print(avg_scores_config)
    print(f'Avg: {sum(avg_scores_config) / len(avg_scores_config):.2f}')
    print(f'Med: {statistics.median(avg_scores_config):.2f}')

    print(median_scores_config)
    print(f'Avg: {sum(median_scores_config) / len(median_scores_config):.2f}')
    print(f'Med: {statistics.median(median_scores_config):.2f}')

    avg_scores_tokenizer = []
    median_scores_tokenizer = []
    for section, section_similarity_score in section_similarity_scores_for_tokenizer.items():
        avg_scores_tokenizer.append(sum(section_similarity_score) / len(section_similarity_score))
        median_scores_tokenizer.append(statistics.median(section_similarity_score))

    print(avg_scores_tokenizer)
    print(f'Avg: {sum(avg_scores_tokenizer) / len(avg_scores_tokenizer):.2f}')
    print(f'Med: {statistics.median(avg_scores_tokenizer):.2f}')

    print(median_scores_tokenizer)
    print(f'Avg: {sum(median_scores_tokenizer) / len(median_scores_tokenizer):.2f}')
    print(f'Med: {statistics.median(median_scores_tokenizer):.2f}')

    print('\\midrule')
    print(f'\\multirow{{2}}{{*}}{{\\textbf{{Across all (sub)sections}}}} & \\textbf{{Avg: {sum(avg_scores_paper)/len(avg_scores_paper):.2f}}} & \\textbf{{Avg: {sum(median_scores_paper)/len(median_scores_paper):.2f}}} & \\textbf{{Avg: {sum(avg_scores_config)/len(avg_scores_config):.2f}}} & \\textbf{{Avg: {sum(median_scores_config)/len(median_scores_config):.2f}}} & \\textbf{{Avg: {sum(avg_scores_tokenizer)/len(avg_scores_tokenizer):.2f}}} & \\textbf{{Avg: {sum(median_scores_tokenizer)/len(median_scores_tokenizer):.2f}}} \\\\')
    print(f' & \\textbf{{Med: {statistics.median(avg_scores_paper):.2f}}} & \\textbf{{Med: {statistics.median(median_scores_paper):.2f}}} & \\textbf{{Med: {statistics.median(avg_scores_config):.2f}}} & \\textbf{{Med: {statistics.median(median_scores_config):.2f}}}  & \\textbf{{Med: {statistics.median(avg_scores_tokenizer):.2f}}} & \\textbf{{Med: {statistics.median(median_scores_tokenizer):.2f}}} \\\\')