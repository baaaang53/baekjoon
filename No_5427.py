#불

import sys
tc = int(input())

for _ in range(tc) :
    w, h = map(int, sys.stdin.readline().split())
    place = []
    fire = []
    for i in range(h) :
        inp = list(sys.stdin.readline().rstrip())
        for j in range(w) :
            if inp[j] == "@" :
                man = [i,j]
            elif inp[j] == "*" :
                fire.append([i,j])
        place.append(inp)

    fire_queue = []
    man_queue = []

    for f in fire :
        fire_queue.append(f);
    fire_queue.append([-1,-1])
    man_queue.append(man);
    man_queue.append([-1,-1])
    count = 0

    while(True) :
        # fire
        escape = False

        for elem in place :
            print(elem)
        print(" ")

        while (len(fire_queue)!=0) :
            [fx,fy] = fire_queue.pop(0)
            if [fx, fy] == [-1, -1]:
                if len(fire_queue) != 0:
                    fire_queue.append([-1, -1])
                break

            # 벽만 아니면 불이 퍼짐.
            #동
            if (fy != w-1) and place[fx][fy+1] != "#" :
                place[fx][fy+1] = "*"
                fire_queue.append([fx,fy+1])
            #서
            if (fy != 0) and place[fx][fy-1] != "#" :
                place[fx][fy-1] = "*"
                fire_queue.append([fx, fy-1])
            #북
            if (fx != 0) and place[fx-1][fy] != "#" :
                place[fx-1][fy] = "*"
                fire_queue.append([fx-1,fy])
            #남
            if (fx != h-1) and place[fx+1][fy] != "#" :
                place[fx+1][fy] = "*"
                fire_queue.append([fx+1, fy])

        # man
        while (len(man_queue) != 0) :
            [mx,my] = man_queue.pop(0)

            # 탈출 성공
            if mx == 0 or my == 0 or mx == h - 1 or my == w - 1:
                escape = True
                break#나

            #한 count cycle 끝남.
            if [mx,my] == [-1,-1] :
                if len(man_queue) != 0:
                    man_queue.append([-1, -1])
                break

            if place[mx-1][my] == "." :
                place[mx-1][my] = "@"
                man_queue.append([mx-1,my])
            if place[mx+1][my] == "." :
                place[mx + 1][my] = "@"
                man_queue.append([mx+1,my])
            if place[mx][my-1] == "." :
                place[mx][my-1] = "@"
                man_queue.append([mx,my-1])
            if place[mx][my+1] == "." :
                place[mx][my+1] = "@"
                man_queue.append([mx,my+1])

        count +=1
        if escape :
            print(count)
            break

        if len(man_queue)==0 and escape == False :
            print("IMPOSSIBLE")
            break
