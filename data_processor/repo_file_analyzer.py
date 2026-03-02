from pprint import pprint

from util import helper, path

if __name__ == '__main__':
    model_ids_file_paths = helper.get_model_file_paths()

    for model_id in helper.get_token_limit_exceed_after_summary_repo_ids():
        print(f'-----------------------------------------------------{model_id}')
        model_dir = path.REPOS_DIRECTORY / helper.get_repo_dir_name(model_id)
        paper_dir = path.MODEL_PAPER_DIRECTORY / f'{helper.get_repo_dir_name(model_id)}'
        model_file_paths = model_ids_file_paths[model_id]
        #
        # total_size_of_directory = 0
        #
        # if paper_dir.exists():
        #     paper_file_path = next(paper_dir.iterdir(), None)
        #     if paper_file_path:
        #         paper_size_in_kb = paper_file_path.stat().st_size / 1024
        #         if paper_size_in_kb > 2048:
        #             print(f'{paper_file_path.name}, {paper_size_in_kb:.2f} KB')
        #         total_size_of_directory += paper_size_in_kb

        repo_files = []
        for file in model_file_paths:
            size_in_kb = file.stat().st_size / 1024
            if file.is_relative_to(model_dir):
                repo_files.append([str(file.relative_to(model_dir)), size_in_kb])
            elif file.is_relative_to(paper_dir):
                repo_files.append([str(file.relative_to(paper_dir)), size_in_kb])

        sorted_files = sorted(repo_files, key=lambda x: x[1], reverse=True)

        for file in sorted_files:
            print(f'{file[0]}, {file[1]:.2f} KB')

        # total_size_of_directory += size_in_kb
            # if size_in_kb > 2048:
            #     try:
            #         print(f'{model_id}: {file.relative_to(model_dir)}, {size_in_kb:.2f} KB')
            #     except ValueError as e:
            #         pass

        # size_mb = total_size_of_directory / 1024
        # print(f'Total size of {model_id} directory: {size_mb:.2f} MB\n')