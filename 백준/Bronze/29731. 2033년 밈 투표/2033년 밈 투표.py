n = int(input())

cnt = 0

memes = ['Never gonna give you up', 'Never gonna let you down', 'Never gonna run around and desert you', 'Never gonna make you cry', 'Never gonna say goodbye', 'Never gonna tell a lie and hurt you', 'Never gonna stop']

for _ in range(n):
    meme = input()
    if meme not in memes:
        print("Yes")
        break
    else:
        cnt += 1
        continue
    
if cnt == n:
    print("No")