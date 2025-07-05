#백준 5525 : ioioi

import sys
input = sys.stdin.readline

n = int(input())
t = int(input())
str = input().strip()

count = 0
i = 0
pattern = 0

while i < t - 1: 
    if str[i] == 'I' and str[i+1] == 'O':
        temp = 0
        while i+2 < t and str[i+1] == 'O' and str[i+2] == 'I':
            temp += 1
            i += 2 #matched -> 2 steps forward
            if temp == n:
                count += 1
                temp -= 1
        i += 1
    else:
        i += 1

print(count)