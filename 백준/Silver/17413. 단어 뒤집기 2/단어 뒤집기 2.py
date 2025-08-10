import re

s = input()

def reverse_word(match):
    return match.group()[::-1]

result = re.sub(r'<[^>]*>|(\w+)', # if <tag> return <tag> else reverse word
                lambda m: m.group() if m.group().startswith('<') else m.group()[::-1], 
                s)

print(result)

# got a help from this link below (re library) 
# https://docs.python.org/3/library/re.html