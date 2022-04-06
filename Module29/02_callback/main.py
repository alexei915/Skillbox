from typing import Callable, Optional, Any
import functools


app = {}


def callback(value: Optional[Any] = None) -> Callable:

    def decorate(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            app[value] = func

        return wrapped_func()
    return decorate


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
