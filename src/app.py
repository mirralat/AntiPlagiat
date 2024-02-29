from comparator import get_significant_subtrees, compare_subtrees
import ast
import os

reorder_depth = 10000
def compare_directory(directory, target_file):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.py')]
    if len(files) == 0:
        print("Directory is empty!")
        return []

    results = []
    with open(directory + target_file, "r") as source:
        target_tree = ast.parse(source.read(), mode="exec")

    target_subtree_list = get_significant_subtrees(target_tree)
    for file in files:
        if file == target_file:
            continue

        file_path = os.path.join(directory, file)
        with open(directory + file, "r") as source:
            tree = ast.parse(source.read(), mode="exec")

        subtree_list = get_significant_subtrees(tree)

        similarity = compare_subtrees(subtree_list, target_subtree_list, reorder_depth)[0]
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