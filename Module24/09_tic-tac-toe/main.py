class Cell:

    def __init__(self, cell_number):
        self.is_busy = False
        self.cell_number = cell_number
        self.value = None


class Board:

    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]

    def print_board(self, index=None, value=None, x=[i for i in range(1, 10)]):
        if value == 'cross':
            x[index - 1] = 'X'
        elif value == 'zero':
            x[index - 1] = 'O'
        print('{:–^28}'.format(''))
        print('|{: ^8}|{: ^8}|{: ^8}|'.format(x[0], x[1], x[2]))
        print('{:-^28}'.format(''))
        print('|{: ^8}|{: ^8}|{: ^8}|'.format(x[3], x[4], x[5]))
        print('{:–^28}'.format(''))
        print('|{: ^8}|{: ^8}|{: ^8}|'.format(x[6], x[7], x[8]))
        print('{:–^28}'.format(''))
        if (str(x[0]) + str(x[1]) + str(x[2]) == 'XXX') or (str(x[0]) + str(x[3]) + str(x[6]) == 'XXX') or \
           (str(x[3]) + str(x[4]) + str(x[5]) == 'XXX') or (str(x[1]) + str(x[4]) + str(x[7]) == 'XXX') or \
           (str(x[6]) + str(x[7]) + str(x[8]) == 'XXX') or (str(x[2]) + str(x[5]) + str(x[8]) == 'XXX') or \
           (str(x[0]) + str(x[4]) + str(x[8]) == 'XXX') or (str(x[2]) + str(x[4]) + str(x[6]) == 'XXX'):
            return True
        elif (str(x[0]) + str(x[1]) + str(x[2]) == 'OOO') or (str(x[0]) + str(x[3]) + str(x[6]) == 'OOO') or \
           (str(x[3]) + str(x[4]) + str(x[5]) == 'OOO') or (str(x[1]) + str(x[4]) + str(x[7]) == 'OOO') or \
           (str(x[6]) + str(x[7]) + str(x[8]) == 'OOO') or (str(x[2]) + str(x[5]) + str(x[8]) == 'OOO') or \
           (str(x[0]) + str(x[4]) + str(x[8]) == 'OOO') or (str(x[2]) + str(x[4]) + str(x[6]) == 'OOO'):
            return True


class Player:

    def __init__(self, name, symbol, board_game):
        self.name = name
        self.symbol = symbol
        self.board_game = board_game

    def running(self, cell):
        if not self.board_game.board[cell - 1].is_busy:
            self.board_game.board[cell - 1].is_busy = True
            self.board_game.board[cell - 1].value = self.symbol
            if self.board_game.print_board(cell, self.symbol):
                return True
        else:
            print('Клетка занята!')

    def game(self):
        answer = input('Игрок {}. Ваш ход: '.format(self.name))
        if not self.board_game.board[int(answer) - 1].is_busy:
            return self.running(int(answer))
        print('Клетка {} занята!'.format(answer))
        return self.game()


my_board = Board()
player_1 = Player('Alex', 'cross', my_board)
player_2 = Player('Nikita', 'zero', my_board)

my_board.print_board()
while True:
    if player_1.game():
        print('Победил {}!.'.format(player_1.name))
        break
    if player_2.game():
        print('Победил {}!.'.format(player_2.name))
        break
