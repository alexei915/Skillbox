from collections.abc import Iterable, Iterator

# Вариант 1. Класс-итератор
# class MyIterator:
#     """Класс-итератор квадратов чисел от 1 до N"""
#     def __init__(self, number: int) -> None:
#         self.__counter = 0
#         self.number = number
#
#     def __iter__(self) -> Iterator:
#         self.__counter = 0
#         return self
#
#     def __next__(self) -> int:
#         self.__counter += 1
#         if self.__counter > self.number:
#             raise StopIteration
#         return self.__counter ** 2
#
#
# seq = MyIterator(5)
# for num in seq:
#     print(num, end=' ')


# Вариант 2. Функция генератор
# def gen_square(last_num: int) -> Iterable[int]:
#     for number in range(1, last_num + 1):
#         yield number ** 2
#
#
# digits = int(input('Введите число: '))
# for square_num in gen_square(digits):
#     print(square_num, end=' ')


# Вариант 3. Генераторное выражение
# digits = int(input('Введите число: '))
# gen_square = (num ** 2 for num in range(1, digits + 1))
#
# for square_num in gen_square:
#     print(square_num, end=' ')
