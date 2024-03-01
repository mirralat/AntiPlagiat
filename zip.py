import os
import zipfile

def unzip_files(zip_folder_path, checking_folder):
    for zip_file in os.listdir(zip_folder_path):
        if zip_file.endswith('.zip'):
            zip_file_path = os.path.join(zip_folder_path, zip_file)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
                extracted_folder = os.path.join(checking_folder, folder_name)
                os.makedirs(extracted_folder, exist_ok=True)
                zip_ref.extractall(extracted_folder)
                check_files_in_folder(extracted_folder)
            print(f'Зип-файл {zip_file_path} успешно разархивирован и перенесен в папку "Checking"')

def check_files_in_folder(folder_path):
    files_in_folder = os.listdir(folder_path)
    py_files = [file_name for file_name in files_in_folder if file_name.endswith('.py')]
    if set(py_files) != {'1.py', 'name.py'}:
        raise ValueError('В папке должны находиться только файлы 1.py и name.py и другие файлы с расширением .py отсутствуют')

if __name__ == '__main__':
    zip_folder_path = input('Введите путь к папке со зип-архивами: ')
    checking_folder = os.path.join(os.getcwd(), 'Checking')
    os.makedirs(checking_folder, exist_ok=True)
    unzip_files(zip_folder_path, checking_folder)
