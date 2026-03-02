from pathlib import Path

from api_clients.openai_chat_client import OpenAIChatClient
from util import constants


class OpenAIChatJsonClient(OpenAIChatClient):
    def __init__(self, model_name: str = constants.GPT_4O_MINI, api_key: str = constants.OPENAI_API_KEY,
                 base_url: str = None):
        super().__init__(model_name, api_key)
        self.base_url = base_url

    def make_request(self, instruction, prompt, file_paths: list[Path] | None, response_schema: dict | None) -> str:
        try:
            response = self.model.chat.completions.create(
                model=self.model_name,
                messages=self.structure_messages(instruction, prompt, file_paths),
                temperature=0.0,
                response_format={
                    'type': 'json_object',
                }
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f'Error: {e}')
