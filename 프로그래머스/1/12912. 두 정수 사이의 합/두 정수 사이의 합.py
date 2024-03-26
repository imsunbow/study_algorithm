def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    
    total = sum(range(start, end + 1))
    
    return total
