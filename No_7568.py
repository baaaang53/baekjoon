def main() :
    n = int(input())
    list = []

    # get input
    for i in range(0,n) :
        u = input().split(" ")
        u.append(1)
        list.append(u)

    for i in range(0,n) :
        for j in range(i+1, n) :
            if int(list[j][0]) > int(list[i][0]) and int(list[j][1]) > int(list[i][1]) :
                list[i][2] += 1
            elif int(list[j][0]) < int(list[i][0]) and int(list[j][1]) < int(list[i][1]) :
                list[j][2] += 1

    for i in range(0,n) :
        print (list[i][2], end =" ")
main()