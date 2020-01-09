def main() :
    n = int(input())
    list = []
    size = 0
    sum = 0

    for i in range (0,n) :
        inp = int(input())
        if (inp != 0) :
            list.append(inp)
            size += 1
        else :
            del list[size-1]
            size -= 1

    for i in range(0,size) :
        sum += list[i]

    print(sum)
main()