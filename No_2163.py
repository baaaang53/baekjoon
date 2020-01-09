def cut(M,N) :
    if (M%2 == 1) :
        if (M == 1) :
            if (N %2 == 1) :
                cut(1, N-1/2) + cut(1, N+1/2)
            else :
                cut(1, N/2) * 2
        else :
            cut(M-1/2, N) + cut(M+1/2, N)
    else :
        cut(M/2, N) * 2

def main() :
    [m,n] = input().split(" ")
    M = int(m)
    N = int(n)
    cut(M,N)
main()