#ABC121 B
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

count = 0

for i in range(n):
    sub_total = 0
    for j in range(m):
        sub_total += a[i][j] * b[j]
    if sub_total + c > 0:
        count += 1
print(count)
