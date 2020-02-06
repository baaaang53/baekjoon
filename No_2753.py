#윤년

year = int(input())
isLunar = False

if (year % 4 == 0) :
    if (year % 100 == 0) :
        if (year % 400 == 0) :
            isLunar = True
    else :
        isLunar = True

if (isLunar) :
    print("1")
else :
    print("0")