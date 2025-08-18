n = int(input())
lst = list(map(int, input().split()))

if sum(lst) > 0:
    print("Right")
elif sum(lst) == 0:
    print("Stay")
else:
    print("Left")