A = list(map(int, input().split()))
A.sort()
prev = A[0]
cost = 0
for i in range(1, 3):
    cost += abs(prev - A[i])
    prev = A[i]
print(cost)
