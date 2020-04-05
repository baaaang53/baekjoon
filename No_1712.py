#손익분기점

A,B,C = map(int, input().split())
x = 0
if C > B :
    x = A // (C-B)
    print(x + 1)

else :
    print(-1)