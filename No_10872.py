def dofact(n) :
    ll = int(n)
    res = 1

    for i in range(1, ll+1) :
        res = res * i

    print(res)

def main() :
    a = input()
    dofact(a)

main()