#피보나치 함수

import sys

tc = int(input())
li = [[0,0] for _ in range(41)]
li[0] = [1,0]
li[1] = [0,1]
for u in range(2, 41):
    li[u][0] = li[u - 1][0] + li[u - 2][0]
    li[u][1] = li[u - 1][1] + li[u - 2][1]

for _ in range(tc) :
    num = int(sys.stdin.readline())

    print(li[num][0], li[num][1])
