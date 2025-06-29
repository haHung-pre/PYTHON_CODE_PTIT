import math

class PhanSo:
    def __init__(self, tu, mau):
        ucln = math.gcd(tu, mau)
        self.tu = tu // ucln
        self.mau = mau // ucln

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)

    def __str__(self):
        return f"{self.tu}/{self.mau}"


a, b, c, d = map(int, input().split())
p = PhanSo(a, b)
q = PhanSo(c, d)

print(p + q)




from math import gcd
a, b, c, d = map(int, input().split())
a = a*d + b*c
b*=d
print(f'{a//gcd(a,b)}/{b//gcd(a,b)}')
