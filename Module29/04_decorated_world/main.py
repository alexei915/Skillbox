from typing import Callable
import functools


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    """ Декоратор для декораторов. Даёт возможность
    любому декоратору принимать произвольные аргументы.
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор: {} {}'.format(args, kwargs))
        return func

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Callable:
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
