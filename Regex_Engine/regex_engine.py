def regular(regex, string):
    if regex == string:
        return True
    if not regex:
        return True
    if len(regex) != len(string):
        return False
    if regex[0] == string[0] or regex[0] == '.':
        return regular(regex[1:], string[1:])
    else:
        return False


regex, string = input().split('|')
print(regular(regex, string))
