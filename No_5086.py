#배수와 약수

import sys

while (True) :
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 :
        break

    if a %b == 0 :
        print("multiple")
        continue

    if b % a == 0 :
        print("factor")
        continue

    print("neither")