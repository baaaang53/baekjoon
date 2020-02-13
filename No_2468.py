#안전 영역

import sys

N = int(input())
village = []
check = [[0]*N for i in range(0,N)] #방문 체크용
M = -99 #모든 곳이 물에 잠기는 강수량 저장
safezone = 1
queue = []

def isEmpty(list) :
    return (len(list) == 0)

def bfs(i,j,water) :
    queue.append([i,j])
    while (isEmpty(queue) == False) :
        [x,y] = queue.pop(0)

        if check[x][y] != water :
            check[x][y] = water

            #동
            if (y != N-1) :
                if (village[x][y+1] - water > 0 and check[x][y+1] != water) :
                    queue.append([x,y+1])
            #서
            if (y != 0) :
                if (village[x][y-1] - water > 0 and check[x][y-1] != water) :
                    queue.append([x,y-1])
            #남
            if (x != N-1) :
                if (village[x+1][y] - water > 0 and check[x+1][y] != water) :
                    queue.append([x+1,y])
            #북
            if (x != 0) :
                if (village[x-1][y] - water > 0 and check[x-1][y] != water) :
                    queue.append([x-1,y])


for i in range(0,N) :
    inp = list(sys.stdin.readline().split())
    inp = [int(j) for j in inp]
    imsi = max(inp)
    if imsi > M :
        M = imsi
    village.append(inp)


for water in range(1,M+1) :
    localsafe = 0
    for i in range(0,N) :
        for j in range(0,N) :
            if (village[i][j]-water > 0 and check[i][j] != water) : #물에 잠기지 않았다면
                bfs(i,j,water)
                localsafe += 1

    if localsafe > safezone :
        safezone = localsafe

print(safezone)
