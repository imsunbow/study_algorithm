#백준 1408: Tournament Selection

cnt = 0

for _ in range(6):
    a = input()
    if a == "W":
        cnt += 1
    else:
        continue

#출력
if cnt >= 5:
    print("1")
elif cnt >= 3 and cnt < 5:
    print("2")
elif cnt >= 1 and cnt < 3:
    print("3")
else:
    print("-1")

