#숫자의 개수

A = int(input())
B = int(input())
C = int(input())

counting = [0 for i in range(0,10)]
res = A*B*C
res = str(res)

for i in range(0,len(res)) :
    counting[int(res[i])] += 1


for i in range(0,10) :
    print(counting[i])