#평균
import sys

N = int(sys.stdin.readline())
sum = 0

scores = list(sys.stdin.readline().split())

for i in range(0,len(scores)) :
    scores[i] = int(scores[i])
    sum += scores[i]

high = max(scores)
print((sum/high*100)/N)
