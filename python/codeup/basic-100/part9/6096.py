board = [
  [0 for i in range(20)] for j in range(20)
]

for i in range(0, 19):
    nums = input().split()
    board[i] = list(map(int, nums))

repeat = int(input())

for i in range(0, repeat):
    point = input().split()
    point = list(map(int, point))
    x = point[0] - 1
    y = point[1] - 1

    for j in range(0, 19) :
        if (board[x][j]) == 0 :
            board[x][j] = 1 
        else :
            board[x][j] = 0
    for k in range(0, 19) :
        if (board[k][y]) == 0 :
            board[k][y] = 1
        else :
            board[k][y] = 0

for i in range(0, 19) :
    for j in range(0, 19) :
        print(board[i][j], end = " ")
    print()