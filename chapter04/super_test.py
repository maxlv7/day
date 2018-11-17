# super真的是调用父类的构造函数吗？


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print('D')
        super().__init__()

if __name__ == '__main__':
    D()
    print(D.mro())

#使用super可以解决钻石继承问题
#super其实是调用mro链的下一个方法(对象)

# mixin模式特点
# 1. mixin类功能单一
# 2. 不和基类关联，可以和任意基类组合，基类可以不和mixin关联也能完成初始化
# 3. 在mixin中不要使用super这种用法
