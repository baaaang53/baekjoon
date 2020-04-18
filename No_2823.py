#유턴 싫어

import sys
import queue

R,C = map(int, input().split())
village = []
visit = [[0]*C for _ in range(R)]

for _ in range(R) :
    now = list(sys.stdin.readline())
    village.append(now)

def dfs(x,y) :
    stac = queue.LifoQueue()
    stac.put((x,y))

    while (stac.empty() != True) :
        (a,b) = stac.get()
        count = 0
        visit[a][b] = 1
        #위
        if a != 0 and village[a-1][b] == '.' :
            count += 1
            if visit[a-1][b] == 0 :
                stac.put((a-1,b))

        #아래
        if a != R-1 and village[a+1][b] == '.' :
            count += 1
            if visit[a+1][b] == 0 :
                stac.put((a+1,b))

        #오른쪽
        if b != C - 1 and village[a][b+1] == '.':
            count += 1
            if visit[a][b+1] == 0 :
                stac.put((a,b+1))

        # 왼쪽
        if b != 0 and village[a][b-1] == '.':
            count += 1
            if visit[a][b-1] == 0 :
                stac.put((a,b-1))

        if count < 2 :
            return False


for i in range(R) :
    for j in range(C) :
        if village[i][j] == "." :
            if dfs(i,j) == False :
                print("1")
                sys.exit()

print("0")
