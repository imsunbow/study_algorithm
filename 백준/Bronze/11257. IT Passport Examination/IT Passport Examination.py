n = int(input())

for _ in range(n):
    id, t1, t2, t3 = map(int, input().split())
    if t1 + t2 + t3 >= 55 and t1 >= 10.5 and t2 >= 7.5 and t3 >= 12:
        print(id, t1 + t2 + t3, "PASS")
    else:
        print(id, t1 + t2 + t3, "FAIL")    