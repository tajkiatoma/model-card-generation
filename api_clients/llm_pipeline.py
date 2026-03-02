from abc import ABC, abstractmethod
from pathlib import Path

from api_clients.llm_base_client import LLMBaseClient


class LLMPipeline(ABC):
    def __init__(self, instruction_path: Path | None, response_schema: dict | None, llm_client: LLMBaseClient):
        self.instruction_path = instruction_path
        self.response_schema = response_schema
        self.llm_client = llm_client

    def get_instruction(self) -> str | None:
        if self.instruction_path:
            with open(self.instruction_path, 'r', encoding='utf-8') as instruction_file:
                return instruction_file.read()
        return None

    @abstractmethod
    def get_prompt(self, id: str) -> str:
        pass

    @abstractmethod
    def get_save_path(self, id: str, next_iteration_no: int = None) -> Path:
        pass

    @staticmethod
    def save_response(response: str, filepath: Path):
        if response.startswith('```markdown') and response.endswith('```'):
            response = response[12:-3]
        elif response.startswith('```json') and response.endswith('```'):
            response = response[8:-3]
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response)

    def process_single_request(self, id: str, file_paths: list[Path] = None, iteration_no: int = None):
        instruction = self.get_instruction()
        self.llm_client.setup_model(instruction, self.response_schema)

        print(f'Requesting to {self.llm_client.model_name} for {id}')
        response = self.llm_client.make_request(instruction, self.get_prompt(id), file_paths, self.response_schema)
        filepath = self.get_save_path(id, iteration_no)
        if filepath.exists():
            return
        self.save_response(response, filepath)

    def process_batch_request(self, ids: list[str], iteration_no: int = None):
        instruction = self.get_instruction()
        self.llm_client.setup_model(instruction, self.response_schema)

        prompts = {id: self.get_prompt(id) for id in ids}
        save_paths = {id: self.get_save_path(id, iteration_no) for id in
                      ids}  # generate filepaths beforehand to calculate next iteration number correctly

        for id in ids:
            if save_paths[id].exists():
                continue
            print(f'Requesting to {self.llm_client.model_name} for {id}')
            try:
                response = self.llm_client.make_request(instruction, prompts[id], None, self.response_schema)
                self.save_response(response, save_paths[id])
            except Exception as e:
                print(f'Error processing {id}: {e}')
                continue

    # ids is a dict of id to list of file paths
    def process_batch_request_with_files(self, ids: dict[str, list[Path]], iteration_no: int = None):
        instruction = self.get_instruction()
        self.llm_client.setup_model(instruction, self.response_schema)

        prompts = {id: self.get_prompt(id) for id in ids.keys()}
        save_paths = {id: self.get_save_path(id, iteration_no) for id in
                      ids}  # generate filepaths beforehand to calculate next iteration number correctly

        for id, file_paths in ids.items():
            if save_paths[id].exists():
                print(f'{save_paths[id].name} already exists, skipping...')
                continue

            print(f'Requesting to {self.llm_client.model_name} for {id} with {len(file_paths)} files')
            try:
                response = self.llm_client.make_request(instruction, prompts[id], file_paths, self.response_schema)
                self.save_response(response, save_paths[id])
            except Exception as e:
                print(f'Error processing {id}: {e}')
                continue