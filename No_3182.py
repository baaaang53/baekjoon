#한동이는 공부가 하기 싫어!

import sys

N = int(input())
know = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]
ask = 0

for i in range(N) :
    know[i+1] = int(sys.stdin.readline().rstrip())

for i in range(1,N+1) :
    seonbae = []
    seonbae.append(i)
    queue = []
    queue.append(i)
    while(queue) :
        now = queue.pop(0)
        if (now not in seonbae) :
            seonbae.append(now)
        if (know[now] not in seonbae) :
            queue.append(know[now])

    result[i] = len(seonbae)
    if result[ask] < result[i] :
        ask = i

print (ask)