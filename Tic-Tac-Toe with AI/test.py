class TicTacToe:

    def __init__(self, start_ceil, x_or_o, ceil):
        self.ceil = ceil
        self.start_ceil = start_ceil
        self.x_or_o = x_or_o

    def start_game(self):
        for i in range(len(self.ceil)):
            for j in range(len(self.ceil)):
                if self.start_ceil[j] == '_':
                    self.ceil[i][j] = ' '
                else:
                    self.ceil[i][j] = self.start_ceil[j]
            self.start_ceil = self.start_ceil[3:]

    def user_move(self):
        count = 0
        coordinat = [int(x) for x in input('Enter the coordinates: ') if x != ' ']
        for i in range(len(coordinat)):
            if count == 0:
                coordinat[i] -= 1
            else:
                if coordinat[i] == 1:
                    coordinat[i] = 2
                elif coordinat[i] == 2:
                    coordinat[i] = 1
                else:
                    coordinat[i] = 0
            count += 1
        print(coordinat)
        if ceil[coordinat[1]][coordinat[0]] == ' ':
            if self.x_or_o == 'X':
                self.ceil[coordinat[1]][coordinat[0]] = 'X'
            else:
                self.ceil[coordinat[1]][coordinat[0]] = 'O'
        else:
            print('This cell is occupied! Choose another one!')

    def chek_wins(self):
        for i in range(0, 3):
            if ceil[i][0] == ceil[i][1] == ceil[i][2]:
                if ceil[i][0] != ' ':
                    return f'{ceil[i][0]} wins'
            if ceil[0][i] == ceil[1][i] == ceil[2][i]:
                if ceil[0][i] != ' ':
                    return f'{ceil[0][i]} wins'
            if ceil[0][0] == ceil[1][1] == ceil[2][2]:
                if ceil[0][0] != ' ':
                    return f'{ceil[0][0]} wins'
            if ceil[0][2] == ceil[1][1] == ceil[2][0]:
                if ceil[0][2] != ' ':
                    return f'{ceil[0][0]} wins'
        return 0


class PrintCeil(TicTacToe):

    def print_ceil(self):
        print("---------")
        print('| {} {} {} |'.format(self.ceil[0][0], self.ceil[0][1], self.ceil[0][2]))
        print('| {} {} {} |'.format(self.ceil[1][0], self.ceil[1][1], self.ceil[1][2]))
        print('| {} {} {} |'.format(self.ceil[2][0], self.ceil[2][1], self.ceil[2][2]))
        print("---------")


if __name__ == '__main__':
    ceil = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]
    start_ceil = input("Enter cells: ")
    if start_ceil.count('X') > start_ceil.count('O'):
        x_or_o = 'O'
    else:
        x_or_o = 'X'
    # game = TicTacToe(start_ceil, x_or_o, ceil)
    prit = PrintCeil(start_ceil, x_or_o, ceil)
    prit.start_game()
    prit.user_move()
    prit.print_ceil()
    # game.start_game()
    # game.print_ceil()
    # game.user_move()
    # game.print_ceil()
    # if game.chek_wins() != 0:
