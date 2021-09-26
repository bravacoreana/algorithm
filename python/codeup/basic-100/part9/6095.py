arr = []
for i in range(20) :
    arr.append([])
    for j in range(20) :
        arr[i].append(0)

n = int(input())
for i in range(n) :
    x,y = input().split()
    arr[int(x)][int(y)] = 1

for i in range(1, 20) :
    for j in range(1, 20) :
        print(arr[i][j], end =' ')
    print()

