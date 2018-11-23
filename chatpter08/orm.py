# 简易orm
# ORM的特点之一是「把表映射成类，把行作为实例，把字段作为属性」
class Field():
    pass


class IntField(Field):
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass


class StrField(Field):
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass


class ModelMetaClass(type):
    def __new__(cls, name,bases,attrs, **kwargs):
        # 定义保存属性的字典,用来保存数据表相关的列
        # 保存当前类属性名和Field字段的映射关系
        maps={}
        for k,v in attrs.items():
            # 是否是Field的子类
            if isinstance(v,Field):
                maps[k] = v
                print("11")
        if '__tablename__' in attrs.keys():
            table = attrs.get('__tablename__')
        else:
            table = name.lower()
        # 删除原来类中的属性，因为会和生成的实例属性重名
        for k in maps.keys():
            attrs.pop(k)
        attrs['table'] = table
        attrs['fields'] = maps

        return super().__new__(cls,name,bases,attrs, **kwargs)


class Model():
    def __init__(self,*args,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)



class User(Model):

    __tablename__= "user"
    name = StrField()
    age = IntField()



if __name__ == '__main__':
    #orm操作

    # u = User()
    u = User(name="li",age=20)
    print(u.__dict__)
    # u.save()