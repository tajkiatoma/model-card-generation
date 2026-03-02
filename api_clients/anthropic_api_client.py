import imghdr
import shutil
from pathlib import Path

import anthropic

from api_clients.llm_base_client import LLMBaseClient
from util import constants, helper, path


class AnthropicAPIClient(LLMBaseClient):
    def __init__(self, model_name: str = constants.CLAUDE_SONNET_4_5, api_key: str = constants.ANTHROPIC_API_KEY):
        super().__init__(model_name, api_key)

    def setup_model(self, instruction: str | None, response_schema: dict | None = None):
        self.model = anthropic.Anthropic(api_key=self.api_key)

    def structure_messages(self, instruction, prompt, file_paths: list[Path] | None):
        unsupported_files = [p for p in file_paths if
                                 p.suffix.lower() in helper.sonnet_unsupported_text_type_suffixes]
        if unsupported_files:
            for unsupported_file in unsupported_files:
                txt_file = unsupported_file.with_name(unsupported_file.name + ".txt")
                file_paths = [file_path if file_path != unsupported_file else txt_file for file_path in file_paths]

                if txt_file.exists():
                    continue
                shutil.copy(unsupported_file, txt_file)

            print(f'Converted {len(unsupported_files)} unsupported files to text files')

        files = []
        for file_path in file_paths or []:
            try:
                if file_path.is_relative_to(path.REPOS_DIRECTORY):
                    model_dir = file_path.relative_to(path.REPOS_DIRECTORY)
                else:
                    model_dir = file_path.relative_to(path.MODEL_PAPER_DIRECTORY)
                display_name = str(Path(*model_dir.parts[1:])).replace('\\', '/')

                if file_path.suffix.lower() in helper.sonnet_unsupported_text_type_suffixes + ['.txt']:
                    content_type = 'document'
                    mime_type = 'text/plain'
                elif file_path.suffix.lower() == '.pdf':
                    content_type = 'document'
                    mime_type = 'application/pdf'
                else:
                    content_type = 'image'
                    file_type = '.' + imghdr.what(file_path)

                    if file_type != file_path.suffix.lower():
                        print(f'Warning: file type {file_type} does not match file suffix {file_path.suffix} for file {file_path.name}')

                    mime_type = constants.MIME_TYPE_MAPPER[file_type]
                uploaded_file = self.model.beta.files.upload(
                        file=(file_path.name, open(file_path, 'rb'), mime_type))
                files.append({
                    'id': uploaded_file.id,
                    'display_name': display_name,
                    'content_type': content_type
                })
            except Exception as e:
                print(f'Error uploading file {file_path}: {e}')

        contents = []

        prompt_with_file_names = prompt + '\n' + '\n'.join([f'\"{file["display_name"]}\"' for file in files]) + '\n'
        contents.append(
            {
                "type": "text",
                "text": prompt_with_file_names
            }
        )

        for file in files:
            contents.append(
                {
                    "type": file["content_type"],
                    "source": {
                        "type": "file",
                        "file_id": file["id"]
                    }
                }
            )
        return [
            {
                "role": "user",
                "content": contents
            }
        ]

    def make_request(self, instruction: str | None, prompt: str, file_paths: list[Path] | None,
                     response_schema: dict | None) -> str:
        structured_messages = self.structure_messages(instruction, prompt, file_paths)
        response = self.model.beta.messages.create(
            model=self.model_name,
            max_tokens=20000,
            temperature=0.0,
            system=instruction,
            messages=structured_messages,
            betas = ["files-api-2025-04-14"], # add "context-1m-2025-08-07" to run with 1M tokens
        )
        return response.content[0].text
