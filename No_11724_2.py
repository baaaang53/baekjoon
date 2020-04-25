#연결요소의 개수

import queue
import sys

N,M = map(int, input().split())
graph = [[0]*(N+1) for i in range(0,N+1)]
count = 0
q = queue.Queue()
# graph[0]은 방문 여부를 체크. visit의 역할.

for i in range(0,M) :
    i,j = map(int, sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1



def bfs(node) :
    graph[0][node] = 1
    q.put(node)

    while(q.empty() == False) :
        now = q.get()

        for i in range(1,N+1) :
            if (graph[now][i] == 1 and graph[0][i] == 0) :
                q.put(i)
                graph[0][i] = 1

for i in range(1,N+1) :
    if graph[0][i] == 0 :
        bfs(i)
        count += 1



print(count)