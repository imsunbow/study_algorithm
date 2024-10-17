#백준 1225: 이상한 곱셈

a,b = map(int,input().split())

a = str(a)
b = str(b)

sum = 0

for i in range(len(a)):
    for j in range(len(b)):
       sum += int(a[i]) * int(b[j])

print(sum)


