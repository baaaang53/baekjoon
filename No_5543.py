#상근날드

import sys
INF = sys.maxsize
burger = INF
drink = INF

for _ in range(3) :
    now = int(input())
    if burger > now :
        burger = now

for _ in range(2) :
    now = int(input())
    if drink > now :
        drink = now

print (burger + drink - 50)