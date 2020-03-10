# 트리
# 연결 요소 : 모든 정점이 서로 연결되어있는 정점의 부분집합.

import sys
import queue


class Node :
    def __init__(self,key):
        self.key = key
        self.adj = []
        self.visit = False

def bfs(node) :
    q = queue.Queue()
    q.put(node)
    result = True
    while (q.empty() != True ) :
        now = q.get()
        if (tree[now].visit == True)  :
            result = False
        else :
            tree[now].visit = True
            for elem in tree[now].adj :
                q.put(elem)
    return result

while True :
    n,m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0 : break
    tree = [Node(i) for i in range(n+1)]
    count = 0

    for i in range(m) :
        a,b = map(int, sys.stdin.readline().split())
        tree[a].adj.append(b)
        #tree[b].adj.append(a)

    for i in range(1,n+1) :
        if tree[i].visit == False :
            if bfs(i) :
                count += 1

    if count == 0 :
        print("Case 3: No trees.")
    elif count == 1 :
        print("Case 2: There is one tree.")
    else :
        print("Case 1: A forest of %d trees." % count)
