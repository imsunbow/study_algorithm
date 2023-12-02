#백준 1357: 뒤집힌 덧셈

a,b = input().split()

a = int(a[::-1])
b = int(b[::-1])
print(int(str(a+b)[::-1]))