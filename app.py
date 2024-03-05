import os
import sys

from src.antiplagiat_calc import check_plagiat


def compare_directory(directory: str, target_file_name: str, state: str = None, similarity_threshold: float = 0):
    results = []

    dir_filenames_list = [f for f in os.listdir(directory) if
                          os.path.isfile(os.path.join(directory, f)) and f.endswith('.py')]

    if not dir_filenames_list:
        print("Directory is empty!")
        return results

    with open(target_file_name, "r") as f:
        source = f.read()

    for filename in dir_filenames_list:
        if os.path.samefile(directory + filename, target_file_name):
            continue

        with open(directory + filename, "r") as f:
            source_to_compare = f.read()

        similarity = check_plagiat(source, source_to_compare, state)
        if similarity >= similarity_threshold:
            results.append((filename, similarity))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def main():
    if len(sys.argv) < 3:
        print(
            f"{sys.argv[0]}: missing operands, correct format:",
            f"appname directory_with_files filename.py",
            sep="\n"
        )
        quit()

    directory, target_file = sys.argv[1], sys.argv[2]

    state = None
    threshold = 0
    if len(sys.argv) == 4:
        if sys.argv[3].isnumeric():
            threshold = float(sys.argv[3])
        else:
            state = sys.argv[3]
    if len(sys.argv) == 5:
        state = sys.argv[3]
        threshold = float(sys.argv[4])


    if not directory.endswith('/'):
        directory += '/'
    if not os.path.isdir(directory):
        raise ValueError(f"Unable to open directory: '{directory}'.")

    if not target_file.endswith('.py'):
        target_file += '.py'
    if not os.path.isfile(target_file):
        raise ValueError(f"Unable to find file: '{target_file}'.")

    if state is not None:
        similarity_list = compare_directory(directory, target_file, state, threshold)

        for result in similarity_list:
            print(f'ID: {result[0]}, Similarity: {result[1]}')

        exit()

    else:
        similarity_list = compare_directory(directory, target_file, 'jaccard', threshold)
        if len(similarity_list) != 0:
            print("------------------------------Jaccard-------------------------------")
            for result in similarity_list:
                print(f'ID: {result[0]}, Similarity: {result[1]}')

        similarity_list = compare_directory(directory, target_file, 'levenshtein', threshold)
        if len(similarity_list) != 0:
            print("----------------------------Levenshtein-----------------------------")
            for result in similarity_list:
                print(f'ID: {result[0]}, Similarity: {result[1]}')

        similarity_list = compare_directory(directory, target_file, 'ast', threshold)
        if len(similarity_list) != 0:
            print("-------------------------------AST----------------------------------")
            for result in similarity_list:
                print(f'ID: {result[0]}, Similarity: {result[1]}')


if __name__ == "__main__":
    main()
