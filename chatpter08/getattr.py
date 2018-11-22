from datetime import date,datetime

class User():
    def __init__(self,name):
        self.name = name

    # 当属性查找找不到时，就会调用这个方法
    def __getattr__(self, item):
        return self.name[item]

    #属性查找都会用到
    # def __getattribute__(self, item):
    #     pass
if __name__ == '__main__':

    u = User({"a":1,"b":2})
    print(u.b)
    print(setattr(u,"test","test"))
    print(u.test)