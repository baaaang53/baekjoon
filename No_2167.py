#2차원 배열의 합
import sys

N,M = map(int, sys.stdin.readline().split())
matrix = [[0]]
ans = []

for i in range(N) :
    inp = list(map(int, sys.stdin.readline().split()))
    inp.insert(0,0)
    matrix.append(inp)

for i in range(1, N+1) :
    for j in range(0, M+1) :
        if j == 0 and i == 1 :
            matrix[i][j] = 0
        elif j == 0 and i != 1 :
            matrix[i][j] += matrix[i-1][M]
        else :
            matrix[i][j] += matrix[i][j-1]


K = int(input())

for i in range(K) :
    i_s,j_s,i_e,j_e = map(int, sys.stdin.readline().split())
    res = 0

    for x in range(i_s,i_e + 1) :
        res += (matrix[x][j_e]-matrix[x][j_s-1])

    ans.append(res)

for elem in ans :
    print(elem)