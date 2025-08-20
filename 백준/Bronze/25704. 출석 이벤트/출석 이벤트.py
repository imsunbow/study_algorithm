n = int(input())
p = int(input())

coupon = [p]

if n >= 5:
    coupon.append(p - 500)
if n >= 10:
    coupon.append(p * 0.9)
if n >= 15:
    coupon.append(p - 2000)
if n >= 20:
    coupon.append(p * 0.75)
    
print(int(min(max(0, x) for x in coupon)))