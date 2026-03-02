from pathlib import Path
from pprint import pprint

from model_card_evaluator.insufficient_information_section_lister import get_insufficient_information_sections_count
from model_card_evaluator.similarity_calculator.section_reader import get_section_content, get_subsection_content
from util import helper, path


def get_not_available_sections_count(source_dir: Path) -> dict:
    selected_repos = helper.get_selected_repos()
    model_ids = selected_repos['model_id'].tolist()

    not_available_sections_count = {}
    for model_id in model_ids:
        # print(f'----------------------------------------------------- {model_id}')
        reorganized_model_card_path = source_dir / f'{helper.get_repo_dir_name(model_id)}.md'

        if not reorganized_model_card_path.exists():
            print(f'File not found for {model_id}')
            continue

        with open(reorganized_model_card_path, 'r', encoding='utf-8') as file:
            reorganized_model_card = file.read()

        for i, (section_header, subsection_headers) in enumerate(helper.section_subsection_headers.items()):
            if len(subsection_headers) == 0:
                if section_header not in not_available_sections_count:
                    not_available_sections_count[section_header] = 0

                reorganized_section = get_section_content(reorganized_model_card, i)
                if 'Not available.'.lower() in reorganized_section.lower():
                    not_available_sections_count[section_header] += 1
                    # print(f'{section_header} contains insufficient information')
            else:
                for j, subsection_header in enumerate(subsection_headers):
                    key = f'{section_header}/{subsection_header}'
                    if key not in not_available_sections_count:
                        not_available_sections_count[key] = 0

                    reorganized_subsection = get_subsection_content(reorganized_model_card, i, j)
                    if 'Not available.'.lower() in reorganized_subsection.lower():
                        not_available_sections_count[key] += 1
                        # print(f'{section_header}/{subsection_header} contains insufficient information')

    # sorted_dict_desc = sorted(insufficient_info_sections.items(), key=lambda item: item[1], reverse=True)
    # pprint(sorted_dict_desc)

    return not_available_sections_count


def print_count_comparison(counts: list[dict], counts_out_of: list[int], headers: list[str]):
    print('\\begin{tabular}{@{}l' + ('r' * len(headers)) + '@{}}')
    print('\t\\toprule')
    print(f'\t\\textbf{{(Sub)sections}} & ' + ' & '.join([f'\\textbf{{{header}}}' for header in headers]) + ' \\\\')
    print('\t\midrule')
    for section in counts[0].keys():
        initial_percentage = 0
        print_stat = f'\t\t{section.replace("### ", "").replace("## ", "").replace(":", "").strip()}'
        for i, count in enumerate(counts):
            count_for_section = count[section] if section in count else 0
            space_or_not = ' ' if count_for_section <=9 else ''
            percentage = (count_for_section / counts_out_of[i]) * 100

            if i == 0:
                print_stat += f' & {percentage:.1f}\% ('+ space_or_not + f'{count_for_section})'
                initial_percentage = percentage
            else:
                diff = percentage-initial_percentage
                if diff > 0:
                    print_stat += f' & \cellcolor{{niceorange!{(diff)*2}!white}}$+$ {diff:.1f}\% ('+ space_or_not + f'{count_for_section})'
                elif diff == 0:
                    print_stat += f' & {diff:.1f}\% (' + space_or_not + f'{count_for_section})'
                else:
                    print_stat += f' & \cellcolor{{softc0!{abs(diff)*2}!white}}$-$ {abs(diff):.1f}\% ('+ space_or_not + f'{count_for_section})'
        print_stat += ' \\\\'
        print(print_stat)
    print('\t\\bottomrule')
    print('\end{tabular}')


if __name__ == '__main__':
    reorganized_model_card_dir = path.REORGANIZED_ORIGINAL_MODEL_CARD_DIRECTORY
    generated_model_card_dir = path.GENERATED_MODEL_CARDS_DIRECTORY

    # generated_model_card_without_paper_dir = path.GENERATED_MODEL_CARDS_WITHOUT_PAPER_DIRECTORY
    # generated_model_card_without_config_dir = path.GENERATED_MODEL_CARDS_WITHOUT_CONFIG_DIRECTORY
    # generated_model_card_without_tokenizer_dir = path.GENERATED_MODEL_CARDS_WITHOUT_TOKENIZER_DIRECTORY

    count1 = get_not_available_sections_count(reorganized_model_card_dir)
    count2 = get_insufficient_information_sections_count(generated_model_card_dir)

    print_count_comparison([count1, count2],
                           [len(helper.get_selected_repos()),
                            len(helper.get_selected_repos())],
                           ['Reorganized', 'Generated'])