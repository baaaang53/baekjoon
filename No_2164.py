#카드2
from collections import deque
n = int(input())

q = deque()
ans = 0
for i in range(1,n+1) :
    q.append(i)

while (len(q) != 0) :
    ans = q.popleft()
    if len(q) != 0 :
        ans = q.popleft()
        q.append(ans)

print(ans)