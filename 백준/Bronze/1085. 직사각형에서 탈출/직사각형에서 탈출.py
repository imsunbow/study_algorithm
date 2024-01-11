#백준 1085: 직사각형에서 탈출

x,y,w,h = map(int,input().split())

dots = [] #list 생성

#최소값 경우의 수 : 4가지
dots.append(x) 
dots.append(w-x)
dots.append(y)
dots.append(h-y)

dots.sort() #오름차순 정렬
print(dots[0]) #0번 인덱스 출력 >> 최소값






