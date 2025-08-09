t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    
    for _ in range(n):
        cloth, type = input().split()
        if type in clothes:
            clothes[type] += 1
        else:
            clothes[type] = 1
            
    result = 1
    
    for cnt in clothes.values(): 
        result *= (cnt + 1)
        
    print(result - 1)