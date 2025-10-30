import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

lst_total = lst_a + lst_b

lst_total.sort()

print(*lst_total)