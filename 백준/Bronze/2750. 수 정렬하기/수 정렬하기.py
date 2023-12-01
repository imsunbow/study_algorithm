#백준 9086 문자열

T = int(input())
numbers_list = [] #리스트 생성

for i in range(T): #리스트에 수 입력
    number = int(input())
    numbers_list.append(number)

numbers_list.sort() #정렬

for number in numbers_list: #출력
    print(number)
