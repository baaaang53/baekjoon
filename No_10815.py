#숫자 카드

N = int(input())
deck = list(map(int, input().split(" ")))

M = int(input())
target = list(map(int, input().split(" ")))

deck.sort()

def bifind(elem) :
    index = 0
    fin = N-1
    while (index <= fin) :
        mid = (index + fin) // 2

        if deck[mid] == elem :
            return 1
        if deck[mid] < elem :
            index = mid + 1
        else :
            fin = mid -1
    return 0


for elem in target :
    print(bifind(elem), end =" ")
