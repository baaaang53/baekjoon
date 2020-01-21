#돈을 최대한 많이 쓰면 된다.



N = int(input())

#costs : 각 카드팩의 가격
costs = input().split(" ")
costs = [int(j) for j in costs]
costs.insert(0,0) #카드 수와 index를 맞춰주기 위함

#pay : index만큼의 카드를 사기 위해서 지불해야 하는 돈
pay = [0 for i in range(N+1)] # 카드 수와 index를 맞춰주기 위함
pay[1] = costs[1] # 한 장 구매 설정
for i in range(2,N+1) :
    maxcost = -99
    for j in range(0,i+1) :
        maxcost = max(maxcost, pay[j] + costs[i-j])
    pay[i] = maxcost

print(pay[N])
