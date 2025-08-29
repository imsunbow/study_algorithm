n1, n2, n3 = map(int, input().split())

if n1 + n2 == n3 or n2 + n3 == n1 or n1 + n3 == n2:
    print(1)
elif n1 * n2 == n3 or n2 * n3 == n1 or n1 * n3 == n2:
    print(2)
else:
    print(3)