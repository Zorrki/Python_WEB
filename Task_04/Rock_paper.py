import random

def rock_paper_scissors():
    options = ["Камень", "Ножницы", "Бумага"]
    while True:
        user_choice = input("Выберите Камень, Ножницы или Бумага (или 'выход' для возврата в меню): ")
        if user_choice.lower() == 'выход':
            break
        if user_choice not in options:
            print("Неверный выбор. Попробуйте снова.")
            continue
        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == "Камень" and computer_choice == "Ножницы") or \
             (user_choice == "Ножницы" and computer_choice == "Бумага") or \
             (user_choice == "Бумага" and computer_choice == "Камень"):
            print("Вы выиграли!")
        else:
            print("Вы проиграли.")

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуйте угадать его!")
    while True:
        user_guess = int(input("Введите ваше предположение: "))
        if user_guess < number_to_guess:
            print("Моё число больше.")
        elif user_guess > number_to_guess:
            print("Моё число меньше.")
        else:
            print("Поздравляю! Вы угадали число.")
            break

def main_menu():
    while True:
        print("\nГлавное меню")
        print("1 - Камень, ножницы, бумага")
        print("2 - Угадай число")
        print("3 - Выход")
        choice = input("Сделайте выбор: ")
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            guess_the_number()
        elif choice == '3':
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
