#웜홀

import sys
INF = sys.maxsize

tc = int(input())

def belman(cost, village, N) :
    cost[1] = 0
    for cycle in range(N) :
        for node in range(1,N+1) :
            for [dest,weight] in village[node] :
                if cost[dest] > cost[node] + weight :
                    cost[dest] = cost[node] + weight
                    if cycle == N-1 :#업데이트 했을 때 사이클 수가 몇번째인지. N번째이면 음수 사이클 .
                        print("YES")
                        return

    print("NO")
    return


for _ in range(tc) :
    N,M,W = map(int, sys.stdin.readline().split())
    village = [[]for _ in range(N+1)]
    cost = [INF] * (N+1)


    for _ in range(M) :
        s,e,w = map(int, sys.stdin.readline().split())
        village[s].append([e,w])
        village[e].append([s,w])

    for _ in range(W) :
        s,e,w = map(int, sys.stdin.readline().split())
        village[s].append([e,-w])


    belman(cost, village, N)