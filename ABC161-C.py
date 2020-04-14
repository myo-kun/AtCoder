# solution to https://atcoder.jp/contests/abc161/tasks/abc161_c
N, K = map(int, input().split())
print(min(N%K, K-(N%K)))
