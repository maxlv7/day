# python中的自省机制
# 自省是通过一定的机制查询到对象的内部结构

class Person():

    name = "person"

class User(Person):
    def __init__(self,brd):
        self.brd = brd

if __name__ == '__main__':
    user = User("Li")
    # print(dir(user))
    # print(user.get_age())

    # 通过__dict__查询属性

    print(user.__dict__)
    user.__dict__["age"] = 19
    print(user.__dict__)