top = int(input())
bottom = input()
botinlist = list(bottom)
bottom = int(bottom)
botinlist = [int(a) for a in botinlist]

for i in range(2,-1,-1) :
    print(botinlist[i] * top)
print(top * bottom)



