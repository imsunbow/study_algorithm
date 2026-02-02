cnt = 0

while True:
    try:
        words = input()
        cnt += 1
    except EOFError:
        break
    
print(cnt)