#셀프 넘버

li = [0] * 10001

for orig in range(1,10001) :
    if li[orig] == 0 :
        while (orig <= 10000) :
            spl = str(orig)
            for i in spl:
                orig += int(i)
            if orig < 10001 :
                li[orig] = 1

for elem in range(1,10001):
    if li[elem] == 0 :
        print(elem)

