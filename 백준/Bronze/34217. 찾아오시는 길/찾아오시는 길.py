a, b = map(int, input().split())
c, d = map(int, input().split())

print("Hanyang Univ." if a + c < b + d else "Yongdap" if a + c > b + d else "Either")