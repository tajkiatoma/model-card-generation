import json
import shutil
from pathlib import Path

from google import genai
from google.genai import types

from api_clients.llm_base_client import LLMBaseClient
from util import constants, helper, path


class GenAIClient(LLMBaseClient):
    def __init__(self, model_name: str = constants.GEMINI_2_5_PRO_STABLE, api_key: str = constants.GEMINI_API_KEY):
        super().__init__(model_name, api_key)

    def setup_model(self, instruction: str | None, response_schema: dict | None = None):
        self.model = genai.Client(api_key=self.api_key)

    def structure_messages(self, instruction, prompt, file_paths: list[Path] | None):
        unsupported_files = [p for p in file_paths if p.suffix.lower() in helper.gemini_unsupported_text_type_suffixes]

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

                if file_path.suffix == '.webp':
                    uploaded_file = self.model.files.upload(file=file_path,
                                                            config=types.UploadFileConfig(display_name=display_name,
                                                                                          mime_type='image/webp'))
                else:
                    uploaded_file = self.model.files.upload(file=file_path,
                                                            config=types.UploadFileConfig(display_name=display_name))
                files.append(uploaded_file)
            except Exception as e:
                print(f'Error uploading file {file_path}: {e}')

        prompt_with_file_names = prompt + '\n' + '\n'.join([f'"{file.display_name}"' for file in files]) + '\n'

        return ([prompt_with_file_names] + files) if files else prompt

    def make_request(self, instruction: str | None, prompt: str, file_paths: list[Path] | None,
                     response_schema: dict | None) -> str:
        contents = self.structure_messages(instruction, prompt, file_paths)
        response = self.model.models.generate_content(
            model=self.model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=instruction,
                temperature=0.0,
                max_output_tokens=65536,
                top_p=0.95,
                top_k=64,
                response_mime_type='text/plain' if response_schema is None else 'application/json',
                response_schema=response_schema
            )
        )

        return response.text
