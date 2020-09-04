import random


def game(user_move, score):
    paper = "paper"
    rock = "rock"
    scissors = "scissors"
    computer = (paper, rock, scissors)
    computer = random.choice(computer)
    while user_move != "!exit":
        if user_move == "!rating":
            print(f'Your rating: {score}')
        if computer == user_move:
            score += 50
            print(f"There is a draw {computer}")
        if user_move == paper and computer == scissors or \
                user_move == rock and computer == paper or \
                user_move == scissors and computer == rock:
            print(f"Sorry, but computer chose {computer}")
        elif user_move == paper and computer == rock or \
                user_move == rock and computer == scissors or \
                user_move == scissors and computer == paper:
            score += 100
            print(f"Well done. Computer chose {computer} and failed")
        menu(score)


def long_game(user_move, score):
    tmp = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper',
           'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
    computer_move = random.choice(user_move)
    while user_move != '!exit':
        user_move = input()
        if user_move == "!rating":
            print(f'Your rating: {score}')
        if not valid(user_move):
            print("Invalid input")
        if computer_move == user_move:
            score += 50
            print(f"There is a draw {computer_move}")
        else:
            user_find = tmp.index(user_move)
            computer_find = tmp.index(computer_move)
            user_find += 7
            computer_find += 7
            win = user_find - computer_find
            if abs(win) >= 7:
                score += 100
                print(f"Well done. Computer chose {computer_move} and failed")
            else:
                print(f"Sorry, but computer chose {computer_move}")
    menu(score)


def valid(user_move):
    tmp = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human',
           'snake', 'scissors', 'fire', '', '!exit', '!rating']
    user_move = user_move.split(',')
    count = 0
    for i in user_move:
        if i in tmp:
            count += 1
    if count != len(user_move):
        return 0
    else:
        return 1


def read_rating(user_name):
    f = open('rating.txt', 'r')
    tmp = f.read().split()
    count = 0
    score = 0
    if user_name in tmp:
        for i in tmp:
            if i == user_name:
                count += 1
                break
            count += 1
        if count > 0:
            score = int(tmp[count])
    return score


def hello():
    user_name = input("Enter your name:")
    print(f"Hello, {user_name}")
    main(user_name)


def start_game(user_name):
    global flag
    score = read_rating(user_name)
    if flag == 0:
        print("Okay, let's start")
    flag = 1
    return score


def menu(score):
    user_move = input()
    while True:
        if user_move == "!exit":
            print("Bye!")
            exit()
        if not valid(user_move):
            print("Invalid input")
        tmp = user_move.split()
        if len(tmp) > 1:
            long_game(user_move, score)
        else:
            game(user_move, score)


def main(user_name):
    global flag
    user_first_move = input()
    if user_first_move == "!exit":
        print("Bye!")
        exit()
    if not valid(user_first_move):
        print("Invalid input")
    else:
        score = start_game(user_name)
        menu(score)


flag = 0
hello()
