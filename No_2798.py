def main() :
    [n, m] = input().split(" ")
    N = int (n)
    M = int (m)
    cards = input().split(" ")
    max = 0

    for i in range(0,N) :
        for j in range(i+1,N) :
            for u in range(j+1,N) :
                imsi = int(cards[i]) + int(cards[j]) + int(cards[u])
                if max < imsi and imsi <= M :
                    max = imsi
                else :
                    continue

    print (max)
main()