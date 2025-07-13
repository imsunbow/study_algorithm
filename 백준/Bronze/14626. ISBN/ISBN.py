# 백준 14626: isbn

isbn = input()
weights = [1 if i % 2 == 0 else 3 for i in range(12)]
missing_idx = isbn.index('*')

weighted_sum = sum(
    int(isbn[i]) * weights[i]
    for i in range(12) if i != missing_idx
)

check_digit = int(isbn[-1]) # check digit at the end of the isbn

for replacement in range(10):
    total = weighted_sum + (replacement * weights[missing_idx])
    if (total + check_digit) % 10 == 0:
        print(replacement)
        break