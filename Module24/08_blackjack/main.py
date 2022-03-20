import random


class Card:
    price_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
                    9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self, suits, rank):
        self.suits = suits
        self.rank = rank
        self.value = self.price_values[self.rank]


class Deck:

    def __init__(self):
        suits = 'Spade', 'Heart', 'Club', 'Diamond'
        rank = 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'
        self.deck = [Card(elem, elem_2) for elem in suits for elem_2 in rank]

    def distribution(self):
        card = self.deck.pop(random.randint(0, len(self.deck) - 1))
        return card


class Player:

    def __init__(self, name, game_deck):
        self.name = name
        self.game_deck = game_deck
        self.cards_on_hand = [self.game_deck.distribution(), self.game_deck.distribution()]
        self.points = sum([i.value for i in self.cards_on_hand])

    def game(self):
        new_card = self.game_deck.distribution()
        self.cards_on_hand.append(new_card)
        if new_card.rank == 'A' and self.points > 10:
            self.points += 1
        else:
            self.points += new_card.value

    def print_info(self):
        print('Player: {}.\nCards on hand: {}.\nPoints: {}.\n'.format(
            self.name, [str(i.rank) + ': ' + i.suits for i in self.cards_on_hand], self.points
        ))


my_deck = Deck()
player_1 = Player('Nastya', my_deck)
player_2 = Player('Comp', my_deck)


while True:
    player_1.print_info()
    action = input('\nВыберите действие:\n1.Взять карту\n2.Остановиться\n')
    while 21 - player_2.points > 4:
        player_2.game()
    if action == '1':
        player_1.game()
        if player_1.points > 21:
            player_1.print_info()
            print('Перебор! Вы проиграли.')
            break
    elif action == '2':
        if player_1.points > player_2.points or player_2.points - 21 > 0:
            print('Вы победили!')
            player_2.print_info()
            break
        elif player_2.points > player_1.points:
            print('Вы проиграли!')
            player_2.print_info()
            break
        else:
            print('Ничья.')
            player_2.print_info()
            break
    else:
        print('Ошибка ввода!')