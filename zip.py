import time
import os
import zipfile

def unzip_files(zip_folder_path, checking_folder, error_folder):
    for zip_file in os.listdir(zip_folder_path):  # перебираем все файлы в папке со зип-архивами
        if zip_file.endswith('.zip'):  # проверяем, является ли файл зип-архивом
            name = zip_file.split('.')  # разбиваем имя файла на части по точке
            filename = name[0].split('/')[0]  # получаем имя папки из имени файла
            zip_file_path = os.path.join(zip_folder_path, zip_file)  # получаем полный путь к зип-файлу
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:  # открываем зип-файл для чтения
                zip_ref.extractall(checking_folder)  # разархивируем файлы в папку для проверки
                if check_files_in_folder(checking_folder, filename, error_folder):
                    os.rename(os.path.join(checking_folder, filename), os.path.join(error_folder, filename))
                else:
                    print(f'Зип-файл {zip_file_path} успешно разархивирован и перенесен в папку "Checking"')

def check_files_in_folder(folder_path, folder_name, error_folder):
    files_in_folder = os.listdir(f"{folder_path}/{folder_name}")  # получаем список всех файлов в папке
    py_files = [file_name for file_name in files_in_folder if file_name.endswith('.py')]  # получаем список всех файлов с расширением .py
    required_files = {'1.py', 'name.py', '2.py', '3.py'}
    missing_files = required_files - set(py_files)
    extra_files = set(py_files) - required_files
    if missing_files or extra_files:
        if missing_files:
            print(f'Ошибка: В папке {folder_name} отсутствуют следующие файлы: {", ".join(missing_files)}')
        if extra_files:
            print(f'Ошибка: В папке {folder_name} присутствуют лишние файлы: {", ".join(extra_files)}')
        return True
    return False

if __name__ == '__main__':
    zip_folder_path = input('Введите путь к папке со зип-архивами: ')  # запрашиваем у пользователя путь к папке со зип-архивами
    checking_folder = os.path.join(os.getcwd(), 'Checking')  # создаем папку для проверки разархивированных файлов
    error_folder = os.path.join(os.getcwd(), 'Error_Checking')  # создаем папку для ошибочных файлов
    os.makedirs(checking_folder, exist_ok=True)  # создаем папку, если она еще не существует
    os.makedirs(error_folder, exist_ok=True)  # создаем папку, если она еще не существует
    try:
        unzip_files(zip_folder_path, checking_folder, error_folder)  # вызываем функцию для разархивирования файлов и проверки наличия нужных файлов
    except ValueError as e:
        print(e)
