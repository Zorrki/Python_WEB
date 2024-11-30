def find_max_number(numbers_str):
    # Разделяем строку на отдельные числа и преобразуем их в целые числа
    numbers = list(map(int, numbers_str.split()))

    # Инициализируем переменную для хранения наибольшего числа
    max_number = numbers[0]

    # Проходим по каждому элементу списка и сравниваем его с текущим наибольшим числом
    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number

# Запросить у пользователя строку с числами
numbers_str = input("Введите список чисел через пробел: ")

# Найти наибольшее число в списке
max_number = find_max_number(numbers_str)

print(f"Наибольшее число в списке: {max_number}")
