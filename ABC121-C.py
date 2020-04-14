#ABC121 C
n, m = map(int, input().split())
shops = []
for i in range(n):
    shops.append(list(map(int, input().split())))
shops = sorted(shops)

price = 0
i = 0
while m > 0:
    if m - shops[i][1] >= 0:
        price += shops[i][0] * shops[i][1]
        m -= shops[i][1]
        i += 1
    else:
        price += shops[i][0] * m
        m -= m
print(price)
