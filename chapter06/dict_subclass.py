# 不建议继承list和dict
# 有时候不会用调用继承的重写方法


from collections import UserDict,defaultdict

class MyDict(UserDict):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def __setitem__(self, key, value):
        super().__setitem__(key,value)

    #  当找不到Key的时候调用
    def __missing__(self, key):
        print(key)
        return 1

a = MyDict(a=1,b=2)
# print(a)
print(a["key"])

my = defaultdict(dict)
v = my["key"]
# print(v)
