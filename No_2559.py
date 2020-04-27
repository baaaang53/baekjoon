#수열
N, K = map(int, input().split())

temper = list(map(int, input().split()))
nujeok = [0] * N

nujeok[0] = temper[0]

for i in range(1,N) :
    nujeok[i] = nujeok[i-1] + temper[i]

maximum = nujeok[K-1]
for i in range(K,N) :
    maximum = max(maximum, nujeok[i]-nujeok[i-K])

print(maximum)