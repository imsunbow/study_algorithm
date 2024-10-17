#백준 1302: 베스트셀러

import collections

n = int(input())

books = []

for _ in range(n):
    book = input()
    books.append(book)

best_seller = collections.Counter(books).most_common() #best seller 구하기
best_seller.sort(key=lambda x: (-x[1],x[0])) #동등 빈도 정렬

print(best_seller[0][0])