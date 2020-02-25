# 이분 그래프
import queue
import sys

tc = int(sys.stdin.readline())
res = []

for test in range(tc) :
    V,E = map(int, sys.stdin.readline().split())
    graph = [[]for _ in range(V+1)]
    group = [0] * (V+1) # 그룹 1과 2로 나뉠 것. 이게 visit의 역할도 수행할 것.
    panjung = True


    for _ in range(E) :
        v1,v2 = map(int, sys.stdin.readline().split())
        graph[v1].append(v2)
        graph[v2].append(v1)


    for lis in graph :
        lis.sort()


    def bfs(node) :
        zb = queue.Queue()
        zb.put(node)

        while(zb.empty() == False) :
            now = zb.get()
            for adj in graph[now] :
                if group[now] == group[adj] : #나랑 연결 된 애가 나랑 같은 그룹에 있다면
                    return False
                elif group[adj] == 0 : #아직 방문 안 되어있다면 나랑 다른 그룹으로 넣어
                    group[adj] = 3-group[now]
                    zb.put(adj)
        return True


    for i in range(1,V+1) :
        if group[i] == 0 :
            group[i] = 1
            if bfs(i) == False :
                panjung = False
                break


    if (panjung) :
        res.append("YES")
    else :
        res.append("NO")

for elem in res :
    print(elem)

