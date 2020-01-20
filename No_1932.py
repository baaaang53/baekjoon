n = int(input())
pyramid = []

for i in range(0,n) :
    line = input().split(" ")
    line = [int(j) for j in line]
    pyramid.append(line)

for i in range(n-2, -1, -1) :
    for j in range(0,len(pyramid[i])) :
        bigger = max(pyramid[i+1][j],pyramid[i+1][j+1])
        pyramid[i][j] += bigger

print(pyramid[0][0])