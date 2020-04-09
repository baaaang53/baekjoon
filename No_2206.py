#벽 부수고 이동하기

# BFS로 길 찾는데, 시작좌표,끝좌표를 설정하게 한다.
# 그래서 벽을 다 피해서 가는 방법을 먼저 구하고
# 각 벽에 대해서 해당 벽을 거쳐서 목적지로 가는 경로를 구한다.
# 입력을 받을 때, 벽 위치 따로 저장해두기

import sys
import queue

M,N = map(int, sys.stdin.readline().split())
walls = [] # 벽 위치를 저장하는 곳
maps = [[1]*(N+1)]
INF = sys.maxsize

def BFS(x_s,y_s,x_e,y_e) :
    q = queue.Queue()
    count = 0
    q.put((x_s,y_s))
    q.put((0,0)) # count용.마트 계산 막대
    while (q.empty() != True) :
        (a,b) = q.get()
        if (a,b) == (x_e,y_e) :
            return count
        elif (a,b) == (0,0) : #count 만나면
            count += 1
            if q.empty() == False :
                q.put((0,0)) # 아직 안 비어있으면 count막대 뒤에 또 추가
        else :
            if a != 1 and ((a-1,b) == (x_e,y_e) or maps[a-1][b] == 0) :
                q.put((a-1,b))
            if a != M and ((a+1,b) == (x_e,y_e) or maps[a+1][b] == 0) :
                q.put((a+1,b))
            if b != 1 and ((a,b-1) == (x_e,y_e) or maps[a][b-1] == 0) :
                q.put((a,b-1))
            if b != N and ((a,b+1) == (x_e,y_e) or maps[a][b+1] == 0) :
                q.put((a,b+1))
    return -1


for i in range(M) :
    inp = list(sys.stdin.readline().rstrip())
    inp = [int(elem) for elem in inp]
    inp.insert(0,1)
    for j in range(1,N+1) :
        if inp[j] == 1 :
            walls.append((i+1,j))
    maps.append(inp)


steps = BFS(1,1,M,N)
if steps == -1 :
    steps = INF
for (a,b) in walls :
    firststep = BFS(1,1,a,b)
    secondstep = BFS(a,b,M,N)
    if firststep != -1 and secondstep != -1 : # 가능한 경우인지 확인
        if steps > firststep + secondstep :
            steps = firststep + secondstep

if steps == INF :
    print("-1")
else :
    print(steps + 1)