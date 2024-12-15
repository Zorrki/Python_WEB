import argparse
import logging
import os
from datetime import datetime

# Настройка логирования
script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('options_logger')
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
def process_args(number, text, repeat, verbose):
    """
    Процессинг числа и строки с опциями.
    """
    if verbose:
        print(f'Полученные аргументы: number={number}, text="{text}", repeat={repeat}')
        logger.info(f'Полученные аргументы: number={number}, text="{text}", repeat={repeat}')

    result = f'Число: {number}, Строка: {" ".join([text] * repeat)}'
    print(result)
    return result

def main():
    try:
        # Создание парсера аргументов
        parser = argparse.ArgumentParser(description='Процессинг числа и строки с дополнительными опциями.')
        
        # Добавление обязательных аргументов
        parser.add_argument('number', type=int, help='Число для вывода')
        parser.add_argument('text', type=str, help='Строка для вывода')
        
        # Добавление опций
        parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
        parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')
        
        # Парсинг аргументов
        args = parser.parse_args()
        
        # Вывод текущих аргументов для проверки
        print(f'Аргументы после парсинга: number={args.number}, text="{args.text}", repeat={args.repeat}, verbose={args.verbose}')
        
        # Вызов функции с аргументами
        process_args(args.number, args.text, args.repeat, args.verbose)
    except SystemExit as e:
        # Логирование ошибки парсинга аргументов
        logger.error(f'Ошибка при парсинге аргументов: {e}', exc_info=True)
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    main()
