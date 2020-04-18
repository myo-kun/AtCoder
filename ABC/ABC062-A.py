X = {1, 3, 5, 7, 8, 10, 12}
Y = {4, 6, 9, 11}
Z = {2}

L = list(map(int, input().split()))
S = set(L)
if len(X-S)==5 or len(Y-S)==2:
    print('Yes')
else:
    print('No')
