import math


class Car:

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir / 57.2958

    def __str__(self):
        return 'Координаты: {}, {}.'.format(self.x, self.y)

    def move(self, distance):
        self.x += distance * math.cos(self.dir)
        self.y += distance * math.sin(self.dir)


class Bus(Car):

    def __init__(self, x, y, dir):
        super().__init__(x, y, dir)
        self.passenger = 0
        self.money = 0

    def go_in(self, count):
        if self.passenger < 90:
            self.passenger += count
            print('Вошло {} пассажиров. Всего в автобусе: {} пассажиров.'.format(
                count, self.passenger
            ))
        else:
            print('Автобус переполнен!')

    def go_out(self, count):
        if self.passenger >= count:
            self.passenger -= count
            print('Вышли {} пассажиров. Всего в автобусе: {} пассажиров.'.format(
                count, self.passenger
            ))
        else:
            print('В автобусе нет столько людей!')

    def move(self, distance):
        self.money += distance * self.passenger * 0.4
        print('Проехал {} километров. Сейчас денег – {}.'.format(
            distance, self.money
        ))


my_car = Car(1, 10, 180)
my_car.move(100)
print(my_car)

my_bus = Bus(1, 10, 90)
my_bus.go_in(15)
my_bus.go_out(3)
my_bus.move(15)
