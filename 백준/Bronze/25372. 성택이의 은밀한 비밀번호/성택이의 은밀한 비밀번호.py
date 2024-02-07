#백준 25372: 성택이의 은밀한 비밀번호

for _ in range(int(input())):
    a = input()
    if len(a) > 9 or len(a) < 6:
        print("no")
    else:
        print("yes")