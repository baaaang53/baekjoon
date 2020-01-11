def main() :
    n = int(input())
    n1, n2 = 0, 1

    for i in range(0, n) :
        n1, n2 = n2, n1+n2

    print(n1)

main()