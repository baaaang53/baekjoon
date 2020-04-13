# K진 트리

import sys
import queue

N,K,Q = map(int, sys.stdin.readline().split())

Tree= [[] for _ in range(N)]

for i in range(1,N) :
    if i % K == 0 :
        Tree[(i//K)-1].append(i)
        Tree[i].append((i//K)-1)
    else :
        Tree[i//K].append(i)
        Tree[i].append(i//K)


def bfs(sour, des) :
    visit = [0]*N
    q = queue.Queue()
    q.put(sour)
    q.put(-1)
    count = 0

    while (q.empty() != True ) :
        now = q.get()
        if now == -1 :
            count += 1
            if q.empty() == True :
                break
            else :
                q.put(-1)
        else :
            if now == des :
                break
            else :
                visit[now] = 1
                for adj in Tree[now] :
                    if visit[adj] == 0 :
                        q.put(adj)


    return count



for _ in range(Q) :
    a,b = map(int, sys.stdin.readline().split())
    print(bfs(a-1, b-1))