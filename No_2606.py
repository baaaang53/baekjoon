N = int(input())

network = [[0]*(N+1) for i in range(0,N+1)] #index와 컴퓨터 번호를 맞춰주기 위함.
dfsstack = []
ccount = 0

m = int(input())


for k in range(0,m) :
    i, j = map(int, input().split())
    network[i][j] = 1
    network[j][i] = 1

def isEmpty(list) :
    return (len(list)==0)

def dfs(start) :
    global ccount
    dfsstack.append(start)

    while(isEmpty(dfsstack) == False) :
        now = dfsstack.pop(0)

        if(network[0][now] == 0) : #방문을 안 했다면
            network[0][now] = 1
            ccount += 1

            for i in range(N, 0, -1) :
                if (network[now][i] == 1 and network[0][i] == 0) :
                    dfsstack.insert(0,i)

dfs(1)
print(ccount-1)