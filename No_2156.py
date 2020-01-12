n = int(input())
wine = []

for i in range(0,n) :
    k = [int(input()), 0, 0]
    wine.append(k)

if (n > 1) :
    # wine[i][0] : i번째 와인 선택, i+1은 선택하지 않았을 때의 와인 양
    # wine[i][1] : i번째 와인을 선택하지 않았을 때 마시는 양 (i+1은 선택했는지 관심 없음)
    # wine[i][2] : i번째 와인과 i+1번째 와인을 모두 선택했을 때 와인의 양
    wine[n-2][1] = wine[n-1][0]
    wine[n-2][2] = wine[n-2][0] + wine[n-1][0]

    for i in range(n-3, -1, -1) :
        orig = wine[i][0]
        wine[i][0] +=  wine[i+1][1]
        wine[i][1] = max(wine[i+1][0], wine[i+1][1], wine[i+1][2])
        wine[i][2] = orig + wine[i+1][0]

print (max(wine[0][0], wine[0][1], wine[0][2]))