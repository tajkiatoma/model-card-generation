import json

from data_processor.repo_file_lister import is_pointer_file
from util import path, helper


def summarize_tokenizer(input_file, output_file, vocab_sample=100, merges_sample=100):
    with open(input_file, "r", encoding="utf-8") as f:
        tokenizer = json.load(f)

    summary = {}

    # 1. Basic model info
    if "model" in tokenizer:
        summary["model"] = {
            "type": tokenizer["model"].get("type", "unknown"),
        }

        vocab = tokenizer["model"].get("vocab", {})

        if isinstance(vocab, dict):
            summary["model"]["vocab_size"] = len(vocab)
            summary["model"]["sample_vocab"] = dict(list(vocab.items())[:vocab_sample])

        elif isinstance(vocab, list):
            summary["model"]["vocab_size"] = len(vocab)
            summary["model"]["sample_vocab"] = vocab[:vocab_sample]

        if "merges" in tokenizer["model"]:
            summary["model"]["sample_merges"] = tokenizer["model"]["merges"][:merges_sample]

    # 2. Normalizer
    if "normalizer" in tokenizer:
        summary["normalizer"] = tokenizer["normalizer"]

    # 3. Pre-tokenizer
    if "pre_tokenizer" in tokenizer:
        summary["pre_tokenizer"] = tokenizer["pre_tokenizer"]

    # 4. Post-processor
    if "post_processor" in tokenizer:
        summary["post_processor"] = tokenizer["post_processor"]

    # 5. Decoder
    if "decoder" in tokenizer:
        summary["decoder"] = tokenizer["decoder"]

    # 6. Added tokens / special tokens
    if "added_tokens" in tokenizer:
        summary["special_tokens"] = [
            tok for tok in tokenizer["added_tokens"] if tok.get("special", False)
        ]

    # Save the summarized version
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"Summary written to {output_file}")


if __name__ == '__main__':
    # Example usage:
    # summarize_tokenizer("tokenizer.json", "tokenizer_summary.json")

    model_ids_file_paths = helper.get_model_file_paths()

    model_id = 'databricks/dolly-v2-12b'
    model_file_paths = model_ids_file_paths[model_id]

    for file in model_file_paths:
        if file.name == "tokenizer.json" and not is_pointer_file(file):
            summary_file_path = file.with_name('tokenizer_summary.json')
            summarize_tokenizer(file, summary_file_path)