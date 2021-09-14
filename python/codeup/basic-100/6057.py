x,y=input().split()
boolX = bool(int(x))
boolY = bool(int(y))
print(boolX and boolY or not boolX and not boolY)