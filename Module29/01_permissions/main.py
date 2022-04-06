from typing import Callable, Optional
import functools

user_permissions = ['admin']


def check_permission(permission: Optional[str] = None) -> Callable:

    def decorate(func: Callable) -> Callable:
        """ Декоратор. Проверяет, есть ли у пользователя
        доступ к вызываемой функции
        """

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Callable:
            try:
                if permission == user_permissions[0]:
                    return func(*args, **kwargs)
                raise PermissionError(
                    'У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(func.__name__))
            except PermissionError as exp:
                print('PermissionError: {}'.format(exp))

        return wrapped_func
    return decorate


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
