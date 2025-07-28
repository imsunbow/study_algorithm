k = int(input())

icon = [
    "*x*",
    " xx",
    "* *"
]

for line in icon:
    scaled_line = ''.join(ch * k for ch in line)
    
    for _ in range(k):
        print(scaled_line)