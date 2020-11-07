from random import randint


class Game:
    def __init__(self, x, o):
        self.first = x
        self.second = o
        self.ceil = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]

    def start_game(self):
        save_ceil = self.ceil
        self.print_ceil()
        while self.chek_wins() == 0 and self.draw() == 0:
            first_chek = self.first.move(self.ceil)
            if first_chek == 1:
                while first_chek == 1:
                    self.ceil = save_ceil
                    self.print_ceil()
                    first_chek = self.first.move(self.ceil)
                save_ceil = self.ceil
                self.print_ceil()
            else:
                self.ceil = first_chek
                self.print_ceil()
                save_ceil = self.ceil
            if self.chek_wins() != 0 or self.draw() != 0:
                self.wins()
            second_check = self.second.move(self.ceil)
            if second_check == 1:
                while second_check == 1:
                    self.ceil = save_ceil
                    self.print_ceil()
                    second_check = self.second.move(self.ceil)
                save_ceil = self.ceil
                self.print_ceil()
            else:
                self.ceil = second_check
                self.print_ceil()
                save_ceil = self.ceil
            if self.chek_wins() != 0 or self.draw() != 0:
                self.wins()

    def wins(self):
        if self.chek_wins() != 0:
            print(self.chek_wins())
            menu()
        elif self.draw() != 0:
            print(self.draw())
            menu()

    def chek_wins(self):
        for i in range(0, 3):
            if self.ceil[i][0] == self.ceil[i][1] == self.ceil[i][2]:
                if self.ceil[i][0] != ' ':
                    return f'{self.ceil[i][0]} wins\n'
            if self.ceil[0][i] == self.ceil[1][i] == self.ceil[2][i]:
                if self.ceil[0][i] != ' ':
                    return f'{self.ceil[0][i]} wins\n'
            if self.ceil[0][0] == self.ceil[1][1] == self.ceil[2][2]:
                if self.ceil[0][0] != ' ':
                    return f'{self.ceil[0][0]} wins\n'
            if self.ceil[0][2] == self.ceil[1][1] == self.ceil[2][0]:
                if self.ceil[0][2] != ' ':
                    return f'{self.ceil[0][2]} wins\n'
        return 0

    def draw(self):
        count = 0
        for i in self.ceil:
            for j in i:
                if j == ' ':
                    count += 1
        if count == 0:
            return "Draw\n"
        return 0

    def print_ceil(self):
        print("---------")
        print('| {} {} {} |'.format(self.ceil[0][0], self.ceil[0][1], self.ceil[0][2]))
        print('| {} {} {} |'.format(self.ceil[1][0], self.ceil[1][1], self.ceil[1][2]))
        print('| {} {} {} |'.format(self.ceil[2][0], self.ceil[2][1], self.ceil[2][2]))
        print("---------")


class User:
    def __init__(self, move):
        self.moveing = move

    def move(self, ceil):
        count = 0
        try:
            coordinat = [int(x) for x in input('Enter the coordinates: ') if x != ' ']
            if coordinat[0] > 3 or coordinat[1] > 3:
                print('"Coordinates should be from 1 to 3!"')
                return 1
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
                ceil[coordinat[1]][coordinat[0]] = str(self.moveing)
                return ceil
            else:
                print('This cell is occupied! Choose another one!')
                return 1
        except ValueError:
            print("You should enter numbers!")
            return 1


class MediumAi:
    def __init__(self, move):
        self.moving = move

    def move(self, ceil):
        print('Making move level "medium"')
        chek_move = 0
        flag = 0
        ai_move = self.moving
        while chek_move < 2:
            for horizont in range(len(ceil)):
                if ceil[horizont].count(ai_move) == 2:
                    for i in range(len(ceil)):
                        if ceil[horizont][i] == ' ':
                            ceil[horizont][i] = self.moving
                            flag += 1
                            break
            if flag == 0:
                zip_ceil = []
                for i in zip(*ceil):
                    zip_ceil.append(list(i))
                for horizont in range(len(zip_ceil)):
                    if zip_ceil[horizont].count(ai_move) == 2:
                        for i in range(len(zip_ceil)):
                            if zip_ceil[horizont][i] == ' ':
                                zip_ceil[horizont][i] = self.moving
                                flag += 1
                                break
                ceil = [[], [], []]
                for i in range(len(zip_ceil)):
                    for j in range(len(zip_ceil)):
                        ceil[i].append(zip_ceil[j][i])

            if flag == 0:
                if (ceil[0][0] == ai_move and ceil[1][1] == ai_move) or (
                        ceil[0][0] == ai_move and ceil[2][2] == ai_move) \
                        or (ceil[2][2] == ai_move and ceil[1][1] == ai_move):
                    if ceil[0][0] == ' ':
                        ceil[0][0] = self.moving
                    elif ceil[1][1] == ' ':
                        ceil[1][1] = self.moving
                    elif ceil[2][2] == ' ':
                        ceil[2][2] = self.moving
                    flag += 1

            if flag == 0:
                if (ceil[0][2] == ai_move and ceil[1][1] == ai_move) or (
                        ceil[0][2] == ai_move and ceil[2][0] == ai_move) \
                        or (ceil[2][0] == ai_move and ceil[1][1] == ai_move):
                    if ceil[0][2] == ' ':
                        ceil[0][2] = self.moving
                    elif ceil[1][1] == ' ':
                        ceil[1][1] = self.moving
                    elif ceil[2][0] == ' ':
                        ceil[2][0] = self.moving
                    flag += 1
            if flag == 0:
                if ai_move == 'X':
                    ai_move = 'O'
                else:
                    ai_move = 'X'
                chek_move += 1
            else:
                break

        if flag == 0:
            loop = True
            while loop:
                x = randint(0, 2)
                y = randint(0, 2)
                if ceil[x][y] == ' ':
                    ceil[x][y] = self.moving
                    loop = False
        return ceil


class EasyAi:
    def __init__(self, move):
        self.moving = move

    def move(self, ceil):
        print('Making move level "easy"')
        loop = True
        while loop:
            x = randint(0, 2)
            y = randint(0, 2)
            if ceil[x][y] == ' ':
                ceil[x][y] = self.moving
                loop = False
        return ceil


def validation_input(command):
    if command[0] == 'exit':
        exit()
    if len(command) != 3:
        print('Bad parameters!')
        menu()
    return 0
    # if command[0] == 'start':
    #     count_users = command.count('user')
    #     count_ai = command.count('easy')
    #     if count_users == 1 and count_ai == 1:
    #         return 0
    #     elif count_users == 2 or count_ai == 2:
    #         return 0
    #     else:
    #         return 1


def menu():
    x = ''
    o = ''
    try:
        command = input('Input command: ').split()
        validation = validation_input(command)
        if validation == 0:
            if command[1] == 'user':
                x = User('X')
            elif command[1] == "easy":
                x = EasyAi('X')
            elif command[1] == 'medium':
                x = MediumAi('X')
            if command[2] == 'user':
                o = User('O')
            elif command[2] == "easy":
                o = EasyAi('O')
            elif command[2] == 'medium':
                o = MediumAi('O')
            game = Game(x, o)
            game.start_game()
    except IndexError:
        print('Bad parameters!')
        menu()
    except NameError:
        print('Bad parameters!')
        menu()


if __name__ == '__main__':
    menu()
