import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_safe_area = 0

empty_spaces = []
virus_positions = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0: # empty space
            empty_spaces.append((i, j)) 
        elif board[i][j] == 2: # virus
            virus_positions.append((i, j))

# print(empty_spaces)
# print(virus_positions)

def spread_virus():
    temp_board = [row[:] for row in board]
    
    queue = deque(virus_positions)
    
    while queue:
        row, col = queue.popleft()
        
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            
            if 0 <= nr < n and 0 <= nc < m and temp_board[nr][nc] == 0:
                temp_board[nr][nc] = 2
                queue.append((nr, nc))
    
    safe_count = 0
    
    for i in range(n):
        for j in range(m):
            if temp_board[i][j] == 0:
                safe_count += 1
    
    return safe_count  # safe_count 반환

# max_safe_area = 0  >> wrong initialization (should be global variable)

def build_walls(wall_count, start_idx):
    global max_safe_area
    
    if wall_count == 3: # if all given walls are built
        safe_area = spread_virus() # spread virus and calculate the amount of safe area
        max_safe_area = max(max_safe_area, safe_area)
        return
    
    for i in range(start_idx, len(empty_spaces)):
        row, col = empty_spaces[i]
        board[row][col] = 1  
        build_walls(wall_count + 1, i + 1)
        board[row][col] = 0 
        
build_walls(0, 0)
print(max_safe_area)