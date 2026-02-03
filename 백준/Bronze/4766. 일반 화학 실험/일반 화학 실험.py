lst = []

while True:
    a = float(input())
    if a == 999:
        break
    lst.append(a)
    
for i in range(len(lst) - 1):
    res = lst[i+1] - lst[i]
    print(f"{res:.2f}")
    