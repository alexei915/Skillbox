import random


class Human:

    def __init__(self, name, house):
        self.name = name
        self.state_of_hunger = 50
        self.house = house

    def eat(self):
        if self.house.fridge < 10:
            self.state_of_hunger -= 10
            print('Еда закончилась! Сытость уменьшается!')
        else:
            self.state_of_hunger += 20
            self.house.fridge -= 10
            print('{} покушал. Сытость - {}. Еды осталось - {}.\n'.format(
                self.name, self.state_of_hunger, self.house.fridge
            ))

    def work(self):
        self.state_of_hunger -= 10
        self.house.money += 20
        print('{} поработал. Теперь денег – {}.\n'.format(
            self.name, self.house.money))

    def game(self):
        self.state_of_hunger -= 10
        print('{} поиграл.\n'.format(self.name))

    def go_to_store(self):
        self.house.fridge += 40
        self.house.money -= 25
        print('{} сходил в магазин. Теперь еды - {}. Денег осталось – {}.\n'.format(
            self.name, self.house.fridge, self.house.money
        ))


class House:

    def __init__(self):
        self.fridge = 50
        self.money = 0


def actions(human):
    if human.state_of_hunger < 20:
        human.eat()
    elif human.house.fridge < 10:
        human.go_to_store()
    elif human.house.money < 50:
        human.work()
    elif number == 1:
        human.work()
    elif number == 2:
        human.eat()
    else:
        human.game()


my_house = House()
my_human = Human('Alex', my_house)
my_human_2 = Human('Nikita', my_house)

day = 0

while day != 365:
    day += 1
    print('День {}-ый.'.format(day))
    number = random.randint(1, 6)
    if my_human.state_of_hunger < 0 or my_human_2.state_of_hunger < 0:
        print('{} умер на {}-й день...'.format(my_human.name, day))
        break
    actions(my_human)
    actions(my_human_2)

