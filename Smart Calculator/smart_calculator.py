def validation_input(command):
    command = command.split()
    tmp = list()
    for i in range(len(command)):
        if len(command[i]) > 1 and command[i][0] != command[i][1]:
            tmp.append(command[i])
        elif command[i].isdigit():
            tmp.append(command[i])
        elif '-' in command[i] and len(command[i]) > 1:
            if len(command[i]) % 2 == 0:
                tmp.append('+')
            else:
                tmp.append('-')
        elif '-' in command[i]:
            tmp.append(command[i])
        elif '+' in command[i]:
            tmp.append('+')
    return tmp


def addition(command):
    count = 0
    for i in range(len(command)):
        if command[i] == '-':
            command[i + 1] = -int(command[i + 1])
        elif command[i] == '+':
            pass
        else:
            count += int(command[i])
    print(count)


while True:
    command = input()
    if command == '/exit':
        print('Bye')
        break
    elif command == '/help':
        print('The program calculates the sum of numbers')
    elif command == '':
        print(command)
    else:
        addition(validation_input(command))

