testcase = int(input())

for i in range(0,testcase) :
    n = int(input())
    jails = []
    count = 0
    # 0 : closed, 1 : opened
    for i in range(0,n) :
        jails.append(0)

    for i in range(1,n+1) :
        for k in range(i-1,n,i) :
            if jails[k] == 0 :
                jails[k] = 1
            else :
                jails[k] = 0

    for i in range(0,n) :
        if jails[i] == 1 :
            count += 1

    print(count)