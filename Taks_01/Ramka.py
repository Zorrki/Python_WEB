def draw_frame(width, height):
    for i in range(height):  # Внешний цикл для строк рамки
        for j in range(width):  # Внутренний цикл для символов в строке
            if i == 0 or i == height - 1:  # Условие для верхней и нижней горизонтальных линий
                print('-', end='')
            elif j == 0 or j == width - 1:  # Условие для вертикальных линий
                print('|', end='')
            else:
                print(' ', end='')  # Пробелы в середине рамки
        print()  # Переход на новую строку

# Запросить у пользователя ширину и высоту рамки
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

draw_frame(width, height)
