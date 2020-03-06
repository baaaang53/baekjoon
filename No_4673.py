# 셀프 넘버

arr = [False] * 10001

def check(ind) :
    sumi = ind

    while(1) :
        if (ind ==0) :
            break
        sumi += ind%10
        ind = ind//10

    if sumi <= 10000 :
        arr[sumi] = True


for i in range(10001) :
    check(i)

for elem in range(1,10001) :
    if (arr[elem] == False) :
        print(elem)