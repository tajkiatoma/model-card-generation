import json
from pathlib import Path

from util import path, helper


def summarize_safetensors_index(index_path: Path, output_file: Path):
    index_path = Path(index_path)
    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    weight_map = data.get("weight_map", {})
    metadata = data.get("metadata", {})
    total_size = metadata.get("total_size", 0)

    # Derive stats
    num_tensors = len(weight_map)
    shards = sorted(set(weight_map.values()))
    num_shards = len(shards)

    # Collect example layer names
    example_layers = list(weight_map.keys())[:550]  # first 5 for preview

    summary = {
        "index_file": str(index_path.name),
        "num_shards": num_shards,
        "num_tensors": num_tensors,
        "total_size_GB": round(total_size / (1024**3), 3),
        "example_shard_files": shards[:3],
        "example_layer_names": example_layers,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)


# Example usage
if __name__ == "__main__":
    model_id = 'deepseek-ai/DeepSeek-V2-Chat'
    index_file = path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / 'model.safetensors.index.json'
    summary_file = index_file.with_name('model.safetensors.index.summary.json')
    summarize_safetensors_index(index_file, summary_file)
