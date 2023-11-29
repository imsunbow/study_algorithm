#백준 2921

T = int(input())
res = 0

for i in range(1, T+1):
    res += 1.5 * i * (i+1)

print(int(res))

