#역사
# 나보다 어려운 애들을 next로 갖는 그래프를 만들고 탐색하면 됨.

import sys
from collections import deque
n, k = map(int, input().split())

events = [[]for _ in range(n+1)]

for _ in range(k) :
    a,b = map(int, sys.stdin.readline().split())
    events[a].append(b)

def bfs(front,end) :
    q = deque()
    visit = [0]*(n+1)
    q.append(front)

    while (len(q) != 0) :
        now = q.popleft()
        if now == end :
            return True
        if visit[now] == 0 :
            visit[now] = 1
            for elem in events[now] :
                if visit[elem] == 0 :
                    q.append(elem)

    return False

ques = int(input())
for _ in range(ques) :
    a,b = map(int, sys.stdin.readline().split())
    if (bfs(a,b)) :
        print("-1")
        continue
    elif (bfs(b,a)) :
        print("1")
        continue
    else :
        print("0")



