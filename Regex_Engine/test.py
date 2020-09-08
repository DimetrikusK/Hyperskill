regex, string = input().split('|')
if regex is string or regex == '' or regex == '.' or regex == string:
    print(True)
elif regex is not string:
    print(False)