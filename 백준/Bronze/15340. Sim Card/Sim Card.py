#백준 15340: Sim Card

while True:
    call,data = map(int,input().split())
    if call == 0 and data == 0:
        break
    else:
        print((min(call*30+data*40,call*35+data*30,call*40+data*20)))

