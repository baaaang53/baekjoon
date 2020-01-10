def VPS(lst) :
    stack = []
    for i in lst :
        if (i == '(' or i == '[') :
            stack.append(i)
            continue

        elif (i == ')') :
            if (len(stack) != 0 and stack[len(stack)-1] == '(') :
                del stack[len(stack) - 1]

            else :
                return False


        elif (i == ']') :
            if (len(stack) != 0 and stack[len(stack) - 1] == '['):
                del stack[len(stack) - 1]

            else:
                return False

    if (len(stack) != 0) : return False
    else : return True

def main() :
    while (True) :
        # when input is over
        inp = input()
        if (inp == ".") :
            break

        else :
            inplist = list(inp)
            isVPS = bool(VPS(inplist))

            if (isVPS) :
                print("yes")
            else :
                print("no")

main()