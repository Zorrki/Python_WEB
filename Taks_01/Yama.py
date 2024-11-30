def draw_pit(N):
    for i in range(N):
        # Левая часть ямы
        left_numbers = ''.join(str(N - j) for j in range(i + 1))
        # Центральная часть ямы (точки)
        dots = '.' * (2 * (N - i - 1))
        # Правая часть ямы
        right_numbers = ''.join(str(N - j) for j in range(i, -1, -1))
        # Полная строка ямы
        pit_row = left_numbers + dots + right_numbers
        print(pit_row)

# Запросить у пользователя число N
N = int(input("Введите число N: "))

draw_pit(N)
