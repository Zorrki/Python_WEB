import os

def batch_rename_files(target_name, num_digits, src_extension, dst_extension, name_range, directory="."):
    # Проверка существования каталога
    if not os.path.isdir(directory):
        print(f"Каталог {directory} не существует.")
        return

    files = [f for f in os.listdir(directory) if f.endswith(src_extension)]
    for i, old_file in enumerate(files, start=1):
        # Извлечение оригинального имени без расширения
        base_name = os.path.splitext(old_file)[0]
        
        # Получение диапазона сохраняемого оригинального имени
        original_part = base_name[name_range[0]-1:name_range[1]]
        
        # Формирование нового имени файла
        new_file_name = f"{original_part}{target_name}{i:0{num_digits}}.{dst_extension}"
        
        # Переименование файла
        old_file_path = os.path.join(directory, old_file)
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(old_file_path, new_file_path)
        print(f"Переименован файл {old_file} в {new_file_name}")

# Пример использования функции
batch_rename_files(
    target_name="newname",
    num_digits=3,
    src_extension=".txt",
    dst_extension="md",
    name_range=[3, 6],
    directory="example_directory"
)
