#이친수

n = int(input())

arr = [[0,0] for _ in range(n)]

arr[0] = [0,1]
for i in range(1,n) :
    arr[i][0] = arr[i-1][0] + arr[i-1][1]
    arr[i][1] = arr[i-1][0]

print(arr[n-1][0] + arr[n-1][1])