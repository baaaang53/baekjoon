# 점수 계산

scores = []
for i in range(1,9) :
    sc = int(input())
    scores.append([sc, i])


scores.sort(reverse = True)

ans  =[]
total = 0
for i in range(5) :
    total += scores[i][0]
    ans.append(scores[i][1])

print(total)
ans.sort()
for elem in ans :
    print(elem, end = " ")