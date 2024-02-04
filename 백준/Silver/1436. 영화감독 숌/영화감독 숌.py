#백준 1436: 영화감독 숌

count = 0
start = 0

N = int(input())
lst = []

while (count < N):
    start += 1

    if "666" in str(start):
        lst.append(start)
        count += 1

print(lst[-1])
