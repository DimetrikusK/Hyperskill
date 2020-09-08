def regular(regex, string):
    if not regex or regex == '.':
        return True
    else:
        return regex == string


regex, string = input().split('|')
print(regular(regex, string))