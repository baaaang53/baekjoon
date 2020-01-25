N = int(input())

mem = [0] * 1000001 #int 범위
mem[0] = 1
mem[1] = 1
for i in range(2, N+1) :
    #mem[i-1] : 1 로 끝남
    #mem[i-2] : 00으로 끝남
    mem[i] = ((mem[i-2]%15746) + (mem[i-1]%15746)) %15746

print(mem[N])