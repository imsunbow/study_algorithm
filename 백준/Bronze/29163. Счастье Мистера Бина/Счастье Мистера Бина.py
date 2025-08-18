odd_cnt = 0
even_cnt = 0

n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    if numbers[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

print('Happy' if even_cnt > odd_cnt else 'Sad')
