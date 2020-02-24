#후보 추천하기

teul = int(input()) # 후보 수가 되는 것.
chucheon = int(input())

thumps = list(map(int, input().split()))
stud = [0] * 101
photo = []
least = 1000
disa = 0

for i in thumps :
    if i in photo : #이미 사진이 올라와있는 애라면
        stud[i] += 1
    else : # 사진 없다면
        if len(photo) < teul : # 자리 있다면
            photo.append(i) # 추가하고
            stud[i] += 1

        else : # 자리 없다면
            for j in range(len(photo)-1, -1, -1) :
                if stud[photo[j]] <= least :
                    least = stud[photo[j]]
                    disa = photo[j]

            least = 1000
            photo.remove(disa)
            stud[disa] = 0
            photo.append(i)
            stud[i] += 1

photo.sort()
for elem in photo :
    print(elem, end =" ")







