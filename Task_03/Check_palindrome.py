def is_palindrome(s):
    # Преобразование всех символов строки в нижний регистр
    s = s.lower()
    
    # Инициализация множества для символов, встречающихся нечётное количество раз
    odd_chars = set()
    
    # Обработка каждого символа в строке
    for char in s:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)
    
    # Проверка размера множества
    return len(odd_chars) <= 1

# Запросить у пользователя строку
input_str = input("Введите строку: ")

# Проверка, является ли строка палиндромом
if is_palindrome(input_str):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
