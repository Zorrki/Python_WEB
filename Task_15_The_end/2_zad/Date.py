import logging
import os
import sys
from datetime import datetime

# Словарь для перевода дней недели на русский язык
days_of_week = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}

# Класс-декоратор для логирования
class LoggerDecorator:
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            self.logger.info(f"Выполнение {func.__name__} с параметрами args: {args}, kwargs: {kwargs}")
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                duration = (end_time - start_time).total_seconds()
                self.logger.info(f"{func.__name__} выполнено успешно за {duration} секунд. Результат: {result}")
                return result
            except Exception as e:
                self.logger.error(f"Ошибка в {func.__name__}: {e}", exc_info=True)
                raise
        return wrapper

# Настройка логирования
script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Форматтер для сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчики логов
debug_info_handler = logging.FileHandler(os.path.join(script_dir, 'debug_info.log'), encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)

warnings_errors_handler = logging.FileHandler(os.path.join(script_dir, 'warnings_errors.log'), encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

@LoggerDecorator(logger)
def display_current_datetime():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = days_of_week[now.strftime('%A')]  # Переводим день недели на русский
    week_number = now.isocalendar()[1]
    
    print(f'Текущие дата и время: {formatted_date}')
    print(f'День недели: {day_of_week}')
    print(f'Номер недели: {week_number}')
    
    return formatted_date, day_of_week, week_number

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Если переданы аргументы командной строки
        print(f'Переданные аргументы: {sys.argv[1:]}')
        logger.info(f'Переданные аргументы: {sys.argv[1:]}')
    else:
        # Запуск без аргументов
        display_current_datetime()
