# class A:
#     name = "A"
#     def __init__(self):
#         self.name = "obj"
# a = A()
#
# print(a.name)

#MRO（Method Resolution Order）：方法解析顺序。
class E(object):
    pass
class D():
    pass

class C(E):
    pass
class B(D):
    pass
class A(B,C):
    pass

#属性查找的顺序
print(A.__mro__)
