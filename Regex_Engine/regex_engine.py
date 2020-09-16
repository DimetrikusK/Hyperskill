import sys

sys.setrecursionlimit(10000)


def main(regex, string):
    if '^' in regex or '$' in regex:
        slice(regex, string)
        exit()
    if '?' in regex or '*' in regex or '+' in regex:
        meta(regex, string)
        exit()
    if regular(regex, string) is True:
        print(True)
    else:
        print(comparison(regex, string))


def meta(regex, string):
    if '?' in regex:
        if len(regex) > len(string):
            if regex[0:regex.find('?')] == string[0:regex.find('?')] or \
                    regex[0:regex.find('?') - 1] == string[0:regex.find('?') - 1]:
                print(True)
        else:
            print(False)
    if '*' in regex and '.' not in regex:
        if regex[0:regex.find('*')] == string[0:regex.find('*')] or \
                regex[0:regex.find('*') - 1] == string[0:regex.find('*') - 1]:
            print(True)
    elif '*' in regex and '.' in regex:
        if regex[0:regex.find('.')] == string[0:regex.find('.')]:
            print(True)
        else:
            print(False)
    if '+' in regex:
        if '.' in regex:
            if regex[0:regex.find('+') - 1] == string[0:regex.find('+') - 1]:
                print(True)
            else:
                print(False)
        else:
            if regex[0:regex.find('+')] == string[0:regex.find('+')]:
                print(True)
            else:
                print(False)


def slice(regex, string):
    if regex[0] == '^' and regex[-1] == '$':
        if len(regex[1:-1]) == len(string):
            if '?' in regex or '*' in regex or '+' in regex:
                meta(regex[1:-1], string)
            else:
                regular(regex[1:-1], string)
        else:
            print(False)
    elif regex[0] == '^':
        if '?' in regex or '*' in regex or '+' in regex:
            if regex[1:regex.find('?')] == string[0:regex.find('?') - 1] or \
                    regex[1:regex.find('*')] == string[0:regex.find('*') - 1] or \
                    regex[1:regex.find('+')] == string[0:regex.find('+') - 1]:
                meta(regex[1:], string[0:len(regex[1:])])
            else:
                print(False)
                exit()
        else:
            regular(regex[1:], string[0:len(regex[1:])])
    elif regex[-1] == '$':
        if '?' in regex or '*' in regex or '+' in regex:
            if string[regex.find('?'):] == regex[regex.find('?') + 1:-1] or \
                        string[regex.find('*'):] == regex[regex.find('*') + 1:-1] or \
                        string[regex.find('+'):] == regex[regex.find('+') + 1:-1]:
                meta(regex[:-1], string[-len(regex[:-1]):])
            else:
                print(False)
                exit()
        else:
            regular(regex[:-1], string[-len(regex[:-1]):])


def comparison(regex, string):
    if not regex:
        return True
    if not string:
        return False
    if regex[0] == string[0] or regex == '.':
        return comparison(regex[1:], string[1:])
    else:
        if not string or len(string) <= 1:
            return False
        else:
            return comparison(regex, string[1:])


def regular(regex, string):
    if regex == string:
        print(True)
        exit()
    if not string:
        print(False)
        exit()
    if not regex:
        print(True)
        exit()
    if regex[0] == string[0] or regex[0] == '.':
        return regular(regex[1:], string[1:])
    else:
        print(False)
        exit()


regex, string = input().split('|')
main(regex, string)
