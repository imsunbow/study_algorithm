s = input()
n = len(s)

a_count = s.count('a')

if a_count == 0 or a_count == n:
    print(0)
else:
    circular_s = s + s
    min_swaps = a_count # worst case
    
    for i in range(n):
        window = circular_s[i: i + a_count]
        b_count = window.count('b')
        min_swaps = min(min_swaps, b_count)
        
    print(min_swaps)