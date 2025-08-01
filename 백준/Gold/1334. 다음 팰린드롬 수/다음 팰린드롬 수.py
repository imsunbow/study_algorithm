import sys

input = sys.stdin.readline

def get_next_palindrome(num_str):
    n = len(num_str)
    num = int(num_str)
    
    if num < 9:
        return str(num + 1)
    if num == 9:
        return "11"
    
    mid = n // 2
    is_odd = n % 2
    
    # make candidate palindrome by mirroing the left half
    left = num_str[:mid + is_odd]    
    mirrored = left[:mid][::-1]
    candidate = left + mirrored
    
    # if candidate is greater than num, return it (it is the next palindrome)
    if int(candidate) > num:
        return candidate
    
    # else: increment the left half and mirror again
    left_int = int(left) + 1
    left_str = str(left_int)

    # re-mirror the left half till it fits the original length
    if len(left_str) > len(left):
        return "1" + "0" * (n - 1) + "1"
        
    return left_str + left_str[:mid][::-1]

num_str = input().strip()
print(get_next_palindrome(num_str))