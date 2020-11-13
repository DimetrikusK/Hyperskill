def validation_input(command):
    expression = command.split()
    tmp = list()
    for i in range(len(expression)):
        if len(expression[i]) > 1 and expression[i][1] != '-' and expression[i][1] != '+'\
                and expression[i][-1].isdigit() is False:
            print('Invalid expression')
            menu()
        elif len(expression[i]) > 1 and expression[i][0] != expression[i][1]:
            tmp.append(expression[i])
        elif expression[i].isdigit():
            tmp.append(expression[i])
        elif '-' in expression[i] and len(expression[i]) > 1:
            if len(expression[i]) % 2 == 0:
                tmp.append('+')
            else:
                tmp.append('-')
        elif '-' in expression[i]:
            tmp.append(expression[i])
        elif '+' in expression[i]:
            tmp.append('+')
    if len(tmp) > 1 and '+' not in tmp and '-' not in tmp:
        print('Invalid expression')
        menu()
    else:
        return tmp


def addition(expression):
    flag = 0
    count = 0
    for i in range(len(expression)):
        if flag == 0:
            count += int(expression[i])
            flag += 1
        else:
            if expression[i].isdigit():
                if expression[i - 1] == '-':
                    count -= int(expression[i])
                elif expression[i - 1] == '+':
                    count += int(expression[i])
    print(count)


def menu():
    while True:
        command = input()
        if '/' in command:
            if command == '/exit':
                print('Bye')
                exit()
            elif command == '/help':
                print('The program calculates the sum of numbers')
            else:
                print('Unknown command')
        elif command.isalpha():
            print('Invalid expression')
        elif command == '':
            pass
        else:
            addition(validation_input(command))


menu()
