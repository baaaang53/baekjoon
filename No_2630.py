def dnq(row_s, row_e, col_s, col_e, matrix) :
    global countWhite
    global countBlue

    standard = matrix[row_s][col_s]
    same = True

    for r in range(row_s,row_e) :
        for c in range(col_s,col_e) :
            if (matrix[r][c] != standard) :
                same = False
                #left top
                dnq(row_s, (row_s + row_e)//2, col_s, (col_s + col_e)//2, matrix) #맞아,, 파이썬은 4/2 = 2.0이지..
                #right top
                dnq(row_s, (row_s + row_e)//2, (col_s + col_e)//2, col_e, matrix)
                #left bottom
                dnq((row_s + row_e)//2, row_e, col_s, (col_s + col_e)//2, matrix)
                #right bottom
                dnq((row_s + row_e)//2, row_e, (col_s + col_e)//2, col_e, matrix)
                return


    if (same and (standard == "1")) :
        countBlue += 1
    elif (same and (standard == "0")) :
        countWhite += 1

def main() :
    n = int(input())
    grid = []
    # take input
    for i in range(0,n) :
        lst = input().split(" ")
        grid.append(lst)

    dnq(0,n,0,n, grid)

    print(countWhite)
    print(countBlue)


countWhite = 0
countBlue = 0

main()