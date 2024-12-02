import os
import zipfile

def create_zip_archive(src_directory, dst_zip_path):
    # Проверка существования исходного каталога
    if not os.path.isdir(src_directory):
        print(f"Каталог {src_directory} не существует.")
        return

    # Создание архива .zip
    with zipfile.ZipFile(dst_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Использование os.walk() для обхода всех файлов и подпапок
        for root, dirs, files in os.walk(src_directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Добавление файла в архив с путями относительно исходного каталога
                arcname = os.path.relpath(file_path, start=src_directory)
                zipf.write(file_path, arcname)
                print(f"Добавлен файл {file_path} как {arcname}")

# Пример использования функции
src_directory = "path/to/source/directory"
dst_zip_path = "path/to/destination/archive.zip"
create_zip_archive(src_directory, dst_zip_path)
