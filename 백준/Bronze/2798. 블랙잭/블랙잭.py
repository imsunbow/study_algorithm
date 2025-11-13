n, m = map(int, input().split())

lst = list(map(int, input().split()))

res = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            card_sum = lst[i] + lst[j] + lst[k]
            
            if card_sum <= m:
                lst.append(card_sum)
            

                
print(max(lst[n-1:]))