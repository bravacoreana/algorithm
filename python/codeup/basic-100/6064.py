x,y,z = input().split()

x=int(x)
y=int(y)
z=int(z)

# a = x if x<y else y 
# b = a if a<z else z 

print((x if x<y else y) if (x if x<y else y < z) else z)