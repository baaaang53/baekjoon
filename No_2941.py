#크로아티아 알파벳

inp = list(input())
i = 0
count = 0
while (i < len(inp)) :
    nothing = True
    if inp[i] == "c" :
        if i != len(inp)-1 and (inp[i+1] == "=" or inp[i+1] == "-") :
            i += 2
            count += 1
            nothing = False
            continue
        else :
            i += 1
            count += 1
            continue
    elif inp[i] == "d" :
        if i != len(inp)-2 and inp[i+1] == "z" and inp[i+2] =="=" :
            i += 3
            count += 1
            continue
        if i != len(inp)-1 and inp[i+1] == "-" :
            i += 2
            count += 1
            continue
        else :
            i += 1
            count += 1
            continue
    elif inp[i] == "l" or inp[i] == "n":
        if i != len(inp)-1 and inp[i+1] == "j" :
            i += 2
            count += 1
            continue
        else :
            i += 1
            count += 1
            continue

    elif inp[i] == "s" or inp[i] == "z":
        if i != len(inp)-1 and inp[i+1] == "=" :
            i += 2
            count +=1
            continue
        else :
            i += 1
            count += 1
            continue
    else :
        count += 1
        i += 1
        continue

print (count)
