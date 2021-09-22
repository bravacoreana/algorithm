h,b,c,s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

value = h*b*c*s
value /= (8 * 1024 * 1024)
print(format(value, ".1f"), "MB", sep=" ")