# 에라토스테네스의 체
import sys

N,K = map(int, input().split())

li = [0]*(N+1)
count = 0

for i in range(2,N+1) :
    if li[i] == 0 :
        mul = 1
        while (mul * i < N+1) :
            if li[mul*i] == 0 :
                li[mul*i] = 1
                count += 1
                if count == K :
                    print(mul*i)
                    sys.exit()
            mul += 1