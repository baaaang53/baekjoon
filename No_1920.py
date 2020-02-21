#수 찾기

import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))

M = int(input())
checks = list(map(int, sys.stdin.readline().split()))

nums = sorted(nums)

def find(wanted) :
    st = -1
    end = N
    while(st + 1 < end) :
        centre = (st+end) // 2

        if wanted == nums[centre] :
            return 1
        elif wanted < nums[centre] :
            end = centre
        else :
            st = centre
    return 0


for wanted in checks :
    print(find(wanted))