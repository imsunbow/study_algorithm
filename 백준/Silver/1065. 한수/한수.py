#백준 1065: 한수

n = int(input())
answer = 0

for i in range(1,n+1):
    if i < 100: #99까지는 모두 한수
        answer += 1
    else:
        nums = list(map(int,str(i)))
        if nums[2] - nums[1] == nums[1] - nums[0]: #등차수열
                answer += 1

print(answer)