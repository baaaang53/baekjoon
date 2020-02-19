#부분합

N,S = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0] * (N+1)
ans = 1000003

for i in range(1,N+1) :
    sum[i] = arr[i-1] + sum[i-1]

if sum[N] < S : # 다 더해도 S가  안 되면
    print(0)
else :
    st_po = 0
    fn_po = 1

    while st_po != N :
        if sum[fn_po] - sum[st_po] >= S :
            if fn_po - st_po < ans :
                ans = fn_po - st_po
            st_po += 1
        else:
            if fn_po != N :
                fn_po += 1
            else :
                break


    print(ans)