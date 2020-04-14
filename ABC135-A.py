A, B = map(int, input().split())
Amod2 = A%2
Bmod2 = B%2
if (Amod2 == Bmod2):
    print(int((A+B)/2))
else:
    print("IMPOSSIBLE")
