# python中垃圾回收的算法 是采用引用计数

a = 1
b = a

del a
print(b)