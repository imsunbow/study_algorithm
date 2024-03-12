#백준 17094: Serious Problem

cnt2 = 0
cnte = 0

t = int(input())
s = input()

#계산
for i in range(0,t):
    if s[i] == "2":
        cnt2 +=1
    else:
        cnte +=1

#출력
if cnt2>cnte:
    print("2")
elif cnt2 ==cnte:
    print("yee")
else:
    print("e")