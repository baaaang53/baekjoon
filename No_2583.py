#영역 구하기

M,N,K = map(int, input().split())

matrix = [[0]*M for i in range(0,N)]
check = [[0]*M for i in range(0,N)]
counting = []

queue = []

for i in range(0,K) :
    xs,ys,xe,ye = map(int,input().split())
    for x in range(xs, xe) :
        for y in range(ys, ye) :
            matrix[x][y] = 1


def isEmpty(list) :
    return (len(list) == 0)


def bfs(a,b) :
    visitcount = 0
    queue.append([a,b])

    while (isEmpty(queue) == False) :
        [x,y] = queue.pop(0)

        if check[x][y] == 0 : # 체크가 안 되어있다면
            check[x][y] = 1
            visitcount += 1

            #동
            if x != N-1 :
                if matrix[x+1][y] == 0 and check[x+1][y] == 0:
                    queue.append([x+1,y])
            #서
            if x != 0 :
                if matrix[x-1][y] == 0 and check[x-1][y] == 0 :
                    queue.append([x-1,y])
            #남
            if y != 0 :
                if matrix[x][y-1] == 0 and check[x][y-1] == 0 :
                    queue.append([x,y-1])
            #북
            if y != M-1 :
                if matrix[x][y+1] == 0 and check[x][y+1] == 0 :
                    queue.append([x,y+1])
    return visitcount

for i in range(0,N) :
    for j in range(0,M) :
        if matrix[i][j] == 0 and check[i][j] == 0:
            u = bfs(i,j)
            counting.append(u)


print(len(counting))
counting.sort()
for i in counting :
    print(i, end =" ")