socks = [int(input()) for _ in range(5)]

for sock in set(socks):
    while socks.count(sock) >= 2:
        socks.remove(sock)
        socks.remove(sock)
        
print(socks[0]) # remaining sock 