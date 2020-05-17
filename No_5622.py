#다이얼

inp = list(input())
total = 0

for elem in inp :
    asc = ord(elem)

    if 65 <= asc < 68 :
        total += 3
    elif 68 <= asc < 71 :
        total += 4
    elif 71 <= asc < 74 :
        total += 5
    elif 74 <= asc < 77 :
        total += 6
    elif 77 <= asc < 80 :
        total += 7
    elif 80 <= asc < 84 :
        total += 8
    elif 84 <= asc < 87 :
        total += 9
    elif 87 <= asc < 91 :
        total += 10

print(total)