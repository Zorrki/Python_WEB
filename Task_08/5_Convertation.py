import csv
import json
import os

def csv_to_json_grouped_by_author(csv_file, json_file):
    # Проверка существования CSV файла
    if not os.path.exists(csv_file):
        print(f"Файл {csv_file} не найден.")
        return
    
    books_by_author = {}
    
    # Чтение данных из CSV файла
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            author = row["author"]
            book = {"title": row["title"], "year": row["year"]}
            if author not in books_by_author:
                books_by_author[author] = []
            books_by_author[author].append(book)
    
    # Запись данных в JSON файл
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(books_by_author, f, ensure_ascii=False, indent=4)

# Пример использования функции
input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zad_5")
csv_file = os.path.join(input_directory, "books.csv")
json_file = os.path.join(input_directory, "books_by_author.json")

print(f"Путь к CSV файлу: {csv_file}")
print(f"Путь к JSON файлу: {json_file}")

csv_to_json_grouped_by_author(csv_file, json_file)
