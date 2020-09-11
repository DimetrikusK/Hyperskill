reg = "appll?e"
string = "appleeeee"

# print(string[-len(reg[:-1]):])

print(reg[0:reg.find('?') - 1] == string[0:reg.find('?') - 1])

with open('/Users/jsabina/PycharmProjects/text.txt', 'w') as f:
    f.write("SHO ZA?")
    f.close()

reader = FileReader('/Users/jsabina/PycharmProjects/text.txxt')
text = reader.read()
print(text)
