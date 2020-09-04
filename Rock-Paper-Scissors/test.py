# import random
#
#
# class Bad_computer:
#     user_move = 0
#     paper = "paper"
#     rock = "rock"
#     scissors = "scissors"
#     computer_move = (paper, rock, scissors)
#
#     def __init__(self):
#         self.user_move = input()
#
#     def game(self):
#         while self.user_move != "!exit":
#             self.computer_move = random.choice(self.computer_move)
#             if self.computer_move == self.user_move:
#                 print(f"There is a draw {self.computer_move}")
#             if self.user_move == self.paper and self.computer_move == self.scissors or\
#                 self.user_move == self.rock and self.computer_move == self.paper or \
#                     self.user_move == self.scissors and self.computer_move == self.rock:
#                 print(f"Sorry, but computer chose {self.computer_move}")
#             elif self.user_move == self.paper and self.computer_move == self.rock or\
#                 self.user_move == self.rock and self.computer_move == self.scissors or \
#                     self.user_move == self.scissors and self.computer_move == self.paper:
#                 print(f"Well done. Computer chose {self.computer_move} and failed")
#             self.valid()
#
#     def valid(self):
#         if self.user_move != "paper" or self.user_move != "rock" or self.user_move != "scissors":
#             print("Invalid input")
#             self.valid()
#         else:
#             self.game()
#
#
# game = Bad_computer()
# while True:
#     game.valid()

# adj = "Good"
# part_of_day = "morning"
# comma = ","
# title = "Ms."
# surname = "Johnson"
#
# # your print() function
# print(adj + ' ' + part_of_day + comma + ' ' + title + ' ' + surname + '!')

#
# long_list = list(range(1000000))
# file_name = "my_file.txt"
# opened_file = open(file_name, 'w')
# for _item in long_list:
#     # complete the next string to write item to my_file.txt
#     print(_item, file=opened_file, flush=False)
# opened_file.close()


tmp = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human',
       'snake', 'scissors', 'fire', '', '!exit', '!rating']

# 4 + 7 = 11
# 8 + 7 = 15
# 12 + 7 = 18
user = 'rock'
computer = 'devil'
a = tmp.index(user)
b = tmp.index(computer)

a += 7
b += 7
print(abs(a - b))
