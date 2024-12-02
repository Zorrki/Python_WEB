from functools import wraps
from typing import Callable, Any

def how_are_you(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор, который спрашивает у пользователя 'Как дела?' и
    выводит предопределенное сообщение перед вызовом декорируемой функции.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Функция-обертка, которая выполняет дополнительное поведение
        перед вызовом декорируемой функции.
        """
        input('Как дела? ')  # Запрашиваем ответ у пользователя
        print('А у меня не очень! Ладно, держи свою функцию.')  # Выводим сообщение
        result = func(*args, **kwargs)  # Вызов оригинальной функции
        return result

    return wrapper

@how_are_you
def test() -> None:
    """
    Проверка декоратора и вывод простого сообщения.
    """
    print('<Тут что-то происходит...>')

@how_are_you
def another_function() -> None:
    """
    Еще один пример функции для проверки декоратора.
    """
    print('Еще один тестовый вывод.')

if __name__ == "__main__":
    test()  # Проверка декоратора на функции
    another_function()
