# 백준 9772: quadrants

while True:
    x,y = map(float, input().split())

    if x == 0 and y == 0:
        print("AXIS")
        break
    elif x == 0 and y != 0:
        print("AXIS")
    elif y == 0 and x != 0:
        print("AXIS")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:   
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")
