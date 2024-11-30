def sum_of_digits(number):
    """Функция для расчета суммы цифр числа"""
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def max_digit(number):
    """Функция для нахождения максимальной цифры числа"""
    max_d = 0
    while number > 0:
        digit = number % 10
        if digit > max_d:
            max_d = digit
        number //= 10
    return max_d

def min_digit(number):
    """Функция для нахождения минимальной цифры числа"""
    min_d = 9
    while number > 0:
        digit = number % 10
        if digit < min_d:
            min_d = digit
        number //= 10
    return min_d

def main():
    """Основная функция, зацикливающая ввод пользователя"""
    while True:
        number = int(input("Введите число (или 0 для выхода): "))
        if number == 0:
            print("Выход из программы.")
            break

        print("Выберите действие:")
        print("1 - Вывести сумму цифр числа")
        print("2 - Вывести максимальную цифру числа")
        print("3 - Вывести минимальную цифру числа")
        action = int(input("Ваш выбор: "))

        if action == 1:
            print(f"Сумма цифр числа {number}: {sum_of_digits(number)}")
        elif action == 2:
            print(f"Максимальная цифра числа {number}: {max_digit(number)}")
        elif action == 3:
            print(f"Минимальная цифра числа {number}: {min_digit(number)}")
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
