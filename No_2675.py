#문자열 반복

import sys
tc = int(input())

for _ in range(tc) :
    tim, word = sys.stdin.readline().split()
    tim = int(tim)
    word = list(word)

    for elem in word :
        print(elem*tim, end ="")
    print("")