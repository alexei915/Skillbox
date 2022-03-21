import random


class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, unit):
        unit.health -= 20


unit_1 = Warrior('Lis')
unit_2 = Warrior('Borland')

while unit_1.health > 0 and unit_2.health > 0:
    result = random.choice([unit_1, unit_2])
    if result == unit_1:
        unit_1.hit(unit_2)
        print("Юнит Borland атаковал юнита Lis. У Lis'a осталось {} HP".format(unit_2.health))
    elif result == unit_2:
        unit_2.hit(unit_1)
        print("Юнит Lis атаковал юнита Borland. У Borland'a осталось {} HP".format(unit_1.health))
if unit_1.health == 0:
    print('\nПобедил Lis')
else:
    print('\nПобедил Borland')
