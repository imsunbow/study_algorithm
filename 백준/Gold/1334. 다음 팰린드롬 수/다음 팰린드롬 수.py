import sys

input = sys.stdin.readline

# def is_palindrome(s):
#     return s == s[::-1]

def get_next_palindrome(num_str):
    n = len(num_str)
    num = int(num_str)
    
    if num < 9:
        return str(num + 1)
    if num == 9:
        return "11"
    
    mid = n // 2
    is_odd = n % 2
    
    left = num_str[:mid + is_odd]
    right = num_str[mid + is_odd:]
    
    mirrored = left[:mid][::-1]
    candidate = left + mirrored
    
    if int(candidate) > num:
        return candidate
    
    left_int = int(left) + 1
    left_str = str(left_int)
        
    left_str = left_str.zfill(len(left))
    return left_str + left_str[:mid][::-1]

num_str = input().strip()
print(get_next_palindrome(num_str))