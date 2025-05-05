#백준 2812: 크게 만들기

n, k = map(int, input().split())
num = list(input())

ans = []

for i in num:
    while ans and ans[-1] < i and k > 0:
        ans.pop()
        k -= 1
    ans.append(i)

print("".join(ans[:len(ans) - k])) #연결