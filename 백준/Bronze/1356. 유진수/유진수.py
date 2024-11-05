# 백준 1356: 유진수

n = input()
is_yujinsu = False

for i in range(1, len(n)):
    left, right = n[:i], n[i:]
    product_left = product_right = 1

    for digit in left:
        product_left *= int(digit)
    for digit in right:
        product_right *= int(digit)

    if product_left == product_right:
        is_yujinsu = True
        break

print("YES" if is_yujinsu else "NO")
