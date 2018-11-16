#数据封装和私有属性

from chapter04.class_method import Date

class User:
    def __init__(self,brd):
        self.__brd = brd
    def get_age(self):
        return 2018-self.__brd.year


if __name__ == '__main__':
    user = User(Date(1999,1,1))
    print(dir(user))
    print(user.get_age())