import itertools

# tmp = str()
# tmp_pass = 'abcdefghijklmnopqrstuvwxyz0123456789'
# for i in range(1, 100):
#     for j in itertools.product(tmp_pass, repeat=i):
#         tmp = ''.join(j)
#         if tmp == 'pass':
#             print(tmp)
#             break




password_tmp = str()
with open('file.txt', 'r', encoding='utf-8')as file:
    for password in file:
        password_tmp += password
    password_tmp = password_tmp.split('\n')
    password_tmp = [x for x in password_tmp if x.isalpha()]

for word in password_tmp:
    mixed_case = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word)))
    for i in mixed_case:
        print(i)

# words = map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in password_tmp)))
# for i in words:
#     print(i)
# for word in password_tmp:
#     src = itertools.product(word.upper(), word.lower())
# for i in src:
#     print(i)



