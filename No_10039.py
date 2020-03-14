# 평균점수

score = 0
for _ in range(5) :
    sc = int(input())
    if sc < 40 :
        sc = 40

    score += sc

print(score // 5)