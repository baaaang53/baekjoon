def Union(lst1, lst2) :
    list_res = list(set(lst1) | set(lst2) )
    return list_res



N = int(input())
friends = [[]]
for i in range(0,N) :
    friends.append([])

m = int(input())
for i in range(0,m) :
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    friends[a].append(b)
    friends[b].append(a)

invite = friends[1]
for i in friends[1] :
    invite = Union(invite,friends[i])

invite.remove(1)

print(len(invite))