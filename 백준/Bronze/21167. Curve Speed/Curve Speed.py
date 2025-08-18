import math

while True:
    try:
        line = input()
        r, s = line.split()
        r = int(r)
        s = float(s)
        v = math.sqrt(r * (s + 0.16) / 0.067)
        print(round(v))    
    except EOFError:
        break