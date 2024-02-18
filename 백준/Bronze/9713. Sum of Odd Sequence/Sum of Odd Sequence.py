#백준 9713: 홀수열의 합

for _ in range(int(input())):
    a = int(input())
    print(sum([i for i in range(1, a+1) if i % 2]))