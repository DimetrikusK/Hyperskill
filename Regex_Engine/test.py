regex = "\\.$"
string = "end."
# ^n.+p$|noooooooope

print(regex[regex.find('\\') + 1] in string)
# print(string[regex.find('*') + 1:] == regex[regex.find('*') + 1:-1])

# print(regex[0:regex.find('.')])
# print(string[0:regex.find('.')])



# print(regex[regex.find('*') + 1:-1])
# print(regex[0:regex.find('*')])
# print(string[0:regex.find('*')])

# if len(regex) > len(string):
#     if regex[0:regex.find('?')] == string[0:regex.find('?')] or regex[0:regex.find('?') - 1] == string[0:regex.find('?') - 1]:
#         print(1)
# else:
#     print(0)
# print(regex[0:regex.find('?')])
# print(string[0:regex.find('?')])
#
# if regex[0:regex.find('*')] == string[0:regex.find('*')]:
#     print(1)
# else:
#     print(0)