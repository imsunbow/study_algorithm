k = int(input())

for i in range(k):
    n, s, d = map(int, input().split())
    total_value = 0
    
    for j in range(n):
        distance, value = map(int, input().split())
        if distance <= s * d:
            total_value += value
    
    print(f"Data Set {i + 1}:")
    print(total_value)
    print()