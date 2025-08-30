def lst_2017(rank):
    if rank == 0:
        return 0
    if rank == 1:
        return 500
    if rank <= 3:
        return 300
    if rank <= 6:
        return 200
    if rank <= 10:
        return 50
    if rank <= 15:
        return 30
    if rank <= 21:
        return 10
    return 0

def lst_2018(rank):
    if rank == 0:
        return 0
    if rank == 1:
        return 512
    if rank <= 3:
        return 256
    if rank <= 7:
        return 128
    if rank <= 15:
        return 64
    if rank <= 31:
        return 32
    return 0

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print((lst_2017(a) + lst_2018(b)) * 10000)