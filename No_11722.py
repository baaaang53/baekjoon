#가장 긴 감소하는 부분 수열

import sys

n = int(input())

if n == 1 :
    print(1)
    sys.exit()


dp = [1]*n
nums = list(map(int, input().split(" ")))

for i in range(n) :
    for j in range(i) :
        if nums[j] > nums[i] and dp[j]+1 > dp[i] :
            dp[i] = dp[j] + 1

print(max(dp))