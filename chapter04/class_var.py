class A:
    aa = 1

    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(2,3)
A.aa = 12
a.aa = 100
#实例找不到，就会向上查找
print(a.x,a.y,a.aa)
print(A.aa)
