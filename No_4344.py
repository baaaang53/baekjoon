#평균은 넘겠지

import sys

tc = int(input())

for i in range(0,tc) :
    inp = list(sys.stdin.readline().split())
    inp = [int(k) for k in inp]
    mean = (sum(inp)-inp[0])/inp[0]
    count = 0
    for j in range(1,len(inp)) :
        if (inp[j] > mean) :
            count += 1

    print("%0.3f%%" %(round(count/inp[0]*100,3)))