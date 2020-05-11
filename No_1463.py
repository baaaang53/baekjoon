#1로 만들기
import sys

INF = sys.maxsize

n = int(input())

if (n == 1) :
    print("0")
    exit()

arr = [INF] * (n+1)

arr[1] = 0
for i in range(2,n+1) :
    if i % 3 == 0 :
        arr[i] = min(arr[i], arr[i//3] + 1)
    if i % 2 == 0 :
        arr[i] = min(arr[i], arr[i // 2] + 1)

    arr[i] = min(arr[i], arr[i-1] + 1)

print(arr[n])