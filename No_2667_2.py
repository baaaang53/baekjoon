#단지 번호 붙이기

import sys
import queue

n = int(input())
village = []
visit = [[0]*n for _ in range(n)]

for _ in range(n) :
    inp = list(sys.stdin.readline().rstrip())
    village.append(inp)

def bfs(i,j) :
    q = queue.Queue()
    q.put((i,j))
    count = 0

    while (q.empty() != True) :
        (x,y) = q.get()
        if visit[x][y] == 0 :
            count += 1
            visit[x][y] = 1

            # up
            if x != 0 and village[x-1][y] == "1" and visit[x-1][y] == 0 :
                q.put((x-1,y))

            # down
            if x != n-1 and village[x+1][y] == "1" and visit[x+1][y] == 0 :
                q.put((x+1, y))

            # left
            if y != 0 and village[x][y-1] == "1" and visit[x][y-1] == 0 :
                q.put((x,y-1))

            #right
            if y != n-1 and village[x][y+1] == "1" and visit[x][y+1] == 0 :
                q.put((x,y+1))

    return count

totalcount = 0
nums = []
for i in range(n) :
    for j in range(n) :
        if village[i][j] == "1" and visit[i][j] == 0:
            totalcount += 1
            nums.append(bfs(i,j))

nums.sort()

print(totalcount)
for elem in nums :
    print(elem)
