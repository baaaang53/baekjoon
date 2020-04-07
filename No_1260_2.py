#DFS와 BFS

import sys
import queue

q = queue.Queue() #BFS용 큐
st = queue.LifoQueue() #DFS용 스택

N,M,I = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)] #그래프 연결 상태 나타내기. index0은 무

def DFS(start) :
    st.put(start)
    visit = [0 for _ in range(N+1)]
    out = []
    while (st.empty() != True) :
        now = st.get()
        if visit[now] == 0 :
            out.append(now)
            visit[now] = 1
            for index in range(len(graph[now])-1, -1, -1) :
                if visit[graph[now][index]] == 0 :
                    st.put(graph[now][index])
    return out

def BFS(start) :
    q.put(start)
    visit = [0 for _ in range(N+1)]
    out = []
    while (q.empty() != True) :
        now = q.get()
        if visit[now] == 0 :
            out.append(now)
            visit[now] = 1

            for elem in graph[now] :
                if visit[elem] == 0 :
                    q.put(elem)

    return out

for _ in range(M) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for list in graph :
    list.sort()

dfsres = DFS(I)
bfsres = BFS(I)

for elem in dfsres :
    print(elem, end = " ")

print()

for elem in bfsres :
    print(elem, end = " ")
