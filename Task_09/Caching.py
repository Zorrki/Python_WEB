def cache_decorator(func):
    """
    Декоратор для кэширования результатов функции.
    :param func: Декорируемая функция
    :return: Функция-обертка с кэшированием
    """
    cache = {}  # Словарь для хранения кэшированных результатов

    def wrapper(number):
        """
        Функция-обертка, которая сначала проверяет кэш перед вызовом функции.
        :param number: Аргумент для декорируемой функции
        :return: Результат выполнения функции
        """
        if number in cache:
            return cache[number]  # Возвращаем результат из кэша, если он есть
        result = func(number)
        cache[number] = result  # Сохраняем результат в кэше
        return result

    return wrapper

@cache_decorator
def fibonacci(number):
    """
    Функция для вычисления чисел Фибоначчи с использованием рекурсии.
    :param number: Позиция числа Фибоначчи
    :return: Число Фибоначчи
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

# Проверка работы декоратора и функции
print(fibonacci(10))  # Ожидаем, что результат будет вычислен и закэширован
print(fibonacci(10))  # Ожидаем, что результат будет возвращен из кэша
print(fibonacci(5))   # Ожидаем, что результат будет вычислен и закэширован
