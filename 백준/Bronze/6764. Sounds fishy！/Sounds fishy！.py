#백준 6764: sounds fishy!

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if n1 < n2 < n3 < n4:
    print("Fish Rising")
elif n1 > n2 > n3 > n4:
    print("Fish Diving")
elif n1 == n2 == n3 == n4:
    print("Fish At Constant Depth")
else:
    print("No Fish")