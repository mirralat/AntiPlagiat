import os

from src.antiplagiat_calc import check_plagiat


def compare_directory(directory, target_file):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.py')]
    if len(files) == 0:
        print("Directory is empty!")
        return []

    results = []
    with open(directory + target_file, "r") as source:
        code_one = source.read()

    for file in files:
        if file == target_file:
            continue

        with open(directory + file, "r") as source:
            code_two = source.read()

        similarity = check_plagiat(code_one, code_two)
        results.append((file, similarity))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


if __name__ == "__main__":
    directory = input("Enter directory with files: ")
    if not directory.endswith('/'):
        directory += '/'
    if not os.path.isdir(directory):
        raise ValueError(f"Unable to open directory: '{directory}'.")

    target_file = input("Enter name of target file: ")

    if not target_file.endswith('.py'):
        target_file += '.py'
    if not os.path.isfile(directory + target_file):
        raise ValueError(f"Unable to find file: '{target_file}'.")

    similarity_list = compare_directory(directory, target_file)
    for result in similarity_list:
        print(f'ID: {result[0]}, Similarity: {result[1]}')
