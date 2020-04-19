L = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
A, B = map(int, input().split())
Alice = L.index(A)
Bob = L.index(B)
if (Alice > Bob):
    print('Alice')
elif (Alice < Bob):
    print('Bob')
else:
    print('Draw')
