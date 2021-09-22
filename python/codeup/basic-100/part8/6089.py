a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

value = a
i=1

while True:
   value *= r
   i+=1
   if i==n :
       break
print(value) 