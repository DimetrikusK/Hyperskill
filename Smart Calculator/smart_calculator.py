from collections import deque
import copy
import re


def count_len_input(expression, value_dict):
    count = expression.count('(') + expression.count(')')
    if count % 2 != 0:
        print('Invalid expression')
        menu(value_dict)
    if len(expression) == 1:
        if expression[0].isalpha():
            if expression[0] in value_dict:
                print(value_dict[expression[0]])
                menu(value_dict)
            else:
                print('Unknown variable')
        elif '-' in expression[0]:
            print(expression[0])
            menu(value_dict)
    else:
        return 0


def ft_count_operator(command):
    expression = command.split()
    for i in range(len(expression)):
        if '-' in expression[i] and len(expression[i]) > 1:
            if len(expression[i]) % 2 == 0:
                expression[i] = '+'
            else:
                expression[i] = '-'
        elif '*' in expression[i] and len(expression[i]) > 1:
            print('Invalid expression')
            menu(value_dict)
        elif '/' in expression[i] and len(expression[i]) > 1:
            print('Invalid expression')
            menu(value_dict)
    expression = ' '.join(expression)
    return expression


def validation_input(command, value_dict):
    tmp = list()
    command = ft_count_operator(command)
    expression = re.findall('[+-]|[*/]|[0-9]+|[()]+|[a-z]+|[A-Z]', command)
    count_len_input(expression, value_dict)
    for i in range(len(expression)):
        if expression[i].isdigit():
            tmp.append(expression[i])
        elif expression[i].isalpha():
            if expression[i] in value_dict:
                tmp.append(value_dict[expression[i]])
            else:
                print('Unknown variable')
        elif expression[i] == expression[i - 1]:
            if expression[i] == '(' or expression[i] == ')':
                tmp.append(expression[i])
            else:
                pass
        else:
            tmp.append(expression[i])
    return tmp, value_dict


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


def ft_summa(rpn, value_dict):
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
    menu(value_dict)


def chek_operat(operation, result, value):
    if len(operation) >= 1 and operation[0] == '(':
        operation.appendleft(value)
    elif len(operation) >= 1:
        if operation[0] == '+' or operation[0] == '-':
            result.append(operation[0])
            operation.remove(operation[0])
            operation.appendleft(value)
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
    if '(' not in operation and len(operation) >= 1:
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
    else:
        operation.appendleft(value)
    return result, operation


def revers_pn(command, value_dict):
    rpn = deque()
    operation = deque()
    if '(' in command or ')' in command:
        command = command.replace('(', '( ')
        command = command.replace(')', ' )')
    command, value_dict = validation_input(command, value_dict)
    for value in command:
        if value.isdigit() or value.isalpha():
            rpn.append(value)
        elif value == '(':
            operation.appendleft('(')
        elif value == ')':
            copy_operation = copy.copy(operation)
            for i in copy_operation:
                if i != '(':
                    rpn.append(i)
                    operation.popleft()
                else:
                    operation.popleft()
                    break
        elif value == '+' or value == '-':
            operation, rpn, value = chek_operat(operation, rpn, value)
        elif value == '*' or value == '/':
            rpn, operation = addet_multiplay(value, rpn, operation)
    for i in operation:
        rpn.append(i)
    ft_summa(rpn, value_dict)


def ft_input_comand(command, value_dict):
    input_command = re.findall('[+-]|[*/]|[0-9]+|[a-z]+', command)
    if len(input_command) == 2:
        if command == '/exit':
            print('Bye')
            exit()
        elif command == '/help':
            print('The program calculates the sum of numbers')
            menu(value_dict)
        else:
            print('Unknown command')
            menu(value_dict)
    else:
        return 0


def menu(value_dict):
    while True:
        command = input()
        if '/' in command:
            ft_input_comand(command, value_dict)
        if command == '':
            pass
        elif '=' in command:
            ft_add(command, value_dict)
        else:
            revers_pn(command, value_dict)


value_dict = dict()
menu(value_dict)
