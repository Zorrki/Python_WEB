import csv
import os

def aggregate_sales(csv_input, csv_output):
    sales_data = {}

    # Чтение данных из CSV файла
    with open(csv_input, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            quantity = int(row["quantity"])
            price = float(row["price"])
            revenue = quantity * price

            if product not in sales_data:
                sales_data[product] = 0
            sales_data[product] += revenue

    # Запись итоговых данных в новый CSV файл
    with open(csv_output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["product", "total_revenue"])
        writer.writeheader()
        for product, total_revenue in sales_data.items():
            writer.writerow({"product": product, "total_revenue": total_revenue})

# Пример использования функции
input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zad_4")
csv_input = os.path.join(input_directory, "sales.csv")
csv_output = os.path.join(input_directory, "total_sales.csv")

aggregate_sales(csv_input, csv_output)
