#백준 11367: Report Card Time

for _ in range(int(input())):
    name,s = input().split()
    score = int(s)

    #출력
    if score >= 97 and score <= 100:
        print(name,"A+")
    elif score >= 90 and score <= 96:
        print(name,"A")
    elif score >= 87 and score <= 89:
        print(name,"B+")
    elif score >= 80 and score <= 86:
        print(name,"B")
    elif score >= 77 and score <= 79:
        print(name,"C+")
    elif score >= 70 and score <= 76:
        print(name,"C")
    elif score >= 67 and score <= 69:
        print(name,"D+")
    elif score >= 60 and score <= 66:
        print(name,"D")
    elif score >= 0 and score <= 59:
        print(name,"F")




