#토마토

import sys
from collections import deque

M,N,H = map(int, sys.stdin.readline().split())
tomato = [[[]for _ in range(N)] for _ in range(H)]
goodtomato = True
count = 0
queue = deque()

def IsnotEmpty(list) :
    return (len(list)!=0)

for z in range(H) :
    for y in range(N) :
        inp = list(map(int, sys.stdin.readline().split()))
        tomato[z][y] = inp
        for x in range(M) :
            if inp[x] == 0 : #안 익은 게 있다면
                goodtomato = False
            if inp[x] == 1 :
                queue.append([z,y,x]) # 익은 걸 다 queue에 넣는다

queue.append([-1,-1,-1]) # 막대기 넣기 _ 한 사이클이 지났는지 확인용


# 모든 토마토가 익어있다면
if goodtomato :
    print(0)
    exit(0)

else :
    while (IsnotEmpty(queue)) :

        [z,y,x] = queue.popleft()
        if ([z,y,x] == [-1,-1,-1]) : # 막대기가 나왔다면
            count += 1
            if IsnotEmpty(queue) :
                queue.append([-1,-1,-1]) # 한 사이클 지났으면 또 막대기 넣기
        else :
            if (z != 0 and tomato[z-1][y][x] == 0) :
                tomato[z-1][y][x] = 1
                queue.append([z-1,y,x])
            if (z != H-1 and tomato[z+1][y][x] == 0) :
                tomato[z+1][y][x] = 1
                queue.append([z+1,y,x])
            if (y != 0 and tomato[z][y-1][x] == 0) :
                tomato[z][y-1][x] = 1
                queue.append([z,y-1,x])
            if (y != N-1 and tomato[z][y+1][x] == 0) :
                tomato[z][y+1][x] = 1
                queue.append([z,y+1,x])
            if (x != 0 and tomato[z][y][x-1] == 0) :
                tomato[z][y][x-1] = 1
                queue.append([z,y,x-1])
            if (x != M-1 and tomato[z][y][x+1] == 0) :
                tomato[z][y][x+1] = 1
                queue.append([z,y,x+1])

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if tomato[i][j][k] == 0 :
                print(-1)
                exit(0)

print(count-1)