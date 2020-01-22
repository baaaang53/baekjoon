N,M,V = map(int, input().split())
graph = [[0] * (N+1) for i in range(0,N+1)]

# 방문 여부. 1: 방문함, 0: 방문하지않음  -> N+1칸인 이유는 node의 번호와 index를 맞추기 위함.
dfsvisit = [0 for i in range(0,N+1)]
bfsvisit = [0 for i in range(0,N+1)]

dfsstack = []
bfsqueue = []

# 방문 순서 저장용
dfsorder = []
bfsorder = []

for i in range(0,M) :
    i,j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

def isEmpty(list) :
    return (len(list)==0)


def dfs(start) :
    dfsstack.append(start)

    while(isEmpty(dfsstack) == False) :
        now = dfsstack.pop(0)

        if(dfsvisit[now] == 0) :
            dfsvisit[now] = 1
            dfsorder.append(now)

            for i in range(N, 0, -1) :
                if (graph[now][i] == 1 and dfsvisit[i] == 0) :
                    dfsstack.insert(0,i)


def bfs(start) :
    bfsqueue.append(start)


    while(isEmpty(bfsqueue) == False) :
        now = bfsqueue.pop(0)

        if(bfsvisit[now] == 0) :
            bfsvisit[now] = 1
            bfsorder.append(now)

            for i in range(0,N+1) :
                if (graph[now][i] == 1 and bfsvisit[i] == 0) :
                    bfsqueue.append(i)


dfs(V)
bfs(V)


for elem in dfsorder :
    print(elem, end = ' ')

print()

for elem in bfsorder :
    print(elem, end = ' ')