S = input()
N = 0
for c in S:
    if c == '+':
        N += 1
    else:
        N -= 1
print(N)
