#OX퀴즈

import sys
n = int(input())

for i in range(0,n) :
    inp = sys.stdin.readline().rstrip()
    sum = 0
    chart = []

    for j in range(0,len(inp)) :
        if inp[j] == "X" :
            chart.append(0)
        elif j == 0 :
            chart.append(1)
            sum += 1
        else :
            k = chart[j-1]+1
            chart.append(k)
            sum += k

    print(sum)