from pathlib import Path

from api_clients.anthropic_api_client import AnthropicAPIClient
from model_card_evaluator.correctness_evaluator_jury.base_correctness_evaluator import BaseCorrectnessEvaluator
from util import helper, constants


class SonnetCorrectnessEvaluator(BaseCorrectnessEvaluator):
    def get_save_path(self, model_id: str, next_iteration_no: int = None, sub_dir_name: str = None) -> Path:
        return super().get_save_path(model_id, next_iteration_no, 'sonnet_4_5')


if __name__ == '__main__':
    sonnet_client = AnthropicAPIClient(constants.CLAUDE_SONNET_4_5, constants.ANTHROPIC_API_KEY)
    correctness_evaluator = SonnetCorrectnessEvaluator(Path('system_instruction_sonnet.md'), None, sonnet_client) # json schema is added in the prompt template

    model_ids_file_paths = helper.get_file_paths_for_jury()
    correctness_evaluator.process_batch_request_with_files(model_ids_file_paths)
