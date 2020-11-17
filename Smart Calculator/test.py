from collections import deque
import copy


def validation_input(command):
    expression = command.split()
    tmp = list()
    if len(expression) == 1 and expression[0].isalpha():
        return expression
    for i in range(len(expression)):
        # if len(expression[i]) > 1 and expression[i][1] != '-' and expression[i][1] != '+'\
        #         and expression[i][-1].isdigit() is False:
        #     print('Invalid expression')
        #     menu()
        if len(expression[i]) > 1 and expression[i][0] != expression[i][1]:
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
        elif '*' in expression[i]:
            tmp.append('*')
        elif '/' in expression[i]:
            tmp.append('/')
        elif '(' in expression[i]:
            tmp.append('( ')
        elif ')' in expression[i]:
            tmp.append(' )')
    if len(tmp) > 1 and '+' not in tmp and '-' not in tmp:
        print('Invalid expression')
        menu()
    else:
        return tmp


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


def menu():
    result = deque()
    operation = deque()
    while True:
        command = input()
        if '(' in command or ')' in command:
            command = command.replace('(', '( ')
            command = command.replace(')', ' )')
        command = validation_input(command)
        for value in command:
            if value.isdigit() or value.isalpha():
                result.append(value)
            elif value == '( ':
                operation.appendleft('(')
            # elif '(' in operation and value.isdigit() is False and value != ' )':  # 3 + 4 * 2 / (1 - 5)
            #     result.append(value)
            elif value == ' )':
                copy_operatio = copy.copy(operation)
                for i in copy_operatio:
                    if i != '(':
                        result.append(i)
                        operation.popleft()
                    else:
                        operation.popleft()
                        break
            elif value == '+' or value == '-':
                if '*' in operation or '/' in operation:
                    operation, result, value = chek_operat(operation, result, value)
                else:
                    operation.appendleft(value)
            elif value == '*' or value == '/':
                result, operation = addet_multiplay(value, result, operation)
        for i in operation:
            result.append(i)
        print(operation)
        print(result)


menu()
