
#自定义列元类
#type是创建类的类
class Person():
    def jump(self):
        print(self)

def say(self):
    return self.name+'!!!!'


class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        # print(*args)
        print(**kwargs)

class My(metaclass=MetaClass):
    a = 1
    def __init__(self,name):
        self.name = name

if __name__ == '__main__':
    User = type("user",(Person,),{"name":"li","say":say})
    # a = User()
    # print(a)
    # print(a.say())
    # a.jump()
    a = My("test")
    print(a.name)
