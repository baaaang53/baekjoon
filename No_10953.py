#A+B -6

import sys

tc = int(input())
for _ in range(tc) :
    a,b = map(int, sys.stdin.readline().split(","))
    print(a+b)