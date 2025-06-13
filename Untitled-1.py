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