T = int(input())
for _ in range(T):
    P, M = map(int, input().split())
    taken_seats = set()
    seated = 0

    for _ in range(P):
        seat = int(input())
        if seat not in taken_seats:
            taken_seats.add(seat)
            seated += 1

    print(P - seated)
