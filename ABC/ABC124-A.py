A, B = map(int, input().split())
coin = 0
coin += max(A, B)
coin += max(min(A, B), max(A, B)-1)
print(coin)
