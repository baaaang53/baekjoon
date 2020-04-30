#나무 자르기

n,m = map(int, input().split())
trees = list(map(int, input().split()))

maxi = max(trees)

left = 0
right = maxi
ans =0

while (left <= right) :
    total = 0
    mid = (left + right) // 2
    for elem in trees :
        total += max(0,elem-mid)

    if total >= m : # 너무 많이 자름.
        if (ans < mid) : # 가능한 최대 길이를 찾는 과정이니까.
            ans = mid
        left = mid+1
    else :
        right = mid-1

print(ans)

