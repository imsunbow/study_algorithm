#백준 10867: 중복 빼고 정렬하기

N = int(input())

numbers = list(map(int,input().split()))
numbers = list(set(numbers))
numbers.sort()

for i in numbers:
    print(i,end=' ')