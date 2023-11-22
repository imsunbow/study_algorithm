#백준 5086

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    elif a % b != 0:
        print("neither")