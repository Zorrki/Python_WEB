def maximum_of_two(a, b):
    """Функция принимает два числа и возвращает большее из них"""
    if a > b:
        return a
    else:
        return b

def maximum_of_three(a, b, c):
    """Функция принимает три числа и возвращает большее из них"""
    # Использует функцию maximum_of_two для нахождения наибольшего из трёх чисел
    return maximum_of_two(maximum_of_two(a, b), c)

# Пример использования функций
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

max_number = maximum_of_three(num1, num2, num3)
print(f"Наибольшее число из {num1}, {num2} и {num3} это: {max_number}")
