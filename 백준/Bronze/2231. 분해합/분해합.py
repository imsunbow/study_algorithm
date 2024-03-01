#백준 2231: 분해합

#풀이법: 브루트포스 알고리즘
n = int(input())

for i in range(1,n+1):
    num = sum((map(int,str(i)))) #숫자를 str처리후 합 구하기
    num_sum = i + num

#생성자 구하기
    if num_sum == n:
        print(i)
        break
#생성자가 없는 경우
    if i == n: 
        print(0)