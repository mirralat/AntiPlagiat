import os
import sys

from src.antiplagiat_calc import check_plagiat


def compare_directory(directory: str, target_file_name: str):
    results = []

    dir_filenames_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.py')]

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

        similarity = check_plagiat(source, source_to_compare)
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

    if not directory.endswith('/'):
        directory += '/'
    if not os.path.isdir(directory):
        raise ValueError(f"Unable to open directory: '{directory}'.")


    if not target_file.endswith('.py'):
        target_file += '.py'
    if not os.path.isfile(target_file):
        raise ValueError(f"Unable to find file: '{target_file}'.")

    similarity_list = compare_directory(directory, target_file)

    for result in similarity_list:
        print(f'ID: {result[0]}, Similarity: {result[1]}')


if __name__ == "__main__":
    main()
