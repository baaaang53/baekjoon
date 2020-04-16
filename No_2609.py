#최대공약수와 최소공배수

A,B = map(int, input().split())

def GCD(a,b) : # 유클리드 호제법
    while (b!=0) :
        rem = a % b
        a = b
        b = rem
    return a

gcd = GCD(A,B)
lcm = A*B // gcd

print(gcd)
print(lcm)