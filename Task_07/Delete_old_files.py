import os
import time

def remove_old_files(directory, days):
    # Получение текущего времени в секундах с начала эпохи (01.01.1970)
    current_time = time.time()
    
    # Преобразование количества дней в секунды
    threshold_time = current_time - (days * 86400)
    
    # Использование os.walk() для рекурсивного обхода всех каталогов и файлов
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Получение времени последнего изменения файла
            file_mtime = os.path.getmtime(file_path)
            
            # Сравнение времени последнего изменения файла с пороговым значением
            if file_mtime < threshold_time:
                # Удаление файла
                os.remove(file_path)
                print(f"Удален файл: {file_path}")

# Пример использования функции
directory = "path/to/directory"
days = 30
remove_old_files(directory, days)
