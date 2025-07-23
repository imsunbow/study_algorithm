# 백준 2985 : 세 수 

a, b, c = map(int, input().split())

# This part was optimized with assistance from ChatGPT.
ops = [('+', lambda x, y: x + y),
       ('-', lambda x, y: x - y),
       ('*', lambda x, y: x * y),
       ('/', lambda x, y: x / y if y != 0 else None)]

for sym, op in ops:
    if op(a, b) == c: # case 1 : operation result equals c
        print(f"{a}{sym}{b}={c}")
        break 
    if op(b, c) == a: # case 2 : operation result equals a
        print(f"{a}={b}{sym}{c}")
        break