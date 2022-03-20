class Parent:
    children = []

    def __init__(self, parent_name, parent_age):
        self.parent_name = parent_name
        self.parent_age = parent_age

    def calm_kid(self):
        for i_state in self.children:
            if i_state.state_of_calm == 2:
                i_state.state_of_calm = 1
        print('Теперь дети спокойны!\n')

    def feed_kid(self):
        for i_state in self.children:
            if i_state.state_of_hunger == 2:
                i_state.state_of_hunger = 1
        print('Дети накормлены и сыты!\n')

    def print_info(self):
        print('Name: {}\nAge: {}\nKids:'.format(
            self.parent_name, self.parent_age))
        for i_info in self.children:
            i_info.print_info_2()


class Kid:
    states_of_calm = {1: 'Спокоен', 2: 'Плачет'}
    states_of_hunger = {1: 'Сыт', 2: 'Голоден'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_of_calm = 2
        self.state_of_hunger = 2
        if parent_1.parent_age - self.age < 16:
            print('Ошибка! Разница должна быть менее 16 лет')
        else:
            Parent.children.append(self)

    def print_info_2(self):
        print('\tName: {}\n\tAge: {}\n\tA state of calm: {}\n\tThe state of hunger: {}\n'.format(
            self.name, self.age, Kid.states_of_calm[self.state_of_calm],
            Kid.states_of_hunger[self.state_of_hunger]
        ))


parent_1 = Parent('Dima', 28)
kids_1 = Kid('Nastya', 15)
kids_2 = Kid('Lena', 2)

parent_1.print_info()
parent_1.calm_kid()
parent_1.feed_kid()

parent_1.print_info()
