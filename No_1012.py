#유기농 배추

import sys
import queue

tc = int(input())

def BFS(i,j) :
    q = queue.Queue()
    q.put((i,j))

    while (q.empty() != True) :
        (a,b) = q.get()
        if Check[a][b] == 0 :
            Check[a][b] = 1

            #위
            if a != 0 and Farm[a-1][b] == 1 and Check[a-1][b] == 0 :
                q.put((a-1,b))
            #아래
            if a != N-1 and Farm[a+1][b] == 1 and Check[a+1][b] == 0 :
                q.put((a+1, b))
            #왼쪽
            if b != 0 and Farm[a][b-1] == 1 and Check[a][b-1] == 0 :
                q.put((a,b-1))
            #오른쪽
            if b != M-1 and Farm[a][b+1] == 1 and Check[a][b+1] == 0 :
                q.put((a,b+1))


for _ in range(tc) :
    M,N, K = map(int, sys.stdin.readline().split())
    Farm = [[0]*M for _ in range(N)]
    Check = [[0]*M for _ in range(N)]
    count = 0

    for _ in range(K) :
        x,y = map(int, sys.stdin.readline().split())
        Farm[y][x] = 1


    for i in range(N) :
        for j in range(M) :
            if Farm[i][j] == 1 and Check[i][j] ==0 :
                BFS(i,j)
                count += 1

    print(count)