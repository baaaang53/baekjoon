# 소수의 연속합

n = int(input())

if n == 1 :
    print(0)
    exit()
if n == 2 :
    print(1)
    exit()
pnums = []

toEra = [True] * (n+1)

def Prime(a) :
    for i in range(2,n+1) :
        if toEra[i] :
            pnums.append(i)
            for j in range(i,n+1,i) :
                toEra[j] = False
            toEra[i] = True



Prime(n)

left =  0
right = 0
summ = pnums[0]
count = 0
while (right < len(pnums)) :
    if summ < n :
        right += 1
        if right == len(pnums) :
            break
        summ += pnums[right]
    elif summ == n :
        count += 1
        right += 1
        if right == len(pnums) :
            break
        summ = summ + pnums[right]-pnums[left]
        left += 1
    else :
        summ -= pnums[left]
        left += 1
print(count)
