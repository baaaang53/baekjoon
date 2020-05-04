#나무 탈출

import sys

n = int(input())
tree = [[] for _ in range(n+1)]
depth = [-1] * (n+1)
total = 0

for i in range(n-1) :
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def findDepth() :
    global total
    queue = []
    queue.append(1)
    queue.append(-1)
    count = 0
    while (len(queue) != 0) :
        now = queue.pop(0)
        leaf = True
        if now == -1 :
            if len(queue) != 0 :
                queue.append(-1)
                count += 1
        else :
            depth[now] = count
            for elem in tree[now] :
                if depth[elem] == -1 : #자식이 있음.
                    leaf = False
                    queue.append(elem)
            if leaf :
                total += depth[now]

findDepth()

if total % 2 == 1 :
    print("Yes")
else :
    print("No")



