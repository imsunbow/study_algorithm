n = int(input())
k = int(input())

total_allocation = k + 60 

if n <= total_allocation:
    cost = n * 1500
else:
    regular = total_allocation
    extra = n - total_allocation
    cost = regular * 1500 + extra * 3000

print(cost)