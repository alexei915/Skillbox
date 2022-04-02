from abc import ABC, abstractmethod
from typing import Any
import math


class Figure(ABC):

    """ Абстрактный базовый класс Фигура.

     Args and attrs:
     figure_name (str): название фигуры
     """

    def __init__(self, figure_name: str) -> None:
        self.figure_name = figure_name

    @abstractmethod
    def show_name(self):
        print(self.figure_name)


class Square(Figure, ABC):
    """ Квадрат. Родитель: абстрактный базовый класс Фигура

    Args and attrs:
    side_len (int) : сторона квадрата
    """

    def __init__(self, side_len: int) -> None:
        super().__init__('Квадрат')
        self.side_len = side_len

    @property
    def side_len(self):
        return self._side_len

    @side_len.setter
    def side_len(self, side_len):
        if not isinstance(side_len, int):
            raise Exception('Ошибка. Длина стороны должна быть целым числом.')
        else:
            self._side_len = side_len

    def get_perimeter(self) -> int:
        perimeter = self._side_len * 4
        return perimeter

    def get_square(self) -> int:
        square = self._side_len ** 2
        return square

    def show_name(self) -> None:
        print(self.figure_name)


class Triangle(Figure, ABC):
    """ Треугольник. Родитель: абстрактный базовый класс Фигура

    Args and attrs:
    base (int) : основание треугольника
    height (int) : высота треугольника
    """

    def __init__(self, base: int, height: int) -> None:
        super().__init__('Треугольник')
        self.base = base
        self.height = height

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, base: int) -> Any:
        if not isinstance(base, int):
            raise Exception('Ошибка. Длина основания должна быть целым числом.')
        else:
            self._base = base

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> Any:
        if not isinstance(height, int):
            raise Exception('Ошибка. Высота должна быть целым числом.')
        else:
            self._height = height

    def get_perimeter(self) -> float:
        side_triangle = math.sqrt(self._height ** 2 + (self._base / 2) ** 2)
        perimeter = self._base + 2 * side_triangle
        return perimeter

    def get_square(self) -> float:
        square = self._base / 2 * self._height
        return square

    def show_name(self) -> None:
        print(self.figure_name)


class Cube(Square):
    """ Куб. Родитель: базовый класс Квадрат

     Args and attrs:
     side_len (int) : сторона куба
     cube (list) : поверхность куба в виде списка квадратов
     """

    def __init__(self, side_len: int):
        super().__init__(side_len)
        self.cube = [Square(side_len), Square(side_len), Square(side_len), Square(side_len), Square(side_len),
                     Square(side_len), Square(side_len), Square(side_len)]

    def surface_square(self) -> int:
        square = sum(area.get_square() for area in self.cube)
        return square


class Pyramid(Triangle):
    """ Пирамида. Родители: базовый класс Треугольник

     Args and attrs:
     base (int) : основание пирамиды
     height (int) : высота пирамиды
     pyramid (list) : поверхность пирамиды в виде списка треугольников
     """

    def __init__(self, base: int, height: int) -> None:
        super().__init__(base, height)
        self.pyramid = [Triangle(base, height), Triangle(base, height), Triangle(base, height),
                        Triangle(base, height)]

    def surface_pyramid(self) -> int:
        square = sum(area.get_square() for area in self.pyramid) + self.base ** 2
        return square


my_cube = Cube(5)
print(my_cube.surface_square())
my_pyramid = Pyramid(6, 10)
print(my_pyramid.surface_pyramid())
