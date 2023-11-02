t = int(input())

for i in range(1,t+1):
  a, b = map(int,input().split())

  result = a + b
  print(f"Case #{i}: {a} + {b} = {result}")