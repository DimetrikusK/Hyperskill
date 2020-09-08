import sys
sys.setrecursionlimit(10000)


def main(regex, string):
    if regular(regex, string) is True:
        print(True)
    else:
        print(comparison(regex, string))


def comparison(regex, string):
    if not regex:
        return True
    if not string:
        return False
    if regex[0] == string[0] or regex == '.':
        if not regex:
            return True
        else:
            return comparison(regex[1:], string[1:])
    else:
        if not string or len(string) <= 1:
            return False
        else:
            return comparison(regex, string[1:])


def regular(regex, string):
    if regex == string:
        return True
    if not string:
        return False
    if not regex:
        return True
    if regex[0] == string[0] or regex[0] == '.':
        return regular(regex[1:], string[1:])
    else:
        return False


regex, string = input().split('|')
main(regex, string)
