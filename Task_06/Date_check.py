import datetime

def is_leap_year(year):
    # Проверка високосного года
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def validate_date(date_str):
    # Шаг 1: Разделение строки даты на день, месяц и год
    day, month, year = map(int, date_str.split('.'))
    
    # Шаг 2: Проверка диапазонов для месяца и дня
    if not (1 <= month <= 12):
        return False
    if not (1 <= year <= 9999):
        return False
    
    # Проверка корректности даты с использованием datetime
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        return False
    
    return True

# Пример использования функции
date_str = "29.02.2020"
print(validate_date(date_str))  # Вывод: True, так как 2020 - високосный год
date_str = "29.02.2019"
print(validate_date(date_str))  # Вывод: False, так как 2019 - не високосный год
