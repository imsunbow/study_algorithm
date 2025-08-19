cnt = 0

jinho = input()
for _ in range(int(input())):
    friend = input()
    if friend == jinho:
        cnt += 1
        
print(cnt)