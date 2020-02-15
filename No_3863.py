#행복한 전화 통화

import sys
ans = []

while (True) :
    N,M = map(int, sys.stdin.readline().split())
    if (N,M) == (0,0) :
        for elem in ans :
            print(elem)
        exit(0)


    call = []

    for _ in range(N) :
        sour,dest,start,dura = map(int, sys.stdin.readline().split())
        call.append([start,start+dura])

    for _ in range(M) :
        check_s,check_d = map(int,sys.stdin.readline().split())
        count = 0
        for k in call :
            if (check_s <= k[0] < check_s+check_d) or (check_s < k[1] <= check_s+check_d)\
                    or k[0] <= check_s < check_s+check_d <= k[1]:
                count += 1

        ans.append(count)