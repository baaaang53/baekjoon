# 분수 합

def GCD(a,b) :
    while (b != 0) :
        rem = a%b
        a = b
        b = rem

    return a

a_top, a_bot = map(int, input().split())
b_top, b_bot = map(int, input().split())

new_top = a_top * b_bot + b_top * a_bot
new_bot = a_bot * b_bot

div = GCD(new_top, new_bot)

print(new_top // div, new_bot // div)
