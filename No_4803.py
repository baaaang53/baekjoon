# 트리
# 연결 요소 : 모든 정점이 서로 연결되어있는 정점의 부분집합.

import sys


class Node :
    def __init__(self):
        adj = []
        visit = False

def bfs(node) :

while True :
    n,m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0 : break
    tree = [Node() for _ in range(n+1)]

    for i in range(m) :
        a,b = map(int, sys.stdin.readline().split())
        tree[a].adj.append(b)
        tree[b].adj.append(a)

    for i in range(1,n+1) :
        if tree[i].visit == False :
            bfs(i)

