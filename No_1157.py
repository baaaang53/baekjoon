# 단어 공부

alpha = [0] * 26

inp = list(input())
maxi = -1
for elem in inp :
    now = ord(elem)
    if 97 <= now <= 122 :
        alpha[now-97] += 1
        if maxi < alpha[now-97] :
            maxi = alpha[now-97]
    else :
        alpha[now-65] += 1
        if maxi < alpha[now-65] :
            maxi = alpha[now-65]

know = True
index = -1


for al in range(len(alpha)) :
    if alpha[al] == maxi and index != -1:
        print("?")
        know = False
        break
    if alpha[al] == maxi :
        index = al

if know :
    print(chr(index+65))