#백준 11726: 2xn 타일링

#필요 라이브러리 호출
import sys

#함수
def tiling(n):
    #풀이법: 다이나믹 프로그래밍

    #메모리 공간 할당
    cache = [0] * 1001

    #cache[1],cache[2] 입력
    cache[1] = 1
    cache[2] = 2

    #규칙 부여
    for i in range(3,n+1):
        cache[i] = (cache[i-1] + cache[i-2]) % 10007

    return cache[n]

#입출력
n = int(sys.stdin.readline().rstrip())
print(tiling(n))

