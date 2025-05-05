#백준 14003: 가장 긴 증가하는 부분 수열 5

import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [arr[0]] #dp
index = [0] #dp에 들어간 값의 인덱스를 저장

for i in range(1, n): #dp에 들어갈 값 찾기
    if arr[i] > dp[-1]: #dp의 마지막 값보다 크다면
        dp.append(arr[i]) #dp에 추가
        index.append(len(dp)-1) #인덱스 저장
    else:
        idx = bisect_left(dp, arr[i]) #이진탐색으로 들어갈 위치 찾기
        dp[idx] = arr[i] #값 변경
        index.append(idx) #인덱스 저장
        
#정답 복원
lis_length = len(dp)
lis = [0] * lis_length
idx = lis_length - 1

for i in range(n - 1, -1, -1): #뒤에서부터 탐색
    if index[i] == idx: #인덱스 값이 같다면
        lis[idx] = arr[i] #정답에 추가
        idx -= 1 #인덱스 값 -1 후 탐색 계속

print(lis_length) #dp의 길이
print(*lis) #정답 출력