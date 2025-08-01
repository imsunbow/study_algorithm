while True:
    try:    
        n1, tx, n2 = input().split()
        n1 = int(n1)
        n2 = int(n2)
        if n1 == 0 and n2 == 0 and tx == 'W':
            break
        elif tx == 'W':
            remaining_balance = n1 - n2
            print(remaining_balance if remaining_balance >= -200 else 'Not allowed')
        elif tx == 'D':
            remaining_balance = n1 + n2
            print(remaining_balance)
    except EOFError:
        break