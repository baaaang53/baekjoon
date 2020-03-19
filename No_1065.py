#한수

count = 0
N = int(input())

for i in range(1,N+1):
    lis = list(map(int, str(i)))
    if len(lis) == 1 :
        count += 1
        continue
    valid = True
    gap = lis[1] - lis[0]
    iter = 1
    while (iter < len(lis)) :




