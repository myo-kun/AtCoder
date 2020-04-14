food = [int(input()) for _ in range(5)]

total = 0
compare = 0
largest = 0

if sum(food)%10 == 0:
    print(sum(food))

else:
    for x in food:
        if (10 - (x % 10) > compare) and ((x % 10) != 0):
            largest = x
            compare = 10 - (x % 10)

    food.remove(largest)

    for i in range(len(food)):
        if food[i] % 10 != 0:
            total += round(food[i] + 5.1, -1)
        else:
            total += food[i]

    print(int(total+largest))
