# MCGenie: Automatic Model Card Generation Using an LLM

## How to Generate a Model Card Using MCGenie
To generate a model card for a repository, edit the following code at the bottom of the `model_card_generator/model_card_generator.py` file:

```python
    model_id = 'CohereForAI/c4ai-command-r-plus'
    file_paths = {model_id: [
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "config.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "generation_config.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "model.safetensors.index.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "special_tokens_map.json",
        path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id) / "tokenizer_config.json"
    ]}
```

Replace `model_id` with the name of the repository for which you want to generate a model card. It doesn't need to be the name of the repository. The `model_id` is used to name the generated model card file.

For, `file_paths`, specify the repository files you want to include in the model card generation process. Each file path must be a `Path` object from the [`pathlib`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) library, referring to the location of the file in your machine. 

A model card will be generated inside the `data/generated_model_cards/run_2` directory with your provided name.

## Reproduce Result of the Paper
