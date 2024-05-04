#백준 13909 : 창문 닫기

#입력
import sys
N = int(sys.stdin.readline())

#초기값 설정 : 결과 = 0, 시작지점 = 1
res = 0
fir = 1

#반복문 : n에 닿을 때까지 fir,res를 계속 늘려가며 실행
while fir*fir <= N:
    fir += 1
    res += 1

#출력
print(res)