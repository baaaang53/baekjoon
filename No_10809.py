#알파벳 찾기

alpha = [-1] * 26

word = list(input())

for i in range(len(word)) :
    asc = ord(word[i])
    if alpha[asc-97] == -1 :
        alpha[asc - 97] = i

for elem in alpha :
    print(elem, end =" ")