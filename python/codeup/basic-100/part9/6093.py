count = int(input())
numbers = input().split()


for i in range(count-1, -1, -1) :
    print(numbers[i], end=" ")