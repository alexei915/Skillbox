class Water:

    def __init__(self):
        self.name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            print('{} + {} = {}'.format(self.name, other.name, Storm().name))
            return Storm()
        if other.name == 'Огонь':
            print('{} + {} = {}'.format(self.name, other.name, Steam().name))
            return Steam()
        if other.name == 'Земля':
            print('{} + {} = {}'.format(self.name, other.name, Mud().name))
            return Mud()


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Вода':
            print('{} + {} = {}'.format(self.name, other.name, Alcohol().name))
            return Alcohol()
        if other.name == 'Энергия':
            print('{} + {} = {}'.format(self.name, other.name, Energy().name))
            return Energy()
        if other.name == 'Земля':
            print('{} + {} = {}'.format(self.name, other.name, Lava().name))
            return Lava()


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Огонь':
            print('{} + {} = {}'.format(self.name, other.name, Lightning().name))
            return Lightning()
        if other.name == 'Вода':
            print('{} + {} = {}'.format(self.name, other.name, Steam().name))
            return Steam()
        if other.name == 'Земля':
            print('{} + {} = {}'.format(self.name, other.name, Dust().name))
            return Dust()


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if other.name == 'Огонь':
            print('{} + {} = {}'.format(self.name, other.name, Lava().name))
            return Lava()


class Storm:

    def __init__(self):
        self.name = 'Шторм'


class Steam:

    def __init__(self):
        self.name = 'Пар'


class Mud:

    def __init__(self):
        self.name = 'Грязь'


class Lightning:

    def __init__(self):
        self.name = 'Молния'


class Dust:

    def __init__(self):
        self.name = 'Пыль'


class Lava:

    def __init__(self):
        self.name = 'Лава'


class Alcohol:

    def __init__(self):
        self.name = 'Спирт'


class Energy:

    def __init__(self):
        self.name = 'Энергия'

