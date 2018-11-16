#abc模块(abstract base class) 它就像java里面的接口一样
#实现某个魔法函数 它就是某个类型


#我们去检查某个类是否有某种方法

class Company():
    def __init__(self,employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)+1

cpy = Company(["li","yyx"])

# print(hasattr(cpy,"__len__"))
# print(len(cpy))


#我们需要强制某个子类必须实现某些方法
#实现了一个web框架，集成cache(redis, cache, memorychache)
#需要设计一个抽象基类， 指定子类必须实现某些方法


#我们在某些情况一希望判定某个对象的类型
from collections.abc import Sized
# print(isinstance(cpy,Sized))

#如何去模拟一个抽象基类

# class CacheBase():
#     def get(self,key):
#         raise NotImplementedError
#     def set(self,key,value):
#         raise NotImplementedError

#使用abc
import abc

#这里更像是一个java中的接口
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self,key):
        pass
    @abc.abstractmethod
    def set(self,key,value):
        pass

    
class RedisCache(CacheBase):
    def get(self,key):
        pass
    def set(self,key,value):
        pass

r = RedisCache()
