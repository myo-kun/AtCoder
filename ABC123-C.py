import math
N = int(input())
cap = [int(input()) for _ in range(5)]

print(math.ceil(N / min(cap)) + 4)
