#백준 10886

N = int(input())
yes = 0
no = 0

for _ in range(N):
    opinion = int(input())
    if opinion == 1:
        yes += 1
    else:
        no += 1

if yes > no:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
