def xor(a, b):
    if a and b or not a and not b:
        return False
    elif a:
        return a
    else:
        return b


a = ''
b = ''
print(xor(a, b))