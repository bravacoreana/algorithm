x = int(input())
sum = 0

for i in range(1, x) :
    sum += i
    if sum >= x :
        print(i)
        break