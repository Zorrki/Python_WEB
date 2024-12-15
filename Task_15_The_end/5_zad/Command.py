import os
import logging
from collections import namedtuple
from argparse import ArgumentParser
from datetime import datetime

# Настройка логирования
script_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger('directory_logger')
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

directory_contents_handler = logging.FileHandler(os.path.join(script_dir, 'directory_contents.log'), encoding='utf-8')
directory_contents_handler.setLevel(logging.INFO)
directory_contents_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)
logger.addHandler(directory_contents_handler)

# Определение namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

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
def collect_info(directory_path):
    """Собирает информацию о содержимом директории и сохраняет в лог."""
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией.")
    
    # Получаем родительский каталог
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    
    # Перебираем содержимое директории
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        # Проверяем, является ли элемент директорией
        if os.path.isdir(entry_path):
            file_info = FileInfo(name=entry, extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)
        
        # Запись в лог
        logger.info(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}')

def main():
    """Основная функция для обработки командной строки и сбора информации."""
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")
    args = parser.parse_args()
    directory_path = args.directory
    try:
        collect_info(directory_path)
        print(f'Информация о содержимом директории "{directory_path}" успешно записана в файл "directory_contents.log".')
    except ValueError as e:
        print(e)
        logger.error(f'Ошибка: {e}', exc_info=True)

if __name__ == '__main__':
    main()
