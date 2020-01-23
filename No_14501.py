N = int(input())
table = [[0,0]]
#price[i][0] : i를 선택했을 때 최대 비용
#price[i][1] : i를 선택하지 않았을 때의 최대 비용
price = [[0,0] for i in range(0,N+1)]
maxi = 0

for i in range(0,N) :
    inp = input().split()
    inp = [int(k) for k in inp]
    table.append(inp)


for i in range(N,0,-1) :
    # 마지막날에 딱 맞게 끝난다면
    if ((i + table[i][0]) == N+1) :
        price[i][0] = table[i][1]

    # 마지막날보다 먼저 끝난다면
    elif ((i + table[i][0]) < N+1):
        next = i + table[i][0]
        price[i][0] = table[i][1] + max(price[next][0],price[next][1])

    if (i != N) :
        price[i][1] = max(price[i + 1][0], price[i + 1][1])


for i in range(1,N+1) :
    if maxi < price[i][0] :
        maxi = price[i][0]

print(maxi)

