i = 0

while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    i += 1
    total = (v // p) * l + min(v % p, l) 
    print(f"Case {i}: {total}")