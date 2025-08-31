z = int(input())

# def custom_round(x):
#     return int(x) if x - int(x) < 0.5 else int(x) + 1

for _ in range(z):
    r_sum, g_sum, b_sum = 0, 0, 0
    for _ in range(10):
        r, g, b = map(int, input().split())
        r_sum += r
        g_sum += g
        b_sum += b
        
    def custom_round(x):
        return int(x) if x - int(x) < 0.5 else int(x) + 1 

    res_r = custom_round(r_sum / 10)
    res_g = custom_round(g_sum / 10)
    res_b = custom_round(b_sum / 10)
    
    print(res_r, res_g, res_b)