n,w,h,l = map(int, input().split())

print(min(int((w/l)) * int((h/l)),n))