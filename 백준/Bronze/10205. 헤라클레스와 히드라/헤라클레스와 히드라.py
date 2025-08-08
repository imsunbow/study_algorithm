k = int(input())

for i in range(1, k + 1):
    h = int(input())
    s = input()
    for j in range(len(s)):
        if s[j] == 'c':
            h += 1
        elif s[j] == 'b':
            h -= 1

    print(f"Data Set {i}:")
    print(h)
    print()