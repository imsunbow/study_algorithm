n = int(input())
print(3 if '7' in str(n) and n % 7 == 0 else 2 if '7' in str(n) else 1 if n % 7 == 0 else 0)