import logging
import os

# Получение пути к директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Настройка логирования
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Форматтер для сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для сообщений уровня DEBUG и INFO
debug_info_handler = logging.FileHandler(os.path.join(script_dir, 'debug_info.log'), encoding='utf-8')
debug_info_handler.setLevel(logging.DEBUG)
debug_info_handler.setFormatter(formatter)
logger.addHandler(debug_info_handler)

# Обработчик для сообщений уровня WARNING и выше
warnings_errors_handler = logging.FileHandler(os.path.join(script_dir, 'warnings_errors.log'), encoding='utf-8')
warnings_errors_handler.setLevel(logging.WARNING)
warnings_errors_handler.setFormatter(formatter)
logger.addHandler(warnings_errors_handler)

# Логирование сообщений различных уровней
logger.debug('Это сообщение уровня DEBUG.')
logger.info('Это сообщение уровня INFO.')
logger.warning('Это сообщение уровня WARNING.')
logger.error('Это сообщение уровня ERROR.')
logger.critical('Это сообщение уровня CRITICAL.')
