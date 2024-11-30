def reversal(x):
    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    return reversed_x

def main():
    # Запрашиваем у пользователя два числа
    N = int(input("Введите первое число: "))
    K = int(input("Введите второе число: "))

    # Переворачиваем числа
    reversed_N = reversal(N)
    reversed_K = reversal(K)

    # Выводим перевёрнутые числа
    print(f"Первое число наоборот: {reversed_N}")
    print(f"Второе число наоборот: {reversed_K}")

    # Складываем перевёрнутые числа
    sum_reversed = reversed_N + reversed_K

    # Переворачиваем сумму
    final_result = reversal(sum_reversed)

    # Выводим результат
    print(f"Сумма: {sum_reversed}")
    print(f"Сумма наоборот: {final_result}")

if __name__ == "__main__":
    main()
