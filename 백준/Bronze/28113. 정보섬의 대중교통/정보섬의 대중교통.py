n, a, b = map(int, input().split())
print("Bus" if a < b else "Subway" if a > b else "Anything")