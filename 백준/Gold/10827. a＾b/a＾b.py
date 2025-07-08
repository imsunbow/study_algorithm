# 백준 10827 : a ^ b

import decimal

decimal.getcontext().prec = 10**5

a,b = map(decimal.Decimal, input().split())
res = a ** b

res_acc = f'{res:.100000f}'.rstrip('0').rstrip('.')
print(res_acc)