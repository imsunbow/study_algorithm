#백준 3058 짝수를 찾아라

T = int(input())

for _ in range(T):
    a = list(map(int,input().split()))
    numbers = []
    for i in a:
        if i % 2 ==0:
            numbers.append(i)
    print(sum(numbers), min(numbers))

