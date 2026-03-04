from pathlib import Path

from api_clients.genai_client import GenAIClient
from api_clients.llm_pipeline import LLMPipeline
from util import constants, path, helper


class ModelCardGenerator(LLMPipeline):
    def get_instruction(self) -> str | None:
        with open('reorganization_template_with_instruction.md', "r") as file:
            model_card_template = file.read()
        if self.instruction_path:
            with open(self.instruction_path, 'r', encoding='utf-8') as instruction_file:
                return instruction_file.read() + '\n"""\n' + model_card_template + '"""'
        return None

    def get_prompt(self, model_id: str) -> str:
        with open('prompt.md', "r") as file:
            return file.read()

    def get_save_path(self, id: str, next_iteration_no: int = None) -> Path:
        iteration_no = next_iteration_no if next_iteration_no else helper.get_next_iteration_no(
            path.GENERATED_MODEL_CARDS_DIRECTORY.parent)
        return path.GENERATED_MODEL_CARDS_DIRECTORY.parent / f'run_{iteration_no}' / f'{helper.get_repo_dir_name(id)}.md'


if __name__ == "__main__":
    gemini_client = GenAIClient(constants.GEMINI_2_5_PRO_PREVIEW, constants.GEMINI_API_KEY)
    model_card_generator = ModelCardGenerator(Path('system_instruction.md'), None, gemini_client)

    # model_ids_file_paths = helper.get_repo_files_without_tokenizer_files()
    # model_card_generator.process_batch_request_with_files(model_ids_file_paths)

    model_id = 'CohereForAI/c4ai-command-r-plus'
    file_paths = {model_id: [
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "config.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "generation_config.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "model.safetensors.index.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "special_tokens_map.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "tokenizer_config.json"
    ]}
    model_card_generator.process_single_request(model_id, file_paths[model_id])