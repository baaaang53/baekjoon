# 최단 경로

import sys
import queue

V,E = map(int, sys.stdin.readline().split())
INF = sys.maxsize
graph = [[] for _ in range(V+1)]

visit = [0] * (V+1)
memo = [INF] * (V+1) #모든 가중치를 다 INF로 둔다.

start = int(input())

q = queue.Queue()

memo[start] = 0 # 나부터 나까지는 0

for _ in range(E) :
    f,t,w = map(int, sys.stdin.readline().split())
    graph[f].append([t,w])

q.put([start,0])

#다익스트라
while (q.empty() != True):
    [node, cost] = q.get()

    if cost > memo[node] : #최단거리가 아님
        continue

    for [to,weight] in graph[node] :
        if (memo[node] + weight < memo[to]) :
            memo[to] = memo[node] + weight
            q.put([to, memo[to]])


for ind in range(1,len(memo)) :
    if memo[ind] == INF :
        print("INF")
    else :
        print(memo[ind])