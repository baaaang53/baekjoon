#수 정렬하기

import sys
n = int(input())
arr = []

for _ in range(n) :
    k = int(sys.stdin.readline())
    arr.append(k)

arr.sort()

for elem in arr :
    print(elem)