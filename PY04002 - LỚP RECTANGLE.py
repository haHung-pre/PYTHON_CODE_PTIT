class Rectangle:
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        
        self.color = color.capitalize()


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
