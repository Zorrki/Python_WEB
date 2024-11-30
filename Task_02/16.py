def to_hex(n):
    if n == 0:
        return '0'
    
    hex_digits = '0123456789ABCDEF'
    is_negative = n < 0
    if is_negative:
        n = -n
    
    hex_str = ''
    while n > 0:
        hex_str = hex_digits[n % 16] + hex_str
        n //= 16
    
    if is_negative:
        hex_str = '-' + hex_str
    
    return hex_str

# Запросить у пользователя целое число
number = int(input("Введите целое число: "))

# Преобразовать число в шестнадцатеричное представление
hex_representation = to_hex(number)

# Проверка с использованием встроенной функции hex
print(f"Пользовательская функция: {hex_representation}")
print(f"Встроенная функция: {hex(number)[2:].upper()}")
