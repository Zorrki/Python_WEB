def calculate_danger(x):
    """Функция для расчета уровня опасности по заданной формуле"""
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(max_danger):
    """Функция для нахождения безопасной глубины с использованием бинарного поиска"""
    low = 0
    high = 4
    mid = (low + high) / 2

    while abs(calculate_danger(mid)) > max_danger:
        if calculate_danger(mid) > 0:
            high = mid
        else:
            low = mid
        mid = (low + high) / 2

    return mid

def main():
    """Основная функция программы"""
    try:
        max_danger = float(input("Введите максимально допустимый уровень опасности: "))
        if max_danger < 0:
            raise ValueError("Максимально допустимый уровень опасности должен быть положительным числом.")

        safe_depth = find_safe_depth(max_danger)
        print(f"Приблизительная глубина безопасной кладки: {safe_depth:.9f} м")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

if __name__ == "__main__":
    main()
