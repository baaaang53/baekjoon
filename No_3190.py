#뱀
import sys

time = 0
moves = [] # 움직임 input
INF = sys.maxsize

N = int(input())
app = int(input())

directions = [[0,1], [1,0], [0,-1], [-1,0]] # 동 남 서 북
now_dir = 0 #현재 가고있는 방향.

apples = [[0]*N for _ in range(N)]
snakes = [[[0,0]for _ in range(N)] for _ in range(N)]
snakes[0][0] = [1,0] #각 element의 첫 원소는 뱀의 유무를, 두번째는 따라오는 몸통들이 여기를 지나갈 때 어느 방향으로 가야하는지.

head = [0,0] # 현재 머리와 꼬리 좌표.
tail = [0,0]

die = False

for _ in range(app) :
    x,y = map(int, sys.stdin.readline().split())
    apples[x-1][y-1] = 1

move = int(input())

for _ in range(move) :
    t, d = sys.stdin.readline().split()
    moves.append([int(t), d])


while (die == False) :
    if (len(moves) != 0) :
        [nexttime,nextdir] = moves.pop(0)
    else :
        nexttime = INF #이제부터는 방향전환이 없다.

    while (time < nexttime) :

        snakes[head[0]][head[1]][1] = now_dir # 가던 방향 저장

        head[0] += directions[now_dir][0]
        head[1] += directions[now_dir][1]
        if head[0] == N or head[0] == -1 or head[1] == N or head[1] == -1 : #벽에 닿으면
            die = True
            break
        elif (snakes[head[0]][head[1]][0] == 1) : #자기 몸을 만나면
            die = True
            break


        snakes[head[0]][head[1]][0] = 1 # 머리 움직임

        if (apples[head[0]][head[1]] != 1) : #사과 안만나면
            snakes[tail[0]][tail[1]][0] = 0 #꼬리를 없애
            dir_past = snakes[tail[0]][tail[1]][1]
            tail[0] += directions[dir_past][0]
            tail[1] += directions[dir_past][1]
        elif (apples[head[0]][head[1]] == 1) : #사과 만나면
            apples[head[0]][head[1]] = 0 # 사과 없애
        time += 1

    if nextdir == "L" : #방향 변경
        now_dir = (now_dir + 3) % 4
    elif nextdir == "D" :
        now_dir = (now_dir + 1) % 4

print(time+1)