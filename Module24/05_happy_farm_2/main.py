class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} уже {}.'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
        self.state_care = 'Не ухожена'

    def grow_all(self):
        if self.state_care == 'Не ухожена':
            print('Грядка не ухожена! Для роста картошки садовнику нужно её обработать.')
            return False
        print('Картошка прорастает!\n')
        for i_potato in self.potatoes:
            i_potato.grow()
        return True

    def all_is_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
        else:
            print('Картошка созрела! Можно собирать урожай.')


class Gardener:
    harvest = []

    def __init__(self, name, potato_garden):
        self.name = name
        self.potato_garden = potato_garden

    def care(self):
        print('Садовник {} обрабатывает грядку'.format(self.name))
        if self.potato_garden.state_care == 'Не ухожена':
            self.potato_garden.state_care = 'Ухожена'
            print('Грядка обработана. Теперь картофель будет расти!')
        else:
            print('Грядка уже ухожена!')

    def harvesting(self):
        for i_potato in self.potato_garden.potatoes:
            if i_potato.state == 3:
                self.harvest.append(i_potato.index)
            else:
                print('Картошка ещё не созрела. Рано собирать...')
                break
        else:
            print('\nУрожай собран. Итого картошки - {} штук.'.format(len(self.harvest)))


my_garden = PotatoGarden(5)

for _ in range(3):
    if my_garden.grow_all():
        my_garden.all_is_ripe()
    else:
        break

my_gardener = Gardener('Vasiliy', my_garden)
my_gardener.care()

for _ in range(3):
    if my_garden.grow_all():
        my_garden.all_is_ripe()

my_gardener.harvesting()
