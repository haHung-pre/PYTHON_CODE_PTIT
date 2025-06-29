class Rectangle:
    def __init__(self, a, b, c):
        self.perimeter = (a+b)*2
        self.area = a*b
        self.color = c.capitalize()

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print('{} {} {}'.format(r.perimeter, r.area, r.color)) 
else:
    print('INVALID')




class Rectangle:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        
        self.color = color[0:1].upper() + color[1:].lower()

    def output(self):
        if self.w <= 0 or self.h <= 0:
            print("INVALID")
        else:
            chu_vi = (self.w + self.h) * 2
            dien_tich = self.w * self.h
            print(chu_vi, dien_tich, self.color)


a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), a[2])
rec.output()
