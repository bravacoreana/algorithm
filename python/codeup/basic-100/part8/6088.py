a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
sum = a
i=1

while True :
    sum += d
    i+=1
    if i == n :
        break

print(sum)