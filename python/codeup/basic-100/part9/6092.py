n = int(input())
tmp = input().split()
arr=[]

for i in range(n) :
    tmp[i] = int(tmp[i])

for i in range(24) :
    arr.append(0)

for i in range(n) :
    arr[tmp[i]] += 1

for i in range(1,24) :
    print(arr[i], end = " ")