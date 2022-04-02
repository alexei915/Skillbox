import math


class MyMath:
    """ Класс «MyMath». Позволяет осуществлять
     различные вычисления, связанные с фигурами
    """

    @classmethod
    def circle_len(cls, radius: float) -> float:
        length = 2 * radius * math.pi
        return length

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        square = math.pi * radius ** 2
        return square

    @classmethod
    def cube_volume(cls, edge_length: float) -> float:
        volume = 6 * edge_length ** 2
        return volume

    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        square = 4 * math.pi * radius ** 2
        return square


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)