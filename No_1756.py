# 피자 굽기
# 위에서부터 내려오면서 걸리는 곳을 찾아야 한다.

oven_num, pizza_num = map(int, input().split())
oven = list(map(int,input().split()))
pizza = list(map(int, input().split()))

for i in range(1, oven_num) :
    oven[i] = min(oven[i], oven[i-1])

p_index = 0

for i in range(oven_num-1, -1, -1) :
    if (pizza[p_index] > oven[i]) : # 피자가 더 크면 오븐 한 칸 이동
        continue
    p_index += 1 # 피자가 들어가면 피자 한 칸 이동

    if (p_index == pizza_num) : #피자가 끝나면
        print(i+1) # 현재 오븐 위치
        exit(0)

print(0)
