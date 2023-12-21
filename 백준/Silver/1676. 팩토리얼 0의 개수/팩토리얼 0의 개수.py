#백준 1676: 팩토리얼 0의 개수

from math import factorial

N = int(input())
result = factorial(N)
count = 0

result_str = str(result) #문자열로 변환

for i in range(1, len(result_str)+1):
    if result_str[-i] == '0':
        count+=1
    else:
        print(count)
        break

