# from random import randint
# import copy
# import sys
#
#
# def winning(ceil, player):
#     for i in range(0, 3):
#         if ceil[i][0] == ceil[i][1] == ceil[i][2]:
#             if ceil[i][0] == player:
#                 return True
#         if ceil[0][i] == ceil[1][i] == ceil[2][i]:
#             if ceil[i][0] == player:
#                 return True
#         if ceil[0][0] == ceil[1][1] == ceil[2][2]:
#             if ceil[i][0] == player:
#                 return True
#         if ceil[0][2] == ceil[1][1] == ceil[2][0]:
#             if ceil[i][0] == player:
#                 return True
#     return False
#
#
# def draw(ceil):
#     count = 0
#     for i in ceil:
#         for j in i:
#             if j == ' ':
#                 count += 1
#     if count == 0:
#         return True
#     return False
#
#
# def minimax(newCeil, deep, is_maximazing):
#     if winning(newCeil, user_char):
#         return scorses[user_char]
#     if winning(newCeil, compute_char):
#         return scorses['loss']
#     if draw(newCeil):
#         return scorses['deaw']
#
#     if is_maximazing:
#         best_score = -sys.maxsize
#         for i in range(len(newCeil)):
#             for j in range(len(newCeil)):
#                 if newCeil[i][j] == ' ':
#                     newCeil[i][j] = compute_char
#                     score = minimax(newCeil, deep + 1, MIN)
#                     newCeil[i][j] = ' '
#                     best_score = max(best_score, score)
#     else:
#         best_score = sys.maxsize
#         for i in range(len(newCeil)):
#             for j in range(len(newCeil)):
#                 if newCeil[i][j] == ' ':
#                     newCeil[i][j] = user_char
#                     score = minimax(newCeil, deep + 1, MAX)
#                     newCeil[i][j] = ' '
#                     best_score = min(best_score, score)
#     return best_score
#
#
# def print_ceil(ceil):
#     print("---------")
#     print('| {} {} {} |'.format(ceil[0][0], ceil[0][1], ceil[0][2]))
#     print('| {} {} {} |'.format(ceil[1][0], ceil[1][1], ceil[1][2]))
#     print('| {} {} {} |'.format(ceil[2][0], ceil[2][1], ceil[2][2]))
#     print("---------")
#
#
# def start():
#     best_score = -sys.maxsize
#     move = None
#     newCeil = copy.deepcopy(ceil)
#     player = 'X'
#     for i in range(len(newCeil)):
#         for j in range(len(newCeil)):
#             if newCeil[i][j] == ' ':
#                 newCeil[i][j] = player
#                 score = minimax(newCeil, 0, MIN)
#                 newCeil[i][j] = ' '
#                 if score > best_score:
#                     best_score = score
#                     x, y = i, j
#     ceil[x][y] = compute_char
#     print_ceil(ceil)

MAX = True
MIN = False
user_char = 'X'
compute_char = 'O'
ceil = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
count = 0
for i in range(len(ceil)):
    for j in range(len(ceil)):
        if ceil[i][j] == ' ':
            count += 1
print(count)

# scorses = {user_char: -1,
#            compute_char: 1,
#            'deaw': 0}
# start()






