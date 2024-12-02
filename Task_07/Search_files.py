import os

def find_files_with_extension(directory, extension):
    # Создание списка для хранения путей к найденным файлам
    matching_files = []
    
    # Использование os.walk() для рекурсивного обхода указанного каталога
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Проверка, имеет ли имя файла указанное расширение
            if file.endswith(extension):
                # Получение полного пути к файлу
                full_path = os.path.join(root, file)
                matching_files.append(full_path)
    
    return matching_files

# Пример использования функции
directory = "path/to/directory"
extension = ".txt"
found_files = find_files_with_extension(directory, extension)
for file in found_files:
    print(file)
