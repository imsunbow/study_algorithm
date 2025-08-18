sleep = int(input())
wake_up = int(input())

time = wake_up - sleep

print(time if time >= 0 else time + 24)