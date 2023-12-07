#백준 5218 :  알파벳 거리

T = int(input())

for _ in range(T):
    s = []
    a,b = map(list,input().split())
    for i in range(len(a)):
        if ord(a[i])<=ord(b[i]):
            s.append(ord(b[i]) - ord(a[i]))
        else:
            s.append(ord(b[i])+26-ord(a[i]))
    print("Distances: ", end='')
    for i in s:
        print(i, end=' ')
    print()





