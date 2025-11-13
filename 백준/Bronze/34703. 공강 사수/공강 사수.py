classes = []

for _ in range(int(input())):
    classes.append(input().strip())
    
classes_set = set(classes)

print("NO" if len(classes_set) ==  5 else "YES")