# AtCoder ABC086A - Product
def even_odd(a,b):
    if (a*b)%2 == 0:
        return "Even"
    elif (a*b)%2 == 1:
        return "Odd"
num1, num2 = map(int, input().split())
print(even_odd(num1, num2))
