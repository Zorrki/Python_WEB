def find_duplicates(lst):
    duplicates = []
    for element in lst:
        if lst.count(element) > 1 and element not in duplicates:
            duplicates.append(element)
    return duplicates

# Пример использования
input_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
result = find_duplicates(input_list)
print("Список с дублирующимися элементами:", result)
