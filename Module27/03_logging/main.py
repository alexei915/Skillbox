from typing import Callable, Any
import datetime
import functools


def logging(func: Callable) -> Callable:
    """ Декоратор. Отвечает за логирование функций """

    print('Название функции:', func.__name__)
    print(func.__doc__)

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except ValueError as v_error:
            with open('function_errors.log', 'a') as file:
                file.write('{} : {} : {}\n'.format(datetime.datetime.now().__str__(), func.__name__, v_error))
        except TypeError as t_error:
            with open('function_errors.log', 'a') as file:
                file.write('{} : {} : {}\n'.format(datetime.datetime.now().__str__(), func.__name__, t_error))

    return wrapped_func


@logging
def fibonacci(number: int) -> int:
    """ Функция. На вход подаётся позиция в ряду Фибонначи,
     возвращает число, находящееся на данной позиции.

     :args: int

     :return: int
     """
    if isinstance(number, int):
        if number < 3:
            return 1
        return fibonacci(number - 1) + fibonacci(number - 2)
    raise ValueError('Ошибка значения. Функция принимает на вход число.')


@logging
def flatten(data: list) -> list:
    """ Функция. На вход принимает список любой вложенности,
     раскрывает все вложенные списки, т. е. возвращает внешний
     список.

     :args: list

     :return: list
     """
    if isinstance(data, list):
        if not data:
            return data
        if isinstance(data[0], list):
            return flatten(data[0]) + flatten(data[1:])
        return data[:1] + flatten(data[1:])
    raise TypeError('Ошибка типа. Функция принимает на вход только список.')


print(fibonacci('f'))
print(flatten([1, [2, 3], [1, [2], 3]]))
