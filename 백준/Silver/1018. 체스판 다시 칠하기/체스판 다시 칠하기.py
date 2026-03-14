#백준 1018: 체스판 다시 칠하기

m,n = map(int,input().split())
board = []
for _ in range(m):
    board.append(input())


color = {0:"B",1:"W"}

paint_list = []

#시작점 탐색
for x_start in range(m-7):
    for y_start in range(n-7):

        paint = 0

        paint_w = 0
        paint_b = 0

        for x in range(x_start,x_start+8):
            for y in range(y_start,y_start+8):
                if board[x][y] != color[(x+y)%2]:
                    paint_b += 1

                else:
                    paint_w += 1

        paint = min(paint_b,paint_w)
        paint_list.append(paint)

print(min(paint_list))

