import json
from pathlib import Path

from api_clients.openai_reasoning_json_client import OpenAIReasoningJsonClient
from model_card_evaluator.correctness_evaluator_jury.base_correctness_evaluator import BaseCorrectnessEvaluator, \
    remove_existings
from util import constants, helper, path


def get_json_schema() -> dict:
    return {
        'type': 'object',
        'properties': {
            'sections': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'section_name': {
                            'type': 'string',
                            'enum': [
                                'Model Details: Person or organization developing model',
                                'Model Details: Model date',
                                'Model Details: Model version',
                                'Model Details: Model type',
                                'Model Details: Training details',
                                'Model Details: Paper or other resource for more information',
                                'Model Details: Citation details',
                                'Model Details: License',
                                'Model Details: Contact',
                                'Intended Use: Primary intended uses',
                                'Intended Use: Primary intended users',
                                'Intended Use: Out-of-scope uses',
                                'How to Use',
                                'Factors: Relevant factors',
                                'Factors: Evaluation factors',
                                'Metrics: Model performance measures',
                                'Metrics: Decision thresholds',
                                'Metrics: Variation approaches',
                                'Evaluation Data: Datasets',
                                'Evaluation Data: Motivation',
                                'Evaluation Data: Preprocessing',
                                'Training Data: Datasets',
                                'Training Data: Motivation',
                                'Training Data: Preprocessing',
                                'Quantitative Analyses: Unitary results',
                                'Quantitative Analyses: Intersectional results',
                                'Memory or Hardware Requirements: Loading Requirements',
                                'Memory or Hardware Requirements: Deploying Requirements',
                                'Memory or Hardware Requirements: Training or Fine-tuning Requirements',
                                'Ethical Considerations',
                                'Caveats and Recommendations: Caveats',
                                'Caveats and Recommendations: Recommendations'
                            ]
                        },
                        'is_correct': {
                            'type': 'boolean'
                        },
                        'incorrect_information': {
                            'type': 'string'
                        }
                    },
                    'required': [
                        'section_name',
                        'is_correct',
                        'incorrect_information'
                    ],
                    'additionalProperties': False
                },
                'additionalProperties': False
            },
        },
        'additionalProperties': False,
        'required': [
            'sections'
        ]
    }


class OMiniCorrectnessEvaluator(BaseCorrectnessEvaluator):
    def get_save_path(self, model_id: str, next_iteration_no: int = None, sub_dir_name: str = None) -> Path:
        return super().get_save_path(model_id, next_iteration_no, 'gpt_5')


if __name__ == '__main__':
    gpt_5_client = OpenAIReasoningJsonClient(constants.GPT_5, constants.ASGAARD_OPENAI_API_KEY)
    correctness_evaluator = OMiniCorrectnessEvaluator(Path('system_instruction_common.md'), get_json_schema(),
                                                      gpt_5_client)

    model_ids_file_paths = helper.get_file_paths_for_jury()

    model_id = 'CAMB-AI/MARS5-TTS'
    correctness_evaluator.process_single_request(model_id, model_ids_file_paths[model_id], 2)

    # with open(path.CONFLICT_REPOS_LIST_FILE, 'r', encoding='utf-8') as file:
    #     conflict_model_ids = json.load(file)
    # conflict_model_ids_file_paths = {model_id: model_ids_file_paths[model_id] for model_id in conflict_model_ids}
    #
    # correctness_evaluator.process_batch_request_with_files(conflict_model_ids_file_paths, 2)
