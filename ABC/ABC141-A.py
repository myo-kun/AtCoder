S = input()
P = ['Sunny', 'Cloudy', 'Rainy']
i = P.index(S)
if (i == 2):
    print(P[0])
else:
    print(P[i+1])
