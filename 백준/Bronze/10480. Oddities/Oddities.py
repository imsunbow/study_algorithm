#벡준 10480: oddities

n = int(input())

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd ")