from pathlib import Path

from api_clients.openai_chat_client import OpenAIChatClient
from util import constants


class OpenAIReasoningJsonClient(OpenAIChatClient):
    def __init__(self, model_name: str = constants.O4_MINI, api_key: str = constants.OPENAI_API_KEY,
                 base_url: str = None):
        super().__init__(model_name, api_key)
        self.base_url = base_url

    def make_request(self, instruction, prompt, file_paths: list[Path] | None, response_schema: dict | None) -> str:
        try:
            input = self.structure_messages(instruction, prompt, file_paths)
            response = self.model.responses.create(
                model=self.model_name,
                input=input,
                text={
                    'format': {
                        'type': 'json_schema',
                        'name': 'json_response',
                        'strict': True,
                        'schema': response_schema
                    }
                },
                reasoning={
                    'effort': 'high',
                },
                tools=[],
                store=True,
                max_output_tokens=20000
            )
            return response.output_text
        except Exception as e:
            raise RuntimeError(f'Error: {e}')
