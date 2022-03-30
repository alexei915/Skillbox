from typing import Callable, Any
import functools


def debug(func: Callable) -> Callable:
    """ Декоратор.при каждом вызове декорируемой функции
    выводит её имя (вместе со всеми передаваемыми аргументами) и
    затем какое значение она возвращает.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        arguments = ', '.join([repr(arg) for arg in args])
        kw_arguments = ', '.join([f'{key}={repr(value)}' for key, value in kwargs.items()])
        if arguments and kw_arguments:
            amount = arguments + ', ' + kw_arguments
        elif arguments:
            amount = arguments
        else:
            amount = kw_arguments
        print('Выполняется {}({})'.format(func.__name__, amount))
        result = func(*args, **kwargs)
        print("'{}' вернула значение {}".format(func.__name__, repr(result)))
        print(result, '\n')
        return result

    return wrapped_func


@debug
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
