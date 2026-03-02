from abc import ABC

from pathlib import Path

from api_clients.llm_pipeline import LLMPipeline
from util import path, helper


class BaseCorrectnessEvaluator(LLMPipeline, ABC):
    def get_prompt(self, model_id: str) -> str:
        generated_model_card_path = path.GENERATED_MODEL_CARDS_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}.md'
        with open(generated_model_card_path, 'r', encoding='utf-8') as file:
            generated_model_card = file.read()

        prompt = (f'Verify the following model card based on provided model repository files:\n'
                  f'Model Card:\n'
                  f'"""\n'
                  f'{generated_model_card}\n'
                  f'"""\n'
                  f'Model Repository Files:')
        return prompt

    def get_save_path(self, model_id: str, next_iteration_no: int = None, sub_dir_name: str = None) -> Path:
        save_root = path.LLM_JURY_RESULT_DIRECTORY / sub_dir_name

        if next_iteration_no:
            return save_root / f'run_{next_iteration_no}' / f'{helper.get_repo_dir_name(model_id)}.json'

        next_iteration_no = helper.get_next_iteration_no(save_root)
        return save_root / f'run_{next_iteration_no}' / f'{helper.get_repo_dir_name(model_id)}.json'


def remove_existings(model_ids: list, source_dir: Path) -> list:
    existing_files = [file.stem for file in source_dir.glob('*.json')]
    return [model_id for model_id in model_ids if helper.get_repo_dir_name(model_id) not in existing_files]