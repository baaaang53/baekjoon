# 체스판 다시 칠하기

import sys

INF = sys.maxsize
M,N = map(int, sys.stdin.readline().split())
differ = [[0]*N for _ in range(M)]
minimum = INF

def counting(i,j) :
    count = 0
    for x in range(i,i+8) :
        for y in range(j,j+8) :
            if differ[x][y] == 1 :
                count += 1
    return min(count, 64-count)

for i in range(M) :
    inp = list(sys.stdin.readline())
    for j in range(N) :
        if (i+j) % 2 == 0 :
            if inp[j] != "B" :
                differ[i][j] = 1
        else :
            if inp[j] != "W" :
                differ[i][j] = 1


for i in range(M-7) :
    for j in range(N-7) :
        minimum = min(minimum, counting(i,j))
print(minimum)