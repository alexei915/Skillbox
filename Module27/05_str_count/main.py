from typing import Callable, Any
import functools


def counter(func: Callable, lst=[]) -> Callable:
    """ Декоратор. Считает и выводит количество
    вызовов декорируемой функции.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        lst.append(1)
        print('Функция {} вызывается {}-ый раз'.format(func.__name__, len(lst)))
        result = func(*args, **kwargs)
        print(result, '\n')
        return result
    return wrapped_func


@counter
def greeting(name: str, age: int = None) -> str:
    """ Функция. Возвращает одну из строк в зависимости от
     переданных аргументов

     :arg: name, age

     :return: str
     """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)