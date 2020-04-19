#적록색약

import sys

N = int(input())

normal = []
special = []

nor_visit = [[0] * N for _ in range(N)]
spe_visit = [[0] * N for _ in range(N)]

nor_count = 0
spe_count = 0

for _ in range(N) :
    inp = list(sys.stdin.readline().rstrip())
    normal.append(inp)
    new = []
    for elem in inp : #G -> R로 저장.
        if elem ==  "G" :
            new.append("R")
        else :
            new.append(elem)
    special.append(new)

def bfs(i,j,color, visit, pic) :
    q = []
    q.append([i,j])

    while (len(q) != 0) :
        [a,b] = q.pop(-1)
        if visit[a][b] == 0 :
            visit[a][b] = 1

            #up
            if a != 0 and pic[a-1][b] == color and visit[a-1][b] == 0 :
                q.append([a-1,b])

            #down
            if a != N-1 and pic[a+1][b] == color and visit[a+1][b] == 0 :
                q.append([a+1,b])

            #left
            if b != 0 and pic[a][b-1] == color and visit[a][b-1] == 0:
                q.append([a,b-1])

            #right
            if b != N-1 and pic[a][b+1] == color and visit[a][b+1] == 0 :
                q.append([a,b+1])


for i in range(N) :
    for j in range(N) :
        if nor_visit[i][j] == 0 :
            nor_count += 1
            bfs(i,j,normal[i][j],nor_visit, normal)

for i in range(N) :
    for j in range(N) :
        if spe_visit[i][j] == 0 :
            spe_count += 1
            bfs(i,j,special[i][j],spe_visit, special)

print(nor_count, spe_count)