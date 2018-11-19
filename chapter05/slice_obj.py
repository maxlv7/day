# 这让我深刻理解到了Python就是基于协议编程的
# 只要一个对象实现了某个魔法函数,那么它就具有了一定的功能
import numbers

# 实现对象的切片
class Fruit():

    def __init__(self,f_list):
        self.f_list = f_list

    def __getitem__(self, item):
        # 找到class
        cls = type(self)
        if isinstance(item,slice):
            return cls(self.f_list[item])
        if isinstance(item,numbers.Integral):
            return 1

    def __setitem__(self, key, value):
        self.f_list[:len(f_list)] = value

f_list = ["apple","pear","banana","egg","bead"]
fs = Fruit(f_list)
# print(fs[0])

# for x in fs:
#     print(x)
b = fs[::2]
print((b.f_list))