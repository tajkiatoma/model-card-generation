import json
from statistics import median

from model_card_evaluator.result_viewer import plot_one_violin
from util import path, helper


def get_section_results(model_id: str, jury_dir_name: str, run_no: int):
    jury_result_file_path = path.LLM_JURY_RESULT_DIRECTORY / jury_dir_name / f'run_{run_no}' / f'{helper.get_repo_dir_name(model_id)}.json'

    if not jury_result_file_path.exists():
        return None

    try:
        with open(jury_result_file_path, 'r', encoding='utf-8') as file:
            jury_result = json.load(file)
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON for {model_id} in {jury_dir_name} run {run_no}: {e}')
        return None

    if 'sections' in jury_result:
        return jury_result['sections']

    return jury_result


def has_result_conflict(model_id, jury_1_results, jury_2_results) -> bool:
    has_conflict = False
    with open(path.SECTION_NAMES_FILE, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        section_names = json_data['section_names']

    for section_name in section_names:
        result_1 = next((item for item in jury_1_results if item.get("section_name") == section_name), None)
        result_2 = next((item for item in jury_2_results if item.get("section_name") == section_name), None)

        if result_1 is None or result_2 is None:
            print(f'Check {section_name} manually for {model_id}')

        if result_1['is_correct'] != result_2['is_correct']:
            return True
            # print(model_id, section_name)
            # if 'incorrect_information' in result_1:
            #     pprint(f'Jury 1: {result_1["incorrect_information"]}')
            # if 'incorrect_information' in result_2:
            #     pprint(f'Jury 2: {result_2["incorrect_information"]}')

    return has_conflict


def has_any_incorrect_section(jury_result) -> bool:
    if jury_result is None:
        return False
    for section_result in jury_result:
        if not section_result.get('is_correct', True):
            return True
    return False


def write_conflict_repos(model_ids: list[str]):
    conflict_repos = []
    for model_id in model_ids:
        gemini_jury_result = get_section_results(model_id, 'gemini_2_5_pro_preview', 1)
        sonnet_jury_result = get_section_results(model_id, 'sonnet_4_5', 2)

        if gemini_jury_result is None or sonnet_jury_result is None:
            continue

        if has_result_conflict(model_id, gemini_jury_result, sonnet_jury_result):
            conflict_repos.append(model_id)
            print(model_id)

    print(f'Total conflicts: {len(conflict_repos)}')
    with open(path.CONFLICT_REPOS_LIST_FILE, 'w', encoding='utf-8') as file:
        json.dump(conflict_repos, file, indent=4)


def write_agreed_incorrect_sections(model_ids: list[str] = None):
    agreed_incorrect_sections = {}

    for model_id in model_ids:
        print(f'------------------------------------------{model_id}')
        gemini_jury_result = get_section_results(model_id, 'gemini_2_5_pro_preview', 1)
        sonnet_jury_result = get_section_results(model_id, 'sonnet_4_5', 2)
        gpt_jury_result = get_section_results(model_id, 'gpt_5', 2)

        incorrect_sections = []
        for gemini_section in gemini_jury_result:
            section_name = gemini_section.get("section_name")
            disagreed = False
            sonnet_section = next((item for item in sonnet_jury_result if item.get("section_name") == section_name), None)

            is_section_correct_in_gemini = gemini_section.get('is_correct', True)
            is_section_correct_in_sonnet = sonnet_section.get('is_correct', True)

            if is_section_correct_in_gemini and is_section_correct_in_sonnet:
                continue
            elif is_section_correct_in_gemini != is_section_correct_in_sonnet:
                disagreed = True
            elif not is_section_correct_in_gemini and not is_section_correct_in_sonnet:
                print(f'{model_id}: {section_name}')
                print('Gemini: ', gemini_section.get('incorrect_information', ''))
                print('Sonnet: ', sonnet_section.get('incorrect_information', ''))

                incorrect_sections.append({
                    'section_name': section_name,
                    'gemini_incorrect_information': gemini_section.get('incorrect_information', ''),
                    'sonnet_incorrect_information': sonnet_section.get('incorrect_information', ''),
                    'category': None
                })

            if disagreed and gpt_jury_result:
                gpt_section = next((item for item in gpt_jury_result if item.get("section_name") == section_name), None)
                is_section_correct_in_gpt = gpt_section.get('is_correct', True)

                if not is_section_correct_in_gpt:
                    print(f'{model_id}: {section_name}')
                    if not is_section_correct_in_gemini:
                        print('Gemini: ', gemini_section.get('incorrect_information', ''))
                        jury_1_name = 'gemini_incorrect_information'
                        incorrect_information = gemini_section.get('incorrect_information', '')
                    else:
                        print('Sonnet: ', sonnet_section.get('incorrect_information', ''))
                        jury_1_name = 'sonnet_incorrect_information'
                        incorrect_information = sonnet_section.get('incorrect_information', '')

                    print('GPT-5: ', gpt_section.get('incorrect_information', ''))

                    incorrect_sections.append({
                        'section_name': section_name,
                        jury_1_name: incorrect_information,
                        'gpt_incorrect_information': gpt_section.get('incorrect_information', ''),
                        'category': None
                    })

        if incorrect_sections:
            agreed_incorrect_sections[model_id] = incorrect_sections

    with open(path.AGREED_INCORRECT_SECTIONS_FILE, 'w', encoding='utf-8') as file:
        json.dump(agreed_incorrect_sections, file, indent=4)

    no_of_incorrect_sections_per_model_card = []
    for model_id, sections in agreed_incorrect_sections.items():
        no_of_incorrect_sections_per_model_card.append(len(sections))

    no_of_correct_model_cards = len(model_ids) - len(agreed_incorrect_sections)
    avg_no_of_incorrect_sections = sum(no_of_incorrect_sections_per_model_card) / len(
        no_of_incorrect_sections_per_model_card) if no_of_incorrect_sections_per_model_card else 0
    median_no_of_incorrect_sections = median(no_of_incorrect_sections_per_model_card) if no_of_incorrect_sections_per_model_card else 0
    no_of_total_sections_per_model_card = 34
    print(
        f'{no_of_correct_model_cards} ({(no_of_correct_model_cards / len(model_ids) * 100):.2f}\%) model cards have all the correct sections based on the jury result. '
        f'From~\\autoref{{fig:distribution_of_no_of_incorrect_sections}}, we can see that the average number of incorrect sections in the rest of the {len(model_ids) - no_of_correct_model_cards} model cards is '
        f'{avg_no_of_incorrect_sections:.2f} ({((avg_no_of_incorrect_sections / no_of_total_sections_per_model_card) * 100):.2f}\% of the total number of sections in a model card), '
        f'with a median of {median_no_of_incorrect_sections} and ranging from {min(no_of_incorrect_sections_per_model_card)} to {max(no_of_incorrect_sections_per_model_card)}.')

    # f'Number of Incorrect Sections per {len(model_ids) - no_of_correct_model_cards} Incorrect Model Card'
    plot_one_violin(no_of_incorrect_sections_per_model_card, 1, no_of_total_sections_per_model_card, path.GRAPHS_DIRECTORY / 'distribution_of_no_of_incorrect_sections.pdf')


if __name__ == '__main__':
    selected_repos = helper.get_selected_repos()
    model_ids = selected_repos['model_id'].values

    write_agreed_incorrect_sections(model_ids)