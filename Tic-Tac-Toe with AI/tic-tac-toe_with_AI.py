import random

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
        try:
            coordinat = [int(x) for x in input('Enter the coordinates: ') if x != ' ']
            if coordinat[0] > 3 or coordinat[1] > 3:
                print('"Coordinates should be from 1 to 3!"')
                return 0
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
            if ceil[coordinat[1]][coordinat[0]] == ' ':
                if self.x_or_o == 'X':
                    self.ceil[coordinat[1]][coordinat[0]] = 'X'
                else:
                    self.ceil[coordinat[1]][coordinat[0]] = 'O'
            else:
                print('This cell is occupied! Choose another one!')
                return 0
        except ValueError:
            print("You should enter numbers!")
            return 0

    def maove_ai(self):


    def chek_wins(self):
        for i in range(0, 3):
            if self.ceil[i][0] == self.ceil[i][1] == self.ceil[i][2]:
                if self.ceil[i][0] != ' ':
                    return f'{self.ceil[i][0]} wins'
            if self.ceil[0][i] == self.ceil[1][i] == self.ceil[2][i]:
                if self.ceil[0][i] != ' ':
                    return f'{self.ceil[0][i]} wins'
            if self.ceil[0][0] == self.ceil[1][1] == self.ceil[2][2]:
                if self.ceil[0][0] != ' ':
                    return f'{self.ceil[0][0]} wins'
            if self.ceil[0][2] == self.ceil[1][1] == self.ceil[2][0]:
                if self.ceil[0][2] != ' ':
                    return f'{self.ceil[0][2]} wins'
        return 0

    def draw(self):
        count = 0
        for i in self.ceil:
            for j in i:
                if j == ' ':
                    count += 1
        if count == 0:
            return "Draw"
        return 0

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
    # start_ceil = input("Enter cells: ")
    # if start_ceil.count('X') > start_ceil.count('O'):
    #     x_or_o = 'O'
    # else:
    #     x_or_o = 'X'
    game = TicTacToe(start_ceil, x_or_o, ceil)
    game.start_game()
    game.print_ceil()
    while game.chek_wins() == 0:
        user_move = game.user_move()
        ai_move = game.maove_ai()
        draw = game.draw()
        chek_wins = game.chek_wins()
        if draw == 0:
            if chek_wins != 0:
                game.print_ceil()
                print(chek_wins)
            elif move != 0:
                game.print_ceil()
                print('Game not finished')
                break
        elif draw != 0:
            game.print_ceil()
            print(draw)
            break




