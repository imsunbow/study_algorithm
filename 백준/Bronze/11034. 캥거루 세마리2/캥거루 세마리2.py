while True:
    try:
        lst = list(map(int, input().split()))
        if lst == [0, 0, 0]:
            break
        lst.sort()
        print(max(lst[1] - lst[0], lst[2] - lst[1]) - 1)
    except EOFError:
        break