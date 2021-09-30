h,w = map(int, input().split())
board = [
    [0 for i in range(0, w)] for j in range(0, h)
]

n = int(input())

for i in range(0, n) :
    point = input().split()
    point = list(map(int, point))
    l = point[0]
    d = point[1]
    x = int(point[2]) -1 
    y = int(point[3]) -1

    for j in range(0, l) :
        if d == 0 :
            board[x][y] = 1
            y+=1
            
        else :
            board[x][y] = 1
            x+=1
            

for i in range(0, h) :
    for j in range(0, w):
        print(board[i][j], end=" ")
    print()