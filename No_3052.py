#나머지

import sys

dic = [0 for i in range(0,42)]
counting = 0

for i in range(0,10) :
    inp = int(sys.stdin.readline())
    rem = inp % 42
    dic[rem] += 1

for elem in dic :
    if elem != 0 :
        counting += 1

print(counting)
