k = int(input())
text = input()

answer = ""
for i, ch in enumerate(text):
    shift = k + 3 * (i + 1)
    new_ch = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
    answer += new_ch

print(answer)