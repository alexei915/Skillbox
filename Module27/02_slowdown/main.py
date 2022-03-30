from time import sleep
from typing import Any, Callable
import functools


def slowing(func: Callable) -> Callable:
    """ Декоратор. Замедляет выполнение функции
     на 5 секунд
     """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        sleep(5)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@slowing
def histogram(text: str) -> dict:
    """ Функция, которая принимает на вход строку и
     формирует словарь частот встречающихся в ней букв

     :return: dict
     """
    frequency_dict = dict()
    for letter in text.lower():
        if letter.isalpha():
            frequency_dict[letter] = frequency_dict.get(letter, 0) + 1

    return frequency_dict


print(histogram('В этом модуле мы изучили декораторы, а теперь применяем их реализацию на практике'))