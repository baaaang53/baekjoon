N = int(input())

matrix = [] # 입력받은 지도 정보 저장
check = [] # 해당 집을 체크했는지 저장. 1은 체크 함, 0은 안함.
housecount = [0] # 번지수에 해당하는 집의 수 저장
for i in range(0,N) :
    inp = map(int, input().split())
    matrix.append(inp)

def findneighbor(x,y) :
    check[x][y] = 1 # 집 방문.
    counting = 1
    notdone = True

    while (notdone) :
        if (x == N-1 or matrix[x+1][y] == 0) :
            if (y == N-1 or matrix[x][y+1] == 0) :
                notdone = False
            else :
                check[x][y+1] = 1
                counting += 1
        else :
            check[x+1][y] = 1
            counting += 1


    housecount.append(counting)



for i in range(0,N) :
    for j in range(0,N) :
        if (matrix[i][j] == 1 and check[i][j] == 0 ): # 집은 있고 아직 방문은 되지 않았다면
            findneighbor(i,j)
