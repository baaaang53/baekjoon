pocket = [[]]

for i in range(0,5) :
    inp = list(input())

    #주머니 갯수 조정
    if (len(inp) > len(pocket)) :
        for k in range(0,len(inp)-len(pocket)) :
            pocket.append([])

    for k in range(0,len(inp)) :
        pocket[k].append(inp[k])

for pck in pocket :
    for elem in pck :
        print (elem, end ="")