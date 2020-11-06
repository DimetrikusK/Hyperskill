
ceil = [[' ', ' ', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', 'X']]

for horizont in range(len(ceil)):
    if ceil[horizont].count('X') == 2:
        for i in range(len(ceil)):
            if ceil[horizont][i] == ' ':
                ceil[horizont][i] = 'X'

zip_ceil = []
for i in zip(*ceil):
    zip_ceil.append(list(i))
for horizont in range(len(zip_ceil)):
    if zip_ceil[horizont].count('X') == 2:
        for i in range(len(zip_ceil)):
            if zip_ceil[horizont][i] == ' ':
                zip_ceil[horizont][i] = 'X'

ceil = [[], [], []]
for i in range(len(zip_ceil)):
    for j in range(len(zip_ceil)):
        ceil[i].append(zip_ceil[j][i])



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




