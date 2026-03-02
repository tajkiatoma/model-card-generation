from util import path, helper
from util.helper import section_subsection_headers


def get_section_content(model_card_content: str, section_index: int) -> str:
    section_headers = list(section_subsection_headers.keys())
    section_header = section_headers[section_index]
    next_section_header = section_headers[section_index + 1] if section_index + 1 < len(
        section_headers) else '---'

    start_index = model_card_content.find(section_header)
    if start_index != -1:
        end_index = model_card_content.find(next_section_header, start_index + len(section_header))
        if end_index != -1:
            return model_card_content[start_index:end_index].strip()
        elif end_index == -1 and next_section_header != '---':
            next_subsection_headers = section_subsection_headers[next_section_header]
            if next_subsection_headers:
                next_subsection_header = next_subsection_headers[0]
                end_index = model_card_content.find(next_subsection_header, start_index + len(section_header))
                if end_index != -1:
                    return model_card_content[start_index:end_index].strip()
        return model_card_content[start_index:].strip()
    else:
        subsection_headers = section_subsection_headers[section_header]
        if subsection_headers:
            subsection_header = subsection_headers[0]
            start_index = model_card_content.find(subsection_header)
            if start_index != -1:
                end_index = model_card_content.find(next_section_header, start_index + len(subsection_header))
                if end_index != -1:
                    return model_card_content[start_index:end_index].strip()
                return model_card_content[start_index:].strip()
        return ''


def get_subsection_content(model_card_content: str, section_index: int, subsection_index: int) -> str:
    section_content = get_section_content(model_card_content, section_index)

    section_headers = list(section_subsection_headers.keys())
    section_header = section_headers[section_index]
    subsection_headers = section_subsection_headers[section_header]

    if len(subsection_headers) == 0:
        subsection_header = section_header
        next_subsection_header = '---'
    else:
        subsection_header = subsection_headers[subsection_index]
        next_subsection_header = subsection_headers[subsection_index + 1] if subsection_index + 1 < len(
            subsection_headers) else '---'

    start_index = section_content.find(subsection_header)
    if start_index != -1:
        end_index = section_content.find(next_subsection_header, start_index + len(subsection_header))
        if end_index != -1:
            return section_content[start_index:end_index].strip()
        return section_content[start_index:].strip()
    return ''


if __name__ == '__main__':
    model_id = 'ai21labs/AI21-Jamba-1.5-Mini'
    run_no = 14

    generated_model_card_path = path.GENERATED_MODEL_CARDS_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}.md'
    with open(generated_model_card_path, 'r', encoding='utf-8') as file:
        generated_model_card = file.read()

    for i, (section_header, subsection_headers) in enumerate(section_subsection_headers.items()):
        section_content = get_section_content(generated_model_card, i)
        print(f'Section content for header "{section_header}"\n{section_content}')

        for j, subsection_header in enumerate(subsection_headers):
            subsection_content = get_subsection_content(generated_model_card, i, j)
            print(f'Subsection content for header "{subsection_header}"\n{subsection_content}')

        print('---')