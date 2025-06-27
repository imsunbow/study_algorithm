s = input().strip()

# 최대값
max_ans = ''
cnt = 0
for c in s:
    if c == 'M':
        cnt += 1
    else:  # 'K'
        if cnt > 0:
            max_ans += '5' + '0' * cnt
        else:
            max_ans += '5'
        cnt = 0
if cnt > 0:
    max_ans += '1' * cnt

# 최소값
min_ans = ''
cnt = 0
for c in s:
    if c == 'M':
        cnt += 1
    else:  # 'K'
        if cnt > 0:
            min_ans += '1' + '0' * (cnt - 1)
        min_ans += '5'
        cnt = 0
if cnt > 0:
    min_ans += '1' + '0' * (cnt - 1)

print(max_ans)
print(min_ans)