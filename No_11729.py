n = int(input())
ccount = 0

def Move(n, source, desti) :
    global ccount
    if n == 1 :
        ccount += 1
        return "%d %d\n" %(source,desti)
    else :
        ccount += 1
        return (Move(n-1, source, (6-source-desti)) + "%d %d\n" %(source,desti) + Move(n-1,(6-source-desti), desti))

res = Move(n,1,3)
print(ccount)
print(res)