# 迭带器
from collections.abc import Iterator,Iterable

class Company():
    def __init__(self,employee_list):
        self.employee = employee_list

    def __iter__(self):
        # 返回一个iterator
        return MyIterator(self.employee)



class MyIterator():
    '''
    实现一个迭带器
    '''
    def __init__(self,list):
        self.iter_list = list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

if __name__ == '__main__':

    my = Company(["li","yyx","lxh"])
    my = iter(my)
    print(isinstance(my,Iterator))
    while True:
        try:
            print(next(my))
        except:
            break
    # for 其实拿到的就是一个Iterator
    # for x in my:
    #     print(x)
    '''
    Python中关于迭代有两个概念，第一个是Iterable，
    第二个是Iterator，协议规定Iterable的__iter__方法会返回一个Iterator, 
    Iterator的__next__方法（Python 2里是next）会返回下一个迭代对象，
    如果迭代结束则抛出StopIteration异常。同时，Iterator自己也是一种Iterable，
    所以也需要实现Iterable的接口，也就是__iter__，这样在for当中两者都可以使用。
    Iterator的__iter__只需要返回自己就行了。
    当for发现没有__iter__但是有__getitem__的时候，会从0开始依次读取相应的下标，
    直到发生IndexError为止，这是一种旧的迭代协议。
    '''


