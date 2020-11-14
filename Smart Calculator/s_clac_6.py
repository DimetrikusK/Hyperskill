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
        elif expression[i].isdigit() or expression[i].isalpha():
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


def ft_add(command, value_dict):
    command = command.replace(' ', '')
    command = command.replace('=', ' ')
    command = command.split()
    if len(command) == 2:
        if command[0].isalpha() and command[1].isdigit():
            value_dict[command[0]] = command[1]
            return value_dict
        elif command[0].isalpha() and command[1].isalpha():
            if command[1] in value_dict:
                value_dict[command[0]] = value_dict[command[1]]
                return value_dict
            else:
                print('Unknown variable')
        else:
            print('Invalid assignment')
    else:
        print('Invalid assignment')


def operation(value, value_dict):
    if len(value) == 1 and value[0].isalpha() and value[0] in value_dict:
        print(value_dict[value[0]])
    else:
        flag = 0
        count = 0
        for i in range(len(value)):
            if flag == 0:
                if value[i].isdigit():
                    count += int(value[i])
                    flag += 1
                elif value[i].isalpha():
                    count += int(value_dict[value[i]])
                    flag += 1
            else:
                if value[i].isdigit():
                    if value[i - 1] == '-':
                        count -= int(value[i])
                    elif value[i - 1] == '+':
                        count += int(value[i])
                elif value[i].isalpha():
                    if value[i - 1] == '-':
                        count -= int(value_dict[value[i]])
                    elif value[i - 1] == '+':
                        count += int(value_dict[value[i]])
                print(count)


def menu():
    value_dict = dict()
    while True:
        command = input()
        if '/' in command:
            if command == '/exit':
                print('Bye')
                exit()
            elif command == '/help':
                print('The program calculates the sum of numbers')
                menu()
            else:
                print('Unknown command')
                menu()
        if '=' in command:
            ft_add(command, value_dict)
        else:
            tmp = validation_input(command)
            operation(tmp, value_dict)


menu()
