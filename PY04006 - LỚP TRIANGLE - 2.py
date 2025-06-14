import math

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k) :
        x0 = self.x - k.x
        y0 = self.y - k.y
        return math.sqrt(x0 * x0 + y0 * y0)

class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def cnt(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print('INVALID')
        else :
            d = math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            print('{:.2f}'.format(d))

a = []
t = int(input())
for x in range(t):
    a += list(map(float,input().split()))
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.cnt()
    i += 6
