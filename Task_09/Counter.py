from functools import wraps
from typing import Callable, Any, Optional

def counter(func: Callable) -> Callable:
    """
    Декоратор для подсчета количества вызовов функции.
    :param func: Декорируемая функция.
    :return: Обертка функции с подсчетом вызовов.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Функция-обертка для увеличения и вывода счётчика вызовов функции.
        :param args: Позиционные аргументы декорируемой функции.
        :param kwargs: Именованные аргументы декорируемой функции.
        :return: Результат вызова декорируемой функции.
        """
        wrapper.count += 1  # Увеличиваем счетчик вызовов на единицу.
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию.
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")  # Выводим количество вызовов.
        return result  # Возвращаем результат вызова оригинальной функции.

    wrapper.count = 0  # Инициализируем счетчик вызовов.
    return wrapper  # Возвращаем обертку.

@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    """
    Приветствие с возрастом и именем.
    :param name: Имя человека.
    :param age: Возраст человека (по умолчанию None).
    :return: Строка с приветствием.
    """
    if age:
        return f"Ого, {name}! Тебе уже {age} лет, ты быстро растешь!"
    else:
        return f"Привет, {name}!"

@counter
def greeting2(name: str) -> None:
    """
    Приветствие с именем. Вывод в консоль.
    :param name: Имя человека.
    :return: None.
    """
    print(f'Привет, {name}!')

def main() -> None:
    """
    Основная функция для запуска.
    :return: None.
    """
    greeting("Том")  # Вызов функции greeting с одним аргументом.
    greeting("Миша", age=100)  # Вызов функции greeting с двумя аргументами.
    greeting2("Маша")  # Вызов функции greeting2.
    greeting(name="Катя", age=16)  # Вызов функции greeting с именем и возрастом.

main()  # Запуск основной функции.
