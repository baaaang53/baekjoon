#등수 찾기
import sys
import copy
from collections import deque

N,M,X = map(int, sys.stdin.readline().split())
better = [[] for _ in range(N+1)]
worse = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]


def bfs(st) :
    check[st] = 1
    countbetter = 0
    countworse = 0
    queue = deque()
    for elem in better[st] :
        queue.append(elem)
    while queue :
        now = queue.popleft()
        if check[now] == 0 :
            check[now] = 1
            countbetter += 1
            for s in better[now] :
                queue.append(s)

    for elem in worse[st] :
        queue.append(elem)
    while queue :
        now = queue.popleft()
        if check[now] == 0 :
            check[now] = 1
            countworse += 1
            for s in worse[now]:
                queue.append(s)
    return (countbetter,countworse)

for _ in range(M) :
    A,B = map(int, sys.stdin.readline().split())
    better[B].append(A)
    worse[A].append(B)

(up,down) = bfs(X)

best = up + 1
worst = N-down

print(best, worst)