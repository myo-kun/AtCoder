n = input()
new_n = ''
for c in n:
    if c == '1':
        new_n += '9'
    else:
        new_n += '1'
print(int(new_n))
