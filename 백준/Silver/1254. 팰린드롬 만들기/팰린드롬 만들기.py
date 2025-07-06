s = input();n = len(s)
for i in range(n):
    if s[i:] == s[i:][::-1]:
        print(n + i)
        break