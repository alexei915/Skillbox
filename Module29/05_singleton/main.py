import functools


def singleton(cls):
    """ Декоратор класса. Превращает класс в
    синглтон (имеет один инстанс).
    """

    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        pass
    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
