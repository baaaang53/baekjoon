def dnq(row_s, row_e, col_s, col_e, grid) :
    standard = grid[row_s][col_s]
    same = True

    for i in range(row_s, row_e) :
        for j in range(col_s, col_e) :
            if (grid[i][j] != standard) :
                same = False
                ltop = dnq(row_s, (row_s + row_e)//2, col_s, (col_s + col_e)//2, grid)
                rtop = dnq(row_s, (row_s + row_e)//2, (col_s + col_e)//2, col_e, grid)
                lbottom = dnq((row_s + row_e)//2, row_e, col_s, (col_s + col_e)//2, grid)
                rbottom = dnq((row_s + row_e)//2, row_e, (col_s + col_e)//2, col_e, grid)

                return("("+ltop+rtop+lbottom+rbottom+")")

    if (same and (standard == "1")) :
        return ("1")
    elif (same and (standard == "0")) :
        return ("0")

def main() :
    n = int(input())
    grid = []

    # generate grid
    for i in range(0, n) :
        inp = list(input())
        grid.append(inp)

    print(dnq(0,n,0,n,grid))

main()