cnt = 0

for _ in range(int(input())):
    s = input()
    if int(s[2:]) <= 90:
        cnt += 1
        
print(cnt)