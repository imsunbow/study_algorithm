lst = []

for _ in range(int(input())):
    lst.append(int(input()))
    
sorted_lst = sorted(lst)
if lst[0] == sorted_lst[0]:
    print("ez")
elif lst[0] == sorted_lst[-1]:
    print("hard")
else:
    print("?")