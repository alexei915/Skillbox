from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """ Декоратор. При вызове декорируемой функции спрашивает
    у пользователя “Как дела?”, отвечает “А у меня не очень!” и
    только потом запускает саму функцию.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        question = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def is_palindrome(word: str) -> None:
    """ Функция, проверяющая, является ли
    передаваемая в неё строка палиндромом

     :return: None
     """
    if word == word[::-1]:
        print('Слово {} является палиндромом.'.format(word))
    else:
        print('Слово {} не является палиндромом.'.format(word))


@how_are_you
def is_prime(number: int) -> None:
    """ Функция, проверяющая, является ли
        передаваемое в неё число простым

    :return: None
    """
    flag = True
    for divider in range(2, number):
        if number % divider == 0:
            flag = False
    if flag:
        print('Число {} - простое.'.format(number))
    else:
        print('Число {} - составное.'.format(number))


is_palindrome('мадам')
is_prime(13)
