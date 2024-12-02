import os
import json
import csv
import pickle

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            total_size += os.path.getsize(file_path)
    return total_size

def scan_directory(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.basename(root)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            size = get_directory_size(dir_path)
            result.append({
                "name": dir,
                "path": dir_path,
                "type": "directory",
                "size": size,
                "parent": parent_dir
            })
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            result.append({
                "name": file,
                "path": file_path,
                "type": "file",
                "size": size,
                "parent": parent_dir
            })
    return result

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "path", "type", "size", "parent"])
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

# Пример использования функций
directory = "path/to/directory"
data = scan_directory(directory)

# Определение текущей директории, где находится скрипт
current_directory = os.path.dirname(os.path.abspath(__file__))

# Сохранение результатов в файлы форматов JSON, CSV и Pickle в ту же директорию
save_to_json(data, os.path.join(current_directory, "output.json"))
save_to_csv(data, os.path.join(current_directory, "output.csv"))
save_to_pickle(data, os.path.join(current_directory, "output.pkl"))
