import math
class PhanSo:
        def __init__(self,tu,mau):
            ucln=math.gcd(tu,mau)
            self.a=tu//ucln
            self.b=mau//ucln
        def __str__(self):
             return f"{self.a}/{self.b}"
x,y=list(map(int,input().split()))
p=PhanSo(x,y)
print(p)




from math import gcd
a, b = map(int, input().split())
print(f'{a//gcd(a,b)}/{b//gcd(a,b)}')

