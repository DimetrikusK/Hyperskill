import itertools

tmp = str()
tmp_pass = 'abcdefghijklmnopqrstuvwxyz0123456789'
for i in range(1, 100):
    for j in itertools.product(tmp_pass, repeat=i):
        tmp = ''.join(j)
        if tmp == 'pass':
            print(tmp)
            break
