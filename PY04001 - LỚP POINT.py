import math
class Point:
  def __init__(self,x,y):
    self.a=x
    self.b=y
t=int(input())
for i in range(t):
  a1,b1,a2,b2=list(map(float,input().split()))
  p1=Point(a1,b1)
  p2=Point(a2,b2)
  result=math.dist([p1.a,p1.b],[p2.a,p2.b])
  print(f"{result:.4f}")
