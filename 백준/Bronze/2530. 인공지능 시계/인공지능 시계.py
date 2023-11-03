hour, minute, second = map(int, input().split())

add = int(input())

second += add
minute += second // 60
hour += minute // 60
print(hour%24 , minute%60, second%60)



