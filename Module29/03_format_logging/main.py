import time
from typing import Callable, Optional
import functools
from datetime import datetime


def timer(cls, func: Callable, date_format: str) -> Callable:

    @functools.wraps(cls)
    def wrapped_func(*args, **kwargs) -> Callable:
        new_format = date_format
        for sym in date_format:
            if sym.isalpha():
                new_format = new_format.replace(sym, '%' + sym)

        print('Запускается {}. Дата и время запуска: {}'.format(
            cls.__name__ + '.' + func.__name__, datetime.strftime(datetime.now(), new_format)))
        start = time.time()
        result = func(*args, **kwargs)
        run_time = time.time() - start
        print('Завершение {}, время работы = {}s '.format(
            cls.__name__ + '.' + func.__name__, round(run_time, 5)))

        return result
    return wrapped_func


def log_methods(date_format: Optional[str] = None):

    def wrapped_func(cls):
        for i_methods_name in dir(cls):
            if not i_methods_name.startswith('__'):
                current_method = getattr(cls, i_methods_name)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, i_methods_name, decorated_method)

        return cls
    return wrapped_func


@log_methods("b d Y - H:M:S")
class A:

    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):

    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника")

    def test_sum_2(self) -> int:
        print("Тут метод test sum 2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()