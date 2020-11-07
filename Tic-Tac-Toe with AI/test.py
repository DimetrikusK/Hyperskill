from random import randint

ceil = [['O', ' ', ' '],
        [' ', 'O', ' '],
        [' ', ' ', ' ']]

chek_move = 0
flag = 0

ai_move = 'X'
moving = 'X'
# if ceil.count(ai_move) > 1:
while chek_move != 2:
    for horizont in range(len(ceil)):
        if ceil[horizont].count(ai_move) == 2:
            for i in range(len(ceil)):
                if ceil[horizont][i] == ' ':
                    ceil[horizont][i] = moving
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
                        zip_ceil[horizont][i] = moving
                        flag += 1
                        break
        ceil = [[], [], []]
        for i in range(len(zip_ceil)):
            for j in range(len(zip_ceil)):
                ceil[i].append(zip_ceil[j][i])

    if flag == 0:
        if (ceil[0][0] == ai_move and ceil[1][1] == ai_move) or (ceil[0][0] == ai_move and ceil[2][2] == ai_move) \
                or (ceil[2][2] == ai_move and ceil[1][1] == ai_move):
            if ceil[0][0] == ' ':
                ceil[0][0] = moving
            elif ceil[1][1] == ' ':
                ceil[1][1] = moving
            elif ceil[2][2] == ' ':
                ceil[2][2] = moving
            flag += 1

    if flag == 0:
        if (ceil[0][2] == ai_move and ceil[1][1] == ai_move) or (ceil[0][2] == ai_move and ceil[2][0] == ai_move) \
                or (ceil[2][0] == ai_move and ceil[1][1] == ai_move):
            if ceil[0][2] == ' ':
                ceil[0][2] = moving
            elif ceil[1][1] == ' ':
                ceil[1][1] = moving
            elif ceil[2][0] == ' ':
                ceil[2][0] = moving
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
            ceil[x][y] = moving
            loop = False

print("---------")
print('| {} {} {} |'.format(ceil[0][0], ceil[0][1], ceil[0][2]))
print('| {} {} {} |'.format(ceil[1][0], ceil[1][1], ceil[1][2]))
print('| {} {} {} |'.format(ceil[2][0], ceil[2][1], ceil[2][2]))
print("---------")
# for i in zip(*ceil):
#     tmp.append(i)
#
# ceil = []
# for i in zip(*tmp):
#     ceil.append(i)
#
# tmp = [[], [], []]
#
# for i in range(len(ceil)):
#     for j in range(len(ceil)):
#         tmp[i].append(ceil[i][j])
#
# print(tmp)
