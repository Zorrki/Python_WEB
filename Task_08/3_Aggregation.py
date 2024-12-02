import json
import csv
import os

def json_to_csv(json_file, csv_file):
    # Чтение данных из JSON файла
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Запись данных в CSV файл
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
        writer.writeheader()
        writer.writerows(data)

# Пример использования функции
input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zad_3")
json_file = os.path.join(input_directory, "products.json")
csv_file = os.path.join(input_directory, "products.csv")

json_to_csv(json_file, csv_file)
