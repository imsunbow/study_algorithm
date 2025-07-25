n = int(input())

has_7 = '7' in str(n)
div_7 = n % 7 == 0

if not has_7 and not div_7:
    print(0)
elif not has_7 and div_7:
    print(1)
elif has_7 and not div_7:
    print(2)
else:
    print(3)