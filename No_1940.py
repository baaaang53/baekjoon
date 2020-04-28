# 주몽
N = int(input())
M = int(input())
arr = list(map(int,input().split()))

arr.sort()
left = 0
right = N-1
count = 0

while (left < right) :
    summ = arr[left] + arr[right]

    if summ == M :
        count += 1
        right -=1
        left += 1
    elif summ > M :
        right -= 1
    else :
        left += 1

print(count)