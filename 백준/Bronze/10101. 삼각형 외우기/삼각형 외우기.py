#백준 10101: 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b == c == 60:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    elif a != b and a != c and b != c:
        print("Scalene")
else:
    print("Error")



