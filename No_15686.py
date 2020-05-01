# 치킨 배달

import sys
from itertools import combinations

N,M = map(int, input().split())
INF = sys.maxsize

house = []
chicken = []
c_ind = 0
totaldis = INF


for i in range(N) :
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(N) :
        if inp[j] == 1 : #house
            house.append([i,j])
        elif inp[j] == 2 : # chicken
            chicken.append([c_ind,i,j])
            c_ind += 1

h_to_c = [[0]*len(chicken) for _ in range(len(house))]

for h in range(len(house)) :
    for c in range(len(chicken)) :
        dis = abs(house[h][0]-chicken[c][1]) + abs(house[h][1]-chicken[c][2])
        h_to_c[h][c] = dis


combis = list(combinations(chicken,M))

for p in combis :
    localdis = 0 # 각 조합에 대한 합 .
    for htoc in h_to_c :
        housedis = INF
        for elem in p :
            housedis = min(housedis, htoc[elem[0]])
        localdis += housedis
    totaldis = min(localdis, totaldis)
print(totaldis)
