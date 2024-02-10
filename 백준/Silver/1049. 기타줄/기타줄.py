#백준 1049: 기타줄

n, m = map(int, input().split())

answer = 0
price_list = []

# 가격 입력
for _ in range(m):
    price = tuple(map(int, input().split()))
    price_list.append(price)

# 최소 패키지와 낱개의 가격을 정렬
six_list = sorted(price_list, key=lambda x: x[0])
one_list = sorted(price_list, key=lambda x: x[1])

# 패키지로만 살 수 있는 경우와 낱개로만 살 수 있는 경우를 비교
package_price = six_list[0][0]
single_price = one_list[0][1]

# 패키지로만 살 때의 가격
package_cost = (n // 6) * package_price + (n % 6) * single_price

# 낱개로만 살 때의 가격
single_cost = n * single_price

# 혼합해서 살 때의 가격
mixed_cost = ((n // 6) + 1) * package_price

# 최소 가격을 선택
answer = min(package_cost, single_cost, mixed_cost)

print(answer)
