n = int(input())
scores = [[0,0,0]] # 바닥 설정. index를 계단 층수로 세기 위해서임.

for i in range(0,n) :
    new = [int(input()),0,0]
    scores.append(new)

if (n > 1) :
    # scores[i][0] : i번째 계단을 선택, i+1번째 계단은 선택하지 않음
    # scores[i][1] : i번째 계단을 선택하지 않음
    # scores[i][2] : i번째 계단과 i+1번째 계단 모두를 선택

    # 마지막 계단은 반드시 밟아야 함.
    scores[n-1][1] = scores[n][0]
    scores[n-1][2] = scores[n-1][0] + scores[n][0]
    scores[n-1][0] = -999

    for i in range(n-2,0,-1) :
        origin = scores[i][0]
        scores[i][0] += scores[i+1][1]
        scores[i][1] = max(scores[i+1][0], scores[i+1][2])
        scores[i][2] = origin + scores[i+1][0]

print(max(scores[1][0], scores[1][1], scores[1][2]))