from collections import deque

s = input()
t = input()

queue = deque([t])
visited = set([t])

found = False

while queue and not found:
    current = queue.popleft()
    
    if current == s:
        found = True
        break
    
    if len(current) <= len(s):
        continue
    
    # if str end with A -> remove a 
    if current[-1] == 'A':
        next_str = current[:-1]
        if next_str not in visited:
            visited.add(next_str)
            queue.append(next_str)
    
    # if str start with B -> reverse b and remove b
    if current[0] == 'B':
        reversed_str = current[::-1]
        next_str = reversed_str[:-1]
        if next_str not in visited:
            visited.add(next_str)
            queue.append(next_str)

print(1 if found else 0)