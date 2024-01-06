#백준 4344: 평균은 넘겠지

C = int(input())

for _ in range(C):
    nums = list(map(int,input().split()))
    avg = sum(nums[1:]) / nums[0] # 평균 구하기

    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1

    rate = (cnt / nums[0]) * 100 # 백분율 변환

    print(f'{rate:.3f}%') #출력