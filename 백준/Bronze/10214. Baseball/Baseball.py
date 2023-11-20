#백준 10214

T = int(input())

for _ in range(T):
    yonsei_total_score = 0
    korea_total_score = 0
    for _ in range(9):
        yonsei_score, korea_score = map(int,input().split())
        yonsei_total_score += yonsei_score
        korea_total_score += korea_score

    if yonsei_total_score > korea_total_score:
        print("Yonsei")
    elif yonsei_total_score == korea_total_score:
        print("Draw")
    else:
        print("Korea")








