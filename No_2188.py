# 축사 배정

#매칭 시스템이라고 생각하면 된다.

import sys

def dfs(i) :
    global cow
    global farm
    global check

    for elem in cow[i] :
        if check[elem] == 1 :
            continue
        check[elem] = 1

        if farm[elem] == -1 :
            farm[elem] = i
            return True
        elif dfs(farm[elem]) :
            farm[elem] = i
            return True
    return False


if __name__ == "__main__" :
    c,f = map(int, sys.stdin.readline().split())

    cow = [[] for _ in range(c+1)]
    farm = [-1]*(f+1)
    count = 0

    for i in range(1,c+1) :
        inp = list(map(int, sys.stdin.readline().split()))
        inp.pop(0)
        cow[i] = inp


    for i in range(1,c+1) :
        check = [0]*(f+1)
        if dfs(i) :
            count += 1


    print (count)