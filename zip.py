import os
import zipfile


def unzip_files(zip_folder_path, checking_folder):
    for zip_file in os.listdir(zip_folder_path):
        if zip_file.endswith('.zip'):
            name = zip_file.split('.')
            filename = name[0].split('/')[0]
            zip_file_path = os.path.join(zip_folder_path, zip_file)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(checking_folder)
                check_files_in_folder(checking_folder, filename)
            print(f'Зип-файл {zip_file_path} успешно разархивирован и перенесен в папку "Checking"')


def check_files_in_folder(folder_path, folder_name):
    files_in_folder = os.listdir(f"{folder_path}/{folder_name}")
    py_files = [file_name for file_name in files_in_folder if file_name.endswith('.py')]
    if set(py_files) != {'1.py', 'name.py'}:
        raise ValueError(
            'В папке должны находиться только файлы 1.py и name.py и другие файлы с расширением .py отсутствуют')


if __name__ == '__main__':
    zip_folder_path = input('Введите путь к папке со зип-архивами: ')
    checking_folder = os.path.join(os.getcwd(), 'Checking')
    os.makedirs(checking_folder, exist_ok=True)
    unzip_files(zip_folder_path, checking_folder)
