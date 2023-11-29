#백준 2501


N, K =map(int,input().split())
divisor_list = []

for i in range(1, N+1):
    if N % i == 0:
        divisor_list.append(i)
    else:
        continue

if K <= len(divisor_list):
    print(divisor_list[K-1])
else:
    print(0)

