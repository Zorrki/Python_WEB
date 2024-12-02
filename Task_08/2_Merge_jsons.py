import glob
import json
import os

def merge_json_files(input_directory):
    # Поиск всех JSON файлов в указанной директории
    json_files = glob.glob(os.path.join(input_directory, '*.json'))
    
    all_employees = []
    
    # Чтение данных из каждого JSON файла и добавление их в общий список
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_employees.extend(data)
    
    # Сохранение объединенных данных в новый JSON файл в той же директории
    output_file = os.path.join(input_directory, "all_employees.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_employees, f, ensure_ascii=False, indent=4)

# Пример использования функции
input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zad_2")
merge_json_files(input_directory)
