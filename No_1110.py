origin = input()

if len(origin) == 1 :
    origin = "0"+origin

num = origin

notyet = True
cycle = 0

while(notyet) :
    sum = str(int(num[0]) + int(num[1]))
    sum = sum[len(sum)-1]
    num = num[1]+sum
    cycle += 1
    if (num == origin) :
        notyet = False


print(cycle)
