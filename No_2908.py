#상수

A,B = input().split()
A = list(A)
B = list(B)

Ac = ""
Bc = ""
for elem in A :
    Ac = elem + Ac

for elem in B :
    Bc = elem + Bc

Ac = int(Ac)
Bc = int(Bc)

if Ac > Bc :
    print(Ac)
else :
    print(Bc)