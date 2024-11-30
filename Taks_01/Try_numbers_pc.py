def guess_number():
    start = 1
    finish = 100
    count = 1  # Начало отсчёта попыток

    while start <= finish:
        guess = (start + finish) // 2  # Среднее значение диапазона
        print(f"Твое число равно, меньше или больше, чем число {guess}?")
        print("1 - равно, 2 - больше, 3 - меньше")
        answer = int(input("Введите ответ: "))

        if answer == 1:
            print(f"Угадано! Число: {guess}. Попыток: {count}")
            break
        elif answer == 2:
            start = guess + 1  # Обновление нижнего предела диапазона
        elif answer == 3:
            finish = guess - 1  # Обновление верхнего предела диапазона
        else:
            print("Некорректный ответ, попробуйте снова.")

        count += 1  # Увеличение счётчика попыток

# Запуск программы
guess_number()
