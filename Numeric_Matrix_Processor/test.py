# def multiplication_matrix():
#     matrix = []
#     matrix_size = input().split()
#     for i in range(int(matrix_size[0])):
#         input_matrix = [int(i) for i in input().split()]
#         if len(input_matrix) != int(matrix_size[1]):
#             print('ERROR')
#         else:
#             matrix.append(input_matrix)
#     multiplicate = int(input())
#     for i in range(int(matrix_size[0])):
#         for j in range(int(matrix_size[1])):
#             matrix[i][j] = matrix[i][j] * multiplicate
#
#
#
# a ='ABCD'
# print(a[-3:])


#
#
# multiplication_matrix()

# def matrix(a, b):
#     c = [[0 for row in range(len(a))] for col in range(len(b[0]))]
#     print(c)
#     for i in range(len(a)):
#         for j in range(len(b[0])):
#             for k in range(len(b)):
#                 c[i][j] += a[i][k] * b[k][j]
#     print(*c)


a = [[1, 1, 1, -1], [2, 2, 2, -2], [3, 3, 3, -3]]
b = []
#
tmp = [i[::-1] for i in a[::-1]]
print(tmp)
for i in zip(*tmp):
    print(i)


# def created_matrix(size):
#     matrix = []
#     input_matrix = []
#     for i in range(int(size[0])):
#         input_matrix = [int(i) for i in input().split()]
#         matrix.append(input_matrix)
#     print(matrix)
#
#
# size = [2, 2]
# created_matrix(size)