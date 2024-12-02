def unique_elements(list1, list2):
    # Шаг 1: Преобразование обоих списков в множества
    set1 = set(list1)
    set2 = set(list2)
    
    # Шаг 2: Нахождение уникальных элементов для каждого множества
    unique_to_set1 = set1 - set2
    unique_to_set2 = set2 - set1
    
    # Шаг 3: Объединение двух результатов
    unique_elements = unique_to_set1 | unique_to_set2
    
    # Шаг 4: Преобразование множества уникальных элементов обратно в список
    return list(unique_elements)

# Пример использования функции
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(unique_elements(list1, list2))  # Вывод: [1, 2, 3, 6, 7, 8]
