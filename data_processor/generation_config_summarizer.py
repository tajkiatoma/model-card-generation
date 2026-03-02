import json
from pathlib import Path

from util import path, helper


def summarize_generation_config(config_file_path: Path, output_file_path: Path):
    with open(config_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    summary = {}

    # Copy only fields relevant for documentation generation
    for key in ["do_sample", "temperature", "top_k", "top_p", "num_beams",
                "max_length", "max_new_tokens", "min_length", "min_new_tokens",
                "repetition_penalty", "no_repeat_ngram_size",
                "bos_token_id", "eos_token_id", "pad_token_id"]:
        if key in data:
            summary[key] = data[key]

    # Tokenizer info
    if "char_to_id" in data:
        summary["tokenizer_type"] = "char-level"
        summary["vocab_size"] = len(data["char_to_id"])
        # sample only first 20 chars
        summary["sample_chars"] = list(data["char_to_id"].keys())[:20]

    # Optional: notes
    summary["notes"] = "Full char-to-ID mapping removed to reduce size; only a summary is kept for documentation."

    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    model_id = 'facebook/seamless-m4t-v2-large'
    config_file = path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / 'generation_config.json'
    summary_file = config_file.with_name('generation_config_summary.json')
    summarize_generation_config(config_file, summary_file)
