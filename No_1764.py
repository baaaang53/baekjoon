N,M = map(int, input().split())
deutdo = []
bodo = []

for i in range(0,N) :
    deutdo.append(input())

for i in range(0,M) :
    bodo.append(input())

deutbo = list(set(deutdo).intersection(bodo))

deutbo.sort()

print(len(deutbo))
for elem in deutbo :
    print(elem)