#백준 23971 : ZOAC 4

H, W, N, M = map(int, input().split())

vertical_seats = 1 + (H - 1) // (N + 1)

horizontal_seats = 1 + (W - 1) // (M + 1)

max_capacity = vertical_seats * horizontal_seats

print(max_capacity)


