# 전화번호 목록
import sys

tc = int(input())
for _ in range(tc) :
    nums = int(sys.stdin.readline())
    inp = [] #해싱 전 전화번호 받아두는 곳 _ 비효율?
    minimum = 11
    for _ in range(nums) :
        imsi = sys.stdin.readline()
        if len(imsi) < minimum : # 최소 길이 구하기 _ 거기에 맞춰서 해싱할 거야
            minimum = imsi
        inp.append(imsi)

    book = [[] * (10**minimum)]
    for elem in inp :
        
