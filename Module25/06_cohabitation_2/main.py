import random


class Humans:

    def __init__(self, name, house):
        self.set_name(name)
        self.satiety = 30
        self.happiness = 100
        self.house = house
        self.amount_food = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно состоять только из букв.')

    def earn(self):
        food_count = random.randint(10, 30)
        self.amount_food += food_count
        self.satiety += food_count
        self.house.humans_food -= food_count
        print('{} покушал. Степень сытости - {}. Еды осталось - {}.\n'.format(
            self.__name, self.satiety, self.house.humans_food
        ))

    def petting_cat(self):
        self.satiety -= 10
        self.happiness += 5
        print('{} погладил(а) кота. Степень счастья - {}.\n'.format(
            self.__name, self.happiness
        ))


class Husband(Humans):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.amount_money = 0

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print('{} поиграл в компьютер. Уровень счастья - {}.\n'.format(self.get_name(), self.happiness))

    def work(self):
        self.house.money += 150
        self.amount_money += 150
        self.satiety -= 10
        print('{} поработал. Денег в тумбочке - {}. Степень сытости - {}.\n'.format(
            self.get_name(), self.house.money, self.satiety
        ))


class Wife(Humans):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.amount_coat = 0

    def buy_groceries(self):
        if self.house.money > 80:
            self.house.humans_food += 60
            self.house.cat_food += 20
            self.house.money -= 80
            self.satiety -= 10
        else:
            self.house.humans_food += 20
            self.house.cat_food += 10
            self.house.money -= 30
            self.satiety -= 10
        print('{} сходила в магазин. Теперь еды в доме - {}. Кошачьей еды - {}.\n'.format(
            self.get_name(), self.house.humans_food, self.house.cat_food
        ))

    def buy_coat(self):
        self.house.money -= 150
        self.happiness += 60
        self.satiety -= 10
        self.amount_coat += 1
        print('{} сходила в магазин. Теперь у жены есть (ещё одна) шуба.\n'.format(
            self.get_name()
        ))

    def cleaning(self):
        if self.house.dirt_count <= 100:
            self.house.dirt_count -= self.house.dirt_count
            self.satiety -= 10
            print('{} убралась в квартире. Теперь абсолютно чисто!\n'.format(self.get_name()))
        else:
            self.house.dirt_count -= 100
            print('{} убралась. Грязи осталось - {}.\n'.format(self.get_name(), self.house.dirt_count))


class Cat:

    def __init__(self, name, house):
        self.set_name(name)
        self.satiety = 30
        self.house = house
        self.amount_food = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно состоять только из букв.')

    def earn(self):
        food_count = random.randint(1, 10)
        self.satiety += food_count * 2
        self.house.cat_food -= food_count
        self.amount_food += food_count
        print('{} покушал. Степень сытости - {}. Еды осталось - {}.\n'.format(
            self.__name, self.satiety, self.house.cat_food
        ))

    def sleep(self):
        self.satiety -= 10
        print('{} поспал.\n'.format(self.__name))

    def tear_up_wallpaper(self):
        self.house.dirt_count += 5
        self.satiety -= 10
        print('{} поточил когти об обои. Грязи прибавилось, теперь - {}.\n'.format(
            self.__name, self.house.dirt_count
        ))


class House:

    def __init__(self):
        self.money = 100
        self.humans_food = 50
        self.cat_food = 30
        self.dirt_count = 0


def actions_husband(human):
    if human.satiety < 20:
        human.earn()
    elif human.happiness < 30:
        human.game()
    elif human.house.money < 300:
        human.work()
    else:
        human.petting_cat()


def actions_wife(human):
    if human.satiety < 30:
        human.earn()
    elif human.house.humans_food < 60 or human.house.cat_food < 40:
        human.buy_groceries()
    elif human.house.money > 300:
        human.buy_coat()
    elif human.house.dirt_count > 90:
        human.cleaning()
    else:
        human.petting_cat()


def actions_cat(pet):
    if pet.satiety < 20:
        pet.earn()
    elif pet.house.dirt_count < 120:
        pet.tear_up_wallpaper()
    else:
        pet.sleep()


my_house = House()
alex = Husband('Alexei', my_house)
nastya = Wife('Nastya', my_house)
markiz = Cat('Markiz', my_house)
day = 0


while day != 365:
    day += 1
    print('День {}.\n'.format(day))
    if my_house.dirt_count > 90:
        alex.happiness -= 10
        nastya.happiness -= 10
        print('Дом сильно загрязнён. Уровень счастья падает!\n')
    my_house.dirt_count += 5
    actions_husband(alex)
    actions_wife(nastya)
    actions_cat(markiz)
    if alex.happiness < 10 or nastya.happiness < 10 or alex.satiety < 0 or nastya.satiety < 0 or markiz.satiety < 0 or \
            my_house.money < 0 or my_house.humans_food < 0 or my_house.cat_food < 0:
        break


total_money = alex.amount_money
total_coat = nastya.amount_coat
total_food = alex.amount_food + nastya.amount_food + markiz.amount_food
print('Итоги за год:\n1. Съедено еды - {} ед.\n2. Заработано денег - {}.\n3. Куплено шуб - {}.'.format(
    total_food, total_money, total_coat
))