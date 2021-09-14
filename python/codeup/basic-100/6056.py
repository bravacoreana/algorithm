x,y=input().split()

boolX = bool(int(x))
boolY = bool(int(y)) 

print(boolX and not boolY or not boolX and boolY)
