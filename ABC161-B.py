n,m = map(int,input().split())
A = list(map(int, input().split()))
x = sum(A)/(4*m)
count = 0
for a in A:
    if a >= x:
        count += 1
if count >= m:
    print("Yes")
else:
    print("No")
