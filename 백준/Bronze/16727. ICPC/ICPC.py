p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

p_total = p1 + p2
s_total = s1 + s2

if p_total == s_total:
    if p1 == s2:
        print("Penalty")
    elif p1 > s2:
        print("Esteghlal")        
    else:
        print("Persepolis")
elif p_total > s_total:
    print("Persepolis")
else:
    print("Esteghlal")