import math


class Circle:

    def __init__(self, radius, x=0, y=0):
        self.radius = radius
        self.x = x
        self.y = y

    def area_circle(self):
        area = math.pi * self.radius ** 2
        return area

    def perimeter_circle(self):
        perimeter = 2 * self.radius * math.pi
        return perimeter

    def increase(self, k):
        self.radius *= k

    def intersection(self, circle):
        distance = math.sqrt((circle.x - self.x) ** 2 + (circle.y + self.y) ** 2)
        summ_r = self.radius + circle.radius
        if summ_r >= distance >= abs(self.radius - circle.radius):
            return True
        return False


circle_1 = Circle(5)
circle_2 = Circle(5, 8, 7)
print(circle_1.area_circle(), circle_1.perimeter_circle())
print(circle_1.intersection(circle_2))
