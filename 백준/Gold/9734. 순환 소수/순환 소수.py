import fractions
import sys

input = sys.stdin.readline

def convert(s):
    s = s.strip()  
    start = s.find('(')
    end = s.find(')')
    
    non_repeat = s[:start]
    repeat = s[start+1:end]
    
    dot = non_repeat.find('.')
    
    if dot == -1:
        integer = non_repeat
        decimal = ""
    else:
        integer = non_repeat[:dot]
        decimal = non_repeat[dot+1:]
    
    # if not integer:
    #     integer = "0"
    # if not decimal:
    #     decimal = ""
    # if not repeat:
    #     return fractions.Fraction(0)
    
    try:
        full_num = int(integer + decimal + repeat)
        non_repeat_str = integer + decimal
        non_repeat_num = int(non_repeat_str) if non_repeat_str else 0
    except ValueError:
        return fractions.Fraction(0)
    
    numerator = full_num - non_repeat_num
    denominator = int('9' * len(repeat) + '0' * len(decimal))
    
    return fractions.Fraction(numerator, denominator)

while True:
    try:
        s = input()  
        if not s:
            break
        result = convert(s)
        print(f"{s.strip()} = {result.numerator} / {result.denominator}")
    except EOFError:
        break