from random import randint


def winning(ceil, player):
    for i in range(0, 3):
        if ceil[i][0] == ceil[i][1] == ceil[i][2]:
            if ceil[i][0] != ' ':
                return True
        if ceil[0][i] == ceil[1][i] == ceil[2][i]:
            if ceil[i][0] != ' ':
                return True
        if ceil[0][0] == ceil[1][1] == ceil[2][2]:
            if ceil[i][0] != ' ':
                return True
        if ceil[0][2] == ceil[1][1] == ceil[2][0]:
            if ceil[i][0] != ' ':
                return True
    return False


def movering(ceil, player):
    if len(tmp) == 9:
        ceil[1][1] = first_move
    elif tmp:
        ceil[tmp[0][0]][tmp[0][1]] = player
        src = winning(ceil, first_move)
        if src == True:
            return 10
        else:
            return -10

# print(ceil[tmp[0][0]][tmp[0][1]])
# tmp.remove(tmp[0])
# print(tmp)
# tmp.remove(tmp[0])
# print(tmp)


ceil = [['X', 'O', 'O'],
        [' ', 'X', 'X'],
        [' ', ' ', 'O']]
first_move = 'X'
second_move = 'O'
tmp = []
score = {}
for i in range(len(ceil)):
    for j in range(len(ceil)):
        if ceil[i][j] == ' ':
            tmp.append([i, j])
print(tmp)
while tmp:
    score[tmp[0][0], tmp[0][1]] = movering(ceil, first_move)
    ceil[tmp[0][0]][tmp[0][1]] = ' '
    tmp.remove(tmp[0])
print(score)
print(ceil)









# def minimax(ceil):
#     availSpots = emptyIndices(newBoard)
#     if winning(newBoard, first_move):
#         return {score: -10}
#     elif winning(newBoard, second_move):
#         return {score: 10}
#     elif availSpots.length == 0):
#         return {score: 0}
#
#     moves = []
#     # for i = 0; i < availSpots.length; i++)
#
#     move = {}
#     move.index = newBoard[availSpots[i]]
#     newBoard[availSpots[i]] = player