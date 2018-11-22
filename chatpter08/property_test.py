from datetime import date,datetime

class User():
    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        print('--',value,'--')
        self._age = value
if __name__ == '__main__':

    u = User("li",date(year=1997,month=12,day=27))


    u.age=22
    print(u.age)

    u.age=24
    print(u.age)