################# TIME OUT CODE #################
# board = [[0 for i in range(10)] for j in range(10)]


# for i in range(10) :
#     point = input().split()
#     board[i] = list(map(int,point))

# x,y = 1,1

# while True:
#     if(board[x][y] == 0) :
#         board[x][y] = 9
#         if board[x][y+1] == 0 :
#             y += 1
#         else :
#             x += 1
#     if board[x][y] == 2 :
#         board[x][y] = 9
#         break

# for i in range(10) : 
#     for j in range(10) : 
#         print(board[i][j], end=' ') 
#     print()

################# TIME OUT CODE END #################

board = [[0 for i in range(10)] for j in range(10)]


for i in range(10) :
    point = input().split()
    board[i] = list(map(int,point))

x,y = 1,1

while board[x][y] == 0 :
    board[x][y] = 9
    if board[x][y+1] == 0 or board[x][y+1] == 2 :
        y += 1
    else :
        x += 1
    if board[x][y] == 2 :
        board[x][y] = 9

for i in range(10) : 
    for j in range(10) : 
        print(board[i][j], end=' ') 
    print()