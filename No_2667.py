N = int(input())

matrix = [] # 입력받은 지도 정보 저장
check = [[0]*N for i in range(0,N)] # 해당 집을 체크했는지 저장. 1은 체크 함, 0은 안함.
housecount = [0] # 번지수에 해당하는 집의 수 저장
counting = 0 # 집 몇갠지 세는 용도

for i in range(0,N) :
    inp = list(input())
    inp = [int(i) for i in inp]
    matrix.append(inp)


def findneighbor(x,y) :
    check[x][y] = 1 # 집 방문.
    counting =1

    #북
    if (x != 0) :
       if (matrix[x-1][y] == 1 and check[x-1][y] == 0) :
           counting += findneighbor(x-1, y)

    #동
    if (y != N-1) :
        if (matrix[x][y+1] == 1 and check[x][y+1] == 0) :
            counting += findneighbor(x, y+1)

    #남
    if (x != N-1) :
        if (matrix[x+1][y] == 1 and check[x+1][y] == 0) :
            counting += findneighbor(x+1, y)

    #서
    if (y != 0) :
        if (matrix[x][y-1] == 1 and check[x][y-1] == 0) :
            counting += findneighbor(x, y-1)

    return counting



for i in range(0,N) :
    for j in range(0,N) :
        if (matrix[i][j] == 1 and check[i][j] == 0 ): # 집은 있고 아직 방문은 되지 않았다면
            num = findneighbor(i,j)
            housecount.append(num)

print(len(housecount)-1)
for k in range(1,len(housecount)) :
    print(housecount[k])