#통나무 옮기기

import sys


N = int(input())
grid = []
counting = [[[999,999]for _ in range(N)]for _ in range(N)] #0이 가로 1이 세로
queue = []
Base = []
End = []

for i in range(N) :
    inp = list(sys.stdin.readline().rstrip())
    for j in range(N) :
        if inp[j] == 'B' :
            Base.append([i,j])
        elif inp[j] == 'E' :
            End.append([i,j])

    grid.append(inp)

Base.sort()
End.sort()

def bfs(i,j,verti) :
    counting[i][j][verti] = 0
    queue.append([i,j,verti])

    while queue :
        [x,y,v] = queue.pop(0)

        if v == 0 : #가로일 때
            # 회전
            if (x != 0 and x != N-1 and grid[x-1][y-1] != '1' and grid[x-1][y+1] != '1'
                    and grid[x+1][y-1] != '1' and grid[x+1][y+1] != '1' and grid[x-1][y] != '1' and grid[x+1][y] != '1') :
                if counting[x][y][1] == 999 : # 방문이 안 돼있으면
                    queue.append([x,y,1])
                counting[x][y][1] = min(counting[x][y][1], counting[x][y][0] + 1)

            # 오른쪽
            if (y != N-2 and grid[x][y+2] != '1') :
                if counting[x][y+1][0] == 999 :
                    queue.append([x,y+1,0])
                counting[x][y+1][0] = min(counting[x][y+1][0], counting[x][y][0] + 1)


            # 왼쪽
            if (y != 1 and grid[x][y-2] != '1') :
                if counting[x][y-1][0] == 999 :
                    queue.append([x,y-1,0])
                counting[x][y - 1][0] = min(counting[x][y - 1][0], counting[x][y][0] + 1)

            # 위
            if (x != 0 and grid[x-1][y-1] != '1' and grid[x-1][y] != '1' and grid[x-1][y+1] != '1')  :
                if counting[x-1][y][0] == 999 :
                    queue.append([x-1,y,0])
                counting[x - 1][y][0] = min(counting[x - 1][y][0], counting[x][y][0] + 1)

            # 아래
            if (x != N-1 and grid[x+1][y-1] != '1' and grid[x+1][y] != '1' and grid[x+1][y+1] != '1') :
                if counting[x+1][y][0] == 999 :
                    queue.append([x+1,y,0])
                counting[x+1][y][0] = min(counting[x+1][y][0], counting[x][y][0] + 1)

        else : #세로일 때
            # 회전
            if (y != 0 and y != N-1 and grid[x-1][y-1]!='1' and grid[x-1][y+1] !='1'
                    and grid[x+1][y-1] != '1' and grid[x+1][y+1] != '1' and grid[x][y-1] != '1' and grid[x][y+1] != '1') :
                if counting[x][y][0] == 999 :
                    queue.append([x,y,0])
                counting[x][y][0] = min(counting[x][y][0], counting[x][y][1] + 1)

            # 오른쪽
            if (y != N-1 and grid[x-1][y+1] != '1' and grid[x][y+1] != '1' and grid[x+1][y+1] != '1') :
                if counting[x][y+1][1] == 999 :
                    queue.append([x,y+1,1])
                counting[x][y + 1][1] = min(counting[x][y + 1][1], counting[x][y][1] + 1)

            # 왼쪽
            if (y != 0 and grid[x-1][y-1] != '1' and grid[x][y-1] != '1' and grid[x+1][y-1] != '1') :
                if counting[x][y-1][1] == 999 :
                    queue.append([x,y-1,1])
                counting[x][y - 1][1] = min(counting[x][y - 1][1], counting[x][y][1] + 1)

            # 위
            if (x != 1 and grid[x-2][y] != '1') :
                if counting[x-1][y][1] == 999 :
                    queue.append([x-1,y,1])
                counting[x - 1][y][1] = min(counting[x - 1][y][1], counting[x][y][1] + 1)

            # 아래
            if (x != N-2 and grid[x+2][y] != '1') :
                if counting[x+1][y][1] == 999 :
                    queue.append([x+1,y,1])
                counting[x + 1][y][1] = min(counting[x + 1][y][1], counting[x][y][1] + 1)

[i,j] = Base[1]
if Base[0][0] == Base[1][0] :
    bfs(i,j,0)
else :
    bfs(i,j,1)

[i,j] = End[1]
if End[0][0] == End[1][0] :
    if counting[i][j][0] == 999 :
        print(0)
    else :
        print(counting[i][j][0]) #가로
else :
    if counting[i][j][1] == 999:
        print(0)
    else :
        print(counting[i][j][1]) #세로