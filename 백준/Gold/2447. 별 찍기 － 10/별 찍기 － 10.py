#백준 2447: 별 찍기 - 10

#함수 구현
def star(k):
    if k == 3: #k = 3일 때
        return ['***','* *','***'] #고정된 패턴 반환

    arr = star(k//3) #패턴생성
    stars = []

    for i in arr: #가로 3배 행 생성
        stars.append(i*3)

    for i in arr: # 가운데 행 생성
        stars.append(i+' '*(k//3)+i)

    for i in arr: # 가로 3배 행 생성
        stars.append(i*3)

    return stars


#출력
print('\n'.join(star(int(input()))))







