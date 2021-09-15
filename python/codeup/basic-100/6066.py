x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)
arr = [x,y,z]

for i in arr :
    if i % 2 == 0 :
        print("even")
    else :
        print("odd")
