N = int(input())

if (N <= 5) :
    if (N == 3 or N == 5) :
        print(1)
    else :
        print(-1)
    exit(0)

sugars = [-1 for i in range(0,N+1)]

# base case 설정
sugars[3] = 1
sugars[5] = 1

for i in range(6, N+1) :
    if (sugars[i-3] != -1) :
        if (sugars[i-5] != -1) :
            sugars[i] = min(sugars[i-3]+1, sugars[i-5]+1)
        else :
            sugars[i] = sugars[i-3]+1
    else :
        if (sugars[i-5] != -1) :
            sugars[i] = sugars[i-5] + 1

print(sugars[N])

