from collections import deque
import copy


def validation_input(command):
    expression = command.split()
    tmp = list()
    if len(expression) == 1 and expression[0].isalpha():
        return expression
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


def addition(value, value_dict):
    if len(value) == 1 and value[0].isalpha():
        if value[0] in value_dict:
            print(value_dict[value[0]])
        else:
            print('Unknown variable')
    elif len(value) > 1:
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


def ft_summa(rpn):
    result = list()
    if len(result) != 1:
        for i in rpn:
            if i.isdigit() or i.isalpha():
                result.append(i)
            if i == '*':
                result.append(int(result.pop(-2)) * int(result.pop(-1)))
            elif i == '/':
                result.append(int(result.pop(-2)) / int(result.pop(-1)))
            elif i == '+':
                result.append(int(result.pop(-2)) + int(result.pop(-1)))
            elif i == '-':
                result.append(int(result.pop(-2)) - int(result.pop(-1)))
    print(*result)
    menu()


def chek_operat(operation, result, value):
    if '(' not in operation:
        for i in operation:
            if i == '*' or i == '/':
                result.append(i)
                operation.remove(i)
                operation.appendleft(value)
                break
    else:
        operation.appendleft(value)

    return operation, result, value


def addet_multiplay(value, result, operation):
    if value == '*':
        sim = '/'
    else:
        sim = '*'
    if value in operation:
        result.append(value)
    elif sim in operation:
        result.append(sim)
        operation.remove(sim)
        operation.appendleft(value)
    else:
        operation.appendleft(value)
    return result, operation


def rever_pn(command):
    rpn = deque()
    operation = deque()
    if '(' in command or ')' in command:
        command = command.replace('(', '( ')
        command = command.replace(')', ' )')
    command = validation_input(command)
    for value in command:
        if value.isdigit() or value.isalpha():
            rpn.append(value)
        elif value == '( ':
            operation.appendleft('(')
        # elif '(' in operation and value.isdigit() is False and value != ' )':  # 3 + 4 * 2 / (1 - 5)
        #     result.append(value)
        elif value == ' )':
            copy_operatio = copy.copy(operation)
            for i in copy_operatio:
                if i != '(':
                    rpn.append(i)
                    operation.popleft()
                else:
                    operation.popleft()
                    break
        elif value == '+' or value == '-':
            if '*' in operation or '/' in operation:
                operation, rpn, value = chek_operat(operation, rpn, value)
            else:
                operation.appendleft(value)
        elif value == '*' or value == '/':
            rpn, operation = addet_multiplay(value, rpn, operation)
    for i in operation:
        rpn.append(i)
    ft_summa(rpn)


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
            else:
                print('Unknown command')
        elif command == '':
            pass
        elif '=' in command:
            ft_add(command, value_dict)
        else:
            rever_pn(command)



menu()
