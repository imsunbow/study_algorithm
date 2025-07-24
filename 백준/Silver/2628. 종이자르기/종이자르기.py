# 백준 2628: 종이 자르기

width, height = map(int, input().split())
cut_cnt = int(input())

hor_cuts = [0, height]
ver_cuts = [0, width]

for _ in range(cut_cnt):
    direction, pos = map(int, input().split())
    if direction == 0:
        hor_cuts.append(pos)
    else:
        ver_cuts.append(pos)

hor_cuts.sort()
ver_cuts.sort()

max_height = max(hor_cuts[i] - hor_cuts[i - 1] for i in range(1, len(hor_cuts)))
max_width = max(ver_cuts[i] - ver_cuts[i - 1] for i in range(1, len(ver_cuts)))

print(max_height * max_width)