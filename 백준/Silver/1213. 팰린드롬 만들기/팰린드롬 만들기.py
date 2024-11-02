# 백준 1213 : 팰린드롬 만들기
import collections

word = input()
check_word = collections.Counter(word)

# 홀수 개수의 문자가 몇 개 있는지 확인
odd_count = 0
mid = ''
result = ''

# 홀수 개수의 문자를 확인하여 처리
for char, count in check_word.items():
    if count % 2 != 0:
        odd_count += 1
        mid = char
    # 홀수 개수의 문자가 2개 이상이면 팰린드롬 불가
    if odd_count > 1:
        print("I'm Sorry Hansoo")
        exit()

# 사전순으로 정렬 후 결과 만들기
for char, count in sorted(check_word.items()):
    result += char * (count // 2)

# 결과 출력
print(result + mid + result[::-1])
