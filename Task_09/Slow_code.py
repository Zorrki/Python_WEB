from functools import wraps
from time import sleep
from typing import Callable, Any

def slowdown_2s(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для замедления работы функции на 2 секунды.
    :param func: Декорируемая функция
    :return: Функция-обертка
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Функция-обертка, которая приостанавливает выполнение на 2 секунды.
        :param args: Позиционные аргументы
        :param kwargs: Именованные аргументы
        :return: Результат выполнения декорируемой функции
        """
        sleep(2)  # Приостановка выполнения на 2 секунды
        result = func(*args, **kwargs)  # Вызов оригинальной функции
        return result

    return wrapper

@slowdown_2s
def test() -> None:
    """
    Проверка декоратора и вывод простого сообщения.
    :return: None
    """
    print('<Тут что-то происходит...>')

@slowdown_2s
def another_function() -> None:
    """
    Еще один пример функции для проверки декоратора.
    :return: None
    """
    print('Еще один тестовый вывод.')

if __name__ == "__main__":
    test()  # Ожидайте задержку 2 секунды перед выводом сообщения
    another_function()  # Ожидайте задержку 2 секунды перед выводом сообщения
