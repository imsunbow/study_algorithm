def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)
            
for _ in range(int(input())):
    n = int(input())
    res = fact(n)
    res_str = str(res)
    print(res_str[-1])