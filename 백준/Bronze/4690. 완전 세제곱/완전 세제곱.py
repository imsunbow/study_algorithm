for a in range(2, 101):      
    a3 = a**3
    for b in range(2, a):
        b3 = b**3
        for c in range(b+1, a):
            c3 = c**3
            for d in range(c+1, a):
                s = b3 + c3 + d**3
                if s == a3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                elif s > a3:
                    break
