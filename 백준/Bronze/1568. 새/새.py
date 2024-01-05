#백준 1568: 새

N = int(input())
count = 0

k = 1

while N > 0:
    if k > N:
        k = 1
    N -= k
    k += 1
    count += 1

print(count)