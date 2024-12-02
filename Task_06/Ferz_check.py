def is_queen_safe(queens):
    n = len(queens)
    
    # Шаг 1: Создаем множества для проверки строк, столбцов и диагоналей
    rows = set()
    cols = set()
    diag1 = set()  # диагональ главная (row - col)
    diag2 = set()  # диагональ побочная (row + col)
    
    for row, col in queens:
        # Проверяем, находится ли ферзь в одной строке или столбце с другим ферзем
        if row in rows or col in cols:
            return False
        
        # Проверяем, находится ли ферзь на одной диагонали с другим ферзем
        if (row - col) in diag1 or (row + col) in diag2:
            return False
        
        # Добавляем координаты в множества
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
    
    return True

# Пример использования функции
queens = [(1, 5), (2, 3), (3, 1), (4, 7), (5, 2), (6, 8), (7, 6), (8, 4)]
print(is_queen_safe(queens))  # Вывод: True, ферзи не бьют друг друга

queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
print(is_queen_safe(queens))  # Вывод: False, все ферзи бьют друг друга
