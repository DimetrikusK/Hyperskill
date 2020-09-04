def add_matrix_one():
    global matrix_size_one
    matrix = []
    matrix_size_one = input('Enter size of first matrix:').split()
    print('Enter first matrix:')
    for i in range(int(matrix_size_one[0])):
        input_matrix = [float(i) for i in input().split()]
        if len(input_matrix) != int(matrix_size_one[1]):
            print('The operation cannot be performed.')
        else:
            matrix.append(input_matrix)
    return matrix


def add_matrix_two():
    global matrix_size_two
    matrix = []
    matrix_size_two = input('Enter size of second matrix:').split()
    valid_size = add_valid_matrix_size()
    if not valid_size:
        print('The operation cannot be performed.')
        exit()
    else:
        print('Enter second matrix:')
        for i in range(int(matrix_size_two[0])):
            input_matrix = [float(i) for i in input().split()]
            if len(input_matrix) != int(matrix_size_two[1]):
                print('The operation cannot be performed.')
            else:
                matrix.append(input_matrix)
    return matrix


def add_valid_matrix_size():
    if matrix_size_one != matrix_size_two:
        return 0
    else:
        return 1


def add_matrix(matrix_1, matrix_2):
    if matrix_1 and matrix_2:
        for i in range(int(matrix_size_one[0])):
            for j in range(int(matrix_size_one[1])):
                matrix_1[i][j] += matrix_2[i][j]
    print_matrix(matrix_1)


def multiplication_matrix_const():
    matrix = []
    matrix_size = input('Enter size of matrix:').split()
    print('Enter matrix:')
    for i in range(int(matrix_size[0])):
        input_matrix = [float(i) for i in input().split()]
        if len(input_matrix) != int(matrix_size[1]):
            print('The operation cannot be performed.')
        else:
            matrix.append(input_matrix)
    print('Enter constant:')
    multiplicate = int(input())
    for i in range(int(matrix_size[0])):
        for j in range(int(matrix_size[1])):
            matrix[i][j] = matrix[i][j] * multiplicate
    print_matrix(matrix)


def multiply_matrices():
    matrix_one_size = input('Enter size of first matrix: ').split()
    print('Enter first matrix: ')
    matrix_one = created_matrix(matrix_one_size)
    matrix_two_size = input('Enter size of second matrix: ').split()
    print('Enter second matrix:')
    matrix_two = created_matrix(matrix_two_size)
    if int(matrix_one_size[1]) != int(matrix_two_size[0]):
        print('The operation cannot be performed.')
        menu()
    new_matrix = [[0 for row in range(int(matrix_two_size[1]))] for col in range(int(matrix_one_size[0]))]
    trans_matrix_two = []
    for i in zip(*matrix_two):
        trans_matrix_two.append(list(i))
    matrix_two = trans_matrix_two
    M = len(matrix_one)
    N = len(matrix_one[0])
    K = len(matrix_two)
    for m in range(M):
        for k in range(K):
            for n in range(N):
                new_matrix[m][k] += matrix_one[m][n] * matrix_two[k][n]
    # for i in range(M):
    #     for j in range(K):
    #         new_matrix[i][j] = int(new_matrix[i][j])
    print_matrix(new_matrix)


def created_matrix(size):
    matrix = []
    for i in range(int(size[0])):
        input_matrix = [float(i) for i in input().split()]
        matrix.append(input_matrix)
    return matrix


def transpose_matrix():
    step = int(input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
"""))
    if step == 1:
        main_diagonal()
    elif step == 2:
        side_diagonal()
    elif step == 3:
        vertical_line()
    elif step == 4:
        horizontal_line()


def main_diagonal():
    size = input("Enter matrix size: ")
    print("Enter matrix: ")
    old_matrix = created_matrix(size)
    matrix = []
    for i in zip(*old_matrix):
        matrix.append(list(i))
    print_matrix(matrix)


def side_diagonal():
    size = input("Enter matrix size: ")
    print("Enter matrix: ")
    matrix = []
    old_matrix = created_matrix(size)
    tmp = [i[::-1] for i in old_matrix[::-1]]
    for i in zip(*tmp):
        matrix.append(i)
    print_matrix(matrix)


def vertical_line():
    size = input("Enter matrix size: ")
    print("Enter matrix: ")
    old_matrix = created_matrix(size)
    matrix = [i[::-1] for i in old_matrix]
    print_matrix(matrix)


def horizontal_line():
    size = input("Enter matrix size: ")
    print("Enter matrix: ")
    old_matrix = created_matrix(size)
    matrix = [i for i in old_matrix[::-1]]
    print_matrix(matrix)


def print_matrix(matrix):
    print('The result is:')
    for i in range(len(matrix)):
        print(*matrix[round(i)])
    menu()


def menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
""")
    step = int(input())
    if step == 1:
        add_matrix(add_matrix_one(), add_matrix_two())
    elif step == 2:
        multiplication_matrix_const()
    elif step == 3:
        multiply_matrices()
    elif step == 4:
        transpose_matrix()
    elif step == 0:
        exit()


menu()
