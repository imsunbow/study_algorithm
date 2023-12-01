#백준 2711 오타맨 고창영

S = int(input())

for _ in range(S):
    a,b = input().split()
    a = int(a)

    text = b[:a-1] + b[a:]
    print(text)




