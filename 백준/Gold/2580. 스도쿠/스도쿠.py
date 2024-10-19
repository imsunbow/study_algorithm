#백준 2580: 스도쿠

sudoku = [list(map(int, input().split())) for _ in range(9)]

cells = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            cells.append((i, j))

def check(x, y, num):
    for i in range(9):
        if sudoku[y][i] == num:
            return False
        if sudoku[i][x] == num:
            return False
    
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[ny + i][nx + j] == num:
                return False
    return True

def dfs(idx):
    if idx == len(cells):
        return True
    
    y, x = cells[idx]
    for num in range(1, 10):
        if check(x, y, num):
            sudoku[y][x] = num
            if dfs(idx + 1):
                return True
            sudoku[y][x] = 0
    
    return False

dfs(0)

for row in sudoku:
    print(*row)
