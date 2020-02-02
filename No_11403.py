N = int(input())
graph = []
queue = []

route = [[0] * N for i in range(0,N)]

for i in range(0,N) :
    inp = input().split()
    inp = [int(elem) for elem in inp]
    graph.append(inp)

def isEmpty(list) :
    return (len(list) == 0)


def bfs(st,dst) :
    route[st][dst] = 1
    queue.append([st,dst])


    while (isEmpty(queue) == False) :
        for i in range(0,N) :
            a = queue[0][1]
            if (graph[a][i] and route[st][i] == False) : # 연결되어있고 방문은 하지 않았다면
                route[st][i] = 1
                queue.append([a,i])

        queue.pop(0)



for st in range(0,N) :
    for dst in range(0,N) :
        if graph[st][dst] == 1 :
            bfs(st,dst)

for i in route :
    for j in i :
        print(j,end =" ")
    print()

