#A+B -8

import sys

tc = int(sys.stdin.readline())

for i in range(1,tc+1) :
    a,b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i,a,b,a+b))