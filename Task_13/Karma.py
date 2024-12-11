import random
import os

# Константа для достижения просветления
NIRVANA_KARMA = 500

# Определение пользовательских исключений
class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы убили кого-то!")

class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Вы напились!")

class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Авария. Вы попали в аварию!")

class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Чревоугодие. Вы обожрались!")

class DepressionError(Exception):
    def __init__(self):
        super().__init__("Депрессия. Вы в депрессии!")

# Функция, моделирующая один день жизни
def one_day():
    # Случайное количество кармы от 1 до 7
    day_karma = random.randint(1, 7)
    # Случайная вероятность выброса исключения
    if random.randint(1, 10) == 5:
        # Случайный выбор исключения
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma

# Основная функция симулятора
def main():
    karma = 0
    # Определяем путь к лог-файлу в той же директории, где находится скрипт
    log_file_path = os.path.join(os.path.dirname(__file__), 'karma.log')
    
    # Открываем файл для записи логов
    with open(log_file_path, 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                # Прибавляем карму за один день
                karma += one_day()
            except Exception as ex:
                # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')
            # Проверяем, достигнуто ли необходимое количество кармы
            if karma >= NIRVANA_KARMA:
                break
    # Сообщаем о достижении цели
    print('Вы достигли Нирваны! Омм...')

# Запуск основной функции
if __name__ == "__main__":
    main()
