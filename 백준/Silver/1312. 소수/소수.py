#백준 1312: 소수

#입력
a,b,n = map(int,input().split())

#손으로 푸는 나눗셈 연산 구하기
for _ in range(n):
    a = (a%b)*10
    result = a//b #int 처리

print(result) #n번째 숫자 반환