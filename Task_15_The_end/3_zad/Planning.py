import logging
import os
import sys
from datetime import datetime, timedelta
import argparse

# Настройка логирования
script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('task_logger')
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

@LoggerDecorator(logger)
def future_date(days_from_now):
    """
    Возвращает дату, которая наступит через указанное количество дней от текущей даты.
    :param days_from_now: Количество дней от текущей даты.
    :return: Отформатированная дата в формате YYYY-MM-DD.
    Примеры:
    >>> future_date(30)
    '2024-09-08'
    >>> future_date(-10)
    '2024-07-30'
    """
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

if __name__ == '__main__':
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Получение даты через указанное количество дней')
    parser.add_argument('days', type=int, help='Количество дней от текущей даты')
    args = parser.parse_args()
    
    # Получение даты через указанное количество дней
    result_date = future_date(args.days)
    print(f'Дата через {args.days} дней: {result_date}')
    logger.info(f'Дата через {args.days} дней: {result_date}')
