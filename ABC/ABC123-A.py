distances = [int(input()) for _ in range(5)]
K = int(input())

if distances[-1] - distances[0] > K:
  print(":(")
else:
  print("Yay!")
