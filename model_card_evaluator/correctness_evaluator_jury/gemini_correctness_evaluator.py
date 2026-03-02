import json
from pathlib import Path

from api_clients.genai_client import GenAIClient
from model_card_evaluator.correctness_evaluator_jury.base_correctness_evaluator import BaseCorrectnessEvaluator
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
                        'is_correct'
                    ]
                }
            }
        }
    }


class GeminiCorrectnessEvaluator(BaseCorrectnessEvaluator):
    def get_save_path(self, model_id: str, next_iteration_no: int = None, sub_dir_name: str = None) -> Path:
        return super().get_save_path(model_id, next_iteration_no, 'gemini_2_5_pro_preview')


if __name__ == '__main__':
    gemini_client = GenAIClient(constants.GEMINI_2_5_PRO_PREVIEW, constants.GEMINI_API_KEY)
    correctness_evaluator = GeminiCorrectnessEvaluator(Path('system_instruction_common.md'), get_json_schema(), gemini_client)

    model_ids_file_paths = helper.get_file_paths_for_jury()

    model_id = 'CAMB-AI/MARS5-TTS'
    correctness_evaluator.process_single_request(model_id, model_ids_file_paths[model_id], 1)

    # correctness_evaluator.process_batch_request_with_files(model_ids_file_paths, 1)
