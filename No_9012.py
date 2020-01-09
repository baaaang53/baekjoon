def VPS(lst) :
    stack = []
    isVPS = True

    for i in lst :
        if (i == "(") :
            stack.append("(")

        # ")" as input
        else :
            # not matching
            if (len(stack) == 0) :
                isVPS = False
                break;

            elif (stack[len(stack)-1] == "(") :
                del stack[len(stack)-1]

    # there's ( left in the stack
    if (len(stack) != 0) : isVPS = False

    if (isVPS) : print("YES")
    else : print("NO")

def main() :
    n = int(input())
    for i in range(0,n) :
        inp = list(input())
        VPS(inp)
main()