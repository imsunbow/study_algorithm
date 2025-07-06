# 백준 16017: telemarketer or not?

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1 == 8 or num1 == 9:
    if num2 == num3:
        if num4 == 8 or num4 == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
