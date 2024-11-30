def generator_function(n):
    for i in range(1, n + 1):
        yield i ** 2

def main():
    # Запросить у пользователя число N
    N = int(input("Введите число N: "))

    # Использование функции-генератора
    print("Последовательность квадратов чисел (функция-генератор):")
    for square in generator_function(N):
        print(square)

    # Генераторное выражение для квадратов чисел от 1 до N
    generator_expression = (i ** 2 for i in range(1, N + 1))

    # Вывод сгенерированных значений
    print("Последовательность квадратов чисел (генераторное выражение):")
    for square in generator_expression:
        print(square)

if __name__ == "__main__":
    main()
