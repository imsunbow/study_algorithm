#백준 2108: 통계학

from collections import Counter #필요 라이브러리 호출: 최빈값 구할 때 사용

N = int(input())
nums_list = []

#입력 및 저장
for _ in range(N):
    word = int(input())
    nums_list.append(word)

nums_list.sort() #오름차순 정렬

#산술평균
average = sum(nums_list) / N
round_average = round(average) #반올림된 결과값
print(round_average)

#중앙값
mid = N // 2
mid_number = nums_list[mid]
print(mid_number)

#최빈값
counter = Counter(nums_list)
max_count = max(counter.values())  # 최대 빈도수

#최빈값이 여러 개일 경우 모든 최빈값을 저장
mode_list = [num for num, count in counter.items() if count == max_count]

#최빈값이 한 개 이상일 때
if len(mode_list) > 1:
    mode_list.sort()  #최빈값이 여러 개일 경우, 가장 작은 값을 출력하기 위해 정렬
    mode = mode_list[1]  #두 번째로 작은 최빈값을 선택
else:
    mode = mode_list[0]

print(mode)

#범위
range = nums_list[N-1] - nums_list[0]
print(range)