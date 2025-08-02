t = int(input())

res = 0

for _ in range(t):
    s = input().strip()
    a = s.count('a')
    b = s.count('b')
    
    res = min(a, b)
    
    print(res)