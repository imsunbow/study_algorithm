from collections import Counter

def norm(word):
    if len(word) <= 2:
        return word
    else: # sort middle part except first/ last word
        return word[0] + ''.join(sorted(word[1:-1])) + word[-1]
    
n = int(input())
dic = Counter(norm(input().strip()) for _ in range(n))

m = int(input())

for _ in range(m):
    words = input().strip().split()
    res = 1
    for w in words:
        res *= dic[norm(w)]
    print(res)