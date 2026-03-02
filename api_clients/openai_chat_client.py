from pathlib import Path

from openai import OpenAI

from api_clients.llm_base_client import LLMBaseClient
from util import constants, helper, path


class OpenAIChatClient(LLMBaseClient):
    def __init__(self, model_name: str = constants.GPT_4O_MINI, api_key: str = constants.OPENAI_API_KEY,
                 base_url: str = None):
        super().__init__(model_name, api_key)
        self.base_url = base_url

    def setup_model(self, instruction: str | None, response_schema: dict | None) -> None:
        if self.base_url is not None:
            self.model = OpenAI(base_url=self.base_url, api_key=self.api_key)
        else:
            self.model = OpenAI(api_key=self.api_key)

    def structure_messages(self, instruction, prompt, file_paths: list[Path] | None):
        files = []
        if file_paths:
            for file_path in file_paths:
                if file_path.is_relative_to(path.REPOS_DIRECTORY):
                    model_dir = file_path.relative_to(path.REPOS_DIRECTORY)
                else:
                    model_dir = file_path.relative_to(path.MODEL_PAPER_DIRECTORY)
                display_name = str(Path(*model_dir.parts[1:])).replace('\\', '/')

                if helper.is_image_file(file_path):
                    with open(file_path, 'rb') as file:
                        uploaded = self.model.files.create(file=file, purpose='vision')
                        files.append({'type': 'input_image', 'file_id': uploaded.id, 'display_name': display_name})
                elif file_path.suffix in helper.gemini_unsupported_text_type_suffixes + ['.py', '.txt', '.html']:
                    pdf_file = file_path.with_name(file_path.name + '.pdf')
                    if not pdf_file.exists():
                        helper.save_as_pdf(file_path, pdf_file)

                    with open(pdf_file, 'rb') as file:
                        uploaded = self.model.files.create(file=file, purpose='user_data')
                        files.append({'type': 'input_file', 'file_id': uploaded.id, 'display_name': display_name})
                else:
                    with open(file_path, 'rb') as file:
                        uploaded = self.model.files.create(file=file, purpose='user_data')
                        files.append({'type': 'input_file', 'file_id': uploaded.id, 'display_name': display_name})

        messages = []
        if instruction not in [None, '']:
            messages.append({
                'role': 'developer',
                'content': [
                    {
                        'type': 'input_text',
                        'text': instruction
                    }
                ]
            })

        prompt_with_file_names = prompt + '\n' + '\n'.join([f'\"{file["display_name"]}\"' for file in files]) + '\n'

        input_items = []
        if prompt not in [None, '']:
            input_items.append({'type': 'input_text', 'text': prompt_with_file_names})

        for file in files:
            input_items.append({'type': file['type'], 'file_id': file['file_id']})

        if input_items:
            messages.append({
                'role': 'user',
                'content': input_items
            })
        return messages

    def make_request(self, instruction, prompt, file_paths: list[Path] | None, response_schema: dict | None) -> str:
        try:
            response = self.model.chat.completions.create(
                model=self.model_name,
                messages=self.structure_messages(instruction, prompt, file_paths),
                temperature=0.0
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f'Error: {e}')
