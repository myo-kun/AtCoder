A, B, C = map(int, input().split())
if (A == B == C) or ((A != B) and (A != C) and (B != C)) :
    print("No")
else:
    print("Yes")
