choice = {1, 2, 3}
magic = set()
A = magic.add(int(input()))
B = magic.add(int(input()))

print(list(choice - magic)[0])
